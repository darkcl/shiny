#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sqlite3

import click
from terminaltables import AsciiTable

# Database related

def list_info(names, path):
    """List information in progress database

    Args:
        names (list of str): Names of the pokemons
        path (str): Path of progress database
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    if len(names) == 0:
        result = cur.execute("""
            SELECT `PKM_NAME`, `ENCOUNTER`, `DONE` FROM counter;
        """)
    else:
        result = cur.execute("""
            SELECT `PKM_NAME`, `ENCOUNTER`, `DONE` FROM counter WHERE `PKM_NAME` IN ( %s );
        """  % ', '.join(map(lambda x: "'" + x + "'", names)))
    
    data = []
    data.append(['Pokemon', 'Encounter', 'Done'])
    for row in result:
        pkm_name = row[0]
        encounter = row[1]

        done = u'\u2714'
        not_done = u'\u274C'

        if row[2] == 0:
            data.append([pkm_name, encounter, not_done])
        else:
            data.append([pkm_name, encounter, done])
        
    
    table = AsciiTable(data)
    click.echo(table.table)

    conn.commit()
    conn.close()

def mark_done(name, path):
    """Mark Done in progress database

    Args:
        name (str): Name of the pokemon
        path (str): Path of progress database
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    result = cur.execute("""
        SELECT EXISTS (SELECT 1 FROM counter WHERE PKM_NAME=? LIMIT 1);
    """, (name, ))

    for row in result:
        if row[0] == 0:
            click.echo("%s not exist" % name)
        else:
            cur.execute("""
                UPDATE `counter` SET `DONE`= 1  WHERE `PKM_NAME`= ?;
            """, (name, ))
            click.echo("Complete hunt for %s" % name)
        break
    conn.commit()
    conn.close()

def add_counter(name, increase_by, path):
    """Add counter in progress database

    Args:
        name (str): Name of the pokemon
        increase_by (int): Adding count
        path (str): Path of progress database
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    result = cur.execute("""
        SELECT EXISTS (SELECT 1 FROM counter WHERE PKM_NAME=? LIMIT 1);
    """, (name, ))

    for row in result:
        if row[0] == 0:
            cur.execute("INSERT INTO `counter`(`ID`,`PKM_NAME`) VALUES (NULL, ?);", (name, ))
            cur.execute("""
                UPDATE `counter` SET `ENCOUNTER`= `ENCOUNTER` + %i  WHERE `PKM_NAME`= ?;
            """ % increase_by, (name, ))
        else:
            cur.execute("""
                UPDATE `counter` SET `ENCOUNTER`= `ENCOUNTER` + %i  WHERE `PKM_NAME`= ?;
            """ % increase_by, (name, ))
        break
    conn.commit()
    conn.close()

def create_hunt(name, path):
    """Create Hunt Record for progress database

    Args:
        name (str): Name of the pokemon
        path (str): Path of progress database
    """

    # Check If Record Exist
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    result = cur.execute("""
        SELECT EXISTS (SELECT 1 FROM counter WHERE PKM_NAME=? LIMIT 1);
    """, (name, ))

    for row in result:
        if row[0] == 0:
            cur.execute("INSERT INTO `counter`(`ID`,`PKM_NAME`) VALUES (NULL, ?);", (name, ))
            click.echo("Start hunting for %s" % name)
        else:
            click.echo("%s already exist" % name)
        break
    conn.commit()
    conn.close()


def initalize_database(path):
    """Initalize Progress Database. Create Table if needed

    Args:
        path (str): Path of progress database
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS `counter` (
        `ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
        `PKM_NAME`	TEXT NOT NULL,
        `ENCOUNTER`	INTEGER DEFAULT 0,
        `DONE`	INTEGER DEFAULT 0
    );
    """)
    conn.commit()
    conn.close()

# Click Staff

@click.group()
def cli():
    """Shiny Counter CLI
    """
    pass

@click.command()
@click.argument('names')
def hunt(names):
    """Start a hunt.
    """
    pkm_name = names.split()
    path = os.path.join(os.getcwd(), 'hunt.sqlite')
    initalize_database(path)
    for pkm in pkm_name:
        create_hunt(pkm, path)


@click.command()
@click.option('--add', default=1, help='Number of encounters')
@click.argument('names')
def count(add, names):
    """Add encounter to hunting target.
    """
    pkm_name = names.split()
    path = os.path.join(os.getcwd(), 'hunt.sqlite')
    initalize_database(path)
    for pkm in pkm_name:
        add_counter(pkm, add, path)
    list_info(pkm_name, path)

@click.command()
@click.argument('names')
def get(names):
    """Complete a hunt.
    """
    pkm_name = names.split()
    path = os.path.join(os.getcwd(), 'hunt.sqlite')
    initalize_database(path)
    for pkm in pkm_name:
        mark_done(pkm, path)

@click.command(name="list")
@click.option('--names', '-n', default="", help="Names of the pokemons")
def list_info_cli(names):
    """List shiny encounter.
    """
    pkm_name = names.split()
    path = os.path.join(os.getcwd(), 'hunt.sqlite')
    initalize_database(path)
    list_info(pkm_name, path)

cli.add_command(hunt)
cli.add_command(count)
cli.add_command(get)
cli.add_command(list_info_cli)

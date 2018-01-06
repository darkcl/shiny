import os
import sqlite3
import datetime
from terminaltables import AsciiTable

import click

# Text file related
def export_text_progress(name, path, text_path):
    """Export progress from progress database to text file

    Args:
        name (str): Name of the pokemon
        path (str): Path of progress database
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    result = cur.execute("""
        SELECT `ENCOUNTER` FROM counter WHERE `PKM_NAME` = ?;
    """, (name, ))

    for row in result:
        with open(text_path, "w") as text_file:
            text_file.write("{}".format(row[0]))
        break


    conn.commit()
    conn.close()

# Database related
class Pokemon(object):
    """Shiny tracking model class:

    Attributes:
        id: Index for the pokemon
        name: A string representing the pokemon's name.
        encounter: A integer tracking the current encounter.
        is_finished: A boolean representing the hunt is finished or not.
        finished_date: A string representing the date of hunt is finished. (optional)
    """
    def __init__(self, index, name, encounter, is_finished, finished_date):
        """Return a Pokemon tracker object.
        """
        self.index = index
        self.name = name
        self.encounter = encounter
        self.is_finished = is_finished
        self.finished_date = finished_date
    
    def dict_representation(self):
        """Return a Pokemon tracker dictionary.
        """
        result = {
            "id": self.index,
            "name": self.name,
            "count": self.encounter,
            "is_finished": self.is_finished
        }

        if len(self.finished_date) != 0:
            result["finished_date"] = self.finished_date
        return result


def list_info_model(path, identity=''):
    """List information as model in progress database

    Args:
        identity : Index of the pokemons
        path (str): Path of progress database
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    if len(identity) == 0:
        result = cur.execute("""
            SELECT `ID`, `PKM_NAME`, `ENCOUNTER`, `DONE` FROM counter;
        """)
    else:
        result = cur.execute("""
            SELECT `ID`, `PKM_NAME`, `ENCOUNTER`, `DONE` FROM counter WHERE `ID` = ?;
        """, (identity,))
    
    data = []
    for row in result:
        index = row[0]
        pkm_name = row[1]
        encounter = row[2]
        done = row[3]

        if done == '0':
            progress = Pokemon(index, pkm_name, encounter, False, '')
            data.append(progress.dict_representation())
        else:
            progress = Pokemon(index, pkm_name, encounter, True, done)
            data.append(progress.dict_representation())

    conn.commit()
    conn.close()
    result = data if len(identity) == 0 else data[0]
    return result

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

        # done = u'\u2714'
        done = row[2]
        not_done = 'In Progress'

        if row[2] == '0':
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
                UPDATE `counter` SET `DONE`= ?  WHERE `PKM_NAME`= ?;
            """, (datetime.datetime.now().strftime("%I:%M %p on %B %d, %Y"), name, ))
            click.echo("Complete hunt for %s" % name)
        break
    conn.commit()
    conn.close()

def add_counter_id(index, path, increase_by=1):
    """Add counter in progress database

    Args:
        index (str): ID of the pokemon
        increase_by (int): Adding count
        path (str): Path of progress database
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute("""
        UPDATE `counter` SET `ENCOUNTER`= `ENCOUNTER` + %i  WHERE `ID`= ?;
    """ % increase_by, (index, ))
    
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
        `DONE`	TEXT DEFAULT 0
    );
    """)
    conn.commit()
    conn.close()
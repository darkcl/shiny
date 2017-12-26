import click
import os
import sqlite3

# Database related

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
    """Main Function
    """
    pass

@click.command()
@click.argument('names')
def hunt(names):
    """Start a hunt.

    Args:
        names (str): Name(s) of the pokemon. Space as separtor.

    """
    pkm_name = names.split()
    path = os.path.join(os.getcwd(), 'hunt.sqlite')

    click.echo('Start Hunting %s' % ", ".join(pkm_name))
    initalize_database(path)

    for pkm in pkm_name:
        create_hunt(pkm, path)


@click.command()
@click.argument('names')
def count(names):
    """Add encounter to hunting target.

    Args:
        names (str): Name(s) of the pokemon. Space as separtor.

    """
    click.echo('Add encounter to counter')

@click.command()
@click.argument('names')
def get(names):
    """Complete a hunt.

    Args:
        names (str): Name(s) of the pokemon. Space as separtor.

    """
    click.echo('Complete hunt for ')

cli.add_command(hunt)
cli.add_command(count)
cli.add_command(get)

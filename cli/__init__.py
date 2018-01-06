#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import click

from core import initalize_database, list_info, create_hunt, export_text_progress, mark_done, add_counter
from web import start_web

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
        text_path = os.path.join(os.getcwd(), "{}.txt".format(pkm))
        export_text_progress(pkm, path, text_path)
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

@click.command(name="serve")
def create_web_server():
    """Start Web Server.
    """
    app = start_web()
    app.run()

cli.add_command(hunt)
cli.add_command(count)
cli.add_command(get)
cli.add_command(list_info_cli)
cli.add_command(create_web_server)

if __name__ == '__main__':
    cli()

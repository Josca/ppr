import click
from . import ppr


@click.command(help='Generate new Python project.')
@click.argument('projectname', nargs=1)
def cmd_ppr(projectname):
    ppr.make_project(projectname)

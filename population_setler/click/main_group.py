import click
from rich import print as rich_print

@click.group()
def main():
    rich_print('''[i]This script is used to balance & divide population of given territory into houses[/i]''')

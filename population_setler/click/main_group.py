import click
from rich import print as rich_print

@click.group()
def main():
    rich_print('''[bold cyan]This script is used to balance & divide population of given territory into houses[/bold cyan] todo descr''')

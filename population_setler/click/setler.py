import click
from .main_group import main

@main.command("set")
@click.option(
        "--id",
        "-i",
        type=int,
        help="IdTODO",
        required=True,
)
#click.option(people_pyramid)
#click.option(territories)
#click.option(--output -o)
#click.option(--year -y)
def set(id : int,) -> None:
    print(id)
    #setler(....)
    pass

import click
from .main_group import main
from ..models import PeopleDivision #todo fix import

@main.command("set")
@click.option(
        "--id",
        "-i",
        type=int,
        help="IdTODO",
        required=True,
)
#click.option(people_pyramid) or count population and default one
#click.option(territories)
#click.option(--output -o)
#click.option(--year -y)
#click.option(--debug -d)
def set(id : int,) -> None:
    print(id)
    test = PeopleDivision()
    print(test.men.count['0-0'])
    pass

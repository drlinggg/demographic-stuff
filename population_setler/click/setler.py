import click
from .main_group import main
from population_setler.models import PeopleDivision, Territory, House 


#todo
#click.option(people_pyramid) or count population and default one
#click.option(territories)
#click.option(--output -o)
#click.option(--year -y)
#click.option(--debug -d)
@main.command("set")
@click.option(
        "--id",
        "-i",
        type=int,
        help="IdTODO",
        required=True,
)
def set(id : int,) -> None:
    """todo add desrc"""
    print(id)

    #test begin
    test = PeopleDivision()
    print("ages | count")
    for x,y in test.men.count.items():
        print(x,y)
    test1 = Territory("Шахты")
    test1.houses.append(House())
    print(test1.houses)
    #test end

    pass

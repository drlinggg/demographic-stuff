import click
from .main_group import main
from population_setler.models import PeopleDivision, Territory, House #todo deleteaftertest
from population_setler.balancer import Balancer


#todo
#click.option(people_pyramid) or count population and default one (mb should be inside of territories)
#click.option(territories) mb with geometry
#click.option(houses?)
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
    test.men.count["1-1"] = 532
    #print("ages | count")
    #for x,y in test.men.count.items():
    #    print(x,y)
    test1 = Territory("Шахты", test)
    test1.houses.append(House(1,1,1))
    print(f'living area: {test1.get_living_area()}')
    print(f'total population: {test1.get_total_population()}')
    print(f'self population: {test1.get_self_population()}')
    print(f'houses: {test1.get_houses()}')
    test2 = Balancer()
    print(test2._check_population_difference(test1))
    print(test2.balance_territories(test1))
    #test end
    pass

#mbtodo command("balance"), command("divide") or keep it inside of setler idk

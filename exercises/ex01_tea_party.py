"""This program uses a 'main planner' function that takes the input 
of the number of guests and computes the number of tea bags, treats, 
and the cost needed to fund the tea bags and treats"""

__author__: str = "730771648"


def main_planner(guests: int) -> None:
    """brings all the functions together that calls each and prints"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    return None


def tea_bags(people: int) -> int:
    """tea_bags function that calculates two tea bags per person"""
    return people * 2


def treats(people: int) -> int:
    """calculates for each tea a person drinks, they want on average 1.5 treats for it"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the total cost of tea bags and treats with each tea bag costing $.50 and each treat costing $.75"""
    return float(tea_count * 0.5 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

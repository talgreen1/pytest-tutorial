from sushi import *

# https://hackebrot.github.io/pytest-tricks/mark_parametrize_with_indirect/

rest = Restaurant("Segev", "Rishon", "Menu")

sushi = Sushi("Inside out", ["egg", "Crab"])
print(str(sushi.is_vegetarian()))


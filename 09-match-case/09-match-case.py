# Structural Pattern Matching
# match subject:
#     case <pattern_1>:
#         <action_1>
#     case <pattern_2>:
#         <action_2>
#     case _:
#         <action_wildcard>
#################################################
def httperror(status):
    match status:
        case 400: 
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case _:
            return "Somthing's wrong with the internet"

print(httperror(406))
print(httperror(400))

#################################################
# point is an (x, y) tuple
x = 9
y = 10
point = (x, y)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

#################################################
from enum import Enum
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

color = Color.RED

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    case _:
        print("Not Color")
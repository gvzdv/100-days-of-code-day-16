# from turtle import Turtle, Screen
#
# # Create a new object using the turtle module and Turtle class
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("pink")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)





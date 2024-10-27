# import turtle
# timmy = turtle.Turtle()
#powyższe = poniższe
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse")
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable() #tworzy obiekt
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"]) #wywołanie metody-funkcji
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l" #ustawienie atrybutu
print(table)

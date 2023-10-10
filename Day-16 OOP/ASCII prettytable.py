#import prettytable class
from prettytable import PrettyTable

#create object
table = PrettyTable()
x = PrettyTable()

#use and syntax of accessing methods

#creating table using add_column (methods)
x.add_column("Pokemon Name",
             ["Pikachu", "Squirtle", "Charmander"])
x.add_column("Type",
             ["Electric", "Water", "Fire"])

#creating table using field_names and add_rows (methods)
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(x)

#use and syntax of accessing attribute
table.align = "l"  # table left alignment

print(table)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["A", "B", "C", "D", "E"])
table.add_column("Score", [12, 23, 15, 24, 'NA'])
table.add_column("Grade", ['F', 'A', 'B', 'A', 'NA'])

table.align = 'l'
print(table)

from prettytable import PrettyTable

#write header
mytable = PrettyTable(["Student name", "Class", "Section", "Percentage"])

#Add rows
mytable.add_row(['Leanord', 'X', 'B', "91.2%"])
mytable.add_row(['Penny', 'X', 'C', '63.5%'])
mytable.add_row(['Howard', 'X', 'A', '90.23%'])
mytable.add_row(['Bernadette', 'X', 'D', '92.7%'])
mytable.add_row(['Sheldon', 'X', 'A', '98.2%'])
mytable.add_row(['Raj', 'X', 'B', '88.1%'])
mytable.add_row(['Amy', 'X', 'B', '95.2%'])

#Output
print(mytable)
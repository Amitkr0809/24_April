import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())



y = re.search("\S",txt)
print("The first capital character is located in position:", y.start())

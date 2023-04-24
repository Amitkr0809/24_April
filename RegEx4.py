import re
txt = "i work for thunder soft india "
x = re.split("\s",txt)
print(x)

y = re.split("\s", txt, 2)
print(y)
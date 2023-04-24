import re

txt = "i work for thunder soft india"
x = re.search("or", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
import re
txt = "i work for Thunder soft india"

x = re.sub("\s", "_", txt)
print(x)

y = re.sub("\s","-",txt)
print(y)
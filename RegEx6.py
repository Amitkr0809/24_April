import re

txt = "hello python"

x = re.findall("^hello", txt)

if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

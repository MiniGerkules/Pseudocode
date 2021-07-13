import re

code = '33453453'
pattern = '334'
obj = re.match(pattern, code)
print(obj.group())

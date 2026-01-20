import re

r = re.compile(r"\+")

match = r.search("+")

print()
print(match)

search = r.search("the abc book, abbbbc!")

print(search)

findall = r.findall("the abc book, abbbbbc!")

print(findall)
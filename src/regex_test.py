import re

r = re.compile(r"(//|#)[^\n]*")

match = r.search("bruv # jotain mitä vaan ahahha fsdij \n" )

print()
print(match)

search = r.search("the abc book, abbbbc!")

print(search)

findall = r.findall("the abc book, abbbbbc!")

print(findall)
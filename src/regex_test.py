import re

r = re.compile(r"(//|#)[^\n]*")
l = re.compile(r"\n")

match = l.search("bruv # jotain mitä\n vaan ahahha fsdij \n" )

print(match)

search = r.search("the abc book, abbbbc!")


findall = r.findall("the abc book, abbbbbc!")

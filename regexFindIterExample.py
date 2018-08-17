import re
str = "AccessItem:tickets intent:delivery time come Facility:White hart lane Facility:home match intent:collect"    

pattern = r'(\w+:\w+(\s\w*\s)*)'
regex = re.compile(pattern, re.IGNORECASE)
for match in regex.finditer(str):
    print "%s,%s: %s" % (match.start(), match.end(),match.group(1))
    

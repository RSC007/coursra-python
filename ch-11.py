import re
handle = open('test.txt')
count = re.findall('[0-9]+', handle.read())
print(sum([ int(x) for x in count]))

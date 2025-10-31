import random

s = ''.join(random.choices(['<', '>', '/', 'b', 'B'], k=50))
print(s)
s = s.replace('<b>', '<BOLD>').replace('<B>', '<BOLD>').replace('</b>', '<AND BOLD>').replace('</B>', '<AND BOLD>')
print(s)

import re

zdanie = 'To be, or not to be, that is the question'
samogloski = re.findall('[aeyuio]',zdanie)
print(len(samogloski))
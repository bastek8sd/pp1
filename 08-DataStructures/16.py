
from Stack import Queue

kolejka = Queue()
for x in range(5):
    kolejka.push(x)

for x in range(3):
    print(kolejka.pop())
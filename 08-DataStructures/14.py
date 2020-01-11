from Stack import Stack

stos = Stack()
for x in range(5):
    stos.push(x)

for x in range(3):
    print(stos.pop())
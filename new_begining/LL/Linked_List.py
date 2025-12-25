class node:
    def __init__(self, data):
        self.data = data
        self.next = None



samin = node(5)
tahmin = node(10)
samin.next = tahmin
safin = node(15)
tahmin.next = safin
print(samin.next.next.next)

while samin is not None:
    print(samin.data)
    samin = samin.next


arr = [5,10,15]
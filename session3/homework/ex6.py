items=[5,7,300,90,24,50,75]
print("Hello my name is Linh and these are my sheep sizes")
print([*items], sep=',')
i = max(items)
print("now my biggest sheep has size",i,"let's shear it")
items[2]=8
print("after shearing, here is my flock")
print(items)
for i in range(len(items)):
    items[i] += 50
print("One month has passed ,now here is my flock")
print([*items], sep=',')
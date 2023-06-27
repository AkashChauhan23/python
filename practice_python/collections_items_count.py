from collections import Counter

inventery = Counter()
data = {
    "Akash" : 18,
    "Varsha" : 20,
}
inventery.update(data)
print(inventery)

data = {
    "Akash" : 28,
    "Varsha" : 20,
    "Shalu" : 12
}
inventery.update(data)

print(inventery)
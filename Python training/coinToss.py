import random
limit = int(input("Number of times to flip coin: "))
sampleSpace = []
for i in range(limit):
    flip = random.randint(0, 1)
    if flip == 0:
        print("Heads")
        sampleSpace.append("H")
    else:
        print("Tails")
        sampleSpace.append("T")
print(str(sampleSpace))
print("Heads:", (sampleSpace.count("H")), "Tails:", sampleSpace.count("T"))
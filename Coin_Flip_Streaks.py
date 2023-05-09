import random
numberOfStreaks = 0
result = []
headsCounter = 0
tailsCounter = 0
for experimentNumber in range(10000):
    # Code that creates a list of 10000 'heads' or 'tails' values.
    headsOrTails = random.randint(0, 1)
    result.append(headsOrTails)
    if headsOrTails == 0:
        headsCounter += 1
        tailsCounter = 0
        if headsCounter == 6:
            numberOfStreaks += 1
    else:
        tailsCounter += 1
        headsCounter = 0
        if tailsCounter == 6:
            numberOfStreaks += 1
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

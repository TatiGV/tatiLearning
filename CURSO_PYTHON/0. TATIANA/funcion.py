import random

def isHit(number):

    if number > 15:
        return True
    else:
        return False

def dice():
    return random.randint(1, 6)

result = dice() + 10


result = result + dice()



    

hit = isHit(result)

print(hit)


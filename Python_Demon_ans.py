import random
n=(input("Enter your name"))
a=int(input("Enter the lower limit"))
b=int(input("Enter the upper limit"))
po=100
rn = random.randint(a, b)
gu=int(input("Input your guess"))
while (gu!=rn)and(po>5):
    if gu>rn:
        print("Too high")
        po=po-5
    elif gu<rn:
        print("Too low")
        po=po-5
    gu=int(input("Input your guess"))
if(po<5):
    print("You failed")
else:
    print(n,", your guess is right!\nYou got",po,"points")


import random

dict = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

print(dict)
comp = random.choice([1,2,3])
c = 0
ch = int(input("Enter your choice: "))
print("You chose: ",dict[ch])
print("computer chose: ",dict[comp])

if(ch < 4):
    if(ch == comp):
        print("draw")
    else:
        if(ch == 1 and comp == 2):
            print("You lose! ")
        elif(ch == 1 and comp == 3):
            print("You Win!")
        elif(ch == 2 and comp == 1):
            print("You Win! ")
        elif(ch == 2 and comp == 3):
            print("You lose!")
        elif(ch == 3 and comp == 1):
            print("You lose! ")
        elif(ch == 3 and comp == 2):
            print("You Win! ")               
else:
    print("Choose the correct option: ")

        



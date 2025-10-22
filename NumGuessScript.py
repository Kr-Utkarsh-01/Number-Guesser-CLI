import random
def game(chances):
    res=random.randint(0,100)
    for i in range(1,chances+1):
        print(f"Chances remaining: {chances-i+1}")
        n=int(input("Enter your guess: "))
        if n==res:
            print(f"Congratulations! You have sucessfully guessed the number. You took {i} tries.")
            return
        elif(n<res):
            print(f"The number is greater than {n}")
        elif(n>res):
            print(f"The number is less than {n}")
    print(f"You FAILED. The number was {res}")
isTrue="Y"
while isTrue.upper()=="Y" or isTrue.upper()=="YES":
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have limited chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")
    choice=int(input("Enter your difficulty choice: "))
    if choice==1:
        print("Great! You have selected the Easy difficulty level.")     
        game(10)
    elif choice==2:
        print("Great! You have selected the Medium difficulty level.")
        game(5)

    elif choice==3:
        print("Great! You have selected the Hard difficulty level.")        
        game(3)
    else:
        print("Invalid choice.")
    isTrue=input("Would you like to play again (y/n)")
print("Thank you for playing.")
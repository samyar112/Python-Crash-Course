FAVORITE_NUMBER = 8

def favorite():
    while True: 
        try: 
         guess = int(input("What's my favorite number from 1 to 10? "))
         if guess == FAVORITE_NUMBER:
                print("Correct! My mayalu so smart. Well Done. Now dame sugaaaaaa")
                break
         else: 
             print("Not Correct. Try Again")
        except ValueError:
            print("Invalid input. Please enter a number between 1 to 10")

favorite()



import random
print("The Guess Game!")
playing = input("Do you want to play the Guess game : ")
if playing.lower() != "yes":
    print("Bye BYE")
    quit()
print("If you want to close the game just press space and enter")
tries = 6
score = 0
rand_num = random.randint(0,100)
the_game = True
while the_game:  
    guess = input("Guess The Number : ")
    try:
        guess = int(guess)
    except:
        print("Please enter a number!")
        quit()
    if guess == rand_num:
        print("that's correct Well done")
        score += 1
        tries = 6
        rand_num = random.randint(0,100)
    elif guess < rand_num:
        print("two low!")
        tries -= 1
        print("Tries: ",tries)
    elif guess > rand_num:
        print("Too High!")
        tries -= 1
        print("Tries: ",tries)
    if tries == 0 :
        print("\n you lost ")
        print('The Random Number was : ', rand_num)
        the_game = False

#init
import random
import time
magic_list = ["I guess we'll never know","It's very likely","Maybe one day...", "Absolutely"," I wouldn't count on it", "Time will tell", "Ask again", "The odds are in your favor", "No.", "Of course!", "Well, go with your gut", "For sure!", "Not sure, but maybe?", "Its very likely" , "Probably"]
#Functions
print("Welcome to your digital magic 8 ball!")

def eight_ball():
    while True:
        try:
            question = input("Enter a yes or no question and see what the universe has in store...please add question mark!") #introduces player to the game
            x = question.endswith("?") #checks if player added a question mark
            if x == True:# if input in yes, they did and response can be given
                print("shaking in progress!!!!")# adds delay and effect to the code for funsies
                time.sleep(3)
                print(random.choice(magic_list)) #gives a random response
                replay = input("Do you want to answer another question?") #asks for another question
                if replay == "Yes"or replay == "y": #if answer is yes they will get another question
                    eight_ball()
                if replay == "No" or replay == "n": #if answer is no they will not get another question
                   print("thanks for playing!") #breaks the code!
                   break
            if x == False:
                print("please retype your question with mark on the end") # if there is no question mark they will have to reanswer
        except:
            print("ERROR: Please enter a string of words..")

eight_ball()# calls the code

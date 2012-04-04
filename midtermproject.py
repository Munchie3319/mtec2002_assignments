from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def ghost_room():
    print "There is a 2 ghost in there."
    print "Which ghost do you prefer to go with."
    print "Red Ghost?"
    print "White Ghost?"
    

    while True:
        next = raw_input("> ")

        if next == "Red":
            dead("You are haunted by the Red Ghost.")
            exit(0)
        elif next == "White":
            print "You are saved, this is actually a person with Vitiligo"
            exit(0)
        else:
            print "I got no idea what that means."
            
def dog_room():
    print "There two type of dogs."
    print "Which one do you want to bring home with you?"
    print "Rottweiller?"
    print "Doberman?"
    

    while True:
        next = raw_input("> ")

        if next == "Rottweiller":
            loyal("She was be loyal and protect you.")
            exit(0)
        elif next == "Doberman":
            print "He goes crazy and bites your head off, you are dead!"
            exit(0)
        else:
            print "I got no idea what that means."
            
def poop_room():
    print "There are two handles."
    print "Which one do you pull?"
    print "Blue?"
    print "White?"
    

    while True:
        next = raw_input("> ")

        if next == "Blue":
            loyal("You get a nice new shirt")
            exit(0)
        elif next == "White":
            print "A whole pile of poop falls on your head!"
            exit(0)
        else:
            print "I got no idea what that means."



def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in the middle of a dark room."
    print "There are 5 doors."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "1":
        bear_room()
    elif next == "2":
        cthulhu_room()
    elif next == "3":
    	ghost_room()
    elif next == "4":
    	dog_room()
    elif next == "5":
    	poop_room()
    else:
        dead("You stumble around the room until you starve.")


start()
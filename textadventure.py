# Text AD

import random
import time


def bad():
    print("Despite your best efforts, it does not seem to do anything \n try keywords: 'get' 'use' 'look'")


inv = []

clothes = 1

sack = 1

door1 = 1

def add(self):
    inv.append(self)
    print('Added %s to inventory!' % self)


def use(thing, thing2):
    print("You used %s on %s" % (thing, thing2))


# start of adventure
print('SKYREACH')

time.sleep(2)

print("You open your eyes to find yourself in a dark room. You are wearing nothing but your undergarments, lying down on something soft. \nYour bed. \nThe only sensory detail you have is a small red light, blinking a few feet away")
time.sleep(.25)

state = int(1)

while state == 1:
    action1 = str.lower(input("What do you do? : "))

    time.sleep(.25)

    if action1 in ['look light']:
        print("You try focusing your eyes on the light. as you stare at it your eyes slowly adjust to the darkness.")
        print("you are able to see the faint outline of a button, the source of the blinking!")

    elif action1 in ['get up', 'stand', 'stand up']:
        print("You make an effort to stand up from the bed. Your head swims with pain from the movement but you manage. The room is still dark")
        state += 1
        continue

    elif action1 in ['touch light', 'grab light', 'get light', 'use button']:
        print("You cannot seem to reach the light from your current, lying down position.")
    else:
                   bad()

while state == 2:
    action2 = str(input("what do you do? :"))
    if action2 in ['touch light', 'grab light', 'feel light', 'push button', 'use button']:
        print('You reach towards the light and brush it with your hand. The room becomes flooded with light and your eyes burn with pain from the sudden brightness')
        state += 1
        continue
    elif action2 in ['look light', 'look button']:
        print("You try focusing your eyes on the light. as you stare at it your eyes slowly adjust to the darkness.")
        print("you are able to see the faint outline of a button")

    else:
        print("It is still dark.")
        bad()

while state ==3:
    action3 = str(input("After a few moments of pain with tightly clenched eyes and... other things, you adjust to the light level of the room. \n What do you do? :"))
    if action3 in ['look room', 'look around']:
        print("The room you stand in has a very clinical look to it. The walls are made of a shiny while material that reflects everything in a fuzzy way. \n The room has a too small bed in the back, a metal shelf, and a metal door. Next to the door is a rectangle. It's pretty nice as rectangles go.")
        state += 1
        continue
    else:
        bad()


while state == 4:
    action4 = str(input("What do you do? :"))
    if action4 in ['look shelf']:
        print("the shelf is made of nice material, solid steel. It is decorated with stripes of copper horizontally along the sides. \n The shelf has a bundle of clothes on it and an equipment sack. It also has numerous small little bobbleheads. You fancy yourself quite the collector")
    elif action4 in ['get sack', 'get equipment sack'] and sack == 1:
        print("You picked up the bag! inside of it is...... a whole granola bar!")
        time.sleep(1)
        print("wait, it has raisins..... gross")
        add('grossnola bar')
        time.sleep(2)
        print("you also find an ID card, it displays a picture of you, wearing an orange and black getup and has your name printed on it: 'Nash Kar'")
        time.sleep(1)
        add('ID card')
        time.sleep(.25)
        print('There is nothing else in the sack. You take it, slinging it over your back.')
        sack += 1
    elif action4 in ['get clothes']:
        print("you put on the clothes. The pants are a dark black material with a yellow strip across the knee of your left leg and the thigh of your right leg. \n the jacket is light blue with white indestinct symbols littered across the back.")
        clothes += 1
    elif action4 in ['inventory']:
        print(inv)
    elif action4 in ['look rectangle']:
        print("The rectangle appears to be a keypad for the door. it reads 'Locked'")
    elif action4 in ['look door', 'open door', 'touch door']:
        print("the door is of a sleek metallic substance, when you run your hand down it, it feels almost like ceramics. Yet it has the clang of metal when \n you knock on it. \n there is no door knob to speak of")
    elif "ID card" in inv and action4 in ['use id card on keypad', 'use id card on door', 'use id card on rectangle'] and door1 == 1:
        use('ID card', 'Keypad')
        print('The keypad lets out a short and satisfying beep and the frame of the door blinks a warm green glow as \n the metallic door slides open.')
        time.sleep(1)
        door1 += 1
    elif action4 in ['use door', 'go door', 'go through door'] and door1 == 2:
        print('You step through the doorway into a low ceiling, but wide room.')
        if clothes == 1:
            print("The ceramic-metallic floor feels cool on your bare feet as you walk through the doorway. \nYou probably should have put some clothes on")
            time.sleep(3)
            print("The room is the cockpit of your space vessel: 'The Roach' \nYou named it after the steed of a famous Polish folk Hero buy the name of 'Gerald'... or something like that.")
        state += 1
    else:
        bad()

while state == 5:
    action5 = str(input("What do you do? :"))
    if action5 in ['look cockpit', 'look room']:
        print("there is a lone chair at the center of the room. It's not your grandmother's chair. \nMade of more of the ceramic-metal, coated with a matte blue and lined with fluffy blue and white strippes, \n this was your helm, your throne... that you happend to inherit from your grandmother.... \n so i suppose it is your grandmother' chair")
        time.sleep(.4)
        print("The left and right sides of the room are piled with boxes and jugs, your food supply. there are no other doors,")
        time.sleep(.4)
        print("but on the floor there is a hatch labeled 'cargo.' which is where you store the packages you ship.")
        time.sleep(.4)
        print("Space trucking isn't an easy job, but it pays hilariously well and most people are scared out of their minds of flying. \nLucky for you, you are not most people. \n Unlucky for you, you are lost. \n after having drifted off course, while you were in your room organizing your bobbleheads,")
        time.sleep(.4)
        print("you found your ship lost in this system. Deciding it would be a good idea to deal with it after some sleep, \n you went to bed. That was probably a few hours ago.")
    elif action5 in ["use hatch"]:
        print('You reach for the hatch but remember that the contract of your delivery specified you were not to look at the cargo. \n Which is fine.... but REALLY tantilizing. You want to peek more than an invisible boy in a womens locker room.')
        time.sleep(3)
        print('unfortunatly, much like the proverbial invisible boy, you probably would see more than you were mentally prepared for. So you decide not to peek... not yet anyway.')
    elif action5 in ['inventory']:
        print(inv)
    else:
        bad()


chair == 0

hail == 0

while state == 6:
    action6 = str(input("What do you do? :"))
    if action6 in ['use chair'] and chair == 0:
        print("You sit in the chair with a sigh of delight, which fades when you look at the console in front of you.")
        chair += 1
    elif action6 in ['stand', 'stand up'] and chair == 1:
        print("You stand up out of the chair.")
        chair -= 1
    elif chair == 1 and action6 in ['look console']:
        print("The console has dozens of blinking lights. It'f familiar, and you notice that the radar shows an unknown vessel 15km away. \nIt seemed to have left a message for you while you slept. How nice of them.")
        print("Their message Reads 'Citizen, We are well aware of what you are shipping. \nIt is in your best interest that you release your cargo hold immediatly and allow us to take what you are carrying.'")
        print("You get the feeling that you .")
    elif chair == 0 and action6 in ['look console', 'look message']:
        print("You cant see the console, the chair is in your way")
    elif action6 in ['inventory']:
        print(inv)
    else:
        bad()
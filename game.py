import random, music, time, led
from re import A


NumberToGuess = random.randint(0,100)

answer = -1

print("You guess it")

def game():
    music.play('start')
    while(answer != NumberToGuess and answer != -1):
        if answer > NumberToGuess :
            answer = -1
            music.play('loose')
            led.blink_r()
            print("Number is lower : ")
            while(answer==-1):
                time.sleep(0,5)
        elif answer < NumberToGuess and answer != -1:
            answer = -1
            music.play('loose')
            led.blink_r()
            print("Number is higher : ")
            while(answer==-1):
                time.sleep(0,5)
        else:
            print("not a good value")
    print("You guess it")
    music.play('win')
    led.blink_multicolor()
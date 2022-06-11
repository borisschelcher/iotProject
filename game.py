import music, time, led

def game(answer , NumberToGuess ):
    while(answer != NumberToGuess and answer != 0):
        if answer > NumberToGuess :
            led.blink_b()
            print("Number is lower : ")
            music.play('Loose')
            return 0
        elif answer < NumberToGuess:
            led.blink_r()
            print("Number is higher : ")
            music.play('Loose')
            return 0
        elif answer == NumberToGuess:
            print("You guess it")
            led.blink_multicolor()
            return 1
        else:
            print("not a good value")
            return 0

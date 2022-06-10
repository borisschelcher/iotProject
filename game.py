import music, time, led

def game(answer , NumberToGuess ):
    while(answer != NumberToGuess and answer != 0):
        if answer > NumberToGuess :
            led.blink_r()
            print("Number is lower : ")
            return 0
        elif answer < NumberToGuess:
            led.blink_r()
            print("Number is higher : ")
            return 0
        elif answer == NumberToGuess:
            print("You guess it")
            led.blink_multicolor()            
        else:
            print("not a good value")
            return 0

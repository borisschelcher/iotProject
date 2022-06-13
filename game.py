import music, time, led

def game(answer , NumberToGuess ):
    while(answer != NumberToGuess and answer != 0):
        if answer > NumberToGuess :
            led.blink_r()
            print("Number is lower, try again >> ")
            return 0
        elif answer < NumberToGuess:
            led.blink_b()
            print("Number is higher, try again >> ")
            return 0
        else:
            led.blink_r()
            print("The value is incorrect")
            return 0
    print("You guessed it !")
    led.blink_multicolor()
    return 1

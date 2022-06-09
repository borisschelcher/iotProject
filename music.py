import variable
from machine import Pin, PWM
from utime import sleep
buzzer = PWM(variable.BUZZER_PIN)




def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(variable.Tones[mysong[i]])
        sleep(0.3)
    bequiet()

def play(songType):
    if songType == 'Win':
        playsong(variable.WinSong)
    elif songType == 'Loose':
        playsong(variable.LooseSong)
    elif songType == 'Start':
        playsong(variable.StartSong)
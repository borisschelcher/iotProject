import variable
import time

led_r = variable.LED_R_PIN
led_g = variable.LED_G_PIN
led_b = variable.LED_B_PIN

def reset():
    led_b.value(0)
    led_r.value(0)
    led_g.value(0)


def blink_r():
    reset()
    led_r.value(1)
    time.sleep(0.5)
    led_r.value(0)
    time.sleep(0.5)
    
def blink_g():
    reset()
    led_g.value(1)
    time.sleep(0.5)
    led_g.value(0)
    time.sleep(0.5)
    
def blink_b():
    reset()
    led_b.value(1)
    time.sleep(0.5)
    led_b.value(0)
    time.sleep(0.5)

def blink_multicolor():
        blink_r()
        blink_b()
        blink_r()
    
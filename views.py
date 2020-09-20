import time
import pynput.mouse as ms
import random

x=random.randint(3,15)#change this to reload page faster or add more randomness
def click():
    mouse = ms.Controller()
    mouse.position = (122, 47)#where the refresh button is , if you don't know check out get mouse co-ords
    mouse.press(ms.Button.left)
    time.sleep(x)
    mouse.release(ms.Button.left)




for i in range(1,1001):#however many times you want to refresh
    click()
    time.sleep(x)
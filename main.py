import pyautogui, keyboard, time
from tkinter import *
app = Tk()
app.title("Autoclicker")
def startAutoClicking():
    running = True
    time.sleep(1)
    while running == True:
        if keyboard.is_pressed("B"):
            running = False
            break
        pyautogui.leftClick(pyautogui.position())
Label(app, text="Note: Press 'B' to stop clicking.").pack()
left_button = Button(app, text="Left Click", command=startAutoClicking).pack()
app.mainloop()

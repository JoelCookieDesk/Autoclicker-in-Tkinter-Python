import pyautogui, keyboard, time
from tkinter import *
app = Tk()
app.title("Autoclicker")
def leftClicking():
    leftClickRunning = True
    time.sleep(1)
    while leftClickRunning == True:
        if keyboard.is_pressed("L"):
            leftClickRunning = False
            break
        pyautogui.leftClick(pyautogui.position())
def rightClicking():
    rightClickRunning = True
    time.sleep(1)
    while rightClickRunning == True:
        if keyboard.is_pressed("R"):
            rightClickRunning = False
            break
        pyautogui.rightClick(pyautogui.position())
Label(app, text="Note: Press 'l' to stop left clicking and 'r' to stop right clicking.").pack()
left_button = Button(app, text="Left Click", command=leftClicking)
left_button.grid(row=1, column=0)
right_button = Button(app, text="Right Click", command=rightClicking)
right_button.grid(row=0, column=1)
app.mainloop()
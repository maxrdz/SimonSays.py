from graphics import *  # Importing graphics.py library and functions
from random import *  # Imports random library from Python
import winsound  # Imports Windows Sound library to make beeps, only on windows computer.


colorsDict = {"R": color_rgb(255, 0, 0), "Y": color_rgb(255, 255, 0), "G": color_rgb(0, 255, 0), "B": color_rgb(0, 0, 255)}

class button:

    def __init__(self, name, color, coord_x, coord_y, radius, init_on, beep_freq, window):
        self.name = name
        self.window = window
        self.circle = Circle(Point(coord_x, coord_y), radius)
        self.on = init_on
        self.color = color
        self.beep_freq = beep_freq
        if self.on:
            self.circle.setFill(color)
        else:
            self.circle.setFill(color_rgb(0, 0, 0))
        self.circle.setOutline(color_rgb(255, 255, 255))
        self.circle.setWidth(3)
        self.circle.draw(self.window)

    def turn_on(self):
        self.circle.setFill(self.color)
        self.on = True

    def turn_off(self):
        self.circle.setFill(color_rgb(0, 0, 0))
        self.on = False

    def blink(self, beep_interval, wait_interval):
        if self.on:
            self.turn_off()
            winsound.Beep(self.beep_freq, beep_interval)
            self.turn_on()
            time.sleep(wait_interval)
        else:
            self.turn_on()
            winsound.Beep(self.beep_freq, beep_interval)
            self.turn_off()
            time.sleep(wait_interval)

def main():
    win = GraphWin("Simon Says", 970, 600)
    win.setBackground('Black')

    redButton = button("R", colorsDict.get("R",0), 250, 200, 50, False, 1000, win)
    yellowButton = button("Y", colorsDict.get("Y", 0), 400, 200, 50, False, 1300, win)
    greenButton = button("G", colorsDict.get("G", 0), 550, 200, 50, False, 1500, win)
    blueButton = button("B", colorsDict.get("B", 0), 700, 200, 50, False, 2000, win)

    buttonDict = {redButton.name: redButton, yellowButton.name: yellowButton, greenButton.name: greenButton, blueButton.name: blueButton}

    counter = Text(Point(880, 75), "0")
    counter.setSize(30)
    counter.setTextColor("Black")

    counterBorder = Circle(Point(880, 75), 40)
    counterBorder.setFill("White")
    counterBorder.setOutline("Red")
    counterBorder.setWidth(2)
    counterBorder.draw(win)
    counter.draw(win)

    startTxt = Text(Point(480, 360), "Press Any Key To Start")
    startTxt.setSize(30)
    startTxt.setTextColor(color_rgb(255, 102, 102))
    startTxt.draw(win)

    # Wait for any key to start game      v  v

    win.getKey()
    startTxt.undraw()

    # Cycle Starts
    stack = []
    colors = ["R", "Y", "G", "B"]
    game_Over = False
    playbackInterval = .500
    currentStage = 4

    while not game_Over:
        counter.undraw()
        counter = Text(Point(880, 75), len(stack))
        counter.setSize(30)
        counter.setTextColor("Black")
        counter.draw(win)

        if (len(stack) == currentStage) and (playbackInterval != .50):
            currentStage += 3
            playbackInterval -= .150

        stack.append(colors[randint(0, 3)])

        for color in stack:
            buttonDict.get(color, None).blink(500, playbackInterval)

        instructions = Text(Point(480, 360), "'R' for Red, 'Y' for yellow, 'G' for Green, 'B' for blue.")
        instructions.setSize(25)
        instructions.setTextColor(color_rgb(255, 255, 255))
        instructions.draw(win)

        for count in stack:
            keyStroked = win.getKey()
            instructions.undraw()
            if keyStroked.upper() == count:
                buttonDict.get(count, None).blink(300, 0)
            else:
                game_Over = True
                break
        time.sleep(1)

    gameOver = Text(Point(480, 360), "GAME OVER")
    gameOver.setSize(30)
    gameOver.setTextColor(color_rgb(255, 0, 0))
    gameOver.draw(win)
    win.getKey()
    win.close()

main()

from graphics import *  # Importing graphics.py library and functions
from random import *  # Imports random library from Python
import winsound  # Imports Windows Sound library to make beeps, only on windows computer.


def main():
    win = GraphWin("Simon Says", 970, 600)
    win.setBackground('Black')

    redButton = Circle(Point(250, 200), 50)
    redButton.setFill(color_rgb(0, 0, 0))
    redButton.setOutline(color_rgb(255, 255, 255))
    redButton.setWidth(3)

    yellowButton = Circle(Point(400, 200), 50)
    yellowButton.setFill(color_rgb(0, 0, 0))
    yellowButton.setOutline(color_rgb(255, 255, 255))
    yellowButton.setWidth(3)

    greenButton = Circle(Point(550, 200), 50)
    greenButton.setFill(color_rgb(0, 0, 0))
    greenButton.setOutline(color_rgb(255, 255, 255))
    greenButton.setWidth(3)

    blueButton = Circle(Point(700, 200), 50)
    blueButton.setFill(color_rgb(0, 0, 0))
    blueButton.setOutline(color_rgb(255, 255, 255))
    blueButton.setWidth(3)

    counter = Text(Point(880, 75), "0")
    counter.setSize(30)
    counter.setTextColor("Black")

    counterBorder = Circle(Point(880, 75), 40)
    counterBorder.setFill("White")
    counterBorder.setOutline("Red")
    counterBorder.setWidth(2)

    blueButton.draw(win)
    greenButton.draw(win)
    yellowButton.draw(win)
    redButton.draw(win)
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
            if color == "R":
                redButton.setFill(color_rgb(255, 0, 0))
                winsound.Beep(1000, 500)
                redButton.setFill(color_rgb(0, 0, 0))
                time.sleep(playbackInterval)
            elif color == "Y":
                yellowButton.setFill(color_rgb(255, 255, 0))
                winsound.Beep(1300, 500)
                yellowButton.setFill(color_rgb(0, 0, 0))
                time.sleep(playbackInterval)
            elif color == "G":
                greenButton.setFill(color_rgb(0, 255, 0))
                winsound.Beep(1500, 500)
                greenButton.setFill(color_rgb(0, 0, 0))
                time.sleep(playbackInterval)
            elif color == "B":
                blueButton.setFill(color_rgb(0, 0, 255))
                winsound.Beep(2000, 500)
                blueButton.setFill(color_rgb(0, 0, 0))
                time.sleep(playbackInterval)

        instructions = Text(Point(480, 360), "'R' for Red, 'Y' for yellow, 'G' for Green, 'B' for blue.")
        instructions.setSize(25)
        instructions.setTextColor(color_rgb(255, 255, 255))
        instructions.draw(win)

        for count in stack:
            keyStroked = win.getKey()
            instructions.undraw()
            if keyStroked.upper() == count:
                if count == "R":
                    redButton.setFill(color_rgb(255, 0, 0))
                    winsound.Beep(1000, 300)
                    redButton.setFill(color_rgb(0, 0, 0))
                elif count == "Y":
                    yellowButton.setFill(color_rgb(255, 255, 0))
                    winsound.Beep(1300, 300)
                    yellowButton.setFill(color_rgb(0, 0, 0))
                elif count == "G":
                    greenButton.setFill(color_rgb(0, 255, 0))
                    winsound.Beep(1500, 300)
                    greenButton.setFill(color_rgb(0, 0, 0))
                elif count == "B":
                    blueButton.setFill(color_rgb(0, 0, 255))
                    winsound.Beep(2000, 300)
                    blueButton.setFill(color_rgb(0, 0, 0))
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

    # point1 = Point(250, 250)
    # point2 = Point(800, 400)
    # rectangle = Rectangle(point1, point2)

    # polygon = Polygon(Point(40,40),
    # Point(100,100),
    # Point(40, 100),
    # Point(0, 60))
    # Drawing Polygon
    # polygon.setFill('Cyan')
    # polygon.setOutline('White')
    # polygon.setWidth(2)
    # polygon.draw(win)

    # rectangle.setOutline(color_rgb(0, 255, 255))                            # Drawing Rectangle
    # rectangle.draw(win)

    # colors=["Blue", "Red", "Yellow"]
    # for n in colors:
    # win.getMouse()
    # polygon.setFill(n)

    # text = Text(Point(300, 300), "In a galaxy far far away ...")
    # text.setTextColor('Cyan')                                               # Drawing Text
    # text.setSize(30)
    # text.setFace('helvetica')
    # text.draw(win)

    # img = Image(Point(200, 200), "Image.png")
    # img.draw(win)                                                           # Drawing Image

    # input_box = Entry(Point(250, 250), 20)
    # input_box.draw(win)
    # input = input_box.getText()

    # txt = Text(Point(300, 300), "")
    # txt.setTextColor('White')
    # txt.draw(win)

    # while True:
    #    txt.setText(input_box.getText())
    # def correct():
    #    for i in range(3):
    #        redButton.setFill(color_rgb(0, 255, 0))
    #        yellowButton.setFill(color_rgb(0, 255, 0))
    #        greenButton.setFill(color_rgb(0, 255, 0))
    #        blueButton.setFill(color_rgb(0, 255, 0))
    #        time.sleep(.500)
    #        redButton.setFill(color_rgb(0, 0, 0))
    #        yellowButton.setFill(color_rgb(0, 0, 0))
    #        greenButton.setFill(color_rgb(0, 0, 0))
    #        blueButton.setFill(color_rgb(0, 0, 0))
    #        time.sleep(.500)

    # def gameOver():
    #    gameOver = Text(Point(480, 360), "GAME OVER")
    #    gameOver.setSize(30)
    #    gameOver.setTextColor(color_rgb(255, 0, 0))
    #    gameOver.draw(win)
    #    time.sleep(3)
    #    gameOver.undraw()
    #    stack = [""]
    #    win.close()


main()

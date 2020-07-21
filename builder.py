from cmu_112_graphics import *
import math

def drawCursor(app, canvas):
    canvas.create_oval(app.cursorX + app.cursorMargin, app.cursorY + app.cursorMargin,
                            app.cursorX + app.sizeX - app.cursorMargin,
                            app.cursorY + app.sizeY - app.cursorMargin,
                            fill="#0088FF", outline="white")

def drawBoard(width, height, canvas, app):
    for i in range(height):
        for j in range(width):
            canvas.create_rectangle(i * app.sizeX, j * app.sizeY,
                                    (i * app.sizeX) + app.sizeX, (j * app.sizeY) + app.sizeY,
                                    fill = "black", outline = "white")

def appStarted(app):
    app.cursorMargin = 10
    app.cursorTileX = 0
    app.cursorTileY = 0
    app.cursorX = 0
    app.cursorY = 0
    app.screenW = 600
    app.screenH = 600
    app.width = 10
    app.height = 10
    app.sizeX = app.screenW // app.width
    app.sizeY = app.screenH // app.height
    app.board = []
    for i in range(app.height):
        temp = []
        for j in range(app.width):
            temp.append("_")
        app.board.append(temp)

def keyPressed(app, event):
    if event.key == "Left" and app.cursorTileX != 0:
        app.cursorX -= app.sizeX
        app.cursorTileX -= 1
    elif event.key == "Right" and app.cursorTileX != app.width:
        app.cursorTileX += 1
        app.cursorX += app.sizeX
    if event.key == "Up" and app.cursorTileY != 0:
        app.cursorTileY -= 1
        app.cursorY -= app.sizeY
    elif event.key == "Down" and app.cursorTileX != app.height:
        app.cursorTileY += 1
        app.cursorY += app.sizeY

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.screenW, app.screenH, fill = "black")
    drawBoard(app.width, app.height, canvas, app)
    drawCursor(app, canvas)

runApp(width=600, height=600)

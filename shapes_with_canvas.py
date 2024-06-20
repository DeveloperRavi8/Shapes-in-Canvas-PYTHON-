from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Shapes in Canvas In Python Project 166")
root.geometry("1000x700")
root.configure(bg="teal")
# GLOBAL VAIRABLES #

keypress = ""

# DEFINING SHAPES FUNCTIONS  #

def circle(event):
    print("circle")
    global keypress

    keypress = "c"

    startX = startXVal.get()
    startY = startYVal.get()
    endX = endXVal.get()
    endY = endYVal.get()

    draw(keypress, startX, startY, endX, endY)


def rectangle(event):
    print("rectangle")
    global keypress
    keypress = "r"

    startX = startXVal.get()
    startY = startYVal.get()
    endX = endXVal.get()
    endY = endYVal.get()

    draw(keypress, startX, startY, endX, endY)


def line(event):
    print("line")
    global keypress
    keypress = "l"

    startX = startXVal.get()
    startY = startYVal.get()
    endX = endXVal.get()
    endY = endYVal.get()

    draw(keypress, startX, startY, endX, endY)


def draw(keypress, startX, startY, endX, endY):
    print(keypress, startX, startY, endX, endY)

    fill_color = ColorValue.get()

    if(keypress == "c"):
        canvas.create_oval(startX, startY, endX, endY, width=3, fill=fill_color)
    if(keypress == "r"):
        canvas.create_rectangle(startX, startY, endX, endY, width=3, fill=fill_color)
    if(keypress == "l"):
        canvas.create_line(startX, startY, endX, endY, width=3, fill=fill_color)


# BINDING KEYS TO ROOT || ADDING LISITNERS TO KEYS #

root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<l>", line)


# UI PART #
canvas = Canvas(root, height="570", width="1000", background="white")
canvas.pack()

label = Label(root, text="Start X: ")
label.place(relx=0.095, rely=0.85, anchor=CENTER)

startXList = [100, 200, 300, 400, 500, 600, 700, 800]
startXVal = StringVar()
combobox = ttk.Combobox(root, values=startXList, textvariable=startXVal)
combobox.place(relx=0.2, rely=0.85, anchor=CENTER)


label2 = Label(root, text="Start Y: ")
label2.place(relx=0.3, rely=0.85, anchor=CENTER)

startYList = [100, 200, 300, 400, 500, 600, 700, 800]
startYVal = StringVar()
combobox = ttk.Combobox(root, values=startYList, textvariable=startYVal)
combobox.place(relx=0.4, rely=0.85, anchor=CENTER)


label3 = Label(root, text="End X: ")
label3.place(relx=0.5, rely=0.85, anchor=CENTER)

endXList = [100, 200, 300, 400, 500, 600, 700, 800]
endXVal = StringVar()
combobox = ttk.Combobox(root, values=endXList, textvariable=endXVal)
combobox.place(relx=0.6, rely=0.85, anchor=CENTER)

label4 = Label(root, text="End Y: ")
label4.place(relx=0.7, rely=0.85, anchor=CENTER)

endYList = [100, 200, 300, 400, 500, 600, 700, 800]
endYVal = StringVar()
combobox = ttk.Combobox(root, values=endYList, textvariable=endYVal)
combobox.place(relx=0.8, rely=0.85, anchor=CENTER)


labelChooseColor = Label(root, text="Choose Color: ")
labelChooseColor.place(relx=0.6, rely=0.9, anchor=CENTER)

ColorChooseList = ["Black", "Blue", "Yellow", "Green", "Red", "Purple", "Orange", "Pink"]
ColorValue = StringVar()
combobox = ttk.Combobox(root, values=ColorChooseList, textvariable=ColorValue)
combobox.place(relx=0.75, rely=0.9, anchor=CENTER)

root.mainloop()
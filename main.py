# Importing  tkinter library
from tkinter import * 
from tkinter import ttk

#Geral colors

color1 = "#000000" # Black to background
color2 = "#212121" # Kinda Clear Black
color3 = "#3F3F3F" # Clearer Black
color4 = "#f0f0f0" # White
color5 = "#B4B4B4" # Gray
color6 = "#4CB93E" # Green



janela =Tk()
janela.title("Calculadora")
janela.geometry("235x305")
janela.config(bg=color1)

# Frames in the app
frame_screen = Frame(janela, width=235, height=50, bg=color1)
frame_screen.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268, bg=color1)
frame_body.grid(row=1, column=0)

# Variable of all values
all_values = ''

# Labels
text_value = StringVar()

# Function
def entry_value(event):

    global all_values

    all_values = all_values + str(event)
    
    text_value.set(all_values)

# Calculate
def calculate():
    global all_values
    try:
        result = eval(all_values)
        text_value.set(str(result))
    except:
        text_value.set("Error")
        all_values = ""

# Clean screen
def clean_screen():
    global all_values
    all_values =""
    text_value.set("")



app_label = Label(frame_screen, textvariable=text_value, width=15, height=2, padx=8, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), 
                  bg=color1, fg=color4)
app_label.place(x=0,y=0)
# Creating buttons

# Clear button (b_1)
b_1 = Button (frame_body, command=clean_screen, text=('C'), width=11, height=2, bg=color3, font=('MSSerif 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=4)
b_1.config(fg=color4)
# Remainder operator (b_2)
b_2 = Button(frame_body, command=lambda: entry_value('%'), text="%", width=5, height=2,bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=4)
b_2.config(fg=color4)
# Division button (b_3)
b_3 = Button(frame_body, command=lambda: entry_value('/'), text="/", width=5, height=2, bg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=4)

# 7 (b_4)
b_4 = Button(frame_body, command=lambda: entry_value('7'), text="7", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=55)
b_4.config(fg=color4)
# 8 (b_5)
b_5 = Button(frame_body,command=lambda: entry_value('8'), text="8", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=55)
b_5.config(fg=color4)
# 9 (b_6)
b_6 = Button(frame_body, command=lambda: entry_value('9'), text="9", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=55)
b_6.config(fg=color4)
# Multiply button (b_7)
b_7 = Button(frame_body, command=lambda: entry_value('*'), text="x", width=5, height=2,bg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=55)

# 4 (b_8)
b_8 = Button(frame_body, command=lambda: entry_value('4'), text="4", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=105)
b_8.config(fg=color4)
# 5 (b_9)
b_9 = Button(frame_body, command=lambda: entry_value('5'), text="5", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=105)
b_9.config(fg=color4)
# 6 (b_10)
b_10 = Button(frame_body, command=lambda: entry_value('6'), text="6", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=105)
b_10.config(fg=color4)
# Subtraction button (b_11)
b_11 = Button(frame_body, command=lambda: entry_value('-'), text="-", width=5, height=2, bg=color5, font=('Courier 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=105)

# 1 (b_12)
b_12 = Button(frame_body, command=lambda: entry_value('1'), text="1", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=155)
b_12.config(fg=color4)
# 2 (b_13)
b_13 = Button(frame_body, command=lambda: entry_value('2'), text="2", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=155)
b_13.config(fg=color4)
# 3 (b_14)
b_14 = Button(frame_body, command=lambda: entry_value('3'), text="3", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=155)
b_14.config(fg=color4)
# Addition button (b_15)
b_15 = Button(frame_body, command=lambda: entry_value('+'), text="+", width=5, height=2,bg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=155)

# 0 (b_16)
b_16 = Button(frame_body, command=lambda: entry_value('0'), text="0", width=11, height=2, bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=205)
b_16.config(fg=color4)
# Comma (b_17)
b_17 = Button(frame_body, command=lambda: entry_value('.'), text=".", width=5, height=2,bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=205)
b_17.config(fg=color4)
# Equal/result button (b_18)
b_18 = Button(frame_body, command= calculate, text="=", width=5, height=2, bg=color6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=205)
b_18.config(fg=color4)

janela.mainloop()
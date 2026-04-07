# Importing  tkinter library
from tkinter import * 
from tkinter import ttk

#Geral colors

cor1 = "#000000" # Black to background
cor2 = "#212121" # Kinda Clear Black
cor3 = "#3F3F3F" # Clearer Black
cor4 = "#f0f0f0" # White
cor5 = "#B4B4B4" # Gray
cor6 = "#4CB93E" # Green



janela =Tk()
janela.title("Calculadora")
janela.geometry("235x305")
janela.config(bg=cor1)

# Frames in the app
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)

# Creating buttons
# Clear button (b_1)
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=4)
b_1.config(fg=cor4)
# Remainder operator (b_2)
b_2 = Button(frame_corpo, text="%", width=5, height=2,bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=4)
b_2.config(fg=cor4)
# Division button (b_3)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=4)

# 7 (b_4)
b_4 = Button(frame_corpo, text="7", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=55)
b_4.config(fg=cor4)
# 8 (b_5)
b_5 = Button(frame_corpo, text="8", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=55)
b_5.config(fg=cor4)
# 9 (b_6)
b_6 = Button(frame_corpo, text="9", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=55)
b_6.config(fg=cor4)
# Multiply button (b_7)
b_7 = Button(frame_corpo, text="x", width=5, height=2,bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=55)

# 4 (b_8)
b_8 = Button(frame_corpo, text="4", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=105)
b_8.config(fg=cor4)
# 5 (b_9)
b_9 = Button(frame_corpo, text="5", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=105)
b_9.config(fg=cor4)
# 6 (b_10)
b_10 = Button(frame_corpo, text="6", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=105)
b_10.config(fg=cor4)
# Subtraction button (b_11)
b_11 = Button(frame_corpo, text="-", width=5, height=2,bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=105)

# 1 (b_12)
b_12 = Button(frame_corpo, text="1", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=155)
b_12.config(fg=cor4)
# 2 (b_13)
b_13 = Button(frame_corpo, text="2", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=155)
b_13.config(fg=cor4)
# 3 (b_14)
b_14 = Button(frame_corpo, text="3", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=155)
b_14.config(fg=cor4)
# Addition button (b_15)
b_15 = Button(frame_corpo, text="+", width=5, height=2,bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=155)

# 0 (b_16)
b_16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=205)
b_16.config(fg=cor4)
# Comma (b_17)
b_17 = Button(frame_corpo, text=",", width=5, height=2,bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=205)
b_17.config(fg=cor4)
# Equal/result button (b_18)
b_18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=205)
b_18.config(fg=cor4)

janela.mainloop()
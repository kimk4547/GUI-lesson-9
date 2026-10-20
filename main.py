from tkinter import *
import tkinter.messagebox
import random

root = Tk()

root.geometry("400x400")

root.title("Guess the Number Game")

def ok():
    name = entry_name.get()
    tkinter.messagebox.showinfo("Welcome!", "hi there, " + name + ". I'm thinking of a number between 1 and 20... can you figure it out?")

number = random.randint(1, 20)

def check():
    guess = int(entry_guess.get())
    if guess > number:
       tkinter.messagebox.showinfo("Whoops!", "Oh no! That's too high.")
    elif guess < number:
        tkinter.messagebox.showinfo("Whoops!", "Oops! The guess is too low.")
    elif guess == number:
        tkinter.messagebox.showinfo("Yay!!!", "Good job, that's correct!")
         
welcome_label = Label(root, text = "Welcome To Our Game!", fg = "black", font = 10)

welcome_label.pack(pady = 20)

name_label = Label(root, text = "what's your name?", fg = "black", font = 8)

name_label.place(x = 3, y = 60)

entry_name = Entry(root, width = 35)

entry_name.place(x = 3, y = 93)

ok_btn = Button(root, text = "enter", command = ok)

ok_btn.place(x = 300, y = 93)

guess_label = Label(root, text = "take a guess!", fg = "black", font = 8)

guess_label.place(x = 3, y = 200)
entry_guess = Entry(root, width = 17,)

entry_guess.place(x = 3, y = 240)

guess_btn = Button(root, text = "guess", command = check)

guess_btn.place(x = 300, y = 240)

root.mainloop()



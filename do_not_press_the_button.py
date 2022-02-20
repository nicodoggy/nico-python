'''
Created on Feb 20, 2022

@author: ctate
'''
import tkinter
if __name__ == '__main__':
    window = tkinter.Tk()
    button = tkinter.Button(window, text="Do not press this button.", width=40)
    button.pack(padx=10, pady=10)
    clickCount = 0
    def onClick(event):
        global clickCount
        clickCount = clickCount + 1
        if clickCount == 1:
            button.configure(text="Seriously? Do. Not. Press. It.")
        elif clickCount == 2:
            button.configure(text="Gah! Next time, no more button.")
        else:
            button.pack_forget()
    button.bind("<ButtonRelease-1>", onClick)
    window.mainloop()
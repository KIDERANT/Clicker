from tkinter import *
from tkinter import messagebox
n = 1
detishki = 0
def button_1():
    global detishki
    detishki += n
    l['text'] = detishki
    if detishki % 10 == 0:
        messagebox.showinfo('Фургон ',"у вас уже " + str(detishki) + " детей")
        
    


root = Tk()
root.title('Каждый клик ворует ребенка')
root.geometry('500x300')
Button(root, text='Своровать детей', width=15, height=2, bg='white', command=button_1).pack()
l = Label(root, width=15, bg='white', fg='cyan', font='consolas')
l.pack()
root.mainloop()
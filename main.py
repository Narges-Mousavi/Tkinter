import tkinter as tk
from tkinter import *
from tkinter import ttk
import math


def clear():
    al.delete('0', 'end')
    bl.delete('0', 'end')
    cl.delete('0', 'end')
    showlabel = tk.Label(frame, width=30, height=2)
    showlabel.grid(row=1, column=0, columnspan=10, padx=18, pady=18)


def calculate():
    showlabel = tk.Label(frame, width=30, height=2)
    showlabel.grid(row=1, column=0, columnspan=10, padx=18, pady=18)

    try:
        a = float(al.get())
        b = float(bl.get())
        c = float(cl.get())
        delta = b ** 2 - 4 * a * c

        showlabel = tk.Label(frame)
        showlabel.grid(row=1, column=0, columnspan=10, padx=18, pady=18)
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            show_x = 'x1 = ' + str(x1) + '\nx2 = ' + str(x2)
            showlabel.config(text=show_x, fg='black', bg='medium sea green')
        elif delta == 0:
            x = (-b + math.sqrt(delta)) / (2 * a)
            show_x = 'x1 = x2 = ' + str(x)
            showlabel.config(text=show_x, fg='black', bg='#00cccc')
        else:
            show_x = 'delta is less than zero'
            showlabel.config(text=show_x, fg='black', bg='red')
    except ZeroDivisionError:
        if b != 0:
            if c != 0:
                x = 'x = ' + str(-c / b)
                showlabel.config(text=x, fg='black', bg='hotpink')
            else:
                showlabel.config(text='x = 0', fg='black', bg='plum')
        else:
            showlabel.config(text='No answer', fg='black', bg='mediumaquamarine')
    except ValueError:
        showlabel.config(text='please enter all of the elements', fg='black', bg='mediumaquamarine')


parent = tk.Tk()

frame = tk.Frame(parent, highlightbackground='#006666', highlightthickness=2)
frame.grid(row=0, columnspan=100, sticky='w')
frame2 = tk.Frame(parent, highlightbackground='#fa140d', highlightthickness=2)
frame2.grid(row=4, sticky='w')

parent.title('Gui Exercises')

al = tk.Entry(frame, width=8, bg='#ccffe5')
al.grid(row=0, column=0, padx=18, pady=18, sticky='W')
tk.Label(frame, text="X^2 +", font=('Times New Roman', 12)).grid(row=0, column=1, sticky='w', padx=18, pady=18)
bl = tk.Entry(frame, width=8, bg='#ccffe5')
bl.grid(row=0, column=2, padx=18, pady=18, sticky='W')
tk.Label(frame, text="X +", font=('Times New Roman', 12)).grid(row=0, column=3, sticky='W', padx=18, pady=18)
cl = tk.Entry(frame, width=8, bg='#ccffe5')
cl.grid(row=0, column=4, padx=18, pady=18, sticky='W')
tk.Label(frame, text="= 0", font=('Times New Roman', 12)).grid(row=0, column=5, sticky='W', padx=18, pady=18, )
tk.Button(frame, text="Submit", bg='teal', border=4, fg='white', command=calculate).grid(row=2, column=2, padx=18,pady=18, columnspan=1)
tk.Button(frame, text=" Clear ", bg='teal', border=4, fg='white', command=clear).grid(row=2, column=3, padx=18, pady=18, columnspan=1)


# BMI
def clear():
    b.delete('0', 'end')
    c.delete('0', 'end')
    a.delete('0', 'end')
    showlabel = tk.Label(frame2, height=3, width=60)
    showlabel.grid(row=6, column=25, columnspan=2)


def show():
    showlabel = tk.Label(frame2, height=3, width=60)
    showlabel.grid(row=6, column=25, columnspan=2)
    showlabel = tk.Label(frame2)
    showlabel.grid(row=6, column=25, columnspan=2)
    try:
        weight = float(b.get())
        height = float(c.get())
        BMI = weight / (height * height)
        if weight <= 0:
            if height <= 0:
                showlabel.config(text='Invalid weight & height\U0001f611', fg='black', bg='cadetblue')
            else:
                showlabel.config(text='Invalid weight\U0001f611', fg='black', bg='red')
        elif height < 0:
            showlabel.config(text='Invalid height\U0001f611', fg='black', bg='red')
        elif BMI <= 18.5:
            show_bmi = 'BMI = ' + str(BMI) + '\n YOU ARE UNDERWEIGHT\N{face with tears of joy}' + '\nYou need ' + str((18.5 * height ** 2) - weight) + ' kg to become normal'
            showlabel.config(text=show_bmi, fg='black', bg='yellow')
        elif 18.5 < BMI <= 24.9:
            show_bmi = 'BMI = ' + str(BMI) + '\n GREAT YOU ARE NORMAL\N{smiling face with sunglasses}'
            showlabel.config(text=show_bmi, fg='black', bg='mediumseagreen')
        elif 24.9 < BMI <= 29.9:
            show_bmi = 'BMI = ' + str(BMI) + '\n UNFORTUNATELY YOU ARE OVERWEIGHT\N{zipper-mouth face}' + '\nYou should ' + str((weight - (25 * height ** 2))) + ' kg lose your weight'
            showlabel.config(text=show_bmi, fg='black', bg='salmon')
        elif BMI >= 30:
            show_bmi = 'BMI = ' + str(BMI) + '\n SORRY YOU ARE OBESITY\N{angry face}' + '\nYou should ' + str((weight - (25 * height ** 2))) + ' kg lose your weight'
            showlabel.config(text=show_bmi, fg='black', bg='red')
    except ZeroDivisionError:
        if weight <= 0:
            showlabel.config(text='Invalid weight & height\U0001f611', fg='black', bg='#ff9999')
        else:
            showlabel.config(text='Invalid height\U0001f611', fg='black', bg='#cc99ff')
    except ValueError:
        showlabel.config(text='please enter all of the elements\U0001f604', fg='black', bg='#cc99ff')


tk.Label(frame2, text="weight(kg)  :", font=('Times New Roman', 14)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
b = tk.Entry(frame2, width=6, bg='#ccffe5')
b.grid(row=0, column=1, sticky='w', columnspan=9, padx=5, pady=5)
tk.Label(frame2, text="height(m)  :", font=('Times New Roman', 14)).grid(row=0, column=10, sticky='w', padx=5, pady=5)
c = tk.Entry(frame2, width=6, bg='#fdfd88')
c.grid(row=0, column=11, sticky='w', columnspan=9, padx=5, pady=5)
tk.Label(frame2, text="Age :", font=('Times New Roman', 14)).grid(row=0, column=20, sticky='w', padx=5, pady=5)
n = tk.StringVar()
a = ttk.Combobox(frame2, width=8, textvariable=n)
a['values'] = list(range(18, 46))
a.grid(column=21, row=0, padx=13)
a.current()

tk.Label(frame2, text="Gender :", font=('Times New Roman', 14)).grid(row=6, column=0, sticky='w', padx=5, pady=5)
tk.Radiobutton(frame2, text='Female', font=('Times New Roman', 12), bg='#fac5fc', value=1).grid(row=7, column=0,rowspan=3, sticky='w', padx=5, pady=5)
tk.Radiobutton(frame2, text='Male', font=('Times New Roman', 12), bg='#ccff99', value=2).grid(row=7, column=1,columnspan=2, sticky='w', padx=5, pady=5)
tk.Button(frame2, text="Submit", bg='#cc99ff', border=4, command=show).grid(row=6, column=16, padx=5, pady=5)
tk.Button(frame2, text=" Clear ", bg='salmon', border=4, command=clear).grid(row=7, column=16, padx=5, pady=5)

parent.mainloop()

# tkinter

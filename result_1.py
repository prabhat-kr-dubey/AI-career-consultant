from tkinter import *
import matplotlib.pyplot as plt
from  result_2 import *
global maths
global bio
global comerse
global arts
global arr
global ddd
def result_1(data1):
    ddd=data1

    print("ayush")
    
    maths=data1["maths"]+data1["che"]+data1["physics"]
    maths=maths/3
    #arr.append(maths)
    #print(maths)
    bio=data1["bio"]+data1["che"]+data1["physics"]
    bio=bio/3
    #arr.append(bio)
    #print(bio)
    comerse=data1["civics"]+data1["economics"]+data1["maths"]
    comerse=comerse/3
    #arr.append(comerse)
    #print(comerse)
    arts=data1["civics"]+data1["history"]+data1["grogrophy"]
    arts=arts/3
    #arr.append(arts)
    #print(arts)
    #print(arr)

    
    res = Tk()
    L1 = Label(res, text="***RESULT***", bg="green", fg="white", font=("bold", 30,), padx=180, pady=5)
    L1.pack()
    # blank_label
    L2 = Label(res)
    L2.pack()
    x = ("HELLO !!!!! According to your prefrences this is your score chart--->  ")
    L3=Label(res, text=x, font=("bold", 14,), pady=5)
    L3.pack()
    L4 = Label(res)
    L4.pack()
    def goHome():
        res.destroy()
        #print("poornima")
        result_2(ddd)

    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = ['MATHS','BIOLOGY','COMERSE','ARTS']
    sizes = [maths,bio,comerse,arts]
    #explode = (0.1,0)
    fig.add_subplot(111).pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
    

    canvas = FigureCanvasTkAgg(fig, master=res)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    b23=Button(text="final_result->",command=goHome,fg="white", bg="black")
    b23.pack()
    
    res.mainloop()    

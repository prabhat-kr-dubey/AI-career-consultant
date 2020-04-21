from tkinter import *
from result_1 import *
def mains_page():

    questions= [

                ["How is your computer skill ?",
                  "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"
                  ],
                 ["How is your Chemistry skill?",
                  "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"
                     ],
                 ["How is your Maths skill ?",
                  "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                 ["How is your Regional Language Skill?",
                  "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                 ["How good are you in History ?",
                  "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
        ["How good are you in Civics?" ,
                   "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How good are you in economics?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How is your geography skill?" ,
                 "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How are you in sports?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How is you Art and Craft skill?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How good are you at Speaking Skill?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How is you Leadership Quality?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How good are you with Current affairs?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How is your biology skill?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"],
                [
                    "How is your Physics skill?" ,
                "POOR",
                  "GOOD",
                  "EXCELENT",
                  "OUTSTANDING"]]
    global i
    i=0
    arr=["computer","che","maths","reg_lang","history","civics","economics","grogrophy","sports","a&c","spacking","leadership","current_aff","bio","physics"]
    global data
    data={}
    def show_question(x):
        
        def get_i():
            return(i)

        def feed():
            value=v.get()
            data[arr[x]]=int(value)
            #print(data)
            root.destroy()


        root=Tk()
        root.title("DETAILS")
        L1=Label(root,text="CAREER COUNSELING SYSTEM  ",bg="green",fg="white",font=("bold",30,),padx=150)
        L1.grid(row=0,column=0)

        L2=Label(root,pady=7)
        L2.grid(row=1,column=0)
        photo = PhotoImage(file = 'abc1.png')
        photo = photo.subsample(2)
        lbl = Label(root,image = photo)
        lbl.image = photo
        lbl.grid(row=2,column=0, columnspan=8)

        L4=Label(root,text="")
        L4.grid(row=3,column=0)

        L5=Label(root,text="QUESTION --->",bg="yellow",fg="black",font=("bold",18,))
        L5.grid(row=4,column=0)

        L6=Label(root,text="",padx=8)
        L6.grid(row=5,column=0)

        L7=Label(text=questions[x][0],font=("bold",14,))
        L7.grid(row=6,column=0)
        L8=Label(root,pady=10)
        L8.grid(row=7,column=0)

        #rabdio button

        v=StringVar()
        R1=Radiobutton(root,text=questions[x][1],variable=v,value="1",font=("bold",12,),pady=6)
        R1.grid(row=8,column=0)
        R2=Radiobutton(root,text=questions[x][2],variable=v,value="2",font=("bold",12,),pady=6)
        R2.grid(row=9,column=0)
        R3=Radiobutton(root,text=questions[x][3],variable=v,value="3",font=("bold",12,),pady=6)
        R3.grid(row=10,column=0)
        R4=Radiobutton(root,text=questions[x][4],variable=v,value="4",font=("bold",12,),pady=6)
        R4.grid(row=11,column=0)

        L9=Label(root)
        L9.grid(row=12,column=0)

        #Button

        B1=Button(root,text="Next->Question",font=("bold",14,),pady=8,bg="red",fg="white",command=feed)
        B1.grid(row=13,column=0)
        root.mainloop()

        

        
    #show_question(0)
    for i in range(0,len(questions)):
        show_question(i)
        #print("ayush")

    else:
        result_1(data)
        #print(data)
        
#mains_page()    

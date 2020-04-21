from tkinter import *
def math_arts(choice1,choice2,dat):
    
    global ddd
    ddd=dat
    dis2=Tk()
    def next_display():
        dis2.destroy()
        dis3=Tk()
        def End():
            dis3.destroy()
                
        dis3.title("result")
        L1=Label(dis3,text="CAREER COUNSELING SYSTEM  ",bg="green",fg="white",font=("bold",30,),padx=15)
        L1.grid(row=0,column=0)

        L2=Label(dis3,pady=7)
        L2.grid(row=1,column=0)

        photo = PhotoImage(file = 'index.png')
        photo = photo.subsample(1)
        Lbl = Label(dis3,image = photo)
        Lbl.image = photo
        Lbl.grid(row=2,column=0, columnspan=8)
        L4=Label(dis3,text="")
        L4.grid(row=3,column=0)
        x="** If you go for '"+"COMERSE"+"' **"
        L5=Label(dis3,text=x,bg="yellow",fg="black",font=("bold",18,))
        L5.grid(row=4,column=0)

        L6=Label(dis3,pady=10)
        L6.grid(row=5,column=0)

        L7=Label(dis3,text="If you go for '"+"ARTS"+"' then you can go for these jobs -->",bg="red",fg="white",font=("bold",20,))
        L7.grid(row=6,column=0)
        L8=Label(dis3,pady=10)
        L8.grid(row=7,column=0)

                    #jobs

        L9=Label(dis3,text="-->> Layer",font=("bold",12,))
        L9.grid(row=9,column=0)
        L10=Label(dis3,text="-->> Politician",font=("bold",12,))
        L10.grid(row=10,column=0)
        L11=Label(dis3,text="-->> Hotel Management",font=("bold",12,))
        L11.grid(row=11,column=0)
        L12=Label(dis3,text="-->> Fashion Designing",font=("bold",12,))
        L12.grid(row=12,column=0)
        L13=Label(dis3,text="-->> Police,IAS,IPS",font=("bold",12,))
        L13.grid(row=13,column=0)
        L14=Label(dis3,text="-->> Banking",font=("bold",12,))
        L14.grid(row=13,column=0)
        L15=Label(dis3,text="-->> Historian,Geographer",font=("bold",12,))
        L15.grid(row=13,column=0)

        L16=Label(dis3,pady=15)
        L16.grid(row=16,column=0)

        B1=Button(dis3,text="End",font=("bold",15,),bg="black",fg="white",command=End)
        B1.grid(row=17,column=0)


        
    dis2.title("result")
    L1=Label(dis2,text="CAREER COUNSELING SYSTEM  ",bg="green",fg="white",font=("bold",30,),padx=15)
    L1.grid(row=0,column=0)

    L2=Label(dis2,pady=7)
    L2.grid(row=1,column=0)

    photo = PhotoImage(file = 'index.png')
    photo = photo.subsample(1)
    lbl = Label(dis2,image = photo)
    lbl.image = photo
    lbl.grid(row=2,column=0, columnspan=8)

    L4=Label(dis2,text="")
    L4.grid(row=3,column=0)
    x="** Acoording to Your our analysis  you are good in both '"+choice1+"' and '"+choice2+"' **"
    L5=Label(dis2,text=x,bg="yellow",fg="black",font=("bold",18,))
    L5.grid(row=4,column=0)

    L6=Label(dis2,pady=10)
    L6.grid(row=5,column=0)

    L7=Label(dis2,text="If you go for '"+choice1+"' then you can go for these jobs -->",bg="red",fg="white",font=("bold",20,))
    L7.grid(row=6,column=0)
    L8=Label(dis2,pady=10)
    L8.grid(row=7,column=0)

    if ddd["computer"]>2:
        #print(data1["computer"])
        L9=Label(dis2,text="--> Data Analyst ",font=("bold",15,))
        L9.grid(row=9,column=0)
        L10=Label(dis2,text="--> Data Administrator ",font=("bold",15,))
        L10.grid(row=10,column=0)
        L11=Label(dis2,text="--> Full Stack Web Devloper",font=("bold",15,))
        L11.grid(row=11,column=0)
        L12=Label(dis2,text="--> Cyber Secruity",font=("bold",15,))
        L12.grid(row=12,column=0)
        L13=Label(dis2,text="--> Sofr Ware Enginner",font=("bold",15,))
        L13.grid(row=13,column=0)
        L14=Label(dis2,text="--> Machine Learning",font=("bold",15,))
        L14.grid(row=14,column=0)
    else:
        L9=Label(dis2,text="-->> Chemical Enginner",font=("bold",15,))
        L9.grid(row=9,column=0)
        L10=Label(dis2,text="-->> Mecanical Enginner",font=("bold",15,))
        L10.grid(row=10,column=0)
        L11=Label(dis2,text="-->> Civil Enginner",font=("bold",15,))
        L11.grid(row=11,column=0)
        L12=Label(dis2,text="-->> Architect",font=("bold",15,))
        L12.grid(row=12,column=0)
        L13=Label(dis2,text="-->> Aavy,Army,AirForce",font=("bold",15,))
        L13.grid(row=13,column=0)

    L14=Label(dis2,pady=15)
    L14.grid(row=14,column=0)

    B1=Button(dis2,text="Next",font=("bold",15,),bg="black",fg="white",command=next_display)
    B1.grid(row=15,column=0)

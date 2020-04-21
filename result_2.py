from tkinter import *
from math_comerse import *
from maths_arts import *
from bio_comerse import *
global maths
global bio
global comerse
global arts
global arr
arr=[]
global i
def result_2(data1):

    def  display1(choise):
        dis1=Tk()
        dis1.title("result")
        L1=Label(dis1,text="CAREER COUNSELING SYSTEM  ",bg="green",fg="white",font=("bold",30,),padx=15)
        L1.grid(row=0,column=0)

        L2=Label(dis1,pady=7)
        L2.grid(row=1,column=0)

        photo = PhotoImage(file = 'index.png')
        photo = photo.subsample(1)
        lbl = Label(dis1,image = photo)
        lbl.image = photo
        lbl.grid(row=2,column=0, columnspan=8)

        L4=Label(dis1,text="")
        L4.grid(row=3,column=0)
        x="** Acoording to Your our analysis if you choose '"+choise+"' then you can go for these jobs **"
        L5=Label(dis1,text=x,bg="yellow",fg="black",font=("bold",18,))
        L5.grid(row=4,column=0)

        L6=Label(dis1,pady=10)
        L6.grid(row=5,column=0)
        

        if(choise=="COMERSE"):
            L7=Label(dis1,text=choise+" related jobs are-->",bg="red",fg="white",font=("bold",20,))
            L7.grid(row=6,column=0)
            L8=Label(dis1,pady=10)
            L8.grid(row=7,column=0)

            #jobs

            L9=Label(dis1,text="-->> Financial Analysise ",font=("bold",15,))
            L9.grid(row=9,column=0)
            L10=Label(dis1,text="-->> Investmnt Manager",font=("bold",15,))
            L10.grid(row=10,column=0)
            L11=Label(dis1,text="-->> Management Consultant  ",font=("bold",15,))
            L11.grid(row=11,column=0)
            L12=Label(dis1,text="-->> Human Resource Manager(HR)",font=("bold",15,))
            L12.grid(row=12,column=0)
            L13=Label(dis1,text="-->> Auditor",font=("bold",15,))
            L13.grid(row=13,column=0)
            L14=Label(dis1,text="-->> Accountant",font=("bold",15,))
            L14.grid(row=14,column=0)
            L15=Label(dis1,text="-->> Marcating",font=("bold",15,))
            L15.grid(row=15,column=0)
        elif choise=="MATHS":
            L7=Label(dis1,text=choise+" related jobs are-->",bg="red",fg="white",font=("bold",20,))
            L7.grid(row=6,column=0)
            L8=Label(dis1,pady=10)
            L8.grid(row=7,column=0)

            #jobs
            if data1["computer"]>2:
                print(data1["computer"])
                L9=Label(dis1,text="--> Data Analyst ",font=("bold",15,))
                L9.grid(row=9,column=0)
                L10=Label(dis1,text="--> Data Administrator ",font=("bold",15,))
                L10.grid(row=10,column=0)
                L11=Label(dis1,text="--> Full Stack Web Devloper",font=("bold",15,))
                L11.grid(row=11,column=0)
                L12=Label(dis1,text="--> Cyber Secruity",font=("bold",15,))
                L12.grid(row=12,column=0)
                L13=Label(dis1,text="--> Sofr Ware Enginner",font=("bold",15,))
                L13.grid(row=13,column=0)
                L14=Label(dis1,text="--> Machine Learning",font=("bold",15,))
                L14.grid(row=14,column=0)
            else:
                L9=Label(dis1,text="-->> Chemical Enginner",font=("bold",15,))
                L9.grid(row=9,column=0)
                L10=Label(dis1,text="-->> Mecanical Enginner",font=("bold",15,))
                L10.grid(row=10,column=0)
                L11=Label(dis1,text="-->> Civil Enginner",font=("bold",15,))
                L11.grid(row=11,column=0)
                L12=Label(dis1,text="-->> Architect",font=("bold",15,))
                L12.grid(row=12,column=0)
                L13=Label(dis1,text="-->> Aavy,Army,AirForce",font=("bold",15,))
                L13.grid(row=13,column=0)
                
        elif choise=="BIO"  :
            L7=Label(dis1,text=choise+" related jobs are-->",bg="red",fg="white",font=("bold",20,))
            L7.grid(row=6,column=0)
            L8=Label(dis1,pady=10)
            L8.grid(row=7,column=0)

            #jobs

            L9=Label(dis1,text="-->> MBBS",font=("bold",15,))
            L9.grid(row=9,column=0)
            L10=Label(dis1,text="-->> Dentist",font=("bold",15,))
            L10.grid(row=10,column=0)
            L11=Label(dis1,text="-->> Doctor",font=("bold",15,))
            L11.grid(row=11,column=0)
            L12=Label(dis1,text="-->> Nurse Practitioner",font=("bold",15,))
            L12.grid(row=12,column=0)
            L13=Label(dis1,text="-->> Pharmasist",font=("bold",15,))
            L13.grid(row=13,column=0)
            L14=Label(dis1,text="-->> Phychologist",font=("bold",15,))
            L14.grid(row=14,column=0)
            L15=Label(dis1,text="-->> Surgeon",font=("bold",15,))
            L15.grid(row=15,column=0)
        elif choise=="ARTS":
            L7=Label(dis1,text=choise+" related jobs are-->",bg="red",fg="white",font=("bold",20,))
            L7.grid(row=6,column=0)
            L8=Label(dis1,pady=10)
            L8.grid(row=7,column=0)

            #jobs

            L9=Label(dis1,text="-->> Layer",font=("bold",12,))
            L9.grid(row=9,column=0)
            L10=Label(dis1,text="-->> Politician",font=("bold",12,))
            L10.grid(row=10,column=0)
            L11=Label(dis1,text="-->> Hotel Management",font=("bold",12,))
            L11.grid(row=11,column=0)
            L12=Label(dis1,text="-->> Fashion Designing",font=("bold",12,))
            L12.grid(row=12,column=0)
            L13=Label(dis1,text="-->> Police,IAS,IPS",font=("bold",12,))
            L13.grid(row=13,column=0)
            L14=Label(dis1,text="-->> Banking",font=("bold",12,))
            L14.grid(row=13,column=0)
            L15=Label(dis1,text="-->> Historian,Geographer",font=("bold",12,))
            L15.grid(row=13,column=0)

           
            
            
        
        dis1.mainloop()

    def display2(choice1,choice2):
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
            x="** If you go for '"+"BIOLOGY"+"' **"
            L5=Label(dis3,text=x,bg="yellow",fg="black",font=("bold",18,))
            L5.grid(row=4,column=0)

            L6=Label(dis3,pady=10)
            L6.grid(row=5,column=0)

            L7=Label(dis3,text="If you go for '"+choice1+"' then you can go for these jobs -->",bg="red",fg="white",font=("bold",20,))
            L7.grid(row=6,column=0)
            L8=Label(dis3,pady=10)
            L8.grid(row=7,column=0)

                    #jobs

            L9=Label(dis3,text="-->> MBBS",font=("bold",15,))
            L9.grid(row=9,column=0)
            L10=Label(dis3,text="-->> Dentist",font=("bold",15,))
            L10.grid(row=10,column=0)
            L11=Label(dis3,text="-->> Doctor",font=("bold",15,))
            L11.grid(row=11,column=0)
            L12=Label(dis3,text="-->> Nurse Practitioner",font=("bold",15,))
            L12.grid(row=12,column=0)
            L13=Label(dis3,text="-->> Pharmasist",font=("bold",15,))
            L13.grid(row=13,column=0)
            L14=Label(dis3,text="-->> Phychologist",font=("bold",15,))
            L14.grid(row=14,column=0)
            L15=Label(dis3,text="-->> Surgeon",font=("bold",15,))
            L15.grid(row=15,column=0)

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

        if data1["computer"]>2:
            print(data1["computer"])
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
    


            
            
        
        
        


        
    maths=data1["maths"]+data1["che"]+data1["physics"]
    maths=maths/3
    arr.append(maths)
    print(maths)
    bio=data1["bio"]+data1["che"]+data1["physics"]
    bio=bio/3
    arr.append(bio)
    print(bio)
    comerse=data1["civics"]+data1["economics"]+data1["maths"]
    comerse=comerse/3
    arr.append(comerse)
    print(comerse)
    arts=data1["civics"]+data1["history"]+data1["grogrophy"]
    arts=arts/3
    arr.append(arts)
    print(arts)
    print(arr)
    #set of arr

    set1=set(arr)
    if len(set1)==len(arr):
        max1=max(arr)
        i=arr.index(max1)
        #print(i)
        if i==0:
            display1("MATHS")
        elif i==1:
            display1("BIO")
        elif i==2:
            display1("COMERSE")
        elif i==3:
            display1("ARTS")        
    else:
        if(arr[0]==arr[1]):
            display2("MATHS","BIO")
        elif(arr[0]==arr[2]):
            #print(data1)
            math_comerse("MATHS","COMERSE",data1)
        elif(arr[0]==arr[3]):
            math_arts("MATHS","ARTS",data1)
        elif(arr[1]==arr[2]):
            bio_comerse("BIO","COMERSE",data1)
        else:
            display1("ARTS")
            
            
#result_2({"computer":3,"che":3,"maths":3,"reg_lang":4,"history":4,"civics":4,"economics":4,"grogrophy":4,"sports":3,"a&c":1,"spacking":3,"leadership":4,"current_aff":4,"bio":4,"physics":3})

            

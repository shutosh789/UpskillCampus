from tkinter import *
from tkinter import ttk

y=0
a=ttk.Notebook()


frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)
frame6 = ttk.Frame(a)
frame7 = ttk.Frame(a)
frame8 = ttk.Frame(a)
frame9 = ttk.Frame(a)
frame10 = ttk.Frame(a)

root = ttk.Frame(a)

def quiz(y):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="Q5")
    a.add(frame6, text="Q6")
    a.add(frame7, text="Q7")
    a.add(frame8, text="Q8")
    a.add(frame9, text="Q9")
    a.add(frame10, text="Q10")

    Label(frame1, text="Total keywords in python ?", font=("Arial", 40, "bold")).grid(row=2, column=2)
    Button(frame1, text="33", font=("calibri", 30, "bold"), bg="light blue", command=a1_right).grid(row=3, column=1)
    Button(frame1, text="31", font=("calibri", 30, "bold"), bg="light green", command=a1_wrong).grid(row=3, column=2)
    Button(frame1, text="30", font=("calibri", 30, "bold"), bg="light pink", command=a1_wrong).grid(row=3, column=3)

    Label(frame2, text="Output of 2**3 ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame2, text="6", font=("calibri", 30, "bold"), bg="light blue",command=a2_right).grid(row=3,column=1)
    Button(frame2, text="8", font=("calibri", 30, "bold"), bg="light green",command=a2_wrong).grid(row=3,column=2)
    Button(frame2, text="9", font=("calibri", 30, "bold"), bg="light pink",command=a2_wrong).grid(row=3, column=3)
    
    Label(frame3, text="Output of np.arrange(1,5) ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame3, text="[1,2,3,4]", font=("calibri", 30, "bold"), bg="light blue",command=a3_right).grid(row=3,column=1)
    Button(frame3, text="[0,1,2,3,4]", font=("calibri", 30, "bold"), bg="light green",command=a3_wrong).grid(row=3,column=2)
    Button(frame3, text="[1,2,3,4,5]", font=("calibri", 30, "bold"), bg="light pink",command=a3_wrong).grid(row=3, column=3)
    
    Label(frame4, text=" Output of 2*12 ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame4, text="24", font=("calibri", 30, "bold"), bg="light blue",command=a4_right).grid(row=3,column=1)
    Button(frame4, text="28", font=("calibri", 30, "bold"), bg="light green",command=a4_wrong).grid(row=3,column=2)
    Button(frame4, text="32", font=("calibri", 30, "bold"), bg="light pink",command=a4_wrong).grid(row=3, column=3)
    
    Label(frame5, text=" Python is _____ programming Language ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame5, text="high level", font=("calibri", 30, "bold"), bg="light blue",command=a5_right).grid(row=3,column=1)
    Button(frame5, text="low level", font=("calibri", 30, "bold"), bg="light green",command=a5_wrong).grid(row=3,column=2)
    Button(frame, text="None", font=("calibri", 30, "bold"), bg="light pink",command=a5_wrong).grid(row=3, column=3)
    
    Label(frame6, text="Python operator always yields the result of ___ ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame6, text="integer", font=("calibri", 30, "bold"), bg="light blue",command=a6_right).grid(row=3,column=1)
    Button(frame6, text="Complex", font=("calibri", 30, "bold"), bg="light green",command=a6_wrong).grid(row=3,column=2)
    Button(frame6, text="floating point", font=("calibri", 30, "bold"), bg="light pink",command=a6_wrong).grid(row=3, column=3)
    
    Label(frame7, text="String in python are ___ ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame7, text="mutable", font=("calibri", 30, "bold"), bg="light blue",command=a7_right).grid(row=3,column=1)
    Button(frame7, text="immutable", font=("calibri", 30, "bold"), bg="light green",command=a7_wrong).grid(row=3,column=2)
    Button(frame7, text="fixed", font=("calibri", 30, "bold"), bg="light pink",command=a7_wrong).grid(row=3, column=3)
    
    Label(frame8, text="Which statement is used for error checking ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame8, text="list", font=("calibri", 30, "bold"), bg="light blue",command=a8_right).grid(row=3,column=1)
    Button(frame8, text="Assert", font=("calibri", 30, "bold"), bg="light green",command=a8_wrong).grid(row=3,column=2)
    Button(frame8, text="tuple", font=("calibri", 30, "bold"), bg="light pink",command=a8_wrong).grid(row=3, column=3)
    
    Label(frame9, text=" Output of all [(2,4,0,6)]?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame9, text="true", font=("calibri", 30, "bold"), bg="light blue",command=a9_right).grid(row=3,column=1)
    Button(frame9, text="false", font=("calibri", 30, "bold"), bg="light green",command=a9_wrong).grid(row=3,column=2)
    Button(frame9, text="0", font=("calibri", 30, "bold"), bg="light pink",command=a9_wrong).grid(row=3, column=3)
    
    Label(frame10, text="list1 is [1,5,9], what is sum(list1) ?" , font=("Arial", 40, "bold")).grid(row2, column2)
    Button(frame10, text="1", font=("calibri", 30, "bold"), bg="light blue",command=a10_right).grid(row=3,column=1)
    Button(frame10, text="15", font=("calibri", 30, "bold"), bg="light green",command=a10_wrong).grid(row=3,column=2)
    Button(frame10, text="9", font=("calibri", 30, "bold"), bg="light pink",command=a10_wrong).grid(row=3, column=3)

    def a1_right():
         Label(frame1, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
         Label(frame1, text="Marks obtained : 1", font=("Arial", 30, "bold"), background="black", fg="white").grid(row=1, column=3)

    def a1_wrong():
         Label(frame1, text="Incorrect", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
         Label(frame1, text="Marks obtained : 0", font=("Arial", 30, "bold"), background="black", fg="white").grid(row=1, column=3)


    def a2_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a2_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)
     

    def a3_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a3_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)


    def a4_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a4_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    
    def a5_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a5_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)


    def a6_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a6_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)
 

    def a7_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a7_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)


    def a8_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a8_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)


    def a9_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a9_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)


    def a10_right():
         Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a10_wrong():
         Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
         Label(frame2,text="Marks obtained : 0 ",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)


quiz(y)
a.pack()
a.mainloop()

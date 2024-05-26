from tkinter import *
# import tkinter.messagebox as tmsg
root=Tk()

root.geometry("658x546")

# heading




Label(root,text="ENTER YOUR INTERNAL MARKS ",font="comicsansms 13 bold",pady=20).grid(row=0,column=3)

#subjects
ENTER_YOUR_NAME=Label(root, bg="grey",text="ENTER_YOUR_NAME",pady=20,relief=SUNKEN)
ENTER_YOUR_USN=Label(root, bg="grey",text="ENTER_YOUR_USN",pady=20,relief=SUNKEN)
MANAGEMENT_AND_ENTERP_FOR_IT_INDUSTRY=Label(root, bg="grey",text="MANAGEMENT_AND_ENTERP_FOR_IT_INDUSTRY",pady=10,relief=SUNKEN)
COMPUTER_NETWORKS=Label(root,bg="grey",text="COMPUTER_NETWORKS",pady=10,relief=SUNKEN)
DATABASE_MANAGEMENT_SYSTEM=Label(root,bg="grey",text="DATABASE_MANAGEMENT_SYSTEM",pady=10,relief=SUNKEN)
AUTOMATA_THEORY_AND_COMPUTABILITY=Label(root,bg="grey",text="AUTOMATA_THEORY_AND_COMPUTABILITY",pady=10,relief=SUNKEN)
JAVA_ADVANCE=Label(root,bg="grey",text="JAVA_ADVANCE",pady=10,relief=SUNKEN)
ARTIFICIAL_INTELEGENCE=Label(root,bg="grey",text="ARTIFICIAL_INTELEGENCE",pady=10,relief=SUNKEN)
COMPUTER_NETWORKS_LAB=Label(root,text="COMPUTER_NETWORKS_LAB",bg="grey",pady=10,relief=SUNKEN)
DATABASE_MANAGEMENT_SYSTEM_LAB=Label(root,text="DATABASE_MANAGEMENT_SYSTEM_LAB",bg="grey",pady=10,relief=SUNKEN)


# packing this for
ENTER_YOUR_NAME.grid(row=1,column=2)
ENTER_YOUR_USN.grid(row=3,column=2)
MANAGEMENT_AND_ENTERP_FOR_IT_INDUSTRY.grid(row=6,column=2)
COMPUTER_NETWORKS.grid(row=7,column=2)
DATABASE_MANAGEMENT_SYSTEM_LAB.grid(row=8,column=2)
AUTOMATA_THEORY_AND_COMPUTABILITY.grid(row=9,column=2)
JAVA_ADVANCE.grid(row=10,column=2)
ARTIFICIAL_INTELEGENCE.grid(row=11,column=2)
COMPUTER_NETWORKS_LAB.grid(row=12,column=2)


# initialize rhe tkinters varaiable for storing a data


name=StringVar()
usn=StringVar()
mit=StringVar()
cn=StringVar()
dbms=StringVar()
atc=StringVar()
java=StringVar()
ai=StringVar()
lab1=StringVar()
lab2=StringVar()


# entries for the form


entry1=Entry(root,textvariable=name)
entry2=Entry(root,textvariable=usn)
entry3=Entry(root,textvariable=mit)
entry4=Entry(root,textvariable=cn)
entry5=Entry(root,textvariable=dbms)
entry6=Entry(root,textvariable=atc)
entry7=Entry(root,textvariable=java)
entry8=Entry(root,textvariable=ai)
entry9=Entry(root,textvariable=lab1)
entry10=Entry(root,textvariable=lab2)


# packing n

entry1.grid(row=1, column=3)
entry2.grid(row=3, column=3)
entry3.grid(row=6, column=3)
entry4.grid(row=7, column=3)
entry5.grid(row=8, column=3)
entry6.grid(row=9, column=3)
entry7.grid(row=10, column=3)
entry8.grid(row=11, column=3)
entry9.grid(row=12, column=3)
entry10.grid(row=13, column=3)



# checkbox and packing it
conformation=Checkbutton(text="confirm your marks")
conformation.grid(row=15,column=3)

# checkbox and packing it


def getvals():
    print("submitting form")
    print(f" Name of the student   {name.get()},\n USN NUMBER  {usn.get()}, \nMANAGEMENT_AND_ENTERP_FOR_IT_INDUSTRY { mit.get()},\n COMPUTER_NETWORKS {cn.get()}"
          f"\n,DATABASE_MANAGEMENT_SYSTEM {dbms.get()},\nAUTOMATA_THEORY_AND_COMPUTABILITY {atc.get()},\n JAVA ADVANCE {java.get()},\n ARTIFICIAL INTELLIGENCE {ai.get()},"
          f"\nCOMPUTER_NETWORKS_LAB {lab1.get()},\n DATABASE_MANAGEMENT_SYSTEM_LAB {lab2.get()}")


    with open("marks.txt","a") as f:
        f.write(f"{name.get(),usn.get(),mit.get(),cn.get(),dbms.get(),atc.get(),java.get(),ai.get(),lab1.get(),lab2.get()}\n")


Button(text="submit yours internal marks",command=getvals).grid(row=16,column=3)
# tmsg.showinfo("done","submitted")


root.mainloop()
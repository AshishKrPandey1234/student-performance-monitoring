from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("658x546")
root.title("Student Performance Monitoring System")

# Heading
Label(root, text="Enter Your Internal Marks", font="comicsansms 13 bold", pady=20).grid(row=0, column=3)

# Subjects
subjects = [
    "Enter Your Name",
    "Enter Your USN",
    "Management and Enterprise for IT Industry",
    "Computer Networks",
    "Database Management System",
    "Automata Theory and Computability",
    "Java Advance",
    "Artificial Intelligence",
    "Computer Networks Lab",
    "Database Management System Lab"
]

# Labels and Entries
variables = {}
for i, subject in enumerate(subjects):
    Label(root, bg="grey", text=subject, pady=10, relief=SUNKEN).grid(row=i+1, column=2)
    variables[subject] = StringVar()
    Entry(root, textvariable=variables[subject]).grid(row=i+1, column=3)

# Checkbox
confirmation = Checkbutton(root, text="Confirm your marks")
confirmation.grid(row=len(subjects)+1, column=3)

def getvals():
    print("Submitting form")
    # Validate inputs
    for subject, var in variables.items():
        if not var.get():
            tmsg.showerror("Error", f"Please enter the {subject.lower()}.")
            return
    
    # Collect data
    data = {subject: var.get() for subject, var in variables.items()}
    print(data)

    with open("marks.txt", "a") as f:
        f.write(str(data) + "\n")
    
    tmsg.showinfo("Success", "Marks submitted successfully")

Button(text="Submit Your Internal Marks", command=getvals).grid(row=len(subjects)+2, column=3)

root.mainloop()

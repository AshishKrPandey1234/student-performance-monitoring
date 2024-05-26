from tkinter import *
import tkinter.messagebox as tmsg

def show_success_page(data):
    success_window = Toplevel(root)
    success_window.title("Submission Successful")
    success_window.geometry("400x300")
    
    Label(success_window, text="Submission Successful!", font="comicsansms 13 bold", pady=20).pack()
    
    details = "\n".join([f"{key}: {value}" for key, value in data.items()])
    Label(success_window, text=details, pady=10).pack()
    
    Button(success_window, text="Close", command=success_window.destroy).pack(pady=20)

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
    
    # Show success page
    show_success_page(data)

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

Button(text="Submit Your Internal Marks", command=getvals).grid(row=len(subjects)+2, column=3)

root.mainloop()

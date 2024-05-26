from tkinter import *
import tkinter.messagebox as tmsg

# Function to display the submission success page
def show_success_page(data):
    success_window = Toplevel(root)
    success_window.title("Submission Successful")
    success_window.geometry("400x300")

    Label(success_window, text="Submission Successful!", font="comicsansms 13 bold", pady=20).pack()

    details = "\n".join([f"{key}: {value}" for key, value in data.items()])
    Label(success_window, text=details, pady=10).pack()

    Button(success_window, text="Close", command=success_window.destroy).pack(pady=20)

# Function to submit student details
def getvals():
    # Validate inputs
    for subject, var in variables.items():
        if not var.get():
            tmsg.showerror("Error", f"Please enter the {subject.lower()}.")
            return

    # Collect data
    data = {subject: var.get() for subject, var in variables.items()}

    # Save data to dictionary
    student_data[data["Enter Your Name"]] = data

    # Clear the entries
    for var in variables.values():
        var.set("")

    # Show success page
    show_success_page(data)

# Function to retrieve student details
def retrieve_student_details():
    name = retrieve_name_var.get()
    if name in student_data:
        show_success_page(student_data[name])
    else:
        tmsg.showerror("Error", "Student not found")

# Initialize main window
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

# Submit button
Button(root, text="Submit Your Internal Marks", command=getvals).grid(row=len(subjects)+2, column=3)

# Retrieve student details section
Label(root, text="Retrieve Student Details", font="comicsansms 13 bold", pady=20).grid(row=len(subjects)+3, column=3)
Label(root, text="Enter Student Name", bg="grey", pady=10, relief=SUNKEN).grid(row=len(subjects)+4, column=2)
retrieve_name_var = StringVar()
Entry(root, textvariable=retrieve_name_var).grid(row=len(subjects)+4, column=3)
Button(root, text="Retrieve Details", command=retrieve_student_details).grid(row=len(subjects)+5, column=3)

# Dictionary to store student data
student_data = {}

root.mainloop()

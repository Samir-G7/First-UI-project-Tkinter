import tkinter as tk
import pyautogui as pyui
import json as myson
import os


class school:
    def __init__(self, name, age, gender, address, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone


class students(school):
    def __init__(self, name, age, gender, address, phone, room, faculty):
        self.room = room
        self.faculty = faculty
        self.totalfee = 500000
        self._form_built = False
        super().__init__(name, age, gender, address, phone)

    def fee(self, paidfee):
        due = self.totalfee - paidfee
        feetk = tk.Label(win, text=f"{self.name} had paid {paidfee}, left due is {due}")
        feetk.pack()

    def search_details(self):
        search =tk.Toplevel(win)
        search.geometry('600x600')
        search.configure(bg= "#258C74")
        #for searching student this is label
        lab = tk.Label(search,text = 'Enter Name of Student')
        lab.pack()
        #Entering Name TExt
        txt = tk.Entry(search)
        txt.pack()
        #get input
        def studentbutsearch():
            var = txt.get()
            with open("project2.json", "r") as file:
                data = myson.load(file)
            
            found = False

            for student in data:
                if var == student["Name"]:
                    det = tk.Label(
                        search,
                        text =
                        f"Name: {student['Name']}\n"
                        f"Age: {student['Age']}\n"
                        f"Gender: {student['Gender']}\n"
                        f"Address: {student['Address']}\n"
                        f"Phone: {student['Phone']}\n"
                        f"Class: {student['Class']}",
                        bg = '#258C74',
                    )
                    det.pack()
                    search.title('Searching for Student')
                    found = True
                    break

            if not found:
                pyui.alert("Student not found.")



        
        but = tk.Button(search, text='Submit',command = studentbutsearch)
        but.pack()
        search.mainloop()


    def Add_student(self):

        if self._form_built:
            return
        self._form_built = True

        name = tk.Label(win, text="Name :")
        name.place(x=200, y=215)
        self.namee = tk.Entry(win)
        self.namee.place(x=200, y=250)

        # for age
        Age = tk.Label(win, text="Age :")
        Age.place(x=200, y=300)
        self.Agee = tk.Entry(win)
        self.Agee.place(x=200, y=350)

        # gender
        Gender = tk.Label(win, text="Gender :")
        Gender.place(x=200, y=400)
        self.Gendere = tk.Entry(win)
        self.Gendere.place(x=200, y=450)

        # for address
        Address = tk.Label(win, text="Address :")
        Address.place(x=200, y=500)
        self.Addresse = tk.Entry(win)
        self.Addresse.place(x=200, y=550)

        # for contact
        Phone = tk.Label(win, text="Phone :")
        Phone.place(x=200, y=600)
        self.Phonee = tk.Entry(win)
        self.Phonee.place(x=200, y=650)

        # for class
        Class = tk.Label(win, text="Class :")
        Class.place(x=200, y=700)
        self.Classe = tk.Entry(win)
        self.Classe.place(x=200, y=750)

        def save():
            Json = {
                "Name": self.namee.get(),
                "Age": self.Agee.get(),
                "Gender": self.Gendere.get(),
                "Address": self.Addresse.get(),
                "Phone": self.Phonee.get(),
                "Class": self.Classe.get()
            }

            filename = "project2.json"

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    try:
                        data = myson.load(file)
                    except myson.JSONDecodeError:
                        data = []
            else:
                data = []

            data.append(Json)

            with open(filename, "w") as file:
                myson.dump(data, file, indent=4)

            self.namee.delete(0, tk.END)
            self.Agee.delete(0, tk.END)
            self.Gendere.delete(0, tk.END)
            self.Addresse.delete(0, tk.END)
            self.Phonee.delete(0, tk.END)
            self.Classe.delete(0, tk.END)

            pyui.alert("Successfully Updated")

        button = tk.Button(win, text='Save', command=save)
        button.place(x=200, y=780)


class teacher(school):
    def __init__(self, name, age, gender, address, phone, salary, expirience, subject):
        super().__init__(name, age, gender, address, phone)
        self.salary = salary
        self.expirience = expirience  
        self.subject = subject

    def teacher_details(self):
        teacher_detailtk = tk.Label( 
            win, 
            text=f"Name : {self.name} \n Age : {self.age}\n Address : {self.address}\n "
                 f"Subject : {self.subject} \n Salary : {self.salary} \n Expirience : {self.expirience}",
            font=('italic', 'bold')
        )
        teacher_detailtk.pack()


student1 = students("samir", 18, 'Male', 'Ktm', '970360066', 12, 'science') 
win = tk.Tk()
win.geometry("900x900")
win.configure(bg="coral")

title = tk.Label(win, text='School Management System',
                  font=('italic', 20, 'italic bold'),
                  bg='coral'
                  )
title.pack()

left_frame = tk.Frame(win, bg='#248f40', height=600, width=400)
left_frame.pack(side='left', pady=10, padx=10)
left_frame.pack_propagate(False)

button_student = tk.Button(
    left_frame,
    text="Search Student",
    command=student1.search_details,
    height=3,
    width=15,
    bg="#0d9a66"
)
button_student.place(x=10, y=10)

# adding student
Add_student = tk.Button(
    left_frame,
    text="Add Student",
    command=student1.Add_student,
    height=3,
    width=15,
    bg="#0d9a66"
)
Add_student.place(x=10, y=110)

win.mainloop()

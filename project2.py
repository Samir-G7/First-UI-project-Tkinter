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
        super().__init__(name, age, gender, address, phone)

    def fee(self, paidfee):
        due = self.totalfee - paidfee
        feetk = tk.Label(win, text=f"{self.name} had paid {paidfee}, left due is {due}")
        feetk.pack()

    def search_details(self):
        search = tk.Toplevel(win)
        search.geometry('600x600')
        search.configure(bg="#258C74")

        lab = tk.Label(search, text='Enter Name of Student')
        lab.pack()

        txt = tk.Entry(search)
        txt.pack()

        def studentbutsearch():
            var = txt.get()
            with open("project2.json", "r") as file:
                data = myson.load(file)

            found = False

            for student in data:
                if var == student["Name"]:
                    det = tk.Label(
                        search,
                        text=
                        f"Name: {student['Name']}\n"
                        f"Age: {student['Age']}\n"
                        f"Gender: {student['Gender']}\n"
                        f"Address: {student['Address']}\n"
                        f"Phone: {student['Phone']}\n"
                        f"Class: {student['Class']}",
                        bg='#258C74',
                    )
                    det.pack()
                    search.title('Searching for Student')
                    found = True
                    break

            if not found:
                pyui.alert("Student not found.")

        but = tk.Button(search, text='Submit', command=studentbutsearch)
        but.pack()

    def Add_student(self):
        fah = tk.Toplevel(left_frame)
        fah.geometry('900x900')
        fah.configure(bg='white')

        name = tk.Label(fah, text="Name :")
        name.place(x=200, y=215)
        self.namee = tk.Entry(fah)
        self.namee.place(x=200, y=250)

        Age = tk.Label(fah, text="Age :")
        Age.place(x=200, y=300)
        self.Agee = tk.Entry(fah)
        self.Agee.place(x=200, y=350)

        Gender = tk.Label(fah, text="Gender :")
        Gender.place(x=200, y=400)
        self.Gendere = tk.Entry(fah)
        self.Gendere.place(x=200, y=450)

        Address = tk.Label(fah, text="Address :")
        Address.place(x=200, y=500)
        self.Addresse = tk.Entry(fah)
        self.Addresse.place(x=200, y=550)

        Phone = tk.Label(fah, text="Phone :")
        Phone.place(x=200, y=600)
        self.Phonee = tk.Entry(fah)
        self.Phonee.place(x=200, y=650)

        Class = tk.Label(fah, text="Class :")
        Class.place(x=200, y=700)
        self.Classe = tk.Entry(fah)
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

        button = tk.Button(fah, text='Save', command=save)
        button.place(x=200, y=780)


class teacher(school):
    def __init__(self, name, age, gender, address, phone, salary, expirience, subject):
        super().__init__(name, age, gender, address, phone)
        self.salary = salary
        self.expirience = expirience
        self.subject = subject

    def Add_teacher(self):
        teacherwin = tk.Toplevel(left_frame)
        teacherwin.geometry('1000x1000')
        teacherwin.configure(bg='white')

        name = tk.Label(teacherwin, text="Name :")
        name.place(x=200, y=200)
        self.namee = tk.Entry(teacherwin)
        self.namee.place(x=200, y=230)

        Age = tk.Label(teacherwin, text="Age :")
        Age.place(x=200, y=260)
        self.Agee = tk.Entry(teacherwin)
        self.Agee.place(x=200, y=290)

        Gender = tk.Label(teacherwin, text="Gender :")
        Gender.place(x=200, y=320)
        self.Gendere = tk.Entry(teacherwin)
        self.Gendere.place(x=200, y=350)

        Address = tk.Label(teacherwin, text="Address :")
        Address.place(x=200, y=380)
        self.Addresse = tk.Entry(teacherwin)
        self.Addresse.place(x=200, y=410)

        Phone = tk.Label(teacherwin, text="Phone :")
        Phone.place(x=200, y=440)
        self.Phonee = tk.Entry(teacherwin)
        self.Phonee.place(x=200, y=470)

        Salary = tk.Label(teacherwin, text="Salary :")
        Salary.place(x=200, y=500)
        self.Salary = tk.Entry(teacherwin)
        self.Salary.place(x=200, y=530)

        Expirience = tk.Label(teacherwin, text="Expirience :")
        Expirience.place(x=200, y=560)
        self.Expirience = tk.Entry(teacherwin)
        self.Expirience.place(x=200, y=590)

        Subject = tk.Label(teacherwin, text="Subject :")
        Subject.place(x=200, y=620)
        self.Subject = tk.Entry(teacherwin)
        self.Subject.place(x=200, y=650)

        def save():
            Json = {
                "Name": self.namee.get(),
                "Age": self.Agee.get(),
                "Gender": self.Gendere.get(),
                "Address": self.Addresse.get(),
                "Phone": self.Phonee.get(),
                "Salary": self.Salary.get(),
                "Expirience": self.Expirience.get(),
                "Subject": self.Subject.get()
            }

            fileteacher = "teacher_details.json"

            if os.path.exists(fileteacher):
                with open(fileteacher, "r") as file:
                    try:
                        data = myson.load(file)
                    except myson.JSONDecodeError:
                        data = []
            else:
                data = []

            data.append(Json)

            with open(fileteacher, "w") as file:
                myson.dump(data, file, indent=4)

            self.namee.delete(0, tk.END)
            self.Agee.delete(0, tk.END)
            self.Gendere.delete(0, tk.END)
            self.Addresse.delete(0, tk.END)
            self.Phonee.delete(0, tk.END)
            self.Salary.delete(0, tk.END)
            self.Expirience.delete(0, tk.END)
            self.Subject.delete(0, tk.END)

            pyui.alert("Successfully Updated")

        button = tk.Button(teacherwin, text='Save', command=save)
        button.place(x=200, y=780)

    def search_teacher(self):
        searchteacher = tk.Toplevel(win)
        searchteacher.geometry('600x600')
        searchteacher.configure(bg="#258C74")

        variable = tk.Label(searchteacher, text='Enter Name of Teacher')
        variable.pack()

        txt = tk.Entry(searchteacher)
        txt.pack()

        def teacherbutsearch():
            var = txt.get()
            with open("teacher_details.json", "r") as file:
                data = myson.load(file)

            found = False

            for Teacher in data:
                if var == Teacher["Name"]:
                    det = tk.Label(
                        searchteacher,
                        text=
                        f"Name: {Teacher['Name']}\n"
                        f"Age: {Teacher['Age']}\n"
                        f"Gender: {Teacher['Gender']}\n"
                        f"Address: {Teacher['Address']}\n"
                        f"Phone: {Teacher['Phone']}\n"
                        f"Salary: {Teacher['Salary']}\n"
                        f"Experience: {Teacher['Expirience']}\n"
                        f"Subject: {Teacher['Subject']}",
                        bg='#258C74',
                    )
                    det.pack()
                    searchteacher.title('Searching for Teacher')
                    found = True
                    break

            if not found:
                pyui.alert("Teacher not found.")

        but = tk.Button(searchteacher, text='Submit', command=teacherbutsearch)
        but.pack()


student1 = students("samir", 18, 'Male', 'Ktm', '970360066', 12, 'science')
teach = teacher("samir", 18, 'Male', 'Ktm', '970360066', 12000, 2, 'science')
win = tk.Tk()
win.geometry("900x900")
win.configure(bg="coral")

title = tk.Label(win, text='School Management System',
                  font=('italic', 20, 'italic bold'),
                  bg='coral'
                  )
title.pack()

left_frame = tk.Frame(win, bg='#248f40', height=900, width=950)
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

Add_student_btn = tk.Button(
    left_frame,
    text="Add Student",
    command=student1.Add_student,
    height=3,
    width=15,
    bg="#0d9a66"
)
Add_student_btn.place(x=10, y=110)

teacher_button = tk.Button(
    left_frame,
    text='Add Teacher',
    command=teach.Add_teacher,
    height=3,
    width=15,
    bg='red',
    font=('italic', 9, 'bold italic')
)
teacher_button.place(x=10, y=230)

search_teacher_btn = tk.Button(
    left_frame,
    text="Search Teacher",
    command=teach.search_teacher,
    height=3,
    width=15,
    bg="#0d9a66"
)
search_teacher_btn.place(x=10, y=350)
right_frame = tk.Frame(win,height = 900,width = 950,bg = 'green')
right_frame.pack(side='right', pady=10, padx=10)
right_frame.pack_propagate(False)
title_right = tk.Label(
    right_frame,
    text = 'Log In/Register Here',
    font =( 'italic',15,'bold italic'),
    bg = 'green')
title_right.pack(padx = 20,pady = 20)

username = tk.Label(
    right_frame,
    text = "Enter Your User_Name",
    bg ='green'
    )
username.place(x = 20,y=100)

usernamebut = tk.Entry(
    right_frame,
    width = 30,
    bg ='green',
    font =('arial',20),
    show ='#')
usernamebut.place(x = 210,y=100)
#---------------------------
password = tk.Label(
    right_frame,
    text = "Enter Your Password :",
    bg ='green'
    )
password.place(x = 20,y=150)

passwordbut = tk.Entry(
    right_frame,
    width = 30,
    bg ='green',
    show ='*',
    font =('arial',20))
passwordbut.place(x = 210,y=150)
#-----------------------
log = tk.Button(right_frame,text="Log in ",bg = 'green')
register = tk.Label(
    right_frame,
    font=('bold'),
    height = 100,
    width =100,
    text = 'Register')
register.pack(padx =210,pady=400)

registerentry = tk.Entry(right_frame,width =25,
                        bg ='green',
                        font=('arial',20))
registerentry.pack()


win.mainloop()

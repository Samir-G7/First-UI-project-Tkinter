import tkinter as tk
import pyautogui as pyui
import json as myson
class school :
    def __init__(self,name,age,gender,address,phone):
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

    def student_details(self):
         pyui.alert (f"Name : {self.name}\nAge : {self.age}\nGender : {self.gender}\n"
                 f"Address : {self.address}\nContact : {self.phone}\n"
                 f"Class : {self.room}"
        )
    def Add_student(self):
        name = tk.Label(win, text="Name :")
        name.place(x=200, y=215)
        namee = tk.Entry(win)
        namee.place(x=200, y=250)

        # for age
        Age = tk.Label(win, text="Age :")
        Age.place(x=200, y=300)
        Agee = tk.Entry(win)
        Agee.place(x=200, y=350)

        # gender
        Gender = tk.Label(win, text="Gender :")
        Gender.place(x=200, y=400)
        Gendere = tk.Entry(win)
        Gendere.place(x=200, y=450)

        # for address
        Address = tk.Label(win, text="Address :")
        Address.place(x=200, y=500)
        Addresse = tk.Entry(win)
        Addresse.place(x=200, y=550)

        # for contact
        Phone = tk.Label(win, text="Phone :")
        Phone.place(x=200, y=600)
        Phonee = tk.Entry(win)
        Phonee.place(x=200, y=650)

        # for class
        Class = tk.Label(win, text="Class :")
        Class.place(x=200, y=700)
        Classe = tk.Entry(win)
        Classe.place(x=200, y=750)

        def save():
            Json = {
                'Name': namee.get(),
                'Age': Agee.get(),
                'Gender': Gendere.get(),
                'Address': Addresse.get(),
                'Phone': Phonee.get(),
                'Class': Classe.get()
            }

            with open('project2.json', 'w') as f:
                myson.dump(Json, f, indent=2)

            pyui.alert("Successfully Updated")

        button = tk.Button(win, text='Save', command=save)
        button.place(x=200, y=780)

class teacher(school):
    def __init__(self,name,age,gender,address,phone,salary,expirience,subject) :
        super().__init__(name,age,gender,address,phone) 
        self.salary = salary 
        self.expirince  = expirience
        self.subject = subject 

    def teacher_details(self):
        teacher_detailtk = tk.label(
            text=f"Name : {self.name} \n Age : {self.age}\n Address : {self.address}\n Subject : {self.subject} \n Salary : {self.salary} \n Expirience : {self.expirience}",
            font = ('italic','bold')
            )  
student1 = students("samir",18,'Male','Ktm',970360066,12,'science')
win = tk.Tk()
win.geometry('900x600')
win.configure(bg="coral")
title = tk.Label(win,text = 'School Management System',
                 font =('italic',20,'italic bold'),
                 bg='coral'
                 )
title.pack()
left_frame = tk.Frame(win,bg='#248f40',height = 600,width = 400)
left_frame.pack(side='left',pady=10,padx=10)
left_frame.pack_propagate(False)
button_student = tk.Button(
    left_frame,
    text="Student",
    command=student1.student_details,
    height = 3,
    width = 15,
    bg = "#0d9a66"
)

button_student.place(x=10,y=10)
#adding student 
Add_student = tk.Button(
    left_frame,
    text="Add Student",
    command=student1.Add_student,
    height = 3,
    width = 15,
    bg = "#0d9a66"
)
Add_student.place(x=10,y=110)


win.mainloop()
        
    
    


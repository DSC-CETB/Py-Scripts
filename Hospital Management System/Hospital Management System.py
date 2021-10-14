from tkinter import *
import mysql.connector as ms

# CONNECT TO DATABASE
db = ms.connect(user="root", password="aryan11", host="localhost",
database="HospitalManagementSystem")
cursor = db.cursor(buffered=True)


class HomePage:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.titleLabel = Label(self.master,
        text="HOSPITAL MANAGEMENT SYSTEM",
        font=("Arial", 28),
        bg="black",
        fg="white")
        self.titleLabel.grid(row=0, column=0, columnspan=4)
        self.optionLabel = Label(self.master,
        text="What do you want to do?",
        font=("Arial", 20),
        bg="black",
        fg="white")
        self.optionLabel.grid(row=2, column=0, columnspan=4)
        self.doctorBtn = Button(self.master, text="Doctor Records",
        command=self.doctor_table)
        self.doctorBtn.grid(row=12, column=2)
        self.patientBtn = Button(self.master, text="Patient Records",
        command=self.patient_table)
        self.patientBtn.grid(row=12, column=1)
        self.frame.grid(row=0, column=0, sticky="W")

    def patient_table(self):
        self.newWindow = Toplevel(self.master)
        self.app = PatientBuffer(self.newWindow)
    
    def doctor_table(self):
        self.newWindow = Toplevel(self.master)
        self.app = DoctorBuffer(self.newWindow)


class PatientBuffer:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.titleLabel = Label(self.master,
        text="Patient Table Options",
        font=("Arial", 28),
        bg="black",
        fg="white")
        self.titleLabel.grid(row=0, column=0, columnspan=4)
        self.add_rec_btn = Button(self.master, text="Add Patient Records",
        command=self.add_record)
        self.add_rec_btn.grid(row=6, column=0)
        self.del_rec_btn = Button(self.master, text="Delete Patient Records",
        command=self.del_record)
        self.del_rec_btn.grid(row=6, column=1)
        self.view_rec_btn = Button(self.master, text="View Patient Records",
        command=self.view_record)
        self.view_rec_btn.grid(row=6, column=2)
        self.frame.grid(row=0, column=0, sticky="W")
    
    def add_record(self):
        self.newWindow = Toplevel(self.master)
        self.app = PatientAddRecord(self.newWindow)
    
    def del_record(self):
        self.newWindow = Toplevel(self.master)
        self.app = PatientDeleteRecord(self.newWindow)
    
    def view_record(self):
        self.newWindow = Toplevel(self.master)
        self.app = PatientViewRecord(self.newWindow)


class PatientAddRecord:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text="Quit", command=self.close_window)
        # CREATING WIDGETS
        self.Patient_id = Entry(self.master, width=30)
        self.Patient_id.grid(row=1, column=1, padx=20, pady=20)
        self.P_name = Entry(self.master, width=30)
        self.P_name.grid(row=2, column=1, padx=20, pady=20)
        self.Age = Entry(self.master, width=30)
        self.Age.grid(row=3, column=1, padx=20, pady=20)
        self.Phone_no = Entry(self.master, width=30)
        self.Phone_no.grid(row=4, column=1, padx=20, pady=20)
        self.Disease = Entry(self.master, width=30)
        self.Disease.grid(row=5, column=1, padx=20, pady=20)
        self.Room_no = Entry(self.master, width=30)
        self.Room_no.grid(row=6, column=1, padx=20, pady=20)
        # Create Text Box Labels
        self.Patient_id_lbl = Label(self.master, text="Patient_id")
        self.Patient_id_lbl.grid(row=1, column=0)
        self.P_name_lbl = Label(self.master, text="P_name")
        self.P_name_lbl.grid(row=2, column=0)
        self.Age_lbl = Label(self.master, text="Age")
        self.Age_lbl.grid(row=3, column=0)
        self.Phone_no_lbl = Label(self.master, text="Phone_no")
        self.Phone_no_lbl.grid(row=4, column=0)
        self.Disease_lbl = Label(self.master, text="Disease")
        self.Disease_lbl.grid(row=5, column=0)
        self.Room_no_lbl = Label(self.master, text="Room_no")
        self.Room_no_lbl.grid(row=6, column=0)
        # Create submit Button
        self.submit_btn = Button(self.master, text="Add record to Database",
        command=self.submit)
        self.submit_btn.grid(row=7, column=1, columnspan=2, pady=10, padx=10)
        self.button1.grid(row=8, column=1, columnspan=2, pady=2, padx=10)
        self.frame.grid(row=0, column=0, sticky="W")
 
    def submit(self):
        # GET VALUES
        self.patient_id = self.Patient_id.get()
        self.p_name = self.P_name.get()
        self.age = self.Age.get()
        self.phone_no = self.Phone_no.get()
        self.disease = self.Disease.get()
        self.room_no = self.Room_no.get()
        # INSERT VALUES
        query = "INSERT INTO Patient VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (self.patient_id, self.p_name, self.age, self.phone_no,
        self.disease, self.room_no))
        # Commit changes
        db.commit()
    def close_window(self):
        self.master.destroy()
    

class PatientDeleteRecord:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Patient_id = Entry(self.master, width=30)
        self.Patient_id.grid(row=1, column=1, padx=20, pady=20)
        self.Patient_id_lbl = Label(self.master, text="Patient_id")
        self.Patient_id_lbl.grid(row=1, column=0)
        self.delete_btn = Button(self.master, text="Delete", command=self.delete)
        self.delete_btn.grid(row=2, column=0)
        self.frame.grid(row=0, column=0)
    def delete(self):
        # GET VALUES
        self.patient_id = self.Patient_id.get()
        cursor.execute("DELETE FROM Patient WHERE Patient_id='{}'".format(self.patient_id))
        # Commit changes
        db.commit()


class PatientViewRecord:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.view_btn = Button(self.master, text="View", command=self.viewer)
        self.view_btn.grid(row=0, column=0)
        self.Patient_id_lbl = Label(self.master, text="Patient_id")
        self.Patient_id_lbl.grid(row=4, column=0)
        self.P_name_lbl = Label(self.master, text="P_name")
        self.P_name_lbl.grid(row=4, column=1)
        self.Age_lbl = Label(self.master, text="Age")
        self.Age_lbl.grid(row=4, column=2)
        self.Phone_no_lbl = Label(self.master, text="Phone_no")
        self.Phone_no_lbl.grid(row=4, column=3)
        self.Disease_lbl = Label(self.master, text="Disease")
        self.Disease_lbl.grid(row=4, column=4)
        self.Room_no_lbl = Label(self.master, text="Room_no")
        self.Room_no_lbl.grid(row=4, column=5)
    def viewer(self):
        cursor.execute("SELECT * FROM Patient")
        records = cursor.fetchall()
        s = ""
        for i in range(len(records)):
            for j in range(6):
                s = s + str(records[i][j]) + "\n"
                patient_lbl = Label(self.master, text=s)
                patient_lbl.grid(row=(i+7+i), column=j)
                s = ""


class DoctorBuffer:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.titleLabel = Label(self.master,
        text="Doctor Table Options",
        font=("Arial", 28),
        bg="black",
        fg="white")
        self.titleLabel.grid(row=0, column=0, columnspan=4)
        self.add_rec_btn = Button(self.master, text="Register Doctor Details",
        command=self.add_record)
        self.add_rec_btn.grid(row=6, column=0)
        self.del_rec_btn = Button(self.master, text="Delete Doctor Details",
        command=self.del_record)
        self.del_rec_btn.grid(row=6, column=1)
        self.view_rec_btn = Button(self.master, text="View Doctor Details",
        command=self.view_record)
        self.view_rec_btn.grid(row=6, column=2)
        self.frame.grid(row=0, column=0, sticky="W")
    def add_record(self):
        self.newWindow = Toplevel(self.master)
        self.app = DoctorAddRecord(self.newWindow)
    def del_record(self):
        self.newWindow = Toplevel(self.master)
        self.app = DoctorDeleteRecord(self.newWindow)
    def view_record(self):
        self.newWindow = Toplevel(self.master)
        self.app = DoctorViewRecord(self.newWindow)

class DoctorAddRecord:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        # CREATING WIDGETS
        self.Doc_id = Entry(self.master, width=30)
        self.Doc_id.grid(row=0, column=1, padx=20, pady=20)
        self.Doc_name = Entry(self.master, width=30)
        self.Doc_name.grid(row=1, column=1, padx=20, pady=20)
        self.Age = Entry(self.master, width=30)
        self.Age.grid(row=2, column=1, padx=20, pady=20)
        self.Phone_no = Entry(self.master, width=30)
        self.Phone_no.grid(row=3, column=1, padx=20, pady=20)
        self.Department = Entry(self.master, width=30)
        self.Department.grid(row=4, column=1, padx=20, pady=20)
        self.ConsultingRoom = Entry(self.master, width=30)
        self.ConsultingRoom.grid(row=5, column=1, padx=20, pady=20)
        self.Doc_id_lbl = Label(self.master, text="Doc_id")
        self.Doc_id_lbl.grid(row=0, column=0)
        self.Doc_name_lbl = Label(self.master, text="Doc_name")
        self.Doc_name_lbl.grid(row=1, column=0)
        self.Age_lbl = Label(self.master, text="Age")
        self.Age_lbl.grid(row=2, column=0)
        self.Phone_no_lbl = Label(self.master, text="Phone_no")
        self.Phone_no_lbl.grid(row=3, column=0)
        self.Department_lbl = Label(self.master, text="Department")
        self.Department_lbl.grid(row=4, column=0)
        self.ConsultingRoom_lbl = Label(self.master, text="ConsultingRoom")
        self.ConsultingRoom_lbl.grid(row=5, column=0)
        # Create submit Button
        self.submit_btn = Button(self.master, text="Add record to Database",
        command=self.submit)
        self.submit_btn.grid(row=7, column=1, columnspan=2, pady=10, padx=10)
        self.frame.grid(row=0, column=0, sticky="W")
    def submit(self):
        # GET VALUES
        self.Doc_id = self.Doc_id.get()
        self.Doc_name = self.Doc_name.get()
        self.Age = self.Age.get()
        self.Phone_no = self.Phone_no.get()
        self.Department = self.Department.get()
        self.ConsultingRoom = self.ConsultingRoom.get()
        # INSERT VALUES
        query = "INSERT INTO Doctor VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (self.Doc_id, self.Doc_name, self.Age, self.Phone_no,
        self.Department, self.ConsultingRoom))
        # Commit changes
        db.commit()

class DoctorViewRecord:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Doc_id_lbl = Label(self.master, text="Doc_id")
        self.Doc_id_lbl.grid(row=4, column=0)
        self.Doc_name_lbl = Label(self.master, text="Doc_name")
        self.Doc_name_lbl.grid(row=4, column=1)
        self.Age_lbl = Label(self.master, text="Age")
        self.Age_lbl.grid(row=4, column=2)
        self.Phone_no_lbl = Label(self.master, text="Phone_no")
        self.Phone_no_lbl.grid(row=4, column=3)
        self.Department_lbl = Label(self.master, text="Department")
        self.Department_lbl.grid(row=4, column=4)
        self.ConsultingRoom_lbl = Label(self.master, text="ConsultingRoom")
        self.ConsultingRoom_lbl.grid(row=4, column=5)
        self.viewBtn = Button(self.master, text="View Records",
        command=self.view_btn)
        self.viewBtn.grid(row=0, column=0)
        self.frame.grid(row=0, column=0)
    def view_btn(self):
        cursor.execute("SELECT * FROM Doctor")
        records = cursor.fetchall()
        s = ""
        for i in range(len(records)):
            for j in range(6):
                s = s + str(records[i][j]) + "\n"
                self.patient_lbl = Label(self.master, text=s)
                self.patient_lbl.grid(row=(i+i+7), column=j)
                s = ""

class DoctorDeleteRecord:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Doc_id = Entry(self.master, width=30)
        self.Doc_id.grid(row=1, column=1, padx=20, pady=20)
        self.Doc_id_lbl = Label(self.master, text="Patient_id")
        self.Doc_id_lbl.grid(row=1, column=0)
        self.delete_btn = Button(self.master, text="Delete", command=self.delete)
        self.delete_btn.grid(row=2, column=0)
        self.frame.grid(row=0, column=0)
    def delete(self):
        # GET VALUES
        self.doc_id = self.Doc_id.get()
        cursor.execute("DELETE FROM Doctor WHERE Doctor_id='{}'".format(self.doc_id))
        # Commit changes
        db.commit()

def main():
    root = Tk()
    app = HomePage(root)
    root.mainloop()
if __name__ == '__main__':
    main()

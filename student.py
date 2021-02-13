## We have to type of packages to access database one is sqlite3 that is used for minor amount of data and one is phpmysql that is for large amount of data
from tkinter import *
from tkinter import ttk ## Provide combo box
from tkinter import messagebox
import pymysql
import re
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.top = Frame(root, height=50, bg = "white")
        self.top.pack(fill=X)
        title = Label(self.top, text = "Student Management System", bd = 10, relief = GROOVE, font = ("times nw roman", 40, "bold"), bg = "#ee7600", fg = "#0715cd")
        title.pack(side = TOP, fill = X)
        self.top_image = PhotoImage(file ='icons/student.png')
        self.top_image_label = Label(self.top, image = self.top_image)
        self.top_image_label.place(x=30, y=10)


        

        ## All database variables................................
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()




        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "#7fe5f0")
        Manage_Frame.place(x = 20, y = 100, width = 450, height = 580)
        m_title = Label(Manage_Frame, text = "Manage Students", bg = "#7fe5f0", fg = "black", font = ("times new roman", 30, "bold"))
        m_title.grid(row = 0, columnspan = 2, pady = 20)



        def validate_roll_no(roll_no):
            if roll_no.isdigit() or roll_no == "":
                return True
            else:
                messagebox.showerror("Warning", "Only digits are allowed", icon = "warning")
                return False


        lbl_roll = Label(Manage_Frame, text = "Roll_No", bg = "#7fe5f0", fg = "blue", font = ("times new roman", 20, "bold"))
        lbl_roll.grid(row = 1, column = 0, pady = 10, padx = 20, sticky = "w")
        txt_Roll = Entry(Manage_Frame, textvariable = self.Roll_No_var, font = ("times new roman", 15, "bold"), bd = 5, relief = GROOVE)
        txt_Roll.grid(row = 1, column = 1, pady = 10, padx = 20, sticky = "w")
        valid_roll_no = Manage_Frame.register(validate_roll_no)
        txt_Roll.config(validate="key", validatecommand=(valid_roll_no, "%P"))




        lbl_name = Label(Manage_Frame, text="Name", bg="#7fe5f0", fg="blue", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable = self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")







        lbl_Email = Label(Manage_Frame, text="Email", bg="#7fe5f0", fg="blue", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable = self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")











        lbl_Gender = Label(Manage_Frame, text="Gender", bg="#7fe5f0", fg="blue", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable = self.gender_var, font = ("times new roman", 13 , "bold"), state = "readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row = 4, column = 1, padx = 20, pady = 10)






        def validate_phone(phone_no):
            if phone_no.isdigit() or phone_no == "":
                return True

            else:
                messagebox.showerror("Warning", "Only digits are allowed", icon = "warning")
                return False
        lbl_Contact = Label(Manage_Frame, text="Contact_No", bg="#7fe5f0", fg="blue", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable = self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE )
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        valid_phoneno = Manage_Frame.register(validate_phone)
        txt_Contact.config(validate="key", validatecommand=(valid_phoneno, "%P"))






        lbl_Dob = Label(Manage_Frame, text="D.O.B", bg="#7fe5f0", fg="blue", font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_Dob = Entry(Manage_Frame,  textvariable = self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")





        lbl_Address = Label(Manage_Frame, text="Address", bg="#7fe5f0", fg="Blue", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width = 30, height = 4, font = ("", 10))
        self.txt_Address.grid(row = 7, column = 1, padx=  20, pady = 10, sticky = W) ## we have no textvariable attribute in textfield
        # self.txt_Address.insert(1.0, "Enter your address")
        # self.txt_Address.bind("<FocusIn>", lambda args: self.txt_Address.delete(1.0, 'end'))


        ## Button Frame...............................
        btn_Frame = Frame(Manage_Frame,  relief=RIDGE, bg="#7fe5f0")
        btn_Frame.place(x=15, y=500, width=420)
        Addbtn = Button(btn_Frame, text = "Add", width = 10, bg = "#e8000d", fg = "white", command = self.add_students).grid(row = 0, column = 0, padx = 10, pady = 30)
        updatebtn = Button(btn_Frame, text="Update", width=10, bg = "#e8000d", fg = "white", command = self.update).grid(row=0, column=1, padx=10, pady=30)
        deletebtn = Button(btn_Frame, text="Delete", width=10, bg = "#e8000d", fg = "white", command = self.delete).grid(row=0, column=2, padx=10, pady=30)
        Clearbtn = Button(btn_Frame, text="Clear", width=10, bg = "#e8000d" , fg = "white", command = self.clear).grid(row=0, column=3, padx=10, pady=30)


        ## Details Frame................................
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#7fe5f0")
        Detail_Frame.place(x=500, y=100, width=800, height=560)
        lbl_search = Label(Detail_Frame, text="Search By ", bg="#7fe5f0", fg="black", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(Detail_Frame, textvariable = self.search_by, width = 10, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        txt_Search = Entry(Detail_Frame, textvariable = self.search_txt, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, bg = "#2c1608", fg = "white", command = self.search_data).grid(row=0, column=3, padx=10, pady=30)
        showallbtn = Button(Detail_Frame, text="Show All", width=10, bg = "#2c1608", fg = "white", command = self.fetch_data).grid(row=0, column=4, padx=10, pady=30)

        ##Table Frame.............................
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="Crimson")
        Table_Frame.place(x=10, y=70, width=760, height=470)
        scroll_x = Scrollbar(Table_Frame, orient = HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns = ("roll", "name", "email", "gender", "contact", "dob", "Address"),
                                          xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text = "Roll_No")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width = 100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.pack(fill = BOTH, expand = 1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()





    def validate_email(self, email):
        match = re.match("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email)
        if (match) != None:
            return True
        else:
            messagebox.showerror("Error", "Email address is not valid", icon = "warning")





    def add_students(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='student_management')
        cur = con.cursor()

        if self.Roll_No_var.get() and self.name_var.get() and self.email_var.get() and self.gender_var.get() \
                and self.contact_var.get() and self.dob_var.get() and self.txt_Address.get(1.0, 'end-1c') != "":
            if (self.email_var.get() != ""):
                try:
                    cur.execute("insert into students values (%s, %s, %s, %s, %s, %s, %s)",(self.Roll_No_var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.txt_Address.get('1.0',END)
                                                                                    ))
                    status = self.validate_email(self.email_var.get())
                    if (status):
                        if (len(self.contact_var.get()) != 10):
                            messagebox.showerror("Warning", "Please enter 10 digit phone number", icon = "warning")
                        else:
                            con.commit()
                            self.fetch_data()
                            self.clear()
                            con.close()
                            messagebox.showinfo("Success", "Student Record Added")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "All fields are required", icon = "warning")

    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='student_management')
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values = row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END )
    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])
    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='student_management')
        cur = con.cursor()

        if self.Roll_No_var.get() and self.name_var.get() and self.email_var.get() and self.gender_var.get()\
                and self.contact_var.get() and self.dob_var.get() and self.txt_Address.get(1.0, 'end-1c') != "":
            if (self.email_var.get() != ""):
                try:
                    cur.execute("update students set name = %s, email = %s, gender = %s, contact = %s, dob = %s, address = %s where roll_no = %s",(
                                                                                 self.name_var.get(),
                                                                                 self.email_var.get(),
                                                                                 self.gender_var.get(),
                                                                                 self.contact_var.get(),
                                                                                 self.dob_var.get(),
                                                                                 self.txt_Address.get('1.0', END),
                                                                                 self.Roll_No_var.get()
                                                                                 ))
                    status = self.validate_email(self.email_var.get())
                    if (status):
                        if (len(self.contact_var.get()) != 10):
                            messagebox.showerror("Warning", "Please enter 10 digit phone number", icon = "warning")
                        else:
                            con.commit()
                            self.fetch_data()
                            self.clear()
                            con.close()
                            messagebox.showinfo("Success", "Student Record Updated")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill all the fields", icon = "warning")

    def delete(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='student_management')
        cur = con.cursor()
        answer = messagebox.askquestion("Warning", "Are you sure that you want to delete >")
        if answer == 'yes':
            try:
                cur.execute("delete from students where roll_no = %s", self.Roll_No_var.get())
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success", "Student Record Deleted")
            except Exception as e:
                messagebox.showerror("Error", str(e))




    def search_data(self):
            con = pymysql.connect(host='localhost', user='root', password='', database='student_management')
            cur = con.cursor()
            cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            if self.search_txt.get() == "":
                messagebox.showerror("Error", "Value is required", icon = "warning")
            else:
             rows = cur.fetchall()
             if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
             elif len(rows) == 0:
                 messagebox.showinfo("Warning", "Student Record doesn't Exist", icon = "warning")



root = Tk()
ob = Student(root)
root.mainloop()




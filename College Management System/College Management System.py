import tkinter as tk
from tkinter import*
from tkinter.ttk import *
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
import random
import sqlite3,sys
import webbrowser as wb 
import webbrowser


window = Tk()
window.title("College Management System")
window.geometry("740x400")
window.configure(background='white')
label = Label(text="Welcome To College Management System", bg="white",font=('Algerian',18))
label.place(relx=0.18,rely=0.1)


def College_Management_System():
    window.destroy()
    def Exit():
        exit()

    def Principal_Field():

        window3 = Tk()
        window3.title("College Management System")
        window3.geometry("700x400")
        window3.configure(background="white")
        label = Label(text="Principal Window",bg="white",font=('Algerian',20))
        label.place(relx=0.34,rely=0.1)

        def Search_online():
            window3.destroy()
            window = Tk()
            window.title("Chrome Search Bar")
            window.geometry("740x400")
            window.configure(background='white')
            label = Label(text="TYPE AND SEARCH FROM CHROME", bg="white",font=('Algerian',18))
            label.place(relx=0.25,rely=0.1)

            def search():
                text = e1.get()
                url="https://www.google.com/search?q="
                search_url=url+text
                webbrowser.open(search_url)

            Label1 = Label(text="Type Something :",bg="white",font=('Arail',11))
            Label1.place(relx=0.27,rely=0.36)


            e1=Entry(bg='gray')
            e1.place(relx=0.49,rely=0.37)

            b1= Button(text = "Search",fg="white", command= search ,activeforeground = "Black",activebackground = "white",pady=4, height=1, width=14) 
            b1.configure(background='black')
            b1.place(relx=0.41,rely=0.53)


            window.mainloop()

        def Main():
            window3.destroy()

            def connection():
                try:
                    conn=sqlite3.connect("student.db")
                except:
                    print("cannot connect to the database")
                return conn    


            def verifier():
                a=b=c=d=e=f=0

                if not book_no.get():
                    t1.insert(END,"<>Book no is required<>\n")
                    a=1
                if not book_name.get():
                    t1.insert(END,"<>Book name is required<>\n")
                    b=1
                if not department.get():
                    t1.insert(END,"<>Depertment name is required<>\n")
                    c=1
                if not semester.get():
                    t1.insert(END,"<>Semester is requrired<>\n")
                    d=1

                if a==1 or b==1 or c==1 or d==1 :
                    return 1
                else:
                    return 0


            def add_book():
                ret=verifier()
                if ret==0:
                    conn=connection()
                    cur=conn.cursor()
                    cur.execute("CREATE TABLE IF NOT EXISTS BOOKS(BOOK_NO INTEGER,BOOK_NAME TEXT,DEPARTMENT TEXT,SEMESTER INTEGER)")
                    cur.execute("insert into BOOKS values(?,?,?,?)",(int(book_no.get()),book_name.get(),department.get(),int(semester.get())))
                    conn.commit()
                    conn.close()
                    t1.insert(END,"ADDED SUCCESSFULLY\n")


            def view_books():
                conn=connection()
                cur=conn.cursor()
                cur.execute("select * from BOOKS")
                data=cur.fetchall()
                conn.close()
                for i in data:
                    t1.insert(END,str(i)+"\n")


            def delete_book():
                ret=verifier()
                if ret==0:
                    conn=connection()
                    cur=conn.cursor()
                    cur.execute("DELETE FROM BOOKS WHERE BOOK_NO=?",(int(book_no.get()),))
                    conn.commit()
                    conn.close()
                    t1.insert(END,"BOOK HAS BEEN DELETED\n")

            def update_book():
                ret=verifier()
                if ret==0:
                    conn=connection()
                    cur=conn.cursor()
                    cur.execute("UPDATE BOOKS SET BOOK_NO=?,BOOK_NAME=?,DEPARTMENT=?,SEMESTER=?",(int(book_no.get()),book_name.get(),department.get(),int(semester.get())))
                    conn.commit()
                    conn.close()
                    t1.insert(END,"UPDATED SUCCESSFULLY\n")


            def clse():
                sys.exit() 


            if __name__=="__main__":
                root=Tk()
                root.title("Student Current Courses")

                book_no=StringVar()   
                book_name=StringVar()
                department=StringVar()
                semester=StringVar()
                

                label1=Label(root,text="Book No     :", bg='black', fg='white', font=('Arail',10))
                label1.place(x=0,y=0)

                label2=Label(root,text="Book Name:", bg='black', fg='white', font=('Arail',10))
                label2.place(x=0,y=30)

                label3=Label(root,text="Department:", bg='black', fg='white', font=('Arail',10))
                label3.place(x=0,y=60)

                label4=Label(root,text="Semester   :", bg='black', fg='white', font=('Arail',10))
                label4.place(x=0,y=90)


                e1=Entry(root,textvariable=book_no)
                e1.place(x=120,y=0)

                e2=Entry(root,textvariable=book_name)
                e2.place(x=120,y=30)

                e3=Entry(root,textvariable=department)
                e3.place(x=120,y=60)

                e4=Entry(root,textvariable=semester)
                e4.place(x=120,y=90)
                

                
                t1=Text(root,width=80,height=20)
                t1.grid(row=10,column=1)

                label = Label(text="Book Records",bg="white",font=('Algerian',18))
                label.place(relx=0.04,rely=0.45)


                b1= Button(text = "ADD BOOKS",fg="white", command= add_book ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
                b1.configure(background='black')
                b1.grid(row=11,column=0)

                b2= Button(text = "VIEW ALL BOOKS",fg="white", command= view_books ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
                b2.configure(background='black')
                b2.grid(row=12,column=0)

                b3= Button(text = "DELETE BOOK",fg="white", command= delete_book ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
                b3.configure(background='black')
                b3.grid(row=13,column=0)

                b4= Button(text = "UPDATE INFO",fg="white", command= update_book ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
                b4.configure(background='black')
                b4.grid(row=14,column=0)

                b5= Button(text = "CLOSE",fg="white", command= clse ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
                b5.configure(background='black')
                b5.grid(row=15,column=0)

                root.mainloop()




        button1= Button(text = "Search Online",fg="white",command= Search_online ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=13)
        button1.configure(background='black')
        button1.place(relx=0.43,rely=0.30)

        button2= Button(text = "Courses",fg="white" ,command= Main,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=13)
        button2.configure(background='black')
        button2.place(relx=0.43,rely=0.50)

        button3= Button(text = "Exit",fg="white",command=Exit ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=13)
        button3.configure(background='black')
        button3.place(relx=0.43,rely=0.70)

        mainloop()

    def Admin_Field():

        def connection():
            try:
                conn=sqlite3.connect("student.db")
            except:
                print("cannot connect to the database")
            return conn    


        def verifier():
            a=b=c=d=e=f=0
            if not student_name.get():
                t1.insert(END,"<>Student name is required<>\n")
                a=1
            if not roll_no.get():
                t1.insert(END,"<>Roll no is required<>\n")
                b=1
            if not branch.get():
                t1.insert(END,"<>Branch is required<>\n")
                c=1
            if not phone.get():
                t1.insert(END,"<>Phone number is requrired<>\n")
                d=1
            if not father.get():
                t1.insert(END,"<>Father name is required<>\n")
                e=1
            if not address.get():
                t1.insert(END,"<>Address is Required<>\n")
                f=1
            if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
                return 1
            else:
                return 0


        def add_student():
                    ret=verifier()
                    if ret==0:
                        conn=connection()
                        cur=conn.cursor()
                        cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO INTEGER,BRANCH TEXT,PHONE_NO INTEGER,FATHER TEXT,ADDRESS TEXT)")
                        cur.execute("insert into STUDENTS values(?,?,?,?,?,?)",(student_name.get(),int(roll_no.get()),branch.get(),int(phone.get()),father.get(),address.get()))
                        conn.commit()
                        conn.close()
                        t1.insert(END,"ADDED SUCCESSFULLY\n")


        def view_student():
            conn=connection()
            cur=conn.cursor()
            cur.execute("select * from STUDENTS")
            data=cur.fetchall()
            conn.close()
            for i in data:
                t1.insert(END,str(i)+"\n")


        def delete_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=?",(int(roll_no.get()),))
                conn.commit()
                conn.close()
                t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

        def update_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("UPDATE STUDENTS SET NAME=?,ROLL_NO=?,BRANCH=?,PHONE_NO=?,FATHER=?,ADDRESS=? where ROLL_NO=?",(student_name.get(),int(roll_no.get()),branch.get(),int(phone.get()),father.get(),address.get(),int(roll_no.get())))
                conn.commit()
                conn.close()
                t1.insert(END,"UPDATED SUCCESSFULLY\n")


        def clse():
            sys.exit() 


        if __name__=="__main__":
            root=Tk()
            root.title("Student Record Management System")
            
            student_name=StringVar()
            roll_no=StringVar()
            branch=StringVar()
            phone=StringVar()
            father=StringVar()
            address=StringVar()
            
            label1=Label(root,text="Student Name:", bg='black', fg='white', font=('Arail',10))
            label1.place(x=0,y=0)

            label2=Label(root,text="Roll No          :", bg='black', fg='white', font=('Arail',10))
            label2.place(x=0,y=30)

            label3=Label(root,text="Branch          :", bg='black', fg='white', font=('Arail',10))
            label3.place(x=0,y=60)

            label4=Label(root,text="Phone Number:", bg='black', fg='white', font=('Arail',10))
            label4.place(x=0,y=90)

            label5=Label(root,text="Father Name  :", bg='black', fg='white', font=('Arail',10))
            label5.place(x=0,y=120)

            label6=Label(root,text="Address         :",bg='black', fg='white', font=('Arail',10))
            label6.place(x=0,y=150)

            e1=Entry(root,textvariable=student_name)
            e1.place(x=120,y=0)

            e2=Entry(root,textvariable=roll_no)
            e2.place(x=120,y=30)

            e3=Entry(root,textvariable=branch)
            e3.place(x=120,y=60)

            e4=Entry(root,textvariable=phone)
            e4.place(x=120,y=90)
            
            e5=Entry(root,textvariable=father)
            e5.place(x=120,y=120)

            e6=Entry(root,textvariable=address)
            e6.place(x=120,y=150)
            
            t1=Text(root,width=80,height=20)
            t1.grid(row=10,column=1)

            label = Label(text="Student Records",bg="white",font=('Algerian',18))
            label.place(relx=0.04,rely=0.45)
        

            b1= Button(text = "ADD STUDENT",fg="white", command= add_student ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
            b1.configure(background='black')
            b1.grid(row=11,column=0)

            b2= Button(text = "VIEW ALL STUDENT",fg="white", command= view_student ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
            b2.configure(background='black')
            b2.grid(row=12,column=0)

            b3= Button(text = "DELETE STUDENT",fg="white", command= delete_student ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
            b3.configure(background='black')
            b3.grid(row=13,column=0)

            b4= Button(text = "UPDATE INFO",fg="white", command= update_student ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
            b4.configure(background='black')
            b4.grid(row=14,column=0)

            b5= Button(text = "CLOSE",fg="white", command= clse ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
            b5.configure(background='black')
            b5.grid(row=15,column=0)

            root.mainloop()


    def Student_Field():

        window4 = Tk()
        window4.title("College Management System")
        window4.geometry("700x400")
        window4.configure(background="white")
        label = Label(text="Student Window",bg="white",font=('Algerian',20))
        label.place(relx=0.34,rely=0.1)
        
        def Main1():
            window4.destroy()
            def connection():
                try:
                    conn=sqlite3.connect("student.db")
                except:
                    print("cannot connect to the database")
                return conn    


            def view_books():
                conn=connection()
                cur=conn.cursor()
                cur.execute("select * from BOOKS")
                data=cur.fetchall()
                conn.close()
                for i in data:
                    t1.insert(END,str(i)+"\n")


            def clse():
                sys.exit() 

            def Exit1():
                exit()


            if __name__=="__main__":
                root=Tk()
                root.title("Student Current Courses")


                label1=Label(root,text="Book No / Book Name / Department / Semester ", fg='black', font=('Arail',10))
                label1.place(x=0,y=0)

            

                t1=Text(root,width=80,height=20)
                t1.grid(row=10,column=1)

                label = Label(text="STUDENT",bg="white",font=('Algerian',22))
                label.place(relx=0.08,rely=0.22)

                label = Label(text="CURRENT",bg="white",font=('Algerian',22))
                label.place(relx=0.08,rely=0.34)

                label = Label(text="COURSES",bg="white",font=('Algerian',22))
                label.place(relx=0.08,rely=0.46)


                b2= Button(text = "VIEW ALL BOOKS",fg="white", command= view_books ,activeforeground = "Black",activebackground = "white",pady=15, height=1, width=40) 
                b2.configure(background='black')
                b2.grid(row=11,column=0)

                b5= Button(text = "CLOSE",fg="white", command= clse ,activeforeground = "Black",activebackground = "white",pady=15, height=1, width=40) 
                b5.configure(background='black')
                b5.grid(row=15,column=0)

                root.mainloop()  



        def Main2():
            window4.destroy()

            def connection():
                try:
                    conn=sqlite3.connect("student.db")
                except:
                    print("cannot connect to the database")
                return conn    


            def view_student():
                conn=connection()
                cur=conn.cursor()
                cur.execute("select * from STUDENTS")
                data=cur.fetchall()
                conn.close()
                for i in data:
                    t1.insert(END,str(i)+"\n")



            def clse():
                sys.exit() 


            if __name__=="__main__":
                root=Tk()
                root.title("Student Record Management System")


                label1=Label(root,text="Student Name/Roll No/Branch/", font=('Arail',10))
                label1.place(x=0,y=0)

                label2=Label(root,text="Phone Number/Father Name/Address", font=('Arail',10))
                label2.place(x=0,y=30)


                t1=Text(root,width=80,height=20)
                t1.grid(row=10,column=1)

                label = Label(text="All",font=('Algerian',18))
                label.place(relx=0.08,rely=0.22)

                label = Label(text="Students",font=('Algerian',18))
                label.place(relx=0.05,rely=0.34)

                label = Label(text=" Records",font=('Algerian',18))
                label.place(relx=0.05,rely=0.46)


                b2= Button(text = "VIEW ALL STUDENTS RECORD",fg="white", command= view_student ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
                b2.configure(background='black')
                b2.grid(row=12,column=0)


                b5= Button(text = "CLOSE",fg="white", command= clse ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=40) 
                b5.configure(background='black')
                b5.grid(row=15,column=0)

                root.mainloop()   

        button1= Button(text = "Students Records",fg="white",command= Main2 ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=13)
        button1.configure(background='black')
        button1.place(relx=0.43,rely=0.30)

        button2= Button(text = "Current Courses",fg="white" ,command= Main1, activeforeground = "Black",activebackground = "white",pady=5, height=1, width=13)
        button2.configure(background='black')
        button2.place(relx=0.43,rely=0.50)

        button3= Button(text = "Exit",fg="white",command=Exit ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=13)
        button3.configure(background='black')
        button3.place(relx=0.43,rely=0.70)

        mainloop()

    def Pass():
        Password_Window()

    def Password_Window():

        def Password_Check():
            principal_password = "123"  
            admin_password = "456"
            student_password = "789"
            if password_guess.get() == principal_password:
                window2.destroy()
                print("Access Granted")
                Principal_Field()
            elif password_guess.get() == admin_password:
                window2.destroy()
                print("Access Granted")
                Admin_Field()
            elif password_guess.get() == student_password:
                window2.destroy()
                Student_Field()
            else:
                messagebox.showwarning("Warning","Access Not Grated")
                window2.destroy()


        window1.destroy()

        window2 = Tk()
        window2.title("Jarvis Google Assistant")
        window2.geometry("600x350")
        window2.configure(background='white')
        label2 = Label(text="Please enter Password",bg="white",font=('Algerian',20))
        label2.place(relx=0.24,rely=0.1)

        password_text = Label(text="Password", bg='black', fg='white', font=('Arail',10) )
        password_text.place(relx=0.175,rely=0.43,height=30, width=120 )
        password_guess = tk.Entry()
        password_guess.place(relx=0.45,rely=0.43,height=30, width=200)
        #use show='*' in configure to hide password
        password_guess.configure(bg='black', fg='white')
        password_guess.focus()

        Ok_Button = Button(text='OK', command= Password_Check)
        Ok_Button.place(relx=0.4702,rely=0.689, height=35, width=57)
        Ok_Button.config(bg='black',fg='white')
        


        #Main Starter
        window1.mainloop()



    window1 = Tk()
    window1.title("College Management System")
    window1.geometry("750x400")
    window1.configure(background='white')
    label1 = Label(text="College Management System",bg ="white", font=('Algerian',18))
    label1.place(relx=0.26,rely=0.1)

    Principal = Button(text = "Principal",fg="white",command=Pass ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=15) 
    Principal.configure(background='black')
    Principal.place(relx=0.41,rely=0.30)

    Admin= Button(text = "Admin",fg="white",command=Pass, activeforeground = "Black",activebackground = "white",pady=5, height=1, width=15) 
    Admin.configure(background='black')
    Admin.place(relx=0.41,rely=0.50)

    Student = Button(text = "Student",fg="white",command=Pass,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=15) 
    Student.configure(background='black')
    Student.place(relx=0.41,rely=0.70)

    window1.mainloop()


#First Window Buttons
StartButton= Button(text = "Start",fg="white", command= College_Management_System ,activeforeground = "Black",activebackground = "white",pady=5, height=1, width=10) 
StartButton.configure(background='black')
StartButton.place(relx=0.42,rely=0.35)

ExitButton= Button(text = "Exit",fg="white", command=exit(), activeforeground = "Black",activebackground = "white",pady=5, height=1, width=10) 
ExitButton.configure(background='black')
ExitButton.place(relx=0.42,rely=0.65)

window.mainloop()
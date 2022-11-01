import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="EddyKubwimana", password="Ilove@Mother2",
                               database='ashesi_student')
cursor = mydb.cursor()
window = tk.Tk()
window.geometry('800x600')
window.title('Student portal')


def createaccount():
    name1 = username.get()
    password1 = password.get()
    sql = "INSERT INTO student (username, password) VALUES(%s, %s)"
    values = [(name1, password1)]
    cursor.executemany(sql, values)
    mydb.commit()


def getdata():
    requestbox = tk.Entry(window, bg='white', font=('arial', 12))
    name1 = username.get()
    password1 = password.get()
    name = cursor.execute(f"SELECT username FROM student where password = {password1}")
    myresult = cursor.fetchall()
    requestbox = myresult


frame = tk.Frame(window, background='white')
frame.place(height=400, width=400)
label1 = tk.Label(frame, text='username', font=('arial', 12))
label1.place(x=100, y=20, height=20, width=100)
username = tk.Entry(frame, background='white', font=('arial', 12))
username.place(x=10, y=40, height=20, width=300)
label2 = tk.Label(frame, text='password', font=('arial', 12))
label2.place(x=100, y=60, height=20, width=100)
password = tk.Entry(frame, background='white', font=('arial', 12))
password.place(x=10, y=80, height=20, width=300)
connectButton = tk.Button(frame, text='create account', font=('arial', 12), activebackground='blue',
                          command=createaccount)
connectButton.place(x=100, y=120, height=20, width=100)
conButton = tk.Button(frame, text='log in', font=('arial', 12), activebackground='blue', command=getdata)
conButton.place(x=100, y=160, height=20, width=100)

window.mainloop()



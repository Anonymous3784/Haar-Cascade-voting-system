import sqlite3
import tkinter as tk
import os
from tkinter import StringVar
root = tk.Tk()
root.title("Enter contact info")
root.geometry("500x500")
conn = sqlite3.connect('user.db')
#SS


def insertData():
    table_name = "userinfo"
    sql = 'create table if not exists ' + table_name + ' (name text, mob char(15))'
    conn.execute(sql)
    
    #insertquery = "INSERT INTO userinfo (name,mob)\values(
    



def getval(self, value):
    print(value)

filepath='./dataset'
dirlist = [ item for item in os.listdir(filepath) if os.path.isdir(os.path.join(filepath, item)) ]

variable = StringVar()
variable.set(dirlist[0]) # default value

w = tk.OptionMenu(root, variable, *dirlist, command= getval)
w.place(relx=0.5, rely=0.3, anchor='n')

EnterMob = tk.Label(root, text="Enter Mobile number", height=2,width=30)
EnterMob.place(relx=0.5, rely=0.4, anchor='n')

OTPtext = tk.Entry(root)
OTPtext.place(relx=0.5, rely=0.5, anchor='n')


btn_login = tk.Button(root, text="Add", width=45, command=insertData)
btn_login.place(relx=0.5, rely=0.6, anchor='n')

import tkinter as tk
import os
from tkinter import messagebox
import requests
from tkinter import StringVar


root = tk.Tk()
root.title("OTP verification")
root.geometry("500x500")
    
votingscreen = tk.Tk()
votingscreen.title("Voting Screen")
votingscreen.geometry("500x500")
votingscreen.withdraw()

counter=0
   
def OTPgeneration():
   OTPfile = open("OTPfile.txt","r")
   OTPfile.seek(0)
   firstline = OTPfile.readline()
   OTPfile.close()
   
   if firstline != "":
       OTPfile = open("OTPfile.txt","w")
       num=int(firstline)
       counter = int(num)+1
       OTPfile.write(str(counter)+"\n")
       OTPfile.close()
       
   else:
       OTPfile = open("OTPfile.txt","w")
       counter = 1
       OTPfile.write(str(counter)+"\n")
       OTPfile.close()

   OTPfile = open("OTPfile.txt","r")
   OTPfile.seek(0)
   firstline = OTPfile.readline()
   OTPfile.close()
   
        
def OTPverification():
   OTPfile = open("OTPfile.txt","r")
   OTPfile.seek(0)
   firstline = OTPfile.readline()
   OTPfile.close()
   num = int(firstline)
   print(num)
   if num == int(OTPtext.get()):
      OTPtext.delete(0,tk.END)
      root.withdraw()
      votingscreen.deiconify()
       
       
def sel():
   val = selection.get()
   messagebox.showinfo("You have voted to:" +val )
   print("done")
   votingscreen.withdraw()
   root.deiconify()
   
selection=StringVar()
R1 = tk.Radiobutton(votingscreen, text="ShivSena", value=1, variable="selection", command=sel)
R1.place(relx=0.2,rely=0.2,anchor='n')
R2 = tk.Radiobutton(votingscreen, text="Congress", value=2, variable="selection", command=sel)
R2.place(relx=0.2,rely=0.3,anchor='n')
R3 = tk.Radiobutton(votingscreen, text="BJP", value=3, variable="selection", command=sel)
R3.place(relx=0.17,rely=0.4,anchor='n')
R4 = tk.Radiobutton(votingscreen, text="NCP", value=4, variable="selection", command=sel)
R4.place(relx=0.17,rely=0.5,anchor='n')


EnterOTPscreen = tk.Label(root, text="OTP Varification", font=('arial', 15))
EnterOTPscreen.place(relx=0.5, rely=0.2, anchor='n')

EnterOTPLabel = tk.Label(root, text="Enter OTP to proceed", height=2,width=30)
EnterOTPLabel.place(relx=0.5, rely=0.4, anchor='n')

OTPtext = tk.Entry(root)
OTPtext.place(relx=0.5, rely=0.5, anchor='n')

btn_login = tk.Button(root, text="Verify", width=45, command=OTPverification)
btn_login.place(relx=0.5, rely=0.6, anchor='n')
OTPgeneration()

tk.mainloop()

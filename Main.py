import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
root = tk.Tk()
root.geometry('500x300')
root.maxsize(500,300)
root.minsize(500,300)
root.title('Send SMS')
root.iconbitmap('Sms.ico')

def send_sms():
        number = phone_no.get()
        messages = message.get("1.0","end-1c") 

        url = "https://http-api.d7networks.com/send"
        querystring = {
            "username":"USERNAME",
            "password":"PASSWORD",
            "from":"SENDER ID/NAME",
            "content":messages,
            "dlr-method":"POST",
            "dlr-url":"https://4ba60af1.ngrok.io/receive",
            "dlr":"yes",
            "dlr-level":"3",
            "to":number,
            }

        headers = {
                 'cache-control': "no-cache"
                 }
        response = requests.request("GET", url, headers=headers, params=querystring)
        messagebox.showinfo("Send SMS",'SMS has been sent successfully')


        






img = ImageTk.PhotoImage(Image.open('background.jpg'))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


label = Label(root,text="Bulk SMS Sender",font=('Helvetica Regular',15,'bold'))
label.place(x=180,y=9)

phone_no = Entry(root,width=20,borderwidth=0,font=('Helvetica Regular',12,'bold'))
phone_no.place(x=175,y=69)
phone_no.insert('end','phone number')

message = Text(root,height=7,width=28,borderwidth=0,font=('Helvetica Regular',12,'bold'))
message.place(x=139,y=100)
message.insert('end','Message')

send = Button(root,text="Send Message",font=('Helvetica Regular',11,'bold'),relief=RIDGE,cursor='hand2',borderwidth=0,command=send_sms)
send.place(x=200,y=245)
root.mainloop()

import base64
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

byte_icon = b'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'

byte_image = b'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'


def generate_random_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    return code

passs= generate_random_code()
print(passs)

def send_email(subject, body):
    # Email configuration
    sender_email = ''  # Your Gmail address
    sender_password = ''  # Your Gmail password or app password
    receiver_email = ''  # Receiver's email address

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Email failed to send:", str(e))

# Usage example
subject = "Passwowrd for your file"
body = f"here is your password {passs}"

send_email(subject, body)


def encrypt():
    password=code.get()
    filename_func = str(text_filename.get("1.0",'end-1c'))

    if password==passs and filename_func !="":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("440x200")
        screen1.configure(bg="#ed3833")


        with open(filename_func, "rb") as videoFile:
            text_encrypt= base64.b64encode(videoFile.read())
            op_name = str(text_filename.get("1.0","end-5c"))
            file = open(f"{op_name}.txt", "wb")
            file.write(text_encrypt)
            file.close()

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Robote 15",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=30,y=40,width=380,height=150)
        text2.insert(END,text_encrypt)

        scrollbar1= Scrollbar(screen1)
        scrollbar1.place(x=415,y=40,height=150)

        scrollbar1.configure(command=text2.yview)
        text2.configure(yscrollcommand=scrollbar1.set)

    elif password=="" or filename_func =="":
        messagebox.showerror("encryption","Select File And Input Password")
    
    elif password != passs:
        messagebox.showerror("encryption","Invalid Password")


def decrypt():
    password=code.get()
    filename_func = str(text_filename.get("1.0",'end-1c'))

    if password==passs and filename_func!="":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        with open(filename_func,"rb") as textfile:
            video_decrypt = base64.b64decode(textfile.read())
            op_name = str(text_filename.get("1.0","end-5c"))
            fh = open(f"{op_name}.mp4", "wb")
            fh.write(video_decrypt)
            fh.close()

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Robote 15",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,"Video File Created Successfully")

    elif password=="" or filename_func=="":
        messagebox.showerror("Decryption","Select file and Input Password")
    
    elif password != passs:
        messagebox.showerror("Decryption","Invalid Password")

def main_screen():

    global screen
    global text_filename
    global code
    global filename

    screen = Tk()
    screen.geometry("385x398")
    screen.title("Video Encrpyter Submitted by : Simarpreet (EN19IT301086)")

    text_filename = Text(screen,font="Robote 15",bg="white",relief=GROOVE, bd=2,width=32,height = 1.5)
    text_filename.place(x=10,y=60)

    # icon
    b1 = base64.b64decode(byte_icon)
    img1 = Image.open(io.BytesIO(b1))
    image_icon = ImageTk.PhotoImage(img1)
    screen.iconphoto(False,image_icon)

    #logo
    b = base64.b64decode(byte_image)
    img = Image.open(io.BytesIO(b))
    resize_img = img.resize((100,110))
    logo = ImageTk.PhotoImage(resize_img)
    logo_image = Label(screen,image=logo)
    logo_image.place(x=137,y=115)

    def reset():
        code.set("")
        text_filename.delete(1.0,END)

    def select_video_file():

        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                                title="Select video file",
                                                filetype=[("all video format", ".mp4"),
                                                                    ("all video format", ".flv"),
                                                                    ("all video format", ".avi"),
                                                                    ("all text format",".txt"),
                                                                                                ])
        
        text_filename.insert("1.0",filename)


    Label(text="Enter Secret Key For Encryption & Decryption",fg="black",font=("calbri",12,"bold")).place(x=10,y=225)
    
    code = StringVar()
    Entry(textvariable=code,width=20,bd=2,font=("arial",25),show="*").place(x=10,y=250)
   
    Button(text="Select File",font =("times new roman",9 ,"bold"),height="2",width=23,bg="#ed3833",fg="white",bd=2,command=select_video_file).place(x=110,y=15)
    Button(text="ENCRYPT",font =("times new roman",9 ,"bold") ,height="2",width=23,bg="#ed3833",fg="white",bd=2,command=encrypt).place(x=10,y=300)
    Button(text="DECRYPT",font =("times new roman",9 ,"bold"),height="2",width=23,bg="#00bd56",fg="white",bd=2,command=decrypt).place(x=203,y=300)
    Button(text="RESET",font =("times new roman",9 ,"bold"),height="2",width=50,bg="#1089ff",fg="white",bd=2,command=reset).place(x=12,y=350)
    
    screen.mainloop()

main_screen()
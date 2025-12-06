#-----------Check USB Software------#
import tkinter as tk
import cv2
from PIL import ImageTk, Image, ImageDraw
import subprocess
from tkinter import messagebox
import sys
#--------Check USB Software END----#

#------Home Page----#
import tkinter as tk
import cv2
from PIL import ImageTk, Image, ImageDraw
#-------Home Page END------#

#------About us------#
import tkinter
from PIL import Image, ImageTk
import webbrowser
from moviepy.editor import *
import cv2
from PIL import Image, ImageDraw
from PIL import Image

#------About us END------#

#-------Guide---------#
import tkinter
from PIL import Image, ImageTk
import webbrowser
from moviepy.editor import *
import cv2
from PIL import Image, ImageDraw
from PIL import Image
#--------Guide End-----#

#------Signup------#
from tkinter import *
from tkinter import messagebox
import ast
from PIL import ImageTk, Image, ImageDraw
import mysql.connector
import cv2
import subprocess
#------Signup END------#

#-------Login------#
from tkinter import Tk, messagebox, Frame, Button, Label, Entry, Canvas
from PIL import Image, ImageTk, ImageDraw
import mysql.connector
import cv2
import tkinter as tk
#-------Login END-----#

#--------KEY GENERATION WITH EMAIL OTP-------#
import tkinter
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets
from PIL import Image, ImageTk, ImageDraw
import cv2
import numpy as np
from tkinter import messagebox
#---------KEY GENERATION WITH EMAIL OTP END------#

#---------DISP---------#
import tkinter as tk
from tkinter import Tk, Canvas
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import mysql.connector
#--------DISP END------#

#-------USB Detection------#
import subprocess
from tkinter import Button, Canvas, Label, Tk
from PIL import Image, ImageTk
import cv2
import numpy as np
#-------USB Detection END-----#

###########-----------------About us----------------#############
def fun1(event):
        global w1
        w1 = tkinter.Toplevel()
        w1.title("About us")

        canvas = tkinter.Canvas(w1, width=1600, height=1000, bd=0, highlightthickness=0)
        canvas.pack()

        image = Image.open("purple.png")
        image = image.resize((1600, 1000))
        photo = ImageTk.PhotoImage(image)
        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image = photo
        canvas.create_image(0, 0, image=photo, anchor="nw")
    
    # Rest of the code...


        def play_video():
            video_path = "Blue Purple.mp4"
            clip = VideoFileClip(video_path).subclip(0, 10)
            resized_clip = clip.resize(height=670)

            frames = []
            for t in range(int(resized_clip.duration * resized_clip.fps)):
                frame = resized_clip.get_frame(t / resized_clip.fps)
                frames.append(frame)

            images = [ImageTk.PhotoImage(image=Image.fromarray(frame)) for frame in frames]

            video_label = tkinter.Label(w1)
            video_label.config(image=images[0])
            video_label.image = images[0]
            video_label.place(x=190, y=80)

            def update_image(idx):
                video_label.config(image=images[idx])
                video_label.image = images[idx]
                w1.after(33, lambda: update_image((idx + 1) % len(images)))

            w1.after(33, lambda: update_image(1))

        play_video()

        def open_link1(event):
            webbrowser.open("https://www.instagram.com/mr_manoj7022/")

        link_label1 = tkinter.Label(w1, text="@mr_manoj7022", fg="white", bg="#B65FCF", cursor="hand2", font=("Times new Roman", 12))
        link_label1.place(x=375, y=555)
        link_label1.bind("<Button-1>", open_link1)

        def open_link2(event):
            webbrowser.open("https://www.instagram.com/itss_vin_17/")

        link_label2 = tkinter.Label(w1, text="@itss_vin_17", fg="white", bg="#B65FCF", cursor="hand2", font=("Times new Roman", 12))
        link_label2.place(x=725, y=620)
        link_label2.bind("<Button-1>", open_link2)

        def open_link3(event):
            webbrowser.open("https://www.instagram.com/vishal_k01/")

        link_label3 = tkinter.Label(w1, text="@vishal_k01", fg="white", bg="#B65FCF", cursor="hand2", font=("Times new Roman", 12))
        link_label3.place(x=1090, y=565)
        link_label3.bind("<Button-1>", open_link3)

        label4 = tkinter.Label(w1, text="+91 7022820630", fg="white", bg="#0F52BA", cursor="hand2", font=("Times new Roman", 16))
        label4.place(x=355, y=520)

        label5 = tkinter.Label(w1, text="+91 9380338484", fg="white", bg="#0F52BA", cursor="hand2", font=("Times new Roman", 16))
        label5.place(x=695, y=585)

        label6 = tkinter.Label(w1, text="+91 6360430056", fg="white", bg="#0F52BA", cursor="hand2", font=("Times new Roman", 16))
        label6.place(x=1055, y=530)

        # Create label buttons on the canvas
        w1b1 = tkinter.Label(w1, text="<  Back")
        w1b1.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
        w1b1.bind("<Button-1>", fun1_back)

        w1b1_window = canvas.create_window(100, 100, anchor="nw", window=w1b1, width=60, height=30)

def fun1_back(event):
        w1.destroy()

###########----------ABOUT US END---------################

##########----------------Guide---------------###########
def gui(event):
        global w8
        w8 = tkinter.Toplevel()
        w8.title("Guide")

        canvas = tkinter.Canvas(w8, width=1600, height=1000, bd=0, highlightthickness=0)
        canvas.pack()

        image = Image.open("purple.png")
        image = image.resize((1600, 1000))
        photo = ImageTk.PhotoImage(image)
         # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image = photo
        canvas.create_image(0, 0, image=photo, anchor="nw")
    
    # Rest of the code...


        def play_video():
            video_path = "guidance.mp4"
            clip = VideoFileClip(video_path).subclip(0, 10)
            resized_clip = clip.resize(height=670)

            frames = []
            for t in range(int(resized_clip.duration * resized_clip.fps)):
                frame = resized_clip.get_frame(t / resized_clip.fps)
                frames.append(frame)

            images = [ImageTk.PhotoImage(image=Image.fromarray(frame)) for frame in frames]

            video_label = tkinter.Label(w8)
            video_label.config(image=images[0])
            video_label.image = images[0]
            video_label.place(x=190, y=80)

            def update_image(idx):
                video_label.config(image=images[idx])
                video_label.image = images[idx]
                w8.after(33, lambda: update_image((idx + 1) % len(images)))

            w8.after(33, lambda: update_image(1))

        play_video()

        # Create label buttons on the canvas
        w8b8 = tkinter.Label(w8, text="<  Back")
        w8b8.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
        w8b8.bind("<Button-1>", gui_back)

        w8b8_window = canvas.create_window(100, 100, anchor="nw", window=w8b8, width=60, height=30)

def gui_back(event):
        w8.destroy()
    

    
##########----------------Guide End---------------###########
    
##########-----------------SIGNUP----------------###########

def fun2(event):
        global w2
        w2 = tkinter.Toplevel()
        w2.title("Signup")
        #w2.geometry('800x770+10+10')
        #w2.configure(bg='#fff')

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user"
        )

        def insert_values():
            cursor = connection.cursor()
            sql = ("INSERT INTO userinfo (name, lastname, phoneno, emailid, password, user_name) VALUES (%s, %s, %s, %s, %s, %s)")
            val = (name.get(), lname.get(), phno.get(), email.get(), code.get(), user.get())
            cursor.execute(sql, val)
            print("Record Inserted Successfully")
            messagebox.showinfo("Success", "Record Inserted Successfully")
            connection.commit()
            cursor.close()
            connection.close()
            #messagebox.showinfo("Success", "Record Inserted Successfully")

        canvas = tkinter.Canvas(w2, width=1600, height=1000, bd=0, highlightthickness=0)
        canvas.pack()



        ###----image1----###
        # Open and resize the first image
        image1 = Image.open("purple.png")
        image1 = image1.resize((1600, 1000))
        photo1 = ImageTk.PhotoImage(image1)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image1 = photo1

        # Create the first image on the canvas
        canvas.create_image(0, 0, image=photo1, anchor="nw")
        ###----image1 END----###

        ###----image4----###
        # Open and resize the fourth image
        image4 = Image.open("insideimage-removebg-preview.png")
        image4 = image4.resize((500, 500))
        photo4 = ImageTk.PhotoImage(image4)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image4 = photo4

        # Create the fourth image on the canvas
        canvas.create_image(300, 150, image=photo4, anchor="nw")
        ###----image4 END----###

        ###----image5----###
        # Open and resize the fifth image
        image5 = Image.open("border.png")
        image5 = image5.resize((570, 620))
        photo5 = ImageTk.PhotoImage(image5)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image5 = photo5

        # Create the fifth image on the canvas
        canvas.create_image(740, 83, image=photo5, anchor="nw")
        ###----image5 END----###

        frame = Frame(w2, width=350, height=410, bg='#fff')
        frame.place(x=850, y=200)

        heading = Label(frame, text='Create Account', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 20, 'bold'))
        heading.place(x=65, y=0)
    # --------------------
        def on_enter(e):
            name.delete(0, 'end')
        def on_leave(e):
            if name.get() == '':
                name.insert(0, 'Name')

        name = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        name.place(x=30, y=45)
        name.insert(0, 'Name')
        name.bind("<FocusIn>", on_enter)
        name.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=67)

    # --------------------
        def on_enter(e):
            lname.delete(0, 'end')
        def on_leave(e):
            if lname.get() == '':
                lname.insert(0, 'Last Name')

        lname = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        lname.place(x=30, y=85)
        lname.insert(0, 'Last Name')
        lname.bind("<FocusIn>", on_enter)
        lname.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # --------------------
        def on_enter(e):
            phno.delete(0, 'end')
        def on_leave(e):
            if phno.get() == '':
                phno.insert(0, 'Phone no')

        phno = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        phno.place(x=30, y=125)
        phno.insert(0, 'Phone no')
        phno.bind("<FocusIn>", on_enter)
        phno.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=147)

    # --------------------
        def on_enter(e):
            email.delete(0, 'end')
        def on_leave(e):
            if email.get() == '':
                email.insert(0, 'Email id')

        email = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        email.place(x=30, y=165)
        email.insert(0, 'Email id')
        email.bind("<FocusIn>", on_enter)
        email.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=187)

    # --------------------
        def on_enter(e):
            user.delete(0, 'end')
        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Username')

        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        user.place(x=30, y=205)
        user.insert(0, 'Username')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=227)

    # --------------------
        def on_enter(e):
            code.delete(0, 'end')
        def on_leave(e):
            if code.get() == '':
                code.insert(0, 'Password')

        code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        code.place(x=30, y=245)
        code.insert(0, 'Password')
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=267)

    # --------------------
        def on_enter(e):
            conform_code.delete(0, 'end')
        def on_leave(e):
            if conform_code.get() == '':
                conform_code.insert(9, 'Confirm Password')

        conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        conform_code.place(x=30, y=285)
        conform_code.insert(0, 'Confirm Password')
        conform_code.bind("<FocusIn>", on_enter)
        conform_code.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=307)

    # -------------

        Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=insert_values).place(x=35, y=327)
        label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=90, y=363)

        signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: fun3(None))
        signin.place(x=200, y=363)


    # Create label buttons on the canvas
        w2b2 = tkinter.Label(w2, text="<  Back")
        w2b2.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
        w2b2.bind("<Button-1>", fun2_back)

        w2b2_window = canvas.create_window(100, 100, anchor="nw", window=w2b2, width=60, height=30)
def fun2_back(event):
        w2.destroy()

     
###########-----------SIGN UP END--------------############

##########-----------LOG IN------------_##########
def fun3(event):
        global w3
        w3 = tkinter.Toplevel()
        w3.title("Login")

        canvas = tkinter.Canvas(w3, width=1600, height=1000, bd=0, highlightthickness=0)
        canvas.pack()

        ###----image1----###
        # Open and resize the first image
        image1 = Image.open("purple.png")
        image1 = image1.resize((1600, 1000))
        photo1 = ImageTk.PhotoImage(image1)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image1 = photo1

        # Create the first image on the canvas
        canvas.create_image(0, 0, image=photo1, anchor="nw")
        ###----image1 END----###

        ###----image2----###
        # Open and resize the second image
        image2 = Image.open("login image.png")
        image2 = image2.resize((400, 500))
        photo2 = ImageTk.PhotoImage(image2)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image2 = photo2

        # Create the second image on the canvas
        canvas.create_image(300, 180, image=photo2, anchor="nw")
        ###----image2 END----###

        ###----image3----###
        # Open and resize the fifth image
        image3 = Image.open("border.png")
        image3 = image3.resize((570, 530))
        photo3 = ImageTk.PhotoImage(image3)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image3 = photo3

        # Create the fifth image on the canvas
        canvas.create_image(840, 120, image=photo3, anchor="nw")
         ###----image3 END----###

        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user"
        )
    
        def signin():
            cursor = connection.cursor()
            query = "SELECT * FROM userinfo WHERE user_name = %s AND password = %s"
            val = (user.get(), code.get())
            cursor.execute(query, val)
            if not cursor.fetchone():
                print("The record does not exist.")
                messagebox.showinfo("ERROR", "Record does not Exist")
            elif val[0] == 'admin' and val[1] == 'admin':
            #w3.withdraw()  # Hide the login window
                generate_key()
            else:
                check_usb()
    
        frame = Frame(w3, width=350, height=350, bg="white")
        frame.place(x=950, y=220)

        heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Tahoma', 23, 'bold'))
        heading.place(x=120, y=10)

###########----------------------------------------------------

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Username')

        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Tahoma', 11))
        user.place(x=30, y=90)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=117)

    ###########-----------------------------------------------------

        def on_enter(e):
            code.delete(0, 'end')

        def on_leave(e):
            name = code.get()
            if name == '':
                code.insert(0, 'Password')

        code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Tahoma', 11))
        code.place(x=30, y=160)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=187)

        ###############################################################

        Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=219)
        label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Tahoma', 9))
        label.place(x=75, y=280)

        sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=lambda: fun2(None))
        sign_up.place(x=215, y=280)

        # Create label buttons on the canvas
        w3b3 = tkinter.Label(w3, text="<  Back")
        w3b3.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
        w3b3.bind("<Button-1>", fun3_back)

        w3b3_window = canvas.create_window(100, 100, anchor="nw", window=w3b3, width=60, height=30)

def fun3_back(event):
        w3.destroy()

##########----------LOGIN END---------#########
    
##########----------DETECTION OF USB---------#########

def check_usb():
        global wch;
        wch = tkinter.Toplevel()
        wch.title("USB Detection")
    
        def check_removable_disk():
            out = subprocess.check_output('wmic logicaldisk get DriveType, caption', shell=True)
            for drive in str(out).strip().split('\\r\\r\\n'):
                if '2' in drive:
                    drive_letter = drive.split(':')[0]
                    drive_type = drive.split(':')[1].strip()
                    if drive_type == '2':
                        return True
            return False

        # Function to execute when the button is clicked
        def button_click():
            if check_removable_disk():
                play_video("usb2.mp4")
                label.config(text="Removable disk detected")
                button = tkinter.Button(wch, text="Next  >", command=disp, bg='black', fg='white', font=('Arial', 17))
                button.place(relx=0.8, rely=0.8, anchor='center')
            else:
                play_video("usbnot1.mp4")
                label.config(text="Removable disk not detected")
                button = tkinter.Button(wch, text="Exit", command=go_back, bg='black', fg='white', font=('Arial', 17))
                button.place(relx=0.8, rely=0.8, anchor='center')

        # Function to play the transparent video
        def play_video(video_path):
            video = cv2.VideoCapture(video_path)
            if video.isOpened():
                width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
                resized_width = 400
                resized_height = 400 * height // width

                # Create a circular mask
                mask = np.zeros((resized_height, resized_width), dtype=np.uint8)
                center = (resized_width // 2, resized_height // 2)
                radius = min(center) - 10
                cv2.circle(mask, center, radius, (255, 255, 255), -1, cv2.LINE_AA)

                # Function to update the canvas with the next video frame
                def update_frame():
                    ret, frame = video.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                        frame = cv2.resize(frame, (resized_width, resized_height))  # Resize the frame
                        frame = cv2.bitwise_and(frame, frame, mask=mask)  # Apply circular mask
                        image = Image.fromarray(frame)
                        photo = ImageTk.PhotoImage(image)
                        canvas.create_image(570, 280, anchor='nw', image=photo)
                        canvas.image = photo
                        wch.after(30, update_frame)
                    else:
                        video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the beginning of the video
                        update_frame()

                # Start updating the canvas with video frames
                update_frame()

        canvas = tkinter.Canvas(wch, width=1600, height=1000, bd=0, highlightthickness=0)
        canvas.pack()

        ###----image1----###
        # Open and resize the first image
        image1 = Image.open("usb1.png")
        image1 = image1.resize((1600, 1000))
        photo1 = ImageTk.PhotoImage(image1)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image1 = photo1

        # Create the first image on the canvas
        canvas.create_image(0, 0, image=photo1, anchor="nw")
        ###----image1 END----###

        # Create the label
        label = tkinter.Label(wch, text="", fg='white', bg='black', font=('Times new Roman', 55))
        label.place(relx=0.5, rely=0.2, anchor='center')  # Place the label at the center of the window

        # Create the button
        button = tkinter.Button(wch, text="Check", command=button_click, bg='black', fg='white', font=('Arial', 17))
        button.place(relx=0.5, rely=0.3, anchor='center')  # Place the button below the label

        #Back function
def go_back():
        wch.withdraw()
    
        #-----back button windows---#
        # Create label buttons on the canvas
        w1b1 = tkinter.Label(wch, text="<  Back")
        w1b1.configure(bg='black', fg='white', font=("Arial", 11, "bold"))
        w1b1.bind("<Button-1>", key_back)

        w1b1_window = canvas.create_window(100, 100, anchor="nw", window=w1b1, width=60, height=30)

def key_back(event):
        wch.destroy()

##########----------DETECTION OF USB END---------#########

##########----------Key Generation---------########
        
def generate_key():
        global w4
        w4 = tkinter.Toplevel()
        w4.title("Key Generation")

        def insert_db(otp):
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="user"
            )
            cursor = connection.cursor()
            query = "INSERT INTO admin VALUES (%s)"
            val = (str(otp), )
            cursor.execute(query, val)
            connection.commit()
            cursor.close()
            connection.close()

        def send_otp(sender_email, otp):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('vishalkadalagi2004@gmail.com', 'qfjulxrdczpxnqzx')

            subject = 'Security Key'
            message = MIMEMultipart()
            message['From'] = 'vishalkadalagi2004@gmail.com'
            message['To'] = 'manojmp81977@gmail.com'
            message['Subject'] = subject

            body = 'Your OTP is ' + str(otp)
            message.attach(MIMEText(body, 'plain'))

            server.sendmail('vishalkadalagi2004@gmail.com', 'manojmp81977@gmail.com', message.as_string())
            print("OTP sent successfully")
            insert_db(str(otp))
            server.quit()

        security_key = ''.join(secrets.choice('0123456789') for _ in range(4))
        sender_email = 'vishalkadalagi2004@gmail.com'
    
        canvas = tkinter.Canvas(w4, width=1600, height=1000, bd=0, highlightthickness=0)
        canvas.pack()

        ###----image1----###
        # Open and resize the first image
        image1 = Image.open("blured 1.png")
        image1 = image1.resize((1600, 1000))
        photo1 = ImageTk.PhotoImage(image1)

         # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image1 = photo1

        # Create the first image on the canvas
        canvas.create_image(0, 0, image=photo1, anchor="nw")
        ###----image1 END----###

        text = "USB Security Key Generator"
        canvas.create_text(800, 100, text=text, fill="white", font=("Times New Roman", 35, "bold"), anchor="center")

        def generate_key_button(event):
            send_otp(sender_email, security_key)
            messagebox.showinfo("Generated Key", f"Decryption Key has sent to EMAIL ID", parent=w4)

        ###----Generate Key button------###
        # Create label buttons on the canvas
        button1 = tkinter.Label(w4, text="Generate Security Key")
        button1.configure(bg='#0F52BA', fg='white', font=("Arial", 15, "bold"))
        button1.bind("<Button-1>", generate_key_button)

        button1_window = canvas.create_window(680, 600, anchor="nw", window=button1, width=250, height=50)

         ###-----Generate Key button End-----###

        frames = []
        video_path = "key logo.mp4"

        video = cv2.VideoCapture(video_path)
        while True:
            ret, frame = video.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            image = Image.fromarray(frame)
            image = image.resize((400, 400))
            mask = Image.new('L', image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
            image.putalpha(mask)
            frame = ImageTk.PhotoImage(image)
            frames.append(frame)

        video.release()

        def update_frame(idx):
            if idx < len(frames):
                canvas.itemconfig(video_frame, image=frames[idx])
                w4.after(100, update_frame, (idx + 1) % len(frames))

        video_frame = canvas.create_image(800, 370, anchor="center")
        w4.after(0, update_frame, 0)

        # Create label buttons on the canvas
        w4b4 = tkinter.Label(w4, text="<  Back")
        w4b4.configure(bg='black', fg='white', font=("Arial", 11, "bold"))
        w4b4.bind("<Button-1>", usb_back)

        w4b4_window = canvas.create_window(100, 100, anchor="nw", window=w4b4, width=60, height=30)

def usb_back(event):
        w4.destroy()

##########----------Key Generation END---------########

######------------Disp---------###########

def disp():
        global w5
        w5 = tkinter.Toplevel()
        w5.title("Directory")
    
        import mysql.connector
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user"
        )

        # Function to list files and directories
        def list_files(directory):
            root = next(os.walk(directory))[0]  # path
            dirnames = next(os.walk(directory))[1]  # list of directories
            files = next(os.walk(directory))[2]  # list of files

            trv.delete(*trv.get_children())  # Clear existing treeview items

            # Insert directories into the treeview
            for i, d in enumerate(dirnames, start=1):
                trv.insert("", 'end', iid=i, values=d)

                path2 = os.path.join(directory, d)  # Path for subdirectory
                files2 = next(os.walk(path2))[2]  # file list of subdirectory

                # Insert files within subdirectories into the treeview
                for j, f2 in enumerate(files2, start=i*10):
                    trv.insert(i, 'end', iid='sub'+str(j), values="-"+f2)

            # Insert files into the treeview
            for k, f in enumerate(files, start=len(dirnames)+1):
                trv.insert("", 'end', iid=k, values=f)

        # Function to open the selected file
        def open_file():
            item_id = trv.focus()  # Get the selected item
            item = trv.item(item_id)
            values = item['values']
            if values and len(values) > 0 and not values[0].startswith('-'):  # If it's a file
                file_path = os.path.join(l1.cget("text"), values[0])
                os.startfile(file_path)

        # Function to handle the decryption key acceptance
        def dcription_key_accept(event):
            #t1.grid(row=5, column=5)
            t1.place(x=600, y=600)
            gobtn = tk.Button(w5, text="Go", command=check_db)
            #gobtn.grid(row=5, column=7)
            gobtn.place(x=730, y=597)

        # Function to check the decryption key in the database
        def check_db():
            # Add your database connection code here
            cursor = connection.cursor()
            val = (t1.get(),)
            query = ("select * from admin where encrypt_key = %s")
            cursor.execute(query,val)
            if not (cursor.fetchone()):
                messagebox.showwarning("Access Denied", "Incorrect decryption key.", parent=w5)
            else:
                open_file()

        # Function to open the directory selection dialog
        def open_directory():
            directory = filedialog.askdirectory(parent=w5)
            if directory:
                l1.config(text=directory)
                list_files(directory)

        canvas = tkinter.Canvas(w5, width=1600, height=1000, bd=0, highlightthickness=0)
        canvas.pack()

        ###----image1----###
        # Open and resize the first image
        image1 = Image.open("purple.png")
        image1 = image1.resize((1600, 1000))
        photo1 = ImageTk.PhotoImage(image1)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image1 = photo1

        # Create the first image on the canvas
        canvas.create_image(0, 0, image=photo1, anchor="nw")
        ###----image1 END----###

        ###----image2----###
        # Open and resize the second image
        image2 = Image.open("disp ima.png")
        image2 = image2.resize((800, 1100))
        photo2 = ImageTk.PhotoImage(image2)

        # Keep a reference to the photo object to prevent it from being garbage-collected
        canvas.image2 = photo2

        # Create the second image on the canvas
        canvas.create_image(600, -220, image=photo2, anchor="nw")
        ###----image2 END----###

        # Render the transparent label text on the canvas
        text = "Enter Decryption Key"
        canvas.create_text(680, 560, text=text, fill="white", font=("Times New Roman", 18), anchor="center")

        # Button to select directory
        b1 = tk.Button(w5, text='Select Directory', font=15, command=open_directory, bg='lightblue')
        b1.place(x=200, y=50)#(row=0, column=0, padx=5, pady=10)

        # Entry field for decryption key
        t1 = tkinter.Entry(w5)

        # Label to display the selected directory path
        l1 = tkinter.Label(w5, text='', bg='white', font=16)
        #l1.grid(row=0, column=1, padx=20)
        l1.place(x=400, y=55)
        # Treeview to display files and directories
        trv = ttk.Treeview(w5, selectmode='browse', height=30)
        #trv.grid(row=1, column=0, columnspan=2, padx=20, pady=0)
        trv.place(x=200, y=100)
        trv["columns"] = ("1")
        trv['show'] = 'tree headings'
        trv.column("#0", width=20, anchor='c')
        trv.column("1", width=300, anchor='w')
        trv.heading("#0", text="#")
        trv.heading("1", text="Name", anchor='w')

        # Bind double-click event to open_file function
        trv.bind("<Double-1>", dcription_key_accept)

        # Create label buttons on the canvas
        w5b5 = tkinter.Label(w5, text="<  Back")
        w5b5.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
        w5b5.bind("<Button-1>", disp_back)

        w5b5_window = canvas.create_window(100, 100, anchor="nw", window=w5b5, width=60, height=30)

def disp_back(event):
        w5.destroy()

######------------Disp END---------###########

        

#########-----------Home Page-----------#########
def home_page():
    from PIL import Image
    root = tkinter.Tk()
    root.title("Home Page")

    # Create a canvas with a transparent background
    canvas = tkinter.Canvas(root, width=2000, height=1000, bd=0, highlightthickness=0)
    canvas.place(x=2, y=2)

    # Set the canvas background image with transparent background
    image = Image.open("purple.png")
    image = image.resize((1550, 900))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor="nw")

    # Render the transparent label text on the canvas
    text = "USB"
    canvas.create_text(350, 150, text=text, fill="white", font=("Footlight MT Light", 65), anchor="center")

    text = "Security"
    canvas.create_text(350, 250, text=text, fill="white", font=("Footlight MT Light", 65), anchor="center")

    text = "The USB Security Key project aims to enhance data security\nand access control by implementing a secure authentication\nmechanism using USB-based security keys. The project\nfocuses on developing a robust and user-friendly system\nthat leverages USB security keys to provide strong\nauthentication for various files"
    canvas.create_text(400, 500, text=text, fill="white", font=("Cambria", 20), anchor="center")

    # Create label buttons on the canvas
    button1 = tkinter.Label(root, text="About us")
    button1.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
    button1.bind("<Button-1>", fun1)

    button2 = tkinter.Label(root, text="Signup")
    button2.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
    button2.bind("<Button-1>", fun2)

    button3 = tkinter.Label(root, text="Login")
    button3.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
    button3.bind("<Button-1>", fun3 )

    button4 = tkinter.Label(root, text="Guide")
    button4.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
    button4.bind("<Button-1>", gui)

    button1_window = canvas.create_window(1020, 100, anchor="nw", window=button1, width=70, height=40)
    button2_window = canvas.create_window(1120, 100, anchor="nw", window=button2, width=70, height=40)
    button3_window = canvas.create_window(1220, 100, anchor="nw", window=button3, width=70, height=40)
    button4_window = canvas.create_window(920, 100, anchor="nw", window=button4, width=70, height=40)

    # Load the video frames
    frames = []
    video_path = "tranparent_usb_AdobeExpress.mp4"

    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        image = Image.fromarray(frame)
        image = image.resize((400, 400))
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
        image.putalpha(mask)
        frame = ImageTk.PhotoImage(image)
        frames.append(frame)
        video.release()

    # Function to update the canvas with the next frame
    def update_frame(idx):
        if idx < len(frames):
            canvas.itemconfig(video_frame, image=frames[idx])
            root.after(100, update_frame, (idx + 1) % len(frames))

    # Create an initial image item on the canvas
    video_frame = canvas.create_image(1095, 400, anchor="center")

    # Start updating the canvas with video frames
    root.after(0, update_frame, 0)
    root.mainloop()

    

###########------------------Home Page END------------#################

#----------Check USB Software----------#
def check_removable_disk():
    out = subprocess.check_output('wmic logicaldisk get DriveType, caption', shell=True)
    for drive in str(out).strip().split('\\r\\r\\n'):
        if '2' in drive:
            drive_letter = drive.split(':')[0]
            drive_type = drive.split(':')[1].strip()
            if drive_type == '2':
                return True
    return False

if check_removable_disk():
    usb_drive = 'H:'  # Replace 'E:' with the appropriate drive letter of your USB drive
    file_name = '.hidden_file.txt'  # Replace '.hidden_file.txt' with the name of your hidden file

# Create the full file path
    file_path = os.path.join(usb_drive, file_name)

    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            connection1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="user"
            )
            cursor1 = connection1.cursor()
            query1 = ("SELECT * FROM key_file WHERE dongle_key = %s")
            val = (str(file_contents),)
            cursor1.execute(query1, val)
            if  cursor1.fetchone():
                home_page()
            connection1.commit()
            cursor1.close()
            connection1.close()
        
    except FileNotFoundError:
        messagebox.showerror("Invalid USB", "This USB has no access to the Software")
        sys.exit()
    except IOError:
        print("")


else:
    messagebox.showerror("Error", "Specified USB is not connected, Software will not Run.")

#----------Check USB Software END----------#


import tkinter as tk
import cv2
from PIL import ImageTk, Image, ImageDraw
import subprocess
from tkinter import messagebox

# Function to check if a removable disk is detected
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
    # Create the main window
    window = tk.Tk()
    window.title("Home Page")

    # Rest of your code...
    # Create a canvas with a transparent background
    canvas = tk.Canvas(window, width=2000, height=1000, bd=0, highlightthickness=0)
    canvas.place(x=2, y=2)

    # Set the canvas background image with transparent background
    image = Image.open("purple.png")
    image = image.resize((1550, 900))  # Adjust the size as per your canvas dimensions

    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor="nw")

    # Render the transparent label text on the canvas
    text = "USB"
    canvas.create_text(350, 150, text=text, fill="white", font=("Footlight MT Light", 65), anchor="center")

    text = "Security"
    canvas.create_text(350, 250, text=text, fill="white", font=("Footlight MT Light", 65), anchor="center")

    text = "The USB Security Key project aims to enhance data security\nand access control by implementing a secure authentication\nmechanism using USB-based security keys. The project\nfocuses on developing a robust and user-friendly system\nthat leverages USB security keys to provide strong\nauthentication for various files"
    canvas.create_text(400, 500, text=text, fill="white", font=("Cambria", 20), anchor="center")

        # Function to handle button clicks
    def change_button_color(event):
        print("Button clicked!")

    # Create label buttons on the canvas
    button1 = tk.Label(window, text="About us")
    button1.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
    button1.bind("<Button-1>", change_button_color)

    button2 = tk.Label(window, text="Signup")
    button2.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
    button2.bind("<Button-1>", change_button_color)

    button3 = tk.Label(window, text="Login")
    button3.configure(bg='#0F52BA', fg='white', font=("Arial", 11, "bold"))
    button3.bind("<Button-1>", change_button_color)

    button1_window = canvas.create_window(1020, 100, anchor="nw", window=button1, width=70, height=40)
    button2_window = canvas.create_window(1120, 100, anchor="nw", window=button2, width=70, height=40)
    button3_window = canvas.create_window(1220, 100, anchor="nw", window=button3, width=70, height=40)

    # Load the video frames
    frames = []
    video_path = "tranparent_usb_AdobeExpress.mp4"  # Update the file path to your video file


    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        # Convert frame to RGBA format with alpha channel
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        image = Image.fromarray(frame)
        image = image.resize((400, 400))  # Adjust the size as per your requirements
    
        # Create a circular mask
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
    
        # Apply the circular mask to the frame
        image.putalpha(mask)
    
        frame = ImageTk.PhotoImage(image)
        frames.append(frame)

    video.release()

    # Function to update the canvas with the next frame
    def update_frame(idx):
        if idx < len(frames):
            canvas.itemconfig(video_frame, image=frames[idx])
            window.after(100, update_frame, (idx + 1) % len(frames))

    # Create an initial image item on the canvas
    video_frame = canvas.create_image(1140, 400, anchor="center")

    # Start updating the canvas with video frames
    window.after(0, update_frame, 0)

    window.mainloop()
else:
    messagebox.showerror("USB Not Connected", "USB is not connected. The window will not open.")

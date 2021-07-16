from tkinter import *
from gtts import gTTS
from playsound import playsound

# window
root = Tk()
root.geometry("350x300")
root.configure(bg="black")
root.title("Text to speech")

# Label
Label(root, text="Text_To_Speech", font="arial 25 bold", bg="black").pack()
Label(text ="Kashfi learning Python", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root, text="Enter Text", font="arial 20 bold", bg="black").place(x=20, y=60)


entry_field = Entry(root, textvariable=Msg, width="50")  # Entry() = creating a input text field
entry_field.place(x=20, y=100)  # placing special position
# Convert text to speech


def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save("Kashfi learning Python.mp3")
    playsound("Kashfi learning Python.mp3")


# exit and reset
def _exit():
    root.destroy()


def _reset():
    Msg.set("")


Button(root, text="Play", font="arial 20 bold", command=text_to_speech, width='4').place(x=25, y=140)
Button(root, font="arial 20 bold", text="Exit", width='4', command=_exit, bg="OrangeRed1").place(x=100, y=140)
Button(root, font="arial 20 bold", text="Reset", width='6', command=_reset).place(x=175, y=140)

root.mainloop()

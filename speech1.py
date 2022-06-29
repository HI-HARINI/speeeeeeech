from tkinter import *
import speech_recognition as sr
from googletrans import Translator
from tkinter import ttk
from googletrans import LANGUAGES

root=Tk()
root.geometry("1000x600")
root.title("Speech Recognizer")
root.configure(bg="pink")
label1=Label(root,text="Language Translater", font=("Bahnschrift Light",15,"bold"))
label1.place(relx=0.5, rely=0.1,anchor=CENTER)

label2=Label(root,text="Enter Text", font=("Bahnschrift Light",10,"bold"))
label2.place(relx=0.1, rely=0.3,anchor=CENTER)

textbox=Text(root, width="30", height="10")
textbox.place(relx=0.1, rely=0.5,anchor=W)

label3=Label(root,text="Output", font=("Bahnschrift Light",10,"bold"))
label3.place(relx=0.7, rely=0.3,anchor=CENTER)

textbox2=Text(root, width="30", height="10")
textbox2.place(relx=0.7, rely=0.5,anchor=W)

language=list(LANGUAGES.values())
dropdown=ttk.Combobox(root,state="readonly",values=language)
dropdown.place(relx=0.3, rely=0.3,anchor=CENTER)
dropdown.set("english")
chooselanguage=list(LANGUAGES.values())
dropdown2=ttk.Combobox(root,state="readonly",values=chooselanguage)
dropdown2.place(relx=0.85, rely=0.3,anchor=CENTER)
dropdown2.set("choose other language")

def translate():
    translator=Translator()
    Input_text=textbox.get(1.0, END)
    srclang=dropdown.get()
    dest_lang=dropdown2.get()
    translated=translator.translate(text= Input_text, src=srclang, dest=dest_lang)
    textbox2.delete(1.0, END)
    textbox2.insert(END, translated.text)
    
button1=Button(root, text="Translate", command=translate)
button1.place(relx=0.5, rely=0.85,anchor=CENTER)

root.mainloop()
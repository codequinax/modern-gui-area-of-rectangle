import customtkinter as ctk
import pyttsx3
engine=pyttsx3.init()
root=ctk.CTk()
def destroy():
    root.destroy()
def area():
    a=entry1.get()
    b=entry2.get()
    a=int(a)
    b=int(b)
    c=a*b
    label.configure(text=c)
    engine.say("the required area of rectangle is equals to ")
    engine.runAndWait()



label1=ctk.CTkLabel(master=root,text="AREA OF RECTANGLE")
label1.pack()
labellenght=ctk.CTkLabel(root,text="Enter the lenght of rectangle")
labellenght.pack(padx=10,pady=10)
entry1=ctk.CTkEntry(master=root)
entry1.pack(pady=10)
labellenght1=ctk.CTkLabel(root,text="Enter the width of rectangle")
labellenght1.pack(padx=10,pady=10)
entry2=ctk.CTkEntry(master=root)
entry2.pack(pady=20)
label=ctk.CTkLabel(master=root,text="")
label.pack()
button2=ctk.CTkButton(master=root,text="area",command=area)
button2.pack(pady=40)
button1=ctk.CTkButton(master=root,text="exit",command=destroy)
button1.pack()
root.mainloop()

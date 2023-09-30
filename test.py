from tkinter import *
import customtkinter
from PIL import Image, ImageTk

root = Tk()
'''
widgets are added here
'''
root.geometry('1920x1080')
root.title('Conference Page')


imglabel = Label(root, borderwidth=0,)
img = Image.open(r"C:\Users\faraa\PycharmProjects\CaseManagement\image\Supreme.png",)
img = img.resize((1325, 300))
imglabel.img = ImageTk.PhotoImage(img)
imglabel['image'] = imglabel.img

imglabel.place(relx=0, rely=0)


header = customtkinter.CTkFrame(root, fg_color='orange', height=30)
appname = customtkinter.CTkButton(header,text="APP NAME",width=10, height=30, fg_color="transparent",
                               text_color="black", font=("Times New Roman", 15), hover_color="orange")
appname.place(x=1190,y=0)
btna = customtkinter.CTkButton(header,text="Home", width=10, height=30, fg_color="transparent", hover_color="green",
                               text_color="black", font=("Times New Roman", 15))
btna.place(x=3,y=0)
btnb = customtkinter.CTkButton(header,text="MY PROFILE", width=10, height=30, fg_color="transparent", hover_color="green",
                               text_color="black", font=("Times New Roman", 15))
btnb.place(x=60,y=0)

optionmenu_var = customtkinter.StringVar(value="SELECT")
btnc = customtkinter.CTkOptionMenu(header, values=["option 1", "option 2","option3","option4"], fg_color="orange",
                                   variable=optionmenu_var, text_color="black",font=("Times New Roman", 15),width=10,
                                   height=30, button_hover_color="green", dropdown_fg_color="orange",
                                   button_color="orange", dropdown_hover_color="green")
btnc.place(x=170,y=0)

optionmenu_var2 = customtkinter.StringVar(value="SELECT")
btnd = customtkinter.CTkOptionMenu(header, values=["option 1", "option 2","option3"], fg_color="orange",
                                   variable=optionmenu_var2, text_color="black",font=("Times New Roman", 15),width=10,
                                   height=30, button_hover_color="green", dropdown_fg_color="orange",
                                   button_color="orange", dropdown_hover_color="green")
btnd.place(x=270,y=0)


def switch_event():
    print("switch toggled, current value:", switch_var.get())


switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(header, text="Receive Notifications", command=switch_event, button_color="blue",fg_color="orange",
                                 variable=switch_var, onvalue="on", offvalue="off",text_color="black",
                                 font=("Times New Roman", 15),width=10, height=30)

switch.place(x=1000,y=0)

createBtn = customtkinter.CTkButton(root, text='Create Meeting', width=200, height=50, fg_color='#39e600',
                                    border_width=1, hover_color='#269900', font=('PMincho', 25), border_spacing=20)
joinBtn = customtkinter.CTkButton(root, text='Join Meeting', width=200, height=50, fg_color='#005ce6',
                                    hover_color='#668cff', font=('PMincho', 25),border_width=1,border_spacing=20)
scheduleBtn = customtkinter.CTkButton(root, text='Schedule a Meeting', width=180, height=50, fg_color='#e65c00',
                                    hover_color='#ff944d', font=('PMincho', 25),border_spacing=20, border_width=1)

link = customtkinter.CTkLabel(root, text="Create an account /", fg_color="transparent", text_color="blue")
link.place(x=572, y=450)
link2 = customtkinter.CTkLabel(root, text="Log In", fg_color="transparent",  text_color="blue")
link2.place(x=684, y=450)

note = customtkinter.CTkLabel(root, text="NOTE: You cannot join a meeting without a .... account", fg_color="transparent"
                              ,font=('Times New Roman', 15), text_color="black")
note.place(x=500, y=500)

label_frame = LabelFrame(root, text='Terms and conditions', background='orange')
label1 = Label(label_frame, text='1. This is a Label.', background='orange')
label2 = Label(label_frame, text='1. This is a Label.', background='orange')
label3 = Label(label_frame, text='1. This is a Label.', background='orange')
label4 = Label(label_frame, text='1. This is a Label.', background='orange')


header.pack(fill=X)
createBtn.place(x=200, y=350)
joinBtn.place(x=550, y=350)
scheduleBtn.place(x=900, y=350)
label_frame.pack(expand='yes', fill=X, anchor=S, pady=(100, 0))
label1.pack(anchor=W, padx=200)
label3.place(x=900)
label2.pack(anchor=W, padx=200)
label4.place(x=900, y=20)


root.config(bg='#d4d7db')
root.mainloop()

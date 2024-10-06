from tkinter import *
from tkinter .ttk import Combobox
from tkinter import messagebox
import string,random

window = Tk()
window.geometry("500x500")
window.title("megala Password Generator")
window.config(bg="beige")
window.resizable(False, False)


def password_generator():
    try:
        length_password = int(solidboss.get())
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation
        all_list = []
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel(" A Problem has been Occured","please Try again")


all_no = {"1" : "1" , "2" : "2", "3" : "3" , "4" : "4" , "5" : "5" , "6" : "6" , "7" : "7" , "8" : "8" , "9" : "9" , "10" : "10" , "11" : "11",}

Title = Label(window, text="megala password Generator", bg="beige", fg="black", font=("futura", 15, "bold"))
Title.pack(anchor="center", pady="20px")
           
length = Label(window, text="Select the length of your Password :- ", fg="darkgreen", bg="beige", font=("ubuntu",12))
length.place(x="20px", y="70px")
           

def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def on_leave(e):
     generate_btn['bg'] = "Orange"
     generate_btn['fg'] = "black"


solidboss = IntVar()
Selector = Combobox(window,textvariable=solidboss,state="readonly")
Selector['values'] = [L for L in all_no.keys()]
Selector.current(7)
Selector.place(x="240px",y="72px")

generate_btn = Button(window, text="Generate password", bg="black",font=("ubuntu", 15), cursor="hand2", command=password_generator)
generate_btn.bind("<Enter>",on_enter)
generate_btn.bind("<Leave>",on_leave)
generate_btn.pack(anchor="center",pady="50px")                      


result_Label= Label(window, text="Generate password here:-",bg="beige",fg="darkgreen",font=("ubuntu",12))
result_Label.place(x="20px", y="160px")

password = StringVar()
password_final = Entry(window, textvariable = password, state="readonly", fg="blue", font=("ubuntu", 15))
password_final.place(x="190px", y="165px")

window.mainloop()

                   


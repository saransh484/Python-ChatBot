from tkinter import *
import chatbot as cb
import bart as bc

# GUI
root = Tk()
root.title("Chatbot")
 
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Arial 14"
FONT_BOLD = "Arial 13 bold"
 
# Send function
def send():
    send = "You : " + e.get()
    txt.insert(END, "\n" + send)
 
    user = e.get().lower()
    
    if user[0] == '&':
        ret = bc.summerize(user[1:])
        txt.insert(END,"\n Bot : " + ret) # type: ignore
    else:
        ints = cb.predict_class(user)
        res = cb.get_response(ints, cb.intents)
        txt.insert(END,"\n Bot : " + res) # type: ignore

    e.delete(0, END)

lable1 = Label(root,  text="ChatBot", font=FONT_BOLD, pady=10, width=40, height=1).grid(row=0)
 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1) # type: ignore
root.mainloop()
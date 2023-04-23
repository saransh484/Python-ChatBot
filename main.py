import tkinter as tk
import tkinter.ttk as ttk
import chatbot as cb
import bart as bc

# GUI
root = tk.Tk()
root.title("Chatbot")
 
BG_GRAY = "#44475a"
BG_COLOR = "#282a36"
TEXT_COLOR = "#f8f8f2"
 
FONT = "Arial 14"
FONT_BOLD = "Arial 13 bold"
 
# Send function
def send():
    send = "You : " + e.get()
    txt.insert(tk.END, "\n" + send)
 
    user = e.get().lower()
    
    if user[0] == '&':
        ret = bc.summerize(user[1:])
        txt.insert(tk.END,"\n Bot : " + ret) # type: ignore
    else:
        ints = cb.predict_class(user)
        res = cb.get_response(ints, cb.intents)
        txt.insert(tk.END,"\n Bot : " + res) # type: ignore

    e.delete(0, tk.END)

lable1 = tk.Label(root,  text="ChatBot", font=FONT_BOLD, pady=10, width=40, height=1).grid(row=0)
 
txt = tk.Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = ttk.Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = tk.Entry(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = tk.Button(root, text="Send", font=FONT_BOLD, command=send).grid(row=2, column=1) # type: ignore
root.mainloop()
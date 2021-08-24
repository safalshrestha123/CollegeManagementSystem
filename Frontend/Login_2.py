import random
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
#import Frontend.Register_1


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry('1000x734+120+0')
        #self.root.iconbitmap()
        #self.root.resizable(0,0)

        #for image.....

        self.bg=ImageTk.PhotoImage(file='images\\bg-0122.jpg')
        bg=Label(self.root,image=self.bg).place(x=0,y=0)

        self.txt = "Login Here"
        #self.tex="*********"
        self.count = 0
        self.text = ''
        self.color = ["#fc01ff", "#02dadf", "#9a55f3","black"]
        self.heading1 = Label(self.root, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        #self.heading2 = Label(self.root, text=self.tex, font=('yu gothic ui', 10, "bold"), bg="white",fg='black', bd=5,relief=FLAT)
        self.heading1.place(x=340, y=80, width=350)
        #self.heading2.place(x=470,y=600,width=450)
        self.slider()
        self.heading_color()


        #labels,entry..............

        self.lbl1_e = StringVar()
        self.lbl2_e = StringVar()

        self.lbl1=Label(self.root,text="Username",bg='white',fg="#4f4e4d",font=('arial',10,'bold'))
        self.lbl1.place(x=340,y=220)

        self.lbl1_e=Entry(self.root,relief=FLAT,bg='white',fg='black',font=('arial', 15,'bold'))
        self.lbl1_e.place(x=377,y=238,width=300,height=30)


        self.lbl2 = Label(self.root, text="Password", bg='white', fg="#4f4e4d", font=('arial', 10,'bold'))
        self.lbl2.place(x=340, y=310)

        self.lbl2_e = Entry(self.root, relief=FLAT, bg='white', fg='black', font=('arial', 15, 'bold'),show='*')
        self.lbl2_e.place(x=372, y=328,width=300,height=30)


        #self.lbl3 = Label(self.root, text="* Are you registered?...", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold "))
        #self.lbl3.place(x=430, y=570)

        self.register_button = Button(self.root, text="Register Here",
                                    font=("yu gothic ui", 13, "bold "), fg="red", relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2",command=self.click_reg)
        self.register_button.place(x=460, y=450)



        #buttons......
        self.login_btn= ImageTk.PhotoImage(file='images\\login.jpg')
        self.loginbtn=Button(self.root,image=self.login_btn,relief=FLAT,borderwidth=0,cursor='hand2',command=self.login_data,)
        self.loginbtn.place(x=445,y=400)

    def click_reg(self):

        """when clicked reg button on login form, qqit will open reg window"""



        #self.root.withdraw()
        # #win.deiconify()
        self.root.destroy()
        self.w1=Toplevel(self.root)










    def slider(self):

        """creates slides for heading by taking the text,
         and that text are called after every 100 ms"""

        if self.count >= len(self.txt):
            self.count = -2
            self.text = ''
            self.heading1.config(text=self.text)
            #self.heading2.config(text=self.tex)

        else:
            self.text = self.text + self.txt[self.count]
            self.heading1.config(text=self.text)
            #self.heading2.config(text=self.tex)
        self.count += 1

        self.heading1.after(100, self.slider)
        #self.heading2.after(100, self.slider)

    def heading_color(self):

        """
        configures heading label
        :return: every 50 ms returned new random color.
        """

        fg = random.choice(self.color)
        self.heading1.config(fg=fg)
        self.heading1.after(50, self.heading_color)
        #self.heading2.config(fg=fg)
        #self.heading2.after(50, self.heading_color)

    def login_data(self):
        if self.lbl1_e.get() == "Safal" and self.lbl2_e.get() == "1234":
            messagebox.showinfo("Info",
                                f" Welcome {self.lbl1_e.get()} and your password is: {self.lbl2_e.get()}")
        if self.lbl1_e.get()=="" and self.lbl2_e.get()=="":
            messagebox.showinfo("Error","Complete the required field" )


        else:
            messagebox.showerror("Error", "Invalid username or password")



root=Tk()
object=Login(root)
root.mainloop()

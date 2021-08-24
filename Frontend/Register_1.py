import random
from tkinter import*
from PIL import Image,ImageTk

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry('1000x734+120+0')
        #self.root.iconbitmap()
        #self.root.resizable(0,0)

        #for image.....

        self.bg=ImageTk.PhotoImage(file='images\\bg-0122.jpg')
        bg=Label(self.root,image=self.bg).place(x=0,y=0)

        self.txt = "Register Here"
        self.count = 0
        self.text = ''
        self.color = ["#fc01ff", "#02dadf", "#9a55f3","black"]
        self.heading1 = Label(self.root, text=self.txt, font=('arial', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading1.place(x=340, y=80, width=350)
        self.slider()
        self.heading_color()

    #lables buttons and entry

        self.lbl1 = Label(self.root, text="Username", bg='white', fg="#4f4e4d", font=('arial', 10, 'bold'))
        self.lbl1.place(x=340, y=220)

        self.lbl1_e = Entry(self.root, relief=FLAT, bg='white', fg='black', font=('arial', 15, 'bold'))
        self.lbl1_e.place(x=377, y=238, width=300, height=30)

        self.lbl2 = Label(self.root, text="Password", bg='white', fg="#4f4e4d", font=('arial', 10, 'bold'))
        self.lbl2.place(x=340, y=310)

        self.lbl2_e = Entry(self.root, relief=FLAT, bg='white', fg='black', font=('arial', 15, 'bold'), show='*')
        self.lbl2_e.place(x=372, y=328, width=300, height=30)


        self.register_button = Button(self.root, text="Register Here",
                                      font=("arial", 13, "bold "), fg="black", relief=FLAT,
                                      activebackground="white"
                                      , borderwidth=0, background="red", cursor="hand2")
        self.register_button.place(x=460, y=450)



    def slider(self):

        """creates slides for heading by taking the text,
         and that text are called after every 100 ms"""

        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading1.config(text=self.text)


        else:
            self.text = self.text + self.txt[self.count]
            self.heading1.config(text=self.text)

        self.count += 1

        self.heading1.after(100, self.slider)


    def heading_color(self):

        """
        configures heading label
        returns every 50 ms returned new random color.
        """

        fg = random.choice(self.color)
        self.heading1.config(fg=fg)
        self.heading1.after(50, self.heading_color)




root=Tk()
object=Register(root)
root.mainloop()

from tkinter import *
import re
from tkinter import messagebox
import pymysql
from PIL import ImageTk,Image


def home():
    root = Tk()
    root.geometry("900x740")
    root.title("Steak House")

    img = ImageTk.PhotoImage(Image.open('food.png'),master=root)
    label = Label(root,image=img)
    label.pack()
    label.place(x=90,y=280)

    frame = Frame(root,bg="black",width=900,height=185)
    frame.pack()
    frame.place(x=0,y=0)
    label = Label(frame,text="Steak House",fg="#FEFC04",bg="black",font=("Georgia bold",45)).place(x=265,y=30)
    qut = Label(root,text="All Day Dinning Restaurant",fg="#B95E2C",font=("Georgia ",30)).place(x=45,y=200)
    qut1 = Label(root,text="A PLACE LIKE HOME...",fg="black",font=("Georgia ",15)).place(x=45,y=250)

    # -----------functions---------------------
    def back():
        menu.open()
        
    def close(a):
        a.destroy()

    def menu():
        menu = Tk()
        menu.geometry("1000x660")
        menu.title("Steak House")

        img = ImageTk.PhotoImage(Image.open('menu.png'),master=menu)
        label = Label(menu,image=img)
        label.pack()
     
        frame3 = Frame(menu,bg="black",width=450,height=450)
        frame3.pack()
        frame3.place(x=90,y=140)

        title = Label(frame3,text="Menu",fg="#F39C12",bg="black",font=("Arial 26 bold")).place(x=190,y=10)
        
        bc = Label(frame3,text="Biriyani",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=80)
        bc_p = Label(frame3,text="-  150",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=80)

        ds = Label(frame3,text="Dosa",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=120)
        ds_p = Label(frame3,text="-    10",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=120)

        pt = Label(frame3,text="Porotta",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=160)
        pt_p = Label(frame3,text="-    15",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=160)

        ct = Label(frame3,text="Chappati",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=200)
        ct_p = Label(frame3,text="-    12",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=200)

        ss = Label(frame3,text="Samosa",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=240)
        ss_p = Label(frame3,text="-    10",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=240)

        il = Label(frame3,text="Idaly",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=280)
        il_P = Label(frame3,text="-      8",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=280)

        cp = Label(frame3,text="Chilli Potato",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=320)
        cp_p = Label(frame3,text="-    20",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=320)
     
        gj = Label(frame3,text="Gulab Jamun",fg="#F39C12",bg="black",font=("Arial 20")).place(x=30,y=360)
        gj_p = Label(frame3,text="-    50",fg="#F39C12",bg="black",font=("Arial 20")).place(x=320,y=360)

        home_btn = Button(frame3,text="Back",fg="#F39C12",bg="black",command=lambda:[close(menu),home()],width=8).place(x=270,y=415)
        login_btn = Button(frame3,text="Login",fg="#F39C12",bg="black",command=lambda:[close(menu),login()],width=8).place(x=350,y=415)

        
        menu.mainloop()

    menu_btn = Button(frame,text="Menu",fg="#FEFC04",bg="black",command=lambda:[close(root),menu()],width=15).place(x=260,y=140)
    team_btn = Button(frame,text="Our Team",fg="#FEFC04",bg="black",width=15).place(x=400,y=140)

    def sinup():
        win = Tk()
        win.geometry("900x600")
        win.title("Steak House")

        img = ImageTk.PhotoImage(Image.open('restaurant.png'),master=win)
        label = Label(win,image=img)
        label.pack()


        frame2 = Frame(win,width=480,height=355)
        frame2.pack()
        frame2.place(x=210,y=123)

        label = Label(frame2,text="Registration Form",font=("Arial",20)).place(x=140,y=10)

        rname_l = Label(frame2,text="Enter Name",font=("Arial",15)).place(x=30,y=65)
        rname = Entry(frame2,width=30)
        rname.place(x=260,y=70)

        email2 = Label(frame2,text="Enter Email",font=("Arial",15)).place(x=30,y=115)
        email2 = Entry(frame2,width=30)
        email2.place(x=260,y=120)

        mobile_label = Label(frame2,text="Enter Mobile",font=("Arial",15)).place(x=30,y=165)
        mobile_e = Entry(frame2,width=30)
        mobile_e.place(x=260,y=170)

        pswd2 = Label(frame2,text="Enter Password",font=("Arial",15)).place(x=30,y=215)
        pswd3_e = Entry(frame2,width=30)
        pswd3_e.place(x=260,y=220)

        pswd4 = Label(frame2,text="Re-Enter Password",font=("Arial",15)).place(x=30,y=265)
        pswd5_e = Entry(frame2,width=30)
        pswd5_e.place(x=260,y=270)

        back_btn = Button(frame2,text="Back",command=lambda:[close(win),home()],width=10).place(x=215,y=315)


        def register():
            name = rname.get()
            email = email2.get()
            mobile = mobile_e.get()
            password = pswd3_e.get()
            pswd = pswd5_e.get()
            x = True
            while x:
                if (len(password)<6 or len(password)>12):
                    break
                elif not re.search("[A-Z]",password):
                    break
                elif not re.search("[a-z]",password):
                    break
                elif not re.search("[0-9]",password):
                    break
                elif not re.search("[@#$]",password):
                    break
                elif re.search("\s",password):
                    break
                else:
                    if (password == pswd):
                        con = pymysql.connect(host='localhost',user='root',passwd='9613',db='restaurant')
                        mycursor = con.cursor()

                        values = [(name,email,mobile,password)]
                        sql = "insert into login values(%s,%s,%s,%s)"
                        mycursor.executemany(sql,values)
                        con.commit()

                        messagebox.showinfo("info","Successfully Registered")
                        close(win)
                        login()
                    else:
                        messagebox.showinfo("info","password mismatch")
                    x = False
                    break
            if x:
                messagebox.showinfo("info","Not Valid")
                sinup()
        
        register_btn = Button(frame2,text="Register",command=register,width=10).place(x=300,y=315)

        win.mainloop()
        

    def login():
        log = Tk()
        log.geometry("900x600")
        log.title("Steak House")

        img = ImageTk.PhotoImage(Image.open('restaurant.png'),master=log)
        label = Label(log,image=img)
        label.pack()

        frame1 = Frame(log,width=400,height=235)
        frame1.pack()
        frame1.place(x=250,y=200)

        lb = Label(frame1,text="Login Page",font=("Arial",25)).place(x=120,y=10)

        email = Label(frame1,text="Enter Email",font=("Arial",15)).place(x=30,y=65)
        email_entry = Entry(frame1,width=30)
        email_entry.place(x=190,y=70)

        pswd = Label(frame1,text="Enter Password",font=("Arial",15)).place(x=30,y=115)
        pswd_entry = Entry(frame1,width=30)
        pswd_entry.place(x=190,y=120)

        label = Label(frame1,text="Don't have an account?",fg="blue").place(x=5,y=165)
        sign = Button(frame1,text="Sign up",command=lambda:[close(log),sinup()],width=8).place(x=135,y=163)
        back = Button(frame1,text="Back",command=lambda:[close(log),home()],width=8).place(x=230,y=163)


        def login_s():
            email_id = email_entry.get()
            pswd = pswd_entry.get()
            
            if email_id=="" or pswd=="":
                messagebox.showerror("Error","Enter User Name And Password",master=log)
            else:
                con = pymysql.connect(host='localhost',user='root',passwd='9613',db='restaurant')
                mycursor = con.cursor()

                values = [(email_id,pswd)]
                sql = "select * from login where email=%s and password=%s"
                mycursor.executemany(sql,values)
                row = mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error" , "Invalid User Name And Password",master=log)
                else:
                    close(log)
                    order_items()

        login_btn = Button(frame1,text="Login",command=login_s,width=8).place(x=300,y=163)

        def clear():
            email_entry.delete(0,'end')
            pswd_entry.delete(0,'end')
        clear = Button(frame1,text="Clear",command=clear,width=8).place(x=300,y=193)

        log.mainloop()



    def order_items():
        order = Tk()
        order.geometry("800x750")
        order.title("Steak House")
     
        img = ImageTk.PhotoImage(Image.open('order.png'),master=order)

        label = Label(order,image=img)
        label.pack()
        label.place(x=0,y=40)

        frame3 = Frame(order,width=600,height=450)
        frame3.pack()
        frame3.place(x=100,y=280)

        title = Label(frame3,text="Menu",font=("Arial 26 bold")).place(x=250,y=0)

        it = Label(frame3,text="Items",font=("Arial 20 bold")).place(x=30,y=40)
        it_p = Label(frame3,text="- Price",font=("Arial 20 bold")).place(x=320,y=40)
        it_l = Label(frame3,text="Quantity",font=("Arial 20 bold")).place(x=450,y=40)

        s1 = StringVar()
        s2 = StringVar()
        s3 = StringVar()
        s4 = StringVar()
        s5 = StringVar()
        s6 = StringVar()
        s7 = StringVar()
        s8 = StringVar()
        total_p = StringVar()

        bc = Label(frame3,text="Biriyani",font=("Arial 20")).place(x=30,y=80)
        bc_p = Label(frame3,text="-  150",font=("Arial 20")).place(x=320,y=80)
        spin = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin.place(x=470,y=85)

        ds = Label(frame3,text="Dosa",font=("Arial 20")).place(x=30,y=120)
        ds_p = Label(frame3,text="-    10",font=("Arial 20")).place(x=320,y=120)
        spin0 = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin0.place(x=470,y=125)

        pt = Label(frame3,text="Porotta",font=("Arial 20")).place(x=30,y=160)
        pt_p = Label(frame3,text="-    15",font=("Arial 20")).place(x=320,y=160)
        spin1 = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin1.place(x=470,y=165)
       
        ct = Label(frame3,text="Chappati",font=("Arial 20")).place(x=30,y=200)
        ct_p = Label(frame3,text="-    12",font=("Arial 20")).place(x=320,y=200)
        spin2 = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin2.place(x=470,y=205)
       
        ss = Label(frame3,text="Samosa",font=("Arial 20")).place(x=30,y=240)
        ss_p = Label(frame3,text="-    10",font=("Arial 20")).place(x=320,y=240)
        spin3 = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin3.place(x=470,y=245)
       
        il = Label(frame3,text="Idaly",font=("Arial 20")).place(x=30,y=280)
        il_P = Label(frame3,text="-      8",font=("Arial 20")).place(x=320,y=280)
        spin4 = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin4.place(x=470,y=285)
       
        cp = Label(frame3,text="Chilli Potato",font=("Arial 20")).place(x=30,y=320)
        cp_p = Label(frame3,text="-    20",font=("Arial 20")).place(x=320,y=320)
        spin5 = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin5.place(x=470,y=325)
       
        gj = Label(frame3,text="Gulab Jamun",font=("Arial 20")).place(x=30,y=360)
        gj_p = Label(frame3,text="-    50",font=("Arial 20")).place(x=320,y=360)
        spin6 = Spinbox(frame3, from_=0, to=10,width=5,font='Times 15')
        spin6.place(x=470,y=365)

        def calculate():
            bd_pr = int(spin.get())
            ds_pr = int(spin0.get())
            pt_pr = int(spin1.get())
            ct_pr = int(spin2.get())
            ss_pr = int(spin3.get())
            il_pr = int(spin4.get())
            cp_pr = int(spin5.get())
            gj_pr = int(spin6.get())

            total = (bd_pr*150) + (ds_pr*10) + (pt_pr*15) + (ct_pr*12) + (ss_pr*10) + (il_pr*8) + (cp_pr*20) + (gj_pr*50)
            total_cost = str(total)
            tal_e.insert(END,total_cost)

        totl_btn = Button(frame3,text="Total",font=20,command=calculate,width=6).place(x=320,y=410)
        back_btn = Button(frame3,text="Back",font=20,command=lambda:[close(order),home()],width=6).place(x=240,y=410)
        tal_e = Entry(frame3,font=("Arial 15"),width=6)
        tal_e.place(x=470,y=415)
        def msg():
            tal = tal_e.get()
            if tal == "":
                messagebox.showinfo("info","Select Items")
            else:
                messagebox.showinfo("info","Successfully Ordered")
        ord_btn = Button(order,text="Order",font=20,command=msg,width=6).place(x=700,y=690)
        lgt = Button(order,text="Logout",command=lambda:[close(order),home()]).place(x=740,y=5)
           


        order.mainloop()

    login_btn = Button(frame,text="Login",fg="#FEFC04",bg="black",command=lambda:[close(root),login()],width=15).place(x=540,y=140)

    order_btn = Button(root,text="Order Now!",fg="white",bg="black",command=lambda:[close(root),login()],font=("Arial 15")).place(x=185,y=280)

    root.mainloop()

n = home()


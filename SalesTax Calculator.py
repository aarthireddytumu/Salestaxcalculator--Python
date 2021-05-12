from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry

class SalesTax():
    def __init__(self): #this is a inbuilt func in python , it gets executed when the class is instantiated, Self parameter is a reference to the current instance of the class and is used to access variable that belong to the class
        window = Tk()
        window.title("Sales Tax Calculator")
        window.configure(background="grey")
        window.geometry("380x320")
        window.resizable(width=False,height=False)

        self.beforetaxprice = StringVar()
        self.saletaxrate = IntVar()
        self.salestax = StringVar()
        self.aftertaxprice = StringVar()

        salestaxrate = Label(window,text="Tax Rate",bg="black",fg="white")
        salestaxrate.grid(column=0,row=0,padx=15,pady=15)

        beforetaxrate = Label(window,text="Before Tax Price",bg="black",fg="white")
        beforetaxrate.grid(column=1,row=0,padx=15,pady=15)
        beforetaxrate_entry = Entry(window,textvariable = self.beforetaxprice,width=14)
        beforetaxrate_entry.grid(column=2,row=0)

        fivepercent_tax = Radiobutton(window,text="0.5%",variable=self.saletaxrate,value=5)
        fivepercent_tax.grid(column=0,row=1)
        tenpercent_tax = Radiobutton(window,text="10%",variable=self.saletaxrate,value=10)
        tenpercent_tax.grid(column=0,row=2)
        fifteenpercent_tax = Radiobutton(window,text="15%",variable=self.saletaxrate,value=15)
        fifteenpercent_tax.grid(column=0,row=3)
        twentypercent_tax = Radiobutton(window,text="20%",variable=self.saletaxrate,value=20)
        twentypercent_tax.grid(column=0,row=4)
        twentyfivepercent_tax = Radiobutton(window,text="25%",variable=self.saletaxrate,value=25)
        twentyfivepercent_tax.grid(column=0,row=5)
        thirtypercent_tax = Radiobutton(window,text="30%",variable=self.saletaxrate,value=30)
        thirtypercent_tax.grid(column=0,row=6)

        taxamount_lbl = Label(window,text="Tax Amount",bg="black",fg="white")
        taxamount_lbl.grid(column=1,row=3,padx=15)
        taxamount_entry = Entry(window,textvariable=self.salestax,width=14)
        taxamount_entry.grid(column=2,row=3)

        aftertaxrate = Label(window,text="After Tax Price",bg="black",fg="white")
        aftertaxrate.grid(column=1,row=5,padx=15)
        aftertaxrate_entry = Entry(window,textvariable = self.aftertaxprice,width=14)
        aftertaxrate_entry.grid(column=2,row=5)

        convert_btn = Button(window,text="Calculate",bg="white",fg="black",width=14,command=self.calculate)  #command acts like a placeholder where u enter the function name
        convert_btn.grid(column=1,row=7,padx=15,pady=25)

        clear_btn = Button(window,text="Clear",bg="white",fg="black",width=14,command=self.clear)
        clear_btn.grid(column=2,row=7,padx=15,pady=25)

        window.mainloop()

    def calculate(self):
        beforetax = float(self.beforetaxprice.get())
        taxpercent = self.saletaxrate.get() / 100
        taxamnt = beforetax * taxpercent
        self.salestax.set(taxamnt)

        aftertax = beforetax + taxamnt
        self.aftertaxprice.set(aftertax)

    def clear(self):
        self.beforetaxprice.set("")
        self.salestax.set("")
        self.aftertaxprice.set("")


SalesTax()

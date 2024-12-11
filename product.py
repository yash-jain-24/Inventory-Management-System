from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Jain Chemicals")
        self.root.config(bg="white")
        self.root.focus_force()
        #========================================
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=550,height=620)
        
         #===title===
        title=Label(product_frame,text="Manage Products Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        lbl_category=Label(product_frame,text="Category",font=("goudy old style",18),bg="white").place(x=40,y=60)
        lbl_supplier=Label(product_frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=40,y=140)
        lbl_product_name=Label(product_frame,text="Name",font=("goudy old style",18),bg="white").place(x=40,y=220)
        lbl_price=Label(product_frame,text="Price",font=("goudy old style",18),bg="white").place(x=40,y=300)
        lbl_quantity=Label(product_frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=40,y=380)
        lbl_status=Label(product_frame,text="Status",font=("goudy old style",18),bg="white").place(x=40,y=460)
        
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=180,y=60,width=230)
        cmb_cat.current(0)    
        

if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop() 
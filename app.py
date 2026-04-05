from tkinter import * 
from tkinter import ttk
import random,os
from PIL import Image,ImageTk
import mysql.connector 
from tkinter import messagebox
import tempfile


def main():
   win = Tk()
   obj=Forensic(win)
   win.mainloop()

class Forensic:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('FORENSIC MANAGEMENT SYSTEM')
        
        #variables
        self.var_caseid=StringVar()
        self.var_body_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_register_date=StringVar()
        self.var_date_of_death=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occuption=StringVar()
        self.var_birthMark=StringVar()
        self.var_death_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_crictal_death=StringVar()
        
        lbl_title=Label(self.root,text='FORENSIC ',font=('times new roman',20,'bold'),bg='#a0b0e2',fg='black',bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=540,height=70)
        
        lbl_title=Label(self.root,text=' MANAGEMENT ',font=('times new roman',20,'bold'),bg='#cdb4e6',fg='black',bd=2,relief=RIDGE)
        lbl_title.place(x=540,y=0,width=540,height=70)
        
        lbl_title=Label(self.root,text='SYSTEM',font=('times new roman',20,'bold'),bd=2,relief=RIDGE,bg='#a8acea',fg='black')
        lbl_title.place(x=1080,y=0,width=540,height=70)
        
        #logo

    
        img3 = Image.open("image/logo.jpg")
        img3= img3.resize((150,120),Image.Resampling.LANCZOS)
        self.photoimg9= ImageTk.PhotoImage(img3)
        
        self.logo=Label(self.root,image=self.photoimg9)
        self.logo.place(x=20,y=5,width=150,height=60) 
        
        #img frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)
        
        img2 = Image.open("image/1.jpeg")
        img2= img2.resize((540,160),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        
        self.ph2=Label(img_frame,image=self.photoimg3)
        self.ph2.place(x=0,y=0,width=540,height=160)
        
        img1 = Image.open("image/3.jpg")
        img1= img1.resize((540,160),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        
        self.ph3=Label(img_frame,image=self.photoimg2)
        self.ph3.place(x=540,y=0,width=540,height=160)
        
        img0 = Image.open("image/th.jpeg")
        img0 = img0.resize((540,160),Image.Resampling.LANCZOS)
        self.photoimg0 = ImageTk.PhotoImage(img0)
        
        self.ph4=Label(img_frame,image=self.photoimg0)
        self.ph4.place(x=1080,y=0,width=540,height=160)
        
        # ==================#Main Frame==========================
        
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=795,height=580)
        
        # Upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Body Infromation',font=('times new roman',11,'bold'),fg='red',bg='light grey')
        upper_frame.place(x=10,y=10,width=770,height=560)
        
        # img bg main frame
        
        imgbg = Image.open("image/FOR.jpg")
        imgbg = imgbg.resize((770,560),Image.Resampling.LANCZOS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)
        
        self.ph5=Label(upper_frame,image=self.photoimgbg)
        self.ph5.place(x=0,y=0,width=770,height=550)
        
         
        # Labels Entry
         
         # case id
        caseid=Label(upper_frame,text='Case ID:',font=('Garamond',11,'bold'))
        caseid.grid(row=0,column=0,padx=2,sticky=W)
         
        caseentry=ttk.Entry(upper_frame,textvariable=self.var_caseid,width=22,font=('Garamond',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
         
         # patient No
        lbl_patient_no=Label(upper_frame,font=("Garamond",11,"bold"),text='Body_No:')
        lbl_patient_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)
         
        txt_patient_no=ttk.Entry(upper_frame,textvariable=self.var_body_no,width=22,font=('Garamond',11,'bold'))
        txt_patient_no.grid(row=0,column=3,padx=2,pady=7)
         
         # Patient Name
        lbl_Name=Label(upper_frame,font=("Garamond",12,"bold"),text="Body Name:")
        lbl_Name.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("Garamond",11,"bold"))
        txt_address.grid(row=1,column=1,padx=7,pady=7)
        
        # Gaurdian cont no
        lbl_nickname=Label(upper_frame,font=("Garamond",12,"bold"),text="Gaurdian cont no")
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)
         
        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=("Garamond",11,"bold"))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)
         
        
        #Arrest Date
        lbl_arrestDate=Label(upper_frame,font=("Garamond",12,"bold"),text="register_Date:")
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)
         
        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_register_date,width=22,font=("Garamond",11,"bold"))
        txt_arrestDate.grid(row=2,column=1,padx=7,pady=7)
        
        # Date of Crime
        lbl_dateofCrime=Label(upper_frame,font=("Garamond",12,"bold"),text="Date of death:")
        lbl_dateofCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)
         
        txt_dateofCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_death,width=22,font=("Garamond",11,"bold"))
        txt_dateofCrime.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        # Address
        lbl_address=Label(upper_frame,font=("Garamond",12,"bold"),text="Address")
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("Garamond",11,"bold"))
        txt_address.grid(row=3,column=1,padx=7,pady=7)
        
        # Age
        lbl_age=Label(upper_frame,font=("Garamond",12,"bold"),text="Age")
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=("Garamond",11,"bold"))
        txt_age.grid(row=3,column=3,padx=2,pady=7)
        
        # occuption
        lbl_occuption=Label(upper_frame,font=("Garamond",12,"bold"),text="Occuption")
        lbl_occuption.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        txt_occuption=ttk.Entry(upper_frame,textvariable=self.var_occuption,width=22,font=("Garamond",11,"bold"))
        txt_occuption.grid(row=4,column=1,padx=7,pady=7)
        
        
        # birthmark
        lbl_birthmark=Label(upper_frame,font=("Garamond",12,"bold"),text="Birth Mark")
        lbl_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=("Garamond",11,"bold"))
        txt_birthmark.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
        # Death Type
        lbl_patienttype=Label(upper_frame,font=("Garamond",12,"bold"),text="Death Type")
        lbl_patienttype.grid(row=5,column=0,sticky=W,padx=2,pady=7)
        
        # txt_deathtype=ttk.Entry(upper_frame,textvariable=self.var_death_type,width=22,font=("Garamond",11,"bold"))
        # txt_deathtype.grid(row=5,column=1,padx=7,pady=7)
        
        combo_search_box=ttk.Combobox(upper_frame,textvariable=self.var_death_type,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select','Murder','Accident','Suicide')
        combo_search_box.current(0)
        combo_search_box.grid(row=5,column=1,sticky=W,padx=5)
        
        
        # Father Name
        lbl_fathername=Label(upper_frame,font=("Garamond",12,"bold"),text="Father Name")
        lbl_fathername.grid(row=5,column=2,sticky=W,padx=2,pady=7)
        
        txt_fathername=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=("Garamond",11,"bold"))
        txt_fathername.grid(row=5,column=3,padx=2,pady=7)
        
        # gender
        lbl_gender=Label(upper_frame,font=("Garamond",12,"bold"),text="Gender")
        lbl_gender.grid(row=6,column=0,sticky=W,padx=2,pady=15)
       
        # Radio Button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE)
        radio_frame_gender.place(x=107,y=233,width=260,height=30)
        
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text="Male",value='male',font=("Garamond",9,"bold"),bg="white")
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text="Female",value='female',font=("Garamond",9,"bold"),bg="white")
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        
        transgender=Radiobutton(radio_frame_gender,variable=self.var_gender,text="TransGender",value='transgender',font=("Garamond",9,"bold"),bg="white")
        transgender.grid(row=0,column=2,pady=2,padx=5,sticky=W)
        
        # wanted
        lbl_wanted=Label(upper_frame,font=("Garamond",12,"bold"),text="Critical death",)
        lbl_wanted.grid(row=7,column=0,sticky=W,padx=2,pady=7)
    
        # Radio Button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_wanted.place(x=107,y=285,width=190,height=30)
        
        Yes=Radiobutton(radio_frame_wanted,variable=self.var_crictal_death,text="Yes",value='yes',font=("Garamond",9,"bold"),bg="white")
        Yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        No=Radiobutton(radio_frame_wanted,text="No",variable=self.var_crictal_death,value='no',font=("Garamond",9,"bold"),bg="white")
        No.grid(row=0,column=1,pady=2,padx=5,sticky=W)
    
        # Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE)
        button_frame.place(x=5,y=350,width=630,height=45)
        
        print_frame=Frame(upper_frame,bd=2,relief=RIDGE)
        print_frame.place(x=5,y=400,width=320,height=45)
        
        #add button -----
        
        btn_add=Button(button_frame,command=self.add_data,text='Record save',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)
        #Update button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
         
         #Delete button     
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)
         
         #Clear button
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)
        
         #print button
        btn_select=Button(print_frame,command=self.gen_bill,text='Select',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
        btn_select.grid(row=0,column=0,padx=3,pady=5)
        btn_print=Button(print_frame,command=self.save_bill,text='Print',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
        btn_print.grid(row=0,column=2,padx=3,pady=5)
        
        #background rigth side image  
         
        img5 = Image.open("image/th.jpeg")
        img5= img3.resize((470,245),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        self.bg=Label(upper_frame,image=self.photoimg5)
        self.bg.place(x=1000,y=0,width=470,height=245) 
         
         
         
        # Down Frame
        down_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Patient Infromation Table',font=('times new roman',11,'bold'),fg='red',bg='lightgrey')
        down_frame.place(x=810,y=205,width=730,height=300)
        # Search Frame 
        # search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Patient Record',font=('times new roman',11,'bold'),fg='red',bg='lightgrey')
        # search_frame.place(x=0,y=0,width=1070,height=60)
        
        
        search_by=Label(down_frame,font=("arial",11,"bold"),text="Search By",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        
        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(down_frame,textvariable=self.var_com_search,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','case_id','Body_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
        
        self.var_search=StringVar()
        search_txt=ttk.Entry(down_frame,textvariable=self.var_search,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)
        
        
         # search button     
        btn_search=Button(down_frame,command=self.search_data,text='Search',font=("arial",11,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3) 
        
        # all button
        btn_all=Button(down_frame,command=self.fetch_data,text='Show All',font=("arial",11,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,)
        
        # forency=Label(down_frame,font=("arial",15,"bold"),text="NATIONAL FORENSIC AGENCY",bg="white",fg='crimson')
        # forency.grid(row=0,column=5,sticky=W,padx=50)
        
        # table frame
        # ====================================================== ===========================================
        Print_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='SAVE INFORMATION',font=('times new roman',11,'bold'),fg='red',bg='lightgrey')
        Print_frame.place(x=810,y=510,width=730,height=300)
        
        scroll_y=ttk.Scrollbar(Print_frame,orient=VERTICAL) 
        self.textarea=Text(Print_frame,yscrollcommand=scroll_y.set,bg="grey",fg="white",font=("arial",9,"bold")) 
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
         
        
        scroll_x=ttk.Scrollbar(Print_frame,orient=HORIZONTAL) 
        scroll_x.pack(side=BOTTOM,fill=X)
        
        
        scroll_x.config(command=self.textarea.xview)
        
       
        # =========================================================== ===============================================
        table_frame=Frame(down_frame,bd=2,relief=RIDGE,bg='grey')
        table_frame.place(x=0,y=40,width=720,height=240)
        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL) 
        
        self.body_table=ttk.Treeview(table_frame,columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.body_table.xview)
        scroll_y.config(command=self.body_table.yview)
        
        self.body_table.heading('1',text="CaseId")
        self.body_table.heading("2",text="BodyNo")
        self.body_table.heading("3",text="BodyName")
        self.body_table.heading("4",text="Gaurdian cont no")
        self.body_table.heading("5",text="Death Date")
        self.body_table.heading("6",text="AutopsyofDate")
        self.body_table.heading("7",text="Address")
        self.body_table.heading("8",text="Age")
        self.body_table.heading("9",text="Occuption")
        self.body_table.heading("10",text="Birth Mark")
        self.body_table.heading("11",text="Death Type")
        self.body_table.heading("12",text="Father Name")
        self.body_table.heading("13",text="Gender")
        self.body_table.heading("14",text="CriticalDeath")
        
        self.body_table['show']='headings'
        
        self.body_table.column("1",width=100)
        self.body_table.column("2",width=100)
        self.body_table.column("3",width=100)
        self.body_table.column("4",width=100)
        self.body_table.column("5",width=100)
        self.body_table.column("6",width=100)
        self.body_table.column("7",width=100)
        self.body_table.column("8",width=100)
        self.body_table.column("9",width=100)
        self.body_table.column("10",width=100)
        self.body_table.column("11",width=100)
        self.body_table.column("12",width=100)
        self.body_table.column("13",width=100)
        self.body_table.column("14",width=100)
        
        
        self.body_table.pack(fill=BOTH,expand=1)
        
        self.body_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  
        self.welcome()
        
        
        
    # ==============================================================INVOICE OF DATA=======================================
        
    def welcome(self):     
        self.textarea.delete(1.0,END) 
        self.textarea.insert(END,"\t\t\t Forensic Report")
        self.textarea.insert(END,f"\n Case ID:\t{self.var_caseid.get()}")
        self.textarea.insert(END,f'\n Body Name:\t{self.var_name.get()}')
        self.textarea.insert(END,f"\n Body_No:\t{self.var_body_no.get()}")
        self.textarea.insert(END,f"\n Guardian No.:\t{self.var_nickname.get()}")
        self.textarea.insert(END,"\n===================================================================================================")
        self.textarea.insert(END,f"\n \t\t\tFORENSIC DATA OF BODY")
        self.textarea.insert(END,"\n===================================================================================================")
        
         
    def gen_report(self): 
        if self.var_caseid.get() == "":
            messagebox.showerror("Error","Please Fill the details",parent=self.root)
        else:
            text=self.textarea.get(10.0,END)
            self.welcome()
            self.textarea.insert(END,text)
            # self.textarea.insert(END,f"\n {self.var_roomtype.get()}\t\t{self.var_noofdays.get()}\t\t{self.var_meal.get()}\t\t{self.var_actualtotal.get()}")
            # self.textarea.insert(END,f"\n===================================================================================================")
            self.textarea.insert(END,f"\n \tRegister_Date:\t\t{self.var_register_date.get()}\t\tDate Of Death:\t{self.var_date_of_death.get()}")
            self.textarea.insert(END,f"\n \tAddress:\t\t{self.var_address.get()}\t\tAge:{self.var_age.get()}")
            self.textarea.insert(END,f"\n \tOccupation:\t\t{self.var_occuption.get()}\t\tBirth Mark:\t{self.var_birthMark.get()}")
            self.textarea.insert(END,f"\n \tDeath Type:\t\t{self.var_death_type.get()}\t\tFather Name:\t{self.var_father_name.get()}")
            self.textarea.insert(END,f"\n \tGender:\t\t{self.var_gender.get()}")
            self.textarea.insert(END,f"\n \tCritical Death:\t\t{self.var_crictal_death.get()}")
            self.textarea.insert(END,f"\n===================================================================================================")    
        
    def save_bill(self):
        op=messagebox.askyesno("Save Report","Do you want to save the Report",parent=self.root)
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('Data/'+str(self.var_caseid.get())+".txt",'w')
            f1.write(self.bill_data)
            messagebox.showinfo("Saved",f"Report No:{self.var_caseid.get()}Saved successfully",parent=self.root)
            f1.close()  
            self.iprint()
        
            
    
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
    
    

    
    
    
    
    
    
    
    
    
    
#    =========================================================================================================================================
   
    
    # Add Function
    def add_data(self):
        if self.var_caseid.get()=="":
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into forensic values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                           self.var_caseid.get(),
                                                                                                           self.var_body_no.get(),
                                                                                                           self.var_name.get(),
                                                                                                           self.var_nickname.get(),
                                                                                                           self.var_register_date.get(),
                                                                                                           self.var_date_of_death.get(),
                                                                                                           self.var_address.get(),
                                                                                                           self.var_age.get(),
                                                                                                           self.var_occuption.get(),
                                                                                                           self.var_birthMark.get(),
                                                                                                           self.var_death_type.get(),
                                                                                                           self.var_father_name.get(),
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_crictal_death.get() 
                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','forensic record has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}',parent=self.root)
                
    # fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
         my_cursor=conn.cursor()
         my_cursor.execute('select * from forensic')
         data=my_cursor.fetchall()
         if len(data)!=0:
             self.body_table.delete(*self.body_table.get_children())
             for i in data:
                 self.body_table.insert('',END,values=i)
             conn.commit()
         conn.close()
         
    # get cursor
    def get_cursor(self,event=""):
        cursur_row=self.body_table.focus()
        content=self.body_table.item(cursur_row)
        data=content['values']
        
        self.var_caseid.set(data[0])
        self.var_body_no.set(data[1])
        self.var_name.set(data[2]) 
        self.var_nickname.set(data[3])
        self.var_register_date.set(data[4])
        self.var_date_of_death.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occuption.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_death_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_crictal_death.set(data[13])
                           
                            
    #update
    def  update_data(self):
        if self.var_caseid.get()=="":
            messagebox.showerror('Error','All filds are required',parent=self.root)
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this patient record',parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update forensic set body_no=%s,body_name=%s,find=%s,register_date=%s,death_of_date=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,deathType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(
                                                                                                                                                                                                                                       
                        
                                                                                                                                                                                                                                       self.var_body_no.get(),
                                                                                                                                                                                                                                       self.var_name.get(),
                                                                                                                                                                                                                                       self.var_nickname.get(),
                                                                                                                                                                                                                                       self.var_register_date.get(),
                                                                                                                                                                                                                                       self.var_date_of_death.get(),
                                                                                                                                                                                                                                       self.var_address.get(),
                                                                                                                                                                                                                                       self.var_age.get(),
                                                                                                                                                                                                                                       self.var_occuption.get(),
                                                                                                                                                                                                                                       self.var_birthMark.get(),
                                                                                                                                                                                                                                       self.var_death_type.get(),
                                                                                                                                                                                                                                       self.var_father_name.get(),
                                                                                                                                                                                                                                       self.var_gender.get(),
                                                                                                                                                                                                                                       self.var_crictal_death.get(), 
                                                                                                                                                                                                                                       self.var_caseid.get()
                                                                                                                                                                                                                                     ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Patient record successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')        
                                                                                                                                                                                                                                       
           
    # delete
    def delete_data(self):
        if self.var_caseid.get()=="":
            messagebox.showerror('Error','All filds are required',parent=self.root)
        else:
            try:
                delete=messagebox.askyesno('delete','Are you sure delete the patient record',parent=self.root)
                if delete>0:
                 conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
                 my_cursor=conn.cursor()
                 sql='delete from forensic where Case_id=%s'
                 value=(self.var_caseid.get(),)
                 my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close() 
                messagebox.showinfo('Success','Patient record successfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}',parent=self.root)
        
        
    # clear
    def clear_data(self):            
        self.var_caseid.set("")
        self.var_body_no.set("")
        self.var_name.set("") 
        self.var_nickname.set("")
        self.var_register_date.set("")
        self.var_date_of_death.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occuption.set("")
        self.var_birthMark.set("")
        self.var_death_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_crictal_death.set("")
        self.textarea.delete(1.0,END)
        self.welcome() 
        
        
    # search
    def search_data(self):
        if self.var_search.get()=="":
             messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
                my_cursor=conn.cursor()
                
                my_cursor.execute('select * from forensic where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                
                if len(rows)!=0:
                    self.body_table.delete(*self.body_table.get_children())
                    for i in rows:
                       self.body_table.insert('',END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}',parent=self.root)
            
                     
                
            
                
#     def print_window(self):
#         self.new_win=Toplevel(self.root)
#         self.app=Print(self.new_win)
         
# class Print:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry('1530x790+0+0')
#         self.root.title('FORENSIC MANAGEMENT SYSTEM')
        
#         #variables
#         self.var_caseid=StringVar()
#         self.var_body_no=StringVar()
#         self.var_name=StringVar()
#         self.var_nickname=StringVar()
#         self.var_register_date=StringVar()
#         self.var_date_of_death=StringVar()
#         self.var_address=StringVar()
#         self.var_age=StringVar()
#         self.var_occuption=StringVar()
#         self.var_birthMark=StringVar()
#         self.var_death_type=StringVar()
#         self.var_father_name=StringVar()
#         self.var_gender=StringVar()
#         self.var_crictal_death=StringVar()
        
        
         
#         # Upper Frame
#         upper_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Body Infromation',font=('times new roman',11,'bold'),fg='red',bg='light grey')
#         upper_frame.place(x=0,y=0,width=795,height=460)
        
#         # img bg main frame
        
#         imgbg = Image.open("image/FOR.jpg")
#         imgbg = imgbg.resize((830,460),Image.Resampling.LANCZOS)
#         self.photoimgbg = ImageTk.PhotoImage(imgbg)
        
#         self.ph5=Label(upper_frame,image=self.photoimgbg)
#         self.ph5.place(x=0,y=0,width=830,height=460)
       
        
         
#         # case id
#         caseid=Label(upper_frame,text='Case ID:',font=('Garamond',11,'bold'))
#         caseid.grid(row=0,column=0,padx=2,sticky=W)
         
#         caseentry=ttk.Entry(upper_frame,textvariable=self.var_caseid,width=22,font=('Garamond',11,'bold'))
#         caseentry.grid(row=0,column=1,padx=2,sticky=W)
         
#         # patient No
#         lbl_patient_no=Label(upper_frame,font=("Garamond",11,"bold"),text='Body_No:')
#         lbl_patient_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)
         
#         txt_patient_no=ttk.Entry(upper_frame,textvariable=self.var_body_no,width=22,font=('Garamond',11,'bold'))
#         txt_patient_no.grid(row=0,column=3,padx=2,pady=7)
         
#         # Patient Name
#         lbl_Name=Label(upper_frame,font=("Garamond",12,"bold"),text="Body Name:")
#         lbl_Name.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
#         txt_address=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("Garamond",11,"bold"))
#         txt_address.grid(row=1,column=1,padx=7,pady=7)
        
#         # Gaurdian cont no
#         lbl_nickname=Label(upper_frame,font=("Garamond",12,"bold"),text="Gaurdian cont no")
#         lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)
         
#         txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=("Garamond",11,"bold"))
#         txt_nickname.grid(row=1,column=3,padx=2,pady=7)
         
        
#         #Arrest Date
#         lbl_arrestDate=Label(upper_frame,font=("Garamond",12,"bold"),text="register_Date:")
#         lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)
         
#         txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_register_date,width=22,font=("Garamond",11,"bold"))
#         txt_arrestDate.grid(row=2,column=1,padx=7,pady=7)
        
#         # Date of Crime
#         lbl_dateofCrime=Label(upper_frame,font=("Garamond",12,"bold"),text="Date of death:")
#         lbl_dateofCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)
         
#         txt_dateofCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_death,width=22,font=("Garamond",11,"bold"))
#         txt_dateofCrime.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
#         # Address
#         lbl_address=Label(upper_frame,font=("Garamond",12,"bold"),text="Address")
#         lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
#         txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("Garamond",11,"bold"))
#         txt_address.grid(row=3,column=1,padx=7,pady=7)
        
#         # Age
#         lbl_age=Label(upper_frame,font=("Garamond",12,"bold"),text="Age")
#         lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
#         txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=("Garamond",11,"bold"))
#         txt_age.grid(row=3,column=3,padx=2,pady=7)
        
#         # occuption
#         lbl_occuption=Label(upper_frame,font=("Garamond",12,"bold"),text="Occuption")
#         lbl_occuption.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
#         txt_occuption=ttk.Entry(upper_frame,textvariable=self.var_occuption,width=22,font=("Garamond",11,"bold"))
#         txt_occuption.grid(row=4,column=1,padx=7,pady=7)
        
        
#         # birthmark
#         lbl_birthmark=Label(upper_frame,font=("Garamond",12,"bold"),text="Birth Mark")
#         lbl_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
#         txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=("Garamond",11,"bold"))
#         txt_birthmark.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
#         # Death Type
#         lbl_patienttype=Label(upper_frame,font=("Garamond",12,"bold"),text="Death Type")
#         lbl_patienttype.grid(row=5,column=0,sticky=W,padx=2,pady=7)
        
#         # txt_deathtype=ttk.Entry(upper_frame,textvariable=self.var_death_type,width=22,font=("Garamond",11,"bold"))
#         # txt_deathtype.grid(row=5,column=1,padx=7,pady=7)
        
#         combo_search_box=ttk.Combobox(upper_frame,textvariable=self.var_death_type,font=("arial",11,"bold"),width=18,state='readonly')
#         combo_search_box['value']=('Select','Murder','Accident','Suicide')
#         combo_search_box.current(0)
#         combo_search_box.grid(row=5,column=1,sticky=W,padx=5)
        
        
#         # Father Name
#         lbl_fathername=Label(upper_frame,font=("Garamond",12,"bold"),text="Father Name")
#         lbl_fathername.grid(row=5,column=2,sticky=W,padx=2,pady=7)
        
#         txt_fathername=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=("Garamond",11,"bold"))
#         txt_fathername.grid(row=5,column=3,padx=2,pady=7)
        
#         # gender
#         lbl_gender=Label(upper_frame,font=("Garamond",12,"bold"),text="Gender")
#         lbl_gender.grid(row=6,column=0,sticky=W,padx=2,pady=15)
       
#         # Radio Button gender
#         radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE)
#         radio_frame_gender.place(x=107,y=233,width=260,height=30)
        
#         male=Radiobutton(radio_frame_gender,variable=self.var_gender,text="Male",value='male',font=("Garamond",9,"bold"),bg="white")
#         male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
#         female=Radiobutton(radio_frame_gender,variable=self.var_gender,text="Female",value='female',font=("Garamond",9,"bold"),bg="white")
#         female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        
#         transgender=Radiobutton(radio_frame_gender,variable=self.var_gender,text="TransGender",value='transgender',font=("Garamond",9,"bold"),bg="white")
#         transgender.grid(row=0,column=2,pady=2,padx=5,sticky=W)
        
#         # wanted
#         lbl_wanted=Label(upper_frame,font=("Garamond",12,"bold"),text="Critical death",)
#         lbl_wanted.grid(row=7,column=0,sticky=W,padx=2,pady=7)
    
#         # Radio Button wanted
#         radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
#         radio_frame_wanted.place(x=107,y=285,width=190,height=30)
        
#         Yes=Radiobutton(radio_frame_wanted,variable=self.var_crictal_death,text="Yes",value='yes',font=("Garamond",9,"bold"),bg="white")
#         Yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
#         No=Radiobutton(radio_frame_wanted,text="No",variable=self.var_crictal_death,value='no',font=("Garamond",9,"bold"),bg="white")
#         No.grid(row=0,column=1,pady=2,padx=5,sticky=W)
    
#         # Buttons
#         button_frame=Frame(upper_frame,bd=2,relief=RIDGE)
#         button_frame.place(x=5,y=350,width=315,height=45)
        
#         # button -----
        
#         btn_add=Button(button_frame,command=self.Msg_button,text='Print',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
#         btn_add.grid(row=0,column=0,padx=3,pady=5)
        
#         #Update button
#         btn_update=Button(button_frame,command=self.Back,text='Back',font=("Garamond",13,"bold"),width=14,bg='blue',fg='white')
#         btn_update.grid(row=0,column=1,padx=3,pady=5)
         
         
             
            
#     #  ----------------------------------------------search_by and DATABASE---------------------------     
    
         
#         # Down Frame
#         down_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Patient Infromation Table',font=('times new roman',11,'bold'),fg='red',bg='lightgrey')
#         down_frame.place(x=810,y=0,width=730,height=460)
        
#         # Search Frame 
#         search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Patient Record',font=('times new roman',11,'bold'),fg='red',bg='lightgrey')
#         search_frame.place(x=0,y=0,width=1070,height=60)
        
#         search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By",bg="red",fg="white")
#         search_by.grid(row=0,column=0,sticky=W,padx=5)
        
#         self.var_com_search=StringVar()
#         combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",11,"bold"),width=18,state='readonly')
#         combo_search_box['value']=('Select Option','case_id','Body_no')
#         combo_search_box.current(0)
#         combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
        
#         self.var_search=StringVar()
#         search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=("arial",11,"bold"))
#         search_txt.grid(row=0,column=2,sticky=W,padx=5)
        
        
#          # search button     
#         btn_search=Button(search_frame,command=self.search_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
#         btn_search.grid(row=0,column=3,padx=3,pady=5) 
        
#         # all button
#         btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
#         btn_all.grid(row=0,column=4,padx=3,pady=5)
        
#         forency=Label(search_frame,font=("arial",30,"bold"),text="NATIONAL FORENSIC AGENCY",bg="white",fg='crimson')
#         forency.grid(row=0,column=5,sticky=W,padx=50,pady=0)
        
#         # ---------------------------------img-----------------------------
        
#          #img frame
#         img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='grey')
#         img_frame.place(x=0,y=460,width=1530,height=340)
        
#         img2 = Image.open("image/a.jpg")
#         img2= img2.resize((520,370),Image.Resampling.LANCZOS)
#         self.photoimg3 = ImageTk.PhotoImage(img2)
        
#         self.ph2=Label(img_frame,image=self.photoimg3)
#         self.ph2.place(x=0,y=0,width=520,height=340)
        
#         img1 = Image.open("image/b.jpg")
#         img1= img1.resize((520,370),Image.Resampling.LANCZOS)
#         self.photoimg2 = ImageTk.PhotoImage(img1)
        
#         self.ph3=Label(img_frame,image=self.photoimg2)
#         self.ph3.place(x=480,y=0,width=520,height=340)
        
#         img0 = Image.open("image/s.jpg")
#         img0 = img0.resize((520,370),Image.Resampling.LANCZOS)
#         self.photoimg0 = ImageTk.PhotoImage(img0)
        
#         self.ph4=Label(img_frame,image=self.photoimg0)
#         self.ph4.place(x=1000,y=0,width=520,height=340)
    
        
        
#         # table frame
        
#         table_frame=Frame(down_frame,bd=2,relief=RIDGE,bg='lightgrey')
#         table_frame.place(x=0,y=60,width=700,height=380)
        
       
        
#         # Scroll bar
#         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL) 
        
#         self.body_table=ttk.Treeview(table_frame,columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)
        
#         scroll_x.config(command=self.body_table.xview)
#         scroll_y.config(command=self.body_table.yview)
        
#         self.body_table.heading('1',text="CaseId")
#         self.body_table.heading("2",text="BodyNo")
#         self.body_table.heading("3",text="BodyName")
#         self.body_table.heading("4",text="Gaurdian cont no")
#         self.body_table.heading("5",text="Death Date")
#         self.body_table.heading("6",text="AutopsyofDate")
#         self.body_table.heading("7",text="Address")
#         self.body_table.heading("8",text="Age")
#         self.body_table.heading("9",text="Occuption")
#         self.body_table.heading("10",text="Birth Mark")
#         self.body_table.heading("11",text="Death Type")
#         self.body_table.heading("12",text="Father Name")
#         self.body_table.heading("13",text="Gender")
#         self.body_table.heading("14",text="CriticalDeath")
        
#         self.body_table['show']='headings'
        
#         self.body_table.column("1",width=100)
#         self.body_table.column("2",width=100)
#         self.body_table.column("3",width=100)
#         self.body_table.column("4",width=100)
#         self.body_table.column("5",width=100)
#         self.body_table.column("6",width=100)
#         self.body_table.column("7",width=100)
#         self.body_table.column("8",width=100)
#         self.body_table.column("9",width=100)
#         self.body_table.column("10",width=100)
#         self.body_table.column("11",width=100)
#         self.body_table.column("12",width=100)
#         self.body_table.column("13",width=100)
#         self.body_table.column("14",width=100)
        
        
#         self.body_table.pack(fill=BOTH,expand=1)
        
#         self.body_table.bind("<ButtonRelease>",self.get_cursor)
#         self.fetch_data()  
    
#     # Add Function
#     def add_data(self):
#         if self.var_caseid.get()=="":
#             messagebox.showerror('Error','All fields are required')
#         else:
#             try:
#                 conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
#                 my_cursor=conn.cursor()
#                 my_cursor.execute('insert into forensic values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
#                                                                                                            self.var_caseid.get(),
#                                                                                                            self.var_body_no.get(),
#                                                                                                            self.var_name.get(),
#                                                                                                            self.var_nickname.get(),
#                                                                                                            self.var_register_date.get(),
#                                                                                                            self.var_date_of_death.get(),
#                                                                                                            self.var_address.get(),
#                                                                                                            self.var_age.get(),
#                                                                                                            self.var_occuption.get(),
#                                                                                                            self.var_birthMark.get(),
#                                                                                                            self.var_death_type.get(),
#                                                                                                            self.var_father_name.get(),
#                                                                                                            self.var_gender.get(),
#                                                                                                            self.var_crictal_death.get() 
#                                                                                                                                  ))
#                 conn.commit()
#                 self.fetch_data()
                
#                 conn.close()
#                 messagebox.showinfo('Success','forensic record has been added')
#             except Exception as es:
#                 messagebox.showerror('Error',f'Due To{str(es)}')
                
#     # fetch data
#     def fetch_data(self):
#          conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
#          my_cursor=conn.cursor()
#          my_cursor.execute('select * from forensic')
#          data=my_cursor.fetchall()
#          if len(data)!=0:
#              self.body_table.delete(*self.body_table.get_children())
#              for i in data:
#                  self.body_table.insert('',END,values=i)
#              conn.commit()
#          conn.close()
         
#     # get cursor
#     def get_cursor(self,event=""):
#         cursur_row=self.body_table.focus()
#         content=self.body_table.item(cursur_row)
#         data=content['values']
        
#         self.var_caseid.set(data[0])
#         self.var_body_no.set(data[1])
#         self.var_name.set(data[2]) 
#         self.var_nickname.set(data[3])
#         self.var_register_date.set(data[4])
#         self.var_date_of_death.set(data[5])
#         self.var_address.set(data[6])
#         self.var_age.set(data[7])
#         self.var_occuption.set(data[8])
#         self.var_birthMark.set(data[9])
#         self.var_death_type.set(data[10])
#         self.var_father_name.set(data[11])
#         self.var_gender.set(data[12])
#         self.var_crictal_death.set(data[13])
       
# #    search 
#     def search_data(self):
#         if self.var_search.get()=="":
#              messagebox.showerror('Error','All fields are required')
#         else:
#             try:
#                 conn=mysql.connector.connect(host='localhost',username='root',password='Rutuja@2121',database='forensic')
#                 my_cursor=conn.cursor()
                
#                 my_cursor.execute('select * from forensic where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
#                 rows=my_cursor.fetchall()
                
#                 if len(rows)!=0:
#                     self.body_table.delete(*self.body_table.get_children())
#                     for i in rows:
#                        self.body_table.insert('',END,values=i)
#                     conn.commit()
#                 conn.close()
#             except Exception as es:
#                 messagebox.showerror('Error',f'Due To{str(es)}')
            
    
   
   
        
        
        
#     def Msg_button(self):
#         if self.var_caseid.get()=="":
#             messagebox.showerror('Error','All filds are required',parent=self.root)
#         else:
#             messagebox.showinfo('Success','Forensic record printed successfully')
    
#     def Back(self):
#         self.root.destroy()
            
                           
                        
                                                                                                           
                        
                        
                        
                        
                        
                        
                        
         
                    
                    
            
        
if __name__=="__main__":
    
    main()
                
            
            
                           
                        
                                                                                                           
                        
                        
                        
                        
                        
                        
                        
         
                    
                    
            
        
# if __name__ =="__main__":
#     root = Tk()
#     obj=Forensic(root)
#     root.mainloop()

        

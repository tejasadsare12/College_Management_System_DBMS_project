from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk



class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        #1st
        img=Image.open(r"college_images\7th.jpg")
        img=img.resize((540,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

       #2nd
        img_2=Image.open(r"college_images\6th.jpg")
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_2.place(x=540,y=0,width=540,height=160) 

        #3rd
        img_3=Image.open(r"college_images\5th.jpg")
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=1000,y=0,width=540,height=160)

        #bg image

        img_4=Image.open(r"college_images\university.jpg")
        img_4=img_4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710) 

        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50) 
        
        #manage Frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="White")
        Manage_frame.place(x=15,y=55,width=1500,height=560)


        #left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="blue",bg="white")
        DataLeftFrame.place(x=10,y=10,width=660,height=540)

        #img
        img_5=Image.open(r"college_images\5th.jpg")
        img_5=img_5.resize((650,120),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(DataLeftFrame,image=self.photoimg,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=650,height=120)

        #Current course LabelFrame Information
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current course Information",font=("times new roman",12,"bold"),fg="blue",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=115)

        #Department
        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=2,padx=2,sticky=W)

        combo_dep=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #Course
        course_std=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Courses",bg="white")
        course_std.grid(row=0,column=0,sticky=W,padx=2,pady=10)

        com_txtcourse_std=ttk.Combobox(std_lbl_info_frame,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_txtcourse_std["value"]=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)

        #year
        course_year=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Year",bg="white")
        course_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_txtcourse_year=ttk.Combobox(std_lbl_info_frame,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_txtcourse_year["value"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        com_txtcourse_year.current(0)
        com_txtcourse_year.grid(row=1,column=1,sticky=W,padx=2,pady=10)

        #semester
        label_Semester=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Semester",bg="white")
        label_Semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        comSemester=ttk.Combobox(std_lbl_info_frame,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        comSemester["value"]=("Select Semester","Semester-1","Semester-2")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)
        
        #Student class LabelFrame Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=("times new roman",12,"bold"),fg="blue",bg="white")
        std_lbl_class_frame.place(x=0,y=235,width=650,height=250)

        #labels entry
        #ID
        lbl_id=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="StudentID:",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        id_entry =ttk.Entry(std_lbl_class_frame,font=("arial",11,"bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        # Name
        lbl_Name=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Student Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(std_lbl_class_frame,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Division
        lbl_div=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Class Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(std_lbl_class_frame,state="readonly",
                                                         font=("arial",12,"bold"),width=18)
        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)       
       
        # Roll
        lbl_roll=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Roll No:",bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        txt_roll=ttk.Entry(std_lbl_class_frame,width=22,font=("arial",11,"bold"))
        txt_roll.grid(row=1,column=3,padx=2,pady=7)

        # gender
        lbl_gender=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_gender=ttk.Combobox(std_lbl_class_frame,state="readonly",
                                                         font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # DOB
        lbl_dob=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        txt_dob=ttk.Entry(std_lbl_class_frame,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=2,column=3,padx=2,pady=7)

        #Email
        lbl_email=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt_email=ttk.Entry(std_lbl_class_frame,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=3,column=1,padx=2,pady=7)      

        # phone
        lbl_phone=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)  
        
        txt_phone=ttk.Entry(std_lbl_class_frame,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=7)

        #Address
        lbl_address=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=4,column=0,sticky=W,padx=2,pady=7)  
        
        txt_address=ttk.Entry(std_lbl_class_frame,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=4,column=1,padx=2,pady=7)

        #Teacher
        txt_teacher=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Teacher:",bg="white")
        txt_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)  
        
        txt_teacher=ttk.Entry(std_lbl_class_frame,width=22,font=("arial",11,"bold"))
        txt_teacher.grid(row=4,column=3,padx=2,pady=7)

        #Button Frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_Add=Button(btn_frame,text="Save",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_Reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Reset.grid(row=0,column=3,padx=1)


        #right frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="blue",bg="white")
        DataRightFrame.place(x=680,y=10,width=800,height=540)
        
        #img1
        img_6=Image.open(r"college_images\6th.jpg")
        img_6=img_6.resize((780,200),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_6)

        my_img=Label(DataRightFrame,image=self.photoimg,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=790,height=200)

        #right frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="blue",bg="white")
        Search_Frame.place(x=0,y=200,width=790,height=60)

        search_by=Label(Search_Frame,font=("arial",11,"bold"),text="Search By:",fg="red",bg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        com_txt_search=ttk.Combobox(Search_Frame,state="readonly",
                                                         font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","Roll","Phone","Student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        txt_search=ttk.Entry(Search_Frame,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(Search_Frame,text="Search",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(Search_Frame,text="Show All",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

        #----------- Student Table and Scroll Bar---------------
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=255)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)

        self.student_table.pack(fill=BOTH,expand=1)











if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()

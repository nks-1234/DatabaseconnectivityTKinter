from tkinter import *
import sqlite3
root = Tk()
root.title("Emplyoeedatabase")
root.geometry("550x300")
root.configure(background="blue")
 

def submit():
    #create a database
    db=sqlite3.connect("employeeDataBase.db")
   
    #create.cursor
    cu = db.cursor()
    
    cu.execute("create table if not exists employeeData(EID text,Name text,Designation text,Salary text)")

    #insert into table
    cu.execute("INSERT INTO employeeData(EID,Name,Designation,Salary) values(?,?,?,?)",(EID.get(),Name.get(),Designation.get(),Salary.get()))
    
    db.commit()
     
    db.close()
    
    
    #clear text boxes
    EID.delete(0, END)
    Name.delete(0, END)
    Designation.delete(0, END) 
    Salary.delete(0, END)

def show():
    
   
    db=sqlite3.connect("employeeDataBase.db")
    #create.cursor
    cu = db.cursor()
    
    id=EID.get()
    print(id)
    data=cu.execute("select * from employeeData where EID="+id)
    
    for r in data:
      Name.insert(0,r[1])
      Designation.insert(0,r[2])
      Salary.insert(0,r[3])
      
        
    db.commit()

    db.close()
    
def Records():
    new = Tk()
    new.title("AllRecords")
    new.geometry("450x800")
    new.configure(background="brown")
    
    
    db=sqlite3.connect("employeeDataBase.db")
    #create.cursor
    cu = db.cursor()
   
    cu.execute("Select * from employeeData")
    data=cu.fetchall()
    
    print_E =''
    print_N =''
    print_D =''
    print_S =''
    
    for r in data:
        print_E +="\n"+str(r[0])+"\n"
        print_N +="\n"+str(r[1])+"\n"
        print_D +="\n"+str(r[2])+"\n"
        print_S +="\n"+str(r[3])+"\n"
    
    #create Records Label
    records_label=Label(new, text=print_E,width=10,bg="lightgray",fg="black")
    records_label.grid(row=1,column=0, padx=14)
    records_label=Label(new, text=print_N,width=10,bg="lightgray",fg="black")
    records_label.grid(row=1,column=1, padx=14)
    records_label=Label(new, text=print_D,width=10,bg="lightgray",fg="black")
    records_label.grid(row=1,column=2, padx=14)
    records_label=Label(new, text=print_S,width=10,bg="lightgray",fg="black")
    records_label.grid(row=1,column=3, padx=14)
    
    
    #create specify content label
    EID_label=Label(new,text="EID",width=10,bg="pink",fg="black")
    EID_label.grid(row=0,column=0)
    Name_label=Label(new,text="Name",width=10,bg="pink",fg="black")
    Name_label.grid(row=0,column=1)
    Designation_label=Label(new,text="Designation",width=10,bg="pink",fg="black")
    Designation_label.grid(row=0,column=2)
    Salary_label=Label(new,text="Salary",width=10,bg="pink",fg="black")
    Salary_label.grid(row=0,column=3,padx=14)
    
    db.commit()

    db.close()

def Delete():
    #create a database
    db=sqlite3.connect("employeeDataBase.db")
   
    #create.cursor
    cu = db.cursor()
    
    cu.execute("delete from employeeData where Eid="+Delete_box.get())
    
    Delete_box.delete(0, END)
    
    db.commit()
    
    db.close()
 

def update():   
    Update = Tk()
    Update.title("UPdate_database")
    Update.geometry("250x300")
    Update.configure(background="black")
    
    db=sqlite3.connect("employeeDataBase.db")
    #create.cursor
    cu = db.cursor()
    
    id = Update_box.get()
    print(id)
    
    cu.execute("select * from employeeData where EID="+id)
    data=cu.fetchall()
    
    global update_EID
    global update_Name
    global update_Designation
    global update_Salary
    
    
    def Exit():
         
         Update.destroy()

    
    #Entry
    update_EID=Entry(Update,width=15)
    update_EID.grid(row=0, column=1, padx=20, pady=5)

    update_Name=Entry(Update,width=15)
    update_Name.grid(row=1, column=1, padx=20, pady=5)

    update_Designation=Entry(Update,width=15)
    update_Designation.grid(row=2, column=1, padx=20, pady=5)

    update_Salary=Entry(Update,width=15)
    update_Salary.grid(row=3, column=1, padx=20, pady=5)
    
    for r in data:
      update_EID.insert(0,r[0])
      update_Name.insert(0,r[1])
      update_Designation.insert(0,r[2])
      update_Salary.insert(0,r[3])
      
    Save_btn = Button(Update, text="Save_DATA", width=10, command=savedata,bg="lightgray",fg="black")
    Save_btn.grid(row=4, column=1, pady=5, padx=5)
    
    exit_btn = Button(Update, text="Exit", width=10,command=Exit,bg="lightgray",fg="black") 
    exit_btn.grid(row=4, column=0, pady=5, padx=5)
    
    #Label
    EID_label=Label(Update,text="Update_EID",width=15,bg="pink",fg="black")
    EID_label.grid(row=0,column=0,)
    Name_label=Label(Update,text="Update_Name",width=15,bg="pink",fg="black")
    Name_label.grid(row=1,column=0)
    Designation_label=Label(Update,text="Update_Designation",width=15,bg="pink",fg="black")
    Designation_label.grid(row=2,column=0)
    Salary_label=Label(Update,text="Update_Salary",width=15,bg="pink",fg="black")
    Salary_label.grid(row=3,column=0)
    
    db.commit()
    
    db.close()
    
def savedata():
    
    db=sqlite3.connect("employeeDataBase.db")
   
    #create.cursor
    cu = db.cursor()
    
    id = Update_box.get()
    cu.execute("update employeeData set EID=?,Name=?,Designation=?,Salary=? where EID=?",(update_EID.get(),update_Name.get(),update_Designation.get(),update_Salary.get(),id))
    
    
    db.commit()
     
    db.close()
    
def reset():
    
    EID.delete(0, END)
    Name.delete(0, END)
    Designation.delete(0, END) 
    Salary.delete(0, END)
    Update_box.delete(0,END)
    Delete_box.delete(0,END)
    
   
def Quit():
    root.destroy()
    

# create Entry box

EID=Entry(root,width=20)
EID.grid(row=0, column=1, padx=0, pady=10)

Name=Entry(root,width=20)
Name.grid(row=0, column=4, padx=5, pady=10)

Designation=Entry(root,width=20)
Designation.grid(row=1, column=4, padx=5, pady=10)

Salary=Entry(root,width=20)
Salary.grid(row=2, column=4, padx=5, pady=10)

#delete box
Delete_box=Entry(root,width=20)
Delete_box.grid(row=6, column=1,padx=5,pady=5)

#UPdate box
Update_box=Entry(root,width=20)
Update_box.grid(row=6,column=4,padx=5,pady=5)

#create box label

EID_label=Label(root,text="EID",width=10,bg="pink",fg="black")
EID_label.grid(row=0,column=0,padx=5)

Name_label=Label(root,text="Name",width=10,bg="pink",fg="black")
Name_label.grid(row=0,column=3,padx=40)

Designation_label=Label(root,text="Designation",width=10,bg="pink",fg="black")
Designation_label.grid(row=1,column=3,padx=40)

Salary_label=Label(root,text="Salary",width=10,bg="pink",fg="black")
Salary_label.grid(row=2,column=3,padx=40)

EnterEID_Label=Label(root,text="Enter EID",width=10,bg="pink",fg="black")
EnterEID_Label.grid(row=6,column=0)

EnterEID_Label=Label(root,text="Enter EID",width=10,bg="pink",fg="black")
EnterEID_Label.grid(row=6,column=3)

#create button
submit_btn = Button(root, text="Save Employee data", command=submit,bg="lightgray",fg="black")
submit_btn.grid(row=5, column=4,  pady=5, padx=5)

show_btn= Button(root, text="EID to show details", command=show, width=10,bg="lightgray",fg="black")
show_btn.grid(row=1, column=1, pady=5, padx=5 ,ipadx=22)

records_btn = Button(root, text="all_Records", width=10,command=Records,bg="lightgray",fg="black")
records_btn.grid(row=10, column=1, pady=5, ipadx=22)

delete_btn = Button(root, text="Delete_records", width=10,command=Delete,bg="lightgray",fg="black")
delete_btn.grid(row=7, column=1, pady=5, ipadx=22)

update_btn = Button(root, text="Update_DATA", width=10, command=update,bg="lightgray",fg="black")
update_btn.grid(row=7, column=4, pady=5, ipadx=22)

reset_btn = Button(root, text="Reset", width=10, command=reset,bg="lightgray",fg="black")
reset_btn.grid(row=10, column=4, pady=5, ipadx=22)

Quit_btn = Button(root, text="Quit", width=10, command=Quit,bg="lightgray",fg="black")
Quit_btn.grid(row=11, column=3, pady=5)


root.mainloop()

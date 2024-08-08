import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

t=tkinter.Tk()
t.geometry('1920x1080')
t.title('Hospital Managment')
t.config(bg='LavenderBlush3')

lt=[]
def fillpatientname():
    db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
    cur=db.cursor()
    sql="select patientname from hospital"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])

def insert():
    db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
    cur=db.cursor()
    aa=c1.get()
    ab=d1.get()
    ac=e1.get()
    ad=f1.get()
    ae=g1.get()
    af=h1.get()
    ag=i1.get()
    ah=j1.get()
    ai=k1.get()
    aj=l1.get()
    ak=m1.get()
    al=n1.get()
    am=o1.get()
    an=p1.get()
    ao=q1.get()
    ap=r1.get()
    aq=s1.get()
    ar=u1.get()
    
    sql="insert into hospital values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar)
    cur.execute(sql)
    db.commit()
    c1.delete(0,100)
    d1.delete(0,100)
    e1.delete(0,100)
    f1.delete(0,100)
    g1.delete(0,100)
    i1.delete(0,100)
    h1.delete(0,100)
    j1.delete(0,100)
    k1.delete(0,100)
    l1.delete(0,100)
    m1.delete(0,100)
    n1.delete(0,100)
    o1.delete(0,100)
    p1.delete(0,100)
    q1.delete(0,100)
    r1.delete(0,100)
    s1.delete(0,100)
    u1.delete(0,100)
    db.close()
    messagebox.showinfo('Insert','Data is inserted ')
    
def find():
    db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
    cur=db.cursor()
    aa1=c1.get()
    sql1="select * from hospital where patientname='%s'"%(aa1)
    cur.execute(sql1)
    data=cur.fetchone()
    d1.delete(0,100)
    e1.delete(0,100)
    f1.delete(0,100)
    g1.delete(0,100)
    i1.delete(0,100)
    h1.delete(0,100)
    j1.delete(0,100)
    k1.delete(0,100)
    l1.delete(0,100)
    m1.delete(0,100)
    n1.delete(0,100)
    o1.delete(0,100)
    p1.delete(0,100)
    q1.delete(0,100)
    r1.delete(0,100)
    s1.delete(0,100)
    u1.delete(0,100)
    d1.insert(0,data[1])
    e1.insert(0,data[2])
    f1.insert(0,data[3])
    g1.insert(0,data[4])
    h1.insert(0,data[5])
    i1.insert(0,data[6])
    j1.insert(0,data[7])
    k1.insert(0,data[8])
    l1.insert(0,data[9])
    m1.insert(0,data[10])
    n1.insert(0,data[11])
    o1.insert(0,data[12])
    p1.insert(0,data[13])
    q1.insert(0,data[14])
    r1.insert(0,data[15])
    s1.insert(0,data[16])
    u1.insert(0,data[17])
    
    db.close()
    messagebox.showinfo('Find','Data Found')
    
def update():
    db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
    cur=db.cursor()
    aa3=c1.get()
    ab3=d1.get()
    ad3=e1.get()
    ae3=f1.get()
    af3=g1.get()
    ag3=h1.get()
    ah3=i1.get()
    ai3=j1.get()
    aj3=k1.get()
    ak3=l1.get()
    al3=m1.get()
    am3=n1.get()
    an3=o1.get()
    ao3=p1.get()
    ap3=q1.get()
    aq3=r1.get()
    ar3=s1.get()
    as3=u1.get()
    sql3="update hospital set nameoftablets='%s', referenceno='%s', dose='%s', nooftablets='%s', issuedate='%s', expdate='%s', dailydose='%s', sideeffect='%s', furtherinformation='%s', bloodpressure='%s', storageadvice='%s', medication='%s', patientid='%s', nhsnumber='%s', lot='%s', dateofbirth='%s', patientaddress='%s' where patientname='%s'"%(ab3,ad3,ae3,af3,ag3,ah3,ai3,aj3,ak3,al3,am3,an3,ao3,ap3,aq3,ar3,as3,aa3)
    cur.execute(sql3)
    db.commit()
    db.close()
    messagebox.showinfo('Update','Data Updated')
    
def delete():
    db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
    cur=db.cursor()
    aa2=c1.get()
    sql2="delete from hospital where patientname='%s'"%(aa2)
    cur.execute(sql2)
    db.commit()
    db.close()
    messagebox.showinfo('Delete','Data Deleted')
    
def close():
    messagebox.showinfo('Exit','Thank you ')
    t.destroy()
    

a=Label(t,text=' Hospital Managment System ',fg='firebrick2',font=('times new roman',40,UNDERLINE),bg='LavenderBlush3')
a.place(x=500,y=30)

b=Label(t,text='Patient Information',fg='blue',font=('times new roman',18),bg='LavenderBlush3')
b.place(x=90,y=150)

c=Label(t,text='Patient Name',font=('times new roman',22),bg='LavenderBlush3')
c.place(x=120,y=190)
c1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
style=ttk.Style()
style.theme_use('clam')
style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
fillpatientname()
c1['values']=lt
c1.place(x=350,y=190)

d=Label(t,text='Name of Tablets',font=('times new roman',22),bg='LavenderBlush3')
d.place(x=120,y=240)
d1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='peachpuff',bd=4)
d1.place(x=350,y=240)

e=Label(t,text='Reference no.',font=('times new roman',22),bg='LavenderBlush3')
e.place(x=120,y=290)
e1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
e1.place(x=350,y=290)

f=Label(t,text='Dose',font=('times new roman',22),bg='LavenderBlush3')
f.place(x=120,y=340)
f1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
f1.place(x=350,y=340)

g=Label(t,text='No.of Tablets',font=('times new roman',22),bg='LavenderBlush3')
g.place(x=120,y=390)
g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
g1.place(x=350,y=390)

h=Label(t,text='Issue Date :',font=('times new roman',22),bg='LavenderBlush3')
h.place(x=120,y=440)
h1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
h1.place(x=350,y=440)

i=Label(t,text='Exp Date :',font=('times new roman',22),bg='LavenderBlush3')
i.place(x=120,y=490)
i1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
i1.place(x=350,y=490)

j=Label(t,text='Daily Dose',font=('times new roman',22),bg='LavenderBlush3')
j.place(x=120,y=540)
j1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
j1.place(x=350,y=540)

k=Label(t,text='Side Effect',font=('times new roman',22),bg='LavenderBlush3')
k.place(x=120,y=590)
k1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
k1.place(x=350,y=590)

l=Label(t,text='Further Information',font=('times new roman',22),bg='LavenderBlush3')
l.place(x=750,y=190)
l1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
l1.place(x=1050,y=190)

m=Label(t,text='Blood Pressure',font=('times new roman',22),bg='LavenderBlush3')
m.place(x=750,y=240)
m1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
m1.place(x=1050,y=240)

n=Label(t,text='Storage Advice',font=('times new roman',22),bg='LavenderBlush3')
n.place(x=750,y=290)
n1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
n1.place(x=1050,y=290)

o=Label(t,text='Medication',font=('times new roman',22),bg='LavenderBlush3')
o.place(x=750,y=340)
o1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
o1.place(x=1050,y=340)

p=Label(t,text='Patient Id',font=('times new roman',22),bg='LavenderBlush3')
p.place(x=750,y=390)
p1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
p1.place(x=1050,y=390)

q=Label(t,text='NHS Number',font=('times new roman',22),bg='LavenderBlush3')
q.place(x=750,y=440)
q1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
q1.place(x=1050,y=440)

r=Label(t,text='Lot : ',font=('times new roman',22),bg='LavenderBlush3')
r.place(x=750,y=490)
r1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
r1.place(x=1050,y=490)

s=Label(t,text='Date Of Birth',font=('times new roman',22),bg='LavenderBlush3')
s.place(x=750,y=540)
s1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
s1.place(x=1050,y=540)

u=Label(t,text='Patient Address',font=('times new roman',22),bg='LavenderBlush3')
u.place(x=750,y=590)
u1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
u1.place(x=1050,y=590)


bt1=Button(t,text='Insert',bd=5,font=1,bg='light slate gray',fg='cyan',command=insert)
bt1.place(x=300,y=680)

bt2=Button(t,text='Find',bd=5,font=1,bg='light slate gray',fg='cyan',command=find)
bt2.place(x=500,y=680)

bt3=Button(t,text='Update',bd=5,font=1,bg='light slate gray',fg='cyan',command=update)
bt3.place(x=700,y=680)

bt4=Button(t,text='Delete',bd=5,font=1,bg='light slate gray',fg='cyan',command=delete)
bt4.place(x=900,y=680)

bt5=Button(t,text='Exit',bd=5,font=1,bg='light slate gray',fg='cyan',command=close)
bt5.place(x=1100,y=680)



t.mainloop()
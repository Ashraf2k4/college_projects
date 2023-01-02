import mysql.connector as a
import csv
con=a.connect(host="localhost",user="root",database="student_examination_portal",passwd="ashraf1000")
if con.is_connected():
    print("Succesfully connected!")

def AddSt(): #Create a student
    sid=input("Enter Student Id: ")
    n=input("Enter Student Name: ")
    r=int(input("Enter Roll no.: "))
    BID=input("Enter Batch ID: ")
    data=(sid,n,r,BID)
    sql='insert into student values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Student added Succesfully.....")
    print("")

def UpdateSt(): #Update a Student
    ID=input("Enter Student Id: ")
    sql='select * from student where ID=%s'
    c=con.cursor()
    c.execute(sql,(ID,))
    d=c.fetchall()
    if d==[]:
        print("Student Not Found.....")
        print("")
    else:
        for i in d:
            print("Name: ",i[1])
            print("Class Rol No.: ",i[2])
            print("Batch Id: ",i[3])
            print("")
            n=input("Enter Name of Student: ")
            r=int(input("Enter New Roll No.: "))
            BID=input("Enter New Batch ID: ")
            data=(n,r,BID,ID)
            sql='update student set name=%s,roll=%s,BID=%s where Id=%s'
            c=con.cursor()
            c.execute(sql,data)
            con.commit()
            print("Student Updated Succesfully.......")
            print("") 

def RemoveSt(): # Remove a Student
    ID=input("Enter Student Id: ")
    n=input("Enter Name of Student: ")
    sql='select * from student where ID=%s and Name=%s'
    data=(ID,n)
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    if d==[]:
        print("Student Not Found.....")
        print("")
    else:
        sql='delete from student where ID=%s and name=%s'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Student Removed Succesfully.......")
        print("")
        
def AddB(): # Add Batch
    BID=input("Enter Batch ID ")
    bname=input("Enter Batch Name: ")
    DID=input("Enter Department ID: ")
    CID=""
    n=int(input("Enter Number of Courses: "))
    for i in range(n-1):
        x=input("Enter Course ID: ")
        x1=x+":"
        CID=CID+x1
    x=input("Enter Course ID: ")
    CID=CID+x
    data=(BID,bname,DID,CID)

    sql='insert into batch values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Batch added Successfully...........")
    print("")
    
def ViewS(): # View all student in the batch
    BID=input("Enter Batch ID: ")
    sql="select name from student where BID=%s"
    c=con.cursor()
    c.execute(sql,(BID,))
    d=c.fetchall()
    if d==[]:
        print("No Students in",BID)
        print("")
    else:
        print("Students in",BID,"are",d)
        print("")
        
def ViewBP(): # View complete performance of all student in the batch
    BID=input("Enter Batch ID: ")
    l=[]
    sql='select student.Id, student.name, student.roll from student where bid=%s'
    c=con.cursor()
    c.execute(sql,(BID,))
    d=c.fetchall()
    for i in d:
       l.append(i)
    for i in l:
        y="Name: "+i[1]+'\n'+"Student Id: "+i[0]+'\n'+"Class Roll No.: "+str(i[2])
        data=(BID,i[0])
        sql='select batch.bname, course.cname, exam.marks from batch,exam,course where bid=%s and exam.cid=course.cid and exam.id=%s'
        c=con.cursor()
        c.execute(sql,data)
        d=c.fetchall()
        print(y)
    for i in d:
        z=i[1]+" : "+str(i[2])
        print(z)
        print()

    
def AddC(): # Add course
    CID=input("Enter Course ID: ")
    n=input("Enter Course Name: ")
    data=(CID,n)
    sql='insert into course values(%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Course Added Succesfully.......")
    print("")
     
def ViewC(): # view list of courses in the batch
    BID=input("Enter Batch ID: ")
    sql="select courses from batch where BID=%s"
    c=con.cursor()
    c.execute(sql,(BID,))
    d=c.fetchone()
    if d==[]:
        print("No Students in",BID)
        print("")
    else:
        print("Courses in",BID,"are",d)
        print("")
        
def ViewP(): # View perfomance of all student in the course
    CID=input("Enter Course ID: ")
    sql='select student.name, student.roll, exam.marks from student, exam where stud.id=exam.id and cid=%s'
    c=con.cursor()
    c.execute(sql,(CID,))
    d=c.fetchall()
    print("[Name,Roll,Marks]")
    for i in d:
        print(i)

def AddM(): # Add marks of all students in a Course
    CID=input("Enter Course ID: ")
    ID=input("Enter Student ID: ")
    m=int(input("Enter Marks Obtained: "))
    data=(CID,ID,m)
    sql='insert INTO exam values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Marks added Succesfully.....")
    print("")        
        

def Report(): # Genereate Report Card
    ID=input("Enter Student ID: ")
    l=[]
    sql='select Id, name, roll from student where id=%s'
    c=con.cursor()
    c.execute(sql,(ID,))
    d=c.fetchone()
    for i in d:
        l.append(i)
    sql='select exam.cid, course.cname, exam.marks from exam, course where id=%s and exam.cid=course.cid'
    c=con.cursor()
    c.execute(sql,(ID,))
    d=c.fetchall()
    y="Name: "+l[1]+'\n'+"Student Id: "+l[0]+'\n'+"Class Roll No.: "+str(l[2])+2*'\n'
    for i in l:
        m=l[0]+"_"+l[1]+".txt"
    with open(m,"w") as x:
        x.write(y)
        x.write("C Code"+" "+"Course Name"+" "*29+"Marks"+" "+"Grade"+" "+"Status"+'\n')
    for i in d:
        for j in i:
            if i[2]<40:
                g='F'
                o="Fail"
            elif i[2]>=90:
                g='A'
                o="Pass"
            elif i[2]>=80:
                g='B'
                o="Pass"
            elif i[2]>=70:
                g='C'
                o="Pass"
            elif i[2]>=60:
                g='D'
                o="Pass"
            elif i[2]>=50:
                g='E'
                o="Pass"
        z=" "+i[0]+" "*3+i[1]+" "*(41-len(i[1]))+str(i[2])+" "+g+" "+o+'\n'
        with open(m,'a') as x:
            x.write(z)
    print("Report Card Generated Succesfully..... ")


def ViewStat(): # Show course Statistcs
    l=[]
    CID=input("Enter Course ID: ")
    sql='select marks from exam where cid=%s'
    c=con.cursor()
    c.execute(sql,(CID,))
    d=c.fetchall()
    for i in d:
        for j in i:
            l.append(j)

    A=B=C=D=E=F=0
    for i in l:
        if i>90:
            A+=1
        elif i>80:
            B+=1
        elif i>70:
            C+=1
        elif i>60:
            D+=1
        elif i<40:
            F+=1
        elif i>50:
            E+=1
    x=[A,B,C,D,E,F]

    import matplotlib.pyplot as plt

    g=["A","B","C","D","E","F"]
    n=x
    fig = plt.figure(figsize = (10, 5))
    plt.bar(g,n,color ='grey',width = 0.5)
    plt.xlabel("Grades")
    plt.ylabel("No. of Students")
    plt.title("Course Statistics")
    plt.show()

def ViewBS(): # View pie chart of percentage of all students
    sql="select distinct(bid) from student"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    b=[]
    n=[]
    for i in d:
        for j in i:
            b.append(j)
            sql="select count(bid) from student where bid=%s"
            c=con.cursor()
            c.execute(sql,(j,))
            d=c.fetchall()
            for i in d:
                for j in i:
                    n.append(j)
    import matplotlib.pyplot as plt
    plt.pie(n,labels=b)
    plt.show()

def AddD(): # Add department
    DID=input("Enter Departent ID: ")
    n=input("Enter Department Name: ")
    data=(DID,n)
    sql='insert into department values(%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Course Added Succesfully.......")
    print("")

def ViewB(): # View all batches in a department
    DID=input("Enter Department ID: ")
    sql="select BID from batch where DID=%s"
    c=con.cursor()
    c.execute(sql,(DID,))
    d=c.fetchall()
    if d==[]:
        print("No Students in",DID)
        print("")
    else:
        print("Batches in",DID,"are",d)
        print("")

def ViewAp(): # Show average perforamnce of all batches in the department
    DID=input("Enter Department ID: ")
    sql="select BID from batch where DID=%s"
    c=con.cursor()
    c.execute(sql,(DID,))
    d=c.fetchall()
    for i in d:
        for j in i:
            l=[]
            l.append(j)
            sql='select avg(exam.marks) from exam, batch, student where student.bid=%s and student.id=exam.id'
            c=con.cursor()
            c.execute(sql,(j,))
            d=c.fetchall()
            for i in d:
                for j in i:
                    x="Department Id: "+l[0]+" "+"Average Performance: "+str(j)
            print(x)

def ViewDS(): # show department stastics
    import matplotlib.pyplot as plt
    import numpy as np
    DID=input("Enter Department ID: ")
    sql="select BID from batch where DID=%s"
    c=con.cursor()
    c.execute(sql,(DID,))
    d=c.fetchall()
    l=[]
    p=[]
    for i in d:
        for j in i:
            l.append(j)
            sql='select avg(exam.marks) from exam, batch, student where student.bid=%s and student.id=exam.id'
            c=con.cursor()
            c.execute(sql,(j,))
            d=c.fetchall()
            for i in d:
                for j in i:
                    p.append(int(j))
    ypoints = np.array(p)
    xpoints=l
    plt.plot(ypoints, xpoints, color = 'r')
    plt.show()


def ViewEP(): # Show performance of all students in the examination
    CID=input("Enter Course ID: ")
    sql='select student.name, student.roll, exam.marks from student,EXAM where CID=%s and EXAM.ID=student.Id'
    c=con.cursor()
    c.execute(sql,(CID,))
    d=c.fetchall()
    for i in d:
        for j in i:
            x="Name:"+i[0]+" "*3+"Roll:"+str(i[1])+" "*3+"Marks:"+str(i[2])
        print(x)
    print()

def ViewES(): # Show examination statistics
    sql="select exam.cid,student.bid,exam.marks from exam, student where exam.id=student.id"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    m=[]
    c=[]
    b=[]
    for i in d:
        m.append(i[2])
        c.append(i[0])
        b.append(i[1])
    marks=m
    course=c
    batch= b
    
    import matplotlib.pyplot as plt
    import numpy as np

    plt.scatter(x=marks,y=batch, s=200, c=course,)
    plt.show()

def backup(): # Mainatining database as csv
    sql='select * from student'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    with open("Student.csv","w",newline="") as myfile:
        f=csv.writer(myfile)
        f.writerow(["Student ID","Name","Class Roll Number","Batch ID"])
        f.writerows(d)

    sql='select * from course'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    with open("Course.csv","w",newline="") as myfile:
        f=csv.writer(myfile)
        f.writerow(["Course ID","Course Name","Marks Obtained"])
        f.writerows(d)
    sql='select * from batch'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    with open("Batch.csv","w",newline="") as myfile:
        f=csv.writer(myfile)
        f.writerow(["Batch ID","Batch Name","Department Name","List of Courses","List of Students"])
        f.writerows(d)
    sql='select * from Department'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    with open("Department.csv","w",newline="") as myfile:
        f=csv.writer(myfile)
        f.writerow(["Department ID","Department Name","List of Batches"])
        f.writerows(d)

def main():
    ch="y"
    while ch in["y","Y"]:
        print("STUDENT EXAMINATION PORTAL ")
        print("1. Student")
        print("2. COURSE")
        print("3. BATCH")
        print("4. DEPARTMENT")
        print("5. Examination")
        m=int(input("Enter Module No.: "))
        print("")

        if m==1:
            op="y"
            while op in ["y","Y"]:
                print("1.Add Student")
                print("2.Update Student")
                print("3.Remove Student")
                print("4.Generate Report Card")
                task=int(input("Enter task No.: "))
                if task==1:
                    AddSt()
                elif task==2:
                    UpdateSt()
                elif task==3:
                    RemoveSt()
                elif task==4:
                    Report()
                else:
                    print("Enter Valid Choice.....!!")
                op=input("Continue in Student Module(y/n):")

        elif m==2:
            op="y"
            while op in["y","Y"]:
                print("1.Create New Course")
                print("2.View Perfomance")
                print("3.Show Course Statistics")
                task=int(input("Enter task No.: "))
                if task==1:
                    AddC()
                elif task==2:
                    ViewP()
                elif task==3:
                    ViewStat()
                else:
                    print("Enter Valid Choice.......!!")
                op=input("Continue in Course Module(y/n):")

        elif m==3:
            op="y"
            while op in["y","Y"]:
                print("1.Create New Batch")
                print("2.View Students in a Batch")
                print("3.View Courses in a Batch")
                print("4.View Performance of a Batch")
                print("5.View Batch Statistics")
                task=int(input("Enter Task No.: "))
                if task==1:
                    AddB()
                elif task==2:
                    ViewS()
                elif task==3:
                    ViewC()
                elif task==4:
                    ViewBP()
                elif task==5:
                    ViewBS()
                else:
                    print("Enter Valid Choice........!!")
                op=input("Continue in Batch Module(y/n):")

        elif m==4:
            op="y"
            while op in["y","Y"]:
                print("1.Create New Department")
                print("2.View Batches in a Department")
                print("3.View Average Peformance of All Batches")
                print("4.View Department Statistics")
                task=int(input("Enter Task No.: "))
                if task==1:
                    AddD()
                elif task==2:
                    ViewB()
                elif task==3:
                    ViewAp()
                elif task==4:
                    ViewDS()
                else:
                    print("Enter Valid choice.......!!")
                op=input("Continue in Department Module(y/n):")

        elif m==5:
            op="y"
            while op in["y","Y"]:
                print("1.Enter Marks")
                print("2.View Performance")
                print("3.Show Examination Statistics")
                task=int(input("Enter Task No.: "))
                if task==1:
                    AddM()
                if task==2:
                    ViewEP()
                if task==3:
                    ViewES()
                else:
                    print("Enter Valid choice.......!!")
                op=input("Continue in Examination Module(y/n):")

        else:
            print("ENTER VALID CHOICE!!")
        ch=input("Do you want to continue(y/n):")
backup()
main()
backup

import sqlite3

con=sqlite3.connect("mybd.db")

cur=con.cursor()

# cur.execute("create table student (id int, name text)")
#cur.execute("insert into student(id,name)values(101,'prasad')")
# cur.execute("insert into student(id,name)values(?,?)",(102,"abc"))
# cur.execute("create table student1 (roll no int,name txt,email text)")
#
#list1=[(103,"xyz"),(104,"bbb"),(105,"ppp")]
#cur.executemany("insert into student(roll nos,name)values(?,?)",list1)

# list2=[(201,"prasad","prasad@gmail.com"),(202,"ashwini","ashwini@gmail.com"),(203,"tupe","tupe@gmail.com"),
#        (204,"abc","abc@gmail.com")]
# cur.executemany("insert into student1(roll,name,email)values(?,?,?)",list2)


# data=cur.execute("select * from student")
#
# for i in data:
#        print(i[0],i[1])

# cur.execute("select * from student1")
# data=cur.fetchall()
#
# for i in data:
#        print(i[0],i[1],i[2])

#update query

# cur.execute("update student set id=110 where id=101")
cur.execute("update student set name=? where id=?",('aaa',120))

#delet query

cur.execute("delete from student where id=?",[120])

# data=cur.execute("select * from student")
# data=cur.fetchone()

con.commit()

con.close()
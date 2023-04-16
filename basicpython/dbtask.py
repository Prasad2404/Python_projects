
import sqlite3

con=sqlite3.connect("task.db")

cur=con.cursor()

cur.execute("create table student1(student_id int, student_name text)")
list1=[(101,"aaa"),(102,"bbb"),(103,"ccc"),(104,"ddd")]
cur.executemany("insert into student1(student_id,student_name)values(?,?)",list1)


# cur.execute("create table dept1(dept_id int, dept_name text)")
# list2=[(101,"aaa"),(102,"abc"),(303,"xyz"),(404,"ddd")]
# cur.executemany("insert into dept(dept_id,dept_name)values(?,?)",list2)

#cur.execute("select * from student1 inner join dept1 on student1.name=dept1.name")

# data=cur.execute("select * from student inner join dept")
# for i in data:
#     print(i)






con.commit()

con.close()
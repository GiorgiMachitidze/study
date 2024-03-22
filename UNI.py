import sqlite3

conn = sqlite3.connect("study.db")

c = conn.cursor()
'''
c.executescript("""
CREATE TABLE IF NOT EXISTS Advisor(
AdvisorID INTEGER NOT NULL,
AdvisorName TEXT NOT NULL,
PRIMARY KEY(AdvisorName)
);

CREATE TABLE IF NOT EXISTS student (
StudentID INTEGER NOT NULL,
StudentName TEXT NOT NULL,
PRIMARY KEY(StudentID)
);

CREATE TABLE IF NOT EXISTS student_advisor(    
StudentID INTEGER NOT NULL,
AdvisorID INTEGER,
PRIMARY KEY(StudentID, AdvisorID),
FOREIGN KEY(StudentID) REFERENCES student(StudentID),
FOREIGN KEY(AdvisorID) REFERENCES advisor(AdvisorID)
);

INSERT INTO student_advisor(StudentID, AdvisorID) VALUES 
(501, 1),
(501, 3),
(502, 1),
(502, 4),
(503, 3),
(504, 2),
(504, 4),
(505, 4),
(506, 2),
(506, 1),
(506, 3),
(507, 2),
(508, 3),
(509, NULL),
(510, 1),
(510, 5);

INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES 
(1,"John Paul"),  
(2,"Anthony Roy"),  
(3,"Raj Shetty"), 
(4,"Sam Reeds"), 
(5,"Arthur Clint wood"); 
  
INSERT INTO Student(StudentID, StudentName) VALUES 
(501,"Geek1"), 
(502,"Geek2"), 
(503,"Geek3"), 
(504,"Geek4"), 
(505,"Geek5"), 
(506,"Geek6"), 
(507,"Geek7"), 
(508,"Geek8"), 
(509,"Geek9"), 
(510,"Geek10"); 
""")
'''
c.execute("""
SELECT advisor.AdvisorID, 
       advisor.AdvisorName,
       COUNT(DISTINCT student_advisor.StudentID) AS number_of_students
FROM advisor 
JOIN student_advisor ON student_advisor.AdvisorID = advisor.AdvisorID 
GROUP BY advisor.AdvisorID, advisor.AdvisorName;

""")
'''
c.execute("""
SELECT student.StudentID,
student.StudentName,
COUNT(DISTINCT student_advisor.AdvisorID) AS number_of_advisors
FROM student
JOIN student_advisor ON student.StudentID = student_advisor.StudentID
GROUP BY student.StudentID, student.StudentName;""")
'''
res = c.fetchall()
print(res)
conn.commit()
conn.close()

import mysql.connector as m

con = m.connect(host="localhost", user="root", password="student", database="db1")
c = con.cursor()

def add_hra():
    try:
        c.execute("ALTER TABLE emp ADD HRA DECIMAL(10,2) DEFAULT 2000")
        print("HRA column added successfully.")
    except:
        print("HRA column already exists or cannot be added.")

def modify_hra():
    eno = int(input("Enter employee number: "))
    hra = float(input("Enter new HRA: "))
    q = "UPDATE emp SET HRA=%s WHERE empno=%s"
    c.execute(q, (hra, eno))
    con.commit()
    if c.rowcount > 0:
        print("HRA updated successfully.")
    else:
        print("Employee not found.")

def display_comm():
    q = "SELECT empname, job, sal*12 AS annual_salary \
FROM emp WHERE comm IS NOT NULL ORDER BY sal DESC"
    c.execute(q)
    data = c.fetchall()
    print("{:<20} {:<15} {:>15}".format("NAME", "JOB", "ANNUAL SALARY"))
    print("-" * 52)
    for r in data:
        print("{:<20} {:<15} {:>15.2f}".format(r[0], r[1], float(r[2])))

def delete_emp():
    eno = int(input("Enter employee number to delete: "))
    q = "DELETE FROM emp WHERE empno=%s"
    c.execute(q, (eno,))
    con.commit()
    if c.rowcount > 0:
        print("Employee record deleted successfully.")
    else:
        print("Employee not found.")

def display_job():
    q = "SELECT e.empno, e.name, e.job, d.dname FROM\
emp e, dept d WHERE e.deptno = d.deptno AND e.job IN ('MANAGER','CLERK')"
    c.execute(q)
    data = c.fetchall()
    print("{:<10} {:<20} {:<15} {:<20}".format("EMPNO", "NAME", "JOB", "DEPARTMENT"))
    print("-" * 68)
    for r in data:
        print("{:<10} {:<20} {:<15} {:<20}".format(r[0], r[1], r[2], r[3]))

def salary_details():
    q = "SELECT job, MIN(sal), MAX(sal), SUM(sal), AVG(sal), COUNT(*) FROM emp GROUP BY job"
    c.execute(q)
    data = c.fetchall()
    print("{:<15} {:>10} {:>10} {:>12} {:>12} {:>8}"\
          .format("JOB", "MIN", "MAX", "SUM", "AVERAGE", "COUNT"))
    print("-" * 72)
    for r in data:
        print("{:<15} {:>10.2f} {:>10.2f} {:>12.2f} {:>12.2f} {:>8}"\
              .format(r[0], float(r[1]), float(r[2]), float(r[3]), float(r[4]), r[5]))

add_hra()
modify_hra()
display_comm()
delete_emp()
display_job()
salary_details()
con.close()

#coding=utf-8
import MySQLdb

if __name__ == '__main__':

  conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='996633',
        db ='university',
        )
  cur = conn.cursor()


def prc_line(line):
        _result = line.decode("utf-8").strip().split(" ")
        _result[2] = int(_result[2])
        _result[4] = int(_result[4])
        return _result

 with open("/home/lin/文档/MySQL上课文件/作业/university/department.txt", "r") as f:
        datas = [prc_line(line) for line in f.readlines()]

 for d in datas:
        cur.execute("insert into department(dept_name,building,budget) values('%s','%s',%d)" % (
        'computer', 'Building_A', 12000))
        cur.execute("insert into department(dept_name,building,budget) values('%s','%s',%d)" % (
        'biology', 'Building_B', 24000))
        cur.execute("insert into department(dept_name,building,budget) values('%s','%s',%d)" % (
        'physics', 'Building_C', 28000))
        cur.execute(
                "insert into department(dept_name,building,budget) values('%s','%s',%d)" % ('new', 'Building_D', 8000))
        cur.execute(
                "insert into department(dept_name,building,budget) values('%s','%s',%d)" % ('math', 'Buding_E', 35000))

 with open("/home/lin/文档/MySQL上课文件/作业/university/student.txt", "r") as f:
        datas = [prc_line(line) for line in f.readlines()]

 for d in datas:
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (1, '廉萱妍', 'f', 19,'loving','computer'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (2, '荀良运', 'm', 17,'single','computer'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (3, '尹枫起', 'm', 14,'loving','computer'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (4, '皇甫梦心', 'f', 13,'loving','computer'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (5, '司马海禧', 'm', 24,'loving','computer'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (6, '薛珊柏', 'f', 21,'single','biology'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (7, '皇甫驰钊', 'm', 21,'single','physics'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (8, '骆谷震', 'm', 23,'singlecomputer'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (9, '吕禧逸', 'm', 18,'single','biology'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (10, '公孙子晨', 'm', 20,'loving','physics'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (11, '王凡康', 'm', 21,'loving','physics'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (12, '谢婷桃', 'f', 21,'single','computer'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (13, '寿雨华', 'f', 20,'single','physics'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (14, '昌菲婧', 'f', 19,'loving','new'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (15, '赵梓梓', 'm', 22,'loving','biology'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (16, '尉迟彩鑫', 'f', 22,'single','new'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (17, '毛骏钊', 'm', 23,'single','new'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (18, '吴腾梁', 'm', 17,'loving','math'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (19, '庞德骏', 'm', 23,'loving','math'))
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values(%d,'%s','%s',%d,'%s','%s')" % (20, '梅昭凡', 'f', 18,'single','computer'))






 with open("/home/lin/文档/MySQL上课文件/作业/university/exam.txt", "r") as f:
        datas = [prc_line(line) for line in f.readlines()]

 for d in datas:
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (11, 'ThirdExam', 93))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (11, 'FinalExam', 60))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (12, 'FirstExam', 98))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (12, 'SecondExam', 48))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (12, 'ThirdExam', 69))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (12, 'FinalExam', 86))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (13, 'FirstExam', 46))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (13, 'SecondExam', 84))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (13, 'ThirdExam', 47))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (13, 'FinalExam', 83))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (14, 'FirstExam', 52))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (14, 'SecondExam', 97))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (14, 'ThirdExam', 91))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (14, 'FinalExam', 84))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (15, 'FirstExam', 85))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (15, 'SecondExam',68))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (15, 'ThirdExam', 00))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (15, 'FinalExam', 52))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (16, 'FirstExam', 59))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (16, 'SecondExam', 58))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (16, 'ThirdExam', 95))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (16, 'FinalExam', 58))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (17, 'FirstExam', 92))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (17, 'SecondExam', 93))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (17, 'ThirdExam', 100))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (17, 'FinalExam', 49))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (18, 'FirstExam', 87))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (18, 'SecondExam', 81))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (18, 'ThirdExam', 93))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (18, 'FinalExam', 58))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (19, 'FirstExam', 85))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (19, 'SecondExam', 88))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (19, 'ThirdExam', 91))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (19, 'FinalExam', 62))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (20, 'FirstExam', 88))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (20, 'SecondExam', 78))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (20, 'ThirdExam', 94))
        cur.execute("insert into exam(student_ID,exam_name,grade) values(%d,'%s',%d)" % (20, 'FinalExam', 100))

cur.close()
conn.close()
f.close()
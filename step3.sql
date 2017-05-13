/*三,写出下列MySQL语句,存到step3.sql文件中,要求写清楚题号,抄题,.*/
/*3-1.把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）写出MySQL语句。*/
select * from peoples where school != 'GDUFS';

/*3-2.查找计算机系每次考试学生的平均成绩(最终显示考试名称, 平均分)。*/
select exam_name,avg(grade) from exam left join student on exam_name=name where depart_name ="computer";

/*3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。*/
select name,avg(grade) 
from student 
where sex = 'f'
having avg(grade) > =80;

/*3-4.找出人数最少的院系以及其年度预算。*/
select min(peoples of yuanxi),budget from school;

/*3-5.计算机系改名了，改成计算机科学系（comp. sci.），写出mysql语句。*/
update computerxi set name ='com.sci' where name = 'com.tch';

/*3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。*/
update school set budget = budget + (count(name)from students)* 2 where xiname='jishuanjixi';

/*3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.*/
insert into department values('avg_budget',NULL,'f',select avg(budget) from school);

/*3-8. 删除计算机系中考试成绩平均分低于70的学生.*/
delete from students where avg(grade)<=70 ;


/*3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.*/
select name from students where emotion_state = 'loving' and avg(grade)<=75;
update students set emotion_state = 'single' where emotion_state = 'loving' and avg(grade)<=75;



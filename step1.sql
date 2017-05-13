/*创建department表*/
CREATE TABLE `department` (
  `dept_name` varchar(45) NOT NULL,
  `building` varchar(45) DEFAULT NULL,
  `budget` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`dept_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

/*创建student表*/
CREATE TABLE `student` (
  `student _ID` int(11) NOT NULL,
  `name` int(10) unsigned NOT NULL,
  `age` int(10) unsigned DEFAULT NULL,
  `dept_name` varchar(45) DEFAULT NULL,
  `sex` varchar(45) DEFAULT NULL,
  `emotion_state` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`student _ID`),
  CONSTRAINT `fk_student_1` FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8

/*创建exam表*/
CREATE TABLE `exam` (
  `exam_Id` int(11) NOT NULL,
  `exam_name` varchar(45) NOT NULL,
  `grade` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`exam_Id`,`exam_name`),
  CONSTRAINT `fk_exam_1` FOREIGN KEY (`exam_Id`) REFERENCES `student` (`student _ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8



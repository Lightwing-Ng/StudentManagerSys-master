# StudentManagerSys-master
## 需求
用户角色，讲师＼学员， 用户登陆后根据角色不同，能做的事情不同，分别如下：
### 讲师视图
```
    1 管理班级，可创建班级，根据学员QQ号把学员加入班级；
    2 可创建指定班级的上课纪录，注意一节上课纪录对应多条学员的上课纪录， 即每节课都有整班学员上；
    3 为了纪录每位学员的学习成绩，需在创建每节上课纪录同时；
    4 为这个班的每位学员创建一条上课纪录；
    5 为学员批改成绩，逐条地手动修改成绩。
```
### 学员视图
```
    1 提交作业；
    2 查看作业成绩；
    3 一个学员可以同时属于多个班级，就像报了Linux的同时也可以报名Python一样，所以提交作业时需先选择班级，再选择具体上课的节数
    
    * 附加：学员可以查看自己的班级成绩排名
```
### 程序分析
```
Date Struct:
    teacher（id, name）            
    student(id, name, qq, grades) 
    grade(id, name, students) # 班级
    grade_record(grade_id, student_id, date, task_status, score)
    grade2student(grade_id, student_id)
```
### 目录结构
```
.
├── README.md                           README.md
├── __init__.py
├── bin
│   ├── __init__.py
│   └── main.py                         程序入口
├── core                                核心代码
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── common.cpython-36.pyc
│   │   ├── student.cpython-36.pyc
│   │   └── teacher.cpython-36.pyc
│   ├── common.py                       三个对象的公共方法
│   ├── grade.py                        班级功能封装
│   ├── student.py                      学生功能封装
│   └── teacher.py                      教师功能封装
└── data                                数据管理
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── init_data.cpython-36.pyc
    │   └── init_database.cpython-36.pyc
    ├── database.db                     SQLite存储文件
    ├── init_data.py                    添加初始数据
    └── init_database.py                数据结构的初始化
```

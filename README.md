# Students Feedback on Academic Courses

It is a system which provides a platform for every student to give their anomalous response regarding each subject at the end of their semester.

## Getting Started


Through this system, the student can give feedback on lecture quality, assignment quality and many other things with any messages or opinion regarding each subject which they want to share with their respective teachers.


### Prerequisites

You need to install these softwares

```
Python
Flask
MongoDB
Bootstrap
```


### Installing

##### Installation and running steps for MongoDB 

Link given below to install.

- [https://www.mongodb.com](https://www.mongodb.com)


After installation

```
Made a data folder in c: drive.
Inside data folder made a db folder.
```

How to run 

```
First open the terminal.
Navigate to bin folder of mongodb, where mangodb was insatalled.
run for mongod.


open another terminal.
Navigate to bin folder of mongodb, where mangodb was insatalled.
run for mongo.

```

##### Installation steps for Python 

Link given below to install .

- [https://www.python.org](https://www.python.org)

##### Installation steps for Flask 

Go to terminal.

```
pip install flask.
```

##### Installation steps for Robo 3T 

This is MongoDB GUI with embedded shell. This GUI will help you to work with your background data which is taking from feedback system.

-[https://robomomgo.org](https://robomomgo.org)


## Running the tests

- First run the MangoDB and then run the real.py. 
- These project.html, submit.html, exits.html should be in template folder.
- And real.py and template folder should be in same directory.

#### We check the inserted data in our database system

Given below steps make sure that insereted data is inserted or not. 

```
Go to that terminal in which you run the mongo cell.
db.getCollection('students').find({})
```





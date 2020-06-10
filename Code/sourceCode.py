import pickle

class Student:
    def __init__(self, name, ID, batch, major):
        self.name = name
        self.ID = ID
        self.batch = batch
        self.major = major

class Instructor:
    def __init__(self, name, school, bio):
        self.name = name
        self.school = school
        self.bio = bio

class Course:
    def __init__(self, name, ID, level, CR):
        self.name = name
        self.ID = ID
        self.level = level
        self.CR = CR

def addStudent():
    name = input()
    ID = input()
    batch = input()
    major = input()
    Data['Students'][Student(name, ID, batch, major)] = []

def addCourse():
    name = input()
    ID = input()
    level = input()
    CR = input()
    Data['Courses'][Course(name, ID, level, CR)] = []

def addInstructor():
    name = input()
    school = input()
    bio = input()
    Data['Instructors'][Instructor(name, school, bio)]

Data = pickle.load(open('Data','rb'))

print(Data)

pickle.dump(Data, open("Data", 'wb'))


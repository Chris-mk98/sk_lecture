class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
    
    def totalScore(self):
        return self.korean+self.english+self.math
    
    def meanScore(self):
        return self.totalScore()/3
    
    def printScore(self):
        return(f"""
Student's name: {self.name}
Korean: {self.korean}
Math: {self.math}
English: {self.english}
total score: {self.totalScore()}
Mean: {round(self.meanScore())}.
========================================
""")


student_list = [Student("Alice", 100, 85, 67), Student("Bob", 78, 52, 19), Student("Chris", 54, 97, 37), Student("David", 21, 57, 84), Student("John", 78, 54, 61)]

for student in student_list:
    print(student.printScore())

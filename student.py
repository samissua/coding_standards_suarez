"""Module providing a function """
import math
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name =name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, g):
        """Function to add grades to student"""
        try:
            if (math.isclose(float(g), 0.0) or (float(g)>0.0)) and (math.isclose(float(g),100.0) or (float(g)<100.0)):
                self.grades.append(g)
        except ():
            print("Not apropiate grade")

    def calc_average(self):
        """Function to calculate average grade."""
        t=0
        i=0
        for x in self.grades:
            t+=x
            i+=1
        avg=t/i

        if avg<60.0:
            return "F"
        elif (math.isclose(avg, 60.0) or (avg>60.0)) and (avg<70.0):
            return "D"
        elif (math.isclose(avg, 70.0) or (avg>70.0)) and (avg<80.0):
            return "C"
        elif (math.isclose(avg, 80.0) or (avg>80.0)) and (avg<90.0):
            return "B"
        elif (math.isclose(avg, 90.0) or (avg>90.0)) and (math.isclose(avg,100.0) or (avg<100.0)):
            return "A"

    def check_honor(self):
        """Function to check if student is electible for honors."""
        if self.calc_average()=="A":
            self.honor = True
        else:
            self.honor = False

    def delete_grade(self, index):
        """Function to delete a grade given an index."""
        del self.grades[index]

    def check_passed(self):
        """Function to check if student has passed"""
        if self.calc_average()!="F":
            self.is_passed="PASSED"
        else:
            self.is_passed="FAILED"

    def report(self):
        """Function to generate a report of student"""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.is_passed)


    def startrun(self):
        """Test"""
        a = Student("x","")
        a.add_grades(100)
        a.add_grades("Fifty")
        a.calc_average()
        a.check_honor()
        a.delete_grade(5)
        a.report()
    startrun()

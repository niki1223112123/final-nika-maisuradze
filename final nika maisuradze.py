class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.grades = []

    def addgrade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade should be between 0 and 100.")

    def finalgrade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class Student:
    def __init__(self, name):
        self.name = name 
        self.courses = {}

    def addcourse(self, coursename, credits):
        if coursename not in self.courses:
            self.courses[coursename] = Course(coursename, credits)

    def removecourse(self, coursename):
        if coursename in self.courses:
            del self.courses[coursename]
        else:
            print("Course not found.")

    def gpa(self):
        totalcredits = 0
        totalgradepoints = 0

        for course in self.courses.values():
            average = course.finalgrade()
            if average >= 91 >=100:
                gradepoint = 4.0 
                print("A")
            elif average >= 81:
                gradepoint = 3.0
                print("B")  
            elif average >= 71: 
                gradepoint = 2.0
                print("C")  
            elif average >= 61:
                gradepoint = 1.0
                print("D")
            elif average >=0 <= 60:
                gradepoint = 0.0
                print("F")

            totalgradepoints += gradepoint * course.credits
            totalcredits += course.credits

        if totalcredits == 0:
            return 0
        return totalgradepoints / totalcredits

    def transcript(self):
        transcript = f"Student: {self.name}\n"
        for coursename, course in self.courses.items():
            average = course.finalgrade()
            transcript += f"{coursename} ({course.credits} credits): {average:.1f}\n"
        transcript += f"GPA: {self.gpa():.1f}"
        return transcript
    
Student= Student("John doe")
Student.addcourse("Math", 10)
Student.addcourse("Science", 5)
math_course = Student.courses["Math"]
math_course.addgrade(85)
math_course.addgrade(92)

science_course = Student.courses["Science"]
science_course.addgrade(78)
science_course.addgrade(88)
print(Student.transcript())
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
            if average >= 91:
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
            else:
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
    
    def savefile(self, filename="students.txt"):
        with open(filename, "w") as file:
            file.write(self.transcript())
        print(f"Transcript saved to {filename}")



    def studentsfromfile(filename="students.txt"):
        students = {}
        with open(filename, "r") as file:
            for i in file:
                data = i.strip().split(',')
                name, coursename, credits, *grades = data
                grades = [int(grade) for grade in grades]
                if name not in students:
                    students[name] = Student(name)
                students[name].addcourse(coursename, int(credits))
                for grade in grades:
                    students[name].courses[coursename].addgrade(grade)
        return students

    students = studentsfromfile("students.txt")
    for student in students.values():
        print(student.transcript())

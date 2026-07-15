class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        
        Student.count += 1
        Student.total_gpa += gpa
        
    #intace method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    @classmethod
    def get_count(cls):
        return f"totalnumber of students {cls.count}"
    @classmethod
    
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"
    
s1 =Student("Muhammad Idrees", 2.93)
s2 = Student("marjan", 4.40)

s2 = Student("marjan fatima", 3.40)
print(Student.get_count())
        
print(Student.get_average())
class CID:
    def __init__(self, cid, name=None, id=None, information=None):
        self.cid = cid
        self.name = name
        self.id = id
        self.information = information

    def display(self):
        return f"CID: {self.cid}, Name: {self.name}, ID: {self.id}, Info: {self.information}"

    def __str__(self):
        return self.display()


class Teacher(CID):
    def teach(self, subject):
        return f"{self.name} teaches {subject}."


class Student(CID):
    def study(self, subject):
        return f"{self.name} studies {subject}."


class Staff(CID):
    def work(self):
        return f"{self.name} is working."


# Example usage
t = Teacher("T001", "Mr. Smith", "101", "Math teacher")
s = Student("S001", "Alice", "202", "Computer Science student")
st = Staff("ST001", "John", "303", "Administrator")

print(t)
print(s)
print(st)

print(t.teach("Math"))
print(s.study("Python"))
print(st.work())


class Student:

    # Constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Display student details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    # Update marks
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"{self.name}'s marks updated to {self.marks}")

    # Check pass/fail status
    def is_passed(self):
        return self.marks >= 40


# Creating student objects
student1 = Student("Rahul", 101, 85)
student2 = Student("Aman", 102, 32)


# Display Rahul's details
print("----- Student 1 -----")
student1.display_details()

if student1.is_passed():
    print("Status: Passed")
else:
    print("Status: Failed")


# Display Aman's details
print("\n----- Student 2 -----")
student2.display_details()

if student2.is_passed():
    print("Status: Passed")
else:
    print("Status: Failed")


# Update Aman's marks
print("\n----- Updating Marks -----")
student2.update_marks(55)

# Display updated details
student2.display_details()

if student2.is_passed():
    print("Status: Passed")
else:
    print("Status: Failed")

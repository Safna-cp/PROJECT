students = {
    "safna": "100",
    "amaya": "101",
    "ashitha": "102"
}
name = input("Enter student name: ").strip().lower()
student_id = students.get(name)
print("id is:",student_id)
 
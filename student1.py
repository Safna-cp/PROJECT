students = {
    "safna": "100",
    "amaya": "101",
    "ashitha": "102"
}
name = input("Enter student name: ").strip().lower()
student_id = students.get(name)
if student_id:
    print(f"The ID of {name.capitalize()} is {student_id}")
else:
    print(f"No student found with the name '{name}'")

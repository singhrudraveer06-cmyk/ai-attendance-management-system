import json
import os
from datetime import date

DATA_FILE = "attendance.json"

def load_data():
    """Loads student data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    """Saves student data back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    """Adds a new student record."""
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    data = load_data()

    
    for s in data:
        if s.get("roll") == roll:
            print("A student with this roll already exists.")
            return

    data.append({"name": name, "roll": roll, "attendance": {}})
    save_data(data)
    print("Student added successfully.")

def show_students():
    """Displays a list of all students."""
    data = load_data()
    if not data:
        print("No students found.")
        return
    print("Roll\tName")
    for s in data:
        print(f"{s['roll']}\t{s['name']}")

def mark_attendance():
    """Marks attendance for all students for the current date."""
    data = load_data()
    if not data:
        print("No students to mark.")
        return

    today = str(date.today())
    print(f"Mark attendance for {today} (P for present, A for absent):")
    for s in data:
        while True:
            status = input(f"{s['name']} ({s['roll']}): ").strip().upper()
            if status in ("P", "A"):
                break
            print("Enter P or A only.")
        
        # ensure attendance is a dict keyed by date
        if "attendance" not in s:
            s["attendance"] = {}
        s["attendance"][today] = status

    save_data(data)
    print("Attendance recorded for", today)

def view_attendance():
    """Views attendance records for a specific date or all dates."""
    data = load_data()
    if not data:
        print("No data found.")
        return
    date_req = input("Enter date (YYYY-MM-DD) or press Enter for all: ").strip()
    if date_req == "":
        for s in data:
            print(f"\n{s['roll']} - {s['name']}")
            for d, st in s.get("attendance", {}).items():
                print(f"  {d}: {st}")
    else:
        print(f"Attendance on {date_req}:")
        for s in data:
            st = s.get("attendance", {}).get(date_req, "-")
            print(f"{s['roll']} - {s['name']}: {st}")

def delete_student():
    """Deletes a student record by roll number."""
    roll = input("Enter roll number to delete: ").strip()
    data = load_data()
    
    # Check if the student exists
    student_exists = any(s.get("roll") == roll for s in data)
    
    if not student_exists:
        print(f"No student found with roll number '{roll}'.")
        return
    
    new = [s for s in data if s.get("roll") != roll]
    save_data(new)
    print(f"Student with roll number '{roll}' record deleted.")

def calculate_percentage():
    """Calculates and displays the overall attendance percentage for a student."""
    roll = input("Enter student roll number to view stats: ").strip()
    data = load_data()
    
    # Find the student using 'next'
    student = next((s for s in data if s.get("roll") == roll), None)

    if not student:
        print(f"No student found with roll number '{roll}'.")
        return

    attendance_data = student.get("attendance", {})
    total_days = len(attendance_data)
    
    if total_days == 0:
        print(f"{student['name']} has no attendance records.")
        return

    present_days = sum(1 for status in attendance_data.values() if status == "P")
    
    # Calculate percentage
    percentage = (present_days / total_days) * 100
    
    print(f"\nAttendance Statistics for {student['name']} ({student['roll']}):")
    print(f"  Total days recorded: {total_days}")
    print(f"  Days Present: {present_days}")
    print(f"  Days Absent: {total_days - present_days}")
    print(f"  Attendance Percentage: **{percentage:.2f}%**")

def predict_risk():
    import pickle
    
    roll = input("Enter student roll number: ").strip()
    data = load_data()

    student = next((s for s in data if s.get("roll") == roll), None)

    if not student:
        print("Student not found.")
        return

    attendance_data = student.get("attendance", {})
    total = len(attendance_data)

    if total == 0:
        print("No attendance data.")
        return

    present = sum(1 for v in attendance_data.values() if v == "P")
    percentage = (present / total) * 100

    # Load AI model
    model = pickle.load(open("model.pkl", "rb"))

    import pandas as pd
    prediction = model.predict(pd.DataFrame([[percentage]], columns=['attendance']))[0]

    print(f"\nAttendance: {percentage:.2f}%")
    print(f"Risk Level: {prediction}")

    if percentage < 75:
        needed = int(((0.75 * total) - present) / (1 - 0.75)) + 1
        print(f"Attend next {needed} classes to reach 75%")
        
def main():
    """The main menu loop for the Attendance Management System."""
    while True:
        print("\n--- Attendance Management System ---")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. View Student List")
        print("5. Delete Student")
        print("6. Calculate Attendance Percentage") 
        print("7. Predict Attendance Risk")
        print("8. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            show_students()
        elif choice == "5":
            delete_student()
        elif choice == "6": 
            calculate_percentage()
        elif choice == "7":
            predict_risk()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

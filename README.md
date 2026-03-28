# AI-Based Smart Attendance Management System

## Project Details

* **Course:** **Fundamentals of AI and ML**
* **Student Name:** Rudraveer Singh
* **Registration Number:** 25BCE10659
* **Project Type:** CLI-based AI + CRUD Application
* **Semester:** 2nd Semester

---

## Overview

This project was developed to solve the common issue of students falling short of attendance due to lack of tracking and timely feedback.
It not only stores and manages student attendance but also predicts whether a student is at risk of low attendance.

---

## Problem Statement

In many cases, students are unaware of their attendance status until it is too late, leading to academic issues.
Traditional systems only store data but do not provide insights or warnings.

---

## Solution

This system:

* Manages attendance records
* Calculates attendance percentage
* Predicts attendance risk using machine learning
* Provides suggestions to maintain required attendance

---

## Features

* Add, update, delete student records (CRUD)
* Mark attendance (P/A)
* View attendance records
* Calculate attendance percentage
*  AI-based risk prediction:

  * Safe
  * Warning
  * Critical
* Suggests how many classes to attend to reach 75%

---

## AI Model

* Model Used: Decision Tree Classifier
* Input: Attendance percentage
* Output: Risk level

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* JSON/File Handling

---

## Project Structure

```
├── code.py
├── model.py
├── dataset.csv
├── model.pkl
├── attendance.json
├── README.md
└── report.pdf
```

---

## How to Run

1. Install dependencies:
   pip install pandas scikit-learn

2. Train the model:
   py model.py

3. Run the application:
   py "code.py"

---

## Example Output

Attendance: 60%
Risk Level: Warning
Suggestion: Attend next 10 classes to reach 75%

---

## Conclusion

This project shows how AI can enhance traditional systems and make them more intelligent and useful in real-world scenarios.

---

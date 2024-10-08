# academic_scores.py

import pandas as pd
import random
from datetime import datetime

# Set random seed for reproducibility
random.seed(42)

# Define subjects and streams for students
streams = {
    "Art": ["Literature in English", "History", "Government", "CRK", "English", "Mathematics", "Yoruba", "Economics", "Civic Education"],
    "Commercial": ["Accounting", "Commerce", "Economics", "Marketing", "English", "Mathematics", "Civic Education", "Business Administration"],
    "Pure Science": ["Physics", "Chemistry", "Biology", "Mathematics", "English", "Food and Nutrition", "Civic Education","Computer Studies"],
    "Engineering": ["Further Mathematics", "Physics", "Technical Drawing", "Mathematics", "Chemistry", "English", "Civic Education","Computer Studies"]
}

jss_subjects = [
    "English Studies", "Literature in English", "Social Studies", "Basic Science",
    "Business Studies", "Book-Keeping & Accounts", "Mathematics", "Agricultural Science",
    "French", "Basic Technology", "Computer Studies", "Physical & Health Education",
    "Home Economics", "Christian Religious Studies", "Fine Arts", "Music", "Citizenship Education", "Yoruba", "CRK"
]

# Helper function to assign a teacher to a subject
def assign_teacher(subject, subject_teacher_map):
    return random.choice(subject_teacher_map[subject])  # Always return a valid teacher for the subject

# Function to generate test, exam scores, and attendance for each subject
def generate_subject_scores_and_attendance():
    term_scores = {}
    for term in ["First Term", "Second Term", "Third Term"]:
        test_score = random.randint(15, 40)  # Test score out of 40
        exam_score = random.randint(30, 60)  # Exam score out of 60
        total_score = test_score + exam_score  # Total score out of 100
        attendance = random.randint(70, 100)  # Attendance percentage out of 100
        term_scores[term] = {"Test": test_score, "Exam": exam_score, "Total": total_score, "Attendance": attendance}

    cumulative_score = sum(term_scores[term]["Total"] for term in term_scores) / 3
    average_attendance = sum(term_scores[term]["Attendance"] for term in term_scores) / 3
    return term_scores, cumulative_score, average_attendance

# Helper function to calculate the starting grade level based on admission year and current grade
def determine_starting_grade(admission_year, current_grade_level):
    grade_levels = ["JSS1", "JSS2", "JSS3", "SS1", "SS2", "SS3"]
    grade_index = grade_levels.index(current_grade_level)
    start_index = max(0, grade_index - (datetime.now().year - admission_year))
    return grade_levels[start_index]

# Function to generate academic history for students based on their starting grade and current grade level
def generate_academic_history(student_id, grade_level, stream, admission_year, subject_teacher_map):
    academic_history = {}
    passed_core_subjects = None  # Randomly chosen below for SS3 students
    jamb_score = None

    # Calculate starting grade level
    start_grade = determine_starting_grade(admission_year, grade_level)
    grade_levels = ["JSS1", "JSS2", "JSS3", "SS1", "SS2", "SS3"]

    # Generate academic history starting from the admission grade up to the current grade level
    start_index = grade_levels.index(start_grade)
    end_index = grade_levels.index(grade_level)

    for i in range(start_index, end_index + 1):
        level = grade_levels[i]
        if level.startswith("JSS"):
            academic_history[level] = {subject: generate_subject_scores_and_attendance() for subject in jss_subjects}
        elif level.startswith("SS"):
            ss_subjects = streams[stream] if stream in streams else []
            academic_history[level] = {subject: generate_subject_scores_and_attendance() for subject in ss_subjects}

    # Additional logic for SS3 students
    if grade_level == "SS3":
        jamb_score = random.randint(150, 340)  # Generate a random JAMB score for SS3 students
        passed_core_subjects = random.choice(["Yes", "No"])  # Randomly assign "Passed Core Subjects" as "Yes" or "No"

    return academic_history, jamb_score, passed_core_subjects

# Create a dictionary mapping subjects to teacher IDs based on teacher specialization
def create_subject_teacher_map(teachers_df):
    subject_teacher_map = {}
    for _, teacher in teachers_df.iterrows():
        subject = teacher["Subject Specialization"]
        if subject not in subject_teacher_map:
            subject_teacher_map[subject] = []
        subject_teacher_map[subject].append(teacher["Teacher ID"])
    
    # Ensure every subject has at least one teacher assigned
    all_subjects = set(jss_subjects) | set(sum(streams.values(), []))  # Union of all subjects
    for subject in all_subjects:
        if subject not in subject_teacher_map:
            subject_teacher_map[subject] = [random.choice(teachers_df["Teacher ID"].tolist())]

    return subject_teacher_map

# Main function to generate academic history and save it as a CSV
def save_academic_history_data(students_filename="students_bio_data.csv", teachers_filename="Teachers_bio_data.csv", output_filename="academic_history_data.csv"):
    # Read the existing student bio-data and teacher data
    students_df = pd.read_csv(students_filename)
    teachers_df = pd.read_csv(teachers_filename)

    # Create subject-teacher map
    subject_teacher_map = create_subject_teacher_map(teachers_df)

    # Create a new dataframe for academic history
    academic_history_data = []

    # Iterate through each student and generate the academic history based on their admission date and current grade
    for index, row in students_df.iterrows():
        student_id = row["Student ID"]
        grade_level = row["Grade Level"]
        stream = row["Stream"]
        admission_year = int(row["Admission Date"].split("-")[0])

        # Generate academic history, JAMB score, and core subject pass status for the student
        academic_history, jamb_score, passed_core_subjects = generate_academic_history(student_id, grade_level, stream, admission_year, subject_teacher_map)

        # Create a record for academic history with student ID and the grades
        for level, subjects in academic_history.items():
            for subject, (scores, cumulative, avg_attendance) in subjects.items():
                teacher_id = assign_teacher(subject, subject_teacher_map)  # Assign teacher based on subject
                for term, term_scores in scores.items():
                    academic_history_data.append({
                        "Student ID": student_id,
                        "Grade Level": level,
                        "Subject": subject,
                        "Term": term,
                        "Teacher ID": teacher_id,
                        "Test Score": term_scores["Test"],
                        "Exam Score": term_scores["Exam"],
                        "Total Score": term_scores["Total"],
                        "Attendance": term_scores["Attendance"],
                        "Cumulative Score": round(cumulative, 2),
                        "Average Attendance": round(avg_attendance, 2),
                        "JAMB Score": jamb_score if level == "SS3" else None,
                        "Passed Core Subjects": passed_core_subjects if level == "SS3" else None
                    })

    # Convert the academic history data to a DataFrame
    academic_history_df = pd.DataFrame(academic_history_data)

    # Calculate the cumulative attendance rate for each student
    cumulative_attendance_df = academic_history_df.groupby("Student ID").agg({
        "Attendance": "mean"  # Calculate the average attendance for all subjects and terms per student
    }).reset_index()
    cumulative_attendance_df.columns = ["Student ID", "Cumulative Attendance Rate"]

    # Merge the cumulative attendance rate back into the academic history DataFrame
    academic_history_df = academic_history_df.merge(cumulative_attendance_df, on="Student ID", how="left")

    # Save the academic history with cumulative attendance, JAMB scores, and Teacher IDs to a new CSV file
    academic_history_df.to_csv(output_filename, index=False)
    print(f"Academic history data saved to {output_filename}")

# Run the data generation if this script is run as main
if __name__ == "__main__":
    save_academic_history_data()

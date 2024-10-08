# main.py
import os
from students_data import save_students_data
from teachers_data import save_teachers_data
from parents_data import save_parents_data
from academic_scores import save_academic_history_data

def main():
    # Create output directory if not exists
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate and save datasets
    save_students_data(os.path.join(output_dir, "students_bio_data.csv"))
    save_teachers_data(os.path.join(output_dir, "teachers_data.csv"))
    save_parents_data(os.path.join(output_dir, "parents_data.csv"))
    save_academic_history_data(os.path.join(output_dir, "academic_scores_data.csv"))

if __name__ == "__main__":
    main()

# students_data.py
import pandas as pd
import random
from datetime import datetime

# Set random seed for reproducibility
random.seed(42)

# Define lists of names and other attributes


# Define common Nigerian first and last names
nigerian_first_names = [
    "Adeola", "Chinedu", "Ifeanyi", "Oluwaseun", "Emeka", "Ngozi", "Temitope", 
    "Kehinde", "Yemi", "Nneka", "Adebayo", "Abiodun", "Chisom", "Ijeoma", 
    "Uche", "Gbenga", "Tunde", "Bola", "Chidi", "Bimbo", "Bisi", "Bassey", 
    "Ikechukwu", "Musa", "Aisha", "Rashidat", "Fatima", "Hassan", "Sadiq",
    "Bukola", "Adamu", "Umar", "Sani", "Ibrahim", "Samuel", "Sunday", "Blessing", 
    "Mercy", "Patience", "Omotola", "Tolu", "Chika", "Olamide", "Funke", "Damilola",
  
    "Lovina", "Ibrahim", "Chidiebere", "Isma'il", "Samuel", "Amiel", "Henry", 
    "Nanle", "Alhaji", "Augustina", "Christiana", "Khadijah", "Betty", "Felix", 
    "Jerome", "Umar", "Victoria", "Asukwo", "Tajudeen", "Johnson", "Charity", 
    "Longdi", "Sunday", "Jamilu", "Oladipupo", "Mary", "Nwanyinnaya", "Ebisu", 
    "Ude", "Olanrewaju", "Mathew", "Yohanna", "Kitoye", "Kenith", "Emmanuel", 
    "Monisola", "Nihinlola", "Silas", "Muhammad", "Adamu", "Umahi", "Mustapha", 
    "Ayodele", "Binam", "John-pius", "Dare", "Victor", "Sodiq", "Ufedo", "Gerald", 
    "Emmanuel", "Mohammed", "Philip", "Sunday", "Igbalumun", "Ayodeji", "Samuel", 
    "Funbi", "Chukwunonso", "Emeke", "Blessing", "Lateef", "Mathew", "Cyril", 
    "Isong", "Emmanuel", "Nduka", "Anzaku", "Abba", "Musa", "Maxwell", "Harisu", 
    "Johnson", "Femi", "Sadiq", "Peter", "Lilian", "Babatunde", "Waheed", "Agai", 
    "Godwin", "Emmanuel", "Hassan", "Clement", "Esther", "Mhungur", "Oleje", 
    "Kabiru", "Bridget", "Isiaka", "Nnedinma", "Ndubuisi", "Emmanuel", "Ternenge", 
    "Joseph", "Inimfon", "Joy", "Felicia", "Zaharudeen", "Omotomilola", "Gbuuka", 
    "Rasaki", "Ifeoma", "Abdullahi", "Hassanat", "Franklin", "Kelechi", "Sani", 
    "Ruth", "Temitayo", "Edward", "Ngozi", "Zayyanu", "Adekunle", "Jafar", "Olatunde", 
    "Isah", "Blessing", "Paul", "Oliver", "Oluwaseun", "Amadi", "Naomi", "Joseph", 
    "Adewumi", "Fatai", "Ugonma", "Mansir", "Haladu", "Terhemba", "Isiyaka", "Sunday", 
    "Binny", "Daniel", "Amomot", "John", "Chinonso", "Vivian", "Fidelis", "Uchechukwu", 
    "Matthew", "Saidu", "Bashar", "Collins", "Nneka", "Roseline", "Alice", "Felicia", 
    "Ibrahim", "Nnamdi", "Zahra", "Kingsley", "Mustapha", "Charity", "Funke", "Atim", 
    "Philip", "Zainab"
]

nigerian_last_names = [
    "Akinola", "Balogun", "Okoro", "Oluwole", "Adebayo", "Nwosu", "Obi", "Ibrahim", 
    "Ahmed", "Ogundele", "Oladipo", "Chukwu", "Anyanwu", "Olayinka", "Eze", 
    "Ogbonna", "Adeleke", "Ogunleye", "Okeke", "Olorunfemi", "Ebi", "Abubakar", 
    "Idris", "Onyeka", "Oduwole", "Mohammed", "Hassan", "Lawal", "Udo", "Ekanem", 
    "Bello", "Fashola", "Osakwe", "Danladi", "Nnamdi", "Femi", "Yusuf", "Ogidi", 
    "Yaro", "Oyedepo", "Alabi", "Ajayi", "Ajibola", "Oshodi", "Ogunsanya", "Baba",
    "Sanni", "Aloye", "Aduku", "Mmaduako", "Salam", "Adesakin", "Sheriff", "Yakubu", 
    "Igbe", "Zarami", "Adebayo", "Stephen", "Yusuf", "Usman", "Olorunfemi", "Ejugwu", 
    "Ishaya", "Okafor", "Jabbi", "Ejeh", "Omesili", "Jayeola", "Uyieidem", "Omora", 
    "Elkanah", "Elaigwu", "Kolapo", "Oluwasanmi", "Abdullahi", "Nwaogwugwu", "Sanbauna", 
    "Ibrahim", "Grace", "Saadu", "Etim", "Akinlade", "Egbunu", "Ene", "Oni", "Okon", 
    "Andrew", "Ladan", "Ogbozor", "Ochoja", "Aminu", "Edeh", "Nnamani", "Otu", 
    "Mohammed", "Adegunju", "Abraham", "Ezeji", "Augustine", "Nnenanya", "Ajeigbe", 
    "Ehanmo", "Eze", "Osanyintipin", "Tsadu", "Njoku", "Ibiam", "Mohammed", "Udofia", 
    "Olaleye", "Amus", "Ekpe", "Odoh", "Okwe", "Ogunbanjo", "Patrick", "Ibiam", "Ehanmo", 
    "Njoku", "Osanyintipin", "Yakubu", "Egbon", "Rasaki", "Abdulqadir", "Ogore", "Kelechi", 
    "James", "Osanyintipin", "Omoh", "Ibiam", "Obiora", "Onyeka", "Udo", "Musa", "Bashar", 
    "Ahmad", "Yusuf", "Afolayan", "Badamasi", "Arinze", "Nnaemeka", "Okorie", "Abdulaziz", 
    "Adeola", "Ahmad", "Sunday", "Nnanna", "Okolie", "Anaba", "Isong", "Igwe", "Akinbode", 
    "Ogunyemi", "Sogbetun", "Oyeniran", "Oguntayo", "Ayeni", "Ehanmo", "Odugu", "Odumodu", 
    "Anjorin", "Okeke", "Onyeka", "Asemota", "Nwadi", "Yekini", "Taiwo", "Uwa", "Igbo", 
    "Yahaya", "Sani", "Yusuf"
]



# Define extracurricular activities
extracurricular_activities = ["Sports", "Music", "Drama", "Debate", "Clubs"]


# Additional Data
lagos_lgas = [
    "Agege", "Alimosho", "Apapa", "Ifako-Ijaye", "Ikeja", "Kosofe", "Mushin", "Oshodi-Isolo", 
    "Shomolu", "Eti-Osa", "Lagos Island", "Lagos Mainland", "Surulere", "Ojo", 
    "Ajeromi-Ifelodun", "Amuwo-Odofin", "Badagry", "Ikorodu", "Ibeju-Lekki", "Epe"
]

state_of_origin = [
    "Abuja", "Kogi", "Kwara", "Nasarawa", "Niger", "Benue", "Plateau", "Adamawa", "Bauchi", 
    "Borno", "Gombe", "Taraba", "Yobe", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", 
    "Sokoto", "Zamfara", "Abia", "Anambra", "Ebonyi", "Enugu", "Imo", "Akwa Ibom", 
    "Bayelsa", "Cross River", "Delta", "Edo", "Rivers", "Ekiti", "Lagos", "Ogun", 
    "Ondo", "Osun", "Oyo"
]

# Define subjects and streams for students
streams = {
    "Art": ["Literature", "History", "Government", "CRK", "English"],
    "Commercial": ["Accounting", "Commerce", "Economics", "Business Studies", "English"],
    "Pure Science": ["Physics", "Chemistry", "Biology", "Mathematics", "English"],
    "Engineering": ["Further Mathematics", "Physics", "Technical Drawing", "Chemistry", "English"]
}

jss_subjects = [
    "English Studies", "Literature in English", "Social Studies", "Basic Science", 
    "Business Studies", "Book-Keeping & Accounts", "Mathematics", "Agricultural Science", 
    "French", "Basic Technology", "Computer Studies", "Physical & Health Education", 
    "Home Economics", "Christian Religious Studies", "Fine Arts", "Music", "Citizenship Education"
]


# Generate a list of Nigerian names
def generate_nigerian_names(num_names=500):
    generated_names = [(random.choice(nigerian_first_names), random.choice(nigerian_last_names)) for _ in range(num_names)]
    return generated_names


# Pre-generated Nigerian names
nigerian_first_last_names = generate_nigerian_names()


# Generate random admission and graduation dates
def generate_admission_graduation_dates(current_grade):
    admission_year = datetime.now().year - random.randint(3, 7)  # Randomly choose between 3 to 7 years ago
    years_to_graduation = {"JSS1": 5, "JSS2": 4, "JSS3": 3, "SS1": 2, "SS2": 1, "SS3": 0}
    graduation_year = admission_year + years_to_graduation[current_grade]
    return f"{admission_year}-09-01", f"{graduation_year}-06-30"



# Function to calculate date of birth based on age
def calculate_date_of_birth(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return datetime(birth_year, random.randint(1, 12), random.randint(1, 28)).strftime("%Y-%m-%d")

# Function to generate a formatted address
def generate_address(lga):
    return f"{random.randint(1, 100)}, {random.choice(['Street', 'Avenue', 'Road'])} in {lga}, Lagos State"

# Function to randomly assign extracurricular activities
def assign_extracurricular_activities():
    # Randomly decide the number of activities for a student (including the option for no activity)
    num_activities = random.choices([0, 1, 2], weights=[0.5, 0.3, 0.2], k=1)[0]  # 50% chance of no activities
    if num_activities == 0:
        return "None"
    else:
        return ", ".join(random.sample(extracurricular_activities, num_activities))

# Function to generate health status and disorder fields
def generate_health_status_and_disorder(total_students):
    health_status_options = ["Good", "Average", "Poor"]
    health_statuses = [random.choice(health_status_options) for _ in range(total_students)]
    yes_disorder_count = max(1, int(total_students * 0.1))  # Ensure at least 1 disorder if sample size is small
    disorders = ["No"] * total_students
    yes_indices = random.sample(range(total_students), yes_disorder_count)
    for index in yes_indices:
        disorders[index] = "Yes"
    return health_statuses, disorders

# Generate Students Data Without Academic Information
def generate_students(num_students=600):
    health_statuses, disorders = generate_health_status_and_disorder(num_students)
    students = []
    for i in range(num_students):
        first_name, last_name = random.choice(nigerian_first_last_names)
        state = random.choice(state_of_origin)
        lga = random.choice(lagos_lgas)
        age = random.randint(10, 20)
        home_address = generate_address(lga)
        date_of_birth = calculate_date_of_birth(age)
        email = f"{first_name.lower()}.{last_name.lower()}@laurelhigh.com"
        grade_level = random.choices(["JSS1", "JSS2", "JSS3", "SS1", "SS2", "SS3"], weights=[0.25, 0.15, 0.20, 0.10, 0.10, 0.20], k=1)[0]
        admission_date, graduation_date = generate_admission_graduation_dates(grade_level)
        stream = random.choice(["General", "Art", "Commercial", "Pure Science", "Engineering"]) if grade_level.startswith("SS") else "General"

        # Assign extracurricular activities
        extracurricular = assign_extracurricular_activities()

        student = {
            "Student ID": f"STU{i+1:03d}",
            "First Name": first_name,
            "Last Name": last_name,
            "Gender": random.choice(["Male", "Female"]),
            "Age": age,
            "Date of Birth": date_of_birth,
            "Health Status": health_statuses[i],
            "Disorder": disorders[i],
            "State of Origin": state,
            "LGA of residence": lga,
            "Home Address": home_address,
            "Living Arrangement": random.choice(["Day", "Boarding"]),
            "Email": email,
            "Grade Level": grade_level,
            "Stream": stream,
            "Extracurricular Activities": extracurricular,
            "Admission Date": admission_date,
            "Graduation Date": graduation_date
        }
        students.append(student)

    return pd.DataFrame(students)

# Save the generated data to CSV
def save_students_data(filename="students_bio_data.csv"):
    students_df = generate_students()
    students_df.to_csv(filename, index=False)
    print(f"Student bio-data saved to {filename}")

# Run the data generation if this script is run as main
if __name__ == "__main__":
    save_students_data()

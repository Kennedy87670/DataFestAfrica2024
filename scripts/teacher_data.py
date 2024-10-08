
# teacher_data.py
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

state_of_origin = [
    "Abuja", "Kogi", "Kwara", "Nasarawa", "Niger", "Benue", "Plateau", "Adamawa", "Bauchi", 
    "Borno", "Gombe", "Taraba", "Yobe", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", 
    "Sokoto", "Zamfara", "Abia", "Anambra", "Ebonyi", "Enugu", "Imo", "Akwa Ibom", 
    "Bayelsa", "Cross River", "Delta", "Edo", "Rivers", "Ekiti", "Lagos", "Ogun", 
    "Ondo", "Osun", "Oyo"
]


lagos_lgas = [
    "Agege", "Alimosho", "Apapa", "Ifako-Ijaye", "Ikeja", "Kosofe", "Mushin", "Oshodi-Isolo", 
    "Shomolu", "Eti-Osa", "Lagos Island", "Lagos Mainland", "Surulere", "Ojo", 
    "Ajeromi-Ifelodun", "Amuwo-Odofin", "Badagry", "Ikorodu", "Ibeju-Lekki", "Epe"
]

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


# Define a function to generate a formatted address
def generate_address(lga):
    return f"{random.randint(1, 100)}, {random.choice(['Street', 'Avenue', 'Road'])} in {lga}, Lagos State"

# Helper function for date of birth calculation
def calculate_date_of_birth(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return datetime(birth_year, random.randint(1, 12), random.randint(1, 28)).strftime("%Y-%m-%d")


# Function to generate a unique 20-digit LASRRA ID
def generate_lasrra_id():
    return f"{random.randint(10**18, 10**19 - 1)}"

def generate_teachers(num_teachers):
    teachers = []
    for i in range(num_teachers):
        first_name, last_name = random.choice(nigerian_first_last_names)
        lga = random.choice(lagos_lgas)
        home_address = generate_address(lga)
        age = random.randint(30, 60)
        email = f"{first_name.lower()}.{last_name.lower()}@laurelhigh.com"
        salary = random.randint(50000, 300000)
        lasrra_id = generate_lasrra_id()
        teacher = {
            "Teacher ID": f"TCH{i+1:03d}",
            "LASRRA ID": lasrra_id,
            "First Name": first_name,
            "Last Name": last_name,
            "Gender": random.choice(["Male", "Female"]),
            "Age": age,
            "Date of Birth": calculate_date_of_birth(age),
            "State of Origin": random.choice(state_of_origin),
            "Years of Experience": random.randint(1, 35),
            "Qualification": random.choice(["NCE", "Bachelor's", "Master's"]),
            "Home Address": home_address,
            "Email": email,
            "Phone Number": f"+234{random.randint(7010000000, 7099999999)}",
            "Residence Type": random.choice(["Lives in School", "Lives Outside School"]),
            "LGA of residence": lga,
            "Digital Literacy": random.choice(["High", "Medium", "Low"]),
            "Salary ₦": salary,
            "Teaching Level": random.choice(["Junior", "Senior"]),
            "Subject Specialization": random.choice(list(jss_subjects + list(sum(streams.values(), []))))
        }
        teachers.append(teacher)
    return pd.DataFrame(teachers)



# Save the generated data to CSV
def save_teacher_data(filename="teacher_bio_data.csv"):
    teacher_df = generate_teachers()
    teacher_df.to_csv(filename, index=False)
    print(f"Teachers bio-data saved to {filename}")


# Run the data generation if this script is run as main
if __name__ == "__main__":
    save_teacher_data()
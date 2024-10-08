
# paresnts_data.py
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


# Function to generate a unique 20-digit LASRRA ID
def generate_lasrra_id():
    return f"{random.randint(10**18, 10**19 - 1)}"

parent_titles = ["Mr.", "Mrs.", "Dr.", "Prof.", "Chief"]


# Generate a list of Nigerian names
def generate_nigerian_names(num_names=500):
    generated_names = [(random.choice(nigerian_first_names), random.choice(nigerian_last_names)) for _ in range(num_names)]
    return generated_names


# Pre-generated Nigerian names
nigerian_first_last_names = generate_nigerian_names()


# Function to calculate date of birth based on age
def calculate_date_of_birth(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return datetime(birth_year, random.randint(1, 12), random.randint(1, 28)).strftime("%Y-%m-%d")


# Function to generate parents data with at least one and at most four students assigned
def generate_parents(student_df):
    parent_data = []
    parent_index = 1

    # Shuffle the student dataframe to randomly assign students to parents
    shuffled_students = student_df.sample(frac=1).reset_index(drop=True)

    # Group students into families of size between 1 and 4
    start = 0
    while start < len(shuffled_students):
        family_size = random.randint(1, 4)  # Each parent will have between 1 and 4 children
        family_students = shuffled_students.iloc[start:start + family_size]

        # Generate a parent for the family
        first_name, last_name = random.choice(nigerian_first_last_names)
        age = random.randint(30, 60)
        lga = random.choice(lagos_lgas)
        home_address = family_students.iloc[0]["Home Address"]
        email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
        parent_id = f"PAR{parent_index:03d}"
        lasrra_id = generate_lasrra_id()

        # Create a parent entry for each child
        for _, student in family_students.iterrows():
            parent = {
                "Parent ID": parent_id,
                "LASRRA ID": lasrra_id,
                "Student ID": student["Student ID"],
                "First Name": first_name,
                "Last Name": last_name,
                "Gender": random.choice(["Male", "Female"]),
                "State of Origin": random.choice(state_of_origin),
                "Title": random.choice(parent_titles),
                "Age": age,
                "Date of Birth": calculate_date_of_birth(age),
                "Email": email,
                "Phone Number": f"+234{random.randint(7010000000, 7099999999)}",
                "Home Address": home_address,
                "Occupation": random.choice(["Farmer", "Teacher", "Engineer", "Medical Professional", "Business", "Civil Servant"]),
                "Financial Status": random.choice(["Low Income", "Middle Income", "High Income"]),
                "Education Level": random.choice(["Primary", "Secondary", "Tertiary"]),
                "Engagement in School Activities": random.choice(["High", "Medium", "Low"]),
                "LGA of residence": lga
            }
            parent_data.append(parent)

        parent_index += 1
        start += family_size  # Move to the next group of students

    return pd.DataFrame(parent_data)

# Save the generated data to CSV
def save_parents_data(filename="parents_bio_data.csv"):
    parents_df = generate_parents()
    parents_df.to_csv(filename, index=False)
    print(f"Parents bio-data saved to {filename}")




# Run the data generation if this script is run as main
if __name__ == "__main__":
    save_parents_data()
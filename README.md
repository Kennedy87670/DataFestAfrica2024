
---

# DataFestAfrica Hackathon 2024 TEAM ZERO: Improving Academic Outcomes For Secondary Education

## 🎯 Project Brief
### Project Title:
**Building a Data-Driven Solution for Laurel High School**

### Description
This project aims to improve academic outcomes for secondary education students by building a comprehensive data-driven solution. The solution involves developing data collection, structuring, and analysis methods to identify critical factors affecting student performance. It also includes building predictive models to assess student performance and offering school administrators and stakeholders actionable insights.

### Project Objective:
To enhance students' academic performance at Laurel High School by leveraging data-driven insights to address educational challenges such as teacher availability, infrastructure quality, and student performance patterns.

### Problem Statement:
The quality of education at Laurel High has faced several challenges that hinder students' ability to perform well in national exams such as JAMB and WASSCE. These challenges include the unavailability of qualified teachers, poor infrastructure, lack of adequate learning resources, and insufficient support for students and teaching staff. This has resulted in below-average academic performance and decreased student engagement.

### Goals:
1. **Identify Areas of Improvement**: Analyze key factors impacting student outcomes at Laurel High School.
2. **Build a Predictive Model**: Use machine learning models to predict which students are at risk of failing and identify contributing factors.
3. **Provide Recommendations**: Create a strategic action plan for school administrators to improve student outcomes.
4. **Visualize and Communicate**: Develop interactive dashboards to communicate findings effectively.

---

## 🛠️ Tools & Technologies
- **Python Libraries**: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `shap`, `matplotlib`, `seaborn`
- **Visualization**: `matplotlib`, `seaborn`, `SHAP`
- **Machine Learning**: `scikit-learn`, `xgboost`, `optuna`
- **Data Preprocessing**: `scikit-learn`, `pandas`


---

## 📂 Project Structure

The project is organized into the following directories and files:

```
project-directory/
│
├── README.md                   # Project documentation
├── LICENSE                     # Project license file
├── requirements.txt            # Dependencies used in the project
│
├── analysis/                   # Contains analysis and evaluation notebooks
│   ├── academic_fraud_analysis.ipynb  # Academic fraud analysis using anomaly detection
│   ├── analysis_walkthrough.ipynb     # Basic analysis of student scores
│   ├── health_impact_on_performance.ipynb  # Impact of health on academic performance
│   ├── survey_analysis.ipynb          # Analysis of survey data
│   └── survey_analysis.html           # Pandas profiler report for survey data
│
├── data/                       # Contains raw and processed data files
│   ├── students_bio_data.csv
│   ├── parents_data.csv
│   ├── teacher_data.csv
│   ├── academic_scores.csv
│   └── survey_student_dataset.csv
│
├── scripts/                    # Core data generation and analysis scripts
│   ├── academic_scores.py      # Script for generating academic scores
│   ├── students_data.py        # Script for generating student bio-data
│   ├── teachers_data.py        # Script for generating teacher data
│   ├── parents_data.py         # Script for generating parents data
│   └── survey_data.py          # Script for generating survey data
│
├── notebooks/                  # Jupyter notebooks for modeling and analysis
│   ├── model_0.ipynb           # First iteration of predictive modeling
│   ├── feature_engineering.ipynb # Feature selection and engineering
│   └── model_comparison.ipynb  # Compare different models and fine-tuning
│
├── main.py                     # Main script to run data generation pipeline
└── requirements.txt            # Dependencies file for the project
```

---

## 📋 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Kennedy87670/DataFestAfrica2024.git
   cd DataFestAfrica2024
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Data Generation Pipeline**:

   ```bash
   python scripts/main.py
   ```

---

## 🚀 Usage

1. **Generate Data**:
   Run the `main.py` file to generate synthetic data for students, teachers, parents, and academic records:

   ```bash
   python scripts/main.py
   ```

2. **Analyze Data**:
   Open the Jupyter notebooks under the `notebooks/` directory for analysis and modeling.

---

## 📄 File Descriptions

- **`data/`**: Contains the generated CSV files for students, parents, teachers, and academic scores.
- **`scripts/`**: Holds the scripts for data generation, feature engineering, and pre-processing.
- **`analysis/`**: Jupyter notebooks for exploratory data analysis, academic fraud analysis, and survey results.
- **`notebooks/`**: Jupyter notebooks for initial modeling and feature engineering.

---

## 📊 Results and Findings

1. **Identified Key Factors**:
   - Parental engagement, teacher qualifications, test_scores, and exam_scores are strong predictors of student success.
   
2. **Built Predictive Models**:
   - Implemented Logistic Regression, Decision Trees, and XGBoost with an accuracy of up to 100% for the `Pass/Fail` prediction.
   
3. **SHAP Analysis**:
   - Used SHAP values to interpret the contribution of features to model predictions, showing that `Study Hours`, `Teacher Experience`, and `Parental Involvement` have significant impacts.

---

## 🙏 Acknowledgments

- **DataFestAfrica Hackathon 2024** for providing a great platform and inspiration for this project.
- **Laurel High School** (fictional) for the problem context.
- **All contributors** for their help in building this project.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---


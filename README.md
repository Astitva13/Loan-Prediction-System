**📌 Project Overview**

Loan approval decisions depend on multiple applicant factors such as income, credit history, education, and property area.
This system uses historical loan data to train a classification model and provides predictions through a simple, user-friendly web app.

**🌐 Web Application (Flask)**

Built using Flask

Accepts user input through an HTML form

Sends data to a trained ML model

Displays loan approval result instantly

**Flow:**
User Input → Flask App → Trained ML Model → Prediction Result

**🔍 Dataset**

Public loan approval dataset (CSV)

**Key features:**

Gender, Marital Status, Education

Applicant & Co-applicant Income

Loan Amount & Term

Credit History

Property Area

Target Variable: Loan_Status

**⚙️ Machine Learning Workflow**

1.Data loading and exploration

2.Handling missing values

3.Exploratory Data Analysis (EDA)

4.Feature encoding

5.Train-test split

6.Model training and evaluation

7.Model serialization

8.Flask integration for prediction
**
🧠 Algorithms Used**

Support Vector Machine (SVM)

**📊 Model Evaluation**

Metric: Accuracy Score

Validation performed on unseen test data

**🛠️ Tech Stack**

Language: Python

ML Libraries: NumPy, Pandas, Scikit-learn

Visualization: Matplotlib, Seaborn

Web Framework: Flask

Frontend: HTML, CSS

IDE: Jupyter Notebook / VS Code
**
📁 Project Structure**
Loan-Prediction-System/
│
├── dataset/
│   └── train.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── Loan_Prediction.ipynb
├── model.pkl
├── requirements.txt
└── README.md
**
▶️ How to Run the Project**

1. Clone the repository

git clone <repo-link>


2. Install dependencies

pip install -r requirements.txt


3. Run the Flask app

python app.py


4. Open browser and go to

http://127.0.0.1:5000/

**🚀 Future Enhancements**

Add advanced models (Random Forest, XGBoost)

Improve UI design

Add input validation

Deploy on cloud platform

Add user authentication

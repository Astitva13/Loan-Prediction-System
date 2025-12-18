import pickle
from sklearn import svm

model = pickle.load(open('model/loan_model.pkl', 'rb'))


# Defining the translator layer for user friendly experience
gender_map = {'Male': 1, 'Female': 0}
married_map = {'Yes': 1, 'No': 0}
education_map = {'Graduate': 1, 'Not Graduate': 0}
self_employed_map = {'Yes': 1, 'No': 0}
property_area_map = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}

def predict_loan_status(user_input: dict):

    processed_input = [
        gender_map[user_input['gender']],
        married_map[user_input['married']],
        int(user_input['dependents']),
        education_map[user_input['education']],
        self_employed_map[user_input['self_employed']],
        float(user_input['applicant_income']),
        float(user_input['coapplicant_income']),
        float(user_input['loan_amount']),
        float(user_input['loan_term']),
        float(user_input['credit_history']),
        property_area_map[user_input['property_area']]
    ]

    prediction = model.predict([processed_input])

    return "Loan Approved" if prediction[0] == 1 else "Loan Rejected"
from flask import Flask, request, render_template
from predict import predict_loan_status

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = {
        'gender': request.form['gender'],
        'married': request.form['married'],
        'dependents': request.form['dependents'],
        'education': request.form['education'],
        'self_employed': request.form['self_employed'],
        'applicant_income': request.form['applicant_income'],
        'coapplicant_income': request.form['coapplicant_income'],
        'loan_amount': request.form['loan_amount'],
        'loan_term': request.form['loan_term'],
        'credit_history': request.form['credit_history'],
        'property_area': request.form['property_area']
    }

    result = predict_loan_status(user_input)

    return render_template('index.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
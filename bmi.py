from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    bmi = None
    message = None
    if request.method == "POST" and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = cal_bmi(weight, height)
        message = classify_bmi(bmi)
    return render_template('bmi_index.html', bmi=bmi, message=message)

def cal_bmi(weight, height):
    # Convert height to meters and calculate BMI
    return round(weight / ((height / 100) ** 2), 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "You are underweight. Eat more."
    elif 18.5 <= bmi < 24.9:
        return "You are normal. Stay the same."
    elif 25 <= bmi < 29.9:
        return "You are overweight. Eat less."
    else:
        return "You are obese. Consult a doctor."

app.run(port = 5001)
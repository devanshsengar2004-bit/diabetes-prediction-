from flask import Flask,render_template,request
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)
data = pd.read_csv("diabetes.csv")
x = data.drop("Outcome",axis=1)
y = data["Outcome"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    pregnancies = int(request.form["pregnancies"])
    glucose = int(request.form["glucose"])
    bloodpressure = int(request.form["bloodpressure"])
    bmi = float(request.form["bmi"])
    age = int(request.form["age"])

    values = np.array([[pregnancies,glucose,bloodpressure,0,0,bmi,0.5,age]])
    result = model.predict(values)

    if result[0] ==1:
        output = "aapko diabetes hai"
    else:
        output = "aapko diabetes nhi hai"
    return render_template("index.html", result=output)

if  __name__ == "__main__":
    app.run(debug=True)
    
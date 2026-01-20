from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import smtplib, os, re
from email.message import EmailMessage

app = Flask(__name__)

# ---------- EMAIL CONFIG ----------
EMAIL_ID = "yourgmail@gmail.com"
EMAIL_PASS = "your_16_character_app_password"

# ---------- TOPSIS FUNCTION ----------
def topsis(df, weights, impacts):
    data = df.iloc[:, 1:].astype(float)
    weights = np.array(weights) / sum(weights)

    norm = data / np.sqrt((data ** 2).sum())
    weighted = norm * weights

    ideal_best, ideal_worst = [], []
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    df["Topsis Score"] = score
    df["Rank"] = score.rank(ascending=False)

    return df

# ---------- EMAIL FUNCTION ----------
def send_email(file_path, user_email):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result File"
    msg["From"] = EMAIL_ID
    msg["To"] = user_email
    msg.set_content("Please find the attached TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ID, EMAIL_PASS)
        server.send_message(msg)

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    file = request.files["file"]
    weights = request.form["weights"].split(",")
    impacts = request.form["impacts"].split(",")
    email = request.form["email"]

    # validations
    if len(weights) != len(impacts):
        return "Error: Number of weights must equal number of impacts"

    if not all(i in ['+', '-'] for i in impacts):
        return "Error: Impacts must be + or -"

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Error: Invalid email address"

    weights = list(map(float, weights))
    df = pd.read_csv(file)

    result = topsis(df, weights, impacts)
    result.to_csv("result.csv", index=False)

    #send_email("result.csv", email)

    return "Result generated and emailed successfully!"

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)

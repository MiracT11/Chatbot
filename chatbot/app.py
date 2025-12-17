from flask import Flask, render_template, request
from excel_okuma import get_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        user_question = request.form["question"]
        answer = get_answer(user_question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    errors = []
    success = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        age = request.form.get("age", "").strip()

        if not name:
            errors.append("Name cannot be empty.")
        if "@" not in email:
            errors.append("Email must contain '@'.")
        if not age.isdigit():
            errors.append("Age must be numeric.")

        if not errors:
            success = f"Form valid! Welcome {name} (Age: {age})."
    return render_template("form.html", errors=errors, success=success)

if __name__ == "__main__":
    app.run(debug=True)

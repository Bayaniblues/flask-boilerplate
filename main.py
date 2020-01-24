from flask import Flask, render_template, request, Response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("component.html", title="website")


# example of list, please configure
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    option = request.form.get("option")
    if not name or not option:
        return "fail"
    # TODO
    return render_template("/basic_form.html")


if __name__ == "__main__":
    app.run()
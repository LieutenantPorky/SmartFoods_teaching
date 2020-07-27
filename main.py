from flask import Flask, render_template

app = Flask(__name__, static_folder="./templates", static_url_path="/templates")
app.debug=True

@app.route("/")
def homePage():
    print("User connected to the homepage")
    return render_template("template_1.html")


if __name__ == "__main__":
    app.run()

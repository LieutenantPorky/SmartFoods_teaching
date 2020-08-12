from flask import Flask, render_template, request, jsonify # Flask is a python module, so it needs to be imported at the start

# Quickly setup the environment - we're telling Flask that it should run as a server, as well as giving it the location
# of static files (files that need to be fetched separately), and telling it to enable debugging

app = Flask(__name__, static_folder="./templates", static_url_path="/templates")
app.debug=True

username = "bob"
currentBudget = 350.0

# Here we're actually telling Flask what to do when a user connects. The @app.route indicates what sub-url the user should go
# to in order for the function that follows to be called - for example, if we have a server address that's "smartfoods.com",
# and have
# @app.route("/fridge")
# def showFridge():
# ...
#
#
# Then showFridge is called whenever a user visits "smartfoods.com/fridge"
#
# In this particular case, we're just going to add the function at the root of the url
@app.route("/")
def homePage():
    #This will be printed to the console once a user connects
    print("User connected to the homepage")

    #This will return the html code that we've included in our template
    return render_template("homepage.html", user= username, budget=currentBudget)


@app.route("/budget", methods=["GET", "POST"])
def changeBudget():
    if request.method == "POST":
        global currentBudget
        newBudget = request.form.get("new_budget")
        print(newBudget)
        currentBudget = newBudget
        return jsonify({"new_budget":newBudget})

    return render_template("budget.html", user= username, budget=currentBudget)


# This statement is only true if the script is actually being launched separately, and not as a sub_process. This ensures we don't
# accidentally start the Flask server in a situation where it may be insecure

if __name__ == "__main__":
    app.run()

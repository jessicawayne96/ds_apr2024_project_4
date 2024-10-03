from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper



#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()
#################################################
# Flask Routes
#################################################

# HTML ROUTES
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/model")
def model():
    return render_template("ML.html")  # Ensure you have a corresponding model.html file

@app.route("/dashboard")
def dashboard():
    return render_template("tableau1.html")

@app.route("/battle")
def battle():
    return render_template("tableau2.html")  # Ensure you have a corresponding battle.html file

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")

@app.route("/findings")
def findings():
    return render_template("findings.html")

@app.route('/makePredictions', methods=['POST'])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    character = content["character"]
    strength = int(content["strength"])
    speed = int(content["speed"])
    intelligence = int(content["intelligence"])
    weaknesses = content["weaknesses"]
    specialAbilities = content["specialAbilities"]
   

    preds = modelHelper.makePredictions(character, strength, speed, intelligence, weaknesses, specialAbilities)
    return(jsonify({"ok": True, "prediction": str(preds)}))



@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)


@app.route("/")
@app.route("/index/")
@app.route("/<title>")
@app.route("/index/<title>")
def index(title=''):
    return render_template(
        "index.html",
        title=title
        )

@app.route("/training/<prof>")
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        prof_type = "engineering"
    else:
        prof_type = "ology"
    
    return render_template(
        "training.html",
        title="training",
        image_path=url_for("static", filename="images/MARS-2-2.png"),
        prof=prof_type
    )

@app.route("/list_prof/<sp_style>")
def list_prof(sp_style):
    list_prof = [
        "пилот",
        "строитель",
        "врач",
    ]
    
    if sp_style not in {"ol", "ul"}:
        sp_style = "None"
    
    return render_template(
        "list_prof.html",
        sp_style=sp_style,
        list_prof=list_prof
    )

@app.route("/auto_answer")
@app.route("/answer")
def answer():
    user_data = {
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": " Всегда мечтал застрять на Марсе!",
        "ready": True,
    }
    
    return render_template(
        "auto_answer.html",
        title="Анкета",
        style_path=url_for("static", filename="css/style_answer.css"),
        user_data=user_data
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
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
        image_path=url_for("static", filename="MARS-2-2.png"),
        prof=prof_type
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

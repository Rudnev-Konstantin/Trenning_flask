from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def std():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route("/promotion")
def promotion():
    text = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]
    return '<br>'.join(text)

@app.route('/image_mars')
def image_mars():
    data = [
        "<h1>Жди нас, Марс!</h1>",
        f"""
<img 
src="{url_for("static", filename="images/MARS.png")}"
alt="здесь должна была быть картинка, но не нашлась"
>
        """,
        "<p>Вот она какая, красная планета</p>"
    ]
    return ''.join(data)

@app.route('/promotion_image')
def promotion_image():
    data = [
        """
<link
rel="stylesheet" 
href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I"
crossorigin="anonymous"
>
        """,
        f'<link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">',
        "<h1>Жди нас, Марс!</h1>",
        f"""
<img 
src="{url_for("static", filename="images/MARS.png")}"
alt="здесь должна была быть картинка, но не нашлась"
>
        """,
        '<div>Человечество вырастет из дерева.</div>',
        '<div>Человечество мала одна планета.</div>',
        '<div>Мы сделаем обитаемыми безжизненные пока планеты</div>',
        '<div>И начнём с Марса!</div>',
        '<div>Присоединяйся!</div>'
    ]
    return ''.join(data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

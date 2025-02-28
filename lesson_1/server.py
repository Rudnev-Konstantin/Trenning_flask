from flask import Flask
from flask import url_for
from flask import request

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

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br/>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Среднее-Профессиональное</option>
                                          <option>Высшие</option>
                                        </select>
                                     </div>
                                    <label class="educationSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                        <br/>
                                        
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">пилот</label>
                                        <br/>
                                        
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">строитель</label>
                                        <br/>
                                        
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">экзобиолог</label>
                                        <br/>
                                        
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">врач</label>
                                        <br/>
                                        
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Другие...</label>
                                        <br/>
                                    </div>
                                    <div class="form-group">
                                        <label for="educationSelect">Какие у Вас есть профессии?</label>
                                        <select class="form-group form-check" id="educationSelect" name="education">
                                          <option>инженер-исследователь</option>
                                          <option>пилот</option>
                                          <option>строитель</option>
                                          <option>экзобиолог</option>
                                          <option>врач</option>
                                          <option>инженер по терраформированию</option>
                                          <option>климатолог</option>
                                          <option>специалист по радиационной защите</option>
                                          <option>астрогеолог</option>
                                          <option>гляциолог</option>
                                          <option>инженер жизнеобеспечения</option>
                                          <option>метеоролог</option>
                                          <option>оператор марсохода</option>
                                          <option>киберинженер</option>
                                          <option>штурман</option>
                                          <option>пилот дронов</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите участвовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

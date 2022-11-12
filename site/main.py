from flask import Flask, render_template, url_for, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

site = Flask(__name__)
site.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
site.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(site)


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)     # primary_key=True робить поля унікальними(щоб не повторювалось)
    name_dish = db.Column(db.String(10), nullable=False)    # nullable=False не можна щоб поле було пустим
    type_dish = db.Column(db.String(10), nullable=False)
    the_ingredients = db.Column(db.String(100), nullable=False)
    steps_dish = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Recipes %r>' % self.id


@site.route('/')
@site.route('/home')
def index():
    return render_template("index.html")


@site.route('/posts')
def posts():
    recipesss = Recipes.query.order_by(Recipes.date.desc()).all() #recipesss = Recipes.query.order_by(Recipes.date.desc()).all()
    return render_template("post.html", recipesss=recipesss)


@site.route('/addrecipes', methods=['POST', 'GET'])
def add_recipes():
    if request.method == 'POST':
        name_dish= request.form['name_dish']
        type_dish = request.form['type_dish']
        the_ingredients = request.form['the_ingredients']
        steps_dish = request.form['steps_dish']

        recipe = Recipes(name_dish=name_dish, type_dish=type_dish, the_ingredients=the_ingredients, steps_dish=steps_dish)
        try:
            db.session.add(recipe)
            db.session.commit()
            return redirect('/')
        except:
            return "Щось пішло нетак"
    else:
        return render_template("addrecipes.html")


@site.route('/main_course')
def main_course():
    return render_template("underdevelopment.html")


@site.route('/soup')
def soup():
    return render_template("underdevelopment.html")


@site.route('/baking')
def baking():
    return render_template("underdevelopment.html")


@site.route('/desserts')
def desserts():
    return render_template("underdevelopment.html")


@site.route('/drinks')
def drinks():
    return render_template("underdevelopment.html")


@site.route('/appetizer')
def appetizer():
    return render_template("underdevelopment.html")


@site.route('/sign_in')
def sign_in():
    return render_template("sign.html")



if __name__ == "__main__":
    site.run(debug=True)

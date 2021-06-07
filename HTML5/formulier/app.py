from datetime import datetime
from flask import Flask, render_template, url_for, request, flash
import sqlite3
from sqlite3 import Error as sqliteError
import uuid

FMT = "%y-%m-%d %H:%M:%S"

random_key = uuid.uuid4().hex
app = Flask(__name__)
app.secret_key = random_key


class CompetitionForm():
    def __init__(self, form_dict):

        if isinstance(form_dict, dict):
            self.data = form_dict
        else:
            raise TypeError(f'form_dict must be of instance `dict` not {type(form_dict)}')

        try:
            self.name = form_dict['name']
            self.first_name = form_dict['first_name']
            self.email = form_dict['email']
            self.recipe_title = form_dict['title']
            self.recipe_type = form_dict['type']
            self.recipe_content = form_dict['content']
        except KeyError as err:
            raise KeyError(err)

    def __str__(self):
        return f'''
        Naam: {self.first_name} {self.name}
        Email: {self.email}
        ==================================
        Recipe: {self.recipe_title}
        Type: {self.recipe_type}
        Ingrediënten: {self.recipe_content}
        '''

    def save_submission(self):
        try:
            conn = sqlite3.connect('competition_submissions.db')
            conn.execute('''INSERT INTO Submissions
            (name, first_name, email, recipe_title, recipe_type, recipe_content)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (self.name, self.first_name, self.email, self.recipe_title, self.recipe_type, self.recipe_content))
        except sqliteError as err:
            print(f'[{datetime.utcnow().strftime(FMT)}]\t Unexpected sqlite3 error detected:\n{err}')
            flash('Something went wrong, submission was not stored, please try again later!')
            conn.rollback()
        else:
            conn.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/competition_form', methods=['POST'])
def competition_form():
    current_form = CompetitionForm(request.form)
    current_form.save_submission()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

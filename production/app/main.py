from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from project import process_the_info
from forms import MainForm

bootstrap = Bootstrap()

app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'

bootstrap.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    if form.validate_on_submit():
        c_i = form.number_of_cities.data
        c_o = form.number_of_colors.data
        n_r = form.number_of_relations.data
        t_r = form.relations.data
        results = process_the_info(c_i, c_o, n_r, t_r)
        return redirect(url_for('result', results=results))

    return render_template('index.html', form=form)


@app.route('/result/<results>', methods=['GET'])
def result(results):
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run()

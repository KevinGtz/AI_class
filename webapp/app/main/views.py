from flask import render_template, redirect, url_for, flash
from . import main
from .forms import MainForm
from ..logic import process_the_info

@main.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    if form.validate_on_submit():
        c_i = form.number_of_cities.data
        c_o = form.number_of_colors.data
        n_r = form.number_of_relations.data
        t_r = form.relations.data
        flash('ok')
        results = process_the_info(c_i, c_o, n_r, t_r)
        return redirect(url_for('.results', results=results))

    return render_template('index.html', form=form)

@main.route('/results/<results>', methods=['GET'])
def results(*args):

    return render_template('results.html', results=results)

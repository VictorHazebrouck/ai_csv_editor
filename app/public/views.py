from flask import Blueprint, render_template


index = Blueprint('index', __name__, template_folder='templates')

@index.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

public = Blueprint('public', __name__, template_folder='templates', static_folder='static', static_url_path='/static')

@public.route('/main', methods=['GET'])
def get_public():
    return render_template('main.html')

@public.route('/column-temp', methods=['GET'])
def get_column_temp():
    return render_template('column-temp.html')
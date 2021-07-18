import os

from flask import Flask, redirect, render_template, request, send_from_directory

app = Flask(__name__)


def get_theme():
    return request.cookies.get('theme') or 'dark'


@app.before_request
def before_request():
    if request.path != '/' and request.path.endswith('/'):  # remove trailing slash
        return redirect(request.path.removesuffix('/'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(_):
    return render_template('error.html', theme=get_theme(), error_code=404,
                           error_message='Тут ничего нет. Или я хочу чтоб вы так думали.')


@app.errorhandler(500)
def internal_server_error(_):
    return render_template('error.html', theme=get_theme(), error_code=500,
                           error_message='Я накосячил. Но виноваты всё равно вы.')


@app.route('/')
def index():
    return render_template('index.html', theme=get_theme())


@app.route('/nudes')
def nudes():
    return render_template('nudes.html', theme=get_theme())


@app.route('/error')
def error():
    pass  # this will cause 500 error (also some traceback shit in logs but who cares)


if __name__ == '__main__':
    app.run()

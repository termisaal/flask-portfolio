import os

from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


def get_theme():
    return request.cookies.get('theme') or 'dark'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('base.html', theme=get_theme())


if __name__ == '__main__':
    app.run()

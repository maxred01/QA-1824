""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """

    return render_template('welcome.html')


@app.route("/error")
def error():
    """Эта функция запуская и отвечает за процесс возврата результата test_error.html."""
    return render_template('test_error.html')


@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


@app.route("/run_ui")
def run_ui():
    """ Эта функция запуская и отвечает за тесты страницы /example. """

    cmd = ["./scriptsh/run_aut_lk.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)

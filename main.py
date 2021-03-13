from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    abort,
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html",title='Japu Salon')


if __name__ == "__main__":
    app.run(debug=True)

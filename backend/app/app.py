from flask import Flask, request, render_template


app = Flask(__name__, template_folder='../../frontend/templates')


@app.route('/')
def landing_page():
    return render_template("index.html"), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

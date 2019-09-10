from flask import Flask
import face_detect_cv3

app = Flask(__name__)


@app.route("/")
def home():
    return face_detect_cv3


if __name__ == "__main__":
    app.run(debug=True)


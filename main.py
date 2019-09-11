from flask import Flask

import downloader
import face_detect_cv3

app = Flask(__name__)


@app.route("/")
def home():
    return "D.id interview test"


@app.route("/detectfaces/url=<path:url>")
def face_detect(url):
    image_path = downloader.download_img(url)
    faces_count = face_detect_cv3.face_detect(image_path)
    return faces_count


if __name__ == "__main__":
    app.run(debug=True)


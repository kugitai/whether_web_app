from flask import Flask,render_template
import whether

app = Flask(__name__)

@app.route("/")
def main_page():
    data = {
        'p_time': whether.publicTimeFormatted(),
        'title': whether.title(),
        'des_p_time': whether.description().publicTimeFormatted(),
        'headlineText': whether.description().headlineText(),
        'bodyText': whether.description().bodyText()
    }
    return render_template("index.html", **data)

if __name__ == '__main__':
    app.run(debug=True)
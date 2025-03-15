# filepath: d:\VS Code\js-study\app.py
from flask import Flask, render_template_string
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Terraria</title>
        <script>
            function onYes() {
                alert("Ні дякую");
            }
            function onNo() {
                window.open("https://youtu.be/3tKubQSYd1o?si=C0JUoxG2oSn4fII-&t=20", "_blank");
            }
        </script>
    </head>
    <body>
        <h1>Чи хочеш грати Терарію?</h1>
        <button onclick="onYes()">Так</button>
        <button onclick="onNo()">Ні</button>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
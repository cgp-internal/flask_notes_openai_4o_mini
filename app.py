from flask import Flask
from routes.note import note_blueprint

app = Flask(__name__)
app.register_blueprint(note_blueprint)

def run_app():
    app.run(debug=True)

if __name__ == "__main__":
    run_app()
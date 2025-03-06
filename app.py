from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"API_KEY={os.getenv('API_KEY')}"

if __name__ == "__main__":
    app.run()

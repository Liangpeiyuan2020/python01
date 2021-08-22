import os

from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')

def hello_world():
    try:
        import demo
        return jsonify(demo.main())
    except Exception as e:
        pass
    return jsonify(300)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
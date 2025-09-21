from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello():
    return jsonify({"msg": "hello", "app": "webapppipeline-demo"})

@app.route ('/items')
def items():
    q = request.args.get('q', '')
    # returns user input unsanitized
    return jsonify({"count": 2, "items": ["jablko", "banan"], "q": q})

@app.route('/calc')
def calc():
    expr = request.args.get('expr', '')
    # using eval on user input
    try:
        result = eval(expr)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"expr": expr, "result": result})

@app.route('/secret')
def secret():
    # exposing a hardcoded secret from config 
    key = app.config.get('API_KEY', '')
    return jsonify({"secret_preview": (key[:8] + '...') if key else None})

if __name__ == '__main__':
    # leaving debug as True
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request, Response
from flask_cors import CORS
from gen_problem import gen_problem
import json

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def my_api():
    data = request.get_json()
    result = gen_problem(data["content"])
    response = Response(response=json.dumps(result, ensure_ascii=False),
                        status=200,
                        mimetype="application/json")
    return response

if __name__ == '__main__':
    app.run(debug=True)
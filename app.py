from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/model',methods=['POST'])
def hello_world():
    # return jsonify(request.value)
    return(request.get_json())
    # return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
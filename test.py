from flask import Flask,request,jsonify

app = Flask(__name__)



@app.route('/api/hello',methods=['GET'])
def hello_word():
    return ""

@app.route('/api/hello2',methods=['POST'])
def hello_return_name():
    data = request.get_json()
    name = data.get('name')
    header_message = request.headers.get('Glock')
    param_name = request.args.get('shite')
    response_message =  f"hello {name} and  {header_message} and {param_name}!"

    return jsonify({"message":response_message})

if __name__=='__main__':
    app.run(host='127.0.0.1',port=4444)
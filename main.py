import google.generativeai as palm

from flask import Flask, request, jsonify, make_response
 
app = Flask(__name__)

palm.configure(api_key='')

@app.route('/chat', methods=['POST', 'OPTIONS'])
def call_palm():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    data = request.json
    prompt = data.get("prompt")
    prompt = "Answer the question as Lord Krishna\n" + prompt
    
    response = jsonify({"response": palm.chat(messages=prompt).last})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()


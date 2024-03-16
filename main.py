from flask import Flask, request, jsonify
from flask_cors import CORS

import json

import requests
API_URL = "https://xevhza5rhd1jhkq8.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json" 
}

app = Flask(__name__)
cors = CORS(app)

def remove_slash(text):
    new_str = ""
    for s in text:
        if s is not "/":
            new_str += s
    
    return new_str
            

def query_to_chatbot(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return json.loads(response.content)

def parse_response(response):
	str_parsed = str(response).split("\\\\n")
	return [ s for s in str_parsed[2:-3]]

@app.route("/docus", methods=["POST"])
def talk_to_docus():
    data = request.get_json()
    data = jsonify(data)

    print(data.data.decode("utf-8"))
    output = query_to_chatbot({
        "inputs": data.data.decode("utf-8"),
        "parameters": { "model": "medalpaca/medalpaca-7b",
                        "tokenizer": "medalpaca/medalpaca-7b",
                        "max_new_tokens": 70,
                        "temperature": 0.1,
                        "top_k": 1
                    }})
    
    # print(output["generated_text"])
    # o = parse_response(output)
    print(output)
    # print(remove_slash(o[0]))
    return jsonify(isError= False, message= "Success", statusCode= 200, data=output[0]["generated_text"]), 200 
    # return jsonify(isError= False, message= "Success", statusCode= 200, data="Can ou work please"), 200 


if __name__ == "__main__":
     app.run()
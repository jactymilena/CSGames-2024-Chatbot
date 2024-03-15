import requests
import json

API_URL = "https://xevhza5rhd1jhkq8.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json" 
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	# response = requests.get(API_URL)
	# return response.content
	return response.content


output = query({
	"inputs": "Can I ask you a question?",
	"parameters": {"model": "medalpaca/medalpaca-7b"}
})

# test = json.loads(output)

print(output)
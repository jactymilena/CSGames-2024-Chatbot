import requests

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

def parse_response(response):
	str_parsed = str(output).split("\\n")

	return [ s for s in str_parsed[2:-3]]

# output = query({
# 	"inputs": "I'm experiencing increased thirst, frequent urination, and unexplained weight loss..",
# 	#"inputs": "I am vomitting",
# 	"parameters": {"model": "medalpaca/medalpaca-7b"
# 				   #"tokenizer": "medalpaca/medalpaca-7b"
# 				   #"top_k": 1,
# 				   #"top_p": 0.95,
# 				   #"temperature": 0.5,
# 				   #"max_new_tokens": 150,
# 				   #"min_new_tokens": 2,
# 				   }})
# coughing, sneezing, wheezing, fever and decrease in appetite.
output = query({
	"inputs": "You are my medical assistant. My symptoms are : runny nose, fever, wheezing, decrease in appetite and sneezing. What is my diagnostic?",
	"parameters": {"model": "medalpaca/medalpaca-7b",
				   "tokenizer": "medalpaca/medalpaca-7b",
				   "max_new_tokens": 70,
				   "temperature": 0.1,
				   "top_k": 1}
})


print(output)
sentences = parse_response(output)

# str_parsed = str(output).split("\\\\n")
# for s in str_parsed[2:]:
# 	sentences.append(s)

print(sentences)


import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content 
    
    def load_json(self):
        json_content=json.loads(req.get_response_body())
        return json_content

# Example usage:
req = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(req.load_json())

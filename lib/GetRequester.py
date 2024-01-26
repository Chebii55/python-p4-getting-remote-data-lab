import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content 
    
    def load_json(self):
        the_list = []
        the_response = json.loads(self.get_response_body())
        for list in the_response:
            the_list.append(list)

        return the_list

# Example usage:
req = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(req.load_json())

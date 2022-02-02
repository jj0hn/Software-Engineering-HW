import requests

NYT_KEY = "Y2LeumHjKp5AR6TbFmLfHFVxgL7HMYaq"
BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

query_params = {
        "api_key": NYT_KEY,
        "q": "coronavirus",
}

response = requests.get(
    BASE_URL,
    params=query_params,
)

print(response.json())
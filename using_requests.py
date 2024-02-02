import requests

try:
    response = requests.get('https://www.python.org', verify=False)
    if response.status_code == requests.codes.OK:
        web_page = response.text   #  response.content is raw (encoded) response data
        print(web_page[:500])
        print("...")
        print(web_page[-500:])
except requests.RequestException as err:
    print(err)
import requests
import json

"""Task_4.1"""
# Make an HTTP read request, save the result to a file
response_get = requests.get('https://jsonplaceholder.typicode.com/posts/3')
data_json = response_get.json()

with open('../requests/response.json', 'w') as file_json:
    json.dump(data_json, file_json, indent=4)

print(f'{data_json = }')
print(f'{response_get.ok = }')


"""Task_4.2"""
# Read the information from the file and make an HTTP request to save
with open('../requests/response.json', 'r') as read_response_json:
    data_response_json = json.load(read_response_json)

status_put = requests.put('https://jsonplaceholder.typicode.com/posts/3', data=data_response_json)

print(f'{data_response_json = }')
print(f'{status_put.ok = }')


"""Task_5"""
# Download any picture from the Internet, save it
response_picture = requests.get('https://cdn.dopl3r.com//media/memes_files/the-best-way-to-learn-a-language-is-to'
                                '-speak-to-natives-the-guy-learning-python-il-vLqyN.jpg')

with open('../requests/img.jpg', 'wb') as picture:
    picture.write(response_picture.content)

import requests
import json
import base64
from flask import Flask, render_template_string

app = Flask(__name__)

# Replace 'your_api_key' with your actual API key
api_key = '_____'
api_url = 'https://insect.kindwise.com/api/v1/'

def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

def identify_insect(image_path):
    endpoint = 'identification'
    url = f'{api_url}{endpoint}'

    headers = {
        'Api-Key': api_key,
        'Content-Type': 'application/json',
    }

    image_base64 = encode_image(image_path)

    payload = {
        'images': [image_base64],
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return {'error': f"Error: {response.status_code}"}

@app.route('/')
def index():
    # Example usage:
    image_path = '/Users/mayank/Desktop/TEST.jpeg'
    identification_result = identify_insect(image_path)

    if 'error' in identification_result:
        return f"Error retrieving identification result: {identification_result['error']}"

    # Render an HTML page with the formatted JSON
    return render_template_string('<pre>{{ result }}</pre>', result=json.dumps(identification_result, indent=4))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

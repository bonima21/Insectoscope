import os  # Add this line to import the os module
import requests
import json
import base64
from flask import Flask, render_template

app = Flask(__name__)

# Replace 'your_api_key' with your actual API key
api_key = 'oNscggVRlsj7FPz2OYvfmWKUpYXLcjII0MBBScXM2xu4uZcx8s'
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
    image_path = 'C:\\Users\\vanla\\OneDrive\\Desktop\\ladybug.jpeg'
    identification_result = identify_insect(image_path)

    if 'error' in identification_result:
        return f"Error retrieving identification result: {identification_result['error']}"

    # Get the full path to the 'result.html' template in the same directory as this script
    template_path = os.path.join(os.path.dirname(__file__), 'result.html')

    # Render the 'result.html' template with the identification result
    return render_template(template_path, classification=identification_result.get("result", {}).get("classification", {}))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

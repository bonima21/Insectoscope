import os
import requests
import base64
 
# Retrieve your API key from the environment variable
api_key = os.environ.get("INSECT_ID_API_KEY")
 
if api_key is None:
    print("API key not found. Please set the INSECT_ID_API_KEY environment variable.")
else:
    def identify_insect(api_key, images, latitude=None, longitude=None, similar_images=False, custom_id=None, datetime=None):
        url = "https://insect.kindwise.com/api/v1/identification"
        headers = {
            "Api-Key": api_key,
           "Content-Type": "application/json"
        }
 
        # Encode images as base64
        encoded_images = [base64.b64encode(open(image, 'rb').read()).decode('utf-8') for image in images]
 
        data = {
            "images": encoded_images,
            "latitude": latitude,
            "longitude": longitude,
            "similar_images": similar_images,
            "custom_id": custom_id,
            "datetime": datetime
        }
 
        response = requests.post(url, headers=headers, json=data)
        return response.json()
 
    # Replace with your actual image file paths
    image_paths = ["path/to/image1.jpg", "path/to/image2.jpg"]
 
    # Make the identification request
    identification_result = identify_insect(api_key, image_paths)
 
    # Display the identification result
    print("Identification Result:")
    print(identification_result)
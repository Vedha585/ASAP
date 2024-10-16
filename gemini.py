import requests

# Replace with your actual API key
API_KEY = 'AIzaSyAi1jAyprJ-yyjKzBFgQXoGkfORQ1avvvg'

# Function to send a request and get the response text
def get_gemini_response(prompt):
    
    # Define the headers with content type
    headers = {
        'Content-Type': 'application/json'
    }

    # Construct the data with the given prompt
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    # Correct API endpoint with the API key included in the URL
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'

    try:
        # Send a POST request
        response = requests.post(url, headers=headers, json=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            response_json = response.json()
            
            # Extract the generated text from the response
            if 'candidates' in response_json:
                for candidate in response_json['candidates']:
                    # Extract the first part of the content text
                    text = candidate.get('content', {}).get('parts', [{}])[0].get('text', '')
                    return text
            return "No generated text found in the response."
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage:
prompt = "Explain the concept of neural networks."
# Call the function and print the result
response_text = get_gemini_response(prompt)
print("Generated Text:", response_text)

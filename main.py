import requests
from bs4 import BeautifulSoup

# Function to extract elements with a specific class attribute
def extract_elements_with_class(url, target_class):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all elements with the specified class attribute
            elements = soup.find_all(class_=target_class)
            
            # Extract the text from the found elements
            extracted_text = [element.text.strip() for element in elements]
            
            return extracted_text
        else:
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Input URL and target class from the user
url = input("Enter the URL of the website: ")
target_class = input("Enter the target class attribute: ")

# Call the function to extract elements with the specified class
extracted_elements = extract_elements_with_class(url, target_class)

# Display the extracted text
if extracted_elements:
    print(f"Text from elements with class '{target_class}':")
    for text in extracted_elements:
        print(text)
else:
    print("Failed to retrieve data from the website.")

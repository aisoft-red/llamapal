import requests
from PIL import Image
import numpy as np
import ollama

# Ollama local server configuration
OLLAMA_API_URL = "http://localhost:11434/api"

def generate_commentary(frame):
    """
    Sends a video frame to the Ollama API for commentary generation.

    Args:
        frame: The video frame (numpy array).

    Returns:
        commentary (str): Generated commentary for the frame.
    """
    # Convert the frame to a format accepted by Ollama
    frame_image = Image.fromarray(frame)
    frame_image.save("frame.jpg")  # Save the frame for debugging

    # Prepare the payload for Ollama API
    payload = {
        "model": "llama3.2-vision",  # Ensure this matches the exact model name in Ollama
        "prompt": "Describe this sports activity in the frame."
    }
    response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['frame.jpg']
    }]
)

    # Send the request to the Ollama API
    #response = requests.post(OLLAMA_API_URL, json=payload)

    # Check if the request was successful
    print(response)
    return response


# Entry point for testing the function
if __name__ == "__main__":
    # Mocking a video frame for demonstration (replace with an actual frame in practice)
    dummy_frame = np.zeros((224, 224, 3), dtype=np.uint8)  # A blank RGB frame

    try:
        commentary = generate_commentary(dummy_frame)
        print("Generated commentary:", commentary)
    except Exception as e:
        print(f"Error: {e}")

from PIL import Image
import numpy as np
import ollama
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os
from encode_image import encode_image

OLLAMA_API_URL = "http://localhost:11434/api"

def generate_commentary(frame, use_groq=False):
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

    # Send the request to the Ollama API
    # Append the all_commentary as a string

    content = (
        "Give a 20 word running sports commentary for this image"
    )
    image_filename = 'frame.jpg'

    if use_groq:
        api_key = os.environ.get("GROQ_API_KEY")
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": content
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encode_image(image_filename)}"
                        }
                    }
                ]
            }
        ]
        response = Groq(api_key=api_key).chat.completions.create(
            model='llama-3.2-11b-vision-preview',
            messages=messages
        )
        current_commentary = response.choices[0].message.content
    else:
        current_commentary = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': content,
                'images': [image_filename]
            }]
        ).message.content

    return current_commentary

# Entry point for testing the function
if __name__ == "__main__":
    # Mocking a video frame for demonstration (replace with an actual frame in practice)
    dummy_frame = np.zeros((224, 224, 3), dtype=np.uint8)  # A blank RGB frame

    try:
        commentary = generate_commentary(dummy_frame)
        print("Generated commentary:", commentary)
    except Exception as e:
        print(f"Error: {e}")

import io

from google import genai
from google.genai import types
import os
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get api key from env
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Set prompt
prompt = "Hyperrealistic close-up of a majestic lion with a flowing mane, in an African savanna at sunrise."

for model_info in client.models.list():
        print(model_info.name)

try:
    response = client.models.generate_content(
        model="imagen-3.0-generate-002",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE']
        )
    )

    if response.candidates and response.candidates[0].content.parts:
        for i, part in enumerate(response.candidates[0].content.parts):
            if part.inline_data:
                image_bytes = part.inline_data.data
                image_mime_type = part.inline_data.mime_type

                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    file_extension = image_mime_type.split('/')[-1]
                    image_filename = f"generate_image_{i}.{file_extension}"
                    image.save(image_filename)
                except Exception as e:
                    print(f"Error processing image data: {e}")
            elif part.text:
                print(f"Text part: {part.text}")
    else:
        print("N image or content found in the response.")

except Exception as e:
    print(f"An error occurred during image generation: {e}")

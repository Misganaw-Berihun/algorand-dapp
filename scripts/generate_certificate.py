import os
import requests 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

VARIABLE_KEY=os.environ.get("OPENAI_KEY")
client = OpenAI(
  api_key=VARIABLE_KEY
)

prompt = """ 
          Create a simple certificate template exclusively crafted for trainees at 10 Academy. This certificate will be presented to individuals who successfully complete the challenging weekly task'
          The certificate design must incorporate the following elements:
          The top left corner should showcase the official logo of the company.
          Adjacent to the logo, include the text '10 Academy.'.
          Below the logo and '10 Academy,' left-justify the 'Issuing Date.'
          On the same line, right-justify the 'Certificate ID.'.
          Boldly state 'Awarded To:' below the 'Issuing Date' and 'Certificate ID.'.
          Display the recipient's bolded 'FULL NAME'  directly beneath 'Awarded To,' aligning it to the center.
          Add the line 'FOR SUCCESSFULLY COMPLETING THE WEB-3 WEEKLY CHALLENGE' on a separate line to the recipient's name.
          On the last line, right-justify the signature and name of the CEO of the company.
          The background color of the image should be white with no images for a clean and professional appearance.
          Ensure readability of the text by selecting appropriate font styles and sizes.
          Allow for ample space between elements to maintain a polished and organized layout.
          The image should showcase a single certificate, extending to fill the entire space.          
          Please use this components only. use the words perfectly like in the given and put 
          the compoinents in the given order
        """

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="hd",
  n=1,
)

image_url = response.data[0].url

image_data = requests.get(image_url).content
with open("certificate.png", "wb") as f:
  f.write(image_data)

print("Image saved successfully.")
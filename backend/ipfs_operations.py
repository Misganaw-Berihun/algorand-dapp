import os
from datetime import datetime
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from dotenv import load_dotenv

load_dotenv()

def pin_to_ipfs(name):
    jwt_key = os.environ.get("jwt")
    jwt = f'Bearer {jwt_key}'
    date = datetime.now()
    output_path = f"../images/{name}_certificate.jpg"
    ec.generate_certificate(name, date, output_path, "CTF123494u5664098")
    src = f"../images/{name}_certificate.jpg"

    multipart_data = MultipartEncoder(
        fields={
            'file': (f'{name}.png', open(src, 'rb'), 'image/png'),
            'pinataMetadata': json.dumps({'name': f'{name}'}),
            'pinataOptions': json.dumps({'cidVersion': 0})
        }
    )

    headers = {
        'Content-Type': multipart_data.content_type,
        'Authorization': jwt
    }

    try:
        response = requests.post(url, data=multipart_data, headers=headers)
        return response.json()["IpfsHash"]
    except Exception as e:
        print(e)
        return None

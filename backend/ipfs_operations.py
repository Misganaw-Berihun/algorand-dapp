import os,sys
from datetime import datetime
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from dotenv import load_dotenv

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from scripts.edit_certificate import generate_certificate

load_dotenv()

def pin_to_ipfs(name):
    jwt_key = os.environ.get("jwt")
    jwt = f'Bearer {jwt_key}'
    print(jwt_key[-10:])
    date = datetime.now()
    output_path = f"../images/op_certificate.jpg"
    generate_certificate(name, date, output_path, "CTF123494U5664098")

    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    src = f"../images/op_certificate.jpg"

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
        print("JSON", response.json())
        return response.json()["IpfsHash"]
    except Exception as e:
        print(e)
        return None

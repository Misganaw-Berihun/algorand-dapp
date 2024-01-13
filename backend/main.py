from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
from ipfs_operations import pin_to_ipfs
from algorand_operations import create_asset
from email_operations import send_email
import os

app = FastAPI()

class Trainee(BaseModel):
    name: str
    email: EmailStr

trainees_db = []

@app.post("/create_trainee")
def issue_nft(trainee: Trainee):
    trainees_db.append(trainee)

    ipfsHash = pin_to_ipfs(trainee.name)
    asset_url = f"https://gateway.pinata.cloud/ipfs/{ipfsHash}"
    asset_id = create_asset(acct.get_keys("tutor"), asset_url)
    
    send_email(trainee.email, asset_id, trainee.name)
    return trainee

@app.post("/opt_in")
def opt_in_to_asset_endpoint(trainee: Trainee):
    try:
        # Assuming trainee provides their email and asset_id in the request
        opt_in_to_asset(trainee.email, trainee.asset_id)
    except HTTPException as e:
        return e
    return {"message": "Opt-in successful!"}
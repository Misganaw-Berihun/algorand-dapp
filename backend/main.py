from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
from ipfs_operations import pin_to_ipfs
from algorand_operations import create_asset, opt_in_asset, transfer_asset, freeze_asset
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
        opt_in_asset(trainee.email, trainee.asset_id, acct.get_keys("trainee_1"))
    except HTTPException as e:
        return e
    return {"message": "Opt-in successful!"}

@app.post("/transfer_asset")
def transfer_asset_endpoint(trainee: Trainee, recipient_address: str):
    try:
        transfer_asset(acct.get_keys("tutor"), acct.get_keys("trainee_1"), created_asset)
        freeze_asset(acct.get_keys("tutor"), acct.get_keys("trainee_1"), created_asset)
    except HTTPException as e:
        return e
    return {"message": "Asset transfer successful!"}
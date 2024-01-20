from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from ipfs_operations import pin_to_ipfs
from algorand_operations import create_asset, opt_in_asset, transfer_asset, freeze_asset
from send_email import send_email
from fastapi.middleware.cors import CORSMiddleware
import os,sys 

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from scripts.account_info import get_keys


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class Trainee(BaseModel):
    name: str
    email: EmailStr

class OptInTrainee(Trainee):
    asset_id: str
    state: str = "created"

class TransferAsset(Trainee):
    reciever_address: str = get_keys("trainee_1")["address"]

# asset_id = ''
trainees_db = []
opt_in_list = []
asset_id = ''

@app.post("/create_trainee")
def issue_nft(trainee: Trainee):
    trainees_db.append(trainee)
    print(*trainees_db)
    ipfsHash = pin_to_ipfs(trainee.name)
    asset_url = f"https://gateway.pinata.cloud/ipfs/{ipfsHash}"
    print("ASSET_URL",asset_url)
    asset_id = create_asset(get_keys("tutor"), asset_url)
    
    send_email(trainee.email, asset_id, trainee.name)
    return trainee

@app.post("/opt_in")
def opt_in_to_asset_endpoint(trainee: OptInTrainee):
    try:
        opt_in_asset(trainee.email, trainee.asset_id, get_keys("trainee_1"))
        opt_in_list.append(trainee)
        asset_id = trainee.asset_id
    except HTTPException as e:
        return e
    return {"message": "Opt-in successful!"}

@app.post("/transfer_asset")
def transfer_asset_endpoint(data: TransferAsset):
    nonlocal asset_id
    try:
        print("Asset ID:", asset_id)
        transfer_asset(get_keys("tutor"), get_keys("trainee_1"), asset_id)
        freeze_asset(get_keys("tutor"), get_keys("trainee_1"), asset_id)
        for index, t in enumerate(opt_in_list):
            if t.email == data.email:
                opt_in_list[index].state = "approved"
    except HTTPException as e:
        return e
    return {"message": "Asset transfer successful!"}

@app.get("/opt_in_list", response_model=List[OptInTrainee])
async def get_opt_in_list():
    return opt_in_list

@app.post("/approve_opt_in", status_code=status.HTTP_204_NO_CONTENT)
async def approve_opt_in(trainee: OptInTrainee):
    for index, t in enumerate(opt_in_list):
        if t.email == trainee.email:
            opt_in_list[index].state = "approved"
            return
    raise HTTPException(status_code=404, detail="Trainee not found")

@app.post("/decline_opt_in", status_code=status.HTTP_204_NO_CONTENT)
async def decline_opt_in(trainee: Trainee):
    for index, t in enumerate(opt_in_list):
        if t.email == trainee.email:
            opt_in_list[index].state = "declined"
            return
    raise HTTPException(status_code=404, detail="Trainee not found")
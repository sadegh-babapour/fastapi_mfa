from datetime import datetime

import pyotp

from bson.objectid import ObjectId

from pymongo.collection import ReturnDocument

from fastapi import APIRouter, status, HTTPException

from app.database import User

from . import schemas

def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "otp_enabled": user["otp_enabled"],
        "otp_verified": user["otp_verified"],
        "otp_base32": user["otp_base32"],
        "otp_auth_url": user["otp_auth_url"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }


router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def Create_User(payload: schemas.UserBaseSchema):
    user = User.find_one({"email": payload.email.lower()})

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already Exists!"
        )

    payload.email = payload.email.lower()
    payload.created_at = datetime.utcnow()
    payload.updated_at = payload.created_at()

    result = User.insert_one(payload.dict())

    return {
        'status': 'success', 'message': "Registered successfully, please login"
    }
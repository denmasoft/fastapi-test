import src.schemas as schemas, src.models as models
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.services import get_users

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db)):
    users = get_users.get_users()
    return {"status": "Success", "total": len(users), "data": users}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(payload: schemas.User, db: Session = Depends(get_db)):
    users = get_users.get_users()
    for user in users:
        db_user = models.User(
            name=user["name"],
            username=user["username"],
            email=user["email"],
        )
        db.add(db_user)
    db.commit()
    db.close()
    return {"status": "Success", "total": len(users), "data": users}


@router.get("/{userId}", status_code=status.HTTP_200_OK)
def get_user(userId: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == userId).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No User with id: `{userId}` found",
        )
    return {"status": "Success", "data": user}

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db import crud
from app.db.database import SessionLocal
from app.security import Hash

router = APIRouter()


# Dependency for getting a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Route used to authenticate the user credentials and send them to the home view
@router.post("/login/")
async def do_login(request: Request, response: Response, db: Session = Depends(get_db)):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    if not Hash.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    response.set_cookie(key="session", value="random_session_token")
    return RedirectResponse(url="/home", status_code=status.HTTP_302_FOUND)


# Route used to logout the user and send them back to the login
@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie("session")
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

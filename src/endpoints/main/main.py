from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(
    prefix="/main",
    tags=["main"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/hello")
async def root():
    return {"message": "Hello World"}

from fastapi import APIRouter
router = APIRouter()

@router.get("/item")
def controller():
    return {"hello":"items"}
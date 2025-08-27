from fastapi import APIRouter

router= APIRouter()


@router.get("/user")
def controller():
    return {"hello":"user"}
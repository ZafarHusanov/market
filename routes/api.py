from fastapi import APIRouter
from src.endpoints.main import main
# from src.endpoints.user import lksadf

router = APIRouter(prefix='/api')

router.include_router(main.router)
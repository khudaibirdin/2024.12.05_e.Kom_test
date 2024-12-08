from fastapi import APIRouter, Body 
from .service import get_templates_name

router = APIRouter()


@router.post('/get_form')
async def get_form(data = Body()):
    validate = get_templates_name(data)
    return validate

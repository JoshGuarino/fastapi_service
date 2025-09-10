from fastapi import APIRouter, HTTPException
from services.character import get_character_quote

router = APIRouter()


@router.get("/character/{character_name}")
async def character_quote(character_name: str):
    quoute = get_character_quote(character_name)
    if quoute is None:
        raise HTTPException(status_code=404, detail="Character not found.")
    return get_character_quote(character_name)

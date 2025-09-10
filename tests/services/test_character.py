from services.character import get_character_quote, get_character_id

def test_character_quote():
    quoute = get_character_quote("Gandalf")
    assert isinstance(quoute, str)

def test_get_character_id():
    id = get_character_id('Gandalf')
    assert isinstance(id, str)

def test_character_id_not_found():
    id = get_character_id('NotFound')
    assert id is None

# convert mongodb data in dictionary
def noteEntity(item) -> dict:
    return {
        "id" : str(item["_id"]),
        "title" : item["title"],
        "desc" : item["desc"],
        "important" : item["important"]
    }
    
def notesEntity(items) -> list:
    return [notesEntity(item) for item in items]
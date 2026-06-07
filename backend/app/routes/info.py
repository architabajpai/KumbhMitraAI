from fastapi import APIRouter

router = APIRouter()

@router.get("/events")
def events():

    return {
        "events": [
            {
                "name":"Morning Aarti",
                "time":"6 AM"
            },
            {
                "name":"Ganga Snan",
                "time":"8 AM"
            }
        ]
    }

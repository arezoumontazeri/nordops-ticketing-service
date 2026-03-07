import uuid
from fastapi import APIRouter, status
from app.api.schemas import TicketCreate, TicketOut

router = APIRouter(prefix="/tickets", tags=["tickets"])

tickets = []


@router.post("", response_model=TicketOut, status_code=status.HTTP_201_CREATED)
def create_ticket(payload: TicketCreate):
    ticket = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "status": "open",
    }
    tickets.append(ticket)
    return ticket


@router.get("", response_model=list[TicketOut])
def list_tickets():
    return tickets
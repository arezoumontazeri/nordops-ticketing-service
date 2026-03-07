import uuid
from fastapi import APIRouter, HTTPException, status
from app.api.schemas import TicketCreate, TicketOut, TicketUpdate

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


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: str):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise HTTPException(status_code=404, detail="Ticket not found")


@router.patch("/{ticket_id}", response_model=TicketOut)
def update_ticket(ticket_id: str, payload: TicketUpdate):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            update_data = payload.model_dump(exclude_unset=True)

            if "title" in update_data:
                ticket["title"] = update_data["title"]
            if "description" in update_data:
                ticket["description"] = update_data["description"]
            if "status" in update_data:
                ticket["status"] = update_data["status"]

            return ticket

    raise HTTPException(status_code=404, detail="Ticket not found")


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id: str):
    for index, ticket in enumerate(tickets):
        if ticket["id"] == ticket_id:
            tickets.pop(index)
            return

    raise HTTPException(status_code=404, detail="Ticket not found")
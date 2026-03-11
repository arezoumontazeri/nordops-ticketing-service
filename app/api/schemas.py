from typing import Optional, Literal
from pydantic import BaseModel, Field

TicketStatus = Literal["open", "in_progress", "resolved", "closed"]


class TicketCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None


class TicketUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=200)
    description: Optional[str] = None
    status: Optional[TicketStatus] = None


class TicketOut(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: TicketStatus

    class Config:
        from_attributes = True
"""
Service Desk API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.service_desk.schemas import (
    TicketCategoryCreate, TicketCategoryResponse, TicketCreate, TicketResponse,
    TicketCommentCreate, TicketCommentResponse, TicketStatusUpdate
)
from app.modules.service_desk.services import ServiceDeskService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/service-desk", tags=["HR Service Desk"])


def format_ticket_response(t) -> dict:
    cat = t.__dict__.get("category")
    emp = t.__dict__.get("employee")
    comments = t.__dict__.get("comments", [])
    return {
        "id": t.id,
        "tenant_id": t.tenant_id,
        "ticket_number": t.ticket_number,
        "category_id": t.category_id,
        "category_name": cat.name if cat else None,
        "employee_id": t.employee_id,
        "employee_name": emp.full_name if emp else None,
        "assigned_agent_id": t.assigned_agent_id,
        "subject": t.subject,
        "description": t.description,
        "priority": t.priority,
        "status": t.status,
        "due_date": t.due_date,
        "resolved_at": t.resolved_at,
        "resolution_summary": t.resolution_summary,
        "comments": [
            {
                "id": c.id,
                "ticket_id": c.ticket_id,
                "author_user_id": c.author_user_id,
                "author_name": c.author_name,
                "comment_text": c.comment_text,
                "is_internal_note": c.is_internal_note,
                "attachment_url": c.attachment_url,
                "created_at": c.created_at,
            } for c in comments
        ],
        "created_at": t.created_at,
    }


@router.get("/categories", response_model=List[TicketCategoryResponse])
async def list_categories(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List service desk ticket categories."""
    return await ServiceDeskService.list_categories(db, current_user.tenant_id or "default")


@router.post("/categories", response_model=TicketCategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    data: TicketCategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("service_desk.admin")),
):
    """Create a ticket category queue."""
    return await ServiceDeskService.create_category(db, current_user.tenant_id or "default", data)


@router.post("/tickets", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
async def create_ticket(
    data: TicketCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("service_desk.ticket.create")),
):
    """Submit an HR service request ticket."""
    ticket = await ServiceDeskService.create_ticket(
        db, current_user.tenant_id or "default", current_user.id, data
    )
    return format_ticket_response(ticket)


@router.get("/tickets", response_model=List[TicketResponse])
async def list_tickets(
    status: Optional[str] = Query(None),
    all_tickets: bool = Query(False),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List service desk tickets."""
    emp_id = None if (all_tickets and (current_user.is_superuser or "service_desk.ticket.manage" in current_user.permissions)) else current_user.id
    tickets = await ServiceDeskService.list_tickets(
        db, current_user.tenant_id or "default", employee_id=emp_id, status=status, skip=skip, limit=limit
    )
    return [format_ticket_response(t) for t in tickets]


@router.get("/tickets/{ticket_id}", response_model=TicketResponse)
async def get_ticket(
    ticket_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Get ticket details and conversation thread."""
    ticket = await ServiceDeskService.get_ticket(db, current_user.tenant_id or "default", ticket_id)
    return format_ticket_response(ticket)


@router.post("/tickets/{ticket_id}/comments", response_model=TicketCommentResponse, status_code=status.HTTP_201_CREATED)
async def add_comment(
    ticket_id: str,
    data: TicketCommentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Add reply or note to ticket."""
    comment = await ServiceDeskService.add_comment(
        db, current_user.tenant_id or "default", ticket_id, current_user.id, current_user.email, data
    )
    return {
        "id": comment.id,
        "ticket_id": comment.ticket_id,
        "author_user_id": comment.author_user_id,
        "author_name": comment.author_name,
        "comment_text": comment.comment_text,
        "is_internal_note": comment.is_internal_note,
        "attachment_url": comment.attachment_url,
        "created_at": comment.created_at,
    }


@router.put("/tickets/{ticket_id}/status", response_model=TicketResponse)
async def update_ticket_status(
    ticket_id: str,
    data: TicketStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("service_desk.ticket.manage")),
):
    """Update ticket resolution or state."""
    ticket = await ServiceDeskService.update_status(
        db, current_user.tenant_id or "default", ticket_id, current_user.id, data
    )
    return format_ticket_response(ticket)

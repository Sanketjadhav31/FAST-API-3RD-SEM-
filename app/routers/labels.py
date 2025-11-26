from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models import Label
from app.schemas import LabelCreate, LabelUpdate, LabelRead

router = APIRouter(prefix="/labels", tags=["Labels"])

@router.post("/", response_model=LabelRead, status_code=201)
def create_label(label_data: LabelCreate, session: Session = Depends(get_session)):
    """Create a new label"""
    # Check if label with same name exists
    existing = session.exec(select(Label).where(Label.name == label_data.name)).first()
    if existing:
        raise HTTPException(status_code=409, detail="Label with this name already exists")
    
    # Create label
    label = Label(
        name=label_data.name,
        color=label_data.color
    )
    session.add(label)
    session.commit()
    session.refresh(label)
    
    return label

@router.get("/", response_model=List[LabelRead])
def get_labels(session: Session = Depends(get_session)):
    """Get all labels"""
    labels = session.exec(select(Label)).all()
    return labels

@router.get("/{label_id}", response_model=LabelRead)
def get_label(label_id: int, session: Session = Depends(get_session)):
    """Get a single label by ID"""
    label = session.get(Label, label_id)
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")
    
    return label

@router.patch("/{label_id}", response_model=LabelRead)
def update_label(label_id: int, label_data: LabelUpdate, session: Session = Depends(get_session)):
    """Update a label"""
    label = session.get(Label, label_id)
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")
    
    # Check name uniqueness if updating name
    update_data = label_data.model_dump(exclude_unset=True)
    if "name" in update_data and update_data["name"] != label.name:
        existing = session.exec(select(Label).where(Label.name == update_data["name"])).first()
        if existing:
            raise HTTPException(status_code=409, detail="Label with this name already exists")
    
    # Update fields
    for key, value in update_data.items():
        if value is not None:
            setattr(label, key, value)
    
    session.add(label)
    session.commit()
    session.refresh(label)
    
    return label

@router.delete("/{label_id}", status_code=204)
def delete_label(label_id: int, session: Session = Depends(get_session)):
    """Delete a label"""
    label = session.get(Label, label_id)
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")
    
    session.delete(label)
    session.commit()
    
    return None

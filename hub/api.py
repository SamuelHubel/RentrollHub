from typing import Annotated

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from hub.db import get_session

app = FastAPI(title="Rent Roll & Maintenance Hub")
router = APIRouter(prefix="/api/v1")


class Health(BaseModel):
    status: str
    database: str


@router.get("/health")
def health(session: Annotated[Session, Depends(get_session)]) -> Health:
    try:
        session.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        raise HTTPException(status_code=503, detail="database unreachable") from exc
    return Health(status="ok", database="ok")


app.include_router(router)

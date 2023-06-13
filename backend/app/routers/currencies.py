from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, desc
from sqlalchemy.orm import Session, session
from starlette import status

from backend.app.database import get_db
from backend.app.models import Deribit

router = APIRouter(
    prefix="/tickers",
    tags=["prices"],
    responses={404: {"description": "Not found"}},

)


@router.get("/{name}", status_code=status.HTTP_200_OK)
def get_ticker_info(ticker: str, db: Session = Depends(get_db)):

    currency_info = db.query(Deribit).filter_by(ticker=ticker).all()
    if currency_info is None:
        raise HTTPException(status_code=404)
    return currency_info


@router.get("/{last_price}", status_code=status.HTTP_200_OK)
def get_last_price(ticker: str, db: Session = Depends(get_db)):

    last_price = db.query(Deribit).filter_by(ticker=ticker).order_by(desc(Deribit.created_at)).first()

    if last_price is None:
        raise HTTPException(status_code=404)
    return last_price


@router.get("/price_by_date")
def get_price(ticker: str, date: str = Query(...), db: Session = Depends(get_db)):
    currency_price = db.query(Deribit).filter(Deribit.ticker == ticker,Deribit.created_at == date).order_by(Deribit.created_at).first()

    if currency_price is None:
        raise HTTPException(status_code=404)
    return currency_price

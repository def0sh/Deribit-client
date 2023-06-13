from sqlalchemy import Column, Integer, String, TIMESTAMP, Numeric

from backend.app.database import Base


class Deribit(Base):
    __tablename__ = "deribit"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,)

    def __repr__(self):
        return f'Deribit {self.ticker}'


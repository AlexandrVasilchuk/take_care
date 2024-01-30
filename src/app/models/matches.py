from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.core.db import Base


class Match(Base):
    user_id1: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    user_id2: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="matches")

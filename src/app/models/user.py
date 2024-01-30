from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship

from src.app.core.base import Base
from src.app.models.matches import Match


class User(SQLAlchemyBaseUserTable[int], Base):
    matches = relationship(Match, back_populates="user")

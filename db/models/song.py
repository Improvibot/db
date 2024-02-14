from datetime       import date
from db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Song(Base):
    __tablename__ = "songs"
    
    id:            Mapped[int] = mapped_column(primary_key=True)
    title:         Mapped[str]
    creation_date: Mapped[date]
    data:          Mapped[bytes]

    def __repr__(self) -> str:
        return(f'Song #{self.id}: {self.title}')


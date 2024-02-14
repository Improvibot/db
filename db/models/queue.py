from db.models.base import Base
from db.models.song import Song
from db.models.user import User
from sqlalchemy     import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Queue(Base):
#class Queue():
    __tablename__ = "queue"

    id:   Mapped[int] = mapped_column(primary_key=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    #song:    Mapped["Song"]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    #user:    Mapped["User"] = relationship(cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f'Queue - {song.title}, requested by {user.username}'

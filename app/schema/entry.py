from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from services.db import Base


class Entry(Base):
    __tablename__ = 'entrys'
    entry_id = Column(Integer, primary_key=True)
    content = Column(String(1024))
    timestamp = Column(DateTime)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
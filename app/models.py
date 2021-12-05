from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class App(Base):
    __tablename__ = "apps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    icon = Column(String, unique=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    screenshots = relationship("Screenshot", back_populates="owner")


class Screenshot(Base):
    __tablename__ = "screenshots"

    id = Column(Integer, primary_key=True, index=True)
    app_id = Column(Integer, ForeignKey("apps.id"))
    file_name = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    owner = relationship("App", back_populates="screenshots")
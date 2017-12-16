#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states")
    else:
        name = ""

    if models.storage_type == "db":
        @property
        def cities(self):
            """Get City instances"""
            list = []
            c = models.storage.all("City").values()
            for item in c:
                if item.state_id == self.id:
                    list.append(item)
            return list

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

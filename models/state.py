#!/usr/bin/python
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    elif models.storage_type == "file":
        name = ""

        @property
        def cities(self):
            list = []
            c = models.storage.all(City)
            for item in c.values():
                if item.state_id == self.id:
                    list.append(item)
            return list
    else:
        print("state.py: Unknown Storage_Type")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

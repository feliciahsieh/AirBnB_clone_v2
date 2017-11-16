#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Representation of Review """
    if models.storage_type == "db":
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)

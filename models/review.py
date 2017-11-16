#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """Representation of Review """
    if models.storage_type == "db":
        pass
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)

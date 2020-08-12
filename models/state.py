#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128))
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City"""
        my_list = []
        extracted_cities = models.storage.all("City")
        for k, v in extracted_cities.items():
            if self.id == v["state_id"]:
                my_list.append(v)
        return my_list

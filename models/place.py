#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128))
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref='place', cascade="all, delete")

    @property
    def reviews(self):
        """getter attribute reviews that returns the list of Review instances
        with place_id equals to the current Place.id
        """
        from models import storage
        my_list = []
        extracted_reviews = models.storage.all(Review).values()
        for review in extracted_reviews:
            if self.id == review.place_id:
                my_list.append(review)
        return my_list

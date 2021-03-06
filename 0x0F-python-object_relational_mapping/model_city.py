#!/usr/bin/python3
"""
city class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
        """
        class representing a city
        """
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

        def __init__(self, name):
                self.name = name

        def __str__(self):
                return '({}) {}'.format(self.id, self.name)

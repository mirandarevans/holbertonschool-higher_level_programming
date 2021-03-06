#!/usr/bin/python3
"""
state class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
        """
        class representing a state
        """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)

        def __init__(self, name):
                self.name = name

        def __str__(self):
                return '{}: {}'.format(self.id, self.name)

#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base  # Updated import

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')  # Fixed typo and URL
    Base.metadata.create_all(engine)  # Capital "Base"
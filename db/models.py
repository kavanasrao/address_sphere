from db.base import Base
from sqlalchemy import Integer, Column, Text,Float

class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(Text, nullable=False)
    lat = Column(Float, nullable=False)
    lon =Column(Float, nullable=False)


    def __repr__(self):
        return f"Address id ={self.id}, Address = {self.address}"


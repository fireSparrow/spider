
from sqlalchemy import Column, Integer, Numeric, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


TableBase = declarative_base()


class ParsedItem(TableBase):
    __table__ = 'item'

    id = Column(Integer, primary_key=True)
    _attributes = relationship('ItemAttribute', backref='item')

    @property
    def attributes(self):
        return {a.name: a.value for a in self._attributes}


class ItemAttribute(TableBase):
    __table__ = 'item_attr'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    name = Column(String, nullable=False)
    value_num = Column(Numeric)

    @property
    def value(self):
        return self.value_num
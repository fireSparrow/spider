
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import json


TableBase = declarative_base()


class Item(TableBase):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('feed.id'), nullable=False)
    title = Column(String)
    update_dt = Column(DateTime)

    feed = relationship('Feed', backref='items')


class Feed(TableBase):
    __tablename__ = 'feed'

    id = Column(Integer, primary_key=True)
    engine_id = Column(Integer, ForeignKey('engine.id'), nullable=False)
    _params = Column(JSON)

    engine = relationship('Engine')

    @property
    def params(self):
        return json.load(self._params)


class Engine(TableBase):
    __tablename__ = 'engine'

    id = Column(Integer, primary_key=True)
    class_name = Column(String)


class Task(TableBase):
    __tablename__ = 'task'

    id = Column(Integer,  primary_key=True)
    worker_id = Column(Integer, ForeignKey('worker.id'), nullable=False)
    scheduled = Column(DateTime)
    feed_id = Column(Integer, ForeignKey('feed.id'))

    feed = relationship('Feed')


class Worker(TableBase):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True)
    class_name = Column(String)



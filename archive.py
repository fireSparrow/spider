
from sqlalchemy import Column, Integer, Numeric, ForeignKey, String, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import json

import source
import worker


TableBase = declarative_base()


class Item(TableBase):
    __table__ = 'item'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('source.id'), nullable=False)
    title = Column(String)
    update_dt = Column(DateTime)

    source = relationship('Source', backref='items')


class Feed(TableBase):
    __table__ = 'feed'

    id = Column(Integer, primary_key=True)
    engine_id = Column(Integer, ForeignKey('engine.id'), nullable=False)
    _params = Column(JSON)

    engine = relationship('Engine')

    @property
    def params(self):
        return json.load(self._params)


class Engine(TableBase):
    __table__ = 'engine'

    id = Column(Integer, primary_key=True)
    class_name = Column(String)


class Task(TableBase):
    __table__ = 'task'

    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey('worker.id'), nullable=False)
    scheduled = Column(DateTime)
    feed_id = Column(Integer, ForeignKey('feed.id'))

    _feed = relationship('Feed')


class Executor(TableBase):
    __table__ = 'worker'

    id = Column(Integer, primary_key=True)
    class_name = Column(String)



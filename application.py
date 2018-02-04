
from mapper import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session
from os import path


class Application:

    _base_path = 'base.sqlite'

    def __init__(self):
        self.base = self._base_path
        base_exist = path.exists(self.base)
        engine = create_engine('sqlite:///{}'.format(self.base))
        self.engine = engine
        if not base_exist:
            self._fill_new_base()

    def new_session(self):
        session = create_session(bind=self.engine)
        return session

    def _fill_new_base(self):
        ses = create_session(bind=self.engine)
        with ses.begin():
            for stmt in _create:
                ses.execute(stmt)
            from source import usefull
            for (idx, class_name) in usefull.items():
                eng = Engine()
                eng.id = idx
                eng.class_name = class_name
                ses.add(eng)

_create = [
    '''
    create table item (
        id integer primary key,
        source_id integer,
        title text,
        update_dt datetime
    ) ''',
    '''
    create table feed (
        id integer primary key,
        engine_id integer,
        _params text
    ) ''',
    '''
    create table engine (
        id integer primary key,
        class_name text
    )''',
    '''
    create table task (
        id integer primary key,
        worker_id integer,
        scheduled datetime,
        feed_id integer
    )''',
    '''
    create table worker (
        id integer primary key,
        class_name text
    )'''
]
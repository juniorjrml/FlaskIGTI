from typing import Any

from data import alchemy
from . import episode
from .bd_model import BdService


class ShowModel(alchemy.Model):
    __tablename__ = 'shows'
    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(80))
    episodes = alchemy.relationship(episode.EpisodeModel, lazy='dynamic')


    def __init__(self, name):
        self.name = name


    def json(self):
        return {'id': self.id, 'name': self.name, 'episodes': [episode.json() for episode in self.episodes.all()]}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def save_to_bd(self):
        alchemy.session.add(self)
        alchemy.session.commit()


    def delete_from_bd(self):
        alchemy.session.delete(self)
        alchemy.session.commit()

    def update(self, name):
        self.name = name
        alchemy.session.commit()

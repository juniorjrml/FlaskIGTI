from data import alchemy

class BdService(alchemy.Model):
    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(80))


    def __init__(self, name):
        self.name = name


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()


    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()
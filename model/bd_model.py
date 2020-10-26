from data import alchemy

class BdService():
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def save_to_db(db, object):
        db.session.add(object)
        db.session.commit()

    @classmethod
    def delete_from_db(db, object):
        db.session.delete(object)
        db.session.commit()
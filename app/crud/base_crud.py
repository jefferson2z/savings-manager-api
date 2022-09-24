from sqlalchemy.orm import Session


class BaseCRUD:
    def __init__(self, model):
        self.model = model

    def get(self, db: Session, id):
        db_item = db.query(self.model).filter(self.model.id == id).first()
        return db_item

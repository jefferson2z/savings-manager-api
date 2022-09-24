from sqlalchemy.orm import Session


class BaseCRUD:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, item_create):
        db_item = self.model(**item_create.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get(self, db: Session, id):
        db_item = db.query(self.model).filter(self.model.id == id).first()
        return db_item

    def list(self, db: Session, *, skip: int = 0, limit: int = 100):
        db_item_list = db.query(self.model).offset(skip).limit(limit).all()
        return db_item_list

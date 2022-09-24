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

    def update(self, db: Session, *, db_item, item_update):
        item_data = item_update.dict(exclude_unset=True)
        for key, value in item_data.items():
            setattr(db_item, key, value)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int):
        db_item = db.query(self.model).get(id)
        db.delete(db_item)
        db.commit()
        return db_item

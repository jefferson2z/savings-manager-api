from sqlalchemy.orm import Session

from app import models
from app.crud.base_crud import BaseCRUD


class DepositCRUD(BaseCRUD):
    def list_by_asset(
        self, db: Session, *, asset_id: int, skip: int = 0, limit: int = 100
    ):
        db_deposit_list = (
            db.query(self.model)
            .where(self.model.asset_id == asset_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return db_deposit_list


deposit = DepositCRUD(models.Deposit)

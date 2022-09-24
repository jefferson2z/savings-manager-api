from sqlalchemy.orm import Session

from app import models
from app.crud.base_crud import BaseCRUD
from app.schemas import asset_schema


class AssetCRUD(BaseCRUD):
    def list_by_portfolio(
        self, db: Session, *, portfolio_id: int, skip: int = 0, limit: int = 100
    ):
        db_asset_list = (
            db.query(self.model)
            .where(self.model.portfolio_id == portfolio_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return db_asset_list


asset = AssetCRUD(models.Asset)

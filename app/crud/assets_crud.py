from sqlalchemy.orm import Session

from app import models
from app.crud.base_crud import BaseCRUD
from app.schemas import asset_schema


class AssetCRUD(BaseCRUD):
    pass


asset = AssetCRUD(models.Asset)


def list_assets(db: Session, portfolio_id: int, skip: int = 0, limit: int = 100):
    db_asset_list = (
        db.query(models.Asset)
        .where(models.Asset.portfolio_id == portfolio_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_asset_list


def update_asset(
    db: Session,
    db_asset: asset_schema.Asset,
    asset_update: asset_schema.AssetUpdate,
):
    asset_data = asset_update.dict(exclude_unset=True)
    for key, value in asset_data.items():
        setattr(db_asset, key, value)
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


def delete_asset(db: Session, asset_id: int):
    db_asset = db.query(models.Asset).get(asset_id)
    db.delete(db_asset)
    db.commit()
    return db_asset

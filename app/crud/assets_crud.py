from sqlalchemy.orm import Session

from app import models
from app.schemas import asset_schema


def create_asset(db: Session, asset_create: asset_schema.AssetCreate):
    db_asset = models.Asset(**asset_create.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


def get_asset(db: Session, asset_id: int):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    return db_asset


def list_assets(db: Session, portfolio_id: int, skip: int = 0, limit: int = 100):
    db_asset_list = (
        db.query(models.Asset)
        .where(models.Asset.portfolio_id == portfolio_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_asset_list

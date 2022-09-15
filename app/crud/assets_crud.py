from sqlalchemy.orm import Session

from app import models
from app.schemas import asset_schema


def create_asset(db: Session, asset_create: asset_schema.AssetCreate):
    db_asset = models.Asset(**asset_create.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

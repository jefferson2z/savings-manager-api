from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import asset_schema
from app.api import dependencies
from app.crud import assets_crud


router = APIRouter(
    prefix="/assets",
    tags=["assets"],
    dependencies=[Depends(dependencies.get_current_user)],
)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=asset_schema.Asset
)
def create_asset(
    asset: asset_schema.AssetCreate,
    db: Session = Depends(dependencies.get_db),
):
    db_asset = assets_crud.create_asset(db, asset)
    return db_asset


@router.get("/{asset_id}", response_model=asset_schema.Asset)
def get_asset(asset_id: int, db: Session = Depends(dependencies.get_db)):
    db_asset = assets_crud.get_asset(db, asset_id=asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

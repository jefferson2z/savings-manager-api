from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
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
    db_asset = crud.asset.create(db, asset)
    return db_asset


@router.get("/{asset_id}", response_model=asset_schema.Asset)
def get_asset(asset_id: int, db: Session = Depends(dependencies.get_db)):
    db_asset = crud.asset.get(db, id=asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset


@router.get("/", response_model=list[asset_schema.Asset])
def list_assets(
    portfolio_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(dependencies.get_db),
):
    db_assets = crud.asset.list_by_portfolio(
        db,
        portfolio_id=portfolio_id,
        skip=skip,
        limit=limit,
    )
    return db_assets


@router.put("/{asset_id}", response_model=asset_schema.Asset)
def asset_update(
    asset_id: int,
    asset: asset_schema.AssetUpdate,
    db: Session = Depends(dependencies.get_db),
):
    db_asset = crud.asset.get(db, id=asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    db_asset = crud.asset.update(db, db_item=db_asset, item_update=asset)
    return db_asset


@router.delete("/{asset_id}", response_model=asset_schema.Asset)
def delete_asset(asset_id: int, db: Session = Depends(dependencies.get_db)):
    db_asset = crud.asset.get(db, id=asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_asset = crud.asset.delete(db, id=asset_id)
    return db_asset

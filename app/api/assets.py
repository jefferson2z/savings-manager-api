from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app.schemas import asset_schema
from app.api import dependencies
from app.crud import assets_crud


router = APIRouter(
    prefix="/assets",
    tags=["assets"],
    dependencies=[Depends(dependencies.get_current_user)],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_asset(
    asset: asset_schema.AssetCreate,
    db: Session = Depends(dependencies.get_db),
):
    db_asset = assets_crud.create_asset(db, asset)
    return {"asset": db_asset}

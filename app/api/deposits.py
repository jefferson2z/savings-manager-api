from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.schemas import deposit_schema
from app.api import dependencies

router = APIRouter(
    prefix="/deposits",
    tags=["deposits"],
    dependencies=[Depends(dependencies.get_current_user)],
)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=deposit_schema.Deposit
)
def create_deposit(
    deposit: deposit_schema.DepositCreate,
    db: Session = Depends(dependencies.get_db),
):
    db_deposit = crud.deposit.create(db, deposit)
    return db_deposit


@router.get("/{deposit_id}", response_model=deposit_schema.Deposit)
def get_deposit(deposit_id: int, db: Session = Depends(dependencies.get_db)):
    db_deposit = crud.deposit.get(db, id=deposit_id)
    if db_deposit is None:
        raise HTTPException(status_code=404, detail="Deposit not found")
    return db_deposit


@router.get("/", response_model=list[deposit_schema.Deposit])
def list_deposits(
    asset_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(dependencies.get_db),
):
    db_deposits = crud.deposit.list_by_asset(
        db,
        asset_id=asset_id,
        skip=skip,
        limit=limit,
    )
    return db_deposits


@router.put("/{deposit_id}", response_model=deposit_schema.Deposit)
def asset_update(
    deposit_id: int,
    deposit: deposit_schema.DepositUpdate,
    db: Session = Depends(dependencies.get_db),
):
    db_deposit = crud.deposit.get(db, id=deposit_id)
    if db_deposit is None:
        raise HTTPException(status_code=404, detail="Deposit not found")
    db_deposit = crud.deposit.update(db, db_item=db_deposit, item_update=deposit)
    return db_deposit


@router.delete("/{deposit_id}", response_model=deposit_schema.Deposit)
def delete_asset(deposit_id: int, db: Session = Depends(dependencies.get_db)):
    db_deposit = crud.deposit.get(db, id=deposit_id)
    if db_deposit is None:
        raise HTTPException(status_code=404, detail="Deposit not found")
    db_deposit = crud.deposit.delete(db, id=deposit_id)
    return db_deposit

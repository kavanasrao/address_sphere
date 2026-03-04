from db.session import engine, get_db
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import uvicorn


from db.base import Base
from schema.address import AddressCreate, AddressResponse
from business.address_logic import add_address, update_address, delete_address, get_addresses, get_nearby_addresses

from core.logging_config import logger

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/address", response_model=AddressResponse)
def create_address(data: AddressCreate, db: Session = Depends(get_db)):
    logger.info("Create address request received")
    try:
        result = add_address(db, data)
        return result
    except Exception as e:
        logger.error(f"Create address failed | {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create address")


@app.put("/address/{address_id}", response_model=AddressResponse)
def update(address_id: int, data: AddressCreate, db: Session = Depends(get_db)):
    logger.info(f"Update request | id={address_id}")
    result = update_address(db, address_id, data)

    if not result:
        logger.warning(f"Update failed | Address {address_id} not found")
        raise HTTPException(status_code=404, detail="Address not found")

    return result


@app.get("/addresses", response_model=list[AddressResponse])
def get_all(db: Session = Depends(get_db)):
    logger.info("Fetching all addresses")
    try:
        return get_addresses(db)
    except Exception as e:
        logger.error(f"Fetch failed | {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch addresses")


@app.delete("/address/{address_id}")
def delete(address_id: int, db: Session = Depends(get_db)):
    logger.info(f"Delete request | id={address_id}")

    result = delete_address(db, address_id)

    if not result:
        logger.warning(f"Delete failed | Address {address_id} not found")
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Address deleted successfully"}


@app.get("/addresses/nearby", response_model=list[AddressResponse])
def nearby(lat: float, lon: float, distance_km: float, db: Session = Depends(get_db)):
    logger.info(f"Nearby search | lat={lat} lon={lon} radius={distance_km}km")

    try:
        return get_nearby_addresses(db, lat, lon, distance_km)
    except Exception as e:
        logger.error(f"Nearby search failed | {str(e)}")
        raise HTTPException(status_code=500, detail="Nearby search failed")


@app.get("/health")
def health():
    logger.info("Health check called")
    return {"status": "OK"}



if __name__ == '__main__':
    uvicorn.run(app, host= "127.0.0.1", port= 8000)
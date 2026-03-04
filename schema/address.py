from pydantic import BaseModel, Field


class AddressCreate(BaseModel):
    address: str
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)


class AddressResponse(AddressCreate):
    id: int

    class Config:
        from_attributes = True
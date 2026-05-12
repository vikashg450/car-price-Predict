from typing import Literal
from pydantic import BaseModel, Field

class CarFeatures(BaseModel):
    Car_Name: str = Field(..., example="swift")
    Year: int = Field(..., example=2014)
    Present_Price: float = Field(..., example=5.59)
    Kms_Driven: int = Field(..., example=27000)
    Fuel_Type: Literal["Petrol", "Diesel", "CNG"]
    Seller_Type: Literal["Dealer", "Individual"]
    Transmission: Literal["Manual", "Automatic"]
    Owner: int = Field(
        ..., ge=0, le=3, example=0, description="Number of previous owners (0,1 or 3)"
    )

class PredictionResponse(BaseModel):
    prediction_price: float

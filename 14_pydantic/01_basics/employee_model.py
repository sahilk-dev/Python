from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Sahil Kamila"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )


class User(BaseModel):
    email: str = Field(...,regex='')
    phone: str = Field(...,regex='')
    age: int = Field(
        ...,
        ge=0,
        le=50,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )
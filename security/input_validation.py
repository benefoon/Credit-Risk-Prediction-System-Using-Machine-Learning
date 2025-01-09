from pydantic import BaseModel, Field, ValidationError

class CreditApplication(BaseModel):
    income: float = Field(gt=1000, description="Income must be greater than $1000")
    age: int = Field(ge=18, le=100, description="Age must be between 18 and 100")
    loan_amount: float = Field(gt=0, description="Loan amount must be greater than zero")

def validate_application(data):
    """Validates credit application input"""
    try:
        validated_data = CreditApplication(**data)
        return {"status": "valid", "data": validated_data}
    except ValidationError as e:
        return {"status": "invalid", "errors": e.errors()}

# Example Usage
application_data = {"income": 5000, "age": 25, "loan_amount": 20000}
print(validate_application(application_data))

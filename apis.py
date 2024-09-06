from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Form, File, HTTPException, UploadFile
from db import engine, Sessionlocal, Base
from md import Buyer, MarketSpecContract
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
app = FastAPI()

@app.post("/submit-profile/")
async def submit_profile(
    first_name: str = Form(...),
    last_name: str = Form(...),
    contact: Optional[str] = Form(None),
    business_type: str = Form(...),
    industry_sector: str = Form(...),
    company_name: Optional[str] = Form(None),
    company_tel: Optional[str] = Form(None),
    company_address_1: Optional[str] = Form(None),
    company_address_2: Optional[str] = Form(None),
    registration_number: Optional[str] = Form(None),
    gst_number: Optional[str] = Form(None),
    id_proof_filename: UploadFile = File(...),
    gst_certificate_filename: UploadFile = File(...),
    trade_license_filename: UploadFile = File(...),
    business_proof_filename: UploadFile = File(...)
):
    try:
        # Read file contents as binary data
        id_proof_filename_data = await id_proof_filename.read()
        gst_certificate_filename_data = await gst_certificate_filename.read()
        trade_license_filename_data = await trade_license_filename.read()
        business_proof_filename_data = await business_proof_filename.read()

        # Create a new profile instance with the uploaded files stored in the database
        profile_data = Buyer(
            first_name=first_name,
            last_name=last_name,
            contact=contact,
            business_type=business_type,
            industry_sector=industry_sector,
            company_name=company_name,
            company_tel=company_tel,
            company_address_1=company_address_1,
            company_address_2=company_address_2,
            registration_number=registration_number,
            gst_number=gst_number,
            id_proof_filename=id_proof_filename_data,
            gst_certificate_filename=gst_certificate_filename_data,
            trade_license_filename=trade_license_filename_data,
            business_proof_filename=business_proof_filename_data
        )

        # Store data in the database
        with Sessionlocal() as session:
            session.add(profile_data)
            session.commit()

        return {"message": "Profile data saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.post("/market-spec-contract/")
async def market_spec_contract(
    farmer_name: Optional[str] = Form(None),
    buyer_name: str = Form(...),
    contract_date: str = Form(...),
    delivery_date: str = Form(...),
    product: str = Form(...),
    quality_req: str = Form(...),
    quantity: str = Form(...),
    packaging_req: str = Form(...),
    buyer_responsibilities: str = Form(...),
    farmer_responsibilities: str = Form(...),
    price: str = Form(...),
    payment_sch: str = Form(...),
    termination_conditions: str = Form(...),
    farmer_sign: UploadFile = File(...),
    buyer_sign: UploadFile = File(...)
):
    try:
        # Convert date strings to 'YYYY-MM-DD' format
        def convert_date(date_str: str) -> str:
            try:
                # Check if the date is already in 'YYYY-MM-DD' format
                if len(date_str) == 10 and date_str[4] == '-' and date_str[7] == '-':
                    datetime.strptime(date_str, '%Y-%m-%d')  # Validate the format
                    return date_str  # Date is already in the correct format
                else:
                    # Convert from 'DD-MM-YYYY' to 'YYYY-MM-DD'
                    date_obj = datetime.strptime(date_str, '%d-%m-%Y')
                    return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid date format: {date_str}")

        formatted_contract_date = convert_date(contract_date)
        formatted_delivery_date = convert_date(delivery_date)

        # Read file contents as binary data
        farmer_sign_data = await farmer_sign.read()
        buyer_sign_data = await buyer_sign.read()

        # Create a new MarketSpecContract instance with the provided data
        new_contract = MarketSpecContract(
            farmer_name=farmer_name,
            buyer_name=buyer_name,
            contract_date=formatted_contract_date,
            delivery_date=formatted_delivery_date,
            product=product,
            quality_req=quality_req,
            quantity=quantity,
            packaging_req=packaging_req,
            buyer_responsibilities=buyer_responsibilities,
            farmer_responsibilities=farmer_responsibilities,
            price=price,
            payment_sch=payment_sch,
            termination_conditions=termination_conditions,
            farmer_sign=farmer_sign_data,
            buyer_sign=buyer_sign_data
        )

        # Save the contract in the database
        with Sessionlocal() as session:
            session.add(new_contract)
            session.commit()

        return {"message": "Contract data saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
from typing import Optional
from db import Base 
from  sqlalchemy import Column,Integer,String,Boolean,ForeignKey,LargeBinary,Date

"""
class Farmer(Base):
"""
    
class Buyer(Base):
    __tablename__='Buyer'
    first_name = Column(String(100),primary_key=True, nullable=False)
    last_name = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)
    business_type = Column(String(100), nullable=False)
    industry_sector = Column(String(100), nullable=False)
    company_name = Column(String(100), nullable=False)
    company_tel = Column(String(20), nullable=False)
    company_address_1 = Column(String(100), nullable=False)
    company_address_2 = Column(String(100), nullable=False)
    registration_number = Column(String(50), nullable=False)
    gst_number = Column(String(50), nullable=False)
    id_proof_filename = Column(LargeBinary, nullable=False)
    gst_certificate_filename = Column(LargeBinary, nullable=False)
    trade_license_filename = Column(LargeBinary, nullable=False)
    business_proof_filename = Column(LargeBinary, nullable=False)
           

class MarketSpecContract(Base):
    __tablename__ = 'market_spec_contract'

    id = Column(Integer, primary_key=True, autoincrement=True)
    farmer_name = Column(String(100))
    buyer_name = Column(String(100), nullable=False)
    contract_date = Column(Date, nullable=False)
    delivery_date = Column(Date, nullable=False)
    product = Column(String(100), nullable=False)
    quality_req = Column(String(100), nullable=False)
    quantity = Column(String(100), nullable=False)
    packaging_req = Column(String(100), nullable=False)
    buyer_responsibilities = Column(String(100), nullable=False)
    farmer_responsibilities = Column(String(100), nullable=False)
    price = Column(String(100), nullable=False)
    payment_sch = Column(String(100), nullable=False)
    termination_conditions = Column(String(100), nullable=False)
    farmer_sign = Column(LargeBinary, nullable=False)
    buyer_sign = Column(LargeBinary, nullable=False)

from numpy import random
from HotelsDataBase import HotelsDataBase
import os

from Redact_hotel_form import Redact_hotel_form



connecting_string = f"{os.getcwd()}\AllHotelsInfo.txt"
HotelList = HotelsDataBase(connecting_string)
form = Redact_hotel_form(HotelList)
form.create_form()   
    

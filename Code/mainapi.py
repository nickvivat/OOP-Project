from typing import Union
import Payment as p
from SearchRoom import RoomCatalog
import Roominstance as r
from User import Member,Admin
from Booking import Booking, BookingHistory
import uuid

from fastapi import FastAPI, HTTPException

app = FastAPI()


class System:
    def __init__(self):
        self.acc_list = []

    def create_member(self, fname: str, lname: str, email: str, password: str, phone_number: str):
        new_member = Member(fname, lname, email, password, phone_number)
        self.acc_list.append(new_member)
        return new_member

    
system = System()

Catalog = RoomCatalog()
admin = Admin('','','')

admin.add_show_room(Catalog, r.room_Deluxepremier)
admin.add_show_room(Catalog, r.room_Chaophraya)
admin.add_show_room(Catalog, r.room_Deluxebalcony)
admin.add_show_room(Catalog, r.room_Mandarin)
admin.add_show_room(Catalog, r.room_State)
admin.add_show_room(Catalog, r.room_JuniorterraceSuite)
admin.add_show_room(Catalog, r.room_Deluxe1bedroomSuite)
admin.add_show_room(Catalog, r.room_Deluxe2bedroomSuite)
admin.add_show_room(Catalog, r.room_ChaophrayaSuite)
admin.add_show_room(Catalog, r.room_AuthorsSuite)
admin.add_show_room(Catalog, r.room_Deluxe1bedroomthemeSuite)
admin.add_show_room(Catalog, r.room_Deluxe2bedroomthemeSuite)
admin.add_show_room(Catalog, r.room_Premier1bedroom)
admin.add_show_room(Catalog, r.room_Premier2bedroomSuite)
admin.add_show_room(Catalog, r.room_Siam1bedroomSuite)
admin.add_show_room(Catalog, r.room_Ambassador2bedroomSuite)
admin.add_show_room(Catalog, r.room_Selandia2bedroomSuite)
admin.add_show_room(Catalog, r.room_RoyalSuite)
admin.add_show_room(Catalog, r.room_Oriental2bedroomSuite)

admin.add_room(Catalog, r.room_Deluxepremier_list)
admin.add_room(Catalog, r.room_Chaophraya_list)
admin.add_room(Catalog, r.room_Deluxebalcony_list)
admin.add_room(Catalog, r.room_Mandarin_list)
admin.add_room(Catalog, r.room_State_list)
admin.add_room(Catalog, r.room_JuniorterraceSuite_list)
admin.add_room(Catalog, r.room_Deluxe1bedroomSuite_list)
admin.add_room(Catalog, r.room_Deluxe2bedroomSuite_list)
admin.add_room(Catalog, r.room_ChaophrayaSuite_list)
admin.add_room(Catalog, r.room_AuthorsSuite_list)
admin.add_room(Catalog, r.room_Deluxe1bedroomthemeSuite_list)
admin.add_room(Catalog, r.room_Deluxe2bedroomthemeSuite_list)
admin.add_room(Catalog, r.room_Premier1bedroom_list)
admin.add_room(Catalog, r.room_Premier2bedroomSuite_list)
admin.add_room(Catalog, r.room_Siam1bedroomSuite_list)
admin.add_room(Catalog, r.room_Ambassador2bedroomSuite_list)
admin.add_room(Catalog, r.room_Selandia2bedroomSuite_list)
admin.add_room(Catalog, r.room_RoyalSuite_list)
admin.add_room(Catalog, r.room_Oriental2bedroomSuite_list)

admin.update_price(r.room_Ambassador2bedroomSuite, 34000)
admin.update_price(r.room_Oriental2bedroomSuite, 89000)
admin.update_price(r.room_RoyalSuite, 45000)
admin.update_price(r.room_Selandia2bedroomSuite, 56000)
admin.update_price(r.room_Chaophraya, 22000)

h = BookingHistory()


@app.post("/register")
async def register(fname: str, lname: str, email: str, password: str, confirmed_password: str, phone_number: str):
    if len(fname) < 3:
        return {"message": "First name needs to be more than 3 characters"}
    if len(lname) < 3:
        return {"message": "Last name needs to be more than 3 characters"}
    if password != confirmed_password:
        return {"message": "Password does not match"}
    if len(phone_number) != 10:
        return {"message": "Phone number should be 10 digits long"}

    # Check if email already exists
    for member in system.acc_list:
        if member.email == email:
            return {"message": "Email already exists"} 

    # If email does not exist, create new user
    global new_member
    new_member = system.create_member(fname, lname, email, password, phone_number)
    return {'message': 'Registration successful'}

@app.get("/show_account_list")
async def show_account_list():
    # system.acc_list = json.loads(system.acc_list)
    return {"account_list" : [vars(member) for member in system.acc_list]}

@app.get("/login")
async def login(email: str, password: str):
    for user in system.get_acc_list():
        if email == user.email:
            if password == user.password:
                return {"message": "Login successful", "user": vars(user)}
            elif password != user.password:
                raise HTTPException(status_code=401, detail="Incorrect password")
    

@app.get("/select_room")
async def select_room(start_date : str, end_date : str, room_type : str):
    global s1
    s1 = new_member.select_room(start_date, end_date, room_type, Catalog)
    return s1


payment_history = p.PaymentHistory()
sc = p.SpecialCode()

sc1 = p.SpecialCode('iata number', 'EASY','5')
sc2 = p.SpecialCode('promo code', 'HARD','10')
sc.add_sc_list(sc1)
sc.add_sc_list(sc2)

@app.post('/payment_info')
async def add_payment_info(sc_type: str,
                           sc_code: str,
                           method: str):
    global p1,c1
    c1=''
    p1 = p.Payment(new_member, s1, method, c1, specialcode='')
    newamount_sc = p1.discount_ccl(sc_type, sc_code, sc.get_sc_list())
    if not newamount_sc[0].startswith('F'):
        p1.set_amount(newamount_sc[0])
        p1.set_specialcode(newamount_sc[1])
    else:p1 = 'Error' # API error
    # newamount = payment.discount_ccl(s1, sc_type, sc_code, sc.get_sc_list())
    # newmethod = payment.process_payment(method)
    # if  not newamount[0].startswith('F'):
    #     global p1,c1
    #     c1=''
    #     p1 = p.Payment(amount=newamount[0], 
    #                    method=newmethod, 
    #                    creditcard=c1, 
    #                    specialcode=newamount[1])
    # else: p1 = 'Error' # API error
    return p1

@app.post('/add_credit_card_info')
async def add_credit_card_info(card_number: str, 
                               cardholder_name: str, 
                               expiration_date: str):
    c1 = p.CreditcardInfo(card_number, 
                           cardholder_name, 
                           expiration_date)
    message = c1.check_creditcard(card_number, 
                                  cardholder_name, 
                                  expiration_date)
    if message == 'success':
        p1.set_creditcard(c1)
        p1.set_transaction_id(str(uuid.uuid4()))
        p1.set_status('PAID')
        payment_history.add_pm_history(p1)
    else: c1 = 'error'
    return c1


@app.get('/show_payment_history')
async def show_payment_history():
    return {"payment_history": payment_history.pm_history}

@app.get("/booking")
async def booking():
    global b1
    b1 = Booking(p1, s1)
    return b1

@app.get("/booking_history")
async def booking_history():
    h.add_book(b1)
    return {"data" : h}
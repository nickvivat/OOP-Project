import customtkinter as ctk
from tkinter import *
import json
import datetime
from tkcalendar import Calendar
from DateCal import DateCal
import requests
from SearchRoom import SelectedRoom, RoomCatalog
from Booking import Booking
from User import Admin, Member
import Roominstance as r
import Payment as p

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

m1 = Member('Vivat','Techakosol','65011001@kmitl.ac.th','1234','0915752833')

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        ctk.set_widget_scaling(1.5)
        self.register_window = None
        self.login_window = None
        logo = PhotoImage(file="Picture/Logo.png")
        logo1 = logo.subsample(1, 1)
        ctk.CTkLabel(self, image = logo1, text='').grid(row = 0, column = 1, columnspan=1)

        register_button = ctk.CTkButton(self, text="Register", command=self.register_popup)
        register_button.grid(row=1, column=1, columnspan=1, pady=10)

        login_button = ctk.CTkButton(self, text="Login", command=self.login_popup)
        login_button.grid(row=2, column=1, columnspan=1, pady=10)

        watch_room_button = ctk.CTkButton(self, text="Watch Rooms", command=lambda : controller.show_frame(ShowRoomPage))
        watch_room_button.grid(row=3, column=1, columnspan=1, pady=50)


    def register_popup(self):
        if self.register_window is None or not self.register_window.winfo_exists():
            self.register_window = RegisterPage(self)  # create window if its None or destroyed
        else:
            self.register_window.focus()  # if window exists focus it

    
    def login_popup(self):
        if self.login_window is None or not self.login_window.winfo_exists():
            self.login_window = LoginPage(self)  # create window if its None or destroyed
        else:
            self.login_window.focus()  # if window exists focus it


class LoginPage(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1250x900")
        self.title("Login")
        self.grab_set()
        self.data = {}
        self.data_list = []
        
        self.message_back = ""

        username_label = ctk.CTkLabel(self, text = "Username:", pady = 30)
        username_entry = ctk.CTkEntry(self)
        password_label = ctk.CTkLabel(self, text = "Password:", pady = 30)
        password_entry = ctk.CTkEntry(self, show='*')
        

        username_label.pack(pady=5)
        username_entry.pack(pady=5)
        password_label.pack(pady=5)
        password_entry.pack(pady=5)

        login_button = ctk.CTkButton(self,text= 'Login', command = self.login)
        login_button.pack(pady = 60)

        self.username_entry = username_entry
        self.password_entry = password_entry

        

        self.incorrect_password = ctk.CTkLabel(self, text="Incorrect password", fg_color="red", text_color="white", corner_radius=5)
        self.correct_password = ctk.CTkLabel(self, text="Login success", fg_color="green", text_color="white", corner_radius=5)
        self.not_found_user = ctk.CTkLabel(self,text="Not found user", fg_color="red", text_color="white", corner_radius=5)

    def login(self, message, app):
        if message == "{'message': 'Login successful'}":
            self.correct_password.pack()
            self.destroy()
            app.show_frame(ShowRoomPage)
        elif message == "{'message': 'Incorrect password'}":
            self.incorrect_password.pack()


        url = f"http://127.0.0.1:8000/login?username={self.username_entry.get()}&password={self.password_entry.get()}"
        response = requests.get(url)
        self.message_back = str(response.json())
        print(self.message_back)
        print(type(self.message_back))
    

class RegisterPage(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1250x900")
        self.title("Register")
        self.grab_set()

        self.data = {}
        self.data_list = []
        self.message_back = ""
        
        fname_label = ctk.CTkLabel(self, text = "First Name:")
        fname_entry = ctk.CTkEntry(self, width=200)
        lname_label = ctk.CTkLabel(self, text = "Last Name:")
        lname_entry = ctk.CTkEntry(self, width=200)
        email_label = ctk.CTkLabel(self, text = "Email:")
        email_entry = ctk.CTkEntry(self, width=200)
        password_label = ctk.CTkLabel(self, text = "Password:")
        password_entry = ctk.CTkEntry(self, show="*", width=200)
        confirmed_password_label = ctk.CTkLabel(self, text = "Confirmed Password:")
        confirmed_password_entry = ctk.CTkEntry(self, show="*", width=200)
        phone_label = ctk.CTkLabel(self, text = "Phone Number:")
        phone_entry = ctk.CTkEntry(self, width=200)

        fname_label.pack(pady=5)
        fname_entry.pack(pady=5)
        lname_label.pack(pady=5)
        lname_entry.pack(pady=5)
        email_label.pack(pady=5)
        email_entry.pack(pady=5)
        password_label.pack(pady=5)
        password_entry.pack(pady=5)
        confirmed_password_label.pack(pady=5)
        confirmed_password_entry.pack(pady=5)
        phone_label.pack(pady=5)
        phone_entry.pack(pady=5)

        register_button = ctk.CTkButton(self, text= " Register", command=self.register)
        register_button.pack(pady = 10)

        self.fname_entry = fname_entry
        self.lname_entry = lname_entry
        self.email_entry = email_entry
        self.password_entry = password_entry
        self.confirmed_password_entry = confirmed_password_entry
        self.phone_entry = phone_entry

        self.fname = self.fname_entry.get()
        self.lname = self.lname_entry.get()
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()
        self.phone = self.phone_entry.get()

        self.m1 = Member(self.fname, self.lname, self.email, self.password, self.phone)

        self.error_password_message = ctk.CTkLabel(self, text="Password do not match", fg_color="red", text_color="white", corner_radius=5)
        self.error_fname_message = ctk.CTkLabel(self, text="First name needs to be more than 3 characters", fg_color="red", text_color="white", corner_radius=5)
        self.error_lname_message = ctk.CTkLabel(self, text="Last name needs to be more than 3 characters", fg_color="red", text_color="white", corner_radius=5)
        self.error_phone_message = ctk.CTkLabel(self, text="Phone number should be 10 digits long", fg_color="red", text_color="white", corner_radius=5)
        self.error_email_message = ctk.CTkLabel(self, text="Email already exists", fg_color="red", text_color="white", corner_radius=5)
        

        self.completed_message = ctk.CTkLabel(self, text="Register completed", fg_color="green", text_color="white", corner_radius=5)

    def check_email(self, message, app):

        if message == "{'message': 'Registration successful'}":
            self.error_email_message.destroy()
            if len(self.fname_entry.get()) >= 3 and len(self.lname_entry.get()) >= 3 and self.password_entry.get() == self.confirmed_password_entry.get() and len(self.phone_entry.get()) == 10:
                self.completed_message.pack()
                self.destroy()
                app.show_frame(ShowRoomPage)
        else :
                self.error_email_message.pack(pady=4)


    def register(self):

        self.data = {
            "fname": self.fname_entry.get(),
            "lname": self.lname_entry.get(),
            "email": self.email_entry.get(),
            "password": self.password_entry.get(),
            "confirmed_password": self.confirmed_password_entry.get(),
            "phone_number": self.phone_entry.get()
        }  

        self.m1 = Member(self.fname_entry.get(), self.lname_entry.get(), self.email_entry.get(), self.password_entry.get(), self.phone_entry.get())

        if len(self.fname_entry.get()) < 3:
            self.error_fname_message.pack(pady=4)
        else:
            self.error_fname_message.destroy()
        if len(self.lname_entry.get()) < 3:
            self.error_lname_message.pack(pady=4)
        else:
            self.error_lname_message.destroy()
        if self.password_entry.get() != self.confirmed_password_entry.get():
            self.error_password_message.pack(pady=4)
        else:
            self.error_password_message.destroy()
        
        # RegisterPage.check_email(self.message_back)

        if len(self.phone_entry.get()) != 10:
            self.error_phone_message.pack(pady=4)
        else:
            self.error_phone_message.destroy()
        
        
        url1 = f"http://127.0.0.1:8000/register?fname={self.fname_entry.get()}&lname={self.lname_entry.get()}&email={self.email_entry.get()}&password={self.password_entry.get()}&confirmed_password={self.confirmed_password_entry.get()}&phone_number={self.phone_entry.get()}"
        response1 = requests.post(url1, json = self.data)
        self.message_back = str(response1.json())
        print(self.message_back)
        print(type(self.message_back))
        
        RegisterPage.check_email(self, self.message_back, gui)

        url2 = f"http://127.0.0.1:8000/show_account_list?fname={self.fname_entry.get()}&lname={self.lname_entry.get()}&email={self.email_entry.get()}&password={self.password_entry.get()}&confirmed_password={self.confirmed_password_entry.get()}&phone_number={self.phone_entry.get()}"
        response2 = requests.get(url2 , json = self.data)
        json_data = requests.get(url2).json()
        print(response2.json())
        self.data_list = json.dumps(json_data)
        self.data_list = json.loads(self.data_list)["account_list"] #บรรทัดนี้ใช้เรียกค่าเฉพาะใน dict json ที่ต้องการ
        print(self.data_list)




class ShowRoomPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        ctk.set_widget_scaling(1.7)
        
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.tabview = ctk.CTkTabview(self, width=1000, height=400)
        self.tabview.grid(row=0, column=0, padx=20, pady=5, sticky="nsew", columnspan=4, rowspan=2)
        self.tabview.add("Stays")
        self.tabview.add("Rooms")
        self.tabview.add("Suites")
        self.tabview.tab("Stays").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Rooms").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Suites").grid_columnconfigure(0, weight=1)

        self.Stays_scrollable_frame = ctk.CTkScrollableFrame(master=self.tabview.tab('Stays'), height=320)
        self.Stays_scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10, rowspan=3)
        self.Stays_scrollable_frame.grid_columnconfigure(0, weight=1)

        self.Rooms_scrollable_frame = ctk.CTkScrollableFrame(master=self.tabview.tab('Rooms'), height=320)
        self.Rooms_scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        self.Rooms_scrollable_frame.grid_columnconfigure(0, weight=1)

        self.Suites_scrollable_frame = ctk.CTkScrollableFrame(master=self.tabview.tab('Suites'), height=320)
        self.Suites_scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        self.Suites_scrollable_frame.grid_columnconfigure(0, weight=1)
        
        room1 = PhotoImage(file="Picture/DeluxePre.png")
        room1pic = room1.subsample(1, 1)
        room2 = PhotoImage(file="Picture/ChaoPRoom.png")
        room2pic = room2.subsample(1, 1)
        room3 = PhotoImage(file="Picture/DeluxeBal.png")
        room3pic = room3.subsample(1, 1)
        room4 = PhotoImage(file="Picture/Mandarin.png")
        room4pic = room4.subsample(1, 1)
        room5 = PhotoImage(file="Picture/State.png")
        room5pic = room5.subsample(1, 1)
        room6 = PhotoImage(file="Picture/Junior.png")
        room6pic = room6.subsample(1, 1)
        room7 = PhotoImage(file="Picture/DeluxeOne.png")
        room7pic = room7.subsample(1, 1)
        room8 = PhotoImage(file="Picture/DeluxeTwo.png")
        room8pic = room8.subsample(1, 1)
        room9 = PhotoImage(file="Picture/ChaoPSuite.png")
        room9pic = room9.subsample(1, 1)
        room10 = PhotoImage(file="Picture/Authors.png")
        room10pic = room10.subsample(1, 1)
        room11 = PhotoImage(file="Picture/Deluxe1.png")
        room11pic = room11.subsample(1, 1)
        room12 = PhotoImage(file="Picture/Deluxe2.png")
        room12pic = room12.subsample(1, 1)
        room13 = PhotoImage(file="Picture/Premier1.png")
        room13pic = room13.subsample(1, 1)
        room14 = PhotoImage(file="Picture/Premier2.png")
        room14pic = room14.subsample(1, 1)
        room15 = PhotoImage(file="Picture/Siam.png")
        room15pic = room15.subsample(1, 1)
        room16 = PhotoImage(file="Picture/Ambassador.png")
        room16pic = room16.subsample(1, 1)
        room17 = PhotoImage(file="Picture/Selandia.png")
        room17pic = room17.subsample(1, 1)
        room18 = PhotoImage(file="Picture/Royal.png")
        room18pic = room18.subsample(1, 1)
        room19 = PhotoImage(file="Picture/Oriental.png")
        room19pic = room19.subsample(1, 1)


        room_pics = [room1pic, room2pic, room3pic, room4pic, room5pic, room6pic, room7pic, room8pic, room9pic, room10pic, room11pic, room12pic, room13pic, room14pic, room15pic, room16pic, room17pic, room18pic, room19pic]
        room_names = [r.room_Deluxepremier, r.room_Chaophraya, r.room_Deluxebalcony, r.room_Mandarin, r.room_State, r.room_JuniorterraceSuite, r.room_Deluxe1bedroomSuite, r.room_Deluxe2bedroomSuite, r.room_ChaophrayaSuite, r.room_AuthorsSuite, r.room_Deluxe1bedroomthemeSuite, r.room_Deluxe2bedroomthemeSuite, r.room_Premier1bedroom, r.room_Premier2bedroomSuite, r.room_Siam1bedroomSuite, r.room_Ambassador2bedroomSuite, r.room_Selandia2bedroomSuite, r.room_RoyalSuite, r.room_Oriental2bedroomSuite]

        for i in range(len(room_pics)):
            frame = ctk.CTkFrame(master=self.Stays_scrollable_frame, width=850)
            frame.grid_columnconfigure((1, 2), weight=1)
            frame.grid(row=i, column=0, padx=0, pady=5, sticky=NSEW)
            ctk.CTkLabel(master=frame, image=room_pics[i], text='').grid(row=0, column=0, padx=10)
            text = ctk.CTkTextbox(master=frame, wrap=None)
            text.grid(row=0, column=1, padx=2, columnspan=2, pady=20, sticky=NSEW)
            text.insert('0.0', text=str(room_names[i]))
            text.configure(state='disabled')

        for i in range(5):
            frame = ctk.CTkFrame(master=self.Rooms_scrollable_frame, width=850)
            frame.grid_columnconfigure((1, 2), weight=1)
            frame.grid(row=i, column=0, padx=0, pady=5, sticky=NSEW)
            ctk.CTkLabel(master=frame, image=room_pics[i], text='').grid(row=0, column=0, padx=10)
            text = ctk.CTkTextbox(master=frame, wrap=None)
            text.grid(row=0, column=1, padx=2, columnspan=2, pady=20, sticky=NSEW)
            text.insert('0.0', text=str(room_names[i]))
            text.configure(state='disabled')

        for i in range(len(room_pics) - 5):
            frame = ctk.CTkFrame(master=self.Suites_scrollable_frame, width=850)
            frame.grid_columnconfigure((1, 2), weight=1)
            frame.grid(row=i + 5, column=0, padx=0, pady=5, sticky=NSEW)
            ctk.CTkLabel(master=frame, image=room_pics[i + 5], text='').grid(row=0, column=0, padx=10)
            text = ctk.CTkTextbox(master=frame, wrap=None)
            text.grid(row=0, column=1, padx=2, pady=20, columnspan=2, sticky=NSEW)
            text.insert('0.0', text=str(room_names[i + 5]))
            text.configure(state='disabled')


        self.next_button = ctk.CTkButton(self, text="Next", command=lambda : controller.show_frame(SelectRoomPage))
        self.next_button.grid(row=2, column=3, columnspan=1)


        back_button = ctk.CTkButton(self, text="Back", command=lambda : controller.show_frame(MainPage))
        back_button.grid(row=2, column=0, columnspan=1)



class SelectRoomPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        ctk.set_widget_scaling(1.5)

        self.check_in_label = ctk.CTkLabel(self, text="Check-in Date")
        self.check_in_label.grid(column=0, row=2)

        self.check_in_cal = Calendar(master=self, background='#2f3640',selectmode = 'day', year = 2023, month = 5, day = 2)
        self.check_in_cal.grid(row=1 ,column=0, sticky=NSEW, padx=100)

        self.check_out_label = ctk.CTkLabel(self, text="Check-out Date")
        self.check_out_label.grid(row=2, column=4)
        
        self.check_out_cal = Calendar(master=self, background='#2f3640',selectmode = 'day', year = 2023, month = 5, day = 4)
        self.check_out_cal.grid(row=1 , column=4, sticky=NSEW, padx=100)

        date1_str = self.check_in_cal.get_date()
        date2_str = self.check_out_cal.get_date()
        # Split the date string into month, day, and year components
        month1, day1, year1 = date1_str.split("/")
        month2, day2, year2 = date2_str.split("/")
        # Reformat the date string as "dd-mm-yy"
        self.start_date = f"{day1}-{month1}-20{year1}"
        self.end_date = f"{day2}-{month2}-20{year2}"
        

        room1 = PhotoImage(file="Picture/DeluxePre.png")
        room1pic = room1.subsample(1, 1)
        room2 = PhotoImage(file="Picture/ChaoPRoom.png")
        room2pic = room2.subsample(1, 1)
        room3 = PhotoImage(file="Picture/DeluxeBal.png")
        room3pic = room3.subsample(1, 1)
        room4 = PhotoImage(file="Picture/Mandarin.png")
        room4pic = room4.subsample(1, 1)
        room5 = PhotoImage(file="Picture/State.png")
        room5pic = room5.subsample(1, 1)
        room6 = PhotoImage(file="Picture/Junior.png")
        room6pic = room6.subsample(1, 1)
        room7 = PhotoImage(file="Picture/DeluxeOne.png")
        room7pic = room7.subsample(1, 1)
        room8 = PhotoImage(file="Picture/DeluxeTwo.png")
        room8pic = room8.subsample(1, 1)
        room9 = PhotoImage(file="Picture/ChaoPSuite.png")
        room9pic = room9.subsample(1, 1)
        room10 = PhotoImage(file="Picture/Authors.png")
        room10pic = room10.subsample(1, 1)
        room11 = PhotoImage(file="Picture/Deluxe1.png")
        room11pic = room11.subsample(1, 1)
        room12 = PhotoImage(file="Picture/Deluxe2.png")
        room12pic = room12.subsample(1, 1)
        room13 = PhotoImage(file="Picture/Premier1.png")
        room13pic = room13.subsample(1, 1)
        room14 = PhotoImage(file="Picture/Premier2.png")
        room14pic = room14.subsample(1, 1)
        room15 = PhotoImage(file="Picture/Siam.png")
        room15pic = room15.subsample(1, 1)
        room16 = PhotoImage(file="Picture/Ambassador.png")
        room16pic = room16.subsample(1, 1)
        room17 = PhotoImage(file="Picture/Selandia.png")
        room17pic = room17.subsample(1, 1)
        room18 = PhotoImage(file="Picture/Royal.png")
        room18pic = room18.subsample(1, 1)
        room19 = PhotoImage(file="Picture/Oriental.png")
        room19pic = room19.subsample(1, 1)


        ctk.CTkLabel(self, image = room1pic, text='').grid(row = 1, column = 1, columnspan=3)
        

        def showroom(choice):
            if choice == "Deluxe Premier Room":
                ctk.CTkLabel(self, image = room1pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Chao Phraya Room":
                ctk.CTkLabel(self, image = room2pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Deluxe Balcony Room":
                ctk.CTkLabel(self, image = room3pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Mandarin Room":
                ctk.CTkLabel(self, image = room4pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "State Room":
                ctk.CTkLabel(self, image = room5pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Junior Terrace Suite":
                ctk.CTkLabel(self, image = room6pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Deluxe One-Bedroom Suite":
                ctk.CTkLabel(self, image = room7pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Deluxe Two-Bedroom Suite":
                ctk.CTkLabel(self, image = room8pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Chao Phraya Suite":
                ctk.CTkLabel(self, image = room9pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Authors' Suites":
                ctk.CTkLabel(self, image = room10pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Deluxe One-Bedroom Theme Suite":
                ctk.CTkLabel(self, image = room11pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Deluxe Two-Bedroom Theme Suite":
                ctk.CTkLabel(self, image = room12pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Premier One-Bedroom Suite":
                ctk.CTkLabel(self, image = room13pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Premier Two-Bedroom Suite":
                ctk.CTkLabel(self, image = room14pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Siam One-Bedroom Suite":
                ctk.CTkLabel(self, image = room15pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Ambassador Two-Bedroom Suite":
                ctk.CTkLabel(self, image = room16pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Selandia Two-Bedroom Suite":
                ctk.CTkLabel(self, image = room17pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Royal Suite":
                ctk.CTkLabel(self, image = room18pic, text='').grid(row = 1, column = 1, columnspan=3)
            elif choice == "Oriental Two-Bedroom Suite":
                ctk.CTkLabel(self, image = room19pic, text='').grid(row = 1, column = 1, columnspan=3)

        # create labels and entry fields for each parameter
        self.room_type = ctk.CTkOptionMenu(self, values=["Deluxe Premier Room",
                                                            "Chao Phraya Room",
                                                            "Deluxe Balcony Room",
                                                            "Mandarin Room",
                                                            "State Room",
                                                            "Junior Terrace Suite",
                                                            "Deluxe One-Bedroom Suite",
                                                            "Deluxe Two-Bedroom Suite",
                                                            "Chao Phraya Suite",
                                                            "Authors' Suites",
                                                            "Deluxe One-Bedroom Theme Suite",
                                                            "Deluxe Two-Bedroom Theme Suite",
                                                            "Premier One-Bedroom Suite",
                                                            "Premier Two-Bedroom Suite",
                                                            "Siam One-Bedroom Suite",
                                                            "Ambassador Two-Bedroom Suite",
                                                            "Selandia Two-Bedroom Suite",
                                                            "Royal Suite",
                                                            "Oriental Two-Bedroom Suite"], 
                                                            dropdown_fg_color=("#487eb0"), 
                                                            width=250, 
                                                            dynamic_resizing=False,
                                                            command=showroom)
        self.room_type.grid(pady = 10, column=1, columnspan=3)
        self.type = self.room_type.get()
        self.s1 = SelectedRoom(self.start_date, self.end_date, self.type, Catalog)

        logo = PhotoImage(file="Picture/Logo.png")
        logo1 = logo.subsample(1, 1)
        ctk.CTkLabel(self, image = logo1, text='').grid(row = 0, column = 1, columnspan=3)

        # create a button to submit the request
        submit_button = ctk.CTkButton(self, text="Submit", command=self.select_room)
        submit_button.grid(pady=0, column=1, columnspan=3)

        next_button = ctk.CTkButton(self, text="Next", command=lambda : controller.show_frame(PaymentPage))
        next_button.grid(column=1,row=5, columnspan=3, pady=10)
    

        # create a label to display error messages
        self.error_message = ctk.CTkLabel(self, text="Invalid Input", fg_color="red", text_color="white", corner_radius=5)
        self.completed_message = ctk.CTkLabel(self, text="Room Selected", fg_color="green", text_color="white", corner_radius=5)

    def select_room(self):
        if DateCal().date_diff(self.start_date, self.end_date) > 0:
            self.completed_message.grid(column=1,row=6, columnspan=3, pady=10)
            # construct the URL with the query parameters from the entry fields
            url = f"http://localhost:8000/select_room?start_date={self.start_date}&end_date={self.end_date}&room_type={str(self.room_type.get())}"
            # send the request and get the response
            response = requests.get(url)
            self.s1 = SelectedRoom(self.start_date, self.end_date, self.type, Catalog)
            # print the response to the console for debugging purposes
            print(response.json())
            
        else:
            self.error_message.grid(column=1, row=5, columnspan=3, pady=10)


sc = p.SpecialCode()

sc1 = p.SpecialCode('iata number', 'EASY','5')
sc2 = p.SpecialCode('promo code', 'HARD','10')
sc.add_sc_list(sc1)
sc.add_sc_list(sc2)

class PaymentPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.selected_room = SelectRoomPage(parent, controller).s1
        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)
        # create labels and entry fields for each parameter
        logo = PhotoImage(file="Picture/Logo.png")
        logo1 = logo.subsample(1, 1)
        ctk.CTkLabel(self, image = logo1, text='').grid(row = 0, column = 0, columnspan=1)
        self.amount = SelectRoomPage(parent, controller).s1.get_total_cost()
        self.amount_label = ctk.CTkLabel(self, text=f"Amount: {SelectRoomPage(parent, controller).s1.get_total_cost()}")
        self.special_code_type = ctk.CTkOptionMenu(self, values=["iata number",
                                                        "promo code",
                                                        "group code"], 
                                                            dropdown_fg_color=("#487eb0"), 
                                                            width=250, 
                                                            dynamic_resizing=False)
        self.special_code_type.grid(column=0, row=1, pady=30, columnspan=1)
        special_code_label = ctk.CTkLabel(self, text="Special code:")
        special_code_entry = ctk.CTkEntry(self)

        method_label = ctk.CTkLabel(self, text="Method:")
        method_label.grid()

        confirm_button = ctk.CTkButton(self, text="Confirm")
        confirm_button.grid(column=3, row=1, pady=10)

        self.method_type = ctk.CTkOptionMenu(self, values=["credit card"], 
                                                            dropdown_fg_color=("#487eb0"), 
                                                            width=250, 
                                                            dynamic_resizing=False)
        self.method_type.grid()
        
        card_number_label = ctk.CTkLabel(self, text="Card number:")
        card_number_entry = ctk.CTkEntry(self)
        cardholder_name_label = ctk.CTkLabel(self, text="Card holder name:")
        cardholder_name_entry = ctk.CTkEntry(self)
        exp_label = ctk.CTkLabel(self, text="Expiration date:")
        exp_entry = ctk.CTkEntry(self)
        

        
        # add the labels and entry fields to the GUI
        self.amount_label.grid(column=1, row=0, pady=5)
        self.special_code_type.grid(column=1, row=1, pady=10)
        special_code_label.grid(column=0, row=1, pady=10)
        special_code_entry.grid(column=2, row=1, pady=10, columnspan=1, sticky=EW)
        self.method_type.grid(column=1, row=2, pady=10)
        
        card_number_label.grid(column=0, row=3, pady=10)
        card_number_entry.grid(column=1, row=3, pady=10, sticky=EW)
        cardholder_name_label.grid(column=0, row=4, pady=10)
        cardholder_name_entry.grid(column=1, row=4, pady=10, sticky=EW)
        exp_label.grid(column=0, row=5, pady=10)
        exp_entry.grid(column=1, row=5, pady=10, sticky=EW)
        
        # create a button to submit the request
        submit_button = ctk.CTkButton(self, text="Submit", command=self.payment)
        submit_button.grid(column=1, row=6, pady=10)

        # set the entry fields as instance variables to access them in other methods
        self.card_number_entry = card_number_entry
        self.cardholder_name_entry = cardholder_name_entry
        self.exp_entry = exp_entry
        self.special_code_entry = special_code_entry
        
        # create a label to display error messages
        self.empty_message = ctk.CTkLabel(self, 
                                          text="please fill the box", 
                                          fg_color="red", 
                                          text_color="white", 
                                          corner_radius=5)
        self.number_error_message = ctk.CTkLabel(self, 
                                                 text="incorrect card number", 
                                                 fg_color="red", 
                                                 text_color="white", 
                                                 corner_radius=5)
        self.expired_error_message = ctk.CTkLabel(self, 
                                                  text="This card is expired or empty", 
                                                  fg_color="red", 
                                                  text_color="white", 
                                                  corner_radius=5)
        self.exp_error_message = ctk.CTkLabel(self, 
                                              text="Invalid or empyty exp", 
                                              fg_color="red", 
                                              text_color="white", 
                                              corner_radius=5)
        self.sc_error_message = ctk.CTkLabel(self, 
                                             text="Invalid code", 
                                             fg_color="red", 
                                             text_color="white", 
                                             corner_radius=5)
        self.completed_message = ctk.CTkLabel(self, 
                                              text="Register completed", 
                                              fg_color="green", 
                                              text_color="white", 
                                              corner_radius=5)
        
        self.sc_type = self.special_code_type.get()
        self.sc_code = self.special_code_entry.get()
        self.info = SelectRoomPage(parent, controller).s1

    
    def payment(self):
        self.data = {
            "sc_type": self.special_code_type.get(),
            "sc_code": self.special_code_entry.get(),
            "method": self.method_type.get(),
            "card_number": self.card_number_entry.get(),
            "cardholder_name": self.cardholder_name_entry.get(),
            "expiration_date": self.exp_entry.get()
        }
        gui.show_frame(BookingPage)
        # check number of card number
        if len(self.card_number_entry.get()) != 16 or self.card_number_entry.get() == '':
            self.number_error_message.grid(column=1, row=7, pady=10)
            # return
        else:
            if self.number_error_message.winfo_exists():
                self.number_error_message.destroy()
         
        # check expiration date   
        try:
            # Convert expiration date string to datetime object
            exp_date = datetime.datetime.strptime(self.exp_entry.get(), '%m/%y')
        except ValueError:
            self.exp_error_message.grid(column=1, row=7, pady=10)
            # return
        else:
            if self.exp_error_message.winfo_exists():
                self.exp_error_message.destroy()

s1 = SelectedRoom('1-1-2023', '4-1-2023', 'Deluxe Balcony Room', Catalog)
p1 = p.Payment(m1, s1)

class BookingPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(1, weight=1)
        ctk.set_widget_scaling(1.5)
        
        s1 = SelectRoomPage(parent, controller).s1

        self.b1 = Booking(p1, s1)
        booking_frame = ctk.CTkFrame(self)
        booking_frame.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=20)

        text_box = ctk.CTkTextbox(master=booking_frame)
        text_box.grid(row=0, column=0, columnspan=3)
        text_box.insert('0.0' ,text=self.b1.__str__())
        
        logo = PhotoImage(file="Picture/Logo.png")
        logo1 = logo.subsample(1, 1)
        ctk.CTkLabel(self, image = logo1, text='').grid(row = 0, column = 1, columnspan=1)


        next_button = ctk.CTkButton(self, text="Next", command=lambda : controller.show_frame(MainPage))
        next_button.grid(row=2, column=2, columnspan=1, pady=10)


class App(ctk.CTk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("Room Catalog")
        self.minsize(1250 ,780)
        # creating a container
        container = ctk.CTkFrame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (ShowRoomPage, SelectRoomPage, MainPage, PaymentPage, BookingPage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(MainPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    

if __name__ == "__main__":
    gui = App()
    gui.mainloop()

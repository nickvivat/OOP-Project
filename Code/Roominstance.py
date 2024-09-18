from Room import Room
import textwrap


# available_rooms = [room for room in room_Chaophraya_list if room.is_available('1-1-2023', '4-1-2023')]
# print(available_rooms[0].reserve('1-1-2023', '4-1-2023'))
# print(available_rooms[0].reserve('2-1-2023', '4-1-2023'))
# print(available_rooms[0].reserve('5-1-2023', '9-1-2023'))

# print(available_rooms[0].get_reservations())
    

room_Deluxepremier = Room(name = "Deluxe Premier Room",
                           type = "Room",
                           room_price = 19500,
                           room_number = 0,
                           bed_type = "King Bed or Twin Beds",
                           size = "43SQM / 463SQF",
                           toilet_type = "Japanese Toilets",
                           complimentary = "Complimentary",
                           speaker = "Bluetooth Speaker",
                           bathrobes = "Bathrobes",
                           details = "These 43sqm rooms are located in the River Wing and each boast a large sofa to relax and enjoy river and pool views. Décor is inspired by life on the Chao Phraya river with wooden floors and Thai touches such as teak furniture and beautiful Thai silk fabrics, while a selection of prints from the hotels rich collection of artworks adorn the walls. Both king and twin beds are available.",
                           highlights = "River View, Bathtub & Walk-In Shower, 24-Hour Butler Service, Corner Sofa",
                           description = "Large rooms with sofa and sitting area to relax, offer wooden floors and nature inspired rugs and furnishing with a Thai touch giving a unique experience in a resort style ambiance with views of the river and city."
                           )

room_Deluxepremier_list = [Room(name = "Deluxe Premier Room",
                           type = "Room",
                           room_price = 19500,
                           room_number = i+101,
                           bed_type = "King Bed or Twin Beds",
                           size = "43SQM / 463SQF",
                           toilet_type = "Japanese Toilets",
                           complimentary = "Complimentary",
                           speaker = "Bluetooth Speaker",
                           bathrobes = "Bathrobes",
                           details = "These 43sqm rooms are located in the River Wing and each boast a large sofa to relax and enjoy river and pool views. Décor is inspired by life on the Chao Phraya river with wooden floors and Thai touches such as teak furniture and beautiful Thai silk fabrics, while a selection of prints from the hotels rich collection of artworks adorn the walls. Both king and twin beds are available.",
                           highlights = "River View, Bathtub & Walk-In Shower, 24-Hour Butler Service, Corner Sofa",
                           description = "Large rooms with sofa and sitting area to relax, offer wooden floors and nature inspired rugs and furnishing with a Thai touch giving a unique experience in a resort style ambiance with views of the river and city.")
                           for i in range(20)]


room_Chaophraya = Room(name = "Chao Phraya Room",
                        type = "Room",
                        room_price = 21000,
                        room_number = 0,
                        bed_type = "King Bed",
                        size = "35SQM / 377SQF",
                        toilet_type = "Japanese Toilets",
                        complimentary = "Complimentary",
                        speaker = "Bluetooth Speaker",
                        bathrobes = "Bathrobes",
                        details = "Located in the Garden Wing, these rooms, with either a flat or split-level layout, offer a residential ambience. The rooms are the epitome of classic elegance with a colonial inspired contemporary interior design that reflects the hotel unique heritage and Thai culture. The 35sqm rooms also enjoy floor-to-ceiling windows overlooking the river and garden.",
                        highlights = "Located in the Garden Wing, Pantry with Large Refrigerator, Living Area, 24-Hour Butler Service",
                        description = "This luxurious room has an entrance area leading to both a spacious and comfortable bedroom and a separate living area with a comfortable sofa."
                        )

room_Chaophraya_list = [Room(name="Chao Phraya Room",
                             type="Room",
                             room_price = 21000,
                             room_number=i+121,
                             bed_type="King Bed",
                             size="35SQM / 377SQF",
                             toilet_type="Japanese Toilets",
                             complimentary="Complimentary",
                             speaker="Bluetooth Speaker",
                             bathrobes="Bathrobes",
                             details="Located in the Garden Wing, these rooms, with either a flat or split-level layout, offer a residential ambience. The rooms are the epitome of classic elegance with a colonial inspired contemporary interior design that reflects the hotel unique heritage and Thai culture. The 35sqm rooms also enjoy floor-to-ceiling windows overlooking the river and garden.",
                             highlights="Located in the Garden Wing, Pantry with Large Refrigerator, Living Area, 24-Hour Butler Service",
                             description="This luxurious room has an entrance area leading to both a spacious and comfortable bedroom and a separate living area with a comfortable sofa.")
                        for i in range(20)]


room_Deluxebalcony = Room(name = "Deluxe Balcony Room",
                           type = "Room",
                           room_price = 22500,
                           room_number = 0,
                           bed_type = "King Bed",
                           size = "37SQM / 397SQF",
                           toilet_type = "Japanese Toilets",
                           complimentary = "Complimentary",
                           speaker = "Bluetooth Speaker",
                           bathrobes = "Bathrobes",
                           details = "Each of these rooms boasts a private 6sqm balcony on which to relax and enjoy views of the bustling river life and the pool. With floor-to-ceiling windows, wooden floors, rugs and furnishings inspired by nature, soft natural tones and Thai décor, these 37sqm rooms add to the overall resort-style ambience.",
                           highlights = "Floor-To-Ceiling Windows, Balcony with Seating, Bathtub & Walk-In Shower, 24-Hour Butler Service",
                           description = "Elegant rooms with wooden floors, nature inspired rugs and furnishings with a private balcony and seating area. The rooms offer a Thai touch, giving a unique experience in a resort-style ambience with pool and river views.",
                           )

room_Deluxebalcony_list = [Room(name = "Deluxe Balcony Room",
                           type = "Room",
                           room_price = 22500,
                           room_number = i+141,
                           bed_type = "King Bed",
                           size = "37SQM / 397SQF",
                           toilet_type = "Japanese Toilets",
                           complimentary = "Complimentary",
                           speaker = "Bluetooth Speaker",
                           bathrobes = "Bathrobes",
                           details = "Each of these rooms boasts a private 6sqm balcony on which to relax and enjoy views of the bustling river life and the pool. With floor-to-ceiling windows, wooden floors, rugs and furnishings inspired by nature, soft natural tones and Thai décor, these 37sqm rooms add to the overall resort-style ambience.",
                           highlights = "Floor-To-Ceiling Windows, Balcony with Seating, Bathtub & Walk-In Shower, 24-Hour Butler Service",
                           description = "Elegant rooms with wooden floors, nature inspired rugs and furnishings with a private balcony and seating area. The rooms offer a Thai touch, giving a unique experience in a resort-style ambience with pool and river views.",)
                           for i in range(20)]


room_Mandarin = Room(name = "Mandarin Room",
                     type = "Room",
                     room_price = 26500,
                     room_number = 0,
                     bed_type = "King Bed",
                     size = "63SQM / 677SQF",
                     toilet_type = "Bath tub and Japanese toilet",
                     complimentary = "Complimentary",
                     speaker = "Bluetooth Speaker",
                     bathrobes = "Bathrobes",
                     details = "The ideal choice for guests looking for more space, these large 63sqm rooms incorporate a spacious seating area with a sofa; dining area overlooking both the city and river through floor-to-ceiling windows. The décor is light with soothing aqua and gold tones balanced with a selection of furnishings upholstered in the finest Thai silks, along with a king-size bed swathed in luxurious linen. The room also features a vanity area and walk-in closet.",
                     highlights = "Balcony with Seating, Spacious Living with Sofa, Dining Area For 2, 24-Hour Butler Service, Walk-in Closet",
                     description = "These rooms feature floor-to-ceiling windows that open out to a balcony with views across the city and river. The bedroom incorporates a spacious seating area with a large comfortable sofa and a dining table."
                    )

room_Mandarin_list = [Room(name = "Mandarin Room",
                     type = "Room",
                     room_price = 26500,
                     room_number = i+161,
                     bed_type = "King Bed",
                     size = "63SQM / 677SQF",
                     toilet_type = "Bath tub and Japanese toilet",
                     complimentary = "Complimentary",
                     speaker = "Bluetooth Speaker",
                     bathrobes = "Bathrobes",
                     details = "The ideal choice for guests looking for more space, these large 63sqm rooms incorporate a spacious seating area with a sofa; dining area overlooking both the city and river through floor-to-ceiling windows. The décor is light with soothing aqua and gold tones balanced with a selection of furnishings upholstered in the finest Thai silks, along with a king-size bed swathed in luxurious linen. The room also features a vanity area and walk-in closet.",
                     highlights = "Balcony with Seating, Spacious Living with Sofa, Dining Area For 2, 24-Hour Butler Service, Walk-in Closet",
                     description = "These rooms feature floor-to-ceiling windows that open out to a balcony with views across the city and river. The bedroom incorporates a spacious seating area with a large comfortable sofa and a dining table."
                    )for i in range(20)]

room_State = Room(name = "State Room",
                   type = "Room",
                   room_price = 37000,
                   room_number = 0,
                   bed_type = "King Bed or Twin Beds",
                   size = "61SQM / 657SQF",
                   toilet_type = "Bath tub and Japanese toilet",
                   complimentary = "Complimentary",
                   speaker = "Bluetooth Speaker",
                   bathrobes = "Bathrobes",
                   details = "Entered via a teak paneled hallway, these rooms are richly decorated in traditional Thai style with dark wood furnishings and brightly coloured Jim Thompson silks. Within the bedroom of these 61sqm rooms there is a seating area furnished with a comfortable sofa and dining table. Large floor-to-ceiling windows open on to a spacious balcony from where guests can enjoy wonderful panoramic river views.",
                   highlights = "Spacious Balcony with River Views, Sumptous Teak Wood Panelling and Floors, Living Area with Sofa, Dining Area For 2",
                   description = "This luxurious rooms offers an amazing Thai experience, the décor features colourful Thai silks by Jim Thompson and teak wood panelling & wooden floors. The rooms are directly river facing & offer dramatic views from the balcony."
                   )

room_State_list = [Room(name = "State Room",
                   type = "Room",
                   room_price = 37000,
                   room_number = i+181,
                   bed_type = "King Bed or Twin Beds",
                   size = "61SQM / 657SQF",
                   toilet_type = "Bath tub and Japanese toilet",
                   complimentary = "Complimentary",
                   speaker = "Bluetooth Speaker",
                   bathrobes = "Bathrobes",
                   details = "Entered via a teak paneled hallway, these rooms are richly decorated in traditional Thai style with dark wood furnishings and brightly coloured Jim Thompson silks. Within the bedroom of these 61sqm rooms there is a seating area furnished with a comfortable sofa and dining table. Large floor-to-ceiling windows open on to a spacious balcony from where guests can enjoy wonderful panoramic river views.",
                   highlights = "Spacious Balcony with River Views, Sumptous Teak Wood Panelling and Floors, Living Area with Sofa, Dining Area For 2",
                   description = "This luxurious rooms offers an amazing Thai experience, the décor features colourful Thai silks by Jim Thompson and teak wood panelling & wooden floors. The rooms are directly river facing & offer dramatic views from the balcony."
                   )for i in range(20)]

room_JuniorterraceSuite = Room(name = "Junior Terrace Suite",
                                type = "Suite",
                                room_price = 37400, 
                                room_number = 0,
                                bed_type = "King Bed",
                                size = "97SQM / 1,043SQF",
                                toilet_type = "Bath tub and Japanese toilet",
                                complimentary = "complimentary",
                                speaker = "Bluetooth Speaker",
                                bathrobes = "Bathrobes",
                                details = "Ideal for long-staying guests, these large 97sqm junior suites feature a stunning 17sqm terrace that overlooks the river and city. The suite combines a spacious open-plan living area with a large sofa and armchairs, a writing desk and a dining table seating up to five. It is decorated with wooden floors throughout and accented with rugs and prints from the hotel's art collection inspired by the Chao Phraya River.",
                                highlights = "Outdoor Terrace with Seating, Dining Area For 5, Walk-in Closet, 24-Hour Butler Service",
                                description = "This large junior suite is ideal for long-staying guests looking for a large open plan space with a combined sitting and dining area. It features a wonderful terrace of 17sqm/188sqf and a working desk."
                                )

room_JuniorterraceSuite_list = [Room(name = "Junior Terrace Suite",
                                type = "Suite",
                                room_price = 37400, 
                                room_number = i+201,
                                bed_type = "King Bed",
                                size = "97SQM / 1,043SQF",
                                toilet_type = "Bath tub and Japanese toilet",
                                complimentary = "complimentary",
                                speaker = "Bluetooth Speaker",
                                bathrobes = "Bathrobes",
                                details = "Ideal for long-staying guests, these large 97sqm junior suites feature a stunning 17sqm terrace that overlooks the river and city. The suite combines a spacious open-plan living area with a large sofa and armchairs, a writing desk and a dining table seating up to five. It is decorated with wooden floors throughout and accented with rugs and prints from the hotel's art collection inspired by the Chao Phraya River.",
                                highlights = "Outdoor Terrace with Seating, Dining Area For 5, Walk-in Closet, 24-Hour Butler Service",
                                description = "This large junior suite is ideal for long-staying guests looking for a large open plan space with a combined sitting and dining area. It features a wonderful terrace of 17sqm/188sqf and a working desk."
                                )for i in range(10)]

room_Deluxe1bedroomSuite = Room(name = "Deluxe One-Bedroom Suite",
                                  type = "Suite",
                                  room_price = 41650,
                                  room_number = 0,
                                  bed_type = "King Bed or Twin Beds",
                                  size = "83SQM / 892SQF",
                                  toilet_type = "Japanese Toilets",
                                  complimentary = "Complimentary",
                                  speaker = "Bose Sound Bar",
                                  bathrobes = "Silk Kimonos",
                                  details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                  highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                  description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet.",
                                  )

room_Deluxe1bedroomSuite_list = [Room(name = "Deluxe One-Bedroom Suite",
                                  type = "Suite",
                                  room_price = 41650,
                                  room_number = i+211,
                                  bed_type = "King Bed or Twin Beds",
                                  size = "83SQM / 892SQF",
                                  toilet_type = "Japanese Toilets",
                                  complimentary = "Complimentary",
                                  speaker = "Bose Sound Bar",
                                  bathrobes = "Silk Kimonos",
                                  details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                  highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                  description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet.",
                                  ) for i in range(10)]

room_Deluxe2bedroomSuite = Room(name = "Deluxe Two-Bedroom Suite",
                                  type = "Suite",
                                  room_price = 58225,
                                  room_number = 0,
                                  bed_type = "King and Twin Beds or Twin and Twin Beds",
                                  size = "125SQM / 1,344SQF",
                                  toilet_type = "Japanese Toilets",
                                  complimentary = "Complimentary",
                                  speaker = "Bose Sound Bar",
                                  bathrobes = "Silk Kimonos",
                                  details = "These 125sqm two-bedroom Deluxe Suites are ideal for families and overlook the pool and river. Guests can relax and unwind on their private balcony with a seating area, or in the living area that offers separate sitting and dining sections for family and friends to enjoy. The master bedroom has a dressing and sitting area with a large walk-in closet, while the bathroom features Italian marble and a separate shower and bath.",
                                  highlights = "Located on High Floor of River Wing, Balcony with Seating, Interconntecting Room, 24-Hour Butler Service",
                                  description = "An ideal suite for families, this two bedroom suite overlooking the pool and the river, features a private balcony with a sitting area. The living area offers separate sitting and dining areas perfect to relax and unwind"
                                  )

room_Deluxe2bedroomSuite_list = [Room(name = "Deluxe Two-Bedroom Suite",
                                  type = "Suite",
                                  room_price = 58225,
                                  room_number = i+221,
                                  bed_type = "King and Twin Beds or Twin and Twin Beds",
                                  size = "125SQM / 1,344SQF",
                                  toilet_type = "Japanese Toilets",
                                  complimentary = "Complimentary",
                                  speaker = "Bose Sound Bar",
                                  bathrobes = "Silk Kimonos",
                                  details = "These 125sqm two-bedroom Deluxe Suites are ideal for families and overlook the pool and river. Guests can relax and unwind on their private balcony with a seating area, or in the living area that offers separate sitting and dining sections for family and friends to enjoy. The master bedroom has a dressing and sitting area with a large walk-in closet, while the bathroom features Italian marble and a separate shower and bath.",
                                  highlights = "Located on High Floor of River Wing, Balcony with Seating, Interconntecting Room, 24-Hour Butler Service",
                                  description = "An ideal suite for families, this two bedroom suite overlooking the pool and the river, features a private balcony with a sitting area. The living area offers separate sitting and dining areas perfect to relax and unwind"
                                  )for i in range(10)]

room_ChaophrayaSuite = Room(name = "Chao Phraya Suite",
                             type = "Suite",
                             room_price = 45050,
                             room_number = 0,
                             bed_type = "King Bed",
                             size = "83SQM / 892SQF",
                             toilet_type = "Japanese Toilets",
                             complimentary = "Complimentary",
                             speaker = "Bose Sound Bar",
                             bathrobes = "Silk Kimonos",
                             details = "These spacious 83sqm suites, located in the Garden Wing, have either a flat or split-level layout, floor-to-ceiling windows and a balcony overlooking the river and gardens. The suites feature a colonial-inspired contemporary interior design to reflect the hotel's unique heritage and Thai culture. A separate lounge with dining area is offered alongside a luxurious bedroom and large marble bathroom with separate bathtub, walk-in shower and a walk-in closet",
                             highlights = "Located in the Garden Wing, Flat or Split-level Layout, Dining Room & Lounge Area, Pantry with Large Refrigerator, 24-Hour Butler Service",
                             description = "Floor-to-ceiling windows overlook the river and our gardens. The elegant bedroom features a large marble bathroom with separate bath, a walk-in shower and a walk-in wardrobe. There is also a living area, dining room and balcony."
                            )

room_ChaophrayaSuite_list = [Room(name = "Chao Phraya Suite",
                             type = "Suite",
                             room_price = 45050,
                             room_number = i+231,
                             bed_type = "King Bed",
                             size = "83SQM / 892SQF",
                             toilet_type = "Japanese Toilets",
                             complimentary = "Complimentary",
                             speaker = "Bose Sound Bar",
                             bathrobes = "Silk Kimonos",
                             details = "These spacious 83sqm suites, located in the Garden Wing, have either a flat or split-level layout, floor-to-ceiling windows and a balcony overlooking the river and gardens. The suites feature a colonial-inspired contemporary interior design to reflect the hotel's unique heritage and Thai culture. A separate lounge with dining area is offered alongside a luxurious bedroom and large marble bathroom with separate bathtub, walk-in shower and a walk-in closet",
                             highlights = "Located in the Garden Wing, Flat or Split-level Layout, Dining Room & Lounge Area, Pantry with Large Refrigerator, 24-Hour Butler Service",
                             description = "Floor-to-ceiling windows overlook the river and our gardens. The elegant bedroom features a large marble bathroom with separate bath, a walk-in shower and a walk-in wardrobe. There is also a living area, dining room and balcony."
                            )for i in range(10)]

room_AuthorsSuite = Room(name = "Authors' Suites",
                          type = "Suite",
                          room_price = 49300,
                          room_number = 0,
                          bed_type = "King Bed or Twin Beds",
                          size = "101SQM / 1,861SQF",
                          toilet_type = "Japanese Toilets",
                          complimentary = "Complimentary",
                          speaker = "Bose Sound Bar",
                          bathrobes = "Silk Kimonos",
                          details = "Individually designed, each 101sqm suite pays tribute in name and ambience, from colour scheme and antique decorations, to one of the celebrated authors who have stayed here. Located in the River Wing, all feature floor-to-ceiling windows and a balcony overlooking the river - perfect for watching river life. Each suite has a spacious sitting room, a bedroom that features a dressing and seating area and a large Italian marble bathroom and walk-in closet.",
                          highlights = "Balcony with River Views, Unique Contemporary Decoration, Spacious Living Area, 24-Hour Butler Service",
                          description = "Located in the River Wing, these suites are tributes to some of the great literary figures that have stayed with us. All feature floor-to-ceiling windows, a balcony, spacious sitting room, a large bathroom and powder room."
                        )

room_AuthorsSuite_list = [Room(name = "Authors' Suites",
                          type = "Suite",
                          room_price = 49300,
                          room_number = i+241,
                          bed_type = "King Bed or Twin Beds",
                          size = "101SQM / 1,861SQF",
                          toilet_type = "Japanese Toilets",
                          complimentary = "Complimentary",
                          speaker = "Bose Sound Bar",
                          bathrobes = "Silk Kimonos",
                          details = "Individually designed, each 101sqm suite pays tribute in name and ambience, from colour scheme and antique decorations, to one of the celebrated authors who have stayed here. Located in the River Wing, all feature floor-to-ceiling windows and a balcony overlooking the river - perfect for watching river life. Each suite has a spacious sitting room, a bedroom that features a dressing and seating area and a large Italian marble bathroom and walk-in closet.",
                          highlights = "Balcony with River Views, Unique Contemporary Decoration, Spacious Living Area, 24-Hour Butler Service",
                          description = "Located in the River Wing, these suites are tributes to some of the great literary figures that have stayed with us. All feature floor-to-ceiling windows, a balcony, spacious sitting room, a large bathroom and powder room."
                        )for i in range(10)]


room_Deluxe1bedroomthemeSuite = Room(name = "Deluxe One-Bedroom Theme Suite",
                                      type = "Suite",
                                      room_price = 49300,
                                      room_number = 0,
                                      bed_type = "King Bed or Twin Beds",
                                      size = "83SQM / 892SQF",
                                      toilet_type = "Japanese Toilets",
                                      complimentary = "Complimentary",
                                      speaker = "Bose Sound Bar",
                                      bathrobes = "Silk Kimonos",
                                      details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                      highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                      description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet.",
                                      )

room_Deluxe1bedroomthemeSuite_list = [Room(name = "Deluxe One-Bedroom Theme Suite",
                                      type = "Suite",
                                      room_price = 49300,
                                      room_number = i+251,
                                      bed_type = "King Bed or Twin Beds",
                                      size = "83SQM / 892SQF",
                                      toilet_type = "Japanese Toilets",
                                      complimentary = "Complimentary",
                                      speaker = "Bose Sound Bar",
                                      bathrobes = "Silk Kimonos",
                                      details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                      highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                      description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet.",
                                      )for i in range(10)]

room_Deluxe2bedroomthemeSuite = Room(name = "Deluxe Two-Bedroom Theme Suite",
                                      type = "Suite",
                                      room_price = 65875,
                                      room_number = 0,
                                      bed_type = "King and Twin Beds or Twin and Twin Beds",
                                      size = "125SQM / 1,344SQF",
                                      toilet_type = "Japanese Toilets",
                                      complimentary = "Complimentary",
                                      speaker = "Bose Sound Bar",
                                      bathrobes = "Silk Kimonos",
                                      details = "These 125sqm two-bedroom Deluxe Suites are ideal for families and overlook the pool and river. Guests can relax and unwind on their private balcony with a seating area, or in the living area that offers separate sitting and dining sections for family and friends to enjoy. The master bedroom has a dressing and sitting area with a large walk-in closet, while the bathroom features Italian marble and a separate shower and bath.",
                                      highlights = "Located on High Floor of River Wing, Balcony with Seating, Interconntecting Room, 24-Hour Butler Service",
                                      description = "An ideal suite for families, this two bedroom suite overlooking the pool and the river, features a private balcony with a sitting area. The living area offers separate sitting and dining areas perfect to relax and unwind"
                                      )

room_Deluxe2bedroomthemeSuite_list = [Room(name = "Deluxe Two-Bedroom Theme Suite",
                                      type = "Suite",
                                      room_price = 65875,
                                      room_number = i+261,
                                      bed_type = "King and Twin Beds or Twin and Twin Beds",
                                      size = "125SQM / 1,344SQF",
                                      toilet_type = "Japanese Toilets",
                                      complimentary = "Complimentary",
                                      speaker = "Bose Sound Bar",
                                      bathrobes = "Silk Kimonos",
                                      details = "These 125sqm two-bedroom Deluxe Suites are ideal for families and overlook the pool and river. Guests can relax and unwind on their private balcony with a seating area, or in the living area that offers separate sitting and dining sections for family and friends to enjoy. The master bedroom has a dressing and sitting area with a large walk-in closet, while the bathroom features Italian marble and a separate shower and bath.",
                                      highlights = "Located on High Floor of River Wing, Balcony with Seating, Interconntecting Room, 24-Hour Butler Service",
                                      description = "An ideal suite for families, this two bedroom suite overlooking the pool and the river, features a private balcony with a sitting area. The living area offers separate sitting and dining areas perfect to relax and unwind"
                                      )for i in range(10)]

room_Premier1bedroom = Room(name = "Premier One-Bedroom Suite",
                              type = "Suite",
                              room_price = 51000,
                              room_number = 0,
                              bed_type = "King Bed or Twin Beds",
                              size = "108SQM / 1,163SQF",
                              toilet_type = "Japanese Toilets",
                              complimentary ="Complimentary",
                              speaker = "Bose Sound Bar",
                              bathrobes = "Silk Kimonos",
                              details = "These spacious 108sqm suites overlook the French Ambassador's residence, with breath-taking views of the Chao Phraya river, a private balcony and sitting area. Elegantly decorated, the Premier Suites have wooden floors in the living and dining areas, complemented perfectly by rugs and prints from the hotel's art collection that are inspired by the River of Kings. The bedroom features a subtle orchid theme, a dressing and sitting area and a walk-in closet.",
                              highlights = "Balcony with Seating, Dining Area For 5, Spacious Living Room and Walk-in Closet, High Bar-style Table, 24-Hour Butler Service",
                              description = "This luxurious suite has an entrance area leading to a spacious sitting area & desk with a separate dining area for 5 people. It has a private balcony with seating area. The specious bedroom has a dressing table and sitting area."
                              )


room_Premier1bedroom_list = [Room(name = "Premier One-Bedroom Suite",
                              type = "Suite",
                              room_price = 51000,
                              room_number = i+271,
                              bed_type = "King Bed or Twin Beds",
                              size = "108SQM / 1,163SQF",
                              toilet_type = "Japanese Toilets",
                              complimentary ="Complimentary",
                              speaker = "Bose Sound Bar",
                              bathrobes = "Silk Kimonos",
                              details = "These spacious 108sqm suites overlook the French Ambassador's residence, with breath-taking views of the Chao Phraya river, a private balcony and sitting area. Elegantly decorated, the Premier Suites have wooden floors in the living and dining areas, complemented perfectly by rugs and prints from the hotel's art collection that are inspired by the River of Kings. The bedroom features a subtle orchid theme, a dressing and sitting area and a walk-in closet.",
                              highlights = "Balcony with Seating, Dining Area For 5, Spacious Living Room and Walk-in Closet, High Bar-style Table, 24-Hour Butler Service",
                              description = "This luxurious suite has an entrance area leading to a spacious sitting area & desk with a separate dining area for 5 people. It has a private balcony with seating area. The specious bedroom has a dressing table and sitting area."
                              )for i in range(10)]

room_Premier2bedroomSuite = Room(name = "Premier Two-Bedroom Suite",
                                  type = "Suite",
                                  room_price = 70125,
                                  room_number = 0,
                                  bed_type = "King and Twin Beds or Twin and Twin Beds",
                                  size = "83SQM / 892SQF",
                                  toilet_type = "Japanese Toilets",
                                  complimentary = "Complimentary",
                                  speaker = "Bose Sound Bar",
                                  bathrobes = "Silk Kimonos",
                                  details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                  highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                  description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet.",
                                  )

room_Premier2bedroomSuite_list = [Room(name = "Premier Two-Bedroom Suite",
                                  type = "Suite",
                                  room_price = 70125,
                                  room_number = i+281,
                                  bed_type = "King and Twin Beds or Twin and Twin Beds",
                                  size = "83SQM / 892SQF",
                                  toilet_type = "Japanese Toilets",
                                  complimentary = "Complimentary",
                                  speaker = "Bose Sound Bar",
                                  bathrobes = "Silk Kimonos",
                                  details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                  highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                  description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet.",
                                  )for i in range(10)]

room_Siam1bedroomSuite = Room(name = "Siam One-Bedroom Suite",
                                type = "Suite",
                                room_price = 140000,
                                room_number = 0,
                                bed_type = "King Bed",
                                size = "107SQM / 1,152SQF",
                                toilet_type = "Japanese Toilets",
                                complimentary = "Complimentary",
                                speaker = "Bose Sound Bar",
                                bathrobes = "Silk Kimonos",
                                details = "Furnished with Thai antiques, magnificent Persian carpets and a varied art collection, this Thai-styled suite is beautifully appointed and eminently comfortable. Large floor-to-ceiling windows open out over the river, while a carved lotus cornice is one of many local touches. The 107sqm suite features a separate living area, as well as a dining area for five guests. Its private balcony with seating area overlooks the river.",
                                highlights = "Thai Antique Inspired Design from Northern Thailand, Balcony with Seating, Spacious Living Room, Dining Area For 5, Bedroom with Walk-In Wardrobe, 24-Hour Butler Service",
                                description = "Inspired by the beauty of Northern Thailand, this exquisite one bedroom suite features a separate elegant living and dining spaces, a large King size bed with dressing area. As well as a balcony and sitting area."
                                )

room_Siam1bedroomSuite_list = [Room(name = "Siam One-Bedroom Suite",
                                type = "Suite",
                                room_price = 140000,
                                room_number = i+291,
                                bed_type = "King Bed",
                                size = "107SQM / 1,152SQF",
                                toilet_type = "Japanese Toilets",
                                complimentary = "Complimentary",
                                speaker = "Bose Sound Bar",
                                bathrobes = "Silk Kimonos",
                                details = "Furnished with Thai antiques, magnificent Persian carpets and a varied art collection, this Thai-styled suite is beautifully appointed and eminently comfortable. Large floor-to-ceiling windows open out over the river, while a carved lotus cornice is one of many local touches. The 107sqm suite features a separate living area, as well as a dining area for five guests. Its private balcony with seating area overlooks the river.",
                                highlights = "Thai Antique Inspired Design from Northern Thailand, Balcony with Seating, Spacious Living Room, Dining Area For 5, Bedroom with Walk-In Wardrobe, 24-Hour Butler Service",
                                description = "Inspired by the beauty of Northern Thailand, this exquisite one bedroom suite features a separate elegant living and dining spaces, a large King size bed with dressing area. As well as a balcony and sitting area."
                                )for i in range(10)]

room_Ambassador2bedroomSuite = Room(name = "Ambassador Two-Bedroom Suite",
                                     type = "Suite",
                                     room_price = 234500,
                                     room_number = 0,
                                     bed_type = "King or Twin Beds",
                                     size = "107SQM / 1,152SQF",
                                     toilet_type = "Japanese Toilets",
                                     complimentary = "Complimentary",
                                     speaker = "Bose Sound Bar",
                                     bathrobes = "Silk Kimonos",
                                     details = "Furnished with Thai antiques, magnificent Persian carpets and a varied art collection, this Thai-styled suite is beautifully appointed and eminently comfortable. Large floor-to-ceiling windows open out over the river, while a carved lotus cornice is one of many local touches. The 107sqm suite features a separate living area, as well as a dining area for five guests. Its private balcony with seating area overlooks the river.",
                                     highlights = "Thai Antique Inspired Design from Northern Thailand, Balcony with Seating, Spacious Living Room, Dining Area For 5, Bedroom with Walk-In Wardrobe, 24-Hour Butler Service",
                                     description = "Inspired by the beauty of Northern Thailand, this exquisite one bedroom suite features a separate elegant living and dining spaces, a large King size bed with dressing area. As well as a balcony and sitting area."
                                     )

room_Ambassador2bedroomSuite_list = [Room(name = "Ambassador Two-Bedroom Suite",
                                     type = "Suite",
                                     room_price = 234500,
                                     room_number = i+301,
                                     bed_type = "King or Twin Beds",
                                     size = "107SQM / 1,152SQF",
                                     toilet_type = "Japanese Toilets",
                                     complimentary = "Complimentary",
                                     speaker = "Bose Sound Bar",
                                     bathrobes = "Silk Kimonos",
                                     details = "Furnished with Thai antiques, magnificent Persian carpets and a varied art collection, this Thai-styled suite is beautifully appointed and eminently comfortable. Large floor-to-ceiling windows open out over the river, while a carved lotus cornice is one of many local touches. The 107sqm suite features a separate living area, as well as a dining area for five guests. Its private balcony with seating area overlooks the river.",
                                     highlights = "Thai Antique Inspired Design from Northern Thailand, Balcony with Seating, Spacious Living Room, Dining Area For 5, Bedroom with Walk-In Wardrobe, 24-Hour Butler Service",
                                     description = "Inspired by the beauty of Northern Thailand, this exquisite one bedroom suite features a separate elegant living and dining spaces, a large King size bed with dressing area. As well as a balcony and sitting area."
                                     )for i in range(10)]

room_Selandia2bedroomSuite = Room(name = "Selandia Two-Bedroom Suite",
                                   type = "Suite",
                                   room_price = 190000,
                                   room_number = 0,
                                   bed_type = "King or Twin Beds",
                                   size = "169SQM / 1,818SQF",
                                   toilet_type = "Japanese Toilets",
                                   complimentary = "complimentary",
                                   speaker = "Bose Sound Bar",
                                   bathrobes = "Silk Kimonos",
                                   details = "This two-bedroom suite is named after the Selandia which in 1912 was the world&#39;s first diesel-powered ocean-going ship that travelled from Copenhagen to Bangkok. The 169sqm suite is beautifully decorated in hues of pale ivory against a background of hazy blues and rich scarlets. Furnished with silk throughout, every detail from brass-cornered tables to plush seating exudes luxurious elegance. It features a large living and dining area and two balconies.",
                                   highlights = "Two Bedrooms, Located on a High Floor, Spacious Living Room with Dining Area, Two Balconies with River and City Views, Master Bedroom with Walk-in Closet24-Hour Butler Service",
                                   description = "The Selandia suite features two bedrooms, a very spacious living room, a dining area for 4 persons and study area. There are two balconies and two bathrooms with views over the river and city."                                  
                                   )

room_Selandia2bedroomSuite_list = [Room(name = "Selandia Two-Bedroom Suite",
                                   type = "Suite",
                                   room_price = 190000,
                                   room_number = i+311,
                                   bed_type = "King or Twin Beds",
                                   size = "169SQM / 1,818SQF",
                                   toilet_type = "Japanese Toilets",
                                   complimentary = "complimentary",
                                   speaker = "Bose Sound Bar",
                                   bathrobes = "Silk Kimonos",
                                   details = "This two-bedroom suite is named after the Selandia which in 1912 was the world&#39;s first diesel-powered ocean-going ship that travelled from Copenhagen to Bangkok. The 169sqm suite is beautifully decorated in hues of pale ivory against a background of hazy blues and rich scarlets. Furnished with silk throughout, every detail from brass-cornered tables to plush seating exudes luxurious elegance. It features a large living and dining area and two balconies.",
                                   highlights = "Two Bedrooms, Located on a High Floor, Spacious Living Room with Dining Area, Two Balconies with River and City Views, Master Bedroom with Walk-in Closet24-Hour Butler Service",
                                   description = "The Selandia suite features two bedrooms, a very spacious living room, a dining area for 4 persons and study area. There are two balconies and two bathrooms with views over the river and city."                                  
                                   )for i in range(10)]

room_RoyalSuite = Room(name = "Royal Suite",
                        type = "Suite",
                        room_price = 340000,
                        room_number = 0,
                        bed_type = "King Bed",
                        size = "306SQM / 3,294SQF",
                        toilet_type = "Bath tub and Japanese toilet",
                        complimentary = "complimentary",
                        speaker = "Bose Sound Bar",
                        bathrobes = "Silk Kimonos",
                        details = "Our jewel in the historic crown is the 306sqm Royal Suite designed to suit official and security needs of discerning guests. It offers private access, meeting, fitness and spa facilities, as well as additional bedrooms to accommodate family and entourage. It is decorated in sumptuous royal colours of purples and yellow that juxtapose with white marble and crystal chandeliers for an ambience of classical but understated elegance.",
                        highlights = "Sumptuous, Colourful Regal Design, Private Access, Large Balcony and Dining Area, Private Spa and Fitness Centre, Kitchen, 24-Hour Butler Service",
                        description = "Designed with visiting Royal guests in mind, this suite offers private access, meeting, fitness and spa facilities, as well as an option of additional bedrooms to accommodate entourage, family members or security detail."
                        )

room_RoyalSuite_list = [Room(name = "Royal Suite",
                        type = "Suite",
                        room_price = 340000,
                        room_number = i+321,
                        bed_type = "King Bed",
                        size = "306SQM / 3,294SQF",
                        toilet_type = "Bath tub and Japanese toilet",
                        complimentary = "complimentary",
                        speaker = "Bose Sound Bar",
                        bathrobes = "Silk Kimonos",
                        details = "Our jewel in the historic crown is the 306sqm Royal Suite designed to suit official and security needs of discerning guests. It offers private access, meeting, fitness and spa facilities, as well as additional bedrooms to accommodate family and entourage. It is decorated in sumptuous royal colours of purples and yellow that juxtapose with white marble and crystal chandeliers for an ambience of classical but understated elegance.",
                        highlights = "Sumptuous, Colourful Regal Design, Private Access, Large Balcony and Dining Area, Private Spa and Fitness Centre, Kitchen, 24-Hour Butler Service",
                        description = "Designed with visiting Royal guests in mind, this suite offers private access, meeting, fitness and spa facilities, as well as an option of additional bedrooms to accommodate entourage, family members or security detail."
                        )for i in range(10)]

room_Oriental2bedroomSuite = Room(name = "Oriental Two-Bedroom Suite",
                                   type = "Suite",
                                   room_price = 430000,
                                   room_number = 0,
                                   bed_type = "King or Twin Beds",
                                   size = "376SQM / 4,046SQF",
                                   toilet_type = "Bathtub & Japanese Toilet",
                                   complimentary = "complitmentary",
                                   speaker = "Bose Sound Bar",
                                   bathrobes = "Silk Kimonos",
                                   details = "This stunning two-bedroom penthouse has welcomed many dignitaries & offers amazing river views with a wrap-around 57.6sqm terrace. Decorated with Thai silks, teak floors & Persian carpets, this suite is ideal for entertaining with a spacious living room with multiple sitting areas, a dining room for 12 and a kitchen. The master bedroom is furnished with antiques and a unique pineapple canopy bed. This 376sqm suite even has its own entertainment room.",
                                   highlights = "Outdoor Terrace with River Views, Master Bedroom with River Views, Fully Equipped Kitchen, Large dining room for 16, Entertainment Room, 24-Hour Butler Service",
                                   description = "This two bedroom penthouse situated on the top floor of the hotel offers amazing full river views with a wrap around terrace of 57.6sqm. It features a private dining room, an entertainment room, multiple sitting areas & a kitchen."
                                   )

room_Oriental2bedroomSuite_list = [Room(name = "Oriental Two-Bedroom Suite",
                                   type = "Suite",
                                   room_price = 430000,
                                   room_number = i+331,
                                   bed_type = "King or Twin Beds",
                                   size = "376SQM / 4,046SQF",
                                   toilet_type = "Bathtub & Japanese Toilet",
                                   complimentary = "complitmentary",
                                   speaker = "Bose Sound Bar",
                                   bathrobes = "Silk Kimonos",
                                   details = "This stunning two-bedroom penthouse has welcomed many dignitaries & offers amazing river views with a wrap-around 57.6sqm terrace. Decorated with Thai silks, teak floors & Persian carpets, this suite is ideal for entertaining with a spacious living room with multiple sitting areas, a dining room for 12 and a kitchen. The master bedroom is furnished with antiques and a unique pineapple canopy bed. This 376sqm suite even has its own entertainment room.",
                                   highlights = "Outdoor Terrace with River Views, Master Bedroom with River Views, Fully Equipped Kitchen, Large dining room for 16, Entertainment Room, 24-Hour Butler Service",
                                   description = "This two bedroom penthouse situated on the top floor of the hotel offers amazing full river views with a wrap around terrace of 57.6sqm. It features a private dining room, an entertainment room, multiple sitting areas & a kitchen."
                                   )for i in range(10)]
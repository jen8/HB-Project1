from model import connect_to_db, db, User, Post
from server import app
import random
from datetime import datetime
import time
from string import Template

end_dt = datetime.now()
end_in_millis = time.mktime(end_dt.timetuple())

start_dt = datetime.strptime("21/08/16 16:30", "%d/%m/%y %H:%M")
start_time_millis = time.mktime(start_dt.timetuple())

delta = end_in_millis - start_time_millis


connect_to_db(app)

locations = ["Mission", "Richmond", "Bernal Heights", "Haight Ashbury", "Noe Valley"]
category = ["crime", "community"]
crime_photo = ["c4.jpg", "Doggie-with-ball.jpg"] # TO DO find crime photos
comm_photo = ["c4.jpg", "Doggie-with-ball.jpg"] # TO DO find comm photos
comm_post_strings = ["Jog in the Park", 
                     "Pacific Cafe, Toy Boat among first businesses in city to receive Legacy Business status!",
                     "Perseid meteor shower primed to go big thanks to real gravitational bully"
                    ]
crim_post_strings = ["Home invasion, a robbery and three suspects charged in June stabbing at $where Bart plaza",
                     "China Beach closed after vandals lit portapotties on fire Monday night; $30,000 in damage"]


for n in range(201):
    loc = locations[random.randrange(len(locations))]
    cat = random.randrange(len(category))
    user_id = random.randint(1,3)
    has_pic = random.randrange(2) == 1
    pic = None

    if category[cat] == "crime":
        post_string = crim_post_strings[random.randrange(len(crim_post_strings))]
        if has_pic:
            pic = crime_photo[random.randrange(len(crime_photo))]
    else:
        post_string = comm_post_strings[random.randrange(len(comm_post_strings))]
        if has_pic:
            pic = comm_photo[random.randrange(len(comm_photo))]

    if "$where" in post_string:
        template = Template(post_string)
        post_string = template.substitute(where=loc)
    
    random_time_in_millis = start_time_millis + random.randrange(delta)
    random_dt = datetime.fromtimestamp( random_time_in_millis )

    print str(random_dt) + " " + loc + " " + category[cat] + " " + str(user_id) + " " + str(pic) + " " + post_string

    post = Post(post=post_string, location=loc, category=category[cat], user_id=user_id, photo_id=pic,\
                date=random_dt)
    db.session.add(post)

    #(post_string % (loc))
    #add_to_start_time = random.randint(range_in_millis)
    #new_date = datetime.fromtimestamp(start_time_in_millis + add_to_start_time)
    #print dateime.strftime("%A, %d. %B %Y %I:%M%p")
    
    # post1 = Post(post="Jog in the Park", location="Richmond", category="community event")
    # post2 = Post(post="Pacific Cafe, Toy Boat among first businesses in city to receive Legacy Business status!", location="Richmond", category="comunity event")
    # post3 = Post(post="Perseid meteor shower primed to go big thanks to real gravitational bully", location="Richmond", category="comunity event") INSERT PHOTO

    # post4 = Post(post="Cops, FBI arrest serial bank robber on his way to another heist on Geary", location="Richmond", category="crime alert")
    # post5 = Post(post="China Beach closed after vandals lit portapotties on fire Monday night; $30,000 in damage", location="Richmond", category="crime alert")(INSERT PHOTO)
    # post6 = Post(post="SFPD seeking graffiti taggers that may live in Richmond District ", location="Richmond", category="crime alert")
    # post7 = Post(post="Home invasion, a robbery and three suspects charged in June stabbing at Mission Bart plaza", location="Richmond", category="crime alert")


    # post8 = Post(post="Tz'utuhil Mayan art comes to Glama-Rama's gallery, artist to visit from Guatemala", location="Mission", category="community event") (w/ photo)
    # post9 = Post(post="Elbo Room on Valencia St. to be replaced by housing w/design that incorporates existing bldg", location="Mission", category="community event") (w/ photo)
    # post10 = Post(post="Self-driving cars cruise Mission District streets - a neighborly opinion", location="Mission", category="community event") (w/ photo)
    # post11 = Post(post="Vegan restaurant Herbivore on Valencia Street closing after 19 years in Mission District", location="Mission", category="community event") 
    # post12 = Post(post="24 units coming to Mission St. in two housing projects between 22nd & 23rd streets", location="Mission", category="community event")

    # post13 = Post(post="A woman was robbed by three men at knifepoint near 23rd and Shotwell Streets.", location="Mission", category="crime alert")
    # post14 = Post(post="A motorcycle officer was injured in a car collision on Wednesday", location="Mission", category="crime alert")
    # post15 = Post(post="Two robberies, man in critical condition after stabbing in SF Mission's Clarion Alley", location="Mission", category="crime alert")
    # post16 = Post(post="A bicyclist was arrested after attempting to snatch a cell phone from a moving car., location="Mission", category="crime alert") 
    # post17 = Post(post="Man in critical condition after Capp St. shooting", location="Mission", category="crime alert") INSERT PHOTO


    # post18 = Post(post="Crowdfunding for Esmeralda Slide Park Artwork Now Tantalizingly Close to Goal", location="Bernal Heights", category="community event")w/photo
    # post19 = Post(post="Fire-Damaged Cole Hardware and Playa Azul Demolished", location="Bernal Heights", category="community event")
    # post20 = Post(post="Nutes Noodles Seeking Permanent Place at 903 Cortland", location="Bernal Heights", category="community event")
    # post21 = Post(post="Emperor Norton Wants YOU in the Bernal Heights Hillwide Garage Sale", location="Bernal Heights", category="community event") 

    # post22 = Post(post="Auto Wheel Thieves Strike on Bocana", location="Bernal Heights", category="crime alert") w/photo
    # post23 = Post(post="Man robs Bernal Heights store while attempting to purchase M&Ms", location="Bernal Heights", category="crime alert")

    # post23 = Post(post="Lower Haight's Two Jack's Nik's Place Named SF Legacy Business", location="Bernal Heights", category="community event")w/photo
    # post24 = Post(post="Pre-Burning Man Events: A Lower Haight Roundup", location="Bernal Heights", category="community event")
    # post25 = Post(post="Lower Haight's Iza Ramen Taking Over SoMa's Former Triptych Space ", location="Bernal Heights", category="community event")
    # post26 = Post(post="National Night Out Brings SFPD Officers, Community Together For Family-Friendly Fun", location="Bernal Heights", category="community event") w/photo

    # post27 = Post(post="Smash-And-Grab Burglary Hits Glass Key", location="Bernal Heights", category="crime alert")w/photo
    # post28 = Post(post="Divisadero Corridor Hit By Duo Of Saturday-Night Armed Robberies", location="Bernal Heights", category="crime alert")
    # post29 = Post(post="SFPD Makes Arrest In 2015's Hayes Valley Quadruple Homicide", location="Bernal Heights", category="crime alert")

    # post30 = Post(post="Noe Valley's Hamlet Reopens Today, With New Look, Food Menus And Boozy Options", location="Noe Valley", category="community event")w/photo
    # post31 = Post(post="Tree falls on car in Noe Valley", location="Noe Valley", category="community event") w/photo
    # post32 = Post(post="Strawberry Moon Solstice over Noe Valley", location="Noe Valley", category="community event")
    # post33 = Post(post="Water main break in Diamond Heights in NoeValleySF. Estimated 2 hour repair", location="Noe Valley", category="community event")

    # post27 = Post(post="The BAR on Dolores robbed at gunpoint TWICE this week.", location="Noe Valley", category="crime alert")w/photo
    # post28 = Post(post="Divisadero Corridor Hit By Duo Of Saturday-Night Armed Robberies", location="Noe Valley", category="crime alert")
    # post29 = Post(post="SFPD Makes Arrest In 2015's Hayes Valley Quadruple Homicide", location="Noe Valley", category="crime alert")w/photo





    # db.session.add(post1)
    # db.session.add(post2)
    # db.session.add(post3)
    # db.session.add(post4)
    # db.session.add(post5)
    # db.session.add(post6)
    # db.session.add(post7)
    # db.session.add(post8)
    # db.session.add(post9)
    # db.session.add(post10)
    # db.session.add(post11)
    # db.session.add(post12)
    # db.session.add(post13)
    # db.session.add(post14)
    # db.session.add(post15)
    # db.session.add(post16)
    # db.session.add(post17)
    # db.session.add(post18)
    # db.session.add(post19)
    # db.session.add(post20)
    # db.session.add(post21)
    # db.session.add(post22)
    # db.session.add(post23)
    # db.session.add(post24)
    # db.session.add(post25)
    # db.session.add(post26)
    # db.session.add(post27)
    # db.session.add(post28)
    # db.session.add(post29)





db.session.commit()
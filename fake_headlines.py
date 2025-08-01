import random

choices = input("Select a category for your fake headline (sports, politics, or education): ")


if choices == "sports":
    sp_subject = [
        "Virat Kohli","Cristiano Ronaldo","Sania Mirza","Hardik Pandya",
        "Cristiano Ronaldo","David Beckham","Sunil Chhetri","Pv Sindhu",
        "MS Dhoni","Yuvraj Singh","Lionel Messi","Rohit Sharma","Rishabh Panth",
        "Goutam Gambhir","Neeraj Chopra","LeBron James",
    ]

    sp_action = ["has announced retirement",
    "is launching a fitness brand",
    "is opening a training academy",
    "has joined Bollywood",
    "is now a travel vlogger",
    "is seen eating pani puri challenge",
    "is caught coaching street kids",
    "was spotted doing breakdance",
    "has announced a surprise wedding"
]

    sp_place = [
        "Wankhede Stadium","Lords Cricket Ground","Eden Gardens","the bus stop","Film City",
        "Dubai","Kolkata","Mumbai","Delhi","London",
        "the dressing room", "Tokyo Olympics Village"
    ]

    use_in =["Dubai","Kolkata","Mumbai","Delhi","London","the dressing room"]
    use_at=["Wankhede Stadium","Lords Cricket Ground","Eden Gardens","the bus stop","Parliament","Film City","Tokyo Olympics Village","press conference hall", "practice ground","stadium gate"]

    while True:
        random_subject = random.choice(sp_subject)
        random_action = random.choice(sp_action)
        random_place = random.choice(sp_place)


        if random_place in use_in:
            prep = "in"
        elif random_place in use_at:
            prep = 'at'
        else:
            prep = 'on'

        subject = f"BREAKING NEWS: {random_subject} {random_action} {prep} {random_place}"

        print("\n" + subject + '\n')

        decision = input("Do you want to save this headline (Y/N): ").strip().upper()
        if decision == 'Y':
            with open("save_file.txt", 'a', encoding='utf-8')as f:
                f.write(subject+'\n')
        
            print("\nsuccessfully saved the fake headline..\n")
        else :
            pass


        re_generate = input("Are you interested in generating more headlines (Y/N): ").strip().upper()

        if re_generate == 'N':
            print("\nThank you for using, have a good day!")
            break


elif choices == "politics":
    pl_subject =[
        "Prime Minister Modi","Rahul Gandhi","Amit Shah","Yogi Adityanath","Bjp worker","TMC workers",
        "Mamta Banerjee","Abhishek Banerjee","Suvendu Adhikari","Kolkata Police","Modon Mitra","Anubrata Mondal"
    ]

    pl_action = [
    "opens a tea stall for common people","forget the prepared speech",
    "was caught dancing in a local fair","gets stuck in the Metro","starts dancing suddenly",
    "launches an app to find party defectors","starts a YouTube channel for youth",
   "declares election victory one year early","starts a podcast on street politics",
   "secretly visits a rival leader's house","is selling 'Biswa Bangla' T-shirts",
   "accidentally joins a hip-hop dance group",
 
        
    ]

    pl_place = [
    "Parliament House", "Rashtrapati Bhavan", "India Gate", "Red Fort", "Raj Ghat",
    "Nabanna", "Victoria Memorial", "Howrah Station", "Kalighat Temple", "College Street",
    "TMC Bhawan", "BJP Office",
    "Kolkata", "Delhi", "Mumbai", "a local train", "the stage", "the bus stop", "railway station"
    ]

    use_in = ["Kolkata", "Delhi", "Mumbai","a local train", "railway station"]
    use_at =[
        "Parliament House", "Rashtrapati Bhavan", "India Gate","Red Fort","Raj Ghat",
        "Nabanna", "Victoria Memorial", "Howrah Station", "Kalighat Temple","TMC Bhawan","BJP Office","the bus stop"
    ]
    use_on =["the stage"]
    use_near = ["College Street", "Raj Ghat"]
    use_from = ["Parliament", "Nabanna","Mumbai","Delhi"]

    while True:

        random_subject = random.choice(pl_subject)
        random_action = random.choice(pl_action)
        random_place = random.choice(pl_place)


        if random_place in use_in:
            prep = 'in'
        elif random_place in use_at:
            prep = 'at'
        elif random_place in use_on:
            prep = 'on'
        elif random_place in use_near:
            prep = 'near'
        elif random_place in use_from:
            prep = 'from'
        else :
            prep = 'at'


        subject = f"BREAKING NEWS: {random_subject} {random_action} {prep} {random_place}!"

        print("\n" + subject + '\n')

        decision = input("Do you want to save this headline (Y/N): ").strip().upper()
        if decision == 'Y':
            with open("save_file.txt", 'a', encoding='utf-8')as f:
                f.write(subject+'\n')
        
            print("\nsuccessfully saved the fake headline..\n")
        else :
            pass



        re_generate = input("Are you interested in generating more headlines (Y/N): ").strip().upper()

        if re_generate == 'N':
            print("\nThank you for using, have a good day!")
            break

elif choices == "education":
    ed_subject =[
       "IIT Professor", "Delhi University", "School Teacher", "Class 10 Topper",
       "AIIMS medical students", "students"
    ]

    ed_action =[
        "launches a free online course","hosts a webinar on AI",
        "writes a viral research paper", "conduct surprise test",
       "organizes an education fair"
    ]

    ed_place =[
        "IIT Delhi", "school auditorium", "conference hall", "the classroom", "college campus",
        "science fair", "local library", 'an online session'
    ]

    use_in =['the classroom', "local library"]
    use_at =['IIT Delhi', "school auditorium", 'conference hall', 'science fair']
    

    while True:
        random_subject = random.choice(ed_subject)
        random_action = random.choice(ed_action)
        random_place = random.choice(ed_place)

        if random_place in use_in:
            prep = 'in'
        elif random_place in use_at:
            prep = 'at'
        else:
            prep = 'on'


        subject = f"BREAKING NEWS: {random_subject} {random_action} {prep} {random_place}"

        print("\n" + subject + '\n')

        decision = input("Do you want to save this headline (Y/N): ").strip().upper()
        if decision == 'Y':
            with open("save_file.txt", 'a', encoding='utf-8')as f:
                f.write(subject+'\n')
        
            print("\nsuccessfully saved the fake headline..\n")
        else :
            pass

        re_generate = input("Are you interested in generating more headlines (Y/N): ").strip().upper()

        if re_generate == 'N':
            
            print("\nThank you for using, have a good day!")
            break
else:
    print("Invalid Category...")

        

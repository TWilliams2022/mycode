


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
 #        {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
  #       {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
   #      {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


NE_animals= farms[0]["agriculture"]

for x in NE_animals:
     print(x)

 for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        # you do the rest

yuck= ["carrots", "celery"]



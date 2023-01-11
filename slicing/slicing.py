challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

print("My " + challenge[2][1] + "! The " + challenge[2][0] + " do" + challenge[3] + "!")

#############################################

#My eyes! The goggles do nothing!
#goggles becuase it holds eyes with : and vice versa
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

print("My " + trial[3]["goggles"] + " the" + trail[2]["eyes"] + " do" + trial[-1] + " !") 

#############################################

#needed this example for later
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a= nightmare[0]["user"]["name"]["first"]
b= nightmare[0]["kumquat"]
c= nightmare[0]["d"]

print(f"My {a}! The {b} do {c}!")

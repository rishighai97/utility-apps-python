#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import random


# In[28]:


family_locations = [
    ["Europe", "Santorini", "Greece", "Beach"],
    ["Europe", "Paris", "France", "City"],
    ["Europe", "Matterhorn", "Switzerland", "Mountain"],
    ["Asia", "Panaji", "India", "Beach"],
    ["Asia", "Tokyo", "Japan", "City"],
    ["Asia", "Kathmandu", "Nepal", "Mountain"]
]
couple_locations = [
    ["North America", "Cabo San Lucas", "Mexico", "Beach"],
    ["Europe", "Paris", "France", "City"],
    ["Europe", "Santorini", "Greece", "Beach"],
    ["Europe", "Matterhorn", "Switzerland", "Mountain"],
    ["Asia", "Kathmandu", "Nepal", "Mountain"]
]

solo_locations =  [
    ["Asia", "Tokyo", "Japan", "City"],
    ["Europe", "Matterhorn", "Switzerland", "Mountain"],
    ["Asia", "Panaji", "India", "Beach"],
]


# In[29]:


source_cities = [
    "Seattle",
    "New York",
    "Chicago",
    "Denver",
    "Los Angeles",
    "Portland",
    "Dallas"
]


# In[30]:


booking_types = [
    "Family/Friends",
    "Couple",
    "Solo"
]


# In[34]:


records = []
for i in range(0, 100001):

    source_city = random.choice(source_cities)
    booking_type = random.choice(booking_types)
    location = random.choice(family_locations)
    if booking_type == "Couple": 
        source_city = random.choice(["Seattle", "New York", "Los Angeles"])
        location = random.choice(couple_locations)
    elif booking_type == "Solo":
        source_city = random.choice(["Dallas", "Portland"])
        location = random.choice(solo_locations)
    records.append({
        "Index": i,
        "Hotel City": location[1],
        "Hotel Country": location[2],
        "Hotel Continent": location[0],
        "Source City": source_city,
        "Trip Type": booking_type,
        "Location Type": location[3],
    })


# In[35]:


dataset = pd.DataFrame(records)


# In[36]:


dataset.to_csv("dataset.csv", index = False)


# In[ ]:





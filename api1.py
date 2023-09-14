from fastapi import FastAPI
import pandas as pd
import json


app = FastAPI()

@app.get("/")

def root():
    return{"Hello : shivesh "}

from pydantic import BaseModel
from typing import Dict

class InputProperties(BaseModel):
  u_L: int
  u_B: int
  u_room: int
  u_car: int
  u_temple: str
  u_gym: str
  u_theater: str
  u_office: str
  u_vastu: str
  u_position: str

# json dataset






property_data = {
  "S_no": {
    "0": 1,
    "1": 2,
    "2": 3,
    "3": 4,
    "4": 5,
    "5": 6,
    "6": 7,
    "7": 8,
    "8": 9,
    "9": 10,
    "10": 11,
    "11": 12,
    "12": 13,
    "13": 14
  },
  "Area": {
    "0": 2400,
    "1": 2400,
    "2": 1344,
    "3": 1440,
    "4": 1540,
    "5": 1296,
    "6": 1575,
    "7": 2400,
    "8": 2500,
    "9": 1296,
    "10": 2400,
    "11": 2420,
    "12": 2400,
    "13": 2000
  },
  "Facing": {
    "0": "Center",
    "1": "Center",
    "2": "Center",
    "3": "Center",
    "4": "Center",
    "5": "Corner",
    "6": "Center",
    "7": "Center",
    "8": "Center",
    "9": "Center",
    "10": "Center",
    "11": "Center",
    "12": "Center",
    "13": "Corner"
  },
  "Direction": {
    "0": "East",
    "1": "West",
    "2": "NW",
    "3": "North",
    "4": "West",
    "5": "South",
    "6": "North",
    "7": "East",
    "8": "SW",
    "9": "West",
    "10": "West",
    "11": "West",
    "12": "West",
    "13": "North"
  },
  "Vastu": {
    "0": "yes",
    "1": "yes",
    "2": "yes",
    "3": "yes",
    "4": "yes",
    "5": "no",
    "6": "yes",
    "7": "yes",
    "8": "no",
    "9": "yes",
    "10": "yes",
    "11": "yes",
    "12": "yes",
    "13": "yes"
  },
  "AR": {
    "0": 0.6666666667,
    "1": 0.6666666667,
    "2": 0.4285714286,
    "3": 0.625,
    "4": 0.6,
    "5": 1,
    "6": 0.7777777778,
    "7": 0.6666666667,
    "8": 1,
    "9": 0.3092783505,
    "10": 0.6666666667,
    "11": 0.375,
    "12": 0.6666666667,
    "13": 0.6964285714
  },
  "Dim_L": {
    "0": 40,
    "1": 40,
    "2": 24,
    "3": 30,
    "4": 30,
    "5": 37,
    "6": 35,
    "7": 40,
    "8": 50,
    "9": 20,
    "10": 40,
    "11": 30,
    "12": 40,
    "13": 39
  },
  "Dim_B": {
    "0": 60,
    "1": 60,
    "2": 56,
    "3": 48,
    "4": 50,
    "5": 37,
    "6": 45,
    "7": 60,
    "8": 50,
    "9": 64.6666666667,
    "10": 60,
    "11": 80,
    "12": 60,
    "13": 56
  },
  "Bedrooms": {
    "0": 4,
    "1": 3,
    "2": 3,
    "3": 4,
    "4": 4,
    "5": 3,
    "6": 4,
    "7": 4,
    "8": 3,
    "9": 4,
    "10": 5,
    "11": 6,
    "12": 3,
    "13": 4
  },

  "Parking_L": {
    "0": 19,
    "1": 15.6666666667,
    "2": 16.75,
    "3": 23.6666666667,
    "4": 17,
    "5": 0,
    "6": 28.5,
    "7": 16.75,
    "8": 12,
    "9": 14.4166666667,
    "10": 16.25,
    "11": 0,
    "12": 13.1666666667,
    "13": 12.4166666667
  },
  "Parking_B": {
    "0": 45,
    "1": 9.3333333333,
    "2": 29.4166666667,
    "3": 22.25,
    "4": 8.4166666667,
    "5": 0,
    "6": 0,
    "7": 44.25,
    "8": 17,
    "9": 4.25,
    "10": 54.25,
    "11": 0,
    "12": 19.6666666667,
    "13": 16
  },
  "Home Theater": {
    "0": "no",
    "1": "no",
    "2": "no",
    "3": "no",
    "4": "no",
    "5": "no",
    "6": "no",
    "7": "no",
    "8": "no",
    "9": "no",
    "10": "yes",
    "11": "no",
    "12": "no",
    "13": "no"
  },
  "Home_theatre_l": {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 22.75,
    "11": 0,
    "12": 0,
    "13": 0
  },
  "Home_theatre_b": {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 20,
    "11": 0,
    "12": 0,
    "13": 0
  },
  "Temple": {
    "0": "yes",
    "1": "no",
    "2": "yes",
    "3": "yes",
    "4": "yes",
    "5": "yes",
    "6": "yes",
    "7": "yes",
    "8": "yes",
    "9": "no",
    "10": "yes",
    "11": "yes",
    "12": "yes",
    "13": "yes"
  },
  "Temple_l": {
    "0": 5,
    "1": 0,
    "2": 4.25,
    "3": 7,
    "4": 8,
    "5": 7.5,
    "6": 4.25,
    "7": 11,
    "8": 6,
    "9": 0,
    "10": 10.25,
    "11": 13,
    "12": 7.3333333333,
    "13": 5
  },
  "Temple_b": {
    "0": 5.5,
    "1": 0,
    "2": 4.3333333333,
    "3": 10.3333333333,
    "4": 7.4166666667,
    "5": 8.25,
    "6": 4.25,
    "7": 6,
    "8": 11,
    "9": 0,
    "10": 15.5,
    "11": 10.75,
    "12": 6.6666666667,
    "13": 7.9166666667
  },
  "Gym": {
    "0": "no",
    "1": "no",
    "2": "no",
    "3": "no",
    "4": "no",
    "5": "yes",
    "6": "no",
    "7": "yes",
    "8": "no",
    "9": "no",
    "10": "yes",
    "11": "no",
    "12": "yes",
    "13": "yes"
  },
  "Gym_l": {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 11,
    "6": 0,
    "7": 33.3333333333,
    "8": 0,
    "9": 0,
    "10": 21.5,
    "11": 0,
    "12": 9.25,
    "13": 9.75
  },
  "Gym_b": {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 19,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 22.25,
    "11": 0,
    "12": 24.8333333333,
    "13": 10.1666666667
  },
  "Office": {
    "0": "no",
    "1": "no",
    "2": "no",
    "3": "no",
    "4": "no",
    "5": "no",
    "6": "no",
    "7": "no",
    "8": "no",
    "9": "no",
    "10": "yes",
    "11": "no",
    "12": "no",
    "13": "no"
  },
  "Office_l": {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 12.25,
    "11": 0,
    "12": 0,
    "13": 0
  },
  "Office_b": {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 12,
    "11": 0,
    "12": 0,
    "13": 0
  },
  "Dim_Aspect_Ratio": {
    "0": 2400,
    "1": 2400,
    "2": 1344,
    "3": 1440,
    "4": 1500,
    "5": 1369,
    "6": 1575,
    "7": 2400,
    "8": 2500,
    "9": 1293.3333333333,
    "10": 2400,
    "11": 2400,
    "12": 2400,
    "13": 2184
  },
  "Parking_area": {
    "0": 855,
    "1": 146.2222222222,
    "2": 492.7291666667,
    "3": 526.5833333333,
    "4": 143.0833333333,
    "5": 0,
    "6": 0,
    "7": 741.1875,
    "8": 204,
    "9": 61.2708333333,
    "10": 881.5625,
    "11": 0,
    "12": 258.9444444444,
    "13": 198.6666666667
  },
  "no_of_cars": {
    "0": 5,
    "1": 0,
    "2": 4,
    "3": 4,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 5,
    "8": 1,
    "9": 0,
    "10": 5,
    "11": 0,
    "12": 2,
    "13": 1
  },
  "Score": {
    "0": 570,
    "1": 410,
    "2": 350,
    "3": 500,
    "4": 450,
    "5": 0,
    "6": 450,
    "7": 530,
    "8": 350,
    "9": 340,
    "10": 350,
    "11": 400,
    "12": 460,
    "13": 0
  }
}
@app.get("/")
def read_root():
    return {"message": "Welcome to the Property API"}

# @app.get("/properties")
# def get_properties():
#     return property_data

def dt(u_area,u_AR,u_room,u_car,u_temple,u_gym,u_theater,u_office,u_vastu,u_position):
    '''applying all the functions on respective columns '''
    json_data = {
      "S_no": {
        "0": 1,
        "1": 2,
        "2": 3,
        "3": 4,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 8,
        "8": 9,
        "9": 10,
        "10": 11,
        "11": 12,
        "12": 13,
        "13": 14
      },
      "Area": {
        "0": 2400,
        "1": 2400,
        "2": 1344,
        "3": 1440,
        "4": 1540,
        "5": 1296,
        "6": 1575,
        "7": 2400,
        "8": 2500,
        "9": 1296,
        "10": 2400,
        "11": 2420,
        "12": 2400,
        "13": 2000
      },
      "Facing": {
        "0": "Center",
        "1": "Center",
        "2": "Center",
        "3": "Center",
        "4": "Center",
        "5": "Corner",
        "6": "Center",
        "7": "Center",
        "8": "Center",
        "9": "Center",
        "10": "Center",
        "11": "Center",
        "12": "Center",
        "13": "Corner"
      },
      "Direction": {
        "0": "East",
        "1": "West",
        "2": "NW",
        "3": "North",
        "4": "West",
        "5": "South",
        "6": "North",
        "7": "East",
        "8": "SW",
        "9": "West",
        "10": "West",
        "11": "West",
        "12": "West",
        "13": "North"
      },
      "Vastu": {
        "0": "yes",
        "1": "yes",
        "2": "yes",
        "3": "yes",
        "4": "yes",
        "5": "no",
        "6": "yes",
        "7": "yes",
        "8": "no",
        "9": "yes",
        "10": "yes",
        "11": "yes",
        "12": "yes",
        "13": "yes"
      },
      "AR": {
        "0": 0.6666666667,
        "1": 0.6666666667,
        "2": 0.4285714286,
        "3": 0.625,
        "4": 0.6,
        "5": 1,
        "6": 0.7777777778,
        "7": 0.6666666667,
        "8": 1,
        "9": 0.3092783505,
        "10": 0.6666666667,
        "11": 0.375,
        "12": 0.6666666667,
        "13": 0.6964285714
      },
      "Dim_L": {
        "0": 40,
        "1": 40,
        "2": 24,
        "3": 30,
        "4": 30,
        "5": 37,
        "6": 35,
        "7": 40,
        "8": 50,
        "9": 20,
        "10": 40,
        "11": 30,
        "12": 40,
        "13": 39
      },
      "Dim_B": {
        "0": 60,
        "1": 60,
        "2": 56,
        "3": 48,
        "4": 50,
        "5": 37,
        "6": 45,
        "7": 60,
        "8": 50,
        "9": 64.6666666667,
        "10": 60,
        "11": 80,
        "12": 60,
        "13": 56
      },
      "Bedrooms": {
        "0": 4,
        "1": 3,
        "2": 3,
        "3": 4,
        "4": 4,
        "5": 3,
        "6": 4,
        "7": 4,
        "8": 3,
        "9": 4,
        "10": 5,
        "11": 6,
        "12": 3,
        "13": 4
      },

      "Parking_L": {
        "0": 19,
        "1": 15.6666666667,
        "2": 16.75,
        "3": 23.6666666667,
        "4": 17,
        "5": 0,
        "6": 28.5,
        "7": 16.75,
        "8": 12,
        "9": 14.4166666667,
        "10": 16.25,
        "11": 0,
        "12": 13.1666666667,
        "13": 12.4166666667
      },
      "Parking_B": {
        "0": 45,
        "1": 9.3333333333,
        "2": 29.4166666667,
        "3": 22.25,
        "4": 8.4166666667,
        "5": 0,
        "6": 0,
        "7": 44.25,
        "8": 17,
        "9": 4.25,
        "10": 54.25,
        "11": 0,
        "12": 19.6666666667,
        "13": 16
      },
      "Home Theater": {
        "0": "no",
        "1": "no",
        "2": "no",
        "3": "no",
        "4": "no",
        "5": "no",
        "6": "no",
        "7": "no",
        "8": "no",
        "9": "no",
        "10": "yes",
        "11": "no",
        "12": "no",
        "13": "no"
      },
      "Home_theatre_l": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 22.75,
        "11": 0,
        "12": 0,
        "13": 0
      },
      "Home_theatre_b": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 20,
        "11": 0,
        "12": 0,
        "13": 0
      },
      "Temple": {
        "0": "yes",
        "1": "no",
        "2": "yes",
        "3": "yes",
        "4": "yes",
        "5": "yes",
        "6": "yes",
        "7": "yes",
        "8": "yes",
        "9": "no",
        "10": "yes",
        "11": "yes",
        "12": "yes",
        "13": "yes"
      },
      "Temple_l": {
        "0": 5,
        "1": 0,
        "2": 4.25,
        "3": 7,
        "4": 8,
        "5": 7.5,
        "6": 4.25,
        "7": 11,
        "8": 6,
        "9": 0,
        "10": 10.25,
        "11": 13,
        "12": 7.3333333333,
        "13": 5
      },
      "Temple_b": {
        "0": 5.5,
        "1": 0,
        "2": 4.3333333333,
        "3": 10.3333333333,
        "4": 7.4166666667,
        "5": 8.25,
        "6": 4.25,
        "7": 6,
        "8": 11,
        "9": 0,
        "10": 15.5,
        "11": 10.75,
        "12": 6.6666666667,
        "13": 7.9166666667
      },
      "Gym": {
        "0": "no",
        "1": "no",
        "2": "no",
        "3": "no",
        "4": "no",
        "5": "yes",
        "6": "no",
        "7": "yes",
        "8": "no",
        "9": "no",
        "10": "yes",
        "11": "no",
        "12": "yes",
        "13": "yes"
      },
      "Gym_l": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 11,
        "6": 0,
        "7": 33.3333333333,
        "8": 0,
        "9": 0,
        "10": 21.5,
        "11": 0,
        "12": 9.25,
        "13": 9.75
      },
      "Gym_b": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 19,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 22.25,
        "11": 0,
        "12": 24.8333333333,
        "13": 10.1666666667
      },
      "Office": {
        "0": "no",
        "1": "no",
        "2": "no",
        "3": "no",
        "4": "no",
        "5": "no",
        "6": "no",
        "7": "no",
        "8": "no",
        "9": "no",
        "10": "yes",
        "11": "no",
        "12": "no",
        "13": "no"
      },
      "Office_l": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 12.25,
        "11": 0,
        "12": 0,
        "13": 0
      },
      "Office_b": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 12,
        "11": 0,
        "12": 0,
        "13": 0
      },
      "Dim_Aspect_Ratio": {
        "0": 2400,
        "1": 2400,
        "2": 1344,
        "3": 1440,
        "4": 1500,
        "5": 1369,
        "6": 1575,
        "7": 2400,
        "8": 2500,
        "9": 1293.3333333333,
        "10": 2400,
        "11": 2400,
        "12": 2400,
        "13": 2184
      },
      "Parking_area": {
        "0": 855,
        "1": 146.2222222222,
        "2": 492.7291666667,
        "3": 526.5833333333,
        "4": 143.0833333333,
        "5": 0,
        "6": 0,
        "7": 741.1875,
        "8": 204,
        "9": 61.2708333333,
        "10": 881.5625,
        "11": 0,
        "12": 258.9444444444,
        "13": 198.6666666667
      },
      "no_of_cars": {
        "0": 5,
        "1": 0,
        "2": 4,
        "3": 4,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 5,
        "8": 1,
        "9": 0,
        "10": 5,
        "11": 0,
        "12": 2,
        "13": 1
      },
      "Score": {
        "0": 570,
        "1": 410,
        "2": 350,
        "3": 500,
        "4": 450,
        "5": 0,
        "6": 450,
        "7": 530,
        "8": 350,
        "9": 340,
        "10": 350,
        "11": 400,
        "12": 460,
        "13": 0
      }
    }

    def AreaScore(area):
      '''function for scoring on the basis of area
      '''
      if area > u_area * 0.9 and area < u_area * 1.1:
        val = 100
      elif area > u_area * 0.8 and area < u_area * 1.2:
        val = 50
      else:
        val = 20

      return val

    def ARScore(AR):
      '''function for scoring on the basis of aspectratio
      '''
      if AR > u_AR * 0.9 and AR < u_AR * 1.1:
        val = 80
      elif AR > u_AR * 0.8 and AR < u_AR * 1.2:
        val = 40
      else:
        val = 10

      return val

    def RoomScore(room):
      '''function for scoring on the basis of no.of rooms
      '''
      if room == u_room:
        val = 100
      elif room > u_room - 1 and room < u_room + 1:
        val = 50
      elif room > u_room - 2 and room < u_room + 2:
        val = 20
      else:
        val = 0

      return val

    def PrkScore(car):
      '''function for scoring on the basis of no. of cars to be parked
      '''
      if car == u_car:
        val = 60
      elif car > u_car - 1 and car < u_car + 1:
        val = 30
      elif car > u_car - 2 and car < u_car + 2:
        val = 10
      else:
        val = 0

      return val

    def templeScore(temple):
      '''function for scoring on the basis of requirement of temple
      '''
      if temple == u_temple:
        val = 80

      else:
        val = 0

      return val

    def gymScore(gym):
      '''function for scoring on the basis of requirement of gym
      '''
      if gym == u_gym:
        val = 40

      else:
        val = 0

      return val

    def theaterScore(theater):
      '''function for scoring on the basis of requirement of home theater
      '''
      if theater == u_theater:
        val = 40

      else:
        val = 0

      return val

    def officeScore(office):
      '''function for scoring on the basis of requirement of office
      '''
      if office == u_office:
        val = 60

      else:
        val = 0

      return val

    def vastuScore(vastu):
      '''function for scoring on the basis of requirement of vastu
      '''
      if vastu == u_vastu:
        val = 70

      else:
        val = 0

      return val

    def positionScore(position):
      '''function for scoring on the basis of requirement of temple
      '''
      if position == u_position:
        val = 1

      else:
        val = 0

      return val

    df = pd.DataFrame(json_data)
    # print(df)
    df['Score'] = 0
    df['Score'] += df['Area'].apply(AreaScore)
    df['Score'] += df['AR'].apply(ARScore)
    df['Score'] += df['Bedrooms'].apply(RoomScore)
    df['Score'] += df['no_of_cars'].apply(PrkScore)
    df['Score'] += df['Temple'].apply(templeScore)
    df['Score'] += df['Gym'].apply(gymScore)
    df['Score'] += df['Home Theater'].apply(theaterScore)
    df['Score'] += df['Office'].apply(officeScore)
    df['Score'] += df['Vastu'].apply(vastuScore)
    df['Score'] *= df['Facing'].apply(positionScore)

    lst = list(df.sort_values(by='Score', ascending=False).head(3)['S_no'][0:3])
    return lst

    print(df.head())
    # score = df["Score"].to_list()
    # s_no_values = df["S_no"].tolist()
    # print(score)
    # score_ = 0
    # for item in score:
    #     score_ += item
    # print("=====>",score_)
    # return score_
    # return s_no_values

@app.post("/property/")
def get_property_by_s_no(test_input: InputProperties):
    print(test_input)
    u_area = test_input.u_L * test_input.u_B
    u_AR = test_input.u_L / test_input.u_B
    return dt(u_area,u_AR,test_input.u_room,test_input.u_car,test_input.u_temple,test_input.u_gym,\
              test_input.u_theater,test_input.u_office,test_input.u_vastu,test_input.u_position)

    # # Create a list of dictionaries containing S_no and their corresponding scores
    # property_scores = [{"S_no": s_no, "Score": score} for s_no, score in enumerate(scores, start=1)]
    #
    # return property_scores


    # return test_input
    # if str(s_no) in property_data["S_no"]:
    #     return property_data["S_no"][str(s_no)]
    # else:
    #     return {"error": "Property not found"}
#


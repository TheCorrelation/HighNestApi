import json

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI()


origins = ["*"]
# Configure cross origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root(request:Request):
    return RedirectResponse('/docs', status_code=200)

from typing import Dict

from pydantic import BaseModel


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


@app.get("/")
def read_root():
    return {"message": "Welcome to the Property API"}

# @app.get("/properties")
# def get_properties():
#     return property_data

def dt(u_area,u_AR,u_room,u_car,u_temple,u_gym,u_theater,u_office,u_vastu,u_position):
    '''applying all the functions on respective columns '''
    json_data = None
    with open('matrix.json') as file_obj:
        json_data = json.load(file_obj)

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

    response_dict = get_image_url(df)
    return response_dict

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

def get_image_url(df):
    response_dict = {}
    with open('image_mapping.json') as file_obj:
        json_data = json.load(file_obj)
    
    for count, data in enumerate(df.sort_values(by='Score', ascending=False).head(3)['S_no'][0:3], start=1):
        response_dict[f'result_{count}'] = json_data.get(f'a{data}')
    
    return response_dict

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

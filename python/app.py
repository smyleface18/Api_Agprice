from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from typing import Union;
from PyPDF2 import PdfReader;
from cron_job import cron_dowload_save;
from cron_job import cron_save_price;
from task import date_current;
from task import productos;
import json;



app = FastAPI();

origins =[
    "http://localhost:4321",
    "http://127.0.0.1:5500"   
]




app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

date =  date_current();


@app.get("/price")

def price():
    date = date_current();
    return productos(date);




@app.get("/historical/prices")

def historicalprices():
    #save_price(date);
    file = open("python/historical_prices.json","r")
    
    return  json.loads(file.read());





if( not(date[4] == "Sabado" or date[4] == "Domingo")):
    cron_dowload_save.start();
     




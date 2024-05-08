from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from typing import Union;
from PyPDF2 import PdfReader;
from cron_job import cron_dowload_save;
from cron_job import cron_save_price;
from task import date_current;
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
     



def productos(date):

    extrac();

    value = False;

    
    with open("python\extrac.txt", "r+") as linea:
        for a in linea:
            arrayWords = a.split();
            if(len(arrayWords) >= 2):
                if(value):
                    if("CABEZONA" == arrayWords[1]):

                        if("ROJA"  == arrayWords[2]):
                            cebolla = arrayWords[0]+" "+arrayWords[1]+" "+arrayWords[2]+" "+arrayWords[8];
                            cebolla = cebolla.split("$");
                            cebolla[1] = float(cebolla[1]);


                        
                if("CEBOLLA" == arrayWords[0]):
                    value = True;
                    
                    
                if("FRIJOL" == arrayWords[0]):
                    frijol = arrayWords[0]+" "+arrayWords[1]+" "+arrayWords[7];
                    frijol = frijol.split("$");
                    frijol[1] = float(frijol[1]);
                    
                    
                    
                if("TOMATE" == arrayWords[0]):
                    if("CHONTO" == arrayWords[1]):
                        tomate = arrayWords[0]+" "+arrayWords[1]+" "+arrayWords[7];
                        tomate = tomate.split("$");
                        tomate[1] = float(tomate[1]); 
                        
                        
                if("MAZORCA" == arrayWords[0]):
                    mazorca = arrayWords[0]+" "+arrayWords[6];
                    mazorca = mazorca.split("$");
                    mazorca[1] = float(mazorca[1]);
                    
                    
                if("PIMENTON" == arrayWords[0]):
                    pimento = arrayWords[0]+" "+arrayWords[6];
                    pimento = pimento.split("$");
                    pimento[1] = float(pimento[1]);
                    


    return [{"name" : cebolla[0],"price": cebolla[1],"location": "Bogota","date" : date[3]+"-"+date[1]+"-"+date[0]},
            {"name" : frijol[0],"price": frijol[1],"location": "Bogota","date" : date[3]+"-"+date[1]+"-"+date[0]},
            {"name" : tomate[0],"price": tomate[1],"location": "Bogota","date" : date[3]+"-"+date[1]+"-"+date[0]},
            {"name" : mazorca[0],"price": mazorca[1],"location": "Bogota","date" : date[3]+"-"+date[1]+"-"+date[0]},
            {"name" : pimento[0],"price": pimento[1],"location": "Bogota","date" : date[3]+"-"+date[1]+"-"+date[0]},
            {"year" : date[0],"month" : date[1],"monthWord": date[2],"day" : date[3],"weekday" : date[4]}]



def extrac():

    data = open(r"Boletin.pdf","rb")
    reader = PdfReader(data);
    page = reader.pages[1];

    archivo = page.extract_text()

    file = open("python\extrac.txt","r+")
    file.write(archivo);
    file.close();


def save_price(date):
    
    array_words = [];
    
    # los dos primero with es para eliminar el ] en el archivo json para poder concaternar el nuevo objeto json
    
    with open("python/historical_prices.json","r+",encoding="utf-8") as historical_prices:
        for linea in historical_prices:
            array_words.append(linea);
    array_words.pop();
    text = "".join(array_words)
    text.replace("\n", "")
    print(text)     

    with open("python/historical_prices.json","w") as historical_prices:
        historical_prices.write(text)


    with open("python/historical_prices.json","a") as historical_prices:
            data = json.dumps(productos(date), indent=4)
            historical_prices.write(","+"\n"+data+"\n"+"]")
     




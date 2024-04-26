from fastapi import FastAPI;
from typing import Union;
from PyPDF2 import PdfReader;
import requests;
from datetime import datetime

app = FastAPI();

@app.get("/price")

def price():
    
    
    return extrac();




    
def extrac():

    data = open(r"Boletin.pdf","rb")
    reader = PdfReader(data);
    page = reader.pages[1];



    archivo = page.extract_text()






    file = open("h.txt","r+")

    file.write(archivo);
    file.close();

    value = False;
    with open("h.txt", "r+") as linea:
        for a in linea:
            arrayWords = a.split();
            print(arrayWords);
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

    return {{"name" : cebolla[0],
             "price": cebolla[1],
             "location": "Bogota"
             },
            {"name" : frijol[0],
             "price": frijol[1],
             "location": "Bogota"
             },
            {"name" : tomate[0],
             "price": tomate[1],
             "location": "Bogota"
             },
        
            }

def date():
    now = datetime.now();
    day = str(now.day);
    month = now.month;
    
    arrayMonths = ("enero","febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    
    month = arrayMonths[month-1];
    
    return day, month;
    
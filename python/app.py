from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from typing import Union;
from PyPDF2 import PdfReader;
from cron_job import scheduler;
from task import date;





app = FastAPI();

origins =[
    "http://localhost:4321",
    
]




app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/price")

async def price():
    return productos();


if( not(date()[4] == "Lunes" or date()[4] == "Domingo")):
    scheduler.start(); 


def productos():

    extrac();

    value = False;

    
    with open("python\h.txt", "r+") as linea:
        for a in linea:
            arrayWords = a.split();
           
            if(value):
                if("CABEZONA" == arrayWords[1]):
                    print("7////////////////"+arrayWords[1])
                    if("ROJA"  == arrayWords[2]):
                        cebolla = arrayWords[0]+" "+arrayWords[1]+" "+arrayWords[2]+" "+arrayWords[8];
                        cebolla = cebolla.split("$");
                        cebolla[1] = float(cebolla[1]);
                        print("7////////////////"+arrayWords[1])
                        print(cebolla)
                       
                        
                    
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

    return [{"name" : cebolla[0],
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
            ]


    
    

def extrac():

    data = open(r"Boletin.pdf","rb")
    reader = PdfReader(data);
    page = reader.pages[1];


    archivo = page.extract_text()

    file = open("python\h.txt","r+")
    file.write(archivo);
    file.close();


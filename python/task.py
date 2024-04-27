import requests;
import os;
from datetime import datetime;


def date():
    
    now = datetime.now();
    day = str(now.day);
    month = now.month;
    year = str(now.year);
    WEEKDAYS = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo");
    
    arrayMonths = ("enero","febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    
    monthWord = arrayMonths[month-1];
    month = str(month);

    weekday = WEEKDAYS[now.weekday()];
    
    return year,month, monthWord, day, weekday;






def dowload_save():
    
    print("hola")
    
    year = date()[0];
    month = date()[1];
    monthWord = date()[2];
    day = date()[3]; 
    
    print(date())
    archivo_delet = "python\Boletin.pdf";
    url_base = "https://boletin.precioscorabastos.com.co/wp-content/uploads/"
    url_date = f"{year}/0{month}/Boletin-25{monthWord}{year}.pdf"


    url = url_base + url_date

    res = requests.get(url);
    print(res)
    
    if os.path.exists(archivo_delet):
        os.remove(archivo_delet)
    
    if res.status_code == 200:
        with open("Boletin.pdf",'wb') as ar:
                ar.write(res.content)
                print("boletin guardado")
                




import tkinter as tk
import requests
import time
import os


def current_time():
    while (True):
        print(time.ctime())
        time.sleep(1)
        os.system('cls')


def getweather(root):
    try:
        city=textfield.get()
        api="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d9db53c6ebe4a8110caa93993b1d48d5"
        json_data=requests.get(api).json()
        condition= json_data['weather'][0]['main']
        temp=int(json_data['main']['temp']-273.15)
        temp_min = int(json_data['main']['temp_min'] - 273.15)
        temp_max = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise=time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-19800))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 19800))

        final_info = condition + "\n" + str(temp) + "℃"
        final_data = "\nMax Temperature : "+str(temp_max)+"\nMin Temperature : "+str(temp_min)+"\nPressure : "+str(pressure)+"\nHumidity : "+str(humidity)+"\nWind Speed : "+str(wind)+"\nSunRise : "+str(sunrise)+"\nSunSet : "+str(sunset)


        l1.config(text = final_info)
        l2.config(text = final_data)
    except:
        invalid="invalid city name OR there is no internet connection !! "
        i.config(text=invalid)

root = tk.Tk()
root.geometry("500x600")
root.title ("weather app")
f=("poppins",15,"bold")
t=("poppins",35,"bold")
col='gray22'
fcol='gray'



root.configure(background = col)    #backgroung color
l0=tk.Label(root,text='City/Place Name',font=t,bg= col,fg=fcol).pack()
l3=tk.Label(root ,text='powered by ajay',font='poppins 10 bold', bg = col,fg= fcol ).place(x='350',y='550')




textfield=tk.Entry(root,font=t,bg=col,fg=fcol)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getweather)

i=tk.Label(root,bg=col,fg=fcol,font ='areal 10 bold')
i.pack()

l1=tk.Label(root,font = t,bg=col,fg=fcol)
l1.pack()
l2=tk.Label(root,font=f,bg=col,fg=fcol)
l2.pack()


root.mainloop()

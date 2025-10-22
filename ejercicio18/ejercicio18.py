import tkinter as tk
app= tk.Tk() #Crea la ventana principal

palabra = tk.StringVar(app)#StringVar. Sirve para conectar el valor mostrado en los widgets
entrada = tk.StringVar(app)

app.geometry("400x400")#Tamaño de la ventana 
app.configure(background="black")#Fondo xd
tk.Wm.wm_title(app,"Helou wourld")#Titulo de la ventana 

def saludo ():
    palabra.set("Bien" + entrada.get()) #Se suma lo que el usuario ingrese(ponga "venido")

tk.Button( #Crea un boton que ejecuta una funcion
    app,
    text="Click me",
    font=("Courtier",14),
    bg="#00a8e8",
    fg="White",
    justify="left",
    relief="flat",
    command=saludo,#Al hacer click llama la funcion saludo 
).pack(     #El pack sirve para colocar el boton y que funcione
    fill=tk.BOTH,
    expand=True,
    )

tk.Label( #Muestra texto que se puede actualizar 
    app,
    text="Hey soy una etiqueta",
    textvariable=palabra, #Aca se vincula al stringvar palabra 
    fg="White",
    bg="black",
    justify="center",
    #Cuando saludo() cambia el valor de 'palabra' , la etiqueta se actualiza
).pack(
    fill=tk.BOTH,
    expand=True,
    )

tk.Entry(  #Permite ingresar texto 
    app,
    text="Hey soy una etiqueta", #Lo que el usuario excriba, se guarda en en entrada 
    fg="black",
    bg="white",
    justify="center",
    textvariable=entrada,
).pack(
    fill=tk.BOTH,
    expand=True,
    )
app.mainloop()  #Refresca la app sin cerrarse 

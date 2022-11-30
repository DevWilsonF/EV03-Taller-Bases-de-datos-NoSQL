from pymongo import MongoClient
MONGO_URL='mongodb://localhost'
cliente = MongoClient(MONGO_URL)
base_de_datos = cliente['covid']
coleccion = base_de_datos['casos']

mensaje= """\n\n********Menu********
1. Cuantos casos se registraron en Bogotá.
2. Cuantos casos se recuperaron en Bogotá.
3. Cual fue la ciudad que más se recuperaron.
4. Cual fue la ciudad que más se recuperaron siendo mujeres.
5. Cuantos fallecidos que fueron mujeres y mayores de 50 años.
6. Cuantos fallecidos que fueron hombres y menores de 50 años.
7. Cuantos casos fueron por personas del extranjero.
8. Cuantos casos se registraron en Antioquía, menores de 30 años y por persona extranjeras.
9. Cuantos casos se registraron por personas de España
10. Cuantos casos se registraron por personas de edad entre 20 y 50 años
11. salir
"""
bandera= True
while bandera:
    print(mensaje)
    opcion= int(input('ingrese una opcion: '))
    if opcion == 1:
        consulta = coleccion.count_documents({'Ciudad de ubicación': 'Bogotá D.C.'})
        print(f"Se registraron en bogota :{consulta} casos")
    elif opcion == 2:
        consulta = coleccion.count_documents({'$and':[{'Ciudad de ubicación': 'Bogotá D.C.','atención':'Recuperado'}]})
        print(f"Se recuperaron en bogota :{consulta} casos")
    elif opcion == 3:
        consulta = coleccion.aggregate([{'$match':{'atención':'Recuperado'}},{'$group':{'_id':'$Ciudad de ubicación','recuperados':{'$sum':1}}},{'$sort':{'recuperados':-1}},{'$limit':1}])
        resultado= [print(f"La ciudad en la que mas se recuperaron fue: {i}") for i in consulta]
    elif opcion == 4:
        consulta = coleccion.aggregate([{'$match':{'atención':'Recuperado','Sexo':'F'}},{'$group':{'_id':'$Ciudad de ubicación','recuperados':{'$sum':1}}},{'$sort':{'recuperados':-1}},{'$limit':1}])
        resultado= [print(f"La ciudad en la que mas mujeres se recuperaron fue: {i}") for i in consulta]
    elif opcion == 5 :
        consulta = coleccion.count_documents({'$and':[{'atención':'Fallecido','Estado':'Fallecido','Edad':{'$gte':50},'Sexo':'F'}]})
        print(f"La cantidad de mujeres que fallecieron  y que eran mayores de 50 años: {consulta}")
    elif opcion == 6 :
        consulta = coleccion.count_documents({'$and':[{'atención':'Fallecido','Estado':'Fallecido','Edad':{'$lte':50},'Sexo':'M'}]})
        print(f"La cantidad de Hombres que fallecieron  y que eran menores de 50 años:{consulta}")
    elif opcion == 7 :
        consulta = coleccion.count_documents({'País de procedencia':{'$not':{'$regex':'/COLOMBIA/'}}})
        print(f"Casos presentados por extranjeros: {consulta}")
    elif opcion == 8 :
        consulta = coleccion.count_documents({'$and':[{'Edad':{'$lte':30},'Departamento o Distrito ':'Antioquia','País de procedencia':{'$not':{'$regex':'/COLOMBIA/'}}}]})
        print(f"Casos registrados en antioquia menores de 30 años y por personas extranjeras:{consulta}")
    elif opcion == 9 :
        consulta = coleccion.count_documents({'País de procedencia':'ESPAÑA'})
        print(f"Casos registrados por personas de españa: {consulta}")
    elif opcion == 10 :
        consulta = coleccion.count_documents({'Edad':{'$gte':20,'$lte':50}})
        print(f"Casos presentados por personas entre la edad de 20 y 50 años: {consulta}")
    else:
        bandera = False
        print('saliendo...')
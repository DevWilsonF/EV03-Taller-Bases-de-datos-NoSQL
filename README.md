# EV03-Taller-Bases-de-datos-NoSQL
- Autor:
- Wilson: Fabian Cruz Andrade
- Ficha: 2502640
- Centro Gestión de Mercados, Logística y Tecnologías de la Información

# Desarrollo de la actividad

Cargar los datos que se encuentran en “DATOS/COVID19/COVID19-JULIO2020.csv” en una base de datos MONGODB llamada “COVID”, en la
colección llamada “CASOS”.

![image](https://user-images.githubusercontent.com/108008266/204658340-3775ed08-6e04-49a0-9b6b-134e9a726056.png)

# importando datos

![image](https://user-images.githubusercontent.com/108008266/204658731-910255c0-ed11-4790-bd55-6c666824bcbf.png)

![image](https://user-images.githubusercontent.com/108008266/204659366-77e3a7df-4d4a-4829-b27f-327642901e43.png)

# Consultas

El desarrollo de las consultas se realizaron en un programa de python en el cual se instalo e importo la libreria
de mongoDB con el comando pip install pymongo 
se establecio la url  en la cual se va a conectar a las bases de datos tambien se instancia  la url en una variable la cual 
se usara para poder indicarle la base de datos a la cual se esta accediendo y por ultimo  se instancia  en una variable la
coleccion a la cual tendremos acceso y podremos realizar las consultas.

![image](https://user-images.githubusercontent.com/108008266/204684946-268214ea-c270-4f03-90fe-6626b47996b2.png)

creamos un menu en el cual podemos acceder a las consultas para el desarrollo de la evidencia en el cual 
por medio de un ciclo "while" podemos acceder a cada consulta  sin nesesidad de ejecutar varias veces el archivo

![image](https://user-images.githubusercontent.com/108008266/204685196-64fcfafc-a65f-4aff-8aa4-3c17b0b6974f.png)


![image](https://user-images.githubusercontent.com/108008266/204685426-dc643443-059b-48a7-9b2e-653f1a2e600a.png)



1. Cuantos casos se registraron en Bogotá.

![image](https://user-images.githubusercontent.com/108008266/204686647-f0db9b9c-0a90-493a-a32c-e0dac7fbcac8.png)


2. Cuantos casos se recuperaron en Bogotá.

![image](https://user-images.githubusercontent.com/108008266/204686696-91907fe4-9461-42a8-b241-f96d27a23212.png)


3. Cual fue la ciudad que más se recuperaron.

![image](https://user-images.githubusercontent.com/108008266/204686740-bda64f2e-fa05-4844-ab96-bad35a2618ae.png)


4. Cual fue la ciudad que más se recuperaron siendo mujeres.

![image](https://user-images.githubusercontent.com/108008266/204686782-87ed7cb3-4ba9-441a-82aa-41247a4d7561.png)


5. Cuantos fallecidos que fueron mujeres y mayores de 50 años.

![image](https://user-images.githubusercontent.com/108008266/204686837-2dbc5523-9f79-401c-aa0d-8d267df53675.png)


6. Cuantos fallecidos que fueron hombres y menores de 50 años.

![image](https://user-images.githubusercontent.com/108008266/204686885-57e5cfd6-2a86-41dd-a435-d700f9bc367f.png)


7. Cuantos casos fueron por personas del extranjero.

![image](https://user-images.githubusercontent.com/108008266/204686944-9c338efa-88bf-4227-8489-f791f1026905.png)


8. Cuantos casos se registraron en Antioquía, menores de 30 años y por persona extranjeras.

![image](https://user-images.githubusercontent.com/108008266/204687024-ad9026f6-7f7b-46cd-9f65-c9122c65c9e9.png)


9. Cuantos casos se registraron por personas de España

![image](https://user-images.githubusercontent.com/108008266/204687083-a130bcca-3347-4f82-b5d6-4d0d4d6c05a1.png)


10. Cuantos casos se registraron por personas de edad entre 20 y 50 años

![image](https://user-images.githubusercontent.com/108008266/204687152-3b58279f-8fa7-456b-894f-42d257c4423b.png)

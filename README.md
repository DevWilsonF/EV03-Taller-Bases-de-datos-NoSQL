# EV03-Taller-Bases-de-datos-NoSQL
- Autor:
- Wilson: Fabian Cruz Andrade
- Ficha: 2502640
- Centro Gestión de Mercados, Logística y Tecnologías de la Información

# Desarrollo de la actividad

Cargar los datos que se encuentran en “DATOS/COVID19/COVID19-JULIO2020.csv” en una base de datos MONGODB llamada “COVID”, en la
colección llamada “CASOS”.

![image](https://user-images.githubusercontent.com/108008266/204689110-f096828c-05e3-49ad-a46d-bfb1891e6d89.png)


# importando datos

![image](https://user-images.githubusercontent.com/108008266/204658731-910255c0-ed11-4790-bd55-6c666824bcbf.png)

![image](https://user-images.githubusercontent.com/108008266/204689265-7c36ce23-4dfd-48ba-bd5c-efa0c11322d4.png)


# Consultas

El desarrollo de las consultas se realizaron en un programa de python en el cual se instaló e importo la librería de MongoDB con el comando pip install pymongo se estableció la url en la cual se va a conectar a las bases de datos también sé instancia la url en una variable la cual se usara para poder indicarle la base de datos a la cual se está accediendo y por último sé instancia en una variable la colección a la cual tendremos acceso y podremos realizar las consultas.

![image](https://user-images.githubusercontent.com/108008266/204688972-d24924bc-9985-4769-aee3-4dea4eb96a97.png)

Creamos un menú en el cual podemos acceder a las consultas para el desarrollo de la evidencia en el cual 
por medio de un ciclo "while" podemos acceder a cada consulta sin necesidad de ejecutar varias veces el archivo

![image](https://user-images.githubusercontent.com/108008266/204685196-64fcfafc-a65f-4aff-8aa4-3c17b0b6974f.png)


![image](https://user-images.githubusercontent.com/108008266/204685426-dc643443-059b-48a7-9b2e-653f1a2e600a.png)



1. Cuantos casos se registraron en Bogotá.

![image](https://user-images.githubusercontent.com/108008266/204687289-d6ed80dd-48b1-4098-9aa9-4d3e2baf970a.png)


![image](https://user-images.githubusercontent.com/108008266/204686647-f0db9b9c-0a90-493a-a32c-e0dac7fbcac8.png)


2. Cuantos casos se recuperaron en Bogotá.

![image](https://user-images.githubusercontent.com/108008266/204687332-2629902c-63ec-4d8d-b79a-88677f59880e.png)


![image](https://user-images.githubusercontent.com/108008266/204686696-91907fe4-9461-42a8-b241-f96d27a23212.png)


3. Cual fue la ciudad que más se recuperaron.

![image](https://user-images.githubusercontent.com/108008266/204687380-3207fd61-4d4e-42f6-a9e5-b723c4dc2b2b.png)


![image](https://user-images.githubusercontent.com/108008266/204686740-bda64f2e-fa05-4844-ab96-bad35a2618ae.png)


4. Cual fue la ciudad que más se recuperaron siendo mujeres.

![image](https://user-images.githubusercontent.com/108008266/204687435-c01b3c05-514b-454a-aeb0-711da2798c93.png)


![image](https://user-images.githubusercontent.com/108008266/204686782-87ed7cb3-4ba9-441a-82aa-41247a4d7561.png)


5. Cuantos fallecidos que fueron mujeres y mayores de 50 años.

![image](https://user-images.githubusercontent.com/108008266/204687491-24dce94b-d184-42e4-865a-12c287f75802.png)


![image](https://user-images.githubusercontent.com/108008266/204686837-2dbc5523-9f79-401c-aa0d-8d267df53675.png)


6. Cuantos fallecidos que fueron hombres y menores de 50 años.

![image](https://user-images.githubusercontent.com/108008266/204687539-d78d5360-6c97-4697-ab72-8027cc53c026.png)


![image](https://user-images.githubusercontent.com/108008266/204686885-57e5cfd6-2a86-41dd-a435-d700f9bc367f.png)


7. Cuantos casos fueron por personas del extranjero.

![image](https://user-images.githubusercontent.com/108008266/204687587-77d3f1dd-196b-4587-afe3-432af6ec91bd.png)


![image](https://user-images.githubusercontent.com/108008266/204686944-9c338efa-88bf-4227-8489-f791f1026905.png)


8. Cuantos casos se registraron en Antioquía, menores de 30 años y por persona extranjeras.

![image](https://user-images.githubusercontent.com/108008266/204687625-c4253166-83de-4aab-a702-4e50064ba84f.png)


![image](https://user-images.githubusercontent.com/108008266/204687024-ad9026f6-7f7b-46cd-9f65-c9122c65c9e9.png)


9. Cuantos casos se registraron por personas de España

![image](https://user-images.githubusercontent.com/108008266/204687662-874b7014-26d1-4a93-b8c2-bbe8125bd0ce.png)


![image](https://user-images.githubusercontent.com/108008266/204687083-a130bcca-3347-4f82-b5d6-4d0d4d6c05a1.png)


10. Cuantos casos se registraron por personas de edad entre 20 y 50 años

![image](https://user-images.githubusercontent.com/108008266/204687694-d0ebfed2-94db-470c-9460-66d1bf447c3a.png)


![image](https://user-images.githubusercontent.com/108008266/204687152-3b58279f-8fa7-456b-894f-42d257c4423b.png)

# LoginApp-Docker-Jenkins
Aplikacja która odpowiada za logowanie lub tworzenia konta dla użytkownika, wykorzystane technologie to MongoDB, MongoExpress, Docker, Jenkins, Kubernetes

Stworzone zostały 2 Dockerfile, jeden tworzył obraz aplikacji a drugi testów:
Tworzony jest katalog wewnątrz kontenera, w przypadku Dockerfile dla app nazywa się on /app , instalowane są wszystkie zależności ustalone w pliku requirements.txt. 
Zastosowany został multi-stage building czyli z każdym kolejnym stage korzystam z mniejszego obrazu dockerowego aby zapewnić to że aplikacja będzie zajmowała możliwie mało miejsca.

![image](https://github.com/user-attachments/assets/1e4dc33d-8583-4767-8afe-6f532f174457)

W przypadku Dockerfile dla testów również tworzony jest katalog o nazwie /app-tests, kopiowane są wszystkie zaleznosci a tekże klasy które potrzedne są do testów.
Tworzone sa 2 podkatalogi w karalofu /app-tests jeden gdzie będzie znajdowała sie aplikacja a drugi z testami

![image](https://github.com/user-attachments/assets/0f922de0-1bd6-44ce-9267-0d09479c77d8)


Stworzony też zosrał Docker compose, uruchamiana jest baza danych mongodb oraz mongo express a także aplikacja i testy:
Do bazy danych zastosowane zostały volumes aby bo usunięciu lub gdy coś sie popsuje zapisane wczesniej wartości były dostępne w bazie danych.
Każdy kontener jest umieszczony w tej samej sieci dockerowej aby mogły się między sobą komunikować. 

![image](https://github.com/user-attachments/assets/19874f84-6693-4d79-a35c-4c8cee8e9877)


![image](https://github.com/user-attachments/assets/1400be9a-bba8-4080-86b7-2e7f760bb7e1)

Jenkinsfile

![image](https://github.com/user-attachments/assets/c41d78dc-8303-46c4-b5d2-8d4ed79eba32)

Do lokalnego przetesowania działania kontenerów wykorzystuję komendę:
docker-compose up -d mongo mongo-express && docker-compose run --rm --service-ports -it test && docker-compose run --service-ports -it app
Uruchamia się mongodb i mongo-express w tle a także testy i aplikacja. Aplikacja i testy uruchamiaja się w trybie interaktywnym, dodatkowo po zakończeniu testów konetener z nimi zostaje usunięty.

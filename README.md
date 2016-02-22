viihdepython
============

Elisa Viihde – Python-skriptejä. Toimii ainakin Python versiolla 2.7 ja 
3.5.

Skriptit kysyvät luvan ennen kuin tekevät siirto/poisto -operaatioita.

Kirjautumistunnisteita tai -keksiä ei tallenneta, joten salasana kysytään
erikseen jokaisella käyttökerralla.

Scripteille voi antaa input parametreja myös komentoriviparametrien avulla 
jos scriptejä halutaan ajaa esim. cronilla.

Mahdolliset komentoriviparametrit saa näkyviin -h vivulla.

delete_duplicates.py
--------------------

Etsii ja poistaa duplikaatit halutusta kansiosta (tai kaikista tallenteista).
Säilyttää ensimmäisen tallenteen.

Huomaa, että duplikaattien tunnistus tehdään ohjelman nimen ja kuvauksen
perusteella, joten esimerkiksi "Yle Uutiset" / "Mukana talous ja kulttuuri"
-nimiset lähetykset tunnistetaan väärin duplikaateiksi.

move_simpsonit.py
-----------------

Siirtää Simpsonit-kansion tallenteet alikansioihin kausien mukaisesti.
Käyttää simpsonit.orgin tietoja jaotteluun.

Riippuvuudet
-----------------------

* BeautifulSoup
* python-requests

Asennus pip:llä python:

$ pip install -r requirements.txt


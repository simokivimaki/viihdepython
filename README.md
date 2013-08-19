viihdepython
============

Elisa Viihde – Python-skriptejä. Toimii ainakin Python versiolla 2.7.

Skriptit kysyvät luvan ennen kuin tekevät siirto/poisto -operaatioita.

Kirjautumistunnisteita tai -keksiä ei tallenneta, joten salasana kysytään
erikseen jokaisella käyttökerralla.

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

Mukana olevat kirjastot
-----------------------

* http://www.crummy.com/software/BeautifulSoup/ (MIT license)
* http://python-requests.org (Apache 2 license)

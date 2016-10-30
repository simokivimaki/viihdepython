viihdepython
============

Elisa Viihde – Python-skriptejä. Toimii ainakin Python versiolla 2.7.

Skriptit kysyvät luvan ennen kuin tekevät siirto/poisto -operaatioita.

Kirjautumistunnisteita tai -keksiä ei tallenneta, joten salasana kysytään
erikseen jokaisella käyttökerralla.

Scripteille voi antaa input parametreja myös komentoriviparametrien avulla 
jos scriptejä halutaan ajaa esim. cronilla.

Mahdolliset komentoriviparametrit saa näkyviin -h vivulla.

asennus
-------

`pip install git+https://github.com/kattelus/viihdepython.git`

delete_duplicates
-----------------

Etsii ja poistaa duplikaatit halutusta kansiosta (tai kaikista tallenteista).
Säilyttää ensimmäisen tallenteen.

Huomaa, että duplikaattien tunnistus tehdään ohjelman nimen ja kuvauksen
perusteella, joten esimerkiksi "Yle Uutiset" / "Mukana talous ja kulttuuri"
-nimiset lähetykset tunnistetaan väärin duplikaateiksi.

move_simpsonit
--------------

Siirtää Simpsonit-kansion tallenteet alikansioihin kausien mukaisesti.
Käyttää simpsonit.orgin tietoja jaotteluun.

kaantaminen ja kehittaminen (esimerkki linux fishshell)
-------------------------------------------------------

```
virtualenv venv
source venv/bin/activate.fish
pip install pybuilder
pyb install_dependencies install
```

Katso [pybuilder](http://pybuilder.github.io/)

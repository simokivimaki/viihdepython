viihdepython
============

Elisa Viihde – Python-skriptejä. Toimii ainakin Python versioilla 2.7 ja 
3.5.

Skriptit kysyvät luvan ennen kuin tekevät siirto/poisto -operaatioita.

Kirjautumistunnisteita tai -keksiä ei tallenneta, joten salasana kysytään
erikseen jokaisella käyttökerralla.

Scripteille voi antaa input parametreja myös komentoriviparametrien avulla 
jos scriptejä halutaan ajaa esim. cronilla.

Mahdolliset komentoriviparametrit saa näkyviin -h vivulla.

asennus
-------

`pip install git+https://github.com/simokivimaki/viihdepython.git`

macOS:n mukana tuleva python2 ei sisällä pip:ä, joten asenna ensin python3
lataamalla asennuspaketti osoitteesta https://www.python.org/downloads/mac-osx/
tai käyttämällä esim. Homebrew-pakettienhallintaa. Asennuksen jälkeen
pip3-komento on käytössä.

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

move_rillithuurussa
-------------------

Siirtää Rillit Huurussa -kansion tallenteet alikansioihin kausien mukaisesti.
Käyttää https://fi.wikipedia.org/wiki/Luettelo_televisiosarjan_Rillit_huurussa_jaksoista
-sivua tietojen jaotteluun.

kaantaminen ja kehittaminen (esimerkki linux fishshell)
-------------------------------------------------------

```
virtualenv venv
source venv/bin/activate.fish
pip install pybuilder
pyb install_dependencies install
```

Katso [pybuilder](http://pybuilder.github.io/)

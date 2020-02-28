## Asennusohje

* Sovelluksen k�ytt�mist� varten koneella tulee olla asennettuna python3 sek� Pythonin pip.

* Sovelluksen toimintaa varten tulee asentaa Pythonin virtuaaliymp�rist� projektin juurikansioon komennolla 
`python3 -m venv venv`

* Projektin tarvitsemat riippuvuudet l�ytyv�t tiedostosta [requirements.txt](https://github.com/AgdaHTH/ruokintasovellus/blob/master/requirements.txt), 
josta ne voi asentaa pipin avulla: `pip install -r requirements.txt`

* Sovelluksen k�ytt�� on kuvailtu yksityiskohtaisesti [k�ytt�tapaukset-tiedostossa](https://github.com/AgdaHTH/ruokintasovellus/blob/master/documentation/userstories.md)

* Sovellus toimii my�s [Heroku-palvelussa](https://ruokintasovellus.herokuapp.com/), 
jolloin sit� ei tarvitse asentaa omalle koneelle.

* Sovellus k�ytt�� paikallisesti SQLite-tietokantaa ja Herokussa PostgreSQL-tietokantaa.
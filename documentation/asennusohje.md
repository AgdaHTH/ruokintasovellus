## Asennusohje

* Sovelluksen käyttämistä varten koneella tulee olla asennettuna python3 sekä Pythonin pip.

* Sovelluksen toimintaa varten tulee asentaa Pythonin virtuaaliympäristö projektin juurikansioon komennolla 
`python3 -m venv venv`

* Projektin tarvitsemat riippuvuudet löytyvät tiedostosta [requirements.txt](https://github.com/AgdaHTH/ruokintasovellus/blob/master/requirements.txt), 
josta ne voi asentaa pipin avulla: `pip install -r requirements.txt`

* Sovelluksen käyttöä on kuvailtu yksityiskohtaisesti [käyttötapaukset-tiedostossa](https://github.com/AgdaHTH/ruokintasovellus/blob/master/documentation/userstories.md)

* Sovellus toimii myös [Heroku-palvelussa](https://ruokintasovellus.herokuapp.com/), 
jolloin sitä ei tarvitse asentaa omalle koneelle.

* Sovellus käyttää paikallisesti SQLite-tietokantaa ja Herokussa PostgreSQL-tietokantaa.
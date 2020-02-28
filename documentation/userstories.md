## Käyttötapaukset

Sovelluksessa on kaksi käyttäjäryhmää, eläinten omistajat ja niiden ruokkijat. 

Autorisointi toimii tällä hetkellä niin, että yhdelle käyttäjätyypille (eläimen omistaja) on mahdollista 
kirjautua sisään sovellukseen ja toiminnallisuus määrittyy tämän perusteella. Kukin omistaja pääsee päivittämään 
vain oman eläimensä tietoja. Nykyisessä muodossaan sovelluksessa ei ole tarvetta admin-tasoiselle käyttäjälle.

### Seuraavat toiminnot ovat mahdollisia *eläimen omistajalle*: 

* Eläimen omistaja voi luoda itselleen profiilin järjestelmään välilehdeltä *Register*.

* Kun omistajalla on profiili ja hän on kirjautunut sisään, hän voi lisätä itselleen 
eläimen välilehdeltä *Add an animal*.

* Alasivulta *Show animal details* kirjautunut käyttäjä (eli eläimen omistaja) näkee kyseisen eläimen tiedot ja voi
lisätä eläimelleen syötettävän ruuan.

* Välilehdellä *Info for current user* omistaja näkee näkee yhteenvedon eläimiään koskevista tiedoista. 

* Siellä hän voi myös merkitä jos eläin on sairaana sekä poistaa eläimen tiedot tietokannasta. 
Huomaa, että Delete animal -nappi poistaa eläimen tiedot välittömästi.

* Sivulla *Info for current user* omistaja näkee, montako eläintä hänellä on ja mikä on eläinten syömien
ruokien hintojen keskiarvo. Lisäksi omistaja näkee yhteenvedon siitä, mitä ruokia hänen eläimensä syövät.

Kirjautuneen käyttäjän eläimet:

    "SELECT * FROM Animal 
         JOIN Account ON Account.id = Animal.account_id
         WHERE account_id = :account_id"

Kirjautuneen käyttäjän eläinten lukumäärä:

    "SELECT COUNT(Account.id) FROM Animal
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Animal.account_id = :account_id"

Kirjautuneen käyttäjän eläinten syömien ruokien hintojen keskiarvo:

    "SELECT AVG(Food.price) FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id 
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Account.id = :account_id"

Listaus kirjautuneen käyttäjän eläinten syömistä ruuista:

    "SELECT Food.name, Animal.name FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id 
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Account.id = :account_id
         GROUP BY Food.name" 

### Seuraavat toiminnot ovat mahdollisia *eläinten hoitajalle*:

* Järjestelmän käyttäjä (eli eläinten ruokkija) voi selata eri eläinten tietoja sivulla *List animals*, 
josta on linkki kunkin eläimen tietoihin: *Show animal details*. Tätä varten käyttäjän ei tarvitse kirjautua 
järjestelmään. 

* Etusivulle listautuvat myös kaikki tietokannasta löytyvät ruuat, joiden hintatietoja voi katsella sivulta
*Show food details*.

* Linkistä *Add a new food* pääsee lisäämään tietokantaan uuden ruuan (ruokien nimet ovat uniikkeja, joten sovellus ei hyväksy toista samannimistä ruokaa).

* Ruuan voi poistaa kohdasta *Delete food*. 
 
Hintatietoja voi muuttaa sivulta *Edit food*:  

    "UPDATE Food
         SET price = :newprice
         WHERE id = :food_id"

Etusivun linkistä *Show animals* näkee kutakin ruokaa syövät eläimet:

    "SELECT Animal.name FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id
         WHERE Food.id = :food_id"

Eläinten hoitajalle eli kirjautumattomalle käyttäjälle alasivu *Show animal details* näyttää eläimen 

   nimen  
   omistajan nimen   
   eläimen terveydentilan  
   eläimelle syötettävät ruuat  
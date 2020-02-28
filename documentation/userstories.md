## K�ytt�tapaukset

Sovelluksessa on kaksi k�ytt�j�ryhm��, el�inten omistajat ja niiden ruokkijat. 

Autorisointi toimii t�ll� hetkell� niin, ett� yhdelle k�ytt�j�tyypille (el�imen omistaja) on mahdollista 
kirjautua sis��n sovellukseen ja toiminnallisuus m��rittyy t�m�n perusteella. Kukin omistaja p��see p�ivitt�m��n 
vain oman el�imens� tietoja. Nykyisess� muodossaan sovelluksessa ei ole tarvetta admin-tasoiselle k�ytt�j�lle.

### Seuraavat toiminnot ovat mahdollisia *el�imen omistajalle*: 

* El�imen omistaja voi luoda itselleen profiilin j�rjestelm��n v�lilehdelt� *Register*.

* Kun omistajalla on profiili ja h�n on kirjautunut sis��n, h�n voi lis�t� itselleen 
el�imen v�lilehdelt� *Add an animal*.

* Alasivulta *Show animal details* kirjautunut k�ytt�j� (eli el�imen omistaja) n�kee kyseisen el�imen tiedot ja voi
lis�t� el�imelleen sy�tett�v�n ruuan.

* V�lilehdell� *Info for current user* omistaja n�kee n�kee yhteenvedon el�imi��n koskevista tiedoista. 

* Siell� h�n voi my�s merkit� jos el�in on sairaana sek� poistaa el�imen tiedot tietokannasta. 
Huomaa, ett� Delete animal -nappi poistaa el�imen tiedot v�litt�m�sti.

* Sivulla *Info for current user* omistaja n�kee, montako el�int� h�nell� on ja mik� on el�inten sy�mien
ruokien hintojen keskiarvo. Lis�ksi omistaja n�kee yhteenvedon siit�, mit� ruokia h�nen el�imens� sy�v�t.

Kirjautuneen k�ytt�j�n el�imet:

    "SELECT * FROM Animal 
         JOIN Account ON Account.id = Animal.account_id
         WHERE account_id = :account_id"

Kirjautuneen k�ytt�j�n el�inten lukum��r�:

    "SELECT COUNT(Account.id) FROM Animal
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Animal.account_id = :account_id"

Kirjautuneen k�ytt�j�n el�inten sy�mien ruokien hintojen keskiarvo:

    "SELECT AVG(Food.price) FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id 
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Account.id = :account_id"

Listaus kirjautuneen k�ytt�j�n el�inten sy�mist� ruuista:

    "SELECT Food.name, Animal.name FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id 
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Account.id = :account_id
         GROUP BY Food.name" 

### Seuraavat toiminnot ovat mahdollisia *el�inten hoitajalle*:

* J�rjestelm�n k�ytt�j� (eli el�inten ruokkija) voi selata eri el�inten tietoja sivulla *List animals*, 
josta on linkki kunkin el�imen tietoihin: *Show animal details*. T�t� varten k�ytt�j�n ei tarvitse kirjautua 
j�rjestelm��n. 

* Etusivulle listautuvat my�s kaikki tietokannasta l�ytyv�t ruuat, joiden hintatietoja voi katsella sivulta
*Show food details*.

* Linkist� *Add a new food* p��see lis��m��n tietokantaan uuden ruuan (ruokien nimet ovat uniikkeja, joten sovellus ei hyv�ksy toista samannimist� ruokaa).

* Ruuan voi poistaa kohdasta *Delete food*. 
 
Hintatietoja voi muuttaa sivulta *Edit food*:  

    "UPDATE Food
         SET price = :newprice
         WHERE id = :food_id"

Etusivun linkist� *Show animals* n�kee kutakin ruokaa sy�v�t el�imet:

    "SELECT Animal.name FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id
         WHERE Food.id = :food_id"

El�inten hoitajalle eli kirjautumattomalle k�ytt�j�lle alasivu *Show animal details* n�ytt�� el�imen 

   nimen  
   omistajan nimen   
   el�imen terveydentilan  
   el�imelle sy�tett�v�t ruuat  
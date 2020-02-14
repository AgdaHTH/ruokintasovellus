Tietokanta sisältää tiedot joukosta eläimiä, niiden omistajista sekä kunkin eläimen ruokinnasta ja terveydetilasta.
Käyttöliittymän kautta seuraavat toiminnot ovat mahdollisia:

1. Omistaja voi luoda profiilin järjestelmään välilehdeltä *Add a new user*.

2. Kun omistajalla on profiili ja hän on kirjautunut sisään, hän voi lisätä itselleen 
eläimen välilehdeltä *Add an animal*.

3. Kirjautuneena omistaja voi selata eläimiään ja yhteenvetoa niiden ruuista välilehdellä *Info for current user*. 
Siellä hän voi myös lisätä eläimelleen syötettävän ruuan, merkitä jos eläin on sairaana sekä poistaa eläimen 
tietokannasta. Huomaa, että Delete animal -nappi poistaa eläimen tiedot välittömästi. 

4. Sivun alareunassa on listaus kaikista kirjautuneen käyttäjän eläinten syömistä ruuista. Se tulostaa 
seuraavan SQL-kyselyn tulokset:

"SELECT Food.name, Animal.name FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id 
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Account.id = :account_id
         GROUP BY Food.name" 

5. Järjestelmän käyttäjä (eli eläinten ruokkija) voi selata eri eläinten ruokintatietoja sivuilla *List animals*, 
josta on linkki kunkin eläimen tietoihin: *Show animal details*. Eläimen tiedoissa on myös merkittynä, onko 
eläin sairas vai terve. Tätä varten käyttäjän ei tarvitse kirjautua järjestelmään. 

6. Alasivu *Show animal details* näyttää eläimen nimen, omistajan nimen, eläimen terveydentilan ja eläimelle 
syötettävät ruuat.

7. Autorisointi toimii tällä hetkellä niin, että yhdelle käyttäjätyypille on mahdollista kirjautua sisään 
sovellukseen ja toiminnallisuus määrittyy tämän perusteella. Nykyisessä muodossa sovelluksessa ei ole tarvetta
admin-tasoiselle käyttäjälle.
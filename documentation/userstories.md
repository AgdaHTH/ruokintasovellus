Tietokanta sis�lt�� tiedot joukosta el�imi�, niiden omistajista sek� kunkin el�imen ruokinnasta ja terveydetilasta.
K�ytt�liittym�n kautta seuraavat toiminnot ovat mahdollisia:

1. Omistaja voi luoda profiilin j�rjestelm��n v�lilehdelt� *Add a new user*.

2. Kun omistajalla on profiili ja h�n on kirjautunut sis��n, h�n voi lis�t� itselleen 
el�imen v�lilehdelt� *Add an animal*.

3. Kirjautuneena omistaja voi selata el�imi��n ja yhteenvetoa niiden ruuista v�lilehdell� *Info for current user*. 
Siell� h�n voi my�s lis�t� el�imelleen sy�tett�v�n ruuan, merkit� jos el�in on sairaana sek� poistaa el�imen 
tietokannasta. Huomaa, ett� Delete animal -nappi poistaa el�imen tiedot v�litt�m�sti. 

4. Sivun alareunassa on listaus kaikista kirjautuneen k�ytt�j�n el�inten sy�mist� ruuista. Se tulostaa 
seuraavan SQL-kyselyn tulokset:

"SELECT Food.name, Animal.name FROM Food
         LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id
         LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id 
         LEFT JOIN Account ON Account.id = Animal.account_id
         WHERE Account.id = :account_id
         GROUP BY Food.name" 

5. J�rjestelm�n k�ytt�j� (eli el�inten ruokkija) voi selata eri el�inten ruokintatietoja sivuilla *List animals*, 
josta on linkki kunkin el�imen tietoihin: *Show animal details*. El�imen tiedoissa on my�s merkittyn�, onko 
el�in sairas vai terve. T�t� varten k�ytt�j�n ei tarvitse kirjautua j�rjestelm��n. 

6. Alasivu *Show animal details* n�ytt�� el�imen nimen, omistajan nimen, el�imen terveydentilan ja el�imelle 
sy�tett�v�t ruuat.

7. Autorisointi toimii t�ll� hetkell� niin, ett� yhdelle k�ytt�j�tyypille on mahdollista kirjautua sis��n 
sovellukseen ja toiminnallisuus m��rittyy t�m�n perusteella. Nykyisess� muodossa sovelluksessa ei ole tarvetta
admin-tasoiselle k�ytt�j�lle.
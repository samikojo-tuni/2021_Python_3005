'''
Harjoitus 1

Kirjoita funktio, joka arpoo numeron väliltä 1-9 (sekä 1 että 9 mukana joukossa).
Funktio kehottaa käyttäjää arvaamaan tämän numeron. Funktio päättyy, kun käyttäjä
arvaa numeron oikein. Jos käyttäjä arvaa numeron väärin, funktio kertoo, onko
pienempi vai suurempi kuin käyttäjän arvaus. Funktio pitää myös kirjaa käyttäjän
arvausten määrästä. Funktion lopussa funktio tulostaa montako arvausta käyttäjä
tarvitsi numeron arvaamiseen.
'''

'''
Harjoitus 2

Alla on esitetty Bubble Sort -algoritmi pseudokoodina.

"Pseudokoodi on tietojenkäsittelytieteessä ohjelmointikielen tapaista koodia,
jonka tarkoituksena on piilottaa eri ohjelmointikielten väliset syntaksierot ja 
jättää jäljelle vain algoritmin perusrakenne" (Wikipedia, Pseudokoodi).
https://fi.wikipedia.org/wiki/Pseudokoodi, viitattu 8.4.2021

Bubble Sort on algoritmi, joka järjestää listan. Bubble Sort on varsin
hidas järjestysalgoritmi, mutta sen toiminta on helppo ymmärtää.
Tämän vuoksi Bubble Sortia käytetään usein esimerkkinä algoritmeja opiskeltaessa.

Tehtävä: Kirjoita pseudokoodia apuna käyttäen Python-funktio bubble_sort, joka järjestää
listan pienimmästä alkiosta suurimpaan. 

Source: https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

procedure bubbleSort( list : array of items )

   loop = list.count;
   
   for i = 0 to loop-1 do:
      swapped = false
		
      for j = 0 to loop-1 do:
      
         /* compare the adjacent elements */   
         if list[j] > list[j+1] then
            /* swap them */
            swap( list[j], list[j+1] )		 
            swapped = true
         end if
         
      end for
      
      /*if no number was swapped that means 
      array is sorted now, break the loop.*/
      
      if(not swapped) then
         break
      end if
      
   end for
   
end procedure return list
'''

'''
Harjoitus 3:

Kirjoita funktio, joka tarkistaa, onko listassa duplikaatteja.
'''

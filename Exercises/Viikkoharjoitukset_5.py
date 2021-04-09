import random

'''
Harjoitus 1

Kirjoita funktio, joka arpoo numeron väliltä 1-9 (sekä 1 että 9 mukana joukossa).
Funktio kehottaa käyttäjää arvaamaan tämän numeron. Funktio päättyy, kun käyttäjä
arvaa numeron oikein. Jos käyttäjä arvaa numeron väärin, funktio kertoo, onko
pienempi vai suurempi kuin käyttäjän arvaus. Funktio pitää myös kirjaa käyttäjän
arvausten määrästä. Funktion lopussa funktio tulostaa montako arvausta käyttäjä
tarvitsi numeron arvaamiseen.
'''
def guess_number():
    num = random.randint(1,9)

    guesses = 0

    guess = 0

    while guess != num:
        guess = 0
        while guess == 0:
            try:
                guess = int(input("Guess a number > "))

                if guess < 1 or guess > 9:
                    print("Syötä numero väliltä 1-9")
                    guess = 0
            
            except ValueError:
                print("Syötä numero")
            

        guesses += 1

        if num < guess:
            print("Number is lower than your guess")
        elif num > guess:
            print("Number is greater than your guess")
    
    print(f"You guessed the number with {guesses} guesses")

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
def bubble_sort(item_list):
    items = len(item_list)
    for i in range(items - 1):
        swapped = False

        for j in range(items-1):
            if item_list[j] > item_list[j+1]:
                item_list[j], item_list[j+1] = item_list[j+1], item_list[j]
                swapped = True
        
        if not sorted:
            break


'''
Harjoitus 3:

Kirjoita funktio, joka tarkistaa, onko listassa duplikaatteja.
'''
def has_duplicates(items):
    bubble_sort(items)
    for i in range(1, len(items)):
        if items[i-1] == items[i]:
            return True
    
    return False


def main():
    # Harjoitus 1
    guess_number()

    # Harjoitus 2
    items = [6,3,6,3,8,0,5,3,7,3,2,1]
    bubble_sort(items)
    print(items)

    # Harjoitus 3
    print(f"Has {items} duplicates? {has_duplicates(items)}")
    items = [3,8,5,1,2,7,6,9,4]
    print(f"Has {items} duplicates? {has_duplicates(items)}")

if __name__ == "__main__":
    main()
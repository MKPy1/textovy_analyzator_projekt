"""
author = Martin Kulišťák
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

# databáze uživatelů
databaze = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# předdefinovaný oddělovac
separator = "-" * 40

# zadání vstupních údajů a podmínky pro pokračování
input_name = input("Your name: ")
input_pass = input("Your pass: ")

print(separator)

if databaze.get(input_name) == input_pass:
    print("Welcome to the app, " + str(input_name))
    print("We have " + str(len(TEXTS)) + " texts to be analyzed.")

    print(separator)

    enter_index = input("Enter a number btw 1 and 3 to select: ")

    print(separator)

    if not enter_index.isdigit():
        print("Wrong choice!")
        exit()

    enter_index = int(enter_index)
    if not 0 < enter_index <= len(TEXTS):
        print("You can enter only digits btw 1 and 3!")
        exit()
    else:
        text = TEXTS[enter_index - 1]

        # vytvoření nového slovníku - pro závěrečný graf
        new_dictionary_first = {}
        new_dictionary_second = {}
        new_dictionary_third = {}

        # úprava textu - rozdělení a očištění
        words_split = text.split()
        words_clean = [word.strip(".:,!?") for word in text.split() if word.strip(".:,!?") != ""]

        for i in words_clean:
            new_dictionary_first[len(i)] = new_dictionary_first.setdefault(len(i), 0) + 1
            new_dictionary_second[len(i)] = new_dictionary_second.setdefault(len(i), 0) + 1
            new_dictionary_third[len(i)] = new_dictionary_third.setdefault(len(i), 0) + 1

        # konverze na list tuplů a seřazení
        new_dictionary_first = sorted(new_dictionary_first.items(), key=lambda x: x[0])
        new_dictionary_second = sorted(new_dictionary_second.items(), key=lambda x: x[0])
        new_dictionary_third = sorted(new_dictionary_third.items(), key=lambda x: x[0])

        # vytvoření nového slovníku, využití list comprehension a výpočet jednotlivých statistik
        new_dictionary = {}
        for i, text in enumerate(TEXTS, 0):
            longest_string = max(words_clean, key=len)

            # list({word: words_clean.count(word) for word in words_clean})
            new_dictionary[f"{i}"] = {"number_words": len(words_clean),
                                      "title_words_upper": sum(1 for word in words_clean if word[0].isupper()),
                                      "upper_words": sum(
                                          1 for word in words_clean if word.isupper() and not word[0].isdigit()),
                                      "lower_words": sum(1 for word in words_clean if word.islower()),
                                      "numeric": sum(1 for word in words_clean if word.isnumeric()),
                                      "sum_numbers": sum(
                                          [int(word) for word in words_clean if type(word) == int or word.isdigit()]),
                                      "len_numbers": list(
                                          {len(word): words_clean.count(word) for word in words_clean if
                                           len(word) in range(1, len(longest_string) + 1)}),
                                      }

        # výpis dle daného výběru, využití formátování pro přehlednější zobrazení
        if enter_index == 1:
            first_len = new_dictionary["0"]["number_words"]
            first_title = new_dictionary["0"]["title_words_upper"]
            first_upper = new_dictionary["0"]["upper_words"]
            first_lower = new_dictionary["0"]["lower_words"]
            first_numeric = new_dictionary["0"]["numeric"]
            first_total = new_dictionary["0"]["sum_numbers"]

            first_count = new_dictionary["0"]["len_numbers"]
            first_count = sorted(first_count)  # seřazení daného textu

            print(f"There are {first_len} words in the selected text.")
            print(f"There are {first_title} titlecase words.")
            print(f"There are {first_upper} uppercase words.")
            print(f"There are {first_lower} lowercase words.")
            print(f"There are {first_numeric} numeric strings.")
            print(f"The sum of all the numbers {first_total} ")

            print(separator)

            # naformátování hlavičky grafu
            print(f"{'LEN|':<7}{'OCCURENCES':<15}{'|NR.'}")

            print(separator)

            # výpis jednotlivých sloupců a formátování
            for j in new_dictionary_first:
                len_int = " " + " " + str(j[0]) + "|"
                asterisk_replace = str(j[1]).replace(str(j[1]), "*" * (j[1]))
                nr = "|" + str(j[1])

                print(f"{len_int:<5}{asterisk_replace:<17}{nr}")

        elif enter_index == 2:
            second_len = new_dictionary["1"]["number_words"]
            second_title = new_dictionary["1"]["title_words_upper"]
            second_upper = new_dictionary["1"]["upper_words"]
            second_lower = new_dictionary["1"]["lower_words"]
            second_numeric = new_dictionary["1"]["numeric"]
            second_total = new_dictionary["1"]["sum_numbers"]

            second_count = new_dictionary["1"]["len_numbers"]
            second_count = sorted(second_count)  # seřazení daného textu

            print(f"There are {second_len} words in the selected text.")
            print(f"There are {second_title} titlecase words.")
            print(f"There are {second_upper} uppercase words.")
            print(f"There are {second_lower} lower words.")
            print(f"There are {second_numeric} numeric strings.")
            print(f"The sum of all the numbers {second_total} ")

            print(separator)

            # naformátování hlavičky grafu
            print(f"{'LEN|':<7}{'OCCURENCES':<18}{'|NR.'}")

            print(separator)

            # výpis jednotlivých sloupců a formátování
            for j in new_dictionary_second:
                len_int = " " + " " + str(j[0]) + "|"
                asterisk_replace = str(j[1]).replace(str(j[1]), "*" * (j[1]))
                nr = "|" + str(j[1])

                print(f"{len_int:<5}{asterisk_replace:<20}{nr}")

        elif enter_index == 3:
            third_len = new_dictionary["2"]["number_words"]
            third_title = new_dictionary["2"]["title_words_upper"]
            third_upper = new_dictionary["2"]["upper_words"]
            third_lower = new_dictionary["2"]["lower_words"]
            third_numeric = new_dictionary["2"]["numeric"]
            third_total = new_dictionary["2"]["sum_numbers"]

            third_count = new_dictionary["2"]["len_numbers"]
            third_count = sorted(third_count)  # seřazení daného textu

            print(f"There are {third_len} words in the selected text.")
            print(f"There are {third_title} titlecase words.")
            print(f"There are {third_upper} uppercase words.")
            print(f"There are {third_lower} lowercase words.")
            print(f"There are {third_numeric} numeric strings.")
            print(f"The sum of all the numbers {third_total} ")

            print(separator)

            # naformátování hlavičky grafu
            print(f"{'LEN|':<7}{'OCCURENCES':<18}{'|NR.'}")

            print(separator)

            # výpis jednotlivých sloupců a formátování
            for j in new_dictionary_third:
                len_int = " " + " " + str(j[0]) + "|"
                asterisk_replace = str(j[1]).replace(str(j[1]), "*" * (j[1]))
                nr = "|" + str(j[1])

                print(f"{len_int:<5}{asterisk_replace:<20}{nr}")

else:
    print("Wrong username or password!")
    exit()

from pathlib import Path
import operator

# Der Trump Parser

# Für unseren Auftraggeber, die Newscom-Presseagentur, sollen wir einen Parser entwickeln, der
# die gesammelten Reden von Donald Trump einliest und nach gewissen Kriterien filtert oder ausgibt.

# Parsen bedeutet in diesem Zusammenhang: Text aufsplitten, von Leer- Satz- und Steuerzeichen bereinigen und in einer Liste verfügbar machen. (Hinweis als Zusatzaufgabe: they're sind zwei Worte!)

# Über  Input soll der User einen Modus wählen können. In Abhängigkeit der Eingabe startet der Parser.

# HINWEIS:
# In der Entwicklungsphase den geladenen Text-Content auf 5000 Zeichen kürzen.
# content = file.read(5000)

userinput_first = input("was möchten sie ausführen? \"sen\" Suchwort um nach"
"Sätzen zu suchen, \"word\" Buchstabenkombination um nach einer"
"Zeichenkombinationen in Wörtern zu suchen und \"top\" um nach den"
"meistgenannten wörtern zu suchen ")

userinput_list = list(userinput_first.split(" "))

# -------------------------------------------------------------------------------------------
# Aufgabe 1: sentence
# der Datei-Content wird in Sätze gesplittet. Ein Punkt gilt als Ende eines Satzes.
# Wenn das eingegebene Suchwort in diesem Satz als Wort enthalten ist, drucke den Satz aus. 
# Die Usereingabe ist festgelegt und soll wie folgt aussehen:SEN <SUCHWORT>
# z.b. SEN America
# soll nur Sätze ausdrucken, in denen konkret das Wort “America” vorkommt. 
# -------------------------------------------------------------------------------------------
if userinput_list[0] == "sen":

    sentence = []
    with open(Path(__file__).parent / "trump_speeches.txt", mode="r", encoding="utf-8") as f:
        sentence = f.read().strip("...").split(".")

    search_word_sentence = userinput_list[1]

    for element in sentence:
        if search_word_sentence.lower() in element.lower():
            print("Der Satz ist:", element.strip())

# -------------------------------------------------------------------------------------------
# Aufgabe 2: Word
# der Datei-Content wird in Wörter gesplittet. Jedes Wort sollte von Kommas und Punkten bereinigt werden.
# Wenn das eingegebene Suchwort in diesem Wort enthalten ist, füge es einer Ergebnis-Liste hinzu (zb. word_list)
# Diese Liste sollte von doppelten Elementen bereinigt werden. Diese Liste muss sortiert ausgegeben werden( sort())
# Die Usereingabe ist festgelegt und soll wie folgt aussehen: WORD <SUCHWORT> 
# z.b.WORD "Am" 
# es sollen sich nur Wörter in der Liste befinden, die „Am“ beinhalten: 'Americans', 'America', 'Amendment', [..] 
# -------------------------------------------------------------------------------------------
elif userinput_list[0] == "word":
    word = []
    word_list = []

    with open(Path(__file__).parent / "trump_speeches.txt", mode="r", encoding="utf-8") as f:
        word = f.read().strip(".").split()

    search_word_word = userinput_list[1]

    for element in word:
        element = element.strip(".,%;$§/-]?\"...[\´s?")
        if search_word_word.casefold() in element.casefold():
            if element not in word_list:
                word_list.append(element)

    print(word_list)

# -------------------------------------------------------------------------------------------
# Aufgabe 3: Ninja 
# der Datei-Content wird in Wörter gesplittet. Jedes Wort sollte von Kommas und Punkten bereinigt werden.
# Gesucht ist die TOP-TEN aller Wortnennungen inklusive Anzahl der Vorkommen. Es sollen nur Worte
# berücksichtigt werden, die >= 5 Zeichen haben, um zumindest Pronomen und Füllwörter etwas auszuschließen.
# Hierbei bitte Groß- und Kleinschreibung NICHT beachten (case-insensitive)
# Die Usereingabe ist festgelegt und soll wie folgt aussehen: TOP
# [('people', 964),
# ('because', 762),
# [..]
# -------------------------------------------------------------------------------------------
elif userinput_list[0] == "top":

    word_count = []
    word_count_dict = {}

    with open(Path(__file__).parent / "trump_speeches.txt", mode="r", encoding="utf-8") as f:
        word_count = f.read().strip(".").split()

    for element in word_count:
        element = element.strip(".,%;$§/-]?\"...[s?").replace(",", " ")
        element = element.casefold()
        if len(element) >= 5:
            if element in word_count_dict:
                word_count_dict[element] += 1
            else:
                word_count_dict[element] = 1

    top_ten = sorted(word_count_dict.items(), key=operator.itemgetter(1))
    top_ten.reverse()
    print("Top Ten Wörter: ", top_ten[:11])

# ---------------------------------------------------------------------------------------------------------
else:
    print("Sorry command nicht erkannt!")

Etapa 3 Proiect PA - echipa "187"

	Bot-ul functioneaza dupa un algoritm greedy, la fiecare pas verifica
fiecare casuta vecina si ia cantitatea de halite din ea, apoi ordoneaza
casutele in functie de catitatea de halite si alege cea mai buna casuta
care nu este ocupata.
	Deasemenea o nava nu se va muta de pe pozitia curenta daca diferenta
dintre cantitatea de halite de pe cea mai buna casuta nu este mai mare 
decat cantitatea de pe pozitia curenta * x (x care se schimba).
	Navele vor incerca sa abandoneze casuta curenta daca in ea se afla mai
putin de 100 de halite; 100 halite ramas in casutele vizitate cel putin o data
va fi colectat pe parcursul jocului cand navele pleace iar din baza.
	Pentru casutele ocupate folosec o lista de aparitie, care stocheaza
atat pozitia curenta a fiecarei nave cat si urmatoare ei pozitie daca
aceasta se muta, am implementat asa deoarece uneori o nava fiind pe o casuta
cu foarte mult halite statea pe loc pentru a colecta iar alte nave incercau 
sa mearga pe aceeasi casuta si se blocau.
	Am adaugat in clasa ship un camp "to_do" care ia valori 1 sau 0, daca o 
nava are to_do 1 asta inseamna ca a colectat cel putin 950 halite si trebuie
sa se intoarca la baza, dupa ce depozitieaza to_do-ul navei devine iar 0
	La sfarsitul jocului cand mai sunt 25 de tururi toate navele se intorc in
baza (to_do-ul lor este schimbat pe 1) si apoi stau pe loc, am realizat 
acest lucru schimband functia naive_navigate, aceasta mai primeste un argument 
terminate ce reprezinta numarul maxim de tururi minus 25 si care testeaza turul 
curent daca acesta este mai mare decat terminatetrimite toate navele in baza 
fara sa verifice deca destinatia este safe (daca este deja o nava in baza).
	Toate numerele magice au fost selectate dupa numeroase teste.

Pentru rulare:
python ./run.py --cmd "python3 MyBot.py"

Algoritmi folositi:
-Bubble sort pentru a sorta pozitiile in functie de halite ammount => complexitate O(n^2)

Responsabilitati:
Corbescu Alexandru-Robert : Scris cod + testat
Neacsu Antoniu-Georgian : Scris cod
Tacu Ovidiu Mihai : Research
Ionita Ada Cosmina : Testat


Documentatie si surse de insipratie:
https://github.com/coreylowman/AllYourTurtles
https://github.com/stefank0/halite3
https://github.com/mattorus/ThePythonator
https://www.youtube.com/watch?v=IXhZLRagXNU
https://forums.halite.io/t/what-was-your-final-strategy-challenge/1326.html
https://forums.halite.io/t/improving-upon-naive-navigate-to-get-in-top-400/669.html
https://forums.halite.io/t/why-are-people-destroying-all-their-ships-at-the-end-of-the-game/627.html


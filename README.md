# Lego-sets

### Projektna naloga pri predmetu Programiranje 1

Analiziral bom Lego sete, ki so izšli v zadnjih ~petih letih s spletne strani [brickset.com](https://brickset.com/sets).

Opazoval bom naslednje podatke:

* tema
* število kock
* cena
* datum izdaje
* cena po kocki
* minifigs
* ocena
* dostopnost
* popularnost

Hipoteze:
* Kako je cena po kocki odvisna od teme
* Spreminjanje povprečne cene setov iz posamezne teme v odvisnosti od leta izdaje
* Cena minifigure v odvisnosti od teme, leta izdaje, dostopnosti
* Popularnost v odvisnosti od teme, števila minifigur, cene po kocki

#### Od nedavnega ta git repozitorij vseubuje še naslednje:
- mapo `obdelani-podatki`, kjer sta shranjeni `.json` in `.csv` datoteki
- mapo `html-nalozeni`, ki vsebuje 315 `.html` datotek, ki sem jih nalozil s spletne strani [brickset.com](https://brickset.com/sets) in so namenjene obdelavi.
- datoteki `urejanje_podatkov.py` in `orodja.py`, ki predstavljata skripti za zajem in obdelavo podatkov.

Obdelani in urejeni podatki so shranjeni v datoteki `bricksets-database-2009-2019.csv` in obsegajo kategorije:
* id
* varinta
* ime seta
* temo
* leto
* tip seta
* število vsebovanih figuric
* število kock
* vrsto pakiranja
* dostopnost
* US ceno in povprečno ceno na kocko v $
* EU ceno in povprečno ceno na kocko v €
* in čas izida v US in EU.

Naletel pa sem tudi na dve izjemi v zapisu posamičnega blok v html datotekah pri zajemu podatkov, ki za razliko od preostalih 7719 vnosov v svojih html datotekah nista imeli podanega tipa bloka teh dveh setov sem skopiral v datoteko `izjemi-brez-podanega-tipa.html`. Tema dvema setoma s funkcijo `tip_seta` v skripti "ročno" podam njuna pravilna tipa.
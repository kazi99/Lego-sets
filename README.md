# Lego-sets

### Projektna naloga pri predmetu Programiranje 1 na [FMF](https://www.fmf.uni-lj.si/si/)

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
1. Lego vsako leto izda več setov
2. Velikosti setov skozi leta
3. *ppp*
   1. Povprečna cena kocke narašča skozi leta
   2. Seti z nižjim *ppp* vsebujejo več kock
4. Najbolj izdane teme
5. Minifigure
   1. Dražji seti vsebujejo več minifigur
   2. Cena minifigure skozi leta
   
____
#### Od nedavnega ta git repozitorij vseubuje še naslednje:
- mapo `obdelani-podatki`, kjer sta shranjeni `.json` in `.csv` datoteki zbranih in obdelanih podatkov,
- mapo `html-nalozeni`, ki vsebuje 315 `.html` datotek, ki sem jih naložil s spletne strani [brickset.com](https://brickset.com/sets) in so namenjene obdelavi,
- datoteki `urejanje_podatkov.py` in `orodja.py`, ki predstavljata skripti za zajem in obdelavo podatkov.

Obdelani in urejeni podatki so shranjeni v datoteki `bricksets-database-2009-2019.csv` in obsegajo kategorije:
* id
* varianta
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

Naletel pa sem tudi na dve izjemi v zapisu posamičnih blokov v html datotekah med zajemanjem podatkov, ki za razliko od preostalih 11887 vnosov v svojih html datotekah nista imeli podanega tipa. Bloka teh dveh setov sem skopiral v datoteko `izjemi-brez-podanega-tipa.html` in jima s funkcijo `tip_seta` v skripti "ročno" podal njuna pravilna tipa.

Analiza podatkov je shranjena v datoteki `lego_analiza.ipynb`, zraven pa je še datoteka `pomozna_analiza.ipynb` v kateri je shranjen le moj proces risanja grafov in nasploh razvijanja glavne analize podatkov v prvo omenjeni datoteki.
____
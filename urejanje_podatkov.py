import re
import orodja

vzorec_bloka = re.compile(
    r"<article class='set'>.*?</article>",
    flags=re.DOTALL
)

vzorec_seta = re.compile(
    r"title=\"(?P<id>.*?)-(?P<variant>\d*?):(?P<ime_seta>.*?)\".*?"
    r"<a href='/sets/theme-.*?'>(?P<tema>.*?)</a>.*"
    r">(?P<leto>.*?)</a> </div><div class='tags'><span id=.*?",
    # r"<dt>Set type</dt><dd>(?P<tip_seta>.*?)</dd>.*?", # <-- ne dela samo za dva seta ki nimata defiranega tipa (bom dodal "na roke")
    flags=re.DOTALL
)

vzorec_tip_seta = re.compile(
    r"<dt>Set type</dt><dd>(?P<tip_seta>.*?)</dd>.*?",
    flags=re.DOTALL
)

def tip_seta(blok, en_set):
    ima_definiran_tip = vzorec_tip_seta.search(blok)
    if ima_definiran_tip:
        en_set['tip_seta'] = ima_definiran_tip['tip_seta'].strip().lower()
    else:       # edino ta dva seta nimata podanega tipa v html-jih. Njiuni vrednosti sem pridobil iz: 
        if en_set['id'] == '2000710':       # https://brickset.com/sets/2000710-1/WeDo-Replacement-Parts-Pack
            en_set['tip_seta'] = 'extended'
        elif en_set['id'] == '40331':       # https://brickset.com/sets/40331-1/Wolf
            en_set['tip_seta'] = 'normal'
        else:
            pass

vzorec_figuric = re.compile(
    r"<dt>Minifigs</dt><dd><a class=.*?>(?P<figurice>\d*?)</a>",
    flags=re.DOTALL
)

vzorec_st_kock = re.compile(
    r"<dt>Pieces</dt><dd><a class=.*?>(?P<st_kock>\d*?)</a>",
    flags=re.DOTALL
)

vzorec_us_cena = re.compile(
    r"<dt>RRP</dt><dd>\$(?P<us_cena>\d{4}.\d{2}|\d{3}.\d{2}|\d{2}.\d{2}|\d.\d{2})", # predpostavljam, da so vse cene < $10000.00
    flags=re.DOTALL
)

vzorec_eu_cena = re.compile(
    r"<dt>RRP</dt><dd>.*?(?P<eu_cena>\d{4}.\d{2}|\d{3}.\d{2}|\d{2}.\d{2}|\d.\d{2})€", # predpostavljam, da so vse cene < 10000.00€
    flags=re.DOTALL
)

vzorec_us_ppp = re.compile(
    r"<dt>PPP</dt><dd>.*?(?P<us_ppp>\d{4}.\d|\d{3}.\d|\d{2}.\d|\d.\d)c",
    flags=re.DOTALL
)

vzorec_eu_ppp = re.compile(
    r"<dt>PPP</dt><dd>.*?(?P<eu_ppp>\d{4}.\d|\d{3}.\d|\d{2}.\d|\d.\d)c</dd>",
    flags=re.DOTALL
)

vzorec_pakiranje = re.compile(
    r"<dt>Packaging</dt><dd>(?P<pakiranje>.*?)</dd>",
    flags=re.DOTALL
)

vzorec_dostopnost = re.compile(
    r"<dt>Availability</dt><dd>(?P<dostopnost>.*?)</dd>",
    flags = re.DOTALL
)

vzorec_cas_izida_us = re.compile(
    r"<dt>First sold</dt><dd>USA: (?P<us_cas_izida>.*?)(,|</dd>)",
    flags=re.DOTALL
)

vzorec_cas_izida_eu = re.compile(
    r"<dt>First sold</dt><dd>.*?UK/EU: (?P<eu_cas_izida>.*?)</dd>",
    flags=re.DOTALL
)

def match(blok, en_set, kategorija, vzorec, func):
    check = vzorec.search(blok)
    if check:
        en_set[kategorija] = func(check[kategorija])
    else:
        en_set[kategorija] = None

def podatki_seta_od(blok): #argument bo blok.group(0)
    if vzorec_seta.search(blok) == None:
        print(blok)
        return
    else:
        en_set = vzorec_seta.search(blok).groupdict()
        en_set['ime_seta'] = en_set['ime_seta'].strip()
        en_set['tema'] = en_set['tema'].strip()
        # en_set['id'] = int(en_set['id']) ker niso vsi id-ji int
        en_set['variant'] = int(en_set['variant'])
        en_set['leto'] = int(en_set['leto'])
        
        tip_seta(blok, en_set)

        sez_kategorij = ['figurice', 'st_kock', 'us_cena', 'eu_cena', 'us_ppp', 'eu_ppp', 'pakiranje', 'dostopnost', 'us_cas_izida', 'eu_cas_izida']
        sez_vzorcev = [vzorec_figuric, vzorec_st_kock, vzorec_us_cena, vzorec_eu_cena, vzorec_us_ppp, vzorec_eu_ppp, vzorec_pakiranje, vzorec_dostopnost, vzorec_cas_izida_us, vzorec_cas_izida_eu]
        sez_funkcij = [int, int, float, float, float, float, lambda x:x, lambda x:x, lambda x:x, lambda x:x]
        for kat,vzorec,func in zip(sez_kategorij, sez_vzorcev, sez_funkcij):
            match(blok, en_set, kat, vzorec, func)

        return en_set

def seti_na_spl_strani(ime_datoteke):
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for blok in vzorec_bloka.finditer(vsebina):
        yield podatki_seta_od(blok.group(0))

def seti_na(leto):
    sez = [14, 16, 17, 18, 18, 17, 16, 19, 18, 18, 20, 21, 24, 28, 29, 30, 32, 34, 34, 32, 31]
    return sez[leto - 1999]

def nalozi_strani():
    counter = 1
    for leto in range(1999, 2020):
        for i in range(1, seti_na(leto) + 1):
            url = (
                f'https://brickset.com/sets/year-{leto}/page-{i}'
            )
            ime_datoteke = (
                f"/Users/thrawn/Documents/git/Lego-sets/html-nalozeni-1999-2019/brickset-database-{counter}.html"
            )
            orodja.shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False)
            counter += 1

vsi_seti = []
def zdruzi_database():
    """ v seznam `vsi_seti` prepise slovarje vseh setov s pomocjo generatorja `seti_na_spl_strani`. """
    for i in range(1,487): 
        spl_str = (
            f"/Users/thrawn/Documents/git/Lego-sets/html-nalozeni-1999-2019/brickset-database-{i}.html"
        )
        for en_set in seti_na_spl_strani(spl_str):
            vsi_seti.append(en_set)


def ustvari_json():
    orodja.zapisi_json(vsi_seti, "/Users/thrawn/Documents/git/Lego-sets/obdelani-podatki/bricksets-database-1999-2019.json")

imena_polj = ['id', 'variant', 'ime_seta', 'tema', 'leto', 'tip_seta', 'figurice', 'st_kock', 'us_cena', 'eu_cena', 'us_ppp', 'eu_ppp', 'pakiranje', 'dostopnost', 'us_cas_izida', 'eu_cas_izida']

def ustvari_csv():
    orodja.zapisi_csv(vsi_seti, imena_polj, "/Users/thrawn/Documents/git/Lego-sets/obdelani-podatki/bricksets-database-1999-2019.csv")



# testi:


# g = seti_na_spl_strani("/Users/thrawn/Documents/git/Lego-sets/html_na_roke/2019 | Brickset: LEGO set guide and database page-1.html")
# print(next(g))
# y = [x['eu_cas_izida'] for x in g]
# print(y)
# orodja.shrani_spletno_stran('https://brickset.com/sets/year-2019/page-32', "/Users/thrawn/Documents/git/Lego-sets/testni.html", vsili_prenos=True)



#--------------------------pozeni--------------------------

# nalozi_strani()
# zdruzi_database()
# ustvari_json()
# ustvari_csv()

#----------------------------------------------------------
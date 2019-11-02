import orodja

def seti_na_strani(leto, st_strani):
    url = (
        f'https://brickset.com/sets/year-{leto}/page-{st_strani}'
    )
    datoteka = '/Users/thrawn/Documents/git/Lego-sets/html_folder/brickset-database-{}
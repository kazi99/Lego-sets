# generator ki razkosa html na bloke
# iskanje po blokih


import re
import requests

vzorec = (
    r"<article class='set'>\n<a href=\".*?\" class=\".*?\" onclick=\".*?\"><img src=\".*?\" title=\".*?\" onError=\".*?\" /></a>\n<div class=\".*?\">\n<h1>(?P<set>.*?)</h1>"
)

zadetki = []
counter = 0

with open("html_na_roke/2019 | Brickset: LEGO set guide and database page-4.html", encoding='utf-8') as file:
    vsebina = file.read()

for zadetek in re.finditer(vzorec, vsebina):
    zadetki.append(zadetek.groupdict())
    counter += 1


""" <article class='set'>
<a href="https://images.brickset.com/sets/large/2000710-1.jpg?201911020910" class="highslide plain mainimg" onclick="return hs.expand(this)"><img src="https://images.brickset.com/sets/small/2000710-1.jpg?201911020910" title="2000710-1: WeDo Replacement Parts Pack" onError="this.src='/assets/images/spacer.png'" /></a>
<div class="highslide-caption">
<h1>WeDo Replacement Parts Pack</h1><div class='tags floatleft'><a href='/sets/2000710-1/WeDo-Replacement-Parts-Pack'>2000710-1</a> <a href='/sets/theme-Education'>Education</a> <a class='subtheme' href='/sets/theme-Education/subtheme-WeDo'>WeDo</a> <a class='year' href='/sets/theme-Education/year-2015'>2015</a> </div><div class='floatright'>&copy;2015 LEGO Group</div>
<div class="pn">
<a href="#" onclick="return hs.previous(this)" title="Previous (left arrow key)">&#171; Previous</a>
<a href="#" onclick="return hs.next(this)" title="Next (right arrow key)">Next &#187;</a>
</div>
</div>
<div class='meta'><h1><a href="/sets/2000710-1/WeDo-Replacement-Parts-Pack"><span>2000710: </span> WeDo Replacement Parts Pack</a></h1><div class='tags'><a href='/sets/2000710-1/WeDo-Replacement-Parts-Pack'>2000710-1</a> <a href='/sets/theme-Education'>Education</a> <a class='subtheme' href='/sets/theme-Education/subtheme-WeDo'>WeDo</a> <a class='year' href='/sets/theme-Education/year-2015'>2015</a> </div><div class='tags'><span id='tags29665'></span></div><div class='col'><dl><dt>Packaging</dt><dd>Polybag</dd><dt>Availability</dt><dd>Educational</dd></dl></div><div class='col'><dl></dl><dl class='highlight'></dl></div></div><div class='action'><dl class='admin'><dt class='hideingallery'>Our community</dt><dd class='hideingallery'><a class='popuplink' href='ownedBy?SetID=29665'>0 own this set</a>, 0 want it</dd></dl><dl class='buylinks'><dt>Buy this set at</dt><dd><ul><li>
</li><li>
<a class="amazon" href="https://www.amazon.com/s/?url=search-alias=aps&amp;field-keywords=LEGO%202000710&amp;tag=brickset-20&amp;link_code=wql&amp;camp=212361&amp;creative=380601&amp;_encoding=UTF-8">Amazon</a>
</li><li>
<a class='ebay' href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=9&pub=5574779132&toolid=10001&campid=5336183597&customid=&icep_uq=LEGO+2000710&icep_sellerId=&icep_ex_kw=&icep_sortBy=12&icep_catId=&icep_minPrice=&icep_maxPrice=&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg">eBay</a>
</li><li>
<a class="bricklink" href='http://alpha.bricklink.com/pages/clone/catalogitem.page?S=2000710-1#T=S&O={"ss":"SI"}'>BrickLink</a>
</li></ul></dd></dl></div></article>
<article class='set'>
<a href="https://images.brickset.com/sets/large/40331-1.jpg?201911020901" class="highslide plain mainimg" onclick="return hs.expand(this)"><img src="https://images.brickset.com/sets/small/40331-1.jpg?201911020901" title="40331-1: Wolf" onError="this.src='/assets/images/spacer.png'" /></a>
<div class="highslide-caption">
<h1>Wolf</h1><div class='tags floatleft'><a href='/sets/40331-1/Wolf'>40331-1</a> <a href='/sets/theme-Promotional'>Promotional</a> <a class='subtheme' href='/sets/theme-Promotional/subtheme-Monthly-Mini-Model-Build'>Monthly Mini Model Build</a> <a class='year' href='/sets/theme-Promotional/year-2019'>2019</a> </div><div class='floatright'>&copy;2019 LEGO Group</div>
<div class="pn">
<a href="#" onclick="return hs.previous(this)" title="Previous (left arrow key)">&#171; Previous</a>
<a href="#" onclick="return hs.next(this)" title="Next (right arrow key)">Next &#187;</a>
</div>
</div>
<div class='meta'><h1><a href="/sets/40331-1/Wolf"><span>40331: </span> Wolf</a></h1><div class='tags'><a href='/sets/40331-1/Wolf'>40331-1</a> <a href='/sets/theme-Promotional'>Promotional</a> <a class='subtheme' href='/sets/theme-Promotional/subtheme-Monthly-Mini-Model-Build'>Monthly Mini Model Build</a> <a class='year' href='/sets/theme-Promotional/year-2019'>2019</a> </div><div class='tags'><span id='tags29664'></span></div><div class='col'><dl><dt>Packaging</dt><dd>Polybag</dd><dt>Availability</dt><dd>Not sold</dd></dl></div><div class='col'><dl><dt>Notes</dt><dd>November 2019</dd></dl><dl class='highlight'></dl></div></div><div class='action'><dl class='admin'><dt class='hideingallery'>Our community</dt><dd class='hideingallery'><a class='popuplink' href='ownedBy?SetID=29664'>0 own this set</a>, 0 want it</dd></dl><dl class='buylinks'><dt>Buy this set at</dt><dd><ul><li>
</li><li>
<a class="amazon" href="https://www.amazon.com/s/?url=search-alias=aps&amp;field-keywords=LEGO%2040331&amp;tag=brickset-20&amp;link_code=wql&amp;camp=212361&amp;creative=380601&amp;_encoding=UTF-8">Amazon</a>
</li><li>
<a class='ebay' href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=9&pub=5574779132&toolid=10001&campid=5336183597&customid=&icep_uq=LEGO+40331&icep_sellerId=&icep_ex_kw=&icep_sortBy=12&icep_catId=&icep_minPrice=&icep_maxPrice=&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg">eBay</a>
</li><li>
<a class="bricklink" href='http://alpha.bricklink.com/pages/clone/catalogitem.page?S=40331-1#T=S&O={"ss":"SI"}'>BrickLink</a>
</li></ul></dd></dl></div></article> """
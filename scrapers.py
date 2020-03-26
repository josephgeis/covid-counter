from lxml import html
import requests

class BaseScraper(object):
    @property
    def locale_name(self): return "Locale"
    

    @property
    def number_of_cases(self): return "0"
    

    @property
    def as_of_date(self): return "now"
    

    @property
    def source_url(self): return None


    @property
    def color_scheme(self): return "t-default"


class CA_OC_Scraper(BaseScraper):
    @property
    def locale_name(self): return "Orange County, CA"

    
    @property
    def number_of_cases(self):
        page = self.page
        tree = html.fromstring(page.content)

        xpath = "//html/body/div/div[3]/div/section/main/div/article/div/div/table/tbody/tr[4]/td[2]/strong"

        return tree.xpath(xpath)[0].text


    @property
    def color_scheme(self): return "t-orange"


    @property
    def source_url(self):
        return "https://occovid19.ochealthinfo.com/coronavirus-in-oc"


    def __init__(self, fetch=True):
        if fetch: self.page = requests.get(self.source_url)


SCRAPERS = {
    "CA.OC": CA_OC_Scraper
}


def get(scraper):
    s = SCRAPERS.get(scraper, None)
    if s: return s()
    else: return s


def available():
    return [(sid, s(fetch=False).locale_name) for (sid, s) in SCRAPERS.items()]

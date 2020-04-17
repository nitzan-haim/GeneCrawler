from ace2_scraper import *
import json


class KnownGeneScraper(Ace2Spider):
    """
    class for scraping information about the ace2 gene in species that are
    obtained from the genome-browser database (therefore they are known).
    currently scrapes human and mouse gene info.
    """

    EXON_SELECTOR = './/td[@id="td_data_knownGene"]//map[@name="map_data_knownGene"]/area[1]/@title'
    INTRON_SELECTOR = './/td[@id="td_data_knownGene"]//map[@name="map_data_knownGene"]/area[2]/@title'

    def set_urls(self):
        with open(self.URLS_PATH) as urls_f:
            urls_d = json.load(urls_f)["known genes"]
            self.urls = [urls_d[k] for k in urls_d]


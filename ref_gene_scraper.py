from ace2_scraper import *
import json


class RefGeneScraper(Ace2Spider):
    """
    class for scraping information about the ace2 gene in species that are
    referenced from other sources.
    currently scrapes dog and cat gene info.
    """

    EXON_SELECTOR = './/map[@name="map_data_refGene"]/area[starts-with(@title, "Exon")]/@title'
    INTRON_SELECTOR = './/map[@name="map_data_refGene"]/area[starts-with(@title, "Intron")]/@title'

    def set_urls(self):
        with open(self.URLS_PATH) as urls_f:
            urls_d = json.load(urls_f)["ref genes"]
            self.urls = [urls_d[k] for k in urls_d]

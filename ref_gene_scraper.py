from ace2_scraper import *


class RefGeneScraper(Ace2Spider):
    """
    class for scraping information about the ace2 gene in species that are
    referenced from other sources.
    currently scrapes dog and cat gene info.
    """

    EXON_SELECTOR = './/map[@name="map_data_refGene"]/area[starts-with(@title, "Exon")]/@title'
    INTRON_SELECTOR = './/map[@name="map_data_refGene"]/area[starts-with(@title, "Intron")]/@title'

    def json_to_urls(self, urls_json):
        urls_d = urls_json["ref genes"]
        return [urls_d[k] for k in urls_d]

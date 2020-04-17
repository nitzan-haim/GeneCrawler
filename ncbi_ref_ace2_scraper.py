from ace2_scraper import *
import json


class NCBIReferenceScraper(Ace2Spider):
    """
    class for scraping information about the ace2 gene in species that are
     referenced from NCBI database.
    currently scrapes chicken, zebra fish and chimp gene info.
    """

    EXON_SELECTOR = './/map[@name="map_data_ncbiRefSeqPredicted"]/area[starts-with(@title, "Exon")]/@title'
    INTRON_SELECTOR = './/map[@name="map_data_ncbiRefSeqPredicted"]/area[starts-with(@title, "Intron")]/@title'

    def set_urls(self):
        with open(self.URLS_PATH) as urls_f:
            urls_d = json.load(urls_f)["ncbi reference"]
            self.urls = [urls_d[k] for k in urls_d]

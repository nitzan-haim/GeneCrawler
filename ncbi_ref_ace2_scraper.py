from ace2_scraper import *


class NCBIReferenceScraper(Ace2Spider):
    """
    class for scraping information about the ace2 gene in species that are
     referenced from NCBI database.
    currently scrapes chicken, zebra fish and chimp gene info.
    """

    EXON_SELECTOR = './/map[@name="map_data_ncbiRefSeqPredicted"]/area[starts-with(@title, "Exon")]/@title'
    INTRON_SELECTOR = './/map[@name="map_data_ncbiRefSeqPredicted"]/area[starts-with(@title, "Intron")]/@title'

    def json_to_urls(self, urls_json):
        urls_d = urls_json["ncbi reference"]
        return [urls_d[k] for k in urls_d]

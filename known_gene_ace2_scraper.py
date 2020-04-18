from ace2_scraper import *


class KnownGeneScraper(Ace2Spider, abc.ABC):
    """
    abstract class for scraping information about the ace2 gene in species that are
    obtained from the genome-browser database (therefore they are known).
    """

    EXON_SELECTOR = './/td[@id="td_data_knownGene"]//map[@name="map_data_knownGene"]/area[1]/@title'
    INTRON_SELECTOR = './/td[@id="td_data_knownGene"]//map[@name="map_data_knownGene"]/area[2]/@title'

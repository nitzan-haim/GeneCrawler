from known_gene_ace2_scraper import *


class HumanScraper(KnownGeneScraper):
    """
    class for scraping information about the ace2 gene in humans.
    includes scraping gene expression.
    """

    """
    selector for the gene expression levels of the gene.
    """
    GENE_EXP_SELECTOR = './/td[@id="td_data_gtexGene"]//map[@name="map_data_gtexGene"]/area/@title'

    def json_to_urls(self, urls_json):
        return [urls_json["known genes"]["human"]]

    def yield_parameters(self, response):
        print("HumanScraper - yield_parameters")
        return {
            **super().yield_parameters(response),
            **{'gene expression level': response.xpath(self.GENE_EXP_SELECTOR).getall()}
        }


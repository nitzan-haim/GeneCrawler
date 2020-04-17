# GeneCrawler
Web crawler for comparing information about genes.

# Background
The ace2 gene is particularly interesting as it is the gene coding for the receptor that the corona virus (aka SARS-CoV-2, the virus causing the COVID-19 desease) binds to. In other words, it is the "key" for the virus to enter the cell. Therefore, species that have the ace2 gene have the potential of being infected by SARS-CoV-2^(2).
# PLEASE NOTE
Do not draw any conclusions from the output of this program, as this project was done for personal perposes only and simply compares information that is already known and available for anyone. This subject is properly researched in laboratories world-wide.

# About the software
This program scrapes information about genes from the genome browser search engine^(1), a standard bioinformatics search engine, using python's scrapy library.
The class Ace2Spider (in ace2_scraper.py) includes the main class for the scraping information about the ace2 gene. Because the information in genome browser is obtained from different sources, the information is stored under a different structure therefore different selectors are needed. The classes KnownGeneScraper, NCBIReferenceScraper and RefGeneScraper (from known_gene_ace2_scraper.py, ncbi_ref_ace2_scraper.py and ref_gene_scraper.py respectively) inherit from Ace2Spider and implement the different selectors needed.
# Output
The program writes the file ace2_comparison.jsonl that contains following attributes about a few selected species.
species: the species that the next information refers to.
size: the size of the gene in bp (base pairs).
chromosome: the chromosome that this gene is located on. 
chromosome start location: the location on the chromosome that the gene starts at (how many bp from the beginning of the chromosome).
chromosome end location: the location on the chromosome that the gene ends at (how many bp from the beginning of the chromosome).
exons^(3) num: how many exons this gene contains.
introns^(3) num: how many introns this gene contains.


# Execution Details
To run the program on your mechine make sure you have python 3.6.X and up installed. Download all files and run the file execute.py. Expect a file ace2_comparison.jsonl to show in the same folder as the program finishes running.

# Source
This program uses the results of searching genome browser^(1) with the different species and the gene "ace2". To get directly the pages the program crawls please refer to the file ace2_genome_browser_urls (JSON format) included in this repository.



-----------------------------------------------------------------
references:
(1) UCSC genome browser: https://genome.ucsc.edu/cgi-bin/hgGateway
(2) Further reading about the connection between ace2 and COVID-19: https://en.wikipedia.org/wiki/Angiotensin-converting_enzyme_2
(3) Further explanations about exons and introns: https://www.news-medical.net/life-sciences/What-are-introns-and-exons.aspx)

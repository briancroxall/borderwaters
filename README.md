# Introduction
This repository contains work related to the conclusion of [Brian Russell Roberts](https://humanities.byu.edu/person/brian-russell-roberts/)'s book [_Borderwaters: Amid the Archipelagic States of America_](https://www.dukeupress.edu/borderwaters). The project began in January 2018 and continued through the publication of the book in spring 2021. 

This project was conducted across six separate repositories, of which this is one. Prior to the publication of the book, the work was collected and organized in this repository, and this repository was made public. The other repositories remain private.

## Data
Data for this project were obtained in several steps and from several sources:
1. JSTOR's [Data for Research](https://www.jstor.org/dfr/) provided us with the bulk of the print runs of the following journals: _American Literature_ from 1929-1999; _American Quarterly_ from 1949-2012; and _Journal of American History_ from 1964-2012. In addition, JSTOR provided us with data from _American Literary History_ (1989-2012) and _Journal of American Studies_ (1967-2012), but in the end we decided to focus our efforts only on the first three journals. 
2. [Duke University Press](https://www.dukeupress.edu) provided us with the data for _American Literature_ from 2000 (vol. 72, no. 1) - 2017 (vol. 89, no. 3).
3. Using a combination of scripts and manual downloads, we collected the remaining data for the 2010s from their respective online platforms: _American Literature_ from 2017-2019 from [Duke University Press](https://dukeupress.edu); _American Quarterly_ from 2013-2019 from [Project Muse](https://muse.jhu.edu/); and _Journal of American History_ from 2013–2019 from [Oxford University Press](https://academic.oup.com/journals/). In each of these cases, our access to the journals' content was made possible by institutional subscriptions managed by BYU's [Harold B. Lee Library](https://lib.byu.edu).

For copyright and licensing reasons, the data that we used cannot be shared; as such, the repository contains only scripts and their output, as well as files we have authored. We know this means that our work is not easily reproducible, but we hope making our process visible will allow interested scholars to understand and/or critique how we performed our analysis. 

## Abbreviations
Throughout this project's scripts and their output, we refer to journals by shortened names:
- `amerlite`: _American Literature_
- `amerlitehist`: _American Literary History_ 
- `amerquar`: _American Quarterly_
- `jamericanhistory`: _Journal of American History_
- `jamerstud`: _Journal of American Studies_ 

## Authorship
The contents of this repository were written almost exclusively by [Brian Croxall](https://briancroxall.net) ([ORCID](https://orcid.org/0000-0001-5602-6830)), Assistant Research Professor of [Digital Humanities](https://odh.byu.edu) at [Brigham Young University](https://byu.edu), Provo, Utah, USA. Errors and faults should be attributed to him. His work was conducted in ongoing and iterative dialogue with Brian Russell Roberts.

[Jeremy Browne](https://humanities.byu.edu/person/jeremy-browne-2/) ([ORCID](https://orcid.org/0000-0003-1464-3042)), Associate Research Professor of Digital Humanities at BYU, made important code contributions that assisted with obtaining the data in the abovementioned [third step](borderwaters#data).

## Peer Review
This documentation in this repository was [peer-reviewed](https://github.com/briancroxall/borderwaters/issues/3) by [Rebecca Sutton Koeser](https://rlskoeser.github.io/), Lead Developer at [The Center for Digital Humanities](https://cdh.princeton.edu/) at Princeton University. Because the book was in press at the time of her review, Koeser did not inspect the code.

## License
Code in this repository is licensed with a [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/). Text and data in this repository are licensed with a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

## Citations
We suggest the following approach for citing this repository using the eighth edition of [MLA style](https://style.mla.org/):

> Croxall, Brian. Borderwaters _Repository_. _GitHub_, v1.0.1, 2021, https://github.com/briancroxall/borderwaters. _Zenodo_, https://doi.org/10.5281/zenodo.4689584.

![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4689584.svg)

## Acknowledgments
We very much appreciate the cooperation of the different publishers and database providers in our research. 

This project began, in part, as the [Digital Humanities and Technology](https://odh.byu.edu/dight/) capstone experience for [Lorin Groesbeck](https://www.linkedin.com/in/lorin-groesbeck-5a236b178/) in Winter 2018, after which she graduated with her BA in American Studies. During the capstone, Groesbeck worked with Croxall to, among other things, prepare the data request for JSTOR, to meet with members of BYU's [Copyright Licensing Office](https://copyright.byu.edu/), and to identify how the JSTOR data needed to be cleaned.

[Rob Reynolds](https://humanities.byu.edu/person/rob-reynolds/) ([ORCID](https://orcid.org/0000-0003-0306-087X)), Assistant Research Professor of Digital Humanities at BYU, provided significant advice about all things Python along the way.

Our work relies on an ecosystem of existing open and free software packages, libraries, and languages. We are grateful for the many organizations and individual developers who create well documented, open source software solutions.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Matplotlib](https://matplotlib.org/)
- [Natural Language Toolkit](https://www.nltk.org/)
- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [tqdm](https://github.com/tqdm/tqdm)
- [XpdfReader](https://www.xpdfreader.com/index.html)

Since the work was done across multiple years, particular versions of dependencies were not tracked throughout the project. Python 3 was used throughout.

# Folders
## [`1get_data/`](1get_data/)
As mentioned above, the bulk of our data came from JSTOR (metadata as `.xml` and articles as `.txt`); Duke UP provided additional data for _American Literature_ (metadata as `.xml` and articles as `.pdf`). Since these two datasets were provided to us directly, no work was necessary. 

### [`step-three-collection/`](1get_data/step-three-collection)
[This folder](1get_data/step-three-collection) collects the scripts related to [Step 3](https://github.com/briancroxall/borderwaters#data) of the data (collecting data from the 2010s for years not provided by either JSTOR or Duke UP). This work was begun in August 2018, was revisited in August 2019, and was completed in December 2019, once each journal published its final issue of the decade. 

#### Steps
1. Collect data 
  - articles from _American Literature_ were downloaded manually as `.html`.
  - articles from _American Quarterly_ were downloaded as `.html` using the sequence of Jeremy Browne-authored scripts in the [`amerquar/`](1get_data/step-three-collection/amerquar) folder.
  - articles from _Journal of American History_ were downloaded as `.html` using the sequence of Jeremy Browne-authored scripts in the [`jamericanhistory/`](1get_data/step-three-collection/jamericanhistory) folder.

## [`2clean_data/`](2clean_data/)
Since data from each source were formatted differently, different approaches for cleaning those data had to be developed.

### [`jstor/`](2clean_data/jstor)
[This folder]((2clean_data/jstor)) contains the scripts we used to clean the data we received from JSTOR. The data came as metadata (in `.xml`) and as the text of articles (in `.txt`). While the filename of an article and its metadata matched, they were not human readable. 

#### Steps
1. Rename files using `rename-jstor-full-data.py`; renamed text goes to a `renamed-articles/` folder and renamed metadata goes to a `renamed-metadata/` folder. Renamed files take the following format: `journalAbbreviation_year_vol_issue_firstPage-lastPage_articleID`.
    - During the renaming process, this script funnels articles that were titled (per their metadata) "Front Matter," "Back Matter," "Volume Information," or "Notes on the Contributors" to a `front-matter/` folder. These articles were no longer included in our data moving forward;
2. Use `jstor-clean.py` to clean the contents of `renamed-articles/`, sending output to `simple-cleaned-articles`.
3. Using Finder on Mac OS, copy contents of `simple-cleaned-articles/` to folder containing all articles. 

### [`duke/`](2clean_data/duke)
[This folder](2clean_data/duke) contains the scripts we used to clean the data we received from Duke UP for _American Literature_ for the years 2000-2017. The data were organized in folders for each issue. In each of those folders was a folder of articles in `.pdf` and a folder of metadata in `.xml`. The names of the metadata and `.pdf` files did not match nor were they always human-readable. The data for issue (vol. 86, no.3) was corrupted, so we downloaded it manually.

In looking through the data, we discovered that book reviews often ended on one page and then another review started on that same page. The result was that many book review `.pdf` files would have text from other book reviews on the page. If we wanted to not have duplicated text in the corpus, we needed to handle the book reviews separately.

#### Steps
1. Use `rename-duke.py` to rename both the article `.pdf` and the metadata `.xml`; renamed `.pdf` files go to a `scripted-renamed/pdfs/` folder and renamed metadata goes to a `scripted-renamed/metadata/` folder. Renamed files take the following format: `journalAbbreviation_year_vol_issue_firstPage-lastPage_articleID`. 
  - During the process, the objects that were identified in their metadata as either "Book Review" or "Brief Mention" were renamed and then placed in a separate folder (`scripted-renamed/pdfs/bookreviews/`) so they could be dealt with separately. 
2. Use `duke-duplicate-resolver.py` within the `scripted-renamed/pdfs/bookreviews/` folder. This runs a file comparison (`filecmp`) to check for files that are duplicates (in case two complete reviews appeared on a page) and then removes all but one copy of those files.
3. Combine all the `.pdf` files for book reviews within one issue into a single `.pdf` using Adobe Acrobat, ensuring that there were no duplicate pages. Since there was not a tool within Acrobat to do this, the work was done manually. We saved these files in the `scripted-renamed/pdfs/bookreviews/` folder.
4. Use `extractor-duke.py` to extract text from the different article `.pdf` files; it draws on the `pdftotext` utility within the [XpdfReader](https://www.xpdfreader.com/index.html) package. This script does its best to extract text only from the meaningful regions of the page, ignoring headers, footers, margins, or page-proof borders. Measurements for these regions were found using Adobe Acrobat. The output was saved in an `extracted-text/` folder. 
5. Use `clean-duke.py` to clean errors that appeared in the extracted text using regular expressions. Cleaned text was saved in a `cleaned-text/` folder. In particular, this script corrects the following:
  - `f-` ligatures
  - hyphenated words across page breaks
  - drop caps, which start each article
  - curved quotation marks and apostrophes
  - spacing around the letter `y` when it appeared at the end of a word
6. Using Finder on Mac OS, copy contents of `cleaned-text/` to folder containing all articles. 

### [`step-three-collection/`](2clean_data/step-three-collection)
This folder contains scripts that we used to clean [the data collected in Step 3](https://github.com/briancroxall/borderwaters#data) (the rest of the 2010s that were not provided by JSTOR or Duke UP). 

#### Steps
1. Rename the harvested `.html` files with [Name Mangler](https://manytricks.com/namemangler/) to to match the structure used throughout the project (`journal_year_vol_iss_fpage-lpage_id`).
2. Use `extract-amerlite.py`, `extract-amerquar.py`, and `extract-jamericanhistory.py` to extract the body and notes for each article from the `.html` and save it to a `.txt` format. During this process, the text was cleaned using substitutions via regular expressions. 
3. Using Finder on Mac OS, copy cleaned text files to the folder containing all articles.

## [`3analyze_data/`](3analyze_data/)
[This folder](3analyze_data/) contains the scripts we used to find frequencies for particular terms and then to graph those frequencies. It contains the `.tsv` output files, as well as images that were produced along the way.

### Steps
1. Find the frequency of keywords from the entire corpus (stored in an `articles` folder) using `count-terms.py`. The script uses regular expressions to find different forms of words (e.g., `archipelago`, `archipelagos`, `archipelagoes`, `archipelagic`, etc.). Output is saved in `.tsv` output files by journal title: [`amerlite.tsv`](3analyze_data/amerlite.tsv), [`amerquar.tsv`](3analyze_data/amerlite.tsv), and [`jamericanhistory.tsv`](3analyze_data/jamericanhistory.tsv). Each line of a `.tsv` includes 
- an article ID, the year the article was published;
- its word count (found using the `word_tokenize` module of the [Natural Language Toolkit](https://www.nltk.org/));
- a count of total instances of a term/regular expression in that article;
- a Y/N column that indicates if the term/regular expression appears in the article (1) or not (0);
- a list of all the hits that the regular expression generated. 

At various points, we used this script to create `set`s of terms found by the regular expression and sent these sets to text outputs. This allowed us to look iteratively for false positives and to improve the functioning of the regular expressions. Evidence of these operations is still visible in the code, but since it was an intermediate step, we do not include these word lists in this repository.

Finally, the script creates [`article-counts.txt`](3analyze_data/article-counts.txt), which displays the total number of articles from each journal in the corpus. Note that while we ultimately decided to report on findings from three journals (_American Literature_, _American Quarterly_, _Journal of American History_), the corpus still includes data from the other two journals (_American Literary History_ and _Journal of American Studies_).

2. Graph the frequency of keywords over time (by year and by decade) in the different journals using `graph_terms.py`. The data for this script come from the `.tsv` files created in the previous step with `count-terms.py`. Those data are transformed into new `.tsv` files that are saved to a `counts/` folder. Then within the `counts` folder, two new folders are created: [`article_yn/`](3analyze_data/counts/article_yn) and `total_counts/`. In each folder, the frequency of a term is reported first by journal and then by either a per-year or per-decade basis. The files in [`article_yn/`](3analyze_data/counts/article_yn) report whether a term appears in an article; regardless of whether the term appears once or 100 times, it reports as a `Yes` (1) or `No` (0). The total yeses are then presented for a given year or decade. So `amerlite_archi_decades_article_counts.tsv` in the `article_yn/` folder shows the number of articles in _American Literature_ within which _archipelago_ and its variants appear at least once over the decades of the journal's existence. The files in the `total_counts/` folder report the total number of times a term appears in a given year or decade. N.B. This repository only includes the [`article_yn`](3analyze_data/counts/article_yn) folder since the analysis in _Borderwaters_ is based on it.

The script then graphs the frequency of the keyword using the [Matplotlib](https://matplotlib.org/) library. Plots are saved in an `images/` folder, with a subfolder based on the date the script is run. Within that dated folder are two folders: `normed/` and [`raw/`](3analyze_data/images/2020_1_16). The former contains graphs of the `total_counts` variety that are normalized (hits / number of words per article). The latter contains raw counts. N.B. This repository only includes the `raw` folder that the analysis in _Borderwaters_ is based on.

N.B. To simplify the contents of this repository, we have only included the data in the `counts/` and `images/` folders that correspond to what we report in the conclusion of _Borderwaters_. The visualizations represent the raw data on a per-decade basis and that show whether a term was or was not in an article (rather than total counts within that article). That said, a user could use `count_terms.py` and then `graph_terms.py` to recreate the full range of what we considered.

3. Calculate the number of times `sea(s)`, variants of `ocean`, or both words appear in articles in the 2010s using `sea-ocean-both.py`. The results are saved in `sob-results-2010s.tsv`. These counts were specifically calculated for footnote 61 of the conclusion.

## [`4publication/`](4publication/)
[This folder](4publication/) contains text that was written by Croxall for endnotes to the conclusion of _Borderwaters_.

- `endnote_drafts.md` was created in May 2019.
- `endnote_edits.docx` was created in January 2020 as the draft of the manuscript was nearing completion, and after the third pass of data collection had been completed.

It also contains the [`graphs_publication_excel/`](4publication/graphs_publication_excel) and [`graphs_publication_png/`](4publication/graphs_publication_png) folders. The former contains Excel files that were created to send to Duke University Press in January 2020 as part of the complete manuscript of _Borderwaters_. The files are named by the figure numbers for the manuscript and contain counts and line graphs. The Duke UP team used these files to make their own version of the graphs for the published book. The latter folder contains individual graphs for the conclusion in PNG format, which are the output of [`graph_terms.py`](borderwaters#steps-4). Files are named by figure numbers for the manuscript.

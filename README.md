# Introduction
This repository contains work related to conclusion of [Brian Russell Roberts](https://humanities.byu.edu/person/brian-russell-roberts/)'s book [_Borderwaters_](https://www.dukeupress.edu/borderwaters). The project began in January 2018 and continued through the publication of the book in spring 2021. 

This project was conducted across six separate, private repositories, of which this is one. Prior to the publication of the book, the work was collected and organized in this repository, and then this repository was made public. 

**_Draft statement:_ This documentation in this repo was peer-reviewed by [Rebecca Sutton Koeser](https://rlskoeser.github.io/), Lead Developer at [The Center for Digital Humanities](https://cdh.princeton.edu/) at Princeton University. The code itself was not reviewed since, at the time of review, the book was in press.**

## Authorship
The code in this repo was written exclusively by [Brian Croxall](https://briancroxall.net) (ORCID: [https://orcid.org/0000-0001-5602-6830](https://orcid.org/0000-0001-5602-6830)), Assistant Research Professor of [Digital Humanities](https://odh.byu.edu) at [Brigham Young University](https://byu.edu), Provo, Utah, USA.

## Data

Data for this project were obtained in several steps and from several sources:
1. JSTOR's [Data for Research](https://www.jstor.org/dfr/) provided us with the bulk of the print runs of the following journals: _American Literature_ from 1929-1999; _American Quarterly_ from 1949-2012; and _Journal of American History_ from 1964-2012. In addition, JSTOR provided us with data from _American Literary History_ (1989-2012) and _Journal of American Studies_ (1967-2012) but in the end we decided to focus our efforts only on the first three journals. 
2. [Duke University Press](https://www.dukeupress.edu) provided us with the data for _American Literature_ from 2000 (vol. 72, no. 1) - 2017 (vol. 89, no. 3).
3. Using a combination of scripts and hand-downloads, we collected the remaining data for the 2010s from their respective online platforms: _American Literature_ from 2017-2019 from [Duke University Press](https://dukeupress.edu); _American Quarterly_ from 2013-2019 from [Project Muse](https://muse.jhu.edu/); and _Journal of American History_ from 2013–2019 from [Oxford University Press](https://academic.oup.com/journals/). In each of these cases, our access to the journals' content was made possible by institutional subscriptions managed by BYU's [Harold B. Lee Library](https://lib.byu.edu).

We very much appreciate the cooperation of the different publishers and database providers in our research. We also appreciate [Jeremy Browne](https://humanities.byu.edu/person/jeremy-browne-2/) in [Brigham Young University](https://byu.edu)’s [Office of Digital Humanities](https://odh.byu.edu/) for his help with obtaining the data **in our third step**.

For copyright and licensing reasons, the repository contains only scripts and text that we have written; the data that we used cannot be shared. We know this means that our work is not immediately reproducible, but we hope making our process visible will allow interested parties to see how we did the work. 

## Abbreviations
Throughout this project, we refer to journals by shortened names:
- `amerlite`: _American Literature_
- `amerquar`: _American Quarterly_
- `jamericanhistory`: _Journal of American History_

# Folders
## 1get_data
As mentioned above, the bulk of our data came from JSTOR; Duke UP provided additional data for _American Literature_. Since these two datasets were provided to us directly, no work was necessary. 

### third-pass-articles
This folder collects the scripts related to [Step 3](https://github.com/briancroxall/borderwaters#data) of the data (collecting data from the 2010s for years not provided by either JSTOR or Duke UP). This work was begun in August 2018, was revisited in August 2019, and was completed in December 2019, once the final issue of the decade was published for each journal. 

Steps
1. Collect data 
  - articles from amerlite were downloaded by hand as HTML
  - articles from amerquar were downloaded using the sequence of Jeremy Browne-authored scripts in the `amerquar` folder
  - articles from jamericanhistory were downloaded using the sequence of Jeremy Browne-authored  scripts in the `jamericanhistory` folder
2. Extract text data 
  - use [Name Mangler](https://manytricks.com/namemangler/) to reformat names of the `HTML` files to match the structure used throughout the project (`journal_year_vol_iss_fpage-lpage_id`)
  - use `extract-amerlite.py`, `extract-amerquar.py`, and `extract-jamericanhistory.py` to extract the article from the `HTML` file and save it to a `txt` format.
3. Combine articles 
  - Copy new text files from this step to the folders with the other text data previously obtained. 

## 2clean_data
Given how data from each source was formatted differently, different approaches for cleaning those data had to be developed.

### Duke UP
This folder contains the scripts that we used to clean the data that we received from Duke UP for _American Literature_ for the years 2000-2017. The data were organized in folders for each issue. In each of those folders was a folder of PDFs and a folder of metadata in `XML` format. The names of the metadata and PDF files did not match nor were they always human-readable. The data for issue (vol. 86, no.3) was corrupted, so we downloaded it by hand.

In looking through the data, we discovered that book reviews often ended on one page and then another review started on that same page. The result was that many book review PDFs would have text from other book reviews on the page. If we wanted to not have duplicated text in the corpus, we needed to handle the book reviews separately.

#### Steps
1. Use `rename-duke.py` to rename both the PDFs and metadata; renamed PDFs go to a `scripted-renamed/pdfs` folder and renamed metadata goes to a `scripted-renamed/metadata` folder. Renamed files take the following format: `journalAbbreviation_year_vol_issue_firstPage-lastPage_articleID`. 
  - During the process, the objects that were identified in the metadata as either "Book Review" or "Brief Mention" were renamed and then placed in a separate folder (`scripted-renamed/pdfs/bookreviews`) so they could be dealt with differently. 
2. Use `duke-duplicate-resolver.py` within the `scripted-renamed/pdfs/bookreviews` folder. This runs a file comparison (`filecmp`) to check for files that are duplicates (in case two complete reviews appeared on a page) and then removes all but one copy of those files.
3. Combine all the PDFs for book reviews within one issue into a single PDF using Adobe Acrobat, ensuring that there were no duplicate pages. Since there was not a tool within Acrobat to do this, the work was done by hand. We saved these files in the `scripted-renamed/pdfs/bookreviews` folder.
4. Use `extractor-duke.py` to extract text from the different PDFs; it draws on the `pdftotext` utility within the [XpdfReader](https://www.xpdfreader.com/index.html) package. This script does its best to extract text only from the meaningful regions of the page, ignoring headers, footers, margins, or page-proof borders. Measurements for these regions were found using Adobe Acrobat. The output was saved in an `extracted-text` folder. 
5. Use `clean-duke.py` to clean errors that appeared in the extracted text. Cleaned text was saved in a `cleaned-text` folder. In particular, this script corrects the following:
  - `f-` ligatures
  - hyphenated words across page breaks
  - drop caps which start each article
  - curved quotation marks and apostrophes
  - spacing around the letter `y` when it appeared at the end of a word
6. 3. Using Finder on Mac OS, copy contents of `cleaned-text` to folder containing all articles. **THIS NEEDS MORE EXPLANATION ONCE I KNOW WHAT OTHER SECTIONS LOOK LIKE.**


### jstor
This folder contains the scripts we used to clean the data we received from JSTOR. The data came as metadata (in `.xml`) and as the text of OCR'd articles (in `.txt`). While the filename of an article and its metadata matched, they were not especially human readable. We used `rename-jstor-full-data.py` to rename both files based on the metadata.

#### Steps
1. Rename files using `rename-jstor-full-data.py`; renamed text goes to a `renamed-articles` folder and renamed metadata goes to a `renamed-metadata` folder. Renamed files take the following format: `journalAbbreviation_year_vol_issue_firstPage-lastPage_articleID`
    - During the renaming process, this script funnels articles that were titled (in metadata) "Front Matter," "Back Matter," "Volume Information," or "Notes on the Contributors" to a `front-matter` folder. These articles were no longer included in our data moving forward.
2. Use `jstor-clean.py` to clean the contents of `renamed-articles`, sending output to `simple-cleaned-articles`.
3. Using Finder on Mac OS, copy contents of `simple-cleaned-articles` to folder containing all articles. **THIS NEEDS MORE EXPLANATION ONCE I KNOW WHAT OTHER SECTIONS LOOK LIKE.**

## 3analyze_data
This folder contains the scripts we used to find frequencies for particular terms and then to graph those frequencies. It contains the TSVs of output, as well as images that were produced along the way.

### Steps
1. Find the frequency of keywords from the entire corpus (stored in an `articles` folder) using `count-terms.py`. The script uses regular expressions to find different forms of words (e.g., `archipelago`, `archipelagos`, `archipelagoes`, `archipelagic`, etc.). Output is saved in TSVs by journal title: `amerlite.tsv`, `amerquar.tsv`, and `jamericanhistory.tsv`. Each line of a TSV includes an article ID, the year it was published, its word count (found using the `word_tokenize` module of the [Natural Language Toolkit](https://www.nltk.org/)), and then, for each term/regular expression, a count of total instances in that article, a Y/N column that indicates if the term appears at all in the article (1) or not (0), and a column that lists all the hits that the regular expression generated. 

At various points, we used this script to create `set`s of terms found by the regular expression and sent these sets to text outputs. This allowed us to look iteratively for false positives and to improve the functioning of the regular expressions. Evidence of these operations are still visible in the code, but since it was an intermediate step, we do not include these word lists in this repository.

Finally, the script creates `article-counts.txt`, which displays the total number of articles from each journal in the corpus. Note that while we ultimately decided to report on findings from three journals (_American Literature_, _American Quarterly_, _Journal of American History_), the corpus still includes data from the other two journals (_American Literary History_ and _Journal of American Studies_).

2. Graph the frequency of keywords over time (by year and by decade) in the different journals using `graph_terms.py`. The data for this script come from the TSVs created in the previous step with `count-terms.py`. Those data are transformed into new TSVs that are saved to a `counts` folder. Then within the `counts` folder, two new folders are created: `article_yn` and `total_counts`. In each folder, the frequency of a term is reported first by journal and then by either a per-year or per-decade basis. The files in `article_yn` report whether a time appears in an article; regardless of whether the term appears once or 100 times, it reports as a `Yes` (1) or `No` (0). The total yeses are then presented for a given year or decade. The files in `total_counts` report the total number of times a term appears in a given year or decade. So `amerlite_archi_decades_article_counts.tsv` in the `article_yn` folder shows the number of articles in _American Literature_ within which _archipelago_ and its variants appear at least once over the decades of the journal's existence. 

The script then graphs the frequency of the keyword using the [Matplotlib](https://matplotlib.org/) library. Plots are saved in an `images` folder, with a subfolder based on the date the script is run. With that dated folder are two folders: `normed` and `raw`. The former contains graphs of the `total_counts` variety that are normalized (hits / number of words per article). The latter contains raw counts.

**In our work, we analyzed the data from a number of different perspectives. In the conclusion of _Borderwaters_, we decided to only use visualizations that represent the data on a per-decade basis and that show whether a term was or was not in an article (rather than total counts within that article). To simplify the contents of this repository, we have only included the data in the `counts` and `images` folders that correspond to what we report on in the conclusion. That said, a user could use `count_terms.py` and then `graph_terms.py` to recreate the full range of what we considered.**

3. Calculate the number of times `sea(s)`, variants of `ocean`, or both words appear in articles in the 2010s using `sea-ocean-both.py`. The results are saved in `sob-results-2010s.tsv`. These counts were specifically calculated for footnote 61 of the conclusion.

## 4publication
This folder contains text that was written by Croxall for endnotes to the conclusion of _Borderwaters_.

- `endnote_drafts.md` was created in May 2019
- `endnote_edits.docx` was created in January 2020 as the draft of the manuscript was nearing completion, and after the third pass of data collection had been completed 

It also contains the `graphs_publication_excel` and `graphs_publication_png` folders. The former contains Excel files that were created to send to Duke University Press in January 2020 as part of the complete manuscript of _Borderwaters_. The files are named by the figure numbers for the manuscript and contain counts and line graphs. The Duke UP team used these files to make their own version of the graphs for the published book. The `graphs_publication_png` folder contains individual graphs for the conclusion in PNG format. Files are named by figure numbers for the manuscript.

# TODO
- [ ] [all-archi-files repo](https://github.com/briancroxall/all-archi-files) (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)
- [x] [amerlite repo](https://github.com/briancroxall/amerlite) (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)
- [x] [borderwaters repo](https://github.com/briancroxall/borderwaters)
- [x] [jstor repo](https://github.com/briancroxall/jstor) (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)
- [ ] [proquest repo](https://github.com/briancroxall/proquest) (I think that I don't need anything from here. This was the original grab of data that Jeremy did in Winter 2018 so Lorin would have something to work with. I think that it all ended up being replaced by the JSTOR data and the third-pass. It's useful to keep around, of course, but I don't know that it'd be fair to say that anything we produced here was critical to the finished version of what we published. 17 March 2021: Now I'm not sure that this can be discarded entirely. See the note in all-archi-files readme about the files taken from this repo)
- [x] [second-pass-articles repo](https://github.com/briancroxall/second-pass-articles) (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)



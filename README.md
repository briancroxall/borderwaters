# Introduction
This repository contains work related to conclusion of [Brian Russell Roberts](https://humanities.byu.edu/person/brian-russell-roberts/)'s book [_Borderwaters_](https://www.dukeupress.edu/borderwaters). The project began in winter 2018 and continued through the publication of the book in spring 2021. 

This project was conducted across four separate, private repositories, of which this is one. Prior to the publication of the book, the work was collected and organized in this repository, and then this repository was made public. 

## Data

Data for this project was obtained in several steps and from several sources:
1. JSTOR's [Data for Research](https://www.jstor.org/dfr/) provided us with the bulk of the print runs of the following journals: _American Literature_ from 1929-1999; _American Quarterly_ from 1949-2012; and _Journal of American History_ from 1964-2012. In addition, JSTOR provided us with data from _American Literary History_ (1989-2012) and _Journal of American Studies_ (1967-2012) but in the end we decided to focus our efforts only on the first three journals. 
2. [Duke University Press](https://www.dukeupress.edu) provided us with the data for _American Literature_ from 2000-2017.
3. Using a combination of scripts and hand-downloads, we collected the remaining data for the 2010s from their respective online platforms: _American Literature_ from 2018-2019 from [Duke University Press](https://dukeupress.edu); _American Quarterly_ from 2013-2019 from [Project Muse](https://muse.jhu.edu/); and _Journal of American History_ from 2013–2019 from [Oxford University Press](https://academic.oup.com/journals/). In each of these cases, our access to the journals' content was made possible by institutional subscriptions managed by BYU's [Harold B. Lee Library](https://lib.byu.edu).

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
This folder collects the scripts related to Step 3 of the data (collecting data from the 2010s for years not provided by either JSTOR or Duke UP). This work was begun in August 2019 and completed in December 2019, once the final issue of the decade was published for each journal. 

Steps
1. Collect data 
  - articles from amerlite were downloaded by hand as HTML
  - articles from amerquar were downloaded using the sequence of Jeremy-Browne-authored scripts in the `amerquar` folder
  - articles from jamericanhistory were downloaded using the sequence of Jeremy-Browne-authored  scripts in the `jamericanhistory` folder
2. Extract text data 
  - use [Name Mangler](https://manytricks.com/namemangler/) to reformat names of the `HTML` files to match the structure used throughout the project (`journal_year_vol_iss_fpage-lpage_id`)
  - use `extract-amerlite.py`, `extract-amerquar.py`, and `extract-jamericanhistory.py` to extract the article from the `HTML` file and save it to a `txt` format.
3. Combine articles 
  - Copy new text files from this step with the other text data previously obtained. 

## 2clean_data

### jstor
This folder contains the scripts we used to clean the data we received from JSTOR. The data came as metadata (in `.xml`) and as the text of OCR'd articles (in `.txt`). While the filename of an article and its metadata matched, they were not especially human readable. We used `rename-jstor-full-data.py` to rename both files based on the metadata.

#### Steps
1. Rename files using `rename-jstor-full-data.py`; renamed text goes to a `renamed-articles` folder and renamed metadata goes to a `renamed-metadata` folder. Renamed files take the following format: `journalAbbreviation_year_vol_issue_firstPage-lastPage_articleID`
    - During the renaming process, this script funnels articles that were titled (in metadata) "Front Matter," "Back Matter," "Volume Information," or "Notes on the Contributors" to a `front-matter` folder. These articles were no longer included in our data moving forward.
2. Use `jstor-clean.py` to clean the contents of `renamed-articles`, sending output to `simple-cleaned-articles`.
3. Using Finder on Mac OS, copy contents of `simple-cleaned-articles` to folder containing all articles. **THIS NEEDS MORE EXPLANATION ONCE I KNOW WHAT OTHER SECTIONS LOOK LIKE.**

## 3analyze_data

## 4interpret_data
This folder contains text that was written by Brian Croxall for endnotes to the conclusion of _Borderwaters_.

- `endnote_drafts.md` was created in May 2019
- `endnote_edits.docx` was created in January 2020 as the draft of the manuscript was nearing completion, and after the third pass of data collection had been completed 


# TODO
- [x] borderwaters repo
- [x] proquest repo (I think that I don't need anything from here. This was the original grab of data that Jeremy did in Winter 2018 so Lorin would have something to work with. I think that it all ended up being replaced by the JSTOR data and the third-pass. It's useful to keep around, of course, but I don't know that it'd be fair to say that anything we produced here was critical to the finished version of what we published.)
- [ ] all-archi-files repo
- [x] jstor repo (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)


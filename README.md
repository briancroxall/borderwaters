# Introduction
This repository contains work related to conclusion of [Brian Russell Roberts](https://humanities.byu.edu/person/brian-russell-roberts/)'s book [_Borderwaters_](https://www.dukeupress.edu/borderwaters). The project began in January 2018 and continued through the publication of the book in spring 2021. 

This project was conducted across six separate, private repositories, of which this is one. Prior to the publication of the book, the work was collected and organized in this repository, and then this repository was made public. 

## Data

Data for this project was obtained in several steps and from several sources:
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

### duke
This folder contains the scripts that we used to clean the data that we received from Duke UP for _American Literature_ for the years 2000-2017. The data were organized in folders for each issue. In each of those folders was a folder of PDFs and a folder of metadata in `XML` format. The names of the metadata and PDF files did not match nor were they always human-readable. 

In looking through the data, we discovered that book reviews often ended on one page and then another review started on that same page. The result was that many book review PDFs would have text from other book reviews on the page. If we wanted to not have duplicated text in the corpus, we needed to handle the book reviews separately.

#### Steps
1. Use `rename-duke.py` to rename both the PDFs and metadata; renamed PDFs go to a `scripted-renamed/pdfs` folder and renamed metadata goes to a `scripted-renamed/metadata` folder. Renamed files take the following format: `journalAbbreviation_year_vol_issue_firstPage-lastPage_articleID`. 
  - During the process, the objects that were identified in the metadata as either "Book Review" or "Brief Mention" were renamed and then placed in a separate folder (`scripted-renamed/pdfs/bookreviews`) so they could be dealt with differently. 
2. Use `duplicate-resolver.py` within the `scripted-renamed/pdfs/bookreviews` folder. This runs a `filecmp` to check for files that are exact duplicates and then removes those files.
3. I then looked through the remaining book review files. Many of the issues were reduced to just a single PDF of the book reviews and then one of the "Brief Mentions." But others had individual files for each review in the volume. Since, as mentioned, reviews did not always start at the top of the page, this would have meant that we had duplicate pages within the dataset. To get around this, I found issues with multiple files for book reviews and then combined these PDFs within Adobe Acrobat and eliminated the duplicate pages. There was no tool built into Acrobat to do that work, so I just did this by hand. I then opened each of these new PDFs and made sure that there were no pages missing nor any remaining duplicates. I saved these files in the `scripted-renamed/pdfs/bookreviews` folder.


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
- [ ] all-archi-files repo (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)
- [ ] amerlite repo (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)
- [x] borderwaters repo
- [x] jstor repo (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)
- [x] proquest repo (I think that I don't need anything from here. This was the original grab of data that Jeremy did in Winter 2018 so Lorin would have something to work with. I think that it all ended up being replaced by the JSTOR data and the third-pass. It's useful to keep around, of course, but I don't know that it'd be fair to say that anything we produced here was critical to the finished version of what we published.)
- [ ] second-pass articles (when I've looked at a file in the repo for consideration in this repo, I'll mark it red in OS X)





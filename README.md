# Introduction
This repository contains work related to conclusion of [Brian Russell Roberts](https://humanities.byu.edu/person/brian-russell-roberts/)'s book [_Borderwaters_](https://www.dukeupress.edu/borderwaters). The project began in winter 2018 and continued through the publication of the book in spring 2021. 

This project was conducted across four separate, private repositories, of which this is one. Prior to the publication of the book, the work was collected and organized in this repository, and then this repository was made public. 

## Data

Data for this project was obtained in several steps and from several sources:
1. JSTOR's [Data for Research](https://www.jstor.org/dfr/) provided us with the bulk of the print runs of the following journals: _American Literature_ from 1929-1999; _American Quarterly_ from 1949-2012; and _Journal of American History_ from 1964-2012. In addition, JSTOR provided us with data from _American Literary History_ (1989-2012) and _Journal of American Studies_ (1967-2012) but in the end we decided to focus our efforts only on the first three journals. 
2. [Duke University Press](https://www.dukeupress.edu) provided us with the data for _American Literature_ from 2000-2017.
3. Using a combination of scripts and hand-downloads, we collected the remaining data for the 2010s from their respective online platforms: _American Literature_ from 2018-2019 from [Duke University Press](https://dukeupress.edu); _American Quarterly_ from 2013-2019 from [Project Muse](https://muse.jhu.edu/); and _Journal of American History_ from 2013–2019 from [Oxford University Press](https://academic.oup.com/journals/). In each of these cases, our access to the journals' content was made possible by institutional subscriptions managed by BYU's [Harold B. Lee Library](https://lib.byu.edu).

We very much appreciate the cooperation of the different publishers and database providers in our research. We also appreciate the help of [Jeremy Browne](https://humanities.byu.edu/person/jeremy-browne-2/) in [Brigham Young University](https://byu.edu)’s [Office of Digital Humanities](https://odh.byu.edu/) for his help with obtaining the data **in our third step**.

For copyright and licensing reasons, the repository contains only scripts and text that we have written; the data that we used cannot be shared. We know this means that our work is not immediately reproducible, but we hope making our process visible will allow interested parties to see how we did the work. 

## Abbreviations
Throughout this project, we refer to journals by shortened names:
- `amerlite`: _American Literature_
- `amerquar`: _American Quarterly_
- `jamericanhistory`: _Journal of American History_

# Folders
## 1get_data

### third-pass-articles
This folder collects the scripts related to Step 3 (collecting data from the 2010s for years not provided by either JSTOR or Duke UP). This work was begun in August/September 2019 and completed in December 2019, once the final issue of the decade was published for each journal. 

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


### third-pass-articles
In this folder you will find the scripts related to the August / September 2019 harvesting of 2018 and 2019 data that we used to round out the data for the book. 

We returned to this process in December 2019 to get the last issue of each of the articles. To make this last pass simpler and faster, I eliminated most of the files that we had collected during the Aug/Sep 2019.

Steps
1. Collect data (by hand for amerlite, by script for other two).
2. Clean data (using Name Mangler and various `extract` Python scripts).
3. Copy data from `amerlite-txt`, `amerquar-txt` and `jamericanhistory-txt` to the `articles` folder in the [`all-archi-files`](https://github.com/briancroxall/all-archi-files) repo.
4. In December 2019, copy data from `amerlite-dec2019-txt`, `amerquar-dec2019-txt`, and `jamericanhistory-dec2019-txt` folders to the `articles` folder in the [`all-archi-files`](https://github.com/briancroxall/all-archi-files) repo.

#### amerlite
I started in this folder with duplicates of the files from the `hand-downloads` folder.

Steps
1. Use [Name Mangler](https://manytricks.com/namemangler/) to change names from the format `“An Extreme Sense of Protest against Everything”_ Chester Himes’s Prison Novel _ American Literature _ Duke University Press.html` to `An_Extreme_Sense_of_Protest_against_Everything-Chester_Himess_Prison_Novel-American_Literature.html`. Got rid of the smart quotes and apostrophes, spaces, the press's name.
	
  * With the Dec 2019 collection, I used Name Mangler to remove smart quotes and apostropes, spaces, the press's name, and the journal's name.
2. Run `extract-amerlite.py`, which extracts text and saves results in the folder `amerlite-txt`. This script was based on  `extract-amerquar.py` in this repo, but was modified to fit its metadata peculiarities.

#### amerlite-txt
Text files generated from `amerlite` folder (see above).

##### hand-downloads
This folder contains the HTML that I hand-downloaded directly from Duke UP (via BYU's Library) for the 2018 and 2019 articles. 

##### hand-downloads-dec2019
This folder contains the HTML that I hand-downloaded directly in December 2019 from Duke UP (via BYU's Library) for the final 2019 issue.

#### amerlite-dec2019-txt
Text files generated from `amerlite` folder (see above) in December 2019. This is the final issue of the decade. I created a separate folder so I wouldn't have to delete the current text files. 

#### amerquar
This folder contains the Python scripts that Jeremy Browne wrote to index and then download the 2018 and 2019 _American Quarterly_ articles from Project Muse. `indexes.txt`, `articles.txt`, and the `indexes` folder are all parts of the scripts. The `articles` folder contains the saved HTML output that we will work on.

Steps
1. Use Name Mangler to add `amerquar_` to the beginning of each file name and to replace `-` with `_` throughout the name.
2. Run `extract-amerquar.py`, which extracts text, cleans it, and saves results in the folder `amerquar-txt`. This script was based on the `extract-jamericanhistory.py` script in this repo and then updated to fit the particular metadata schema.

#### amerquar-txt
Text files generated from `amerquar` folder (see above).

#### amerquar-dec2019-txt
Text files generated from `amerquar` folder (see above) in December 2019. This is the final issue of the decade. I created a separate folder so I wouldn't have to delete the current text files. 

#### jamericanhistory
This folder contains the Python scripts that Jeremy Browne wrote to index and then download the 2018 and 2019 _Journal of American History_ articles from Oxford UP. `indexes.txt`, `articles.txt`, and the `indexes` folder are all parts of the scripts. The `articles` folder contains the saved HTML output that we will work on.

Steps
1. Use Name Mangler to add `jamericanhistory_` to the beginning of each file name and to replace `-` with `_` throughout the name.
2. Run `extract-jamericanhistory.py`, which extracts text and saves results in the folder `jamericanhistory-txt`. This script was based on the similarly named script in the [second-pass-articles](https://github.com/briancroxall/second-pass-articles) repo.

#### jamericanhistory-txt
Text files generated from `jamericanhistory` folder (see above).

#### jamericanhistory-dec2019-txt
Text files generated from `jamericanhistory` folder (see above) in December 2019. This is the final issue of the decade. I created a separate folder so I wouldn't have to delete the current text files. 

## 2clean_data

## 3analyze_data

## 4interpret_data
This folder contains text that was written by Brian Croxall for endnotes to the conclusion of _Borderwaters_.

- `endnote_drafts.md` was created in May 2019
- `endnote_edits.docx` was created in January 2020 as the draft of the manuscript was nearing completion


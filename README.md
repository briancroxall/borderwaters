# borderwaters
This repository contains work related to conclusion for [Brian Russell Roberts](https://humanities.byu.edu/person/brian-russell-roberts/)'s book [_Borderwaters_](https://www.dukeupress.edu/borderwaters). The work for this project began in winter 2018 and continued through the publication of the book in spring 2021. 

For copyright reasons, the repo mostly contains only scripts and text that we have written. The data that we used cannot be shared. We know this means that our work is not immediately reproducible but we hope that making our process visible will allow interested parties to see how we did the work. 

# Folders
## third-pass-articles
In this folder you will find the scripts related to the August / September 2019 harvesting of 2018 and 2019 data that we used to round out the data for the book. 

We returned to this process in December 2019 to get the last issue of each of the articles. To make this last pass simpler and faster, I eliminated most of the files that we had collected during the Aug/Sep 2019.

Steps
1. Collect data (by hand for amerlite, by script for other two).
2. Clean data (using Name Mangler and various `extract` Python scripts).
3. Copy data from `amerlite-txt`, `amerquar-txt` and `jamericanhistory-txt` to the `articles` folder in the [`all-archi-files`](https://github.com/briancroxall/all-archi-files) repo.
4. In December 2019, copy data from `amerlite-dec2019-txt`, `amerquar-dec2019-txt`, and `jamericanhistory-dec2019-txt` folders to the `articles` folder in the [`all-archi-files`](https://github.com/briancroxall/all-archi-files) repo.

### amerlite
I started in this folder with duplicates of the files from the `hand-downloads` folder.

Steps
1. Use [Name Mangler](https://manytricks.com/namemangler/) to change names from the format `“An Extreme Sense of Protest against Everything”_ Chester Himes’s Prison Novel _ American Literature _ Duke University Press.html` to `An_Extreme_Sense_of_Protest_against_Everything-Chester_Himess_Prison_Novel-American_Literature.html`. Got rid of the smart quotes and apostrophes, spaces, the press's name.
	
  * With the Dec 2019 collection, I used Name Mangler to remove smart quotes and apostropes, spaces, the press's name, and the journal's name.
2. Run `extract-amerlite.py`, which extracts text and saves results in the folder `amerlite-txt`. This script was based on  `extract-amerquar.py` in this repo, but was modified to fit its metadata peculiarities.

### amerlite-txt
Text files generated from `amerlite` folder (see above).

#### hand-downloads
This folder contains the HTML that I hand-downloaded directly from Duke UP (via BYU's Library) for the 2018 and 2019 articles. 

#### hand-downloads-dec2019
This folder contains the HTML that I hand-downloaded directly in December 2019 from Duke UP (via BYU's Library) for the final 2019 issue.

### amerlite-dec2019-txt
Text files generated from `amerlite` folder (see above) in December 2019. This is the final issue of the decade. I created a separate folder so I wouldn't have to delete the current text files. 

### amerquar
This folder contains the Python scripts that Jeremy Browne wrote to index and then download the 2018 and 2019 _American Quarterly_ articles from Project Muse. `indexes.txt`, `articles.txt`, and the `indexes` folder are all parts of the scripts. The `articles` folder contains the saved HTML output that we will work on.

Steps
1. Use Name Mangler to add `amerquar_` to the beginning of each file name and to replace `-` with `_` throughout the name.
2. Run `extract-amerquar.py`, which extracts text, cleans it, and saves results in the folder `amerquar-txt`. This script was based on the `extract-jamericanhistory.py` script in this repo and then updated to fit the particular metadata schema.

### amerquar-txt
Text files generated from `amerquar` folder (see above).

### amerquar-dec2019-txt
Text files generated from `amerquar` folder (see above) in December 2019. This is the final issue of the decade. I created a separate folder so I wouldn't have to delete the current text files. 

### jamericanhistory
This folder contains the Python scripts that Jeremy Browne wrote to index and then download the 2018 and 2019 _Journal of American History_ articles from Oxford UP. `indexes.txt`, `articles.txt`, and the `indexes` folder are all parts of the scripts. The `articles` folder contains the saved HTML output that we will work on.

Steps
1. Use Name Mangler to add `jamericanhistory_` to the beginning of each file name and to replace `-` with `_` throughout the name.
2. Run `extract-jamericanhistory.py`, which extracts text and saves results in the folder `jamericanhistory-txt`. This script was based on the similarly named script in the [second-pass-articles](https://github.com/briancroxall/second-pass-articles) repo.

### jamericanhistory-txt
Text files generated from `jamericanhistory` folder (see above).

### jamericanhistory-dec2019-txt
Text files generated from `jamericanhistory` folder (see above) in December 2019. This is the final issue of the decade. I created a separate folder so I wouldn't have to delete the current text files. 
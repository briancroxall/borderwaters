# borderwaters
Scripts related to the _Borderwaters_ project.

# Folders
## third-pass-articles
In this folder you will find the scripts related to the August / September harvesting of 2018 and 2019 data that we used to round out the data for the book.

### amerlite
This folder contains the HTML that I hand-downloaded directly from Duke UP (via BYU's Library) for the 2018 and 2019 articles. 

### jamericanhistory
This folder contains the Python scripts that Jeremy Browne wrote to index and then download the 2018 and 2019 _Journal of American History_ articles from Oxford UP. `indexes.txt`, `articles.txt`, and the `indexes` folder are all parts of the scripts. The `articles` folder contains the saved HTML output that we will work on.

Steps
1. Use Name Mangler to add `jamericanhistory_` to the beginning of each file name and to replace `-` with `_` throughout the name.
2. Run `extract-jamericanhistory.py`, which extracts text and saves results in the folder `jamericanhistory-txt`. This script was based on the similarly named script in the [second-pass-articles](https://github.com/briancroxall/second-pass-articles) repo.

### amerquar
This folder contains the Python scripts that Jeremy Browne wrote to index and then download the 2018 and 2019 _American Quarterly_ articles from Project Muse. `indexes.txt`, `articles.txt`, and the `indexes` folder are all parts of the scripts. The `articles` folder contains the saved HTML output that we will work on.

Steps
1. Use Name Mangler to add `amerquar_` to the beginning of each file name and to replace `-` with `_` throughout the name.
2. Run `extract-amerquar.py`, which extracts text, cleans it, and saves results in the folder `amerquar-txt`. This script was based on the `extract-jamericanhistory.py` script in this repo and then updated to fit the particular metadata schema.
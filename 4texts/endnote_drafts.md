# Paragraphs for BR book
## Data Provenance footnote (full)
We obtained the data for the three journals we analyze through four different steps. First, JSTOR’s Data for Research service provided us with the bulk of the journals’ print runs: *American Quarterly* from 1949-2012 (4,167 articles); *American Literature* from 1929-1999 (8,609 articles); and *Journal of American History* from 1964-2012 (27,170 articles). The data we received from JSTOR included plain text files of the articles, including notes and works cited, and metadata. Prior to analysis, we used Python to clean XML artifacts from the JSTOR text files. The code for this part of the project can be found at https://github.com/briancroxall/jstor. 

Second, Duke University Press provided us with the data for *American Literature* from 2000-2017 (approximately 692 articles). The data we received included PDFs and metadata. Prior to analysis, we extracted the text layer from the PDFs using the pdftotext module from the [Poppler](https://poppler.freedesktop.org/) library. The output, including notes and works cited, was then cleaned  using Python. The code for this part of the project can be found at https://github.com/briancroxall/amerlite. 

Third, we downloaded the data for *Journal of American History* from 2013-2017 (587 articles) directly from the Oxford University Press website. The articles were retrieved as HTML, and text, including notes, was extracted using Python. The code for this part of the project can be found at https://github.com/briancroxall/second-pass-articles. 

Fourth, we downloaded the data for *American Quarterly* from 2012-2017 (440 articles) from Project Muse. The articles were retrieved as HTML, and text, including notes, was extracted using Python. The code for this part of the project can be found at https://github.com/briancroxall/proquest. 

We very much appreciate the cooperation of the different publishers and database providers in our research. We also appreciate the help of Jeremy Browne in Brigham Young University’s Office of Digital Humanities for his help scraping the third and fourth tranches of our data. 

## Data Provenance footnote (short)
We obtained the data for the three journals we analyze through four different steps. First, JSTOR’s Data for Research service provided us with the bulk of the journals’ print runs: *American Quarterly* from 1949-2012 (4,167 articles); *American Literature* from 1929-1999 (8,609 articles); and *Journal of American History* from 1964-2012 (27,170 articles). Second, Duke University Press provided us with the data for *American Literature* from 2000-2017 (approximately 692 articles). Third, we downloaded the data for *Journal of American History* from 2013-2017 (587 articles) directly from the Oxford University Press website. Fourth, we downloaded the data for *American Quarterly* from 2012-2017 (440 articles) from Project Muse. We very much appreciate the cooperation of the different publishers and database providers in our research. We also appreciate the help of Jeremy Browne in Brigham Young University’s Office of Digital Humanities for his help scraping the third and fourth tranches of our data. 

## Search terms / process note (full)
We traced search terms within the corpus using regular expressions. Regular expressions allow for searching for very particular strings of text, similar to what one finds in a “find and replace” tool within a word processor. Insofar as regular expressions accommodate pattern-matching on or around metacharacters (e.g., all digits or word boundaries), they allow for searching that is simultaneously more expansive and more precise. For example, our regular expression for *archipelago* finds many forms of the term, including singular (*archipelago*), plural (*archipelagos* or *archipleagoes*), adjectival (*archipelagic* or *archipelic*), possessive (*archipelago’s*) and compound (*transarchipelagic* and *meta-archipelagic*). Moreover, a regular expression allows us to anticipate characters that are known to give optical-character recognition (OCR) tools difficulties. When the original, 1929 issues of *American Literature* were scanned, for example, there was a chance that the *i* in *archipelago* could have been misinterpreted as a *l* or a *1*. The regular expression we used made it possible to allow for *arch1pelic* or *archlpelagic*. Since regular expressions can, as mentioned, be both precise and expansive, our scripts did more than simply count the words that appeared.  Each instance of a “hit” was saved to a spreadsheet, connected to the article in which it appeared, so we could monitor the performance of the code. 

We followed the same principles in designing the regular expressions for *island*, *ocean*, *mainland*, *continent*, and *transnational*. The basic search for the first, for example, looked primarily for the characters *isl* as this made it possible to capture appearances of the singular and plural of both *island* and *isle*. Monitoring the results, we saw a number of false positives for words like *aisle* or *Carlisle*. We adjusted the regular expression to avoid these terms while continuing to allow for *transislandic* or *island-hopper*. Similarly, our search for *continent* allows for *metatranscontinentalisms* but avoids the red herring *incontinent*. 

We created a much more narrow regular expression for *sea*, one which *only* identifies the singular and the plural, *seas*. The decision to narrow the scope in this manner was due to the much higher frequency of the letters *sea* appearing in words that were not related to the world’s waterways. As a result, terms such as *seafaring* or *seaside* do not appear in such searches.

The code for counting the frequency of the different terms, including the different regular expressions, can be found at https://github.com/briancroxall/all-archi-files. 

## Search terms / process note (short)
We traced search terms within the corpus using regular expressions. Regular expressions allow for searching for very particular strings of text, similar to what one finds in a “find and replace” tool within a word processor. Insofar as regular expressions accommodate pattern-matching on or around metacharacters (e.g., all digits or word boundaries), they allow for searching that is simultaneously more expansive and more precise. For example, our regular expression for *archipelago* finds many forms of the term, including singular (*archipelago*), plural (*archipelagos* or *archipleagoes*), adjectival (*archipelagic* or *archipelic*), possessive (*archipelago’s*), and compound (*transarchipelagic* and *meta-archipelagic*). Each instance of a “hit” was saved to a spreadsheet, connected to the article in which it appeared, so we could monitor the performance of the code and eliminate false positives through refinements. We followed the same principles in designing the regular expressions for *island*, *ocean*, *mainland*, *continent*, and *transnational*. We created a much more narrow regular expression for *sea*, one which *only* identifies the singular and the plural, *seas*. 

## Search terms / process note (really short)
We traced search terms within the corpus using regular expressions. Regular expressions allow for searching for very particular strings of text, similar to what one finds in a “find and replace” tool within a word processor. Insofar as regular expressions accommodate pattern-matching on or around metacharacters (e.g., all digits or word boundaries), they allow for searching that is simultaneously more expansive and more precise. For example, our regular expression for *archipelago* finds many forms of the term, including singular (*archipelago*), plural (*archipelagos* or *archipleagoes*), adjectival (*archipelagic* or *archipelic*), possessive (*archipelago’s*), and compound (*transarchipelagic* and *meta-archipelagic*). Each instance of a “hit” was saved to a spreadsheet, connected to the article in which it appeared, so we could monitor the performance of the code and eliminate false positives through refinements. 
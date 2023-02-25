# Python-project
A program that reports the five most frequent two-word sequences in a text file download from Project Gutenberg

The program will:
1.	Find the beginning and the end of the text (look for the markers "*** START OF THE PROJECT GUTENBERG EBOOK..." and "*** END OF THE PROJECT GUTENBERG EBOOK...") and discard everything before the beginning and after the end, including the markers.

2.	Break the text into words using spaces as separators. 
3.	Convert each word to lowercase and remove the punctuation, if any. If a "word" consists only of punctuation, discard it entirely. Thus, "Huck Finn is drawn from life ; Tom Sawyer also, but" shall become "huck finn is drawn from life tom sawyer also but". 
4.	Count all combinations of two consecutive words (they are known as bigrams -- e.g., "huck finn," "finn is," "is drawn," "drawn from") and report the ten most frequent of them.
Test your program by counting bigrams in https://www.gutenberg.org/files/74/74-0.txt. Do not write code for downloading the file.
Deliverables: the Python file and the output of the program as a text file with the bigrams and their counts, one result per line, ordered in the decreasing order of counts (the most frequent bigram at the top).

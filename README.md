# typeProofer
A python script for proofing typefaces

# Description
Are you just like me fed up with using heavy and cumbersome InDesign files for proofing your fonts? Well... exit InDesign, here's typeProofer!
Use this script to proof your typefaces by running it in Drawbot app.
It collects font files (.otf, .ttf), reads .txt files and saves a PDF with the text from the .txt files set in the fonts.

![](https://github.com/originaltype/typeProofer/blob/main/img/Screen%20Shot%202021-04-19%20at%2016.22.00.png)



# How to use this script
* Download or clone this repository
* Place your font files in the ```/source/fonts``` directory
* Place your txt files with your proofing text strings in the ```/source/txt``` directory. If there is a .txt file present named ```paragraph.txt``` it will use the contents of this file to type set a page with a 2-column paragraph setting.
* Download and fire up [Drawbot](https://www.drawbot.com/)
* Open ```typeProofer.py``` in Drawbot
* Replace Original Type with your name between the quotation marks in ```myName = 'Original Type'```
* Run the script
* Go to ```/source/proofs``` and open the PDF.

# To do
- [ ] Add page template for large words setting
- [X] Save the PDF with time stamp and project name in the file name
- [ ] Make lay-out dimensions and positions relative to the page so that you can easily change the page size
- [ ] Make option to set proofing strings in various font sizes on the page
- [ ] Make the order the fonts in the PDF based on weight and width class
- [ ] Proof text with OT features activated

# Credits
This script was written applying the things I learned while following [@roberto-arista's](https://github.com/roberto-arista) great [Python for Designers course](https://pythonfordesigners.com/). Parts of the code in the first draft of the script we're written in a very make-do style, Roberto was so kind to afterwards clean up the code.

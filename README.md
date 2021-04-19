# typeProofer
A python script for proofing typefaces

# Description
Are you just like me fed up with using heavy and cumbersome InDesign files for proofing your fonts? Well... exit InDesign, here's typeProofer!
Use this script to proof your typefaces by running it in Drawbot app.
It collects font files (.otf, .ttf), reads .txt files and saves a PDF with the text from the .txt files set in the fonts.

![](https://github.com/originaltype/typeProofer/blob/main/img/Screen%20Shot%202021-04-19%20at%2016.22.00.png)



# How to use this script
* Download or clone this repository
* Place your font files in the ```./fonts``` directory
* Place your txt files with your proofing text strings in the ```./txt``` directory. If there is a .txt file present named ```paragraph.txt``` it will use the contents of this file to type set a page with a 2-column paragraph setting.
* Download and fire up [Drawbot](https://www.drawbot.com/)
* Open ```typeProofer.py``` in Drawbot
* Replace Original Type with your name between the quotation marks in ```myName = 'Original Type'```
* Run the script
* Go to ```./proofs``` and open the PDF.

# To do
- [ ] Add page template for large words setting
- [ ] Save file with time stamp and project name in the file name
- [ ] Make lay-out dimensions and positions relative to the page so that you can easily change the page size

# Credits
This script was written while following [@roberto-arista's](https://github.com/roberto-arista) [Python for Designers course](https://pythonfordesigners.com/) so lot's of credits to him for his guidance and help.

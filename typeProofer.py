"""
Make a PDF proof using a folder of fonts and a folder of txt files as input.
If there is a file calles 'paragraph.txt' in the directory './txt', the script will use the text in that file to create a page with two columns paragraph text setting.
"""


# --- Modules ------------------------------------------------------------- #
import datetime
now = datetime.datetime.now()
import os
from os.path import join, isfile
from os import listdir
from pathlib import Path


# --- Constants ------------------------------------------------------------- #

# set your name in the footer
myName = 'Original Type'

# set paths to directories with fonts and txt files
fontFolder = './fonts'
txtFolder = './txt'

# set font sizes
fontSizeLarge = 28
fontSizeParagraph9 = 9
fontSizeParagraph12 = 12

# set page dimensions and positions for header and footer items
PAGE_FORMAT = 'A4Landscape'
FROM_MM_TO_PT = 2.834627813

MARGIN_BOTTOM = 20*FROM_MM_TO_PT
MARGIN_X1 = 20*FROM_MM_TO_PT
MARGIN_X2 = 70*FROM_MM_TO_PT
MARGIN_X3 = 120*FROM_MM_TO_PT
MARGIN_X4 = 200*FROM_MM_TO_PT
MARGIN_X5 = 270*FROM_MM_TO_PT

# large sample textbox dimensions
large = MARGIN_X1, 20*FROM_MM_TO_PT, 262*FROM_MM_TO_PT, 165*FROM_MM_TO_PT

# paragraph sample textbox dimensions
ParagraphBox1 = MARGIN_X1, 20*FROM_MM_TO_PT, 121*FROM_MM_TO_PT, 162*FROM_MM_TO_PT
ParagraphBox2 = MARGIN_X1*8, 20*FROM_MM_TO_PT, 121*FROM_MM_TO_PT, 162*FROM_MM_TO_PT


# --- Functions ------------------------------------------------------------- #

def typeAttributes():
    fill(0)
    stroke(None)
    font('SFMono-Regular', 8)

# draw the header and footer
def drawHeaderFooter():
    p = Path(fileName)
    print(p.stem)
    projectName = fontName.split('-')
    typeAttributes()
    text('Project:' + ' ' + projectName[0], (MARGIN_X1, height()-14*FROM_MM_TO_PT), align='left')
    text(f'Date: {now:%Y-%m-%d %H:%M}', (MARGIN_X2, height()-14*FROM_MM_TO_PT), align='left')
    text(f'Fontfile: {fontName}', (MARGIN_X3, height()-14*FROM_MM_TO_PT))
    text('Characterset:' + ' ' + p.stem, (MARGIN_X4, height()-14*FROM_MM_TO_PT))
    text(f'Page {pageCount()-1:0>2d}/', (MARGIN_X5, height()-14*FROM_MM_TO_PT), align='right')
    text(f'© {now:%Y}' + ' ' + myName, (MARGIN_X1, MARGIN_BOTTOM/2))
    
# read lines from a texfile
def readStringsFromFile(fileName):
    with open(fileName, mode='r', encoding='utf-8') as txtFile:
        return [ll.rstrip() for ll in txtFile.readlines()]

# collect font files from folder
def collectFilesPaths(folder, extension=''):
    """hidden files (starting with a dot) are filtered out"""
    paths = []
    for eachFileName in [nn for nn in listdir(folder) if not nn.startswith('.')]:
        eachPath = join(folder, eachFileName)
        if isfile(eachPath) and eachPath.endswith(extension):
            paths.append(eachPath)
    return paths

# draw a page
def initPage():
    t1 = '\n'.join(proofSet)
    t2 = '\n'.join(proofSet)
    while len(t1):
        newPage(PAGE_FORMAT)
        fill(1)
        fill(0)
        if fileName == './txt/paragraph.txt':
            typeAttributes()
            text(f'{fontName}'+' '+'9 pts', (MARGIN_X1, height()-25*FROM_MM_TO_PT))
            font(fontName, fontSizeParagraph9)
            t1 = textBox(f'{t1}', (ParagraphBox1))
            typeAttributes()
            text(f'{fontName}'+' '+'12 pts', (MARGIN_X1*8, height()-25*FROM_MM_TO_PT))
            font(fontName, fontSizeParagraph12)
            t2 = textBox(f'{t2}', (ParagraphBox2))
        else:
            font(fontName, fontSizeLarge)
            t1 = textBox(f'{t1}', (large))
        drawHeaderFooter()
        

# --- Instructions ------------------------------------------------------------- #

# store fonts and txt files in a variable
allFonts = collectFilesPaths(fontFolder)
alltxtFiles = collectFilesPaths(txtFolder)

# iterate over all fonts and text files and draw the pages
for eachFontPath in allFonts:
    for fileName in alltxtFiles:
        fontName = installFont(eachFontPath)
        proofSet = readStringsFromFile(fileName)
        initPage()
    
# get all pages
allPages = pages()
# count how many pages are available
totalPages = len(allPages)
# loop over allpages
for page in allPages:
    # set the page as current context
    with page:
        # draw the total pagecount in each of them
        typeAttributes()
        text(f'{totalPages}', (270*FROM_MM_TO_PT, height()-14*FROM_MM_TO_PT), align='left')

    
saveImage("./proofs/typeProof.pdf")
# if autoOpen:
#     os.system(f"open -a Preview {'./proofs/typeProof.pdf'}")
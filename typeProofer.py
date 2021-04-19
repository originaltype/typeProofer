"""
Make a PDF proof using a folder of fonts and a folder of txt files as input.
"""


# --- Modules --- #
import datetime
now = datetime.datetime.now()
import os
from os.path import join, isfile
from os import listdir
from pathlib import Path

# --- Constants --- #
# set paths to directories with fonts and txt files
fontFolder = './fonts'
txtFolder = './txt'

# set font sizes
fontSizeLarge = 48
fontSizeParagraphSmall = 9

FROM_MM_TO_PT = 2.834627813
PAGE_FORMAT = 'A4Landscape'

LINE_HEIGHT = 16
MARGIN_BOTTOM = 20*FROM_MM_TO_PT
MARGIN_X1 = 20*FROM_MM_TO_PT
MARGIN_X2 = 70*FROM_MM_TO_PT
MARGIN_X3 = 120*FROM_MM_TO_PT
MARGIN_X4 = 200*FROM_MM_TO_PT
MARGIN_X5 = 270*FROM_MM_TO_PT

x, y, w, h = MARGIN_X1, 20*FROM_MM_TO_PT, 262*FROM_MM_TO_PT, 165*FROM_MM_TO_PT

# --- Functions --- #
def typeAttributes(pointSize=8):
    fill(0)
    stroke(None)
    familyName = 'ColomMono'
    styleName = 'Regular'
    font(f'{familyName}-{styleName}', pointSize)

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
    text(f'Page {pageCount()-1:0>2X}/', (MARGIN_X5, height()-14*FROM_MM_TO_PT), align='right')
    text('Original Type', (MARGIN_X1, MARGIN_BOTTOM/2))
    
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

# draw the page
def initPage():
    t = proofSet
    while len(t):
        newPage(PAGE_FORMAT)
        fill(1)
        rect(x, y, w, h)
        fill(0)
        font(fontName, fontSizeLarge)
        t = textBox(f'{t}', (x, y, w, h))
        drawHeaderFooter()
        
# draw the paragraph page
def initPragraphPage():
    t = proofSet
    while len(t):
        newPage(PAGE_FORMAT)
        fill(1)
        rect(x, y, w, h)
        fill(0)
        font(fontName, fontSizeParagraphSmall)
        t = textBox(f'{t}', (x, y, w, h))
        drawHeaderFooter()

# --- Variables --- #

# --- Instructions --- #
# store fonts and txt files in a variable
allFonts = collectFilesPaths(fontFolder)
alltxtFiles = collectFilesPaths(txtFolder)
print(alltxtFiles)

# interate over all fonts and text files and draw the pages
for eachFontPath in allFonts:
    for fileName in alltxtFiles:
        fontName = installFont(eachFontPath)
        proofSet = readStringsFromFile(fileName)
        if proofSet is './txt/paragraph.txt':
            initPragraphPage()
        else:
            initPage()
    
# get all pages
allPages = pages()
# count how many pages are available
totalPages = len(allPages)
# loop over allpages
for page in allPages:
    # set the page as current context
    with page:
        # draw a text in each of them
        typeAttributes()
        text(f'{totalPages}', (270*FROM_MM_TO_PT, height()-14*FROM_MM_TO_PT), align='left')

    
saveImage("./proofs/typeProof.pdf")
# if autoOpen:
#     os.system(f"open -a Preview {'./proofs/typeProof.pdf'}")

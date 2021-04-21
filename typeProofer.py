"""
Make a PDF proof using a folder of fonts and a folder of txt files as input.
If there is a file calles 'paragraph.txt' in the directory './txt', the script will use the text in that file to create a page with two columns paragraph text setting.
"""


# --- Modules ------------------------------------------------------------- #
import datetime
import os
from os.path import join, isfile
from os import listdir
from pathlib import Path
from drawBot import fill, stroke, font, text, height, newPage, textBox
from drawBot import installFont, pages, pageCount, saveImage
from fontTools.ttLib.ttFont import TTFont

# --- Constants ------------------------------------------------------------- #

# just now
NOW = datetime.datetime.now()

# set your name in the footer
MY_NAME = 'Original Type'

# set paths to directories with fonts and txt files
FONT_FOLDER = './fonts'
TXT_FOLDER = './txt'
proofFolder = './proofs'

# set font sizes
FONT_SIZE_LARGE = 28
FONT_SIZE_PAR_SMALL = 9
FONT_SIZE_PAR_MED = 12

# set page dimensions and positions for header and footer items
PAGE_FORMAT = 'A4Landscape'
FROM_MM_TO_PT = 2.834627813

MARGIN_BOTTOM = 20*FROM_MM_TO_PT
MARGIN_X1 = 20*FROM_MM_TO_PT
MARGIN_X2 = 70*FROM_MM_TO_PT
MARGIN_X3 = 120*FROM_MM_TO_PT
MARGIN_X4 = 200*FROM_MM_TO_PT
MARGIN_X5 = 270*FROM_MM_TO_PT

# Open the PDF after saving in Preview True or False
AUTO_OPEN = True

# large sample textbox dimensions
LARGE = MARGIN_X1, 20*FROM_MM_TO_PT, 262*FROM_MM_TO_PT, 165*FROM_MM_TO_PT

# paragraph sample textbox dimensions
BOX1 = MARGIN_X1, 20*FROM_MM_TO_PT, 121*FROM_MM_TO_PT, 162*FROM_MM_TO_PT
BOX2 = MARGIN_X1*8, 20*FROM_MM_TO_PT, 121*FROM_MM_TO_PT, 162*FROM_MM_TO_PT


# --- Functions ------------------------------------------------------------- #

def typeAttributes():
    fill(0)
    stroke(None)
    font('SFMono-Regular', 8)

# draw the header and footer
def drawHeaderFooter(postscriptFontName, fileName):
    p = Path(fileName)
    familyName = postscriptFontName.split('-')[0]
    typeAttributes()
    text(f'Project: {familyName}', (MARGIN_X1, height()-14*FROM_MM_TO_PT), align='left')
    text(f'Date: {NOW:%Y-%m-%d %H:%M}', (MARGIN_X2, height()-14*FROM_MM_TO_PT), align='left')
    text(f'Fontfile: {postscriptFontName}', (MARGIN_X3, height()-14*FROM_MM_TO_PT))
    text(f'Characterset: {p.stem}', (MARGIN_X4, height()-14*FROM_MM_TO_PT))
    text(f'Page {pageCount()-1:0>2d}/', (MARGIN_X5, height()-14*FROM_MM_TO_PT), align='right')
    text(f'© {NOW:%Y}' + ' ' + MY_NAME, (MARGIN_X1, MARGIN_BOTTOM/2))

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

def sortFonts(fontPaths):
    return sorted(fontPaths, key=lambda ff: TTFont(file=ff)["OS/2"].usWeightClass)

def drawTwoColumnsLayout(txt, postscriptFontName):
    typeAttributes()
    text(f'{postscriptFontName} 9 pts', (MARGIN_X1, height()-25*FROM_MM_TO_PT))
    font(postscriptFontName, FONT_SIZE_PAR_SMALL)
    textBox(f'{txt}', (BOX1))
    typeAttributes()
    text(f'{postscriptFontName} 12 pts', (MARGIN_X1*8, height()-25*FROM_MM_TO_PT))
    font(postscriptFontName, FONT_SIZE_PAR_MED)
    textBox(f'{txt}', (BOX2))
    # we don't aknowledge overflow, so we return an empty string
    return ""

def drawOneColumnsLayout(txt, postscriptFontName):
    font(postscriptFontName, FONT_SIZE_LARGE)
    txt = textBox(f'{txt}', (LARGE))
    return txt

def drawProof(proofSet, postscriptFontName):
    txt = '\n'.join(proofSet)
    while txt:
        newPage(PAGE_FORMAT)
        fill(0)
        if fileName == './txt/paragraph.txt':
            txt = drawTwoColumnsLayout(txt, postscriptFontName)
        else:
            txt = drawOneColumnsLayout(txt, postscriptFontName)
        drawHeaderFooter(postscriptFontName, fileName)


# --- Instructions ------------------------------------------------------------- #
if __name__ == '__main__':
    # store fonts and txt files in a variable
    allFonts = sortFonts(collectFilesPaths(FONT_FOLDER))
    alltxtFiles = collectFilesPaths(TXT_FOLDER)

    # iterate over all fonts and text files and draw the pages
    for eachFontPath in allFonts:
        for fileName in alltxtFiles:
            postscriptFontName = installFont(eachFontPath)
            proofSet = readStringsFromFile(fileName)
            drawProof(proofSet, postscriptFontName)

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

    projectName = postscriptFontName.split('-')

    saveTo = f'{proofFolder}/{projectName[0]}-proof-{NOW:%Y-%m-%d}.pdf'
    saveImage(saveTo)

    if AUTO_OPEN:
        os.system(f"open -a Preview {saveTo}")

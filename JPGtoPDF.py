import os
import shutil
from fpdf import FPDF
from PIL import Image

inPath = "C:\\input"
outPath = "C:\\output"


def delete_folder(pth) :
    for sub in pth.iterdir() :
        if sub.is_dir() :
            delete_folder(sub)
        else :
            sub.unlink()
    pth.rmdir()


def makePdf(pdfFileName, listPages, dir = ''):
    cover = Image.open(dir + "\\" + str(listPages[1]))
    width, height = cover.size

    # regularPage = Image.open(dir + "\\" + str(listPages[10]))
    # reg_width, reg_height = regularPage.size

    pdf = FPDF(unit="pt", format=[width, height])

    # Pop first and last images out of the list
    # listPages.pop(0)
    # listPages.pop()

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + "\\" + str(page), 0, 0)

    pdf.output(outPath + pdfFileName + ".pdf", "F")

    cover.close()

    # Remove the image directory
    # shutil.rmtree(dir, ignore_errors=True)


for chapterName in os.listdir(inPath):
    makePdf(chapterName, os.listdir(inPath + "\\" + chapterName), inPath + "\\" + chapterName)
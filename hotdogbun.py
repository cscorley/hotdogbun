import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

def split(paperpdf, splitpdf):
    output = PdfFileWriter()

    with open(paperpdf, "rb") as l:
        with open(paperpdf, "rb") as r:
            # I know... I know.
            left = PdfFileReader(l)
            right = PdfFileReader(r)

            pagecount = left.getNumPages()
            print("%s has %s pages to split." % (paperpdf,pagecount))

            for num in range(0, pagecount):
                left_page = left.getPage(num)
                right_page = right.getPage(num)
                midpoint = (
                        left_page.mediaBox.getUpperRight_x() / 2,
                        left_page.mediaBox.getUpperRight_y()
                        )

                left_page.mediaBox.upperRight = midpoint
                output.addPage(left_page)

                right_page.mediaBox.upperLeft = midpoint
                output.addPage(right_page)

            print("Writing %s pages to %s" % (output.getNumPages(), splitpdf))
            with open(splitpdf, "wb") as s:
                output.write(s)

def main(argv):
    # options are for suckers
    pdfs = argv[1:]

    for original in pdfs:
        if original.endswith('.pdf'):
            splitpdf = original[:-4] + '-split.pdf'
        else:
            splitpdf = original + '-split.pdf'

        split(original, splitpdf)

if __name__ == '__main__':
    main(sys.argv)

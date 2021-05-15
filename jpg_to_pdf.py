import os
import sys
import img2pdf
from PIL import Image

img_Folder = "from_img/"+sys.argv[1]+"/"
extension  = ".jpg"
pdf_FileName = "to_pdf/"+sys.argv[1]+".pdf"

with open(pdf_FileName,"wb") as f:
    f.write(img2pdf.convert([Image.open(img_Folder+j).filename for j in os.listdir(img_Folder)if j.endswith(extension)]))
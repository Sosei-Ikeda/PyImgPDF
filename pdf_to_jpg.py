import os
import sys
from pathlib import Path
from pdf2image import convert_from_path

poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

pdf_path = Path("./from_pdf/"+sys.argv[1])
pages = convert_from_path(str(pdf_path))
image_dir = Path("./to_img/"+sys.argv[2])
for i, page in enumerate(pages):
    file_name = pdf_path.stem + "_{:03d}".format(i + 1) + ".jpg"
    image_path = image_dir / file_name
    # JPEGで保存
    page.save(str(image_path), "JPEG")
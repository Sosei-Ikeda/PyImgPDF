*最初に
PyImgPdfがCDの状態でpython -m venv env
env\Scripts\activate
pip install -r requirements.txt

*使うたびに
env\Scripts\activate

*convert_jpg
仮想環境上でpython convert_jpg.py folder1 folder2 width height

*jpg_to_pdf
仮想環境上でpython jpg_to_pdf.py folder (pdf名はfolder)

*pdf_to_jpg
仮想環境上でpython pdf_to_jpg.py file.pdf folder
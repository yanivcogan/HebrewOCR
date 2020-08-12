# pytesseract related imports
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# local files imports
import fileManager
import db

# relative path to the folder into which the source images are placed
img_path = ".\\images\\"
# relative path to the folder into which the output pdf files will be placed
pdf_path = ".\\pdf\\"

# replace this with the absolute path to the tesseract installation
# installation link: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def process_archive():
    # fetches the relative paths to all the files within the folder specified in img_path
    paths = fileManager.get_file_paths_in_directory(img_path)
    # iterate over the paths
    for p in paths:
        # extract text
        text = pytesseract.image_to_string(Image.open(img_path+p), lang='heb')
        # extract recognition data
        data = pytesseract.image_to_data(Image.open(img_path+p), output_type='dict', lang='heb')
        # calculate the average confidence score for the document from the recognition data
        conf = [a for a in data['conf'] if a != '-1']
        avg_conf = sum(conf) / len(conf)
        # the searchable pdf of the document currently being processed will be saved here
        path_to_pdf = pdf_path+fileManager.path_to_pdf(p)
        # this is the path to the source image
        path_to_img = img_path+p
        # the relative path to the file from the source folder. used as a unique identifier.
        name = p
        # generate and store searchable pdf
        pdf = pytesseract.image_to_pdf_or_hocr(img_path+p, extension='pdf', lang='heb')
        fileManager.mkdir_p(path_to_pdf)
        with open(path_to_pdf, 'w+b') as f:
            f.write(pdf)  # pdf type is bytes by default
        # insert/update document information in mysql database
        db.save_docs(name, path_to_img, path_to_pdf, text, avg_conf)
    db.commit()


process_archive()

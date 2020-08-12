try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import fileManager
import db

img_path = ".\images\\"
pdf_path = ".\pdf\\"


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def process_archive():
    paths = fileManager.get_file_paths_in_directory(img_path)
    for p in paths:
        text = pytesseract.image_to_string(Image.open(img_path+p), lang='heb')
        data = pytesseract.image_to_data(Image.open(img_path+p), output_type='dict', lang='heb')
        conf = [a for a in data['conf'] if a != '-1']
        avg_conf = sum(conf) / len(conf)
        path_to_pdf = pdf_path+fileManager.path_to_pdf(p)
        path_to_img = img_path+p
        name = p
        pdf = pytesseract.image_to_pdf_or_hocr(img_path+p, extension='pdf', lang='heb')
        fileManager.mkdir_p(path_to_pdf)
        with open(path_to_pdf, 'w+b') as f:
            f.write(pdf)  # pdf type is bytes by default
        db.save_docs(name, path_to_img, path_to_pdf, text, avg_conf)
    db.commit()


process_archive()


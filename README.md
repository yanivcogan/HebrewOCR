# HebrewOCR
OCR solutions for the Akevot Institute

Required Packages:
pytesseract
mysql-connector

For pytesseract to function properly, first install tesseract:
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe

When installing, make sure to download the Hebrew and Arabic language packs.

After installing tesseract, set pytesseract.pytesseract.tesseract_cmd (in main.py) to the absolute path to the pytesseract.exe (should be somewhere inside the ProgramFiles folder)

Put the documents into the /images folder, and run the program. The searchable pdf files will be output into the /pdf folder.
Note that the program won't work unless you either properly configure or disable the database related features (see below).

The Pytesseract documentation is very useful:
https://pypi.org/project/pytesseract/


Database Installation:
The program allows for the storage of the OCR results in a MySQL database, which can later be used to search documents according to their contents.
If you  wouldn't like to use this functionality, set the suppress_db variable in db.py to 1

If you would like to use it, you would first need to create a new MySQL database.
MySQL Installation:
MySQL can be installed independetly, or alongside PHP and APACHE through WAMP.
For the sake of this tutorial, download the whole WAMP package.
https://www.wampserver.com/en/

After you've completed the installation (just press "next" whenever you are asked) launch WAMP, and navigate in your browser to:
localhost/phpmyadmin
Login using the default credentials (user="root", password=""). Make sure to choose "MySQL" as your server.
Create a new database named "akevot" (or anything else, but make sure to update db.py accordingly). set the collation to utf8_general_ci.
Import the db_structure.sql file (which can be found in this git repository)

You are all set. Happy OCR-ing!

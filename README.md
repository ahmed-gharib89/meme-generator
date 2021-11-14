# Meme Generator

A Web application that dynamicly create images with overlaid quotes.

## Getting Started

The following instructions to help you set a development environment and test the app.

- **Prerequisites**:

  1. Python >= 3.6 to install `python` follow the official instructions [here](https://www.python.org/downloads/).
  2. pdftotext to install `pdftotext` follow the official instructions [here](https://www.xpdfreader.com/download.html).
  3. GIT to install `git` follow the official instructions [here](https://git-scm.com/downloads).

- **Clone the repository**:

  Run `git clone https://github.com/ahmed-gharib89/meme-generator.git` to clone the repository to your local machine.

- **Install dependencies**:

  Run `python -m pip install --upgrade pip && pip install -r requirements.txt` to install all the dependencies.

- **Run the web app**:

  1. cd to src/ directory.
  2. Run `export FLASK_APP=app.py` to set the app to run.
  3. Run `export FLASK_ENV=development` to set the environment to development.
  4. Run `flask run` to run the app.

- **Using the cli**:

  1. cd to src/ directory.
  2. Run `python meme.py --help` to see the available commands.

- **Sample output**

![Screenshot from the webapp](https://i.imgur.com/jUWWacr.png)

### Project Structure

.</br>
├── Makefile: file to run commands from the shell</br>
├── Pipfile: pipenv configuration file</br>
├── Pipfile.lock: dependencies file</br>
├── pyproject.toml: configuration file</br>
├── README.md: this file</br>
└── src: directory for the application</br>
├── app.py: Flask application</br>
├── \_data: directory for data files</br>
│   ├── DogQuotes: directory for sample data files</br>
│   │   ├── DogQuotesCSV.csv</br>
│   │   ├── DogQuotesDOCX.docx</br>
│   │   ├── DogQuotesPDF.pdf</br>
│   │   └── DogQuotesTXT.txt</br>
│   ├── photos: Directory for sample photos</br>
│   │   └── dog</br>
│   │   ├── xander_1.jpg</br>
│   │   ├── xander_2.jpg</br>
│   │   ├── xander_3.jpg</br>
│   │   └── xander_4.jpg</br>
│   └── SimpleLines: directory for sample files</br>
│   ├── SimpleLines.csv</br>
│   ├── SimpleLines.docx</br>
│   ├── SimpleLines.pdf</br>
│   └── SimpleLines.txt</br>
├── fonts: directory for custom fonts</br>
│   ├── LilitaOne-Regular.ttf</br>
│   └── RoadRage-Regular.ttf</br>
├── meme_engine: Meme Engine module</br>
│   ├── \_\_init\_\_.py: initialize the module</br>
│   └── MemeEngine.py: MemeEngine class</br>
├── meme.py: meme generator cli</br>
├── quotes: Quotes Engine Module</br>
│   ├── CSVIngestor.py: CSVIngestor class to ingest csv files</br>
│   ├── DocxIngestor.py: DocxIngestor class to ingest docx files</br>
│   ├── IngestorInterface.py: IngestorInterface abstract class interface for all ingestors</br>
│   ├── Ingestor.py: Strategy object class to interact with different ingestors</br>
│   ├── \_\_init\_\_.py: Initialization file</br>
│   ├── PDFIngestor.py: PDFIngestor class to ingest pdf files</br>
│   ├── quote_model.py: Qoute Model class</br>
│   ├── TextIngestor.py: TextIngestor class to ingest text files</br>
│   └── utility.py: utitlity functions</br>
├── templates: directory to hold html templates for flask app</br>
│   ├── base.html</br>
│   ├── meme_form.html</br>
│   └── meme.html</br>

#### Find me in social media

[![Github](https://img.shields.io/badge/-Github-black?style=flat&labelColor=black&logo=github&logoColor=white "Github")](https://github.com/ahmed-gharib89 "Github")
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white "LinkedIn")](https://www.linkedin.com/in/agharib89/ "LinkedIn")
[![Facebook](https://img.shields.io/badge/-Facebook-informational?style=flat&labelColor=informational&logo=facebook&logoColor=white "Facebook")](https://www.facebook.com/a.gharib89/)
[![Whatsapp](https://img.shields.io/badge/-Whatsapp-brightgreen?style=flat&labelColor=brightgreen&logo=whatsapp&logoColor=whiteg "Whatsapp")](https://wa.me/201096995535?text=Hello)
[![Instagram](https://img.shields.io/badge/-Instagram-c13584?style=flat&labelColor=c13584&logo=instagram&logoColor=white "Instagram")](https://www.instagram.com/ahmed.gharib89/)

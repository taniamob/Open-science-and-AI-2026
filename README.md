[![Documentation Status](https://readthedocs.org/projects/open-science-and-ai-2026/badge/?version=latest)](https://open-science-and-ai-2026.readthedocs.io/en/latest/)
# Open-science-and-AI-2026
# Grobid Text Analysis

## Project Overview

This software enables extracting and analysis of scientific papers using Grobid and Python.

The analysis is performed on 10 open-access research papers from arXiv. 

The program does the following:

* Extracts **abstracts** from each paper
* Generates a **keyword cloud** based on abstract text
* Creates a **visualization of the number of figures per article**
* Extracts **all links found in each paper**

---

# Data

The dataset consists of 10 open-access research papers from arXiv.

The PDF files are stored in:

```
data/papers
```

---


# Environment Setup

The project was developed using **Anaconda**.

Create and activate the environment:

```
conda create -n grobid-project python=3.10
conda activate grobid-project
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Main method of running the project

## Step 1 — Start Grobid

Run the Grobid server using Docker:

```
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0
```

Leave this terminal running.

---

## Step 2 — Run the Scripts

Open a second terminal using anaconda and activate the environment:

```
conda activate grobid-project
```

Run the following script:

```
python code/extract.py
```
This will turn the pdfs into xml files which will be save on data/xml. 

Before running extract_abs.py, make sure that in the outcome file there already exists the file abstracts.txt. 

Then run the following scripts:
```
python code/extract_abs.py
python code/keyword_cloud.py
python code/num_fig.py
python code/links.py
```

Each script performs part of the analysis and saves results to:

```
outcome/
```
# Outcomes

The project gives the following outcomes:

abstract.txt : Extracted abstracts from all papers
keyword_cloud.png : Keyword frequency visualization 
figures_per_article.png : Visualization of number of figures per article
links.txt  : List of links found in the papers


---

# Running the Project with Docker

The project can also be executed using Docker.

##Step 1 - Build the image

```
docker build -t grobid-project .
```

##Step 2 - Run Grobid server

```
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0
```

##Step 3 - Run project container

```
docker run grobid-project
```

The scripts inside the container will execute automatically.


# Testing

The test verifies that all expected outputs were produced.

To run the test do:

```
pytest
```


The tests check that the following files exist:

* abstracts.txt
* keyword_cloud.png
* figures_per_article.png
* links.txt

If the files exist, the tests pass.


# Limitations

Some limitations include:

* Grobid may fail on PDFs with unusual formatting
* Some links may be missed if they are embedded in images

---

# License

MIT License

---

# Author

Tania Mobasser Aslfakouri
Open Science and AI — 2026

## Citation

If you use this project, please cite:

Tania Mobasser Aslfakouri(2026).  Grobid Text Analysis. Zenodo. https://doi.org/XXXX

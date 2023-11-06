
# Eggnog Downloader 

## Project Description
This Python script automates the downloading of files from the [Eggnog](http://eggnog-mapper.embl.de) result page for protein and genomic data. It is designed to be user-friendly and handle common errors.

## Technologies Used
- Python 3
- Beautiful Soup 4
- Requests

## Badges
![Python version](https://img.shields.io/badge/python-3.8-blue.svg)

## Code Explanation and Features
- Modular structure for easy maintenance.
- Input validation for URLs and file paths to prevent common errors.
- Defensive programming practices to handle unexpected situations.

## Prerequisites
- Python 3.6 or higher
- Pip for Python package management

## Installation of Dependencies
```sh
pip install requests beautifulsoup4
```

## How to Use
1. Run the script with Python.
2. Enter the URL of the Eggnog result page when prompted.
3. Provide the destination directory path for downloading the files.
4. Enter a sample identifier that will be prefixed to the names of downloaded files.

## Supported Files

The script is configured to fetch and download the following Eggnog Mapper files:

- emapper.err
- emapper.out
- info.txt
- out.emapper.annotations
- out.emapper.annotations.xlsx
- out.emapper.decorated.gff
- out.emapper.genepred.fasta
- out.emapper.genepred.gff
- out.emapper.hits
- out.emapper.orthologs
- out.emapper.seed_orthologs
- queries.fasta
- queries.raw


## Project Status
The project is currently in the development phase.

## Authors and Acknowledgment
- Main Developer: [Douglas Felipe](https://github.com/DougFelipe)

## Support
If you encounter any problems using the script, please open an `issue` in the GitHub repository where the script is hosted.

## Contribution
Contributions to the script are welcome. Please feel free to `fork` the repository, make your changes and open a `pull request`.

## Changelog
- v1.0.0 - Initial release
- v1.1.0 - Added defensive programming features


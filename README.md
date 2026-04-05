# README.md
# Email Spam Detection and Risk Analysis System

## Team Members
- Richard Leomo - rleomo@stevens.edu - TBD
- Vincent Estridge - vestridg@stevens.edu - TBD

## Project Overview
This project builds a rule-based Email Spam Detection and Risk Analysis System in Python. The program reads a dataset of email messages, processes the text, computes a weighted risk score, and classifies each message as Not Spam, Suspicious, or Spam.

The classification method is rule-based and uses a weighted scoring and threshold approach. The program checks for suspicious words, URLs, repeated punctuation, all-caps words, and sender patterns.

## Classification Method
This project builds a rule-based weighted scoring system instead of machine learning.

Risk Score Formula:

Risk Score =
2 * spam_keyword_count
+ 3 * url_count
+ 1 * exclamation_count
+ 2 * all_caps_word_count
+ 2 * suspicious_sender_flag

Thresholds:
- Score < 5 : Not Spam
- Score 5-9 : Suspicious
- Score >= 10 : Spam

## Libraries / Dependencies
- Python 3.12 / 3.13 / 3.14
- pandas
- numpy
- matplotlib
- pytest
- jupyter

## File Structure
- `main_notebook.ipynb`: main program notebook
- `src/email_message.py`: EmailMessage class
- `src/spam_filter.py`: EmailMessage class
- `src/utils.py`: helper functions
- `src/custom_exceptions.py`: tests for utility functions
- `tests/test_spam_filter.py`: tests for spam scoring logic
- 'data/emails.csv`: dataset file

## How to Run
1. Install dependencies:
   `pip install pandas numpy matplotlib pytest jupyter`

2. Start Jupyter:
   `jupyter notebook`

3. Open `main_notebook.ipynb` and run all cells in order.

## Main Contributions of Each Team Member
- Richard Leomo: proposal, README, folder structure, EmailMessage class, notebook workflow, integration
- Vincent Estridge: SpamFilter support, testing, charts, dataset review

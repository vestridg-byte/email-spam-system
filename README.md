# README.md
# Email Spam Detection and Risk Analysis System

## Team Members
- Richard Leomo - rleomo@stevens.edu - 20044588
- Vincent Estridge - vestridg@stevens.edu - 20045305

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
- `src/spam_filter.py`: SpamFilter class
- `src/utils.py`: helper functions
- `src/custom_exceptions.py`: custom exceptions classes
- `tests/test_utils.py`: tests for utility functions
- `tests/test_spam_filter.py`: tests for spam scoring logic
- `data/emails.csv`: dataset file

## How to Run
1. Install dependencies:
   `pip install pandas numpy matplotlib pytest jupyter`

2. Start Jupyter:
   `jupyter notebook`

3. Open `main_notebook.ipynb` and run all cells in order.

## Main Contributions of Each Team Member
- Richard Leomo:
  - Proposal writing
  - README structure and updates
  - Folder architecture
  - EmailMessage class
  - Main notebook workflow integration
  - Dataset setup and notebook execution

- Vincent Estridge:
  - Initial repository setup 
  - Project folder creation
  - Development log and repository maintenance
  - Test file support and later refactoring contributions
  - Visualization and evaluation metrics


## Model Evaluation

We compute overall classification accuracy by comparing predicted labels to actual labels.

## Exception Handling

This project includes multiple meaningful exception handling scenarios:

1. File Loading Errors  
   - Raises `FileNotFoundError` if the dataset file does not exist.
   - Raises `ValueError` if required dataset columns are missing.

2. Email Validation  
   - Raises `ValueError` if an email message is missing sender, subject, or body content.

These safeguards ensure data integrity and program stability.

## Advanced Python Features Used

The project intentionally incorporates several advanced Python features:

- Generator expressions (used in scoring logic)
- Lambda functions (used in notebook label transformation)
- enumerate() (used during batch prediction)
- Set operations (used for optimized keyword matching)
- Operator overloading (`__len__`, `__eq__`)
- __name__ execution guard

These features demonstrate intermediate-to-advanced Python proficiency.

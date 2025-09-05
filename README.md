# Spam Filter

A simple Naive Bayes–based spam filter for classifying emails as spam or ham (legitimate).

## Features:
- Implements Naive Bayes filtering for email classification.
- Modular design with:
    - utils.py – reading classifications.
    - corpus.py – extracting and processing words from emails.
    - trainingcorpus.py – training data handling.
    - filter.py – main filter logic.
- Supports training on labeled datasets and testing on unseen emails.
- Outputs predictions to !prediction.txt.

## Usage:
1. Prepare a dataset with emails and a !truth.txt file containing labels (SPAM/OK).
2. Train the filter:
```
python filter.py --train path/to/training_data
```
3. Test on new emails:
```
python filter.py --test path/to/test_data
```

## Results:
- Achieved accuracy between 92% – 97% on provided datasets.

## Future Improvements:
- Apply cross-validation for training/testing splits.
- Explore alternative training datasets.
- Experiment with advanced text classification methods (e.g., word2vec).

License
© 2023 Leila Babayeva & Laura Babayeva

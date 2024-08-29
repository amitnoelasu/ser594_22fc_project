# Personality Prediction Using Twitter Data

## Overview

This project investigates the potential for predicting the Big Five personality traits of Twitter users using their tweet data. The study aims to extrapolate insights from the personality scores of celebrities to predict the personality traits of individual Twitter users, evaluating the feasibility and reliability of this approach. 

## Abstract

In response to the growing popularity of social media, researchers have been conducting interdisciplinary studies to explore the connection between personality traits and social media activity. Traditionally, these studies require extensive data collection to establish ground truth, but this project focuses on achieving similar results using existing datasets. Specifically, we analyze the relationships between lexical usage in tweets and Big Five personality scores.

The results indicate that it is challenging to generalize personality predictions from a celebrity dataset to a typical individual Twitter user due to inherent linguistic chaos in tweet content. This research calls into question the feasibility of using existing celebrity data for such predictive modeling.

## Keywords

- Big Five Personality
- Natural Language Processing (NLP)
- Machine Learning
- Twitter Data
- Support Vector Machines
- Linear Regression

## Introduction

With the increasing need to evaluate individual capabilities in the workplace, personality has emerged as a key factor alongside intelligence and energy. This project focuses on predicting personality traits from digital behavior, specifically using Twitter data. 

We chose the Big Five personality model (OCEAN model: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) due to its data-driven development and proven reliability in predicting workplace success. While collecting personality data from Twitter users is challenging and time-consuming, this research attempts to use existing datasets to make predictions without directly collecting data from individuals.

## Objectives

- Identify trends in lexical usage of randomly selected Twitter users.
- Predict Big Five personality traits based on tweet content.
- Evaluate the reliability and validity of using existing celebrity datasets to generalize predictions to ordinary users.
- Analyze model performance and identify potential gaps or limitations.

## Methodology

### Data Collection

- **Dataset**: We utilized a dataset containing Twitter handles and Big Five personality scores of 140 celebrities, partially available on Kaggle.
- **Tweet Retrieval**: Tweets were extracted using the Twitter API and preprocessed using Python's natural language processing libraries.

### Feature Extraction

- **Term Frequency-Inverse Document Frequency (TF-IDF)** was used to extract features from the tweets, representing the significance of words relative to each user.

### Machine Learning Models

- Multiple models were tested, including:
  - **Linear Regression**
  - **Ridge Regression**
  - **Lasso Regression**
  - **Support Vector Machines (SVM) Regression**

Each model was evaluated using Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) to measure prediction accuracy.

## Results

- **Best Performing Model**: Linear Regression showed the lowest error rates.
- **Comparison**: Ridge and Lasso Regression performed comparably to Linear Regression, while SVM Regression had slightly higher error rates.
- Adding real, scraped data to testing significantly worsened performance, suggesting overfitting or dataset reliability issues.

### Evaluation Metrics

| Method              | MAE      | RMSE     |
|---------------------|----------|----------|
| Linear Regression   | 4.385784 | 5.763045 |
| Ridge Regression    | 4.390807 | 5.744391 |
| Lasso Regression    | 4.391514 | 5.711964 |
| SVM Regression      | 4.731647 | 6.077709 |

## Discussion

The results suggest that generalizing personality predictions from celebrity datasets to typical users is not feasible due to differences in tweet language complexity and potential dataset biases. The language used in tweets, characterized by informal grammar and abbreviations, adds complexity to feature extraction and model accuracy.

## Conclusion

This project highlights the challenges in using Twitter data to predict personality traits, especially when relying on existing datasets with potential biases. Future research should focus on collecting data directly from individual users to improve accuracy and reliability. The feasibility of assessing personality from tweet data remains questionable due to inherent limitations in tweet content length and lexical diversity.

## Reproducing the Results

To reproduce the results, run the `wf_core.py` script provided in the project repository.

## Acknowledgments

This project was undertaken as part of the course curriculum for SER 594: Data Science for Software Engineers. Special thanks to Professor Ruben Acuña for guidance and support throughout the project.

## References

1. Tariq, Muhammad Usman, et al. "Human behavior analysis using intelligent big data analytics." Frontiers in Psychology 12 (2021): 686610.
2. Maharani, Warih, and Veronikha Effendy. "Big five personality prediction based in Indonesian tweets using machine learning methods." International Journal of Electrical & Computer Engineering (2088-8708) 12.2 (2022).
3. Goldberg, Lewis R. "An alternative 'description of personality': the big-five factor structure." Journal of Personality and Social Psychology 59.6 (1990): 1216.
4. Golbeck, Jennifer, et al. "Predicting personality from twitter." 2011 IEEE third international conference on privacy, security, risk and trust and 2011 IEEE third international conference on social computing. IEEE, 2011.
5. Karanatsiou, Dimitra, et al. "My tweets bring all the traits to the yard: Predicting personality and relational traits in Online Social Networks." ACM Transactions on the Web (TWEB) 16.2 (2022): 1-26.

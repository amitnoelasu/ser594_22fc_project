# Introduction
This repository contains files for the individual course project in SER594: Data Science for Software Engineers (fall 2022) created by AMIT NOEL THOKALA for partial fulfillment of the course requirements. It was cleared by course staff (R. Acuna, V. Gupta) for public release on 12/13/2022.


1. Introduction
The introduction highlights the importance of assessing personality traits in various contexts, particularly in workplaces, and introduces the concept of using digital behavior data, specifically Twitter data, for personality evaluation. It contrasts the Myers-Briggs Test and the Big-5 personality test, explaining why the latter is chosen for its reliability. The Big-5 model, comprising openness, conscientiousness, extraversion, agreeableness, and neuroticism, is explained in brief.

1.1 Related Work
This section discusses previous research in predicting personalities using digital behavior data, noting that most studies focused on collecting data to establish ground truth. The paper aims to extend this research by utilizing existing datasets of celebrities to predict personalities of average individuals. It also mentions different machine learning models used in previous studies.

2. Exploratory Data Analysis
Here, the dataset is described, which includes Twitter handles and Big-5 scores of celebrities. The process of retrieving tweets via the Twitter API and appending them to the dataset is explained. The distribution of personality scores is analyzed, showing pareto distribution for openness and normal distributions for conscientiousness and extraversion.

3. Methodology
This section details the methodology used for personality prediction. It begins with obtaining Twitter handles from the Kaggle dataset and extracting tweets using the Twitter API. The tweets are then preprocessed using natural language processing techniques. Feature extraction is performed using TF-IDF, and machine learning models such as Linear Regression, Ridge Regression, Lasso Regression, and Support Vector Machines are applied for personality prediction.

4. Results and Discussion
The results of the study are presented, with evaluation metrics like Mean Absolute Error (MAE) and Root-mean-square Error (RMSE) used to assess model performance. Linear Regression emerges as the best-performing model, followed closely by Ridge Regression and Lasso Regression, while Support Vector Machines perform poorly. The discussion delves into potential issues with data reliability and bias, especially when real data points are added to the testing data.

5. Conclusion
The conclusion summarizes the findings of the study, stating that it's not feasible to extrapolate personality data from celebrities to typical users due to complexities in tweet language and potential biases in the dataset. It suggests that using data collected directly from individuals may yield more accurate results in personality prediction.

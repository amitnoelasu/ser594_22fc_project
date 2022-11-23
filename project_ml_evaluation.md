#### SER594: Machine Learning Evaluation
#### Extracting personality traits from user twitter data (title)
#### Amit Noel Thokala (author)
#### 11/21/2022 (date)

## Evaluation Metrics
### Metric 1
**Name:** Mean Absolute Error (MAE)

**Choice Justification:** The project invloves value prediction, so it is a regression problem, and so it is best to evaluate the model based on how close the predicted value is to the actual value. Mean absolute error can be used to determine that error

**Interpretation:** The higher the value, the higher the error. It talks about the distance between the predicted values and the actual values.

### Metric 2
**Name:** Root Mean Square Error (RMSE)

**Choice Justification:** The project involves value prediction, so it is a regression problem, and so it is best to evaluate the model based on how close the predicted value is to the actual value. RMSE can be used not only to calculate the correctness of the model but it also to represent the performance of the model against outliers.


## Alternative Models
### Alternative 1: Ridge reggression
**Construction:** The model is a modification on Linear Regression. It diminishes features that are highly correlated

**Evaluation:** The model performed very well on the testing data. However, it was slightly worse than the main model. It had similar error to that of the main model in both the metrics.
### Alternative 2: Lasso Regression
**Construction:** The model is a modification on Linear Regression. It eliminates features that are highly correlated and helps with feature set reduction

**Evaluation:** The model performed very well on the testing data. However, it was slightly worse than the main model. It had similar error to that of the main model in both the metrics.
### Alternative 3: SVM Regression
**Construction:** SVM is an entirely different model to linear regression. This was mainly used to verify the results achieved using linear regression against a different model

**Evaluation:** The model performed decently on the test data. However, it was worse than all the linear regression models. Nevertheless, it had single-digit error in both the metrics.


## Best Model

**Model:** The best performing model among alternative models was the Ridge regression model
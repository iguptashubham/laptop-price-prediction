# Laptop Price Prediction [ ML ]
----
### Summary

A machine learning model was developed using the Stacking Regressor technique, which combines multiple individual models to improve predictive performance. This particular stacked model is composed of three distinct algorithms: Random Forest Classifier, Gradient Boosting Regression, and XGBoost Regressor. Each of these algorithms brings its unique strengths to the ensemble, enhancing the model’s ability to generalize from the training data. The Random Forest Classifier contributes its robustness against overfitting, the Gradient Boosting Regression adds its capability of optimizing on differentiable loss functions, and the XGBoost Regressor provides its efficiency and flexibility in modeling complex patterns. Together, these algorithms form a powerful stacked model that can deliver superior predictions on diverse datasets. The creation of this model signifies an advanced application of machine learning techniques to harness the collective power of multiple algorithms. It represents a significant step forward in predictive modeling, offering a robust and versatile tool for data analysis and prediction.

---
### Pipeline of Machine Learning Model
The machine learning model was built using a pipeline that consists of two main steps. The first step is a ColumnTransformer with OneHotEncoder, which handles categorical variables by transforming them into a binary vector representation. The second step is a StackingRegressor that combines the predictions of several base estimators (Random Forest, Gradient Boosting, and XGBoost) to improve the predictive accuracy. The final estimator, Ridge Regression, is used to aggregate the predictions of the base estimators. This pipeline ensures a streamlined workflow from preprocessing to prediction, enhancing the model’s performance and efficiency.

![Screenshot 2024-06-14 111323](https://github.com/iguptashubham/laptop-price-prediction/assets/140319219/57e9c961-2487-4537-b5f1-b8d3fb0e5f76)

### Streamlit Web app

The Streamlit web app serves as an interactive interface for the stacked regression model. Users can input the features of their choice, and the app will use the model to predict the outcome. The app also displays the pipeline diagram of the model for users to understand the underlying process. This user-friendly application makes complex machine learning predictions accessible and easy to understand, bridging the gap between advanced analytics and end-users

![Screenshot 2024-06-14 111222](https://github.com/iguptashubham/laptop-price-prediction/assets/140319219/e74b518c-26f1-4385-8308-c98ba056c0c5)

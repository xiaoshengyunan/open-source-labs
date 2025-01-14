# Introduction

This lab demonstrates how to use quantile regression to create prediction intervals using scikit-learn. We will generate synthetic data for a regression problem, apply the function to it, and create observations of the target using a lognormal distribution. We will then split the data into training and test datasets, fit non-linear quantile and least squares regressors, and create an evenly spaced evaluation set of input values spanning the [0, 10] range. We will compare the predicted median with the predicted mean, analyze the error metrics, and calibrate the confidence interval. Finally, we will tune the hyper-parameters of the quantile regressors.

> You can open the `plot-gradient-boosting-quantile.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> Labby cannot automatically verify the answers because it cannot access the notebook.

# Introduction

This is code for fitting a decision tree ML model from Sci-kit learn and predicting the classes of future text.
inspired by [article](https://medium.com/@rnbrown/creating-and-visualizing-decision-trees-with-python-f8e8fa394176)

The points of this notebook is to show what's going on under the hood of Sci-kit's model, especially how it weighs the inputs on the model.
The Jupyter notebook will output the following image
![Decision Tree!](DecisionTree.png "Decision Tree")

## Dataset

The dataset is a an email dataset with label 1 (spam) and 0 (not spam). Raw file is emails.csv
Link to [dataset](https://www.kaggle.com/karthickveerakumar/spam-filter/version/1)
The proccessed emails are stemmed, tokenized, have some junk text removed, and all numbers are replaced with the string "NUMBER". As well as some other small things.

## Compatibility

Code updated to work with sklearn 0.22, but will break with 0.23.

Required packages are

- pydotplus
- GraphViz

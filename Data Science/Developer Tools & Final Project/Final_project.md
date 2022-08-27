# Final Week Project
This week's instructions are in a Markdown file, not an `ipynb` file; I am very keen on you having at least one properly formatted data science notebook that is all yours - if I create the notebook on Colab it will still have me as the author, so this week I want you to create it!

Additionally this week, I want you to explain what you're doing in text boxes alongside the code. If you're unsure how to do this,  click the `+ Text` cell in the top left of the Colab page, or hovering at the top of a cell when you select it. Data science/analysis is as much about communication of results as the results themselves, so please don't underestimate this bit!

I also *highly* encourage you to find some data relevant to your interests for this project. It will make it more fun and applicable for you, and is much more impressive than working on a "generic ML dataset" like the one we'll use by default. Finding datasets is it's own skill - [Google Datasets](https://datasetsearch.research.google.com/) can help somewhat but really this is where your domain knowledge should come in!

For any dataset - I would like the following structure of work - these questions are written with the "general" dataset in mind, but will be applicable to any dataset.

## Importing and Parsing Data
* Upload the data to Colab and import it into Python
* Ensure that the data has imported correctly by using the `pandas` `.head()` method.
* Look for N/A, missing or invalid items. Using the `.fillna()` method, come up with a strategy for dealing with these items. Do we need to remove them for analysis or can we set them to a sensible value?

## Data Exploration
* Using `pandas`, get an idea about the "shape" of your data. What are the types you are working with? What are the maximum, minimum and average values?
* Using `matplotlib`, come up with some questions about your data. For example, for a classification task, how do your categorical variables impact the end classification (bar plot)? What about continuous variables (histogram plots)?
* Try to find if there are any relationships *between* your features (not the labels) - for example in the general dataset, are private employees more likely to have capital gains? This can be useful when intepreting your data later!
* Identify questions to take forward for a machine learning model - what are we trying to find out or predict? In the general dataset, we are building a classifier to predict the income of someone based on their attributes - but you may be clustering countries based on GDP and life expectancy. This question should be informed by your visualisations and general exploration!

## Model Building
* Think about what models you can use for your data. Is it an unsupervised (unlabelled) or supervised (labelled) dataset? What kind of problem are you trying to solve (classification, regression, clustering)?
* Preprocess your data for your model. Perform a train/test split and scale your data in an intelligent manner. Ensure your data is in the right format for the model you're using - are the string entires encoded into numerical ones?
* Train your model using the training set of the data. Save any metrics you have during training.

## Model Evaluation
* Predict your testing dataset using your model, and compare the output to the testing labels using a suitable metric.
* Compare the model above with at least 5 other models - these can be other types of models (e.g. K nearest neighbours vs SVM model), or the same models with different hyperparameters (e.g. K means clustering with `k = 5` and `k = 10`. For each model (including the first), repeat this process at least 10 times to validate your results. You should end up with at least 5 lists (one for each model) of metrics.
* Taking the mean and standard deviation of these models, graph them on a bar chart using `matplotlib` with appropriate x and y labels.

## Discussion
Write about the following:
* Which was the best model out of those you tested? Can you think of what that might be?
* Was your metric well-chosen?
* Were there any ethical concerns with how the dataset might have been collected or used, or how your model might be used maliciously? Was there any bias in the dataset or your model (for example, are people with high incomes more likely to respond to a study about income levels)?
* Conclude your findings - what have you achieved in this project? What haven't you been able to do? What were the pros/cons and drawbacks/successes of your model?

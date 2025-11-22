# Hello and welcome to my final project. 

This is my final project for my dan IT Python course. I used the [Extended Iris dataset](https://www.kaggle.com/datasets/samybaladram/iris-dataset-extended) from Kaggle in this machine learning project. 

From the description of the dataset: 
> The dataset consists of 1200 rows and 21 columns that include both original attributes like 'Species', 'Sepal Length', 'Sepal Width', 'Petal Length', and 'Petal Width', as well as newly added environmental and morphological attributes such as 'Elevation', 'Soil Type', and 'Petal Curvature'.

I chose this dataset due to my familiarity with it, plus the new categorical column allowed me to practice categorical variables as well. 
It has 1200 different irises, which is more than the original dataset and allows for more extensive training and more accurate predictions. 

You may find two folders here: 
1) iris_ml, which contains parts 1-3 of the project (machine learning and graphs)
2) iris_prediction, which contains the Django website. 

To deploy the Django website locally, do the following: 
1) activate the environment and install the requirements
> python -m venv venv
> venv/Script/activate 
> pip install -r requirements

2) migrate the models
> cd .\iris_prediction\
> python .\manage.py makemigrations
> python .\manage.py migrate

3) run
> python .\manage.py runserver

## About iris_ml
iris_ml contains several files, out of which the significant ones are: 
1) Rohal_tasks_1-2.ipynb, which is a Jupyter notebook containing parts 1 (Аналіз та підготовка даних) and 2 (Розробка моделі машинного навчання) of my homework. 
2) Rohal_task_3.ipynb, which is a Jupyter notebook containing part 3 (Візуалізація даних) of my homework. 
3) iris_extended.csv which is the dataset I worked with. 
4) edited_extended_iris_df.csv which is the dataset I used for part 3 of my homework, identical to the one I did the machine learning on. 
5) iris_extended_model.joblib, which is the machine learning model I exported using joblib (and iris_joblib_test.ipynb is the notebook in which I tested the functionality of the joblib file). 

Everything in tasks 1-2 and 3 has been documented in its respective jupyter notebooks. 


## About iris_prediction
iris_prediction contains the django website for my project, which is also part 4 (Розробка веб-сторінки у Django) and 5 (Тестування та валідація) of my homework. 

It has an app called dashboard, the main part called iris_prediction, and folders ml_model, which contains the joblib file with the model, and templates, which contains the templates used.

There is no CSS, since I used bootstrap and inline formatting. I also used crispy forms, which allowed me to format the input form for my prediction website. 

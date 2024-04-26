Content-based Recipe Recommendation System

Taazkir Nasir and Tamara Estrada


### Our Goal
	
The goal of this project is to create a personalized recipe recommendation system that suggests personalized meal plans based on users’ dietary preferences. In today’s online world, there are many diet resources online, which often leaves users to be confused as they sift through numerous amounts of information to find recipes that align with their dietary restrictions, preferences, and ingredient availability. The purpose of this project is to make this process more efficient by using machine learning techniques to offer the user personalized recipe suggestions. Through this program, the users can input their preferred ingredients and tags, which will allow the algorithm to inspect their input and compare them with a database of recipes. We implemented techniques like TF-IDF vectorization and cosine similarity, with this the program can efficiently determine and recommend recipes that match the user’s input as closely as possible. After the algorithm determines the recommended recipes, the output will also include detailed recipe information, including ingredients, descriptions, and directions. 

### Significance of the Project

This project is meaningful because it addresses the dietary needs of individuals. As health diseases and concerns rise, the need for a health-conscious lifestyle does as well. There always seems to be a big demand for the latest diet so this recipe recommendation system will provide a valuable tool for people looking to embark on their healthier eating journey or habits.  Our recipe recommendation system is helpful to all people because it helps individuals with cultural, ethical, or personal preferences attain tailored recommendations.  

### Installation and Usage Instructions

To use and run this recipe recommendation system, all you do is clone the GitHub repository and open the code on Google Colab. This dataset is too big to be included in the repository, users will need to download it from Kaggle and upload it to their Colab environment. Users should make sure that the file path in the code correctly represents the location where the dataset is in Colab. Once the dataset is successfully loaded into their environment, the user can run the code in the cells to load the data, extract the features, input their dietary preferences, generate recommendations, and view recipe details.

### Discussing Dataset

The original dataset contains many features that give essential context to each recipe entry. It contains the name, duration, nutrition details, cooking steps, description, ingredients list, and the number of ingredients required. ‘name’ is the name of the recipe, and each entry is unique. 

Columns provided by the original dataset:
-	‘minutes’ represents the duration of making the recipe.
-	‘nutrition’ format is a list of values. Its breakdown is as follows, Daily Value (%DV) for key nutritional 	components such as calories, total fat, and sugar. 
-	‘steps’ are detailed instructions for the preparation of the recipe.
-	‘description’ is additional recommendations, written by the author of each recipe.
-	‘ingredients’ is a list of ingredients that are needed to prepare the recipe.
-	‘n_ingredients’ is the total number of ingredients that are needed to prepare the recipe.


### Code Structure

<img width="666" alt="Screenshot 2024-04-26 at 3 22 59 PM" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/6f2424a1-39cf-47ce-a5f0-42b6cafeddc7">

### List of Functionalities and Test Results
1.	Data Loading:
a.	load_data(): function successfully loads the dataset from a CSV file found from Kaggle.
<img width="442" alt="image" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/f9a9199c-dd6b-472c-9bf2-5e5f06816ffc">
b.	It handles any cases where the file is not found in the project structure or any other error and deals with those errors accordingly.

2.	Data Preprocessing:
a.	Cleaning and formatting datasets to ensure consistency.
b.	It is tested with various data inconsistencies like missing values, mixed data types, and formalities in preprocessing or formatting.
<img width="508" alt="image" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/35912e4d-aec5-47ee-b985-a118062004c8">

3.	Feature Extraction:
a.	Will extract needed attributes from the dataset and vectorize them using TF-IDF. Extracts features like (tags, descriptions, ingredients).
b.	It is tested with different textual data to make sure that the feature extraction and vectorization were performed accurately.
c.	Also makes sure that the TF-IDF vectorizer ensures robustness and captures the vocabulary and weights.
<img width="499" alt="image" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/67e157ab-edac-4165-b64a-4beb89e6f934">

4.	User Input Collection:
a.	CLI prompts the user to input their preferred ingredients and tags.
b.	Is tested with numerous user inputs, making sure to use a wide range of combinations of ingredients and tags.
c.	Checked that the input was retrieved successfully and correctly processed for further processing.

<img width="453" alt="image" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/50559072-fc81-46b9-8808-9f5a042b9bdd">

5.	Recommendation Generation:
a.	Calculates the cosine similarity between the user input vector and the recipe features matrix to differentiate and identify recipes.
b.	Selects the top N recipes that are most in common based on the input provided. Is manually tested with different user parameters. 
<img width="468" alt="image" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/7be08df2-cb37-463a-b592-302e53f49dfb">

6.	Recipe Display:
a.	The user is prompted to pick from the list of recommended recipes to access more detailed information about a specific recipe.
b.	The name, ingredients, description, and directions will be displayed.
<img width="469" alt="image" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/ccc65d3c-7494-40d8-a4fb-9c017251bd18">

### Results

<img width="519" alt="image" src="https://github.com/TamaraEstrada/cmpsc_445_final/assets/105894181/952d2dac-eacb-4951-b0ef-1539f96eba9f">


### Discussion and Conclusions
Through the output, users can see that the dataset was successfully loaded. Then the user will be prompted to input their preferred ingredients, in this case, “chicken” and “potatoes” are typed and a tag “healthy”. These ingredients will be used to create a personalized recipe search. The recommendations are then outputted based on the user’s preferences, the system will generate a list of recipes best aligned with the user’s specified ingredients and tags. The top recommendations for this search included dishes like "Healthy Chicken and Potato" and "Scalloped Chicken and Potatoes”. The user then selects a from the list of recommended recipes for further detailed information. 
We encountered many limitations and issues while building this project. One of the main challenges was the dataset availability. While this recommendation system recommends recipes that align closely to the input parameters, the scope, and accuracy could be improved even more if there were a larger and more diverse dataset. The algorithms currently implemented are effective and complete their purpose, but they can be further improved by implementing more advanced machine learning techniques so that the recommendation and accuracy could improve. 
Three main course learnings were applied in this project. The first is data preprocessing, where the data is cleansed and formatted. Performing this step ensures that the data is clear and consistent for analysis. Secondly, feature extraction was another technique used to separate and discern meaningful features from the dataset’s columns. Lastly, this project implemented algorithms for recommendation generation like cosine similarity, TF-IDF vectorization, and dimensionality reduction. 

### Dataset Used

https://www.kaggle.com/datasets/hugodarwood/epirecipes/code








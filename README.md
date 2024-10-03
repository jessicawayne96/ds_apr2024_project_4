# Superhero Battle Prediction: Machine Learning Model

This project explores the intersection of data science and pop culture by using machine learning to predict the outcomes of superhero battles against an average opponent. Our model analyzes various superhero attributes—such as strength, speed, intelligence, weaknesses, and special abilities to predict the likely winner.

## Data Cleaning
We started with three datasets: one containing randomized superhero statistics, one with basic hero information, and one detailing superhero powers. We began by checking for missing values and found that the "Universe" column was randomized and inaccurate. We created a new column with the correct universe values.

We then inspected the superhero information dataset and found that while no null values were initially present, several columns contained hyphens that represented missing data. Specifically, columns like eye color, hair color, race, and skin color had this issue. We replaced the hyphens with NaN values and eventually dropped these columns, as dropping the rows would have led to losing 90% of the dataset. Some negative values were found in the height and weight columns, which were not feasible. We replaced these negative values with the median to retain data while correcting the issue.

We grouped the superhero powers into more general categories such as physical attributes, energy-related abilities, elemental powers, and cosmic/magic powers. This reduced the dataset's dimensionality, making it more manageable. After cleaning, we merged the superhero information and powers datasets on hero names. This made the data more intuitive and easier to use for visualization in Tableau.

## Machine Learning

We started by importing necessary libraries (e.g., pandas, scikit-learn, and pickle). We dropped the "Universe" column, as it didn’t add much predictive value. We one-hot encoded categorical columns like special abilities, character traits, and weaknesses. For numerical data (speed, strength, intelligence), we applied a StandardScaler. Initially, we aimed to use a preprocessing pipeline but encountered roadblocks, so we opted to preprocess the data manually.

We then trained our models using the "battle outcome" as the target variable. We ran various machine learning models including Random Forest, Logistic Regression, Support Vector Classifier (SVC), Decision Tree, Extra Trees, AdaBoost, and Gradient Boost. After comparing their performance, we chose Logistic Regression as the best fit for our dataset due to its consistency and interpretability.

After selecting Logistic Regression, we retrained the model using the full dataset and saved it using pickle. Unfortunately, we encountered issues with the pickle file being much smaller than expected, which raised concerns about its functionality.

## Dashboard Design Concepts
We created two Tableau dashboards to visualize superhero statistics and battle outcomes, offering an interactive platform for users to explore different hero comparisons and predictions.

Our first dashboard explores the battle dataset, which contains randomized qualities such as strength, speed, and intelligence assigned to various superheroes. This dataset was crucial for training our machine learning model to predict the outcome of superhero battles. The dashboard visualizes the distribution of these randomized attributes, providing insights into which qualities were most influential in determining the winner. Users can explore how key traits like intelligence, strength, and speed were assigned across superheroes, offering a deeper understanding of the factors that contributed to the model’s predictions.

The second dashboard focuses on the superhero dataset, which contains real-world data on over 600 superheroes. This dashboard allows users to investigate various characteristics of superheroes, such as height, weight, alignment (good, evil, or neutral), and publisher. It also highlights the number and types of powers that each superhero possesses. The dashboard features filters for gender and alignment, allowing users to narrow down and compare specific groups of superheroes. The visualizations provide a clear view of how different traits and powers are distributed, giving a comprehensive look at the diversity and attributes of superheroes.

## Testing and Deployment
We tested the model locally to ensure it worked, and we defined a make_predictions function for making predictions. However, during the web app deployment, we encountered issues loading the pickle files, which prevented real-time predictions. We are still debugging this problem.

## Bias and Limitations
The model assumes an "average opponent" whose attributes are unknown, which may lead to biased predictions. Additionally, the dataset is limited in scope with only eight characters and a small set of special abilities and weaknesses. This restricts the model's ability to generalize to more complex battles.

The most significant technical limitation we faced was the inability to load the model in our web app. Furthermore, manual preprocessing added complexity to the process, which could have been streamlined with a preprocessing pipeline. A more comprehensive dataset would improve the model’s performance and generalizability.

## Conclusion
This project highlights the potential for using machine learning to predict superhero battle outcomes. While our model provides a good starting point, there is room for improvement in terms of dataset diversity, model performance, and deployment. Future iterations could address these limitations to create a more robust and scalable solution.

Please Feel free to download the data and run it on your local server.

Or you can access the web app here: until January 2025
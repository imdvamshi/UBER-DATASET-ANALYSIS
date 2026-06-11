# RIDESHARE.DB DATASET INSIGHTS REPORT
## PROJECT OVERVIEW

This project presents an exploratory data analysis (EDA) of  Uber ride-sharing dataset containing information about users, drivers, riders, trips, locations, payments, reviews, and cancellations.

The primary objective of this analysis is to understand user behavior, driver activity, trip patterns, customer satisfaction, payment preferences, and cancellation trends. The project involves data loading, data understanding, data cleaning, exploratory data analysis, and visualization to uncover meaningful business insights.

Multiple tables were analyzed and combined where necessary to evaluate platform performance from both operational and customer perspectives. The findings from this analysis provide valuable insights that can help improve service quality, optimize operations, and support data-driven business decisions.

**Tools & Technologies Used:**

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* SQLite

## KEY FINDINGS

### INSIGHT 1 : City with Highest Number of Users
Analysis shows that city - **Houston** has highest number of users i.e 552 users. While city - **Los Angeles** is the second highest in the context of active users.

### INSIGHT 2 : Driver Distribution Among Users
Out of 2000 total users, **400** are registered as drivers, accounting for 20% of the user base. This highlights the proportion of users contributing to the platform's service operations as drivers.

### INSIGHT 3 : City with the Highest Number of Drivers
**Houston** has the highest number of registered drivers in the dataset. This indicates that the city has the largest driver supply, helping meet ride demand more effectively than other cities.

### INSIGHT 4 : Vehicle mostly used by Drivers
**Nissan** is the most frequently used vehicle brand among drivers, appearing 50 times in the dataset. This suggests that Nissan vehicles are a popular choice among drivers on the platform.
Among vehicle models, **Equinox** is the most commonly used model, appearing 17 times in the dataset. This indicates a preference for this model among drivers and highlights its prominence within the platform's vehicle fleet.

### INSIGHT 5 : Vehicle brand with highest rating 
As per the analysis, **Ford** has the highest rating with an average of 4.302381 rating. This suggests that drivers using Ford vehicle brand tend to receive better customer feedback, potentially due to factors such as comfort, reliability, or overall ride experience.

### INSIGHT 6 : Vehicle model with highest rating
**F-150** achieved the highest average rating among all vehicle models in the dataset. This indicates that rides provided using F-150 vehicles are generally associated with higher customer satisfaction and positive rider experiences.

### INSIGHT 7 :  City with highest driver ratings
Among all cities, **New York** recorded the highest average driver rating. This suggests that drivers in this city consistently provide a better customer experience, leading to higher rider satisfaction and positive feedback.

### INSIGHT 8 : Active Driver Analysis
Out of all registered drivers, **351** out of 400 are currently active. This indicates the number of drivers actively contributing to platform operations and fulfilling ride demand.

### INSIGHT 9 : City with the Highest Rider Ratings
**New York** achieved the highest average rider rating of 4.00 among all cities in the dataset. This indicates that riders in New York tend to receive the most positive feedback, reflecting a high level of satisfaction and engagement on the platform.
Additionally, the average ratings across all cities are relatively close, suggesting a consistent rider experience throughout the platform.

### INSIGHT 10 : City with the Highest Number of Riders
**Houston** has the highest number of riders in the dataset. This indicates a strong user base and higher platform adoption in the city, making it a key market for customer engagement and business growth.

### INSIGHT 11 : Zone Type with the Highest Number of Locations
**Residential** has the highest number of locations in the dataset. This indicates that a significant portion of the service area is concentrated within this zone category, highlighting its importance in the overall location network.

### INSIGHT 12 : Location Distribution Across Cities
Each city in the dataset contains **10** locations, indicating an equal distribution of locations across **New York, Chicago, Los Angeles, and Houston**. This suggests that the dataset was designed with balanced geographical coverage, allowing for unbiased comparisons between cities.

### INSIGHT 13 : Trip Status Distribution
The dataset contains **16,827 completed trips**, representing 100% of all recorded trips. This indicates that the dataset consists exclusively of successfully completed ride transactions.

### INSIGHT 14 : Average Trip Distance and Duration
The average trip distance is **18.01** km, while the average trip duration is **31** minutes. This indicates that most rides are relatively short and can be completed within a moderate travel time, reflecting typical urban transportation patterns.

### INSIGHT 15 : Most Preferred Payment Method
**Card** payments are the most preferred payment method, indicating a strong user preference for cashless transactions. This indicates that users prefer digital and card-based transactions for ride payments, highlighting the importance of maintaining a seamless electronic payment experience.

### INSIGHT 16 : Average Customer Rating
The average rating across all reviews is **3.67/5**. This indicates that users generally have a positive experience with the platform, with most ratings concentrated between 3 and 4 stars. The relatively small number of low ratings suggests that negative experiences are less common.

### INSIGHT 17 : Reviews with Comments
A total of **9,216** reviews contain written comments. This indicates that a significant number of users chose to provide detailed feedback in addition to ratings, offering valuable qualitative insights into customer experiences and service quality.

### INSIGHT 18 : Trip Cancellation Analysis
**Riders are responsible for the majority of trip cancellations**, accounting for 2,069 cancellations compared to 897 cancellations by drivers. This indicates that riders cancel trips more than twice as often as drivers, suggesting that factors such as changes in travel plans, long wait times, or booking errors may have a significant impact on cancellation rates.

### INSIGHT 19 : Top Cancellation Reasons
**Personal emergency** is the most common reason for trip cancellations, with 396 occurrences. Other frequent reasons include long wait times (284) and riders changing their minds (283). These findings suggest that while some cancellations are unavoidable, reducing wait times may help lower overall cancellation rates and improve customer satisfaction.
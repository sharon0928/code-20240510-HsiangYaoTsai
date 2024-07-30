## Data Cleansing and Validation of "Winner_Price" for Machine Learning Pipeline

### Task Description:
#### I cleaned and validated the "winner_price" data, which serves as the target variable in a machine learning pipeline. The data had to be free from anomalies and invalid prices to ensure the accuracy and reliability of the model.

### Objective:
#### The primary goal was to ensure the integrity of the "winner_price" data, which represents the lowest price that wins a contract and is awarded contract fulfillment. This process involved both automated and manual approaches to identify and rectify any data issues. 

### Key automated steps include:
##### 1.	Data Type Configuration: Automatically defining data types for each column to ensure uniformity and prevent errors.
##### 2.	Filtering Information: Setting up automated filters to exclude irrelevant data and focus on pertinent information.
##### 3.	Column Management: Automating the deletion of unnecessary columns to streamline the dataset.
##### 4.	Outlier Detection: Implementing automated restrictions and rules to identify and handle outliers.
##### 5.	Data Transformation: Converting categorical variables into dummy variables for analytical purposes through automated processes.
## Manual Tasks
### Despite automation, certain tasks require manual intervention to ensure data integrity:
##### 1.	Exception Handling: Identifying and rectifying anomalies or nonsensical data entries that automation might miss.
##### 2.	Initial Data Review: Manually inspecting the dataset upon receipt to catch and correct human errors. For example:
###### •	In the *“contract_type”* column, correcting entries like “wide area” to the appropriate type.
###### •	In the *“second_place_outcome”* column, ensuring that entries reflect the correct status (e.g., changing incorrect 'win' entries to 'lost').
##### 3.	Frequent Error Correction: Regularly checking and correcting common errors, such as those in the date columns.


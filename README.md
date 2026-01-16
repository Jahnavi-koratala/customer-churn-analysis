# Customer Churn Analysis & EDA

**Author:** Jahnavi Koratala

---

## Project Overview

Welcome to my project on Customer Churn. I created this to look into a telecom company's data and understand why customers are cancelling their service. "Churn" basically means customers leaving, and I wanted to find the reasons behind it so the company can solve these issues.

I used **Python** to work with the data, clean it up, and make charts to show the results clearly.

---

## Tools Used

*   **Python**: The main programming language I used.
*   **Pandas & NumPy**: I used these to load and organize the data.
*   **Matplotlib & Seaborn**: These helped me create graphs to visualize the trends.

---

## Project Structure

Here is a list of the files in this project:

*   **`customer_data.csv`**: The data file with all the customer information.
*   **`run_analysis.py`**: The entry point that runs the entire analysis.
*   **`data_analysis.py`**: Handles data loading and statistical analysis.
*   **`visualizations.py`**: Contains all the code for generating the charts.
*   **`logging_setup.py`**: Sets up the logging system for the project.

---

## Key Findings

After looking at the data, here are the main things I found:

### 1. Senior Citizens
Older customers are leaving the service more often than younger ones. This suggests they might need better support or plans that are easier to use.

### 2. Fiber Optic Internet
This was interesting. Customers with Fiber Optic internet (which is usually faster and more expensive) are leaving more than others. It is possible the price is too high or the service quality isn't good enough.

### 3. Contracts
It is clear that customers with **Month-to-Month** contracts leave the most. People who sign 1-year or 2-year contracts stay much longer.

### 4. Payment Methods
There is a pattern with payments: customers who pay by **Electronic Check** leave more often compared to those using other methods.

### 5. New Customers
Most customers who leave do so in the first few months. The data shows that if a customer stays for at least a year, they are very likely to keep the service for a long time.
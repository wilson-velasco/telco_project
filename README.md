# Project Description

The aim of this project is to look at what drives customer churn for a fictional company, Telco.

The main goals are:
  * Determine at least two factors that contribute to customer churn.
  * Predict with 80% accuracy whether a given customer will churn.
  * Provide stakeholders with recommendations as to how to reduce customer churn.

Hypothesis:

  monthly_charges and tenure are the most determining factors of whether a customer will churn.   

## Data Dictionary

Column Name | Description | 
--- | --- |
customer_id | Unique identification number of customer |
gender | Customer gender (here, Male or Female) |
senior_citizen | Whether a customer is senior (0 = No, 1 = Yes) |
partner | Whether a customer has a partner |
dependents | Whether a customer has dependents (i.e. children) |
tenure | Length of time (in months) that customer has been with the company |
phone_service | Whether customer has phone service with Telco (Yes or No) |
multiple_lines | Whether customer has multiple lines (Yes, No, or No Phone Service, which indicates customer only has internet service) |
online_security | Whether a customer has online security (Yes, No, or No Internet Service, which indicates customerly only has phone service) | 
online_backup | Whether a customer has online backup (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
device_protection | Whether a customer has device protection (Yes, No, or No Internet Service, which indicates customerly only has phone service) | 
tech_support | Whether a customer has tech support (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
streaming_tv | Whether a customer has streaming TV (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
streaming_movies | Whether a customer has streaming movies (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
paperless_billing | Whether a customer has paperless billing (Yes or No) |
monthly_charges | Amount of monthly charges to customer, in dollars |
total_charges | Cumulative amount of charges to customer over course of their tenure, in dollars |
churn | Whether customer has churned (Yes or No) |
contract_type | Type of contract (Month-to-month, Two year, or One year) |
internet_service_type | Type of internet service (Fiber optic, DSL, None) |
payment_type | Type of payment method used (Electronic check, Mailed check, Bank transfer, Credit card) |

# Project Planning

  * Acquire all relevant data from telco_churn database.
  * Prepare data for handling. Check/handle nulls if applicable.
  * Isolate four variables that might affect customer churn. 
  * Explore each variable for distribution, counts, ranges, etc. Run stats tests to determine dependence for each variable.
  * Run through different classification models to determine best fit.
  * Determine accuracy of best fit model and use said model to provide predictions on the test dataset.
  * Provide stakeholders with recommendations on reducing churn.

# Key Findings, Takeaways, and Recommendations

  * TBD

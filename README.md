# Project Description

The aim of this project is to look at what drives customer churn for a fictional company, Telco.

The main goals are:
  * Determine at least two factors that contribute to customer churn.
  * Predict with at least 80% accuracy whether a given customer will churn.
  * Provide stakeholders with recommendations as to how to reduce customer churn.

Hypothesis:

  monthly_charges and tenure are the most determining factors of whether a customer will churn.   

## Data Dictionary

Column Name | Description | Key |
--- | --- | --- |
customer_id | Unique identification number of customer |   |
gender | Customer gender | Male, Female | 
senior_citizen | Whether a customer is senior | (0 = No, 1 = Yes) |
partner | Whether a customer has a partner | (0 = No, 1 = Yes) |
dependents | Whether a customer has dependents (i.e. children) | (0 = No, 1 = Yes) |
tenure | Length of time (in months) that customer has been with the company | |
phone_service | Whether customer has phone service with Telco | (0 = No, 1 = Yes) |
multiple_lines | Whether customer has multiple lines | (Yes, No, or No Phone Service, which indicates customer only has internet service) |
online_security | Whether a customer has online security | (Yes, No, or No Internet Service, which indicates customerly only has phone service) | 
online_backup | Whether a customer has online backup | (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
device_protection | Whether a customer has device protection | (Yes, No, or No Internet Service, which indicates customerly only has phone service) | 
tech_support | Whether a customer has tech support | (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
streaming_tv | Whether a customer has streaming TV | (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
streaming_movies | Whether a customer has streaming movies | (Yes, No, or No Internet Service, which indicates customerly only has phone service) |
paperless_billing | Whether a customer has paperless billing | (0 = No, 1 = Yes) |
monthly_charges | Amount of monthly charges to customer, in dollars | |
total_charges | Cumulative amount of charges to customer over course of their tenure, in dollars | |
churn | Whether customer has churned | (0 = No, 1 = Yes) |
contract_type | Type of contract | (Month-to-month, Two year, or One year) |
internet_service_type | Type of internet service | (Fiber optic, DSL, None) |
payment_type | Type of payment method used | (Electronic check, Mailed check, Bank transfer, Credit card) |

# Project Planning

  * Acquire all relevant data from telco_churn database.
  * Prepare data for handling. Check/handle nulls if applicable.
  * Isolate at least four variables that might affect customer churn. 
  * Explore each variable for distribution, counts, ranges, etc. Run stats tests to determine dependence for each variable.
  * Run through different classification models to determine best fit.
  * Determine accuracy of best fit model and use said model to provide predictions on the test dataset.
  * Provide stakeholders with recommendations on reducing churn.

# Key Findings

  * The variables had the following p-values, in descending order.
     * tenure e-119
     * contract type e-105
     * online security e-66
     * tech support e-52
     * payment type e-47
     * monthly charges .01
  * On average, 50% of customers that will churn will churn by the 10-month mark.
  * Fiber optic internet service has a much higher ratio of churn:no_churn than DSL.
  * Month-to-month contract type is most susceptible to churn.
  * 7.40% of customers with no internet will churn vs. 31.83% of customers with internet.
  * Among those who have internet, customers who churn pay an average of $1.57 more than those who don't per month.
  * 45.94% of customers that pay with electronic check have churned.

# Recommendations

  * Invest in R&D for their Fiber Optic service.
  * Offer incentives to customers once they hit the 10-month mark.
  * Look into possible issues with electronic check payments. Might be client-side, might be customer-side.
  * Offer incentives for customers to switch to automatic method of payment.

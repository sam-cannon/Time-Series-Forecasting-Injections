# Predicting Injections Per Day
Business Problem

 

I work for a large private medical practice located in Mississippi that has just begun to realize the potential of the data they have access to. A program was created at this practice in 2016 to begin administering allergy medications in the form of shots to patients who were coming to the clinic. These shots are administered by nurses who are scheduled to be at the clinic during the hours of operation (7:30 AM - 4:30 PM). Up to this point, the nurses have been staffed arbitrarily, with no attention being paid to the number of nurses scheduled on a given day. Scheduling the nurses in shifts in this manner has led to several problems, primarily:

Nurses are over-scheduled, meaning there are too many nurses on staff during these hours, leading to loss in revenue 

Nurses are under-staffed, patients are not receiving the best care because the nursing staff is not prepared to handle a larger influx of patients

 

The Data

 

Data for this problem will be drawn from a Microsoft SQL Server over a period dating back to the first of January, 2016, when the new program was started. The data is a series of daily aggregated shot numbers, timestamped on the daily level, running up through the current day. I will pull the data from the SQL database each time I am going to train a new model to make sure that the model is receiving the most up-to-date data. 

 

Practical Implications

 

Solving this problem will potentially allow the clinic to schedule the appropriate number of nurses per day. Scheduling the correct number of nurses will increase the quality of patient care while simultaneously reducing the cost of having nurses staffed who are unnecessary given the lower volumes of shots for any given day. Since the clinic is currently not basing their decisions off of any real data, this model will help introduce the possibilities of a data-driven approach to other business problems in addition to the current issue.

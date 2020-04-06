# Roller Coaster

For this project, data visualisation covering international roller coaster rankings and roller coaster statistics will be covered.

The project occurs as follows:
- Roller coasters are often split into two main categories based on their construction material: wood or steel. Rankings for the best wood and steel roller coasters from the 2013 to 2018 Golden Ticket Awards are provided in 'Golden_Ticket_Award_Winners_Wood.csv' and 'Golden_Ticket_Award_Winners_Steel.csv', respectively.  Each dataframe is loaded so can gain familarity.
- A plot for ranking of given rollercoaster over time is plotted with arguments for this function being a roller coaster's name and a ranking DataFrame and park name as arguments.  Park name is included as most roller coaster names are not unique, with the plot showing multiple rankings for given year.  Saved as 'rollercoaster_rank_per_year.png'.
- Plot of ranking for two given roller coasters over time as lines.  This takes in both roller coasters' names and a ranking DataFrame.  Like before, both park names are added as well.  Saved as 'multiple_rollercoaster_rank_per_year.png'.
- Plot the ranking of the top n ranked roller coasters over time as lines.  Take a number n and a ranking DataFrame as arguments.  Saved as 'top_5_rollercoasters_per_year.png'.
- Now that visual ranking analysis complete, time to head into actual stats of the roller coasters.  Captain Coaster is a popular site for recording roller coaster information.  Data on all roller coasters documented on Captain Coaster has been accessed through its API and stored in roller_coasters.csv.  This data is then loaded into dataframe.
- Plot a histogram of any numerical column of the roller coaster DataFrame.  Take in a DataFrame and a column name for which a histogram should be constructed.  Saved as 'histogram_rollercoaster_column.png'.
- Create a bar chart showing the number of inversions for each roller coaster at an amusement park.  Inputs should be the roller coaster Data Frame and an amusement park name.  Saved as 'bar_chart_inversion_by_coaster.png'.
- Create a pie chart comparing the number of operating roller coasters ('status.operating') to the number of closed roller coasters ('status.closed.definitely').  Input should be rollercoaster DataFrame.  Saved as 'pie_chart_operating_status.png'.
- Create a scatter plot of two numeric columns of the roller coaster Data Frame.  Inputs should be roller coaster Data Frame and two-column names as inputs.  Saved as 'scatter_plot_two_cols.png'.
- An extra question considered is what roller coaster seating type is most popular?  This is plotted as bar graph and saved as 'bar_chart_most_popular_seating_type.png'.

import matplotlib.pyplot as plt
import pandas as pd

# load rankings data here:
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(steel.head())

print(wood.head())


# write function to plot rankings over time for 1 roller coaster here:

def plot_rank_over_time(name, rank, park):
    plt.figure(figsize=(20, 18))
    coaster_rankings = rank['Rank'][(rank['Name'] == name) & (rank['Park'] == park)]
    ax = plt.subplot()
    plt.title('Ranking of Rollercoaster at park per year')
    plt.plot(rank['Year of Rank'][(rank['Name'] == name) & (rank['Park'] == park)], coaster_rankings)
    legend_label = [name]
    plt.legend(legend_label)
    plt.xlabel('Year of Ranking')
    plt.ylabel('Ranking')
    ax.invert_yaxis()
    ax.set_xticks(rank['Year of Rank'])
    ax.set_yticks(rank['Rank'])
    plt.subplots_adjust(wspace=0.5, bottom=0.2)
    plt.savefig('rollercoaster_rank_per_year.png')


plot_rank_over_time("El Toro", wood, "Six Flags Great Adventure")
plt.show()

# write function to plot rankings over time for 2 roller coasters here:

def plot_ranks_over_time_two_roller_coaster(name1, name2, rank, park1, park2):
    coaster_rankings1 = rank['Rank'][(rank['Name'] == name1) & (rank['Park'] == park1)]
    coaster_rankings2 = rank['Rank'][(rank['Name'] == name2) & (rank['Park'] == park2)]
    print(coaster_rankings2)
    plt.figure(figsize=(20, 18))
    ax = plt.subplot()
    plt.title('Ranking of Rollercoaster at park per year')
    plt.plot(rank['Year of Rank'][(rank['Name'] == name1) & (rank['Park'] == park1)], coaster_rankings1)
    plt.plot(rank['Year of Rank'][(rank['Name'] == name2) & (rank['Park'] == park2)], coaster_rankings2)
    legend_labels = [name1, name2]
    plt.legend(legend_labels)
    plt.xlabel('Year of Ranking')
    plt.ylabel('Ranking')
    ax.invert_yaxis()
    ax.set_xticks(rank['Year of Rank'])
    ax.set_yticks(rank['Rank'])
    plt.subplots_adjust(wspace=0.5, bottom=0.2)
    plt.savefig('multiple_rollercoaster_rank_per_year.png')


plot_ranks_over_time_two_roller_coaster("El Toro", "Phoenix", wood, "Six Flags Great Adventure",
                                        "Knoebels Amusement Resort")

plt.show()


# write function to plot top n rankings over time here:
def top_n_rankings(n, rank):
    coaster_rankings_rank_max = rank[rank['Rank'] <= n]
    plt.figure(figsize=(32, 18))
    ax = plt.subplot()
    plt.title('Ranking of top 5 Rollercoasters per year')
    legend_labels = []

    for coaster in set(coaster_rankings_rank_max['Name']):
        print(coaster)
        coaster_rankings = coaster_rankings_rank_max[coaster_rankings_rank_max['Name'] == coaster]
        plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'])
        legend_labels.append(coaster)

    plt.legend(legend_labels)
    ax.invert_yaxis()
    ax.set_xticks(rank['Year of Rank'])
    ax.set_yticks(rank['Rank'])
    plt.subplots_adjust(wspace=0.5, bottom=0.2)
    plt.savefig('top_5_rollercoasters_per_year.png')


top_n_rankings(5, steel)
plt.show()

# load roller coaster data here:
roller_coaster_data = pd.read_csv('roller_coasters.csv')
# roller_coaster_data = roller_coaster_data.apply(pd.to_numeric, errors = 'coerce')
print(roller_coaster_data.head())


# write function to plot histogram of column values here:
def plot_histogram_of_col_vals(dataframe, col_name):
    dataframe = dataframe.dropna()
    plt.figure(figsize=(50, 18))
    ax = plt.subplot()
    plt.title('Histogram of ' + col_name + ' per rollercoaster')
    plt.xlabel(col_name)
    plt.ylabel('Frequency')

    if col_name == 'height':
        dataframe = dataframe[dataframe['height'] <= 140]

    ax.set_xticks(dataframe[col_name])
    plt.subplots_adjust(wspace=0.5, bottom=0.2)
    plt.hist(dataframe[col_name])
    plt.savefig('histogram_rollercoaster_column.png')


plot_histogram_of_col_vals(roller_coaster_data, "length")
plt.show()


# write function to plot inversions by coaster at a park here:
def inversions_by_coaster(dataframe, amusement_park):
    coaster_amusement_park = dataframe[dataframe['park'] == amusement_park]
    print(coaster_amusement_park.head())
    plt.figure(figsize=(50, 18))
    plt.title('Bar chart of inversion by coaster')
    plt.xlabel('Coaster')
    plt.ylabel('Frequency of inversions')
    plt.subplots_adjust(wspace=0.5, bottom=0.2)
    plt.bar(coaster_amusement_park['name'], coaster_amusement_park['num_inversions'])
    plt.savefig('bar_chart_inversion_by_coaster.png')


inversions_by_coaster(roller_coaster_data, "Parc Asterix")
plt.show()


# write function to plot pie chart of operating status here:
def plot_pie_chart_operating_status(dataframe):
    status_operating = dataframe[dataframe['status'] == 'status.operating']
    status_closed_definitely = dataframe[dataframe['status'] == 'status.closed.definitely']
    plt.figure(figsize=(20, 20))
    status_counts = [len(status_operating), len(status_closed_definitely)]
    plt.title('Operating status of rollercoaster per theme park')
    plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.axis('equal')
    plt.savefig('pie_chart_operating_status.png')


plot_pie_chart_operating_status(roller_coaster_data)
plt.show()


# write function to create scatter plot of any two numeric columns here:
def create_scatter_plot(dataframe, col1, col2):
    plt.figure(figsize=(32, 20))
    plt.title('Scatter plot comparing 2 numerical columns in roller_coasters.csv')
    if col1 == 'height' or col2 == 'height':
        dataframe = dataframe[dataframe['height'] <= 140]

    plt.scatter(dataframe[col1], dataframe[col2], marker='^')
    plt.savefig('scatter_plot_two_cols.png')


create_scatter_plot(roller_coaster_data, 'speed', 'height')
plt.show()

def most_popular_rollercoaster_seating_type(dataframe):
    plt.figure(figsize=(50, 18))
    plt.title('Most popular rollercoaster seating type')
    plt.xlabel('Seating type')
    plt.ylabel('Frequency of seating type')
    dataframe['seating_type'].value_counts().plot(kind='bar');
    plt.savefig('bar_chart_most_popular_seating_type.png')


most_popular_rollercoaster_seating_type(roller_coaster_data)
plt.show()
plt.clf()

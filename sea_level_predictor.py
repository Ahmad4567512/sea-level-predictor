import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    data = pd.read_csv('epa-sea-level.csv')

    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    years_extended = range(1880, 2051)  
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], label='Best fit line (1880 to 2050)', color='r')

    data_since_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(data_since_2000['Year'], data_since_2000['CSIRO Adjusted Sea Level'])

    plt.plot(years_extended, [slope_2000 * year + intercept_2000 for year in years_extended], label='Best fit line (2000 to 2050)', color='g')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    plt.legend()

    plt.show()

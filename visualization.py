''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''
import numpy as np
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, FactorRange, HoverTool, Title
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models.widgets import Select

# Set up data of latimes-state
rawdata_state = pd.read_csv('california-coronavirus-data-master/latimes-state-totals.csv')
rawdata_state['date_time'] = pd.to_datetime(rawdata_state['date'])
newdata = rawdata_state[['date_time','new_confirmed_cases']]
newdata = newdata[(newdata['date_time'] > "2020-08-01") & (newdata['date_time'] <= "2020-08-31")]

# Set up plot of latimes-state
p_state = figure(y_axis_label='New Confirmed Cases', x_axis_type='datetime')
p_state.line('date_time', 'new_confirmed_cases', source=newdata, line_width=2)
p_state.circle('date_time', 'new_confirmed_cases', source=newdata, fill_color='red', size=6)

p_state.add_tools(HoverTool(
    tooltips=[
        ('date', '@date_time{%Y-%m-%d}'),
        ('new cases', '@new_confirmed_cases')
    ],

    formatters={
        '@date_time': 'datetime',  # use 'datetime' formatter for '@date_time' field
    }
))

p_state.add_layout(Title(text="Date of last update: Oct. 15, 2020.", text_font_style="italic"), 'above')
p_state.add_layout(Title(text="Publish from the day at latimes.com/coronavirustracker'", text_font_style="italic"), 'above')
p_state.add_layout(Title(text="Data provide: local public health agencies.", text_font_style="italic"), 'above')
p_state.add_layout(Title(text="Available data: The Times database", text_font_style="italic"), 'above')
p_state.add_layout(Title(text="Access the data: https://github.com/datadesk/california-coronavirus-data",
                         text_font_style="italic"), 'above')
p_state.add_layout(Title(text="New Coronavirus cases in California", text_font_size="14pt"), 'above')


# Set up data of ethnicity
rawdata_race = pd.read_csv('california-coronavirus-data-master/cdph-race-ethnicity.csv')
dates = pd.unique(rawdata_race['date'])
date = list(dates)
races = pd.unique(rawdata_race['race'])

selectDate = "2020-05-14"
curdata = rawdata_race[rawdata_race['date'] == selectDate]

def cases_get_y(curdata):
    cases = curdata[curdata['age'] == 'all']['confirmed_cases_percent']
    populations = curdata[curdata['age'] == 'all']['population_percent']
    y = sum(zip(cases, populations), ())
    return y

def death_get_y(curdata):
    deaths = curdata[curdata['age'] == 'all']['deaths_percent']
    populations = curdata[curdata['age'] == 'all']['population_percent']
    y = sum(zip(deaths, populations), ())
    return y

# Set up plot of ethnicity
# plot case
barnames = ['cases','population']
x = [(race, barname) for race in races for barname in barnames]
y = cases_get_y(curdata)
source = ColumnDataSource(data=dict(x=x, y=y))

p_cases = figure(x_range=FactorRange(*x), plot_height=500)
r_cases = p_cases.vbar(x='x', top='y', width=0.9, source=source,
                       line_color="white", fill_color=factor_cmap('x', palette=['sandybrown', 'blue'],
                        factors=barnames, start=1, end=2))


p_cases.y_range.start = 0
p_cases.x_range.range_padding = 0.1
p_cases.xaxis.major_label_orientation = 1
p_cases.xgrid.grid_line_color = None

p_cases.add_tools(HoverTool(
    tooltips=[
        ('Classification', '@x'),
        ('percentage', '@y')
    ]
))

p_cases.add_layout(Title(text="Date of last update: Oct. 15, 2020.", text_font_style="italic"), 'above')
p_cases.add_layout(Title(text="Publish from the day at latimes.com/coronavirustracker'", text_font_style="italic"), 'above')
p_cases.add_layout(Title(text="Data provide: California Department of Public Health", text_font_style="italic"), 'above')
p_cases.add_layout(Title(text="Access the data from California Department of Public Health: https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx",
                         text_font_style="italic"), 'above')
p_cases.add_layout(Title(text="Access the data from github: https://github.com/datadesk/california-coronavirus-data",
                         text_font_style="italic"), 'above')
p_cases.add_layout(Title(text="Cases(%) - Population", text_font_size="14pt"), 'above')

# plot death
barnames_death = ['death','population']
x_ = [(race, barname) for race in races for barname in barnames_death]
y_ = death_get_y(curdata)
source_death = ColumnDataSource(data=dict(x=x_, y=y_))

p_death = figure(x_range=FactorRange(*x_), plot_height=500)
r_death = p_death.vbar(x='x', top='y', width=0.9, source=source_death,
                       line_color="white", fill_color=factor_cmap('x', palette=['firebrick', 'blue'],
                       factors=barnames_death, start=1, end=2))

p_death.y_range.start = 0
p_death.x_range.range_padding = 0.1
p_death.xaxis.major_label_orientation = 1
p_death.xgrid.grid_line_color = None

p_death.add_tools(HoverTool(
    tooltips=[
        ('Classification', '@x'),
        ('percentage', '@y')
    ]
))

p_death.add_layout(Title(text="Date of last update: Oct. 15, 2020.", text_font_style="italic"), 'above')
p_death.add_layout(Title(text="Publish from the day at latimes.com/coronavirustracker'", text_font_style="italic"), 'above')
p_death.add_layout(Title(text="Data provide: California Department of Public Health", text_font_style="italic"), 'above')
p_death.add_layout(Title(text="Access the data from California Department of Public Health: https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx",
                         text_font_style="italic"), 'above')
p_death.add_layout(Title(text="Access the data from github: https://github.com/datadesk/california-coronavirus-data",
                         text_font_style="italic"), 'above')
p_death.add_layout(Title(text="Death(%) - Population", text_font_size="14pt"), 'above')

# Set up widgets
select_case_date = Select(title="Select a date:", value=date[0], options=date)
select_death_date = Select(title="Select a date:", value=date[0], options=date)

# Set up callbacks
def update_plot_cases(attrname, old, new):
    curdata = rawdata_race[rawdata_race['date']==select_case_date.value]
    r_cases.data_source.data['y'] = cases_get_y(curdata)

def update_plot_death(attrname, old, new):
    curdata = rawdata_race[rawdata_race['date']==select_death_date.value]
    r_death.data_source.data['y'] = death_get_y(curdata)

select_case_date.on_change('value', update_plot_cases)
select_death_date.on_change('value', update_plot_death)


# Set up layouts and add to document
inputs_case = column(select_case_date)
inputs_death = column(select_death_date)

curdoc().add_root(row(p_state, width=800))
curdoc().add_root(row(p_cases, inputs_case, p_death, inputs_death, width=800))
# curdoc().add_root(row(p_death, inputs_death, width=800))

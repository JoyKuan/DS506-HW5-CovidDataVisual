FROM python:3.7-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD covid_data_visual.py /
ADD cdph-race-ethnicity.csv /
ADD latimes-state-totals.csv /
CMD ["bokeh", "serve" ,"--show", "covid_data_visual.py"]


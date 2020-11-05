# DS506-HW5-CovidDataVisual
Using California Coronavirus Data with Bokeh for dashboard visualizations and releasing these visualizations through a Docker container.

#### Author: Kuan-Hui Lin
#### Operating system: MacOS Catalina v10.15


# How to install and run your visualization with Bokeh
### Step 1. Clone "DS560-HW5-CovidDataVisual" into a directory using `git clone <url>`
```bash
git clone https://github.com/JoyKuan/DS506-HW5-CovidDataVisual.git
```
### Step 2. Create a new environment on your machine and install the dependencies necessary for running the Bokeh dashboard

* Create a new environment on your machine
If you want to create a virtual environment, changing your current working directory by using "cd" command into DS506-HW5-CovidDataVisual you cloned from step 1, and then install virtualenv first. (If you already have virtualenv, just skip creating virtualenv step.)
```bash
pip install virtualenv
```
Then, creating a virtual environment which is named dsci560H5:
```bash
python3 -m venv dsci560H5
```
If all steps mentioned above are not failure, activate your virtual environment by using this command
```bash
source dsci560H5/bin/activate
```
and you will see 
<img width="730" alt="Screen Shot 2020-11-04 at 19 16 22" src="https://user-images.githubusercontent.com/54604816/98193518-42f12f00-1ed2-11eb-838c-42f53e5832a8.png">

* Install the dependencies
Install the dependencies which are included in requirements.txt before executing the python script:
```bash
pip install -r requirements.txt
```
If you install the dependencies on your virtual environment successfully, you will see 
<img width="1450" alt="Screen Shot 2020-11-04 at 19 21 39" src="https://user-images.githubusercontent.com/54604816/98193946-25709500-1ed3-11eb-929d-93bf5b9b973f.png">

### Step 3. Run the python script using 
To run a Bokeh application on a Bokeh server from a single Python script (covid_data_visual.py), pass the script name to `<bokeh serve>`on the command line:
```bash
bokeh serve --show covid_data_visual.py 
```
-- show: It will raise a browser to the correct location for you and you will see the dashboard visualizations.

<img width="850" alt="Screen Shot 2020-11-04 at 19 44 27" src="https://user-images.githubusercontent.com/54604816/98195293-3b338980-1ed6-11eb-9e66-968e67cd2fd0.png">


# How to release the dashboard visualization through a Docker container







# License
Apache License 2.0



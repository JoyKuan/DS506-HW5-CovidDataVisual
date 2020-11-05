# DS506-HW5-CovidDataVisual
Using California Coronavirus Data with Bokeh for dashboard visualizations and releasing these visualizations through a Docker container.

#### Author: Kuan-Hui Lin
#### Operating system: MacOS Catalina v10.15

# How to install and run your visualization with Bokeh
## Step 1. Clone DS560-HW5-CovidDataVisual into a directory using ```git clone <url>```
```bash
git clone https://github.com/JoyKuan/DS506-HW5-CovidDataVisual.git
```
## Step 2. Create a new environment on your machine and install the dependencies necessary for running the Bokeh dashboard

### Create a new environment on your machine
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

### Install the dependencies
Install the dependencies which are included in requirements.txt before executing the python script:
```bash
pip install -r requirements.txt
```
If you install the dependencies on your virtual environment successfully, you will see 
<img width="1450" alt="Screen Shot 2020-11-04 at 19 21 39" src="https://user-images.githubusercontent.com/54604816/98193946-25709500-1ed3-11eb-929d-93bf5b9b973f.png">

## Step 3. Run the python script using 
To run a Bokeh application on a Bokeh server from a single Python script (covid_data_visual.py), pass the script name to ```bokeh serve``` on the command line:
```bash
bokeh serve --show covid_data_visual.py 
```
-- show: It will raise a browser to the correct location for you and you will see the dashboard visualizations.



# How to release the visualization through a Docker container







# License
Apache License 2.0









# Setup
Before to run plot_equation.py, you need to install Matplotlib:

+ Install Matplotlib with Anaconda Prompt
```bash
conda install matplotlib
```
+ Install Matplotlib with pip
  
  Use the package manager pip to install matplotlib
```bash
pip install matplotlib
```

# How to run Python scripts
System: macOS

Open a command-line and take note of the path of the Python script in Finder. Use the cd command to navigate to the folder containing the Python file. If you copide the pathname before, paste the pathname after the cd command. If you hava python3 version, and then run them in order. Type the following command to execute three scripts:
```bash
$ python3 generate_input_x.py
$ python3 generate_output_y.py
$ python3 plot_equation.py
```

# Output Files
If there is no problem after you run all three scripts in order, you will see three output files in your disk.
If there exists some problems, you will need to check your Python installation.

**Output Files:**
1. x_dataset.csv
2. y_dataset.csv
3. equation_graph.png

# Jupyter Notebook
See notebook [visualization_equation.ipynb](https://github.com/JoyKuan/DS560-HW2/blob/master/visualization_equation.ipynb).

This Python Notebook that calls the three scripts, generate_input_x.py, generate_output_y.py and plot_equation.py, in order. You can follow the instructions mentioned in Notebook, and then you will see the graph of a linear equation y=3x+6.

# License
Apache License 2.0

# Execute GitHub project(DS560-HW2) on a virtual environment
System: MacOS

The instructions and details will be clearly described below.

## Step 1. Clone DS560-HW2 into your local repository  (Question 1)
Clones the repository, DS560-HW2, into a newly created directory with git clone <url>. For example, if you want to clone the Git linkable library called DS560-HW2, you can do so like this:
```bash
git clone https://github.com/JoyKuan/DS560-HW2.git
```

## Step 2. Create a blank environment on the local repository and name it dsci560H4  (Question 1)
1. Install virtualenv on the local repository on MacOS.
```bash
pip install virtualenv
```

2. Create a virtual environment
The second argument is the location to create the virtual environment. You can use "env" or change "env" into your name of the environment(e.g. dsci560H4). 
* Generally, the commands is
```bash
python3 -m venv env 
```
* In this project, the command is 
```bash
python3 -m venv dsci560H4
```
  
3. Activate your virtual environment and install the dependencies for executing the random number generator script **(Question 2)**
Before you start installing or using packages in the virtual environment you’ll need to activate it. 
```bash
source env/bin/activate
```

And then install the package, pandas, for executing the random number script (generate_input_x.py).
In order to save the dependencies, you need to execute the command which records an environment's current package list into requirements.txt.
In the requirements.txt file that contains a list of commands for pip that installs the required versions of dependent packages.
If you did not install the dependencies, you will see the empty content in requirements.txt file.
```bash
pip freeze > requirements.txt
```

The screenshot shows the change of requirements.txt. If you do not install the dependencies, you will see the empty content in requirements.txt file. Once you execute the random number script and it shows error message that notify you to install the module 'pandas'. After you installed the package, pandas, then executing the pip command metioned above, and you will see the necessary packages listed in requirements.txt. In this screenshot, you will find all these required packages are generated after manually installing pandas. You can see a mapping of package names and version constraints and also include the pandas dependency and the version of pandas(1.1.3) to use. **( Question 2 and Question 4(a) )**
* numpy==1.19.2
* pandas==1.1.3
* python-dateutil==2.8.1
* pytz==2020.1
* six==1.15.0

![Xnip2020-10-25_01-04-35](https://user-images.githubusercontent.com/54604816/97101866-19c4d900-165e-11eb-9d41-48aedf26a161.jpg)

Also, after installing the package, matplotlib, for executing the visualization script, you can view 
![Xnip2020-10-25_01-40-44](https://user-images.githubusercontent.com/54604816/97102483-2861bf00-1663-11eb-87f4-b233c09827d6.jpg)


This screenshot of the terminal with the activated environment after running the script for the number generator. **( Question 3 )**
Because there is no print in this file, it will not show any output result but will store the output data into the disk.
![Screen Shot 2020-10-25 at 00 49 08](https://user-images.githubusercontent.com/54604816/97101586-057fdc80-165c-11eb-82b1-4cfefa6bedff.png)

## Step 3. (Question 4(b))
Create a .gitignore file in the repository's root directory via the command. And set .gitignore to tell Git do not track content of the folder, dsci560H4.
```bash
touch .gitignore
```
and set .gitignore configurations via vim and save it.
```bash
vim .gitignore
```

## Step 4. (Question 4(c))
Upload your extracted dependencies to GitHub via Github Desktop. Push changes to GitHub and send the committed changes in your local repository to the remote repository on GitHub.


# Binder Repository (Question 6(b))
Launch the noteook with latest visualization_equation : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JoyKuan/DS560-HW2/master?filepath=visualization_equation.ipynb)

visualization_equation.ipynb is a short Jupyter Notebook that generates a plot of the equation.



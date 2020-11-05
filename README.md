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

* **Create a new environment on your machine**
  
  If you want to create a virtual environment, changing your current working directory by using "cd" command into DS506-HW5-CovidDataVisual you cloned from step   1, and then install virtualenv first. (If you already have virtualenv, just skip creating virtualenv step.)
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
  <img width="730" alt="Screen Shot 2020-11-04 at 19 16 22" src="https://user-images.githubusercontent.com/54604816/98195782-68cd0280-1ed7-11eb-8b14-19c10b9bd21d.png">

* **Install the dependencies**
  
  Install the dependencies which are included in requirements.txt before executing the python script:
  ```bash
  pip install -r requirements.txt
  ```
  If you install the dependencies on your virtual environment successfully, you will see 
  <img width="1450" alt="Screen Shot 2020-11-04 at 19 21 39" src="https://user-images.githubusercontent.com/54604816/98193946-25709500-1ed3-11eb-929d-93bf5b9b973f.png">

### Step 3. Run the python script on a Bokeh server
To run a Bokeh application on a Bokeh server from a single Python script (covid_data_visual.py), pass the script name to `<bokeh serve>` on the command line:
```bash
bokeh serve --show covid_data_visual.py 
```
-- show: It will raise a browser to the correct location for you and you will see the dashboard visualizations.

<img width="850" alt="Screen Shot 2020-11-04 at 19 44 27" src="https://user-images.githubusercontent.com/54604816/98195293-3b338980-1ed6-11eb-9e66-968e67cd2fd0.png">


# How to release the dashboard visualization through a Docker container
### Step 1. Install [Docker Destop](https://www.docker.com/products/docker-desktop) on your computer which using MacOS
About how to install Docker Desktop on Mac, you can refer this link: https://docs.docker.com/docker-for-mac/install/

After you’ve successfully installed Docker Desktop, open a terminal and run `<docker --version>` to check the version of Docker installed on your machine.
Test that your installation works by running the hello-world Docker image through this comman:
```bash
docker run hello-world
```
and you will see this result which means you already install Docker successfually.
<img width="726" alt="Screen Shot 2020-11-04 at 20 07 03" src="https://user-images.githubusercontent.com/54604816/98196639-800cef80-1ed9-11eb-9df0-a88ca46a9938.png">







# License
Apache License 2.0



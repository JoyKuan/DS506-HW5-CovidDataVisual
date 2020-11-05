# DS560-HW5-CovidDataVisual
Using California Coronavirus Data with Bokeh for dashboard visualizations and releasing these visualizations through a Docker container.

#### Author: Kuan-Hui Lin
#### Operating system: MacOS Catalina v10.15


# How to install and run your visualization with Bokeh
### Step 1. Clone "DS560-HW5-CovidDataVisual" into a directory using `git clone <url>`
```bash
git clone https://github.com/JoyKuan/DS560-HW5-CovidDataVisual.git
```
### Step 2. Create a new environment on your machine and install the dependencies necessary for running the Bokeh dashboard

* **Create a new environment on your machine**
  
  If you want to create a virtual environment, changing your current working directory by using "cd" command into DS560-HW5-CovidDataVisual you cloned from step   1, and then install virtualenv first. 
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
  <img width="1298" alt="Screen Shot 2020-11-05 at 00 44 04" src="https://user-images.githubusercontent.com/54604816/98217962-0e946780-1f00-11eb-949c-29e09d05583b.png">

* **Install the dependencies**
  
  Install the dependencies which are included in requirements.txt before executing the python script:
  ```bash
  pip install -r requirements.txt
  ```
  If you install the dependencies on your virtual environment successfully, you will see 
  <img width="1450" alt="Screen Shot 2020-11-04 at 19 21 39" src="https://user-images.githubusercontent.com/54604816/98193946-25709500-1ed3-11eb-929d-93bf5b9b973f.png">

### Step 3. Run the python script on a Bokeh server
To run a Bokeh application on a Bokeh server from a single Python script (covid_data_visual.py), pass the script name to `bokeh serve` on the command line:
```bash
bokeh serve --show covid_data_visual.py 
```
**-- show**: It will raise a browser to the correct location for you and you will see the dashboard visualizations.

<img width="1299" alt="Screen Shot 2020-11-05 at 00 47 42" src="https://user-images.githubusercontent.com/54604816/98218376-8cf10980-1f00-11eb-8774-44e88510e957.png">


# How to release the dashboard visualization through a Docker container with a view of the dashboard from a local machine
If you are already in virtual environment, please deactivate your venv by typing `deactivate` in your shell.
### Step 4. Install [Docker Destop](https://www.docker.com/products/docker-desktop) on your computer which using MacOS
About how to install Docker Desktop on Mac, you can refer this link: https://docs.docker.com/docker-for-mac/install/

After you’ve successfully installed Docker Desktop and the docker daemon is running, open a terminal and run `docker --version` to check the version of Docker installed on your machine.
Test that your installation works by running the hello-world Docker image through this comman:
```bash
docker run hello-world
```
and you will see this result which means you already install Docker successfually. Under this command, Docker will find whether the image exists locally, but it definitely does not exist because the environment has just been installed. After that, Docker will go to the remote Docker registry server to download the image.

<img width="745" alt="Screen Shot 2020-11-05 at 00 58 41" src="https://user-images.githubusercontent.com/54604816/98219660-2836ae80-1f02-11eb-8a21-1fe25433e0df.png">

### Step 5. Change your current working dictionary to the repository you already cloned from step 1 
Make sure you are in the directory **DS560-HW5-CovidDataVisual** in a terminal using the cd command. 

### Step 6. Build the image
The repository, **DS560-HW5-CovidDataVisual**, already has a Dockerfile, a python script (covid_data_visual.py) and two csv files, then you can build your first image, and make sure the containers launched from it work as expected. Run the following command to build your **covidashboard** image with the version 1.0:
```bash
docker build --tag covidashboard:1.0 .
```
**--tag**: The parameter is used to specify the name of the image file
If not specified the version, the default tag is **latest**

If successful, the build process should like this:

<img width="1237" alt="Screen Shot 2020-11-04 at 22 58 56" src="https://user-images.githubusercontent.com/54604816/98207999-5fe92a80-1ef1-11eb-967d-90634f4bb0d3.png">

You also can use this command to see your all images you built and check whether or not there is the name of repository, **covidashboard** and its tag is 1.0.
```bash
docker images
```
<img width="835" alt="Screen Shot 2020-11-04 at 23 11 18" src="https://user-images.githubusercontent.com/54604816/98208993-13065380-1ef3-11eb-87fe-e33a8c6c0e1c.png">

### Step 7. Run the image as a container
Start a container based on your image, **covidashboard:1.0**, by using the following command:
```bash
docker run -p 5006:5006 -it covidashboard:1.0
```

**-p 5006:5006** - map port 5006 of the host to port 5006 in the container

**-it** - is short for --interactive + --tty when you docker run with this command, it would take you straight inside of the container

**covidashboard:1.0** - the image to use

Once your container works correctly, open the port below, when using Bokeh serve the ports are displayed in the console. 
http://localhost:5006/covid_data_visual

Some screenshots of the final result:
<img width="798" alt="Screen Shot 2020-11-04 at 23 33 39" src="https://user-images.githubusercontent.com/54604816/98210994-4696ad00-1ef6-11eb-945d-7765f401d50a.png">
![Screen Shot 2020-11-04 at 23 35 58](https://user-images.githubusercontent.com/54604816/98211299-b0af5200-1ef6-11eb-8d83-bc385c735473.png)


# License
Apache License 2.0



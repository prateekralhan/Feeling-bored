# 🤔 Feeling bored? 🥱 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

Not to worry !! This simple webapp will give you suggestions for doing random but interesting tasks.

![low_banner](https://user-images.githubusercontent.com/29462447/165392925-90d78675-47cd-427c-80fd-d50a34902ddd.png)

## Demo: 
![demo](https://user-images.githubusercontent.com/29462447/165392894-0acec9a2-b3fd-4455-a193-962f64c35d9d.gif)

## Installation:
* Simply run the command **pip install -r requirements.txt** to install the necessary dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Make a directory within this cloned repository with the name `.streamlit` *(Don't forget the dot !!)*.
3. Create a file `config.toml` in this directory *(Be aware of the file extension !!)*.
4. Copy-Paste the following contents in this file and save :
```
[theme]
primaryColor="#ffb5b5"
backgroundColor="#132743"
secondaryBackgroundColor="#407088"
textColor="#ffb5b5"
```

5. Navigate to the root directory of this repository and simply run the command: 
```
streamlit run app.py
```
Navigate to http://localhost:8501 in your web-browser.


![1](https://user-images.githubusercontent.com/29462447/165393284-5f311f89-15e5-4498-abb2-f9194adff594.png)

![2](https://user-images.githubusercontent.com/29462447/165393277-782db1e2-df6c-4659-adef-3e41fc43fb84.png)


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```

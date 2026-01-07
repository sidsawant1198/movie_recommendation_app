Sign in to github

APP LINK : https://movierecommendationapp101.streamlit.app/

1) Create Repo

2) gitbash
3) cd d:
4) Go to git Repo (Green button Code)-> Copy the url of repo (HTTPS)
5) git clone <repo_URL>

6) Now the git repo gets made/cloned in the D: drive

7) cd match_resume.ai/    (went to the actual folder - main to open VScode there)
8) code .
9) IN vscode now you will land on the project match_resume.ai/ , click on newfile
10) create .env file (to store api etc.) GOOGLE-GEMINI-API = "api_key"
11) create requirements.txt (Google colab comes with preinstalled libraries, but not vscode)
12) streamlit, pypdf, google-generativeai, (now we want to run the apikey to run locally before it goes global)
so python-dotenv, langchaiin
13) Click on terminal (powershell opens)(convert it to Gitbash)
14) Now lets create the virtual env 
15) Before that optionally we can write notes in read me
16) Check python version
17) python -m venv .venv  (create venv)
18) source .venv/Scripts/activate    or source .venv/bin/activate (works for macos)
19) pip install - requirements.txt
20) create app.py
21) Write or copy the code
22) lets say you want to test the code written so far use command streamlit run app.py
23) for the first time it will ask for some credentials
24) once you are done running the app go to gitbash
25) activate venv (if needed) then type git init
26) git add. (add everything)
27) git commit -m "Final-Commit"
28) If running git the first time:
	git config --global user.email <emailid>
	git config --global user.name  <user_name>
29) git push origin main
30) git commit -m "Final-Commit"
31) git push origin main
32) GO to streamlit and login using GitHub , click on create app
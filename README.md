# fryns-kafka

## Installation
First clone the repository
```
git clone https://github.com/XTCDo/fryns-kafka.git
```

Make sure you have python virtualenv installed
```
pip install virtualenv
```

Then make a python virtual environment. 
```
python3 -m venv venv
```

Now activate the virtual environment, make sure you are in the project root folder
```
source venv/bin/activate
```
You will see if you are in the virtual environment if your command line says `(venv)`

Then install the requirements
```
pip install -r requirements.txt
```

To leave the virtual environment type `deactivate`
If the program does not properly run, make sure you are in the virtual environment
If any additional dependencies are needed, please add them to requirements.txt

## Running
Activate the virtual environment and run
```
python3 src/producer.py
```

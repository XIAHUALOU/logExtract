# how to use logExtract
## Set Up Enviroment
1. install python environment
2. pip install -r requirements.txt
## How to named logfile
logfile should be lowercase and endswith ".log",when a log was generated,it should 
has time property and number of tests
## where is logfiles
put logfile into log folder,it can be anyplace under the log folder

Example: nginx2019060101,in this case "20190601" is time,the last "01" is number of tests 
## config.ini
#### set up workers
In config.ini,you can see workers option.you can set workers under it(example workers = Python,Ruby),
Python and Ruby log will be extracted,All logs will be extracted,if u don't set anything
#### set up test times
For instance,if u execute one script 5 times and generate 5 logs,then you should set times = 5 under test_times option
## Run logExtract
python start.py
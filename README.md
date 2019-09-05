# how to use logExtract
## Set Up Enviroment
1. install python3 environment
2. pip3 install -r requirements.txt
## How to named logfile
logfile should be lowercase and endswith ".log",when a log was generated,it should 
has time property and number of tests
## logfiles path
put logfile into log folder,it can be anyplace under the log folder,set platform = ubuntu in config.ini if your log belongs to ubuntu
Example: nginx01,in this case ,last "01" is number of tests 
## config.ini
#### set up workers
In config.ini,you can see workers option.you can set workers under it(example workers = Python,Ruby) and first character must be uppercase
Python and Ruby log will be extracted,All logs will be extracted,if u don't set anything
#### set up test times
For instance,if u execute one script 5 times and generate 5 logs,then you should set times = 5 under test_times option

## Run logExtract
run command python3 start.py ,a little time later,report.xlsx will lie beside start.py










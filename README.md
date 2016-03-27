# Python + Selenium UI testing for Sportamore

## Installation Instructions

System Requirements: a Unix-like OS with java and python3.

```
pip3 install -r requrements.txt
```

## Launching tests
```
# launch the Selenium grid hub
java -jar selenium-server-standalone-2.52.0.jar -port 4444 -role hub -nodeTimeout 1000

&

# launch the first Firefox node
java -jar selenium-server-standalone-2.52.0.jar -role node -hub http://localhost:4444/grid/register -browser browserName=firefox -port 5555

&

# launch the second Firefox node
java -jar selenium-server-standalone-2.52.0.jar -role node -hub http://localhost:4444/grid/register -browser browserName=firefox -port 5556

# run the tests
py.test -n 2 main.py
```

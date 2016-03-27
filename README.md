# Python + Selenium UI testing for Sportamore

## Installation Instructions

System Requirements: a Unix-like OS with java and python3.

```
pip3 install -r requrements.txt
```

Download the Selenium server
```
wget http://goo.gl/IHP6Qw
```

## Launching tests

1. Launch the Selenium grid hub
```
java -jar selenium-server-standalone-2.53.0.jar -port 4444 -role hub -nodeTimeout 1000
```

2. Launch the first Firefox node on port 5555
```
java -jar selenium-server-standalone-2.53.0.jar -role node -hub http://localhost:4444/grid/register -browser browserName=firefox -port 5555
```

3. Launch the second Firefox node on port 5556
```
java -jar selenium-server-standalone-2.53.0.jar -role node -hub http://localhost:4444/grid/register -browser browserName=firefox -port 5556
```

4. Run the two tests in parallel
```
py.test -n 2 main.py
```

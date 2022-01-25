# quantcast-challenge: 
## given a cookie log, return the most active cookie on a given date 


### Setup
```python
# installing all necessary python packages
pip3 install -r requirements.txt
```

## Example usage: 

### One expected output 
```python
# script filePath targetDate
./most_active_cookie cookie_log.csv -d 2018-12-09
```
```
AtY0laUfhglK3lC7
```

### Multiple expected outputs
```python
# script filePath targetDate
./most_active_cookie.py cookie_log.csv -d 2018-12-08
```
```
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
```

### Using pytest

Move into "test" directory and input "pytest" on command line to run pytest





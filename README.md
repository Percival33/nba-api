# nba-api

This is recruitment task for Intern Python Developer at [Profil Software](https://profil-software.com/).

Task is to build a script/CLI that will process data from external API about NBA related data and return desirable results.

## TODO

- [x] add specification section
- [x] add examples of usage
- [x] teams related data ie. teams grouped into divisions
- [x] specific player data
- [x] season statistics
- [x] storing options (json, csv, sqlite, stdout)
- [ ] add type hinting

## Instalation

To install all dependencies:

```py
pip install requirements.txt
```

## Usage

### 0. To get help with arguments or its values run

```py
# to get help with general usage
python script.py -h

# or with specific one
python script.py teams-stats --season 2018 -h
```

### 1. Getting all teams grouped by divisions

```py
python script.py grouped-teams
```

### Example output

```
Southeast
        Atlanta Hawks (ATL)
        Charlotte Hornets (CHA)
        Miami Heat (MIA)
        Orlando Magic (ORL)
        Washington Wizards (WAS)
Atlantic
        Boston Celtics (BOS)
        Brooklyn Nets (BKN)
        New York Knicks (NYK)
        Philadelphia 76ers (PHI)
        Toronto Raptors (TOR)
<rest of the teams and divisions>
```

### 2. Get players with a specific name who is the tallest and another one who weight the most (values in metric system)

`--name` parameter is required. Provide first or last name.

```py
python script.py players-stats --name James
```

### Example output

```
The tallest player: James Johnson 2.03 meters
The heaviest player: LeBron James 113 kilograms
```

or if there is no data provided:

```
The tallest player: Not found
The heaviest player: Not found
```

### 3. Get statistics for a given season and optionally store it

- `--season` parameter is **required**. Seasons are represented by the year they began. For example, 2018 represents season 2018-2019
- `--output` parameter is optional. The default value is `stdout`.

  Possible parameters:

  - json
  - csv
  - sqlite
  - stdout

```py
python script.py teams-stats --season 2018
```

### Example output

```
Atlanta Hawks (ATL)
    won games as home team: 17
    won games as visitor team: 12
    lost games as home team: 24
    lost games as visitor team: 29
Boston Celtics (BOS)
    won games as home team: 30
    won games as visitor team: 24
    lost games as home team: 15
    lost games as visitor team: 22
Brooklyn Nets (BKN)
<rest of teams statistics>
```

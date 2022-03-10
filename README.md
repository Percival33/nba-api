# nba-api

This is recruitment task for Intern Python Developer at [Profil Software](https://profil-software.com/).

## TODO

- [ ] add specification section
- [ ] add examples of usage
- [x] teams related data ie. teams grouped into divisions
- [x] specific player data
- [ ] season statistics
- [ ] storing options (json, csv, sqlite, stdout)
- [ ] add type hinting

## Usage

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

`--name` parameter is required

```py
python script.py players-stats --name James
```

### Example output

```
The tallest player: James Johnson 2.03 meters
The heaviest player: LeBron James 112 kilograms
```

or if there is no data provided:

```
The tallest player: Not found
The heaviest player: Not found
```

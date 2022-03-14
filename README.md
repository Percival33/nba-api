# nba-api

Author: [Marcin Jarczewski](https://github.com/Percival33).

This is recruitment task for Intern Python Developer at [Profil Software](https://profil-software.com/).

Task is to build a script/CLI that will process data from external [API](https://www.balldontlie.io/) about NBA related data and return desirable results.

## Installation

Start by cloning the repository:

```
git clone https://github.com/Percival33/nba-api.git
```

Usage of `virtualenv` is recommended.

> While working on macOS replace `pip` with `pip3` and `python` with `python3`. To install pip3 on macOS install python3.
>
> ```
> brew install python3
> ```
>
> or follow instructions from this [page](https://www.delftstack.com/howto/python/python-install-pip3-mac/).

- Start by installing `virtualenv`

```
pip install virtualenv
```

- When installation is completed, go to project folder

```
cd nba-api
```

- Create virtual environment called `venv`

```
python -m virtualenv venv
```

- Then activate `venv` it

```
source venv/bin/activate
```

- Install all python dependencies:

```py
pip install -r requirements.txt
```

- **Now you are ready to use script**

>  - When you are done, deactivate `venv` using command:
>
>  ```
>  deactivate
>  ```

## Usage

### 0. To get help with arguments or its values

- Example usage: (to get help with general usage)

  ```py
  $ python script.py -h
  usage: script.py [-h] {grouped-teams,players-stats,teams-stats} ...

  positional arguments:
    {grouped-teams,players-stats,teams-stats}
      grouped-teams       Get all teams grouped in divisions
      players-stats       Get players with name (first or last) who is the tallest and is the heaviest
      teams-stats         Get statistics for a given season and optionally store it

  optional arguments:
    -h, --help            show this help message and exit
  ```

- Example usage: (of specific help)

  ```py
  $ python script.py teams-stats --season 2018 -h
  usage: script.py teams-stats [-h] --season SEASON [--output {csv,json,sqlite,stdout}]

  optional arguments:
    -h, --help            show this help message and exit
    --season SEASON       Seasons are represented by the year they began. For example, 2018 represents season 2018-2019.
    --output {csv,json,sqlite,stdout}
                          Choose output format. stdout is default
  ```

- To get help with specific argument value use `-h` or `--help`

  Example usage:

  ```py
  $ python script.py players-stats -h
  usage: script.py players-stats [-h] --name NAME

  optional arguments:
    -h, --help   show this help message and exit
    --name NAME  Provide first or last name of player to get their statistics
  ```

### 1. Getting all teams grouped by divisions

Example input:

```py
python script.py grouped-teams
```

Example output:

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

`--name` parameter is **required**. Provide first or last name.

Example input:

```py
python script.py players-stats --name James
```

Example output:

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

- `--output` parameter is optional. The default value is `stdout`. Otherwise, output.\* file will be created.

  Possible parameters:

  - json
  - csv
  - sqlite
  - stdout

Example input:

```py
python script.py teams-stats --season 2018
```

Example output:

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

## TODO (in future)

- [x] add specification section
- [x] add examples of usage
- [x] teams related data i.e. teams grouped into divisions
- [x] specific player data
- [x] season statistics
- [x] storing options (json, csv, sqlite, stdout)
- [x] add type hinting
- [ ] add **tests**
- [ ] add autocomplete/autosuggestion

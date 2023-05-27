
# Espressoft

This software is a desktop application specifically designed for importing data from an Excel file (dummy file). It efficiently manages and presents information regarding total sales and employee records in a visually appealing and user-friendly interface. The primary objective is to provide a seamless experience for users, allowing them to easily view and comprehend the data.

## Requirements
- Python
- Conda
- MySQL 5 or higher
- Docker (not necessary)

## Run These commands to get everything set up

1. Clone the project

```bash
  $ git clone https://JulioSD26/Espressoft
```

2. Go to the project directory

```bash
  $ cd Espressoft/Espressoft-master
```

3. Create environment (conda) (If you have Conda, you can skip step 4)

```bash
  $ conda env create -f environment.yml
```
(Venv, Step 4 is forced)
```bash
  $ python -m venv espressoft
```

4. Install dependecies

```bash
  $ pip install -r requirementsPip.txt
```

## Other commands

Update dependecies

```bash
  $ pip freeze > requirementsPip.txt
```

If you use Docker for enable database for the first time (run mysql_dump file):
```bash
  $ docker-compose up --build
```
Turn it down:
```bash
  $ docker-compose down
```
Turn it back on:
```bash
  $ docker-compose up
```


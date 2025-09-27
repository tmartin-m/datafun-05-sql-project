# datafun-05-sql-project

![NHL LOGO](C:\Users\tmmar\datafun-05-sql-project\nhl_logo.png)

## Overview
This project demonstrates how to use Python and SQLite to analyze NHL player and team statistics using SQL queries. It includes data manipulation, aggregation, and visualization.

1. Machine Setup
https://github.com/denisecase/pro-analytics-01/blob/main/01-machine-setup/MACHINE-SETUP.md

2. Project Initialization
- Either Copy an existing project of create a new on from scratch (choose 1)
     - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/01a-copy-existing-repo-in-github.md
     - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/01b-create-repo-in-github.md

- Clone repo to local.md
   - ALWAYS Use Git to clone the new repository to your local machine
```
git clone https://github.com/youraccount/yourrepo
```
   - File > Preferences > Settings > Search 'terminal.integrated.cwd' > update file pathway

- If starting from scratch only : Add key files such as .gitignore and requirements.txt
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/03-add-gitignore-and-requirements.md
  - Create a new file in your root repo folder named exactly: .gitignore IMPORTANT: Spelling, capitalization, and name are critical. If the name or location is not exact, it will not work. Find the .gitignore file in the root of this pro-analytics-01 repo and paste the entire contents into your .gitignore file. This is a good starting point for many Python projects. Actual .gitignore contents will vary by project.
  - Create a new file in your root project folder named exactly: requirements.txt. IMPORTANT: Spelling, capitalization, and name are critical. If the name or location is not exact, the commands we provide will not work. Find the requirements.txt file in the root of this pro-analytics-01 repo and paste the entire contents into your requirements.txtfile. This is a good starting point for many Python projects. Actual requirements.txt contents will vary by project.

- If starting from scratch only: Use Git to add, commit, and push your new files to GitHub:
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/04-git-add-commit-push.md
```
git add .
```
```
git commit -m "Add .gitignore and requirements.txt files"
```
```
git push -u origin main
```
- ALWAYS create a python virtual environment for your project:
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/05-create-virtual-environment.md
```
py -m venv .venv
```

3. Repeatable Project Workflow
- Pull Changes
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/01-git-pull-before-changes.md
```
git pull origin 
```

- Activate Virtual Environment
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/02-activate-virtual-environment.md
```
.venv\Scripts\activate
```
  - https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5
```
cmd.exe
```
```
pwsh.exe -ExecutionPolicy AllSigned
```

- Install Dependencies
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/03-install-dependencies.md
```
.\.venv\Scripts\activate
```
```
py -m pip install --upgrade pip setuptools wheel
```
```
py -m pip install -r requirements.txt
```

- Run Scripts and/or Jupyter notebooks
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/04a-activate-and-run-python-script.md
    - Ctrl+Shift+P
    - Python: Select Interpreter
    - Choose an Interpreter - Look for the recommended local .venv option.
    - Activate and Execute
```
.\.venv\Scripts\activate
```
```
py myfile.py
```

- https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/04b-activate-and-run-jupyter-notebook.md
    - Open the project notebook in VS Code. The file will have a .ipynb extension.
    - If prompted, select a Python interpreter that corresponds to your .venv.
    - If not prompted, click the kernel selector in the top-right corner of the notebook editor and choose the interpreter associated with your Python Environment / .venv.
    - Or:
    - From VS Code Menu, select View / Command Palette... (CTRL SHIFT P)
    - Type: Python: Select Interpreter
    - Choose your .venv from the list

- Modify Code and test
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/05-modify-and-test.md

- Save
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/06-git-add-commit-push.md
```
git add .
```
```
git commit -m "Add .gitignore and requirements.txt files"
```
```
git push -u origin main
```

4. Example Repo
https://github.com/denisecase/datafun-05-spec
- Project Checklist
  - Design a schema with at least two related tables, including foreign key constraints. Document the schema design in your README.md.
    - sql_create folder:
      - 01_drop_tables.sql - drop tables to restart
      - 02_create_tables.sql - create your database schema using sql
      - 03_insert_records.sql - insert at least 10 additional records into each table.
    - db01_setup.py:
      - Create a Python script that demonstrates the ability to create a database, define a schema, and insert records. Make it easy to re-run by dropping the tables first.
  - Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements. You might create an additional table, insert new records, and perform data querying (with filters, sorting, and joining tables), data aggregation, and record update and deletion.
    - sql_features folder:
      - update_records.sql - update 1 or more records in a table.
      - delete_records.sql - delete 1 or more records from a table.
    - db02_features.py
      - Create a Python script that demonstrates the ability to run sql scripts to interact with fields, update records, delete records, and maybe add additional columns.
  - Implement SQL statements and queries to perform aggregations and queries.
    - sql_queries folder:
      - query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
      - query_filter.sql - use WHERE to filter data based on conditions.
      - query_sorting.sql - use ORDER BY to sort data.
      - query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
      - query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.
    - db03_queries.py
      - Use Python to execute the SQL queries and maybe chart, illustrate, and/or summarize your findings:

5. Data Source
   - https://www.nhl.com/stats/skaters?reportType=season&seasonFrom=20242025&seasonTo=20242025&gameType=2&sort=points,goals,assists&page=0&pageSize=100
   - NHL Player and NHL Team Data was pulled and thinned for the 2024-2025 season for all 32 teams and for all 920 players listed on the website.

6. 📈 Summary of Findings

- Total number of players analyzed.
- Average points scored per player.
- Total games played across all players.
- Players with more than 100 points.
- Points and penalty minutes summarized by position.
- Team-player relationships and performance.

7. 📊 Visualizations

### Average Penalty Minutes by Position
![Average Penalty Minutes](avg_penalty_minutes_by_position.png)

### Points Summary by Position
![Points Summary](points_summary_by_position.png)




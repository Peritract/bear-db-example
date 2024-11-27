# Small DB example

This folder contains a small example of the following:

1. Setting up a basic DB
2. Seeding it with basic data
3. Updating lots of rows at once efficiently

## Database creation, setup, and insertion

- Make a `venv`
- Activate it
- `pip3 install -r requirements.txt`
- `psql postgres -f schema.sql` to make the database and all tables
- `psql bear_attacks -f seed.sql` to put seed data into the database
- `python3 simulate_attacks.py` to generate fake data
- `python3 bulk_insert.py` to upload all generated data to the database

"""A script that inserts bulk data efficiently."""

from csv import DictReader

from db_functions import get_db_connection, upload_attacks, get_bear_type_mapping_dict, get_location_mapping_dict, format_attacks_for_insertion

def load_attack_data(filename="attacks.csv") -> list[dict]:
    """Returns a list of attack dicts from a file."""

    with open(filename, 'r', encoding='utf-8') as f:
        reader = DictReader(f)
        data = list(reader)

    return data

if __name__ == "__main__":

    # Ideally would load from ENV
    db_config = {
        "DB_NAME": "bear_attacks",
    }

    db_conn = get_db_connection(db_config)

    # Load the attack data from a file
    attacks = load_attack_data()

    # Access the seeded data IDs to simplify upload
    location_mapping = get_location_mapping_dict(db_conn)
    bear_mapping = get_bear_type_mapping_dict(db_conn)

    # Process the attack data for insertion
    attacks = format_attacks_for_insertion(attacks, location_mapping, bear_mapping)

    # Upload the formatted data
    upload_attacks(attacks, db_conn)

    print("Upload complete.")
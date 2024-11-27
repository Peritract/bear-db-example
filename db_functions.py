"""Functions that interact with the database."""

from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor, execute_values

def get_db_connection(config) -> connection:
    """Returns a live connection to the database."""
    return connect(
        database=config["DB_NAME"],
        cursor_factory=RealDictCursor
    )


def get_all_bear_types(conn: connection) -> list:
    """Returns all bear types from the database."""

    cur = conn.cursor()
    cur.execute("SELECT bear_type FROM bear_type;")
    rows = cur.fetchall()
    cur.close()

    return [r["bear_type"] for r in rows]


def get_location_mapping_dict(conn: connection) -> dict:
    """Returns a dict mapping location names to in-database IDs."""

    with conn.cursor() as cur:
        cur.execute("SELECT location_name, location_id FROM location;")
        rows = cur.fetchall()
    return {row["location_name"]: row["location_id"] for row in rows}

def get_bear_type_mapping_dict(conn: connection) -> dict:
    """Returns a dict mapping bear type names to in-database IDs."""

    with conn.cursor() as cur:
        cur.execute("SELECT bear_type, bear_type_id FROM bear_type;")
        rows = cur.fetchall()
    return {row["bear_type"]: row["bear_type_id"] for row in rows} # Dictionary comprehension

    mapping = {}
    for row in rows:
        mapping[row["bear_type"]] = row["bear_type_id"]

def format_attacks_for_insertion(attack_data: list[dict],
                                 loc_map: dict, bear_map: dict) -> list[tuple]:
    """Returns a list of attack tuples in which string values have been replaced
    with relevant IDS from the database."""

    formatted = []

    for attack in attack_data:
        formatted.append((
            bear_map[attack["bear_type"]],
            loc_map[attack["location"]],
            attack["created_at"]
        ))

    return formatted


def upload_attacks(attack_data: list[dict], conn: connection) -> None:
    """Returns the number of attacks inserted to the DB."""

    query = """
        INSERT INTO bear_attack
            (bear_type_id, location_id, created_at)
        VALUES %s
        ;
    """

    with conn.cursor() as cur:
        execute_values(cur, query, attack_data)
        
    conn.commit()

if __name__ == "__main__":

    conn = get_db_connection({"DB_NAME": "bear_attacks"})

    print(get_all_bear_types(conn))
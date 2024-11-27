from unittest.mock import MagicMock

from db_functions import get_all_bear_types


"""
1. Does it return the right kind of thing?
2. Does it attempt to interact the database?
3. Does it attempt to use the connection/cursor correctly?
"""

def test_get_all_bear_types_returns_list_of_strings():

    fake_conn = MagicMock()
    fake_cur = fake_conn.cursor() 
    fake_cur.fetchall.return_value = [{"bear_type": "fake bear type"}]

    result = get_all_bear_types(fake_conn)

    assert isinstance(result, list)
    assert all(isinstance(t, str) for t in result)


def test_get_all_bear_types_executes_1_query_only():

    fake_conn = MagicMock()
    fake_cur = fake_conn.cursor()
    fake_cur.fetchall.return_value = [{"bear_type": "fake bear type"}]
    fake_execute = fake_cur.execute

    result = get_all_bear_types(fake_conn)

    assert fake_execute.call_count == 1


def test_get_all_bear_types_executes_select_query():

    fake_conn = MagicMock()
    fake_cur = fake_conn.cursor()
    fake_cur.fetchall.return_value = [{"bear_type": "fake bear type"}]
    fake_execute = fake_cur.execute

    result = get_all_bear_types(fake_conn)

    assert  "SELECT" in fake_execute.mock_calls[0][1][0].upper()
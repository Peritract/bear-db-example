import pytest

import pandas as pd

@pytest.fixture
def test_df_with_nulls():
    return pd.DataFrame(columns=["A", "B"],
                           data=[(1, 1), (1, ".."), ("NOT KNOWN", 1), (1,)])
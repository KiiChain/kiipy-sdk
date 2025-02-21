"""Test coins."""

# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
import pytest

from kiipy.aerial.coins import parse_coins
from kiipy.protos.cosmos.base.v1beta1.coin_pb2 import Coin


@pytest.mark.parametrize(
    "input_coins,expected_result",
    [
        ("", []),
        ("          ", []),
        ("50000ukii", [Coin(amount="50000", denom="ukii")]),
        (
            "50000ukii,     200foobar",
            [
                Coin(amount="50000", denom="ukii"),
                Coin(amount="200", denom="foobar"),
            ],
        ),
        (
            "500ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B",
            [
                Coin(
                    amount="500",
                    denom="ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B",
                )
            ],
        ),
        (
            "500ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B, 50000ukii",
            [
                Coin(
                    amount="500",
                    denom="ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B",
                ),
                Coin(amount="50000", denom="ukii"),
            ],
        ),
    ],
)
def test_parsing_coins(input_coins, expected_result):
    """Test parsing coins."""
    assert parse_coins(input_coins) == expected_result

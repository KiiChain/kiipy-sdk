# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
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

"""Staking example test."""

import subprocess  # nosec
from pathlib import Path

import pytest

from tests.integration.test_contract import MAX_FLAKY_RERUNS, RERUNS_DELAY


ROOT_DIR = Path(__file__).parent.parent.parent.parent


@pytest.mark.flaky(reruns=MAX_FLAKY_RERUNS, reruns_delay=RERUNS_DELAY)
def test_balance_example():
    """Test examples/aerial_kii_get_balance.py"""
    proc = subprocess.run(  # nosec
        f"python {ROOT_DIR}/examples/aerial_kii_get_balance.py",
        shell=True,
        check=True,
        capture_output=True,
        timeout=100,
    )

    expected_address = "kii1pyt53arxkg5t4aww892esskltrf54mg88va98y"
    expected_balance = 200000000

    assert (
        f"{expected_address} has a balance of {expected_balance} ukii.".encode()
        in proc.stdout
    ), proc.stdout

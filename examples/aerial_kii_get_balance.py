"""Example of aerial get balance."""

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
from kiipy.aerial.client import LedgerClient, NetworkConfig


def main():
    """Run main."""
    # Connecting to the Kii testnet
    ledger_client = LedgerClient(NetworkConfig.kii_testnet())

    wallet_address = "kii1pyt53arxkg5t4aww892esskltrf54mg88va98y"

    # Get balances, we expect 0 balance since the wallet is newly-created
    print(f"Getting wallet balances for {wallet_address}...")
    denom = "tkii"
    balance = ledger_client.query_bank_balance(wallet_address, denom=denom)
    print(f"{wallet_address} has a balance of {balance} {denom}.")


if __name__ == "__main__":
    main()

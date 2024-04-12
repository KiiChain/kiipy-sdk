"""Example of aerial send tokens using the kii testnet."""

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

import os

from kiipy.aerial.client import LedgerClient, NetworkConfig
from kiipy.aerial.wallet import LocalWallet
from kiipy.crypto.keypairs import PrivateKey


def _get_from_environment(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise KeyError(f"Environment variable {key} not found!")

    return value


def main():
    """Run main."""
    # Get wallet key from the environment variables
    sender_key = _get_from_environment("WALLET_PRIV")
    receiver = _get_from_environment("RECEIVER_ADDR")

    # Connect client to testnet
    ledger = LedgerClient(NetworkConfig.kii_testnet())

    # Connect wallet
    wallet = LocalWallet(PrivateKey(sender_key), prefix="kii")

    # Get balances
    print(
        f"Sender   Address: {wallet.address()} Balance: {ledger.query_bank_balance(wallet.address())}"
    )
    print(
        f"Receiver Address: {receiver} Balance: {ledger.query_bank_balance(receiver)}"
    )

    # Send tokens
    tx = ledger.send_tokens(
        receiver, 1, "tkii", wallet, gas_limit=100000, memo="test send"
    )

    print(f"TX {tx.tx_hash} waiting to complete...")
    tx.wait_to_complete()
    print(f"TX {tx.tx_hash} waiting to complete...done")

    # Get balances
    print(
        f"Sender   Address: {wallet.address()} Balance: {ledger.query_bank_balance(wallet.address())}"
    )
    print(
        f"Receiver Address: {receiver} Balance: {ledger.query_bank_balance(receiver)}"
    )


if __name__ == "__main__":
    main()

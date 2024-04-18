"""Example of aerial staking."""

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

from kiipy.aerial.client import LedgerClient, Validator
from kiipy.aerial.config import NetworkConfig
from kiipy.aerial.tx_helpers import SubmittedTx
from kiipy.aerial.wallet import LocalWallet
from kiipy.crypto.keypairs import PrivateKey


def _wait_for_tx(operation: str, tx: SubmittedTx):
    print(f"Waiting for {operation} to complete... (tx: {tx.tx_hash})")
    tx.wait_to_complete()
    print(f"Waiting for {operation} to complete... done")


def _get_from_environment(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise KeyError(f"Environment variable {key} not found!")

    return value


def _get_staking_info(ledger: LedgerClient, address: str):
    return ledger.query_staking_summary(address)


def _print_staking_info(ledger: LedgerClient, address: str):
    summary = _get_staking_info(ledger, address)
    print("==== Staked tokens ====")
    for pos in summary.current_positions:
        print(
            f"Validator: {pos.validator} Staked Amount: {pos.amount} Reward: {pos.reward}"
        )

    print("=== Unbonded tokens ===")
    for pos in summary.unbonding_positions:
        print(f"Validator: {pos.validator} Staked Amount: {pos.amount}")

    print("======= Summary =======")
    print(
        f"Staked: {summary.total_staked} Unbonding: {summary.total_unbonding} Rewards: {summary.total_rewards}"
    )


def _print_staking_summary(ledger: LedgerClient, address: str):
    summary = ledger.query_staking_summary(address)
    print(summary)
    print(
        f"Summary: Staked: {summary.total_staked} Unbonding: {summary.total_unbonding} Rewards: {summary.total_rewards}"
    )


def main():
    """Run main."""
    # Get wallet key from the environment variables
    wallet_key = _get_from_environment("WALLET_PRIV")

    # Connect client to testnet
    ledger = LedgerClient(NetworkConfig.kii_testnet())

    # Connect wallet
    wallet = LocalWallet(PrivateKey(wallet_key), prefix="kii")

    balances = ledger.query_bank_all_balances(wallet.address())
    if balances:
        for balance in balances:
            print(
                f"{wallet.address()} has a balance of {balance.amount}{balance.denom}."
            )
    else:
        print(f"{wallet.address()} is empty.")

    # get the get all the active validators on the network
    validators = ledger.query_validators()
    kii_aventador: Validator = None
    kii_pagani: Validator = None

    # choose two of the kii validators to delegate to
    for v in validators:
        if v.moniker == "KiiAventador":
            kii_aventador = v
        elif v.moniker == "KIIPagani":
            kii_pagani = v

    # get current staking summary
    _print_staking_info(ledger, wallet.address())

    # delegate some tokens to kii aventador
    tx = ledger.delegate_tokens(kii_aventador.address, 10, wallet)
    _wait_for_tx("delegate", tx)
    _print_staking_info(ledger, wallet.address())

    # redelegate the tokens to another validator
    tx = ledger.redelegate_tokens(kii_aventador.address, kii_pagani.address, 5, wallet)
    _wait_for_tx("redelegate", tx)
    _print_staking_info(ledger, wallet.address())

    # undelegate the tokens from the first validator
    tx = ledger.undelegate_tokens(kii_aventador.address, 5, wallet)
    _wait_for_tx("undelegate", tx)
    _print_staking_info(ledger, wallet.address())

    # finally, lets collect up all the rewards we have earned so far
    claimed = False
    summary = _get_staking_info(ledger, wallet.address())
    for position in summary.current_positions:
        if position.reward > 0:
            claimed = True

            tx = ledger.claim_rewards(position.validator, wallet)
            _wait_for_tx(f"claim from {str(position.validator)}", tx)

    if claimed:
        _print_staking_info(ledger, wallet.address())


if __name__ == "__main__":
    main()

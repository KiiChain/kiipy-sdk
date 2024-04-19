"""CLI commands to show example of basic transactions in the Kii Blockchain."""

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
from pathlib import Path
from typing import Any, List, Optional

import click
from prettytable import DOUBLE_BORDER, PrettyTable

from kiipy.aerial.client import LedgerClient, NetworkConfig
from kiipy.aerial.tx_helpers import SubmittedTx
from kiipy.aerial.wallet import LocalWallet
from kiipy.crypto.keypairs import PrivateKey


PUBKEY_FILE = "keys/NAME.pub"
PRIVKEY_FILE = "keys/NAME.priv"


@click.group()
def kii():
    """Commands to interact with the Kii blockchain."""
    pass


def _connect() -> LedgerClient:
    return LedgerClient(NetworkConfig.kii_testnet())


def _connect_wallet(priv_key: str) -> LocalWallet:
    return LocalWallet(PrivateKey(priv_key))


def _save_key(filename: str, name: str, key: str) -> None:
    file = Path(filename)
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(key)
    print(f"Saved {name} to {filename}.")


def _load_key(filename: str, name: str) -> str:
    print(f"Reading {name} from {filename}")
    return Path(filename).read_text()


def _print_table(title: str, headers: List[str], data: List[List[Any]]) -> None:
    table = PrettyTable(title=title, field_names=headers)
    table.add_rows(data)
    table.set_style(DOUBLE_BORDER)
    print(table)


def _wait_tx(operation: str, tx: SubmittedTx) -> None:
    print(f"Waiting for {operation} operation to complete... (tx: {tx.tx_hash})")
    tx.wait_to_complete()
    print(f"Waiting for {operation} operation to complete... done!")


@kii.command()
@click.argument("name")
def create_wallet(name: str) -> None:
    """Create a wallet. Keys will be saved at keys/NAME.pub and keys/NAME.priv."""
    print(f"Creating new wallet '{name}'...")
    wallet = LocalWallet.generate()
    print(f"Created {name} with address {wallet.address().data}")

    _save_key(
        PUBKEY_FILE.replace("NAME", name), "public key", wallet.public_key().public_key
    )
    _save_key(
        PRIVKEY_FILE.replace("NAME", name), "private key", wallet.signer().private_key
    )


@kii.command()
@click.argument("address")
def get_all_balances(address: str) -> None:
    """Get the wallet balance of ADDRESS in all denominations."""
    print(f"Getting wallet balances for {address}...")
    client = _connect()
    balances = client.query_bank_all_balances(address)

    if not balances:
        print(f"Wallet {address} is empty!")
        return

    data: List[List[Any]] = []
    for b in balances:
        data.append(
            [
                b.amount,
                b.denom,
            ]
        )
    _print_table(title="Balance", headers=["Amount", "Denom"], data=data)


@kii.command()
@click.argument("address")
@click.argument("denom")
def get_balance(address: str, denom: str) -> None:
    """Get the wallet balance of ADDRESS for DENOM."""
    print(f"Getting {denom} wallet balance for {address}...")
    client = _connect()
    amount = client.query_bank_balance(address, denom=denom)
    print(f"Wallet has {amount} {denom}.")


@kii.command()
def get_validators() -> None:
    """Get all the validators in the blockchain."""
    print("Getting validators...")
    client = _connect()
    validators = client.query_validators()

    if not validators:
        print(f"There are no validators for {client.network_config.chain_id}!")
        return

    data: List[List[Any]] = []
    for v in validators:
        data.append(
            [
                v.address,
                v.moniker,
                v.status,
                v.tokens,
            ]
        )
    _print_table(
        title=f"{client.network_config.chain_id} Validators",
        headers=["Address", "Moniker", "Status", "Tokens"],
        data=data,
    )


@kii.command()
@click.argument("address")
def get_stakes(address: str) -> None:
    """Query the staked tokens information for wallet identified by ADDRESS."""
    print(f"Getting staking information for {address}...")

    # get staking summary
    client = _connect()
    summary = client.query_staking_summary(address)

    # print bonded tokens
    data: List[List[Any]] = []
    for pos in summary.current_positions:
        data.append(
            [
                pos.validator,
                pos.amount,
                pos.reward,
            ]
        )
    _print_table(
        title="Bonded Tokens",
        headers=["Validator", "Staked Amount", "Reward"],
        data=data,
    )

    # print unbonded tokens
    data: List[List[Any]] = []
    for pos in summary.unbonding_positions:
        data.append(
            [
                pos.validator,
                pos.amount,
            ]
        )
    _print_table(
        title="Unbonded Tokens", headers=["Validator", "Staked Amount"], data=data
    )

    # output summary
    print(
        f"Staked: {summary.total_staked} Unbonding: {summary.total_unbonding} Rewards: {summary.total_rewards}"
    )


@kii.command()
@click.argument("tx_hash")
def get_tx(tx_hash: str) -> None:
    """Query a transaction given its TX_HASH."""
    print(f"Getting details for tx {tx_hash}...")
    client = _connect()
    tx = client.query_tx(tx_hash)

    print(f"Hash: {tx.hash}")
    print(f"Height: {tx.height}")
    print(f"Status: {'Success' if tx.code == 0 else 'Failed'}")
    print(f"Gas Wanted: {tx.gas_wanted}")
    print(f"Gas Used: {tx.gas_used}")
    if tx.timestamp:
        print(f"Timestamp: {tx.timestamp}")
    print(f"Link: https://app.kiiglobal.io/kii/tx/{tx_hash}")


@kii.command()
@click.argument("priv_key_path", type=click.Path())
@click.argument("receiver_addr")
@click.argument("amount")
@click.option(
    "--denom", default="tkii", help="token denomination to be sent; DEFAULT: 'tkii'"
)
@click.option("--memo", help="transaction memo")
def send(
    priv_key_path: click.Path,
    receiver_addr: str,
    amount: int,
    denom: Optional[str],
    memo: Optional[str],
) -> None:
    """Send AMOUNT tokens from the sender wallet identified by the key in PRIV_KEY_PATH to the specified RECEIVER_ADDR.

    If you do not have an existing wallet, see create-wallet command.
    """  # noqa
    print(f"Sending {amount} {denom} to {receiver_addr}...")
    # connect to wallet
    priv_key = _load_key(priv_key_path, "private key")
    wallet = _connect_wallet(priv_key)
    print(f"Connected to {wallet.address()}.")

    # send tokens
    client = _connect()
    print(f"Sending {amount} {denom} from {wallet.address()} to {receiver_addr}...")
    tx = client.send_tokens(receiver_addr, amount, denom, wallet, memo=memo)
    _wait_tx("send", tx)


@kii.command()
@click.argument("priv_key_path", type=click.Path())
@click.argument("validator_addr")
@click.argument("amount")
@click.option("--memo", help="transaction memo")
def delegate(
    priv_key_path: str, validator_addr: str, amount: int, memo: Optional[str] = None
) -> None:
    """Delegate AMOUNT tokens from the sender wallet identified by the key in PRIV_KEY_PATH to the specified VALIDATOR_ADDR.

    If you do not have an existing wallet, see create-wallet command.
    """  # noqa
    print(f"Delegating to {validator_addr}...")
    # connect to wallet
    priv_key = _load_key(priv_key_path, "private key")
    wallet = _connect_wallet(priv_key)
    print(f"Connected to {wallet.address()}.")

    # delegate tokens
    client = _connect()
    print(
        f"Delegating {amount} {client.network_config.staking_denomination} from {wallet.address()} to {validator_addr}..."
    )
    tx = client.delegate_tokens(validator_addr, amount, wallet, memo=memo)
    _wait_tx("delegate", tx)


@kii.command()
@click.argument("priv_key_path", type=click.Path())
@click.argument("src_validator_addr")
@click.argument("dst_validator_addr")
@click.argument("amount")
@click.option("--memo", help="transaction memo")
def redelegate(
    priv_key_path: str,
    src_validator_addr: str,
    dst_validator_addr: str,
    amount: int,
    memo: Optional[str] = None,
) -> None:
    """Redelegate AMOUNT tokens from SRC_VALIDATOR_ADDR to DST_VALIDATOR_ADDR by the sender wallet identified by the key in PRIV_KEY_PATH.

    If you do not have an existing wallet, see create-wallet command.
    """  # noqa
    print(f"Redelegating to {src_validator_addr} to {dst_validator_addr}...")

    # connect to wallet
    priv_key = _load_key(priv_key_path, "private key")
    wallet = _connect_wallet(priv_key)
    print(f"Connected to {wallet.address()}.")

    # redelegate tokens
    client = _connect()
    print(
        f"Redelegating {amount} {client.network_config.staking_denomination} from {src_validator_addr} to {dst_validator_addr}..."
    )
    tx = client.redelegate_tokens(
        src_validator_addr, dst_validator_addr, amount, wallet, memo=memo
    )
    _wait_tx("redelegate", tx)


@kii.command()
@click.argument("priv_key_path", type=click.Path())
@click.argument("validator_addr")
@click.argument("amount")
@click.option("--memo", help="transaction memo")
def undelegate(
    priv_key_path: str, validator_addr: str, amount: int, memo: Optional[str] = None
) -> None:
    """Undelegate AMOUNT tokens from VALIDATOR_ADDR to the sender wallet identified by the key in PRIV_KEY_PATH.

    If you do not have an existing wallet, see create-wallet command.
    """  # noqa
    print(f"Undelegating from {validator_addr}...")
    # connect to wallet
    priv_key = _load_key(priv_key_path, "private key")
    wallet = _connect_wallet(priv_key)
    print(f"Connected to {wallet.address()}.")

    # undelegate tokens
    client = _connect()
    print(
        f"Undelegating {amount} {client.network_config.staking_denomination} from {validator_addr}..."
    )
    tx = client.undelegate_tokens(validator_addr, amount, wallet, memo=memo)
    _wait_tx("undelegate", tx)


if __name__ == "__main__":
    kii(max_content_width=150)

# Examples

In this directory, you can find examples of basic ledger interactions using `kiipy`, such as transferring tokens, staking, and deploying.

## CLI App

The CLI App can be used to perform basic operations, including querying transactions and creating wallets.

Some operations such as `send` and `delegate` require a Kii wallet. If you do not have a Kii wallet yet, use the `create-wallet` command to create one. The new keys will be saved in the `keys/` directory.

Newly-created wallets are empty. Details on how to request tokens from the Kii Testnet faucet can be found in this [guide](https://docs.kiiglobal.io/docs/validate-the-network/run-a-validator-full-node/testnet-faucet).

Full usage of the CLI app can be viewed with `python cli.py --help`.

```bash
$ python cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  Commands to interact with the Kii blockchain.

Options:
  --help  Show this message and exit.

Commands:
  create-wallet     Create a wallet.
  delegate          Delegate AMOUNT tokens from the sender wallet identified by the key in PRIV_KEY_PATH to the specified VALIDATOR_ADDR.
  get-all-balances  Get the wallet balance of ADDRESS in all denominations.
  get-balance       Get the wallet balance of ADDRESS for DENOM.
  get-stakes        Query the staked tokens information for wallet identified by ADDRESS.
  get-tx            Query a transaction given its TX_HASH.
  get-validators    Get all the validators in the blockchain.
  redelegate        Redelegate AMOUNT tokens from SRC_VALIDATOR_ADDR to DST_VALIDATOR_ADDR by the sender wallet identified by the key in...
  send              Send AMOUNT tokens from the sender wallet identified by the key in PRIV_KEY_PATH to the specified RECEIVER_ADDR.
  undelegate        Undelegate AMOUNT tokens from VALIDATOR_ADDR to the sender wallet identified by the key in PRIV_KEY_PATH.
```

`--help` is also available for each command.

```bash
$ python cli.py delegate --help
Usage: cli.py delegate [OPTIONS] PRIV_KEY_PATH VALIDATOR_ADDR AMOUNT

  Delegate AMOUNT tokens from the sender wallet identified by the key in PRIV_KEY_PATH to the specified VALIDATOR_ADDR.

  If you do not have an existing wallet, see create-wallet command.

Options:
  --memo TEXT  transaction memo
  --help       Show this message and exit.
```

## Sample scripts

Sample scripts that show usage of basic operations such as sending tokens, getting wallet balance, and staking are also available.

### Environment Variables

Running the sample scripts require you to set the following environment variables in your machine:
- `WALLET_PRIVATE`: Private key of the main wallet you're using to connect to the blockchain.
- `WALLET_ADDR`: Address of the main wallet you're using to connect to the blockchain.
- `RECEIVER_ADDR`: Address of the receiver wallet used when doing operations that involve sending tokens.

To set the environment variables, run the following commands:
```bash
export WALLET_PRIV="<wallet_private_key>"
export WALLET_ADDR="<wallet_address>"
export RECEIVER_ADDR="<receiver_address>"
```

To check if the environment variables are present, run the following commands:
```bash
printenv WALLET_PRIV
printenv WALLET_ADDR
printenv RECEIVER_ADDR
```

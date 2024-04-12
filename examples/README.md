# Examples

In this directory, you can find examples of basic ledger interactions using `kiipy`, such as transferring tokens, staking, and deploying.

## Environment Variables

Running the scripts require you to set the following environment variables in your machine:
- `WALLET_PRIVATE`: Private key of the main wallet you're using to connect to the blockchain.
- `WALLET_ADDR`: Address of the main wallet you're using to connect to the blockchain.
- `RECEIVER_ADDR`: Address of the receiver wallet used when doing operations that involve sending tokens.

To set the environment variables, run the following commands:
```
export WALLET_PRIV="<wallet_private_key>"
export WALLET_ADDR="<wallet_address>"
export RECEIVER_ADDR="<receiver_address>"
```

To check if the environment variables are present, run the following commands:
```
printenv WALLET_PRIV
printenv WALLET_ADDR
printenv RECEIVER_ADDR
```

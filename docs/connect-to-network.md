To start interacting with a blockchain, you first need to establish a connection to a network node. You can use `LedgerClient` as a client object which takes a `NetworkConfig` as an argument.

```python
from kiipy.aerial.client import LedgerClient, NetworkConfig

ledger_client = LedgerClient(NetworkConfig.kii_testnet())
```

For convenience, some networks' configurations are provided automatically. For example, `NetworkConfig.kii_testnet()` is the configuration for the Kii ledger. If you want to interact with other chains, you can customise `NetworkConfig` as shown in the example below:

```python
cfg NetworkConfig(
    chain_id="kiiventador",
    url="rest+https://a.testnet.kiivalidator.com/",
    fee_minimum_gas_price=0,
    fee_denomination="tkii",
    staking_denomination="tkii",
    faucet_url=None,
)

ledger_client = LedgerClient(cfg)
```

A full list of chain identifiers, denominations and end-points can be found at the Cosmos [chain registry](https://github.com/cosmos/chain-registry/).

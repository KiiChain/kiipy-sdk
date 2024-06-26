<h1 align="center">
    <b>KiiPy</b>
</h1>

<p align="center">
A python library for interacting with KiiChain and other Cosmos-based blockchain networks
</p>

[comment]: # (TODO: Add proper badges here)

<p align="center">
  <!-- <a href="https://pypi.org/project/kiipy/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/kiipy">
  </a>
  <a href="https://pypi.org/project/kiipy/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/kiipy">
  </a>
  <a href="https://github.com/KiiBlockchain/kiipy/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/pypi/l/kiipy">
  </a>
  <br />
  <a>
    <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/kiipy">
  </a> -->
  <a href="https://github.com/KiiBlockchain/kiipy/actions/workflows/workflow.yml">
    <img alt="Sanity checks and tests" src="https://github.com/KiiBlockchain/kiipy/actions/workflows/workflow.yml/badge.svg">
  </a>
  <!-- <a href="https://pypi.org/project/kiipy/">
    <img alt="Download per Month" src="https://img.shields.io/pypi/dm/kiipy">
  </a> -->
</p>

*This project has been forked from [Fetch AI's CosmPy](https://github.com/fetchai/cosmpy).*

## DEVELOPMENT NOTES

**This project is still under development.**

Details on how to setup the dev environment can be found in the [development guidelines][developing]. Using poetry virtual environment is highly encouraged to ensure seamless development.

Notes:
- Items that need to be looked into are marked as `TODO:` in the code and docs.
- Workflows are failing due to usage limits. It's advisable to fix this to ensure code quality. Current workaround is to make sure to run corresponding checks and tests locally.


## Installation

### Install with pip

```bash
pip install kiipy
```

### Install from source code

1. Clone the repository
```
git clone https://github.com/KiiBlockchain/kiipy.git
cd kiipy
```

2. Install the required dependencies
```
poetry install
```

3. Open the virtual environment
```
poetry shell
```

## Getting Started

Below is a simple example for querying an account's balances:

```python
from kiipy.aerial.client import LedgerClient, NetworkConfig

# connect to Kii test network using default parameters
ledger_client = LedgerClient(NetworkConfig.kii_testnet())

alice: str = 'kii1pyt53arxkg5t4aww892esskltrf54mg88va98y'
balances = ledger_client.query_bank_all_balances(alice)

# show all coin balances
for coin in balances:
  print(f'{coin.amount}{coin.denom}')
```

## Documentation

[comment]: # (TODO: Update this and other occurence with proper docs url)
The full documentation can be found [here](https://docs.kiiglobal.io/kiipy/).

## Examples

Under the `examples` directory, you can find examples of basic ledger interactions using `kiipy`, such as transferring tokens, staking, and deploying.

## Contributing

All contributions are very welcome! Remember, contribution is not only PRs and code, but any help with docs or helping other developers solve their issues are very appreciated!

Read below to learn how you can take part in the KiiPy project.

### Code of Conduct

Please be sure to read and follow our [Code of Conduct][coc]. By participating, you are expected to uphold this code.

### Contribution Guidelines

Read our [contribution guidelines][contributing] to learn about our issue and pull request submission processes, coding rules, and more.

### Development Guidelines

Read our [development guidelines][developing] to learn about the development processes and workflows.

### Issues, Questions and Discussions

We use [GitHub Issues][issues] for tracking requests and bugs, and [GitHub Discussions][discussion] for general questions and discussion.

## License

The KiiPy project is licensed under [Apache License 2.0][license].

[contributing]: https://github.com/KiiBlockchain/kiipy/blob/main/CONTRIBUTING.md
[developing]: https://github.com/KiiBlockchain/kiipy/blob/main/DEVELOPING.md
[coc]: https://github.com/KiiBlockchain/kiipy/blob/main/CODE_OF_CONDUCT.md
[discussion]: https://github.com/KiiBlockchain/kiipy/discussions
[issues]: https://github.com/KiiBlockchain/kiipy/issues
[license]: https://github.com/KiiBlockchain/kiipy/blob/main/LICENSE

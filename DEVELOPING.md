# Development Guidelines

- [Getting the Source](#get)
- [Setting up a New Development Environment](#setup)
- [Development](#dev)
  - [General code quality checks](#general)
  - [Updating documentation](#docs)
  - [Updating API documentation](#api)
  - [Updating dependencies](#deps)
  - [Tests](#tests)
  - [Miscellaneous checks](#misc)
- [Generating python types from Cosmos SDK protobuf schemas](#protobuf)
- [Contributing](#contributing)

## <a name="get"></a> Getting the Source

1. Fork the [repository][repo].
2. Clone your fork of the repository:

   ``` shell
   git clone git@github.com:<github username>/kiipy.git
   ```

3. Define an `upstream` remote pointing back to the main KiiPy repository:

   ``` shell
   git remote add upstream https://github.com/KiiBlockchain/kiipy.git
   ```

## <a name="setup"></a> Setting up a New Development Environment

1. Ensure you have Python (version `3.9` or `3.10`) and [`poetry`][poetry].

2. ``` shell
   make new-env
   ```

   This will create a new virtual environment using poetry with the project and all the development dependencies installed.

   > We use <a href="https://python-poetry.org" target="_blank">poetry</a> to manage dependencies. All python specific dependencies are specified in `pyproject.toml` and installed with the library. 
   > 
   > You can have more control on the installed dependencies by leveraging poetry's features.

3. ``` shell
   poetry shell
   ```

    To enter the virtual environment.

To [update the protobuf schemas](#protobuf) and generate their associated python types, you will need [Google Protocol Buffers][protobuf].

## <a name="dev"></a>Development

### <a name="general"></a>General code quality checks

To run general code quality checkers, formatters and linters:

- ``` shell
   make lint
  ```

  Automatically formats your code and sorts your imports, checks your code's quality and scans for any unused code.

- ``` shell
   make mypy
  ```

  Statically checks the correctness of the types.

- ``` shell
   make pylint
  ```

  Analyses the quality of your code.

- ``` shell
   make security
  ```

  Checks the code for known vulnerabilities and common security issues.

- ``` shell
   make clean
  ```

  Cleans your development environment and deletes temporary files and directories.

To run all available checks and tests:

- ``` shell
   ./scripts/run-checks.sh
  ```

### <a name="docs"></a>Updating documentation

We use [`mkdocs`][mkdocs] and [`material-for-mkdocs`][material] for static documentation pages. To make changes to the documentation:

- ``` shell
   make docs-live
  ```
  <!-- markdown-link-check-disable -->
  This starts a live-reloading docs server on localhost which you can access by going to <http://127.0.0.1:8000/> in your browser. Making changes to the documentation automatically reloads this page, showing you the latest changes.
  <!-- markdown-link-check-enable -->
  To create a new documentation page, add a markdown file under `/docs/` and add a reference to this page in `mkdocs.yml` under `nav`.

### <a name="api"></a>Updating API documentation

If you've made changes to the core `kiipy` package that affects the public API:

- ``` shell
   make generate-api-docs
  ```

  This regenerates the API docs. If pages are added/deleted, or there are changes in their structure, these need to be reflected manually in the `nav` section of `mkdocs.yaml`.

### <a name="deps"></a>Updating dependencies

We use [`poetry`][poetry] and `pyproject.toml` to manage the project's dependencies.

If you've made any changes to the dependencies (e.g. added/removed dependencies, or updated package version requirements):

- ``` shell
   poetry lock
  ```

  This re-locks the dependencies. Ensure that the `poetry.lock` file is pushed into the repository (by default it is).

- ``` shell
   make liccheck
  ```

  Checks that the licence for the library is correct, taking into account the licences for all dependencies, their dependencies and so forth.

### <a name="tests"></a>Tests

To test the project, we use `pytest`. To run the tests:

- ``` shell
   make test
  ```

  Runs all the tests.

- ``` shell
   make unit-test
   ```

  Runs all unit tests.

- ``` shell
   make integration-test
  ```

  Runs all integration tests.

- ``` shell
   make coverage-report
  ```

  Produces a coverage report (you should run tests using one of the above commands first).

### <a name="misc"></a>Miscellaneous checks

- ``` shell
   make copyright-check
  ```

  Checks that all files have the correct copyright header (where applicable).

## <a name="protobuf"></a> Generating python types from Cosmos SDK protobuf schemas

This library uses python types which are generated (using [Google's Protocol Buffers](https://developers.google.com/protocol-buffers/) compiler) from protocol buffer schemas in the [Cosmos SDK](https://github.com/cosmos/cosmos-sdk) and [WasmD](https://github.com/CosmWasm/wasmd).

When updating the Cosmos-SDK version that is supported by this library (see the version currently used under `COSMOS_SDK_VERSION` in [Makefile](Makefile)), you will need to fetch its corresponding protobuf schemas and generate their associated python types, replacing the existing ones.

Cosmos-SDK now hosts its proto files in [BSR](https://buf.build/cosmos/cosmos-sdk). To fetch the protobuf schemas, you will need `buf`. Details on how to can be found [here](https://buf.build/docs/installation).

To generate python types from Cosmos-SDK protobuf schemas, you will need [Google Protocol Buffers](https://developers.google.com/protocol-buffers/) compiler. A guide on how to install it can be found [here](https://fetchai.github.io/oef-sdk-python/user/install.html#protobuf-compiler).

> Note: This process has to be done only once when the Cosmos-SDK version supported by this library is changed.

- To regenerate the protobuf schema files, run the following:

  ```bash
  make proto
  ```

>Note: For this library to be functional, only python types generated from protobuf schemas are required, not the schema files themselves.
> The schema files are fetched on-demand only to enable the generation of python types.
> Therefore, the schema files are intentionally stored as **local** files and are **NOT** checked in to this repository to minimise its filesystem footprint.

[comment]: # (TODO: Add info on how to setup a local Kii node)

## <a name="contributing"></a>Contributing

For instructions on how to contribute to the project (e.g. creating Pull Requests, commit message convention, etc), see the [contributing guide][contributing guide].

[protobuf]: https://developers.google.com/protocol-buffers/
[ipfs]: https://docs.ipfs.tech/install/
[go]: https://golang.org/doc/install
[golines]: https://github.com/segmentio/golines
[golangci-lint]: https://golangci-lint.run
[mkdocs]: https://www.mkdocs.org
[material]: https://squidfunk.github.io/mkdocs-material/
[poetry]: https://python-poetry.org
[contributing guide]: https://github.com/KiiBlockchain/kiipy/blob/main/CONTRIBUTING.md
[release process]: https://github.com/KiiBlockchain/kiipy/blob/main/scripts/RELEASE_PROCESS.md
[repo]: https://github.com/KiiBlockchain/kiipy

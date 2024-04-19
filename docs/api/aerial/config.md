<a id="kiipy.aerial.config"></a>

# kiipy.aerial.config

Network configurations.

<a id="kiipy.aerial.config.NetworkConfigError"></a>

## NetworkConfigError Objects

```python
class NetworkConfigError(RuntimeError)
```

Network config error.

**Arguments**:

- `RuntimeError`: Runtime error

<a id="kiipy.aerial.config.NetworkConfig"></a>

## NetworkConfig Objects

```python
@dataclass
class NetworkConfig()
```

Network configurations.

**Raises**:

- `NetworkConfigError`: Network config error
- `RuntimeError`: Runtime error

<a id="kiipy.aerial.config.NetworkConfig.validate"></a>

#### validate

```python
def validate()
```

Validate the network configuration.

**Raises**:

- `NetworkConfigError`: Network config error

<a id="kiipy.aerial.config.NetworkConfig.kii_testnet"></a>

#### kii`_`testnet

```python
@classmethod
def kii_testnet(cls) -> "NetworkConfig"
```

Kii testnet.

**Returns**:

Network configuration


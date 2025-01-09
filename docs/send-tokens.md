Once you have your [`wallet`](wallets-and-keys.md) configured, you can send transactions to the network. The `LedgerClient` object provides useful utilities to do common operations. The following example shows how to send `10` `ukii` to another address:

```python
destination_address = 'kii1pyt53arxkg5t4aww892esskltrf54mg88va98y'

tx = ledger_client.send_tokens(destination_address, 10, "ukii", wallet)

# block until the transaction has been successful or failed
tx.wait_to_complete()
```

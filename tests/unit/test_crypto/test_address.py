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

"""Tests for the Address module of the Crypto Package."""

import json
import unittest

from kiipy.common.utils import json_encode
from kiipy.crypto.address import Address
from kiipy.crypto.keypairs import PublicKey


class AddressTestCase(unittest.TestCase):
    """Test case of KeyPair module."""

    def test_create_from_public_key(self):
        """Test create Address from public key with positive result."""
        pk = PublicKey(
            b"\x02\xae3N\xcd\xb1\xb3\xa2\x81\x88\x13U\x81r\xa0\xd2L\x06I\xe9\xd4\xe0\xd1\x1cWC\x02\x15\xafD\x06\xa4\xd3"
        )
        address = Address(pk)
        self.assertEqual(str(address), "kii1qmfqk9tqu6ne9zf54srmhl4pzqudlqate7230z")
        self.assertEqual(address, "kii1qmfqk9tqu6ne9zf54srmhl4pzqudlqate7230z")
        self.assertEqual(
            bytes(address),
            b"\x06\xd2\x0b\x15`\xe6\xa7\x92\x894\xac\x07\xbb\xfe\xa1\x108\xdf\x83\xab",
        )

    def test_create_from_address(self):
        """Test create Address from another Address with positive result."""
        addr1 = Address(
            b"\x06\xd2\x0b\x15`\xe6\xa7\x92\x894\xac\x07\xbb\xfe\xa1\x108\xdf\x83\xab"
        )
        addr2 = Address(addr1)
        self.assertEqual(str(addr1), str(addr2))

    def test_create_from_bytes(self):
        """Test create Address from bytes with positive result."""
        address = Address(
            b"\x06\xd2\x0b\x15`\xe6\xa7\x92\x894\xac\x07\xbb\xfe\xa1\x108\xdf\x83\xab"
        )
        self.assertEqual(str(address), "kii1qmfqk9tqu6ne9zf54srmhl4pzqudlqate7230z")

    def test_create_from_str(self):
        """Test create Address from string with positive result."""
        address = Address("kii1qmfqk9tqu6ne9zf54srmhl4pzqudlqate7230z")
        self.assertEqual(
            bytes(address),
            b"\x06\xd2\x0b\x15`\xe6\xa7\x92\x894\xac\x07\xbb\xfe\xa1\x108\xdf\x83\xab",
        )

    def test_invalid_byte_length_address(self):
        """Test create Address from bytes with negative result."""
        with self.assertRaises(RuntimeError):
            Address(b"wrong byte len")

    def test_invalid_bech32_address(self):
        """Test create Address from str with negative result."""
        with self.assertRaises(RuntimeError):
            Address("certainly not an address")

    def test_address_from_address_with_custom_prefix(self):
        """Test create an Address from another but with a custom prefix."""
        address = Address("kii1qmfqk9tqu6ne9zf54srmhl4pzqudlqate7230z")
        val_address = Address(address, prefix="kiivaloper")
        self.assertEqual(
            str(val_address), "kiivaloper1qmfqk9tqu6ne9zf54srmhl4pzqudlqatvg3zwk"
        )

    def test_string_compatible_address(self):
        """Test address can be dumped to json using json_encode utility method."""
        address = Address("kii1qmfqk9tqu6ne9zf54srmhl4pzqudlqate7230z")
        json_data = json_encode({"address": address})
        restored_address = Address(json.loads(json_data)["address"])
        assert restored_address == address

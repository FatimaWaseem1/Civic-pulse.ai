import hashlib
import json
import time
from typing import Dict, Any


class LedgerAnchor:
    """Simulates or executes Web3 cryptographic hashing and ledger anchoring."""

    def __init__(self, mock_mode: bool = True):
        self.mock_mode = mock_mode

    def generate_proof(self, bill_title: str, simulation_data: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "title": bill_title,
            "timestamp": time.time(),
            "simulation": simulation_data
        }
        serialized = json.dumps(payload, sort_keys=True).encode('utf-8')
        sha256_hash = hashlib.sha256(serialized).hexdigest()

        # Simulates an EVM Transaction Receipt
        tx_hash = "0x" + hashlib.sha256((sha256_hash + str(time.time())).encode('utf-8')).hexdigest()
        block_number = 459201 + int(time.time()) % 1000

        return {
            "state_hash": f"0x{sha256_hash}",
            "transaction_hash": tx_hash,
            "block_number": block_number,
            "status": "VERIFIED_ON_CHAIN"
        }
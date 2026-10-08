"""Phase 4 adapter-only: 1 canned tx."""
class BtcAdapter:
    chain = "BTC"
    def get_transactions(self, address): return [{"canned": True}]
    def get_address_labels(self, address): return []
    def get_token_transfers(self, address): return []
    def get_block(self, height): return {"height": height}

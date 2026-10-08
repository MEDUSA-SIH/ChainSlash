"""Phase 4 BNB live adapter (mirror ETH)."""
class BnbAdapter:
    chain = "BNB"
    def get_transactions(self, address): return []
    def get_address_labels(self, address): return []
    def get_token_transfers(self, address): return []
    def get_block(self, height): return {"height": height}

"""Phase 25 DemoBlockchainProvider — same interface, zero live calls."""
class DemoBlockchainProvider:
    def get_transactions(self, address): return [{"demo": True, "address": address}]
    def get_address_labels(self, address): return []
    def get_token_transfers(self, address): return []
    def get_block(self, height): return {"height": height, "demo": True}

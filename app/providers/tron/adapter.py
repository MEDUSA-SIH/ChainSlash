"""Phase 4 TRON live adapter (TRON-first). TODO: TronGrid tx + energy/sponsor fields."""
class TronAdapter:
    chain = "TRON"
    def get_transactions(self, address): return []
    def get_address_labels(self, address): return []
    def get_token_transfers(self, address): return []
    def get_block(self, height): return {"height": height}

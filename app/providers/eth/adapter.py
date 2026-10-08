"""Phase 4 ETH live adapter. TODO: trace/debug + event-log parsing."""
class EthAdapter:
    chain = "ETH"
    def get_transactions(self, address): return []
    def get_address_labels(self, address): return []
    def get_token_transfers(self, address): return []
    def get_block(self, height): return {"height": height}

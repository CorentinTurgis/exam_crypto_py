class AssetService(Asset):
    def __init__(self, asset_id: int, symbol: str, name: str, price: str, rank: int, supply: float, max_supply: float, market_cap: float, update_time: datetime.datetime = None):
        self.id = asset_id
        self.symbol = symbol
        self.name = name
        self.price = price
        self.rank = rank
        self.supply = supply
        self.maxSupply = max_supply
        self.marketCap = market_cap
        self.updateTime = update_time or datetime.datetime.now()
    
    def update_price(self, new_price: str):
        self.price = new_price
        self.updateTime = datetime.datetime.now()
    
    def update_supply(self, new_supply: float):
        self.supply = new_supply
        self.updateTime = datetime.datetime.now()


# Exemple :
'''
if __name__ == "__main__":
    asset_service = AssetService(
        asset_id=1,
        symbol="BTC",
        name="Bitcoin",
        price="30000",
        rank=1,
        supply=18000000,
        max_supply=21000000,
        market_cap=600000000000
    )
'''
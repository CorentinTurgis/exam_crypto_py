class UserAssetsService(UserAssets):
    def __init__(self, id: int, userId: int, assetId: int, quantity: float, value: float, updateTime: datetime.datetime = None):
        self.id = id
        self.userId = userId
        self.assetId = assetId
        self.quantity = quantity
        self.value = value
        self.updateTime = updateTime or datetime.datetime.now()

    def update_quantity(self, new_quantity: float):
        self.quantity = new_quantity
        self.updateTime = datetime.datetime.now()

    def update_value(self, new_value: float):
        self.value = new_value
        self.updateTime = datetime.datetime.now()


# Exemple :
'''
if __name__ == "__main__":
    user_asset_service = UserAssetsService(id=1, userId=42, assetId=101, quantity=10.5, value=5000.0)
'''
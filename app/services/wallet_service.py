from fastapi import HTTPException

from app.core.db import db, Wallets


def save_wallet(name: str, owner: str) -> None:
    with db.atomic():
        Wallets.create(
            name=name,
            owner=owner
        )

def get_wallet_by_user_id(user_id) -> Wallets or None:
    try:
        wallet = Wallets.get_or_none(Wallets.owner == user_id)
        if wallet is None:
            raise HTTPException(status_code=404, detail='wallet_not_found')
        return wallet
    except Exception as e:
        print(f'ERREUR : {e}')
    return None

# class WalletService(Wallet):
#     def __init__(self, wallet_id: int, user_id: int, value: float, number_of_assets: int, update_time: datetime.datetime = None):
#         self.id = wallet_id
#         self.userId = user_id
#         self.value = value
#         self.numberOfAssets = number_of_assets
#         self.updateTime = update_time or datetime.datetime.now()
#
#     def deposit(self, amount: float):
#         self.value += amount
#         self.updateTime = datetime.datetime.now()
#
#     def withdraw(self, amount: float):
#         if amount > self.value:
#             raise ValueError("Insufficient funds in the wallet.")
#         self.value -= amount
#         self.updateTime = datetime.datetime.now()
#
#     def add_asset(self, count: int = 1):
#         self.numberOfAssets += count
#         self.updateTime = datetime.datetime.now()
#
#     def remove_asset(self, count: int = 1):
#         if count > self.numberOfAssets:
#             raise ValueError("Insufficient assets to remove.")
#         self.numberOfAssets -= count
#         self.updateTime = datetime.datetime.now()
#
#     def __str__(self):
#         update_str = self.updateTime.strftime('%Y-%m-%d %H:%M:%S')
#         return (f"Wallet(id={self.id}, userId={self.userId}, value={self.value:.2f}, "
#                 f"numberOfAssets={self.numberOfAssets}, updateTime={update_str})")


# Exemple :
'''
if __name__ == "__main__":
    wallet_service = WalletService(wallet_id=1, user_id=42, value=1000.0, number_of_assets=5)
    print(wallet_service)

    wallet_service.deposit(500.0)
'''
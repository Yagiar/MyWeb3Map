import csv
from web3 import Web3
from eth_account import Account
from eth_account.hdaccount import Mnemonic

# Подключение к сети Ethereum
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/609c9e3dac4b481789824f51b35ed054'))

# Включение использования функциональности Mnemonic
Account.enable_unaudited_hdwallet_features()

# Генерация нового кошелька MetaMask с помощью 12-словной фразы
def generate_metamask_wallet(num_wallets):
    wallets = []
    for _ in range(num_wallets):
        mnemonic = Mnemonic().generate()
        account = Account.from_mnemonic(mnemonic)
        private_key = account._private_key
        address = account.address
        wallets.append((mnemonic, private_key.hex(), address))
    return wallets

# Запись кошельков в файл CSV
def write_wallets_to_csv(wallets):
    with open('wallets.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Mnemonic', 'Private Key', 'Address'])
        for wallet in wallets:
            writer.writerow(wallet)

# Получение количества создаваемых кошельков от пользователя
num_wallets = int(input("Введите количество создаваемых кошельков: "))

# Генерация кошельков
wallets = generate_metamask_wallet(num_wallets)

# Запись кошельков в файл CSV
write_wallets_to_csv(wallets)

print(f"{num_wallets} кошельков были успешно созданы и записаны в файл wallets.csv.")

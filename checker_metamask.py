from web3 import Web3

# Подключение к различным блокчейнам
blockchains = {
    'Ethereum Mainnet': 'https://mainnet.infura.io/v3/609c9e3dac4b481789824f51b35ed054',
    # Добавьте другие блокчейны по желанию
}

# Функция для проверки баланса кошелька в каждом блокчейне
def check_metamask_balance(address):
    balances = {}
    for blockchain, url in blockchains.items():
        w3 = Web3(Web3.HTTPProvider(url))
        checksum_address = w3.to_checksum_address(address)
        balance = w3.eth.get_balance(checksum_address)
        balances[blockchain] = w3.from_wei(balance, 'ether')
    return balances

# Чтение списка кошельков из файла
wallets_file = 'wallets.txt'
wallets = []
with open(wallets_file, 'r') as file:
    wallets = [line.strip() for line in file]

# Проверка балансов кошельков
for address in wallets:
    balances = check_metamask_balance(address)
    print(f"Address: {address}")
    for blockchain, balance in balances.items():
        print(f"Balance in {blockchain}: {balance} ETH")
    print()

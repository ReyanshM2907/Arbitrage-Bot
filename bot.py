from web3 import Web3

infura_url = "https://goerli.infura.io/v3/97b8b242908c4d1591210f7dcaa76c64"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

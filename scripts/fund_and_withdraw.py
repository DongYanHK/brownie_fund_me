from brownie import FundMe
from scripts.helpful_scripts import get_account
from web3 import Web3


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The entrance fee is {entrance_fee}")
    print("Try to fund")
    fund_me.Fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()

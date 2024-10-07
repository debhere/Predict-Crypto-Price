import sys
#import requests
import pandas as pd


from predictcrypto.component.cmg import training_manager

if __name__ == "__main__":
    training_manager("prophet")
    
import json
from sos32.contract import Contract
from sos32.state_variable import StateVariable
import sys

# TODO : Handle Mapping, Arrays (fixed + dynamic), Strings Strucs, Enums & other types
# TODO : Recreate a solidity contract with the sorted state variables
# TODO : Handle several contracts, files & folders
# TODO : verbose levels -> logging
# TODO : Solve 1 large optimization problem instead of 1 per slot (if feasible)
# TODO : Try to integrate static analyzers if tool is useful


def main():
    path = sys.argv[1]
    # path = "out/SOS32Example.sol/SOS32Example.json"
    data=json.load(open(path))

    storage = []
    for sto in data["storageLayout"]["storage"]:
        sto["name"] = sto.pop("label")
        storage.append(sto)
        
    storage_full = [{**sto, **data["storageLayout"]["types"][sto["type"]], **{"position":idx}} for idx,sto in enumerate(storage)]

    state_vars = [StateVariable(**sto) for sto in storage_full]

    c = Contract(state_vars)
    c.optimize_storage()
    c.show_results()



if __name__== "__main__":
    main()
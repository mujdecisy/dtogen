import sys
from dtogen import main

if __name__ == "__main__":
    args = "-i test/dto_contract.yaml -o _output/ -l golang"
    for e in args.split(" "):
        sys.argv.append(e)
    main()
# creative-tonie-cli
A cli to put custom content on your creative tonie

# Prerequesites

- clone [tonie_api](https://github.com/moritzj29/tonie_api) to `./../tonie_api`
- or use provided docker file to build and run...

# build

## docker 
- `docker build -t creativetonie .`

## python3
- `pip3 install -r requirements-all.txt`

### regenerate dependencies with

`pip-compile requirements.txt --output-file requirements-all.txt`


# run
- `export TONIECLOUD_USERNAME=...`
- `export TONIECLOUD_PASSWORD=...`

## docker
- `docker run -ti --rm -e TONIECLOUD_USERNAME=$TONIECLOUD_USERNAME -e TONIECLOUD_PASSWORD=$TONIECLOUD_PASSWORD selamanse/creativetonie print-tonies`

## python3
- `python3 ./creative-tonie.py print-tonies`

# commands:

to get a current list of commands run program with `--help`

-  copy-path
-  print-tonie-chapters
-  print-tonies
-  wipe-tonie

# thx to

- [tonie-podcast-sync](https://github.com/alexhartm/tonie-podcast-sync)
- [tonie-api](https://github.com/moritzj29/tonie_api)
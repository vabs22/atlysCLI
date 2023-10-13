python_setup:
	echo "Installing python3 and pip"
	sudo apt-get update -y
	sudo apt install software-properties-common -y
	sudo apt-get install build-essential -y
	sudo apt install libpq-dev -y

	# install python
	sudo su
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install python3.9 python3.9-venv python3.9-dev
	#python3.9 --version

	# install pip
	sudo apt-get install -y python3-pip
	#pip3 -V
	pip3.9 install --upgrade pip

setup: python_setup
	echo "Installing project packages"
	pip3 install -r requirements.txt

country_data_setup:
	python3 src/cli.py precomputeCountryMetadata

checkVisa: country_data_setup
	python3 src/cli.py checkVisa ${country}


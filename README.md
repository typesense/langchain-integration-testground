# LangChain Typesense integration testground

This repo has scripts to exercise the LangChain Typesense integration. 

## Setup

Required Python 3.11

**Install Dependencies:**
```shell
brew install python3
virtualenv venv -p /opt/homebrew/bin/python3 # On M1
source venv/bin/activate

pip3 install -r requirements.txt
```

**Start Typesense:**
```shell
export TYPESENSE_API_KEY="..."

mkdir $(pwd)/typesense-data

docker run -p 8108:8108 -v$(pwd)/typesense-data:/data typesense/typesense:0.24.1 \
  --data-dir /data --api-key=$TYPESENSE_API_KEY --enable-cors
```

**Run LangChain script:**
```shell
export OPENAI_API_KEY="..."
export TYPESENSE_API_KEY="..."

python3 main.py
```
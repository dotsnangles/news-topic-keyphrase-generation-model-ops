### build dependencies for bentoml
poetry install
poetry shell
dvc pull

### save bento model, build bento, and containerize bento service
python save_bento_model.py
bentoml build
bentoml containerize news-topic-keyphrase-generator-t5-base:latest

### launch containerized bento service
# docker run --gpus all -it --rm -p 3000:3000 news-topic-keyphrase-generator-t5-base:[TAG] serve
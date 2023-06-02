### build dependencies for bentoml
poetry install
poetry shell
dvc pull

### save bento model, build bento, and containerize bento service
python save_bento_model.py
bentoml build
bentoml containerize news-topic-keyphrase-generator-t5-base:latest

### launch containerized bento service
# docker run \
# --gpus all -it --rm \
# -p 6666:3000 \
# --name news-topic-keyphrase-generator-t5-base-server \
# news-topic-keyphrase-generator-t5-base:wxtozqabagvmmasc serve

### endpoint = 'http://127.0.0.1:6666/news_topic_keyphrase_generator_t5_base'
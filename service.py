import bentoml
from bentoml.io import JSON
from transformers import AutoTokenizer
import json

ckpt = "checkpoints/paust_pko_t5_base_v4_run_1"
tokenizer = AutoTokenizer.from_pretrained(ckpt)

prefix = "generate keyphrases: "

runner = bentoml.transformers.get(
    "news-topic-keyphrase-generator-t5-base:latest"
).to_runner()

svc = bentoml.Service("news-topic-keyphrase-generator-t5-base", runners=[runner])


@svc.api(input=JSON(), output=JSON())
def news_topic_keyphrase_generator_t5_base(input_texts_json):
    inputs = json.loads(input_texts_json)["inputs"]
    inputs = [prefix + input_ for input_ in inputs]
    encoded = tokenizer(
        inputs,
        max_length=1024,
        truncation=True,
        padding="max_length",
        return_tensors="pt",
    )

    outputs = runner.generate.run(**encoded, max_length=64).detach().cpu().tolist()
    outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    outputs = dict(outputs=outputs)
    outputs = json.dumps(outputs)

    return outputs

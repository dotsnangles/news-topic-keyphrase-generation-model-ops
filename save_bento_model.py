from transformers import (
    AutoConfig,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)

import bentoml


def save_bemtoml_model():
    CKPT = "checkpoints/paust_pko_t5_base_v4_run_1/merged"
    model = AutoModelForSeq2SeqLM.from_pretrained(CKPT)

    bento_model = bentoml.transformers.save_model(
        "news-topic-keyphrase-generator-t5-base",
        model,
        signatures={
            "generate": {"batchable": True},
        },
    )
    print(bento_model)


if __name__ == "__main__":
    save_bemtoml_model()

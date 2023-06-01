# news-topic-keyphrase-generation-model-ops

## BentoML을 활용한 모델 추론 API 컨테이너 생성
- containerize.sh 파일에 정의된 순서대로 프로젝트 디펜던시를 빌드하고, Bento 및 Docker 이미지를 생성한 뒤 컨테이너화가 가능합니다.
- test_bentoml_clientside.ipynb를 통해 API 추론 부하량을 시험해볼 수 있습니다.

## Bento Model 저장 및 Service 정의
- 각각 save_bento_model.py와 service.py에 정의합니다.
- test_bentoml_service.ipynb를 사용해 Service를 정의하고 디버깅한 뒤 service.py를 작성합니다.
- Bento화/컨테이너화 전 service.sh를 실행해 API를 시험해볼 수 있습니다.
  - API를 시험 시 .old 내의 bentoml_configuration.yaml을 사용할 수도 있습니다.

## bentofile.yaml
- Bento화 및 컨테이너화에 필요한 설정이 정의된 파일입니다.

## BentoML 워크플로우
- 추론에 사용할 모델의 체크포인트를 Bento Model로 저장합니다.
- Bento Model을 활용해 Service를 정의합니다.
- Bento를 생성하고 Service를 시험합니다.
- Bento를 컨테이너화하여 Docker/Kubernetes 환경에서 API를 사용합니다.
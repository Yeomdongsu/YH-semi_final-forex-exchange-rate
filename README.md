# YH-semi_final-forex-exchange-rate
중간 프로젝트 첫번째 

2004년 이후 외환 환율 웹 대시보드 만들기

순서)
1. 분석할 데이터를 준비한다.

2. 주피터 노트북으로 데이터를 분석한다. ( 가상환경 맞춰서 )

3. 필요에 의해서 머신러닝을 수행할 수도 있다.

4. 분석이 완료되면, 대시보드 앱으로 개발한다.

5. 대시보드 앱은 vscode로 개발한다.

6. 로컬에서 테스트해서 이상이 없으면 클라우드 서버에 배포한다. (24시간 서비스, 배포 자동화)
# Streamlit Tutorials

#### Install
```
pip install streamlit
```

#### Run
```
cd [directory]
streamlit run app.py --server.address 0.0.0.0 --server.port [your port]
# http://0.0.0.0:[your port]
```
## Main App
```
# run
streamlit run app.py --server.address 0.0.0.0 --server.port [your port]
```

<p align="center">
    <img src='asset/main.gif?raw=1' width = '900' >
</p>

## 💸 Stock Price Dashboard ✨

```
# install
pip install yfinance fbprophet plotly

# run
cd stock-price-dashboard
streamlit run app.py --server.address 0.0.0.0 --server.port [your port]
```

<p align="center">
    <img src='asset/finance.gif?raw=1' width = '900' >
</p>

## 🙃 Cartoon StyleGAN ✨

- [`happy-jihye/Cartoon-StyleGAN`](https://github.com/happy-jihye/Cartoon-StyleGAN)

```
# install
pip install bokeh ftfy regex tqdm gdown
# for styleclip
pip install git+https://github.com/openai/CLIP.git

# run
cd cartoon-stylegan
streamlit run app.py --server.address 0.0.0.0 --server.port [your port]
```

<p align="center">
    <img src='asset/cartoon-stylegan-1.gif?raw=1' width = '700' >
</p>


## 🖼️ VQGAN-CLIP ✨

```
# install python packages
pip install ftfy regex tqdm omegaconf pytorch-lightning IPython kornia imageio imageio-ffmpeg einops torch_optimizer

# clone other repositories
git clone 'https://github.com/openai/CLIP'
git clone 'https://github.com/CompVis/taming-transformers'

# download checkpoints
mkdir checkpoints
curl -L -o checkpoints/vqgan_imagenet_f16_16384.yaml -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1' #ImageNet 16384
curl -L -o checkpoints/vqgan_imagenet_f16_16384.ckpt -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1' #ImageNet 16384

# run
cd VQGAN-CLIP
streamlit run app.py --server.address 0.0.0.0 --server.port [your port]
```


<p align='center'><img src='asset/vqgan.gif?raw=1' width = '1100' ></p>

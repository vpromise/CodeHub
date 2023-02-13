
# Install Instruction

## dataset generation
- [datagen_few_seed.py](./datagen_few_seed.py)


## conda env configuration 
```bash
conda create -n ofa python=3.8
conda activate ofa
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge

pip --version    # 22.1.2
pip install -r requirements.txt  # Errors out with fairseq metrics import error

python -m pip install pip==21.2.4  # downgrade pip
pip uninstall fairseq
pip install -r requirements.txt  # No longer any import errors

pip install tensorboard
pip install g2p_en

pip3 install setuptools==59.5.0  #  AttributeError: module 'distutils' has no attribute 'version'
# https://sebhastian.com/python-attributeerror-module-distutils-has-no-attribute-version/
```
## correct error

edit `./criterions/label_smoothed_cross_entropy.py`
before line 222, add
```python
net_output=list(net_output)
net_output[0] = net_output[0].masked_fill(~constraint_masks, -math.inf)
```

## requirements.txt
```txt
-e ./fairseq/
opencv-python
timm
ftfy==6.0.3
tensorboardX==2.4.1
pycocotools==2.0.4
pycocoevalcap==1.2
pytorch_lightning
einops
datasets
rouge_score
soundfile
editdistance
librosa
python-Levenshtein
zhconv
pypinyin==0.47.1
tensorboard
g2p_en
```
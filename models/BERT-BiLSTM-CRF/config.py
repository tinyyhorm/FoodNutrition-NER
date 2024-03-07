import os
import torch

random_state = 1

files = ['train', 'test']
data_dir = './datasets/Human Review Data/'
exp_dir = './models/BERT-BiLSTM-CRF/experiments/fnner/'
cases_dir = './models/BERT-BiLSTM-CRF/case/'

train_dir = data_dir + 'train.npz'
test_dir = data_dir + 'test.npz'
vocab_path = data_dir + 'vocab.npz'
model_dir = exp_dir + 'model.pth'
log_dir = exp_dir + 'train.log'
case_dir =  cases_dir + 'bad_case-%d.txt' %random_state
case_log_dir = cases_dir + 'record-%d.csv' %random_state

bert_model = './models/BERT-BiLSTM-CRF/pretrained_bert_models/bert-base-chinese'
roberta_model = './models/BERT-BiLSTM-CRF/pretrained_bert_models/RoBERTa_zh_L12_PyTorch'
# 训练集、验证集划分比例
dev_split_size = 0.25

# 是否加载训练好的NER模型
load_before = False

# 是否对整个BERT进行fine tuning
full_fine_tuning = True

# hyper-parameter
learning_rate = 2e-3
weight_decay = 0.1
clip_grad = 5

#batch_size = 32
batch_size = 12
#epoch_num = 50
epoch_num = 20
min_epoch_num = 15
patience = 0.0002
patience_num = 10

gpu = ''

if gpu != '':
    device = torch.device(f"cuda:{gpu}")
else:
    device = torch.device("cpu")

labels = ['Nutrient', 'NotNutrient', 'Food', 'Group', 'Organ', 'Disease']

label2id = {
    "O": 0,
    "B-Nutrient": 1,
    "B-NotNutrient": 2,
    "B-Food": 3,
    'B-Group': 4,
    'B-Organ': 5,
    'B-Disease': 6,
    'I-Nutrient': 7,
    'I-NotNutrient': 8,
    'I-Food': 9,
    'I-Group': 10,
    "I-Organ": 11,
    "I-Case": 12,
    "I-Disease": 13
}

id2label = {_id: _label for _label, _id in list(label2id.items())}

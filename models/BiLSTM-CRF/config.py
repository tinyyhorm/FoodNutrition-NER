import os

random_state = 10

files = ['train', 'test']
data_dir = './datasets/Human Review Data/'
exp_dir = './models/BiLSTM-CRF/experiments/fnner/'
cases_dir = './models/BiLSTM-CRF/case/'

train_dir = data_dir + 'train.npz'
test_dir = data_dir + 'test.npz'
vocab_path = data_dir + 'vocab.npz'
model_dir = exp_dir + 'model.pth'
log_dir = exp_dir + 'train.log'
case_dir =  cases_dir + 'bad_case-%d.txt' %random_state
case_log_dir = cases_dir + 'record-%d.csv' %random_state

max_vocab_size = 1000000
n_split = 5
#dev_split_size = 0.1
dev_split_size = 0.25
#batch_size = 32
batch_size = 16
embedding_size = 128
hidden_size = 384
drop_out = 0.1
lr = 2e-3
betas = (0.9, 0.999)
lr_step = 10
#lr_gamma = 0.8
lr_gamma = 0.8
#epoch_num = 30
epoch_num = 20
min_epoch_num = 15
patience = 0.002
patience_num = 3

gpu = '0'

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

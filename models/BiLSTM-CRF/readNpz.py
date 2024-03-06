import config
import numpy as np

data = np.load(config.train_dir, allow_pickle=True)

print(data.files)
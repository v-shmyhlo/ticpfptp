import os
import numpy as np
import random
import torch


def fix_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


def one_hot(input, num_classes):
    eye = torch.eye(num_classes).to(input.device)

    return eye[input]


def save_model(model, path):
    torch.save(model, os.path.join(path, 'model.pt'))
    torch.save(model.state_dict(), os.path.join(path, 'weights.pt'))


def load_model(path):
    return torch.load(os.path.join(path, 'model.pt'))


# TODO:
def load_weights(model, path, map_location=None):
    model.load_state_dict(torch.load(os.path.join(path, 'weights.pt'), map_location=map_location))

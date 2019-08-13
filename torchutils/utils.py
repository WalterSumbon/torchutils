import torch as _torch
import numpy as _np
from ._validate import _validate_param

__all__ = ['set_random_seed']


def set_random_seed(seed):
    """
    Set random seed for numpy, torch and torch.cuda.

    Parameters
    ----------
    seed : int
        Seed value.

    Returns
    -------
    None
        Nothing.
    """

    _validate_param(seed, 'seed', 'int')
    _np.random.seed(seed)
    _torch.manual_seed(seed)
    if _torch.cuda.is_available():
        _torch.cuda.manual_seed(seed)

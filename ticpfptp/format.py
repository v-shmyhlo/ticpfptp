def args_to_path(args):
    ignored_keys = ['dataset_path', 'experiment_path', 'fold', 'restore_path', 'epochs']
    args = vars(args)
    keys = sorted([k for k in args.keys() if k not in ignored_keys])
    return '|'.join(['{}:{}'.format(k, args[k]) for k in keys])

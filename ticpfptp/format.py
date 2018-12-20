# TODO:
def args_to_string(args, ignore=[]):
    args = vars(args)

    return 'arguments:\n' + '\n'.join(['\t{}: {}'.format(k, args[k]) for k in sorted(args.keys())])


# TODO:
def args_to_path(args, ignore=[]):
    args = vars(args)
    keys = sorted([k for k in args.keys() if k not in ignore])
    return '|'.join(['{}:{}'.format(k, args[k]) for k in keys])

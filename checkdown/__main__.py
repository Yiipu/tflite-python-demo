#!/usr/bin/env python
def main():
    from checkdown.utils import get_model_path
    default_model_path = get_model_path()

    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, help='Path to the input data')
    parser.add_argument('--model',default=default_model_path, type=str, help='Path to the model file')
    args = parser.parse_args()

    if args.input is None:
        parser.print_help()
        return

    from checkdown.cli import main
    main(args)

if __name__ == '__main__':
    main()
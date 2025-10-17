import argparse

parser = argparse.ArgumentParser(description="Калькулятор")
parser.add_argument("a", type=float, help='Первое число')
parser.add_argument("sign", type=float, help='Действие')
parser.add_argument("b", type=float, help='Второе число')
parser.add_argument(
    '--sign', '-s',
    type=str,
    choices=['+', '-', '*', '/'],
    help='Действие'
    )
parser.add_argument(
    '--int', 
    '-i', 
    action='store_true',
    help='Приводить к целому числу'
    )
args = parser.parse_args()

code = f'{args.a} {args.sign} {args.b}'
if args.int:
    print(f'{code} = {eval(code)}')
else:
    print(f'{code} = {eval(code)}')
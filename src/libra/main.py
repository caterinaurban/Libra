"""
Libra Static Neural Network Analyzer
====================================

:Author: Caterina Urban
"""
import argparse
from multiprocessing import cpu_count

from libra.engine.bias_analysis import BiasAnalysis, AbstractDomain


def checker(domain):
    if domain == 'boxes':
        return AbstractDomain.BOXES
    elif domain == 'symbolic':
        return AbstractDomain.SYMBOLIC3
    elif domain == 'deeppoly':
        return AbstractDomain.DEEPPOLY
    elif domain == 'neurify':
        return AbstractDomain.NEURIFY
    error = "Invalid abstract domain! Valid domains are 'boxes', 'symbolic', 'deeppoly', or 'neurify'."
    raise argparse.ArgumentTypeError(error)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'specification',
        help='input specification')
    parser.add_argument(
        'neural_network',
        help='neural network (.py file) to analyze')

    parser.add_argument(
        '--domain',
        help='abstract domain to be used for the forward pre-analysis (boxes, symbolic, deeppoly, or neurify)',
        type=checker,
        default='symbolic')

    parser.add_argument(
        '--min_lower',
        help='minimum lower bound for the forward pre-analysis',
        type=float,
        default=0.25)
    parser.add_argument(
        '--lower',
        help='lower bound for the forward pre-analysis',
        type=float,
        default=1)

    parser.add_argument(
        '--upper',
        help='upper bound for the forward pre-analysis',
        type=int,
        default=0)
    parser.add_argument(
        '--max_upper',
        help='upper bound for the forward pre-analysis',
        type=int,
        default=2)

    parser.add_argument(
        '--cpu',
        help='number of CPUs to be used for the analysis',
        type=int,
        default=cpu_count())

    args = parser.parse_args()

    spec = args.specification
    domain = args.domain
    minL = args.min_lower
    L = args.lower
    U = args.upper
    maxU = args.max_upper
    cpu = args.cpu
    nn = args.neural_network

    BiasAnalysis(spec, domain=domain, minL=minL, startL=L, startU=U, maxU=maxU, cpu=cpu).main(nn)


if __name__ == '__main__':
    main()

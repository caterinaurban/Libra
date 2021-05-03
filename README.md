# Tool (tool-paper #16)

Nowadays, machine-learned software plays an increasingly important role 
in critical decision-making in our social, economic, and civic lives.

Tool is a static analyzer for certifying **fairness** of *feed-forward neural networks* 
used for classification of tabular data. Specifically, 
given a choice (e.g., driven by a causal model) of input features 
that are considered (directly or indirectly) sensitive to bias,
a neural network is fair if the classification 
is not affected by different values of the chosen features. 

When certification succeeds, Tool provides definite guarantees, 
otherwise, it describes and quantifies the biased behavior.

A preliminary version of Tool was developed to implement and test the analysis method described in:

	C. Urban, M. Christakis, V. Wüstholz, F. Zhang - Perfectly Parallel Fairness Certification of Neural Networks
	In Proceedings of the ACM on Programming Languages (OOPSLA), 2020.

Tool now additionally includes new abstract domains including a generic reduced product domain construction, 
a new auto-tuning mechanism for finding the optimal configuration for Tool’s forward pre-analysis, and
a tasks scheduling optimization to leverage all the available CPUs for Tool’s backward analysis. 
These new features are described in:
	
	Anonymous - Reduced Products of Abstract Domains for Fairness Certification of Neural Networks
	Submitted to SAS 2021, tool-paper #16.

## Getting Started 

### Docker Container

The provided Docker container is a virtual image ready to run Tool and replicate the experiments presented in the SAS submission. To modify, create, and inspect files we already installed `nano` and `vim`.

The container is organized as follow:
```
/home
├── networks              # neural networks as python scripts
│   ├── 10.py               # network with 10 ReLU nodes
│   ├── 12.py               # network with 12 ReLU nodes
│   ├── 20.py               # network with 20 ReLU nodes
│   ├── 40.py               # network with 40 ReLU nodes
│   ├── 45.py               # network with 45 ReLU nodes
│   └── example.py          # toy network
├── scripts               # experiment scripts               
│   ├── configurations.sh   # experiment A   
│   ├── cpus.sh             # experiment B
│   └── models.sh           # experiment C
├── specs                 # network specifications
│   ├── census.txt          # spec file for all the experiments
│   └── example.txt         # spec for the toy network 
├── logs                  # scripts print their logs here
├── fetch.py              # python script to fetch logs
└── README.md             # this file
```

### Command Line Usage

#### Tool Input

Tool expects as input a *ReLU-based feed-forward neural network* in Python program format. 
We already provided some neural networks in the right input format in `/home/networks`

A *specification* of the input features is also necessary for the analysis.
This has the following format, 
depending on whether the chosen sensitive feature for the analysis 
is categorical or continuous (some examples are provided in `/home/specs`):

  | Categorical | Continuous |
  | ----------- | ---------- |
  | `number of inputs representing the sensitive feature` | `1` |
  | `list of the inputs, one per line` | `value at which to split the range of the sensitive feature` |

The rest of the file should specify the other (non-sensitive) categorical features. 
The (non-sensitive) features left unspecified are assumed to be continuous. 

For instance, these are two examples of valid specification files:

  | Categorical | Continuous |
  | ----------- | ---------- |
  | 2           | 1          |
  | x03         | x00        |
  | x04         | 0.5        |
  | 2           | 2          |
  | x00         | x01        |
  | x01         | x02        |

In the case on the left there is one unspecified non-sensitive continuous feature (`x02`). 

#### Running Tool

To analyze a specific neural network run:

    > tool <specification> <neural-network>.py [OPTIONS]

The following command line options are recognized:

    --domain [ABSTRACT DOMAIN]
    
        Sets the abstract domain to be used for the forward pre-analysis.
        Possible options for [ABSTRACT DOMAIN] are:
        * boxes (interval abstract domain)
        * symbolic (combination of interval abstract domain with symbolic constant propagation 
        [Li et al. - Analyzing Deep Neural Networks with Symbolic Propagation: Towards Higher Precision and Faster Verification (SAS 2019)])
        * deeppoly (deeppoly abstract domain 
        [Singh et al. - An Abstract Domain for Certifying Neural Networks (POPL 2019)]) 
        * neurify (neurify symbolic relaxation 
        [Wang et al. - Efficient Formal Safety Analysis of Neural Networks (NeurIPS 2018)]) 
        * boxes_deeppoly (product of boxes and deeppoly)
        * boxes_neurify (product of boxes and neurify)
        * deeppoly_symbolic (product of deeppoly and symbolic)
        * neurify_symbolic (product of neurify and symbolic)
        * deeppoly_neurify (product of deeppoly and neurify)
        * boxes_deeppoly_neurify (product of boxes, deeppoly, and neurify)
        * deeppoly_neurify_symbolic (product of deeppoly, neurify, and symbolic)
        Default: symbolic

    --lower [LOWER BOUND]
    
        Sets the lower bound for the forward pre-analysis.
        Default: 0.25
    
    --min_lower [LOWER BOUND]
    
        Sets the minimum lower bound for the (auto-tuning of the) forward pre-analysis.
        Default: the value of the lower bound
        
    --upper [UPPER BOUND]
    
        Sets the upper bound for the forward pre-analysis.
        Default: 2
        
    --max_upper [UPPER BOUND]
    
        Sets the maximum upper bound for the (auto-tuning of the) forward pre-analysis.
        Default: the value of the upper bound
    
    --cpu [CPUs]
    
        Sets the number of CPUs to be used for the analysis.
        Default: the value returned by cpu_count() 

During the analysis, Tool prints on standard output 
which regions of the input space are certified to be fair,
which regions are found to be biased, 
and which regions are instead excluded from the analysis due to budget constraints.

We also provided a toy network, to 
To test Tool, we also provided a toy network `/home/networks/example.py` and the relative  specification file `/home/specs/example.txt`. Run Tool as follows:

    > tool specs/example.txt networks/example.py --domain boxes -- lower 0.25 --upper 2

The `/home/networks/example.py` file represents a small neural network with three inputs representing two input features 
(one, represented by `x`, is continuous and one, represented by `y0` and `y1`, is categorical). 
The specification `/home/specs/example.txt` tells the analysis to consider the categorical feature sensitive to bias.
In this case the analysis should be able to certify 23.4375% of the input space, 
find bias in 71.875% of the input space, and leave 4.6875% of the input space unanalyzed.
Changing the domain to any of the other options should analyze the entire input space finding bias in 73.44797685362308% of it.
The input regions in which bias is found are reported on standard output. 

## Step-by-Step Experiment Reproducibility

The experimental evaluation in the SAS submission was conducted on a machine 
with two 16-core Intel ® Xeon ® 5218 CPU @ 2.4GHz, 192GB of RAM, and running CentOS 7.7 with linux kernel 3.10.0.

### Experiment 1: Effect of Neural Network Structure on Precision and Scalability

To reproduce the results shown in Table 1 one can use the script `/home/scripts/models.sh` as follows

    > sh /home/scripts/models.sh

The script will generate the corresponding log files in `/home/models/logs` at the end of the executions (logs will be also available in the stdout channel during the execution).

> Please take note of the expected execution times before launching the script. 
On a less powerful machine than that used for our evaluation 
it might be preferable to run only single executions, running Tool directly from outside the script.

### Experiment 2: Scalability-vs-Precision Tradeoff

To reproduce the results shown in Table 2 one can use the script `/home/scripts/configurations.sh` as follows

    > sh /home/scripts/configurations.sh

The script will generate the corresponding log files in `/home/logs/configurations`.

> Please take note of the expected execution times before launching the script. 
On a less powerful machine than that used for our evaluation 
it might be preferable to run only single executions, running Tool directly from outside the script.

### Experiment 3: Leveraging Multiple CPUs

To reproduce the results shown in Table 3 and Figure 1 one can use the script `/home/scripts/cpus.sh`.
Note that, this experiment requires 64 CPUs. Please, modify the script before running, in order to fit your resources.

    > sh /home/scripts/cpus.sh

The script will generate the corresponding log files in `/home/logs/cpus`.

> Please take note of the expected execution times before launching the script. 
On a less powerful machine than that used for our evaluation 
it might be preferable to run only single executions, running Tool directly from outside the script.
 
## Utilities

We provided a python script to fetch log files automatically, to retrieve only major information about the execution.
 
    > python3 fetch.py <log-path>

The script will return a json composed by: the autotuning parameters (lower and upper bound where autotuning stabilizes), partitions information (the number of feasible and completed partitions), total space analyzed and biased space found, and the total running time. 

# Libra

<p align="center">
  <img src ="https://raw.githubusercontent.com/caterinaurban/Libra/master/icon.png" width="25%"/>
</p>

Nowadays, machine-learned software plays an increasingly important role 
in critical decision-making in our social, economic, and civic lives.

Libra is a static analyzer for certifying **fairness** of *feed-forward neural networks* 
used for classification of tabular data. Specifically, 
given a choice (e.g., driven by a causal model) of input features 
that are considered (directly or indirectly) sensitive to bias,
a neural network is fair if the classification 
is not affected by different values of the chosen features. 

When certification succeeds, Libra provides definite guarantees, 
otherwise, it describes and quantifies the biased behavior.

## Getting Started 

### Prerequisites

* Install **Git**

* Install [**APRON**](https://github.com/antoinemine/apron)

    * Install [**GMP**](https://gmplib.org/) and [**MPFR**](https://www.mpfr.org/)
    
    | Linux                              | Mac OS X                                   |
    |------------------------------------| ------------------------------------------ |
    | `sudo apt-get install libgmp-dev`  | `brew install gmp`                         |
    |                                    | `ln -s /usr/local/Cellar/gmp/ /usr/local/` |
    |                                    |                                            |
    | `sudo apt-get install libmpfr-dev` | `brew install mpfr`                        |
    |                                    | `ln -s /usr/local/Cellar/mpfr /usr/local/` |

    * Install **APRON**
    
    | Linux or Mac OS X                                |
    | ------------------------------------------------ |
    | `./configure -no-cxx -no-java -no-ocaml -no-ppl` |
    | `make`                                           |
    | `sudo make install`                              |


* Install [**Python 3.7**](http://www.python.org/)

* Install ``virtualenv``:

    | Linux or Mac OS X                     |
    | ------------------------------------- |
    | `python3.7 -m pip install virtualenv` |


### Installation

* Create a virtual Python environment:

    | Linux or Mac OS X                     |
    | ------------------------------------- |
    | `virtualenv --python=python3.7 <env>` |

* Install apronpy in the virtual environment:

    | Linux or Mac OS X                 |
    | --------------------------------- |
    | `./<env>/bin/pip install apronpy` |

* Install Libra in the virtual environment:

    | Linux or Mac OS X                                                        |
    | ------------------------------------------------------------------------ |
    | `./<env>/bin/pip install git+https://github.com/caterinaurban/Libra.git` | 
    
### Command Line Usage

Libra expects as input a *ReLU-based feed-forward neural network* in Python program format.
This can be obtained from a Keras model using the script `keras2python.py` as follows:

  | Linux or Mac OS X                      |
  | -------------------------------------- |
  | `python3.7 keras2python.py <model>.h5` |
   
The script will produce the corresponding `<model>.py` file. 
In the file, the inputs are named `x00`, `x01`, `x02`, etc. 

A *specification* of the input features is also necessary for the analysis.
This has the following format, 
depending on whether the chosen sensitive feature for the analysis 
is categorical or continuous:

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


To analyze a specific neural network  run:

   | Linux or Mac OS X                             |
   | --------------------------------------------- |
   | `./<env>/bin/libra <neural-network>.py <specification>` [OPTIONS] | 
   
The following command line options are recognized:

    TODO

## Authors

* **Caterina Urban**, INRIA & École Normale Supérieure, Paris, France

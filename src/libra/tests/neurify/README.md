# How to test Neurify state domain

Note that, we decided to test the Neurify state domain over the toy neural network.
To check whether the domain is still performing correctly we added to this directory some log files computed "by hand".

The name of the file recalls the input bounds of the toy-network inputs checked during the forward analysis. Roughly speaking, these are the logs of the first six analyses performed by the ForwardInterpreter.
E.g., the file "log_toy_0_1_0.51_1" recalls the forward analysis over the toy-network with bounds:
> {x01: (0, 1), x02: (0.51, 1)}

Currently, the neuron-numbering technique of Libra slightly differs from the one chosen for the logs. This is the conversion (Libra's neuron -> log's neuron):
* x01 -> x0     # input
* x02 -> x1     # input
* x11 -> x2
* x12 -> x3
* x21 -> x4
* x22 -> x5
* x31 -> x6'    # output
* x32 -> x7'    # output

To check Neurify we added to the Libra execution logs the inputs/outputs bounds of each forward pass. Remember that Libra uses floating-point numbers, based on the apron library, thus rounding errors may occur (still better than python itself though).

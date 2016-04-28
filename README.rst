Perceptron
==========

|PyPI version| |Build Status|

Perceptron implements a *multilayer perceptron* network written in Python.
This type of network consists of multiple layers of neurons, the first
of which takes the input. The last layer gives the ouput. There can be
multiple middle layers but in this case, it just uses a single one.

    For further information about multilayer perceptron networks, please
    read `this <https://en.wikipedia.org/wiki/Multilayer_perceptron>`__
    entry on the Wikipedia.

Requirements
------------

-  `python <https://www.python.org/>`__ >= 2.7

Installation
------------

You can install the package via ``easy_install`` or ``pip``:

.. code:: bash

    easy_install perceptron
    pip install perceptron

Feeding Forward
---------------

The neural network uses the *hyperbolic tangent (tanh)* function.

.. figure:: http://mathworld.wolfram.com/images/interactive/TanhReal.gif
   :alt: Hyperbolic tangent

   Hyperbolic tangent

The x-axis is the total input to the node. As the input aproaches to 0,
the output starts to climb quickly. With an input of 2, the output is
almos at 1 and doesn't get much higher. This is a type of *sigmoid*
functions to calculate the output of the neurons.

    Note: Before runing the ``feedforward`` algorithm, the network will
    have to query the nodes and connections, and build, in memory, the 
    position of the network that is relevant to a specific input.

Training with Backpropagation
-----------------------------

The backpropagation algorithm then performs the following steps.

For each node in the output layer:

1. Calculate the difference between the node's current output and what it should be.
2. Use the ``dtanh`` function to determine how much the node's total input has to change.
3. Change the strenght of every inconming input in proportion to the input's current strength and the learning rate.

For each node in the hidden layer:

1. Change the output of the node by the sum of the strength of each output value multiplied by how much its targets has to change.
2. Use the ``dtanh`` function to determine how much the node's total input has to change.
3. Change the strenght of every inconming input in proportion to the input's current strength and the learning rate.

The implementation of this algorithm actually calculates all the errors
in advance and then adjusts the weigths, because all the calculations
rely on knowing the current weights rather than the updated weights.

    Note: Before runing ``backpropagation`` method, it's necessary to
    run ``feedforward`` so that the current output of every node will be
    stored in the instance variables.

Usage
-----

Import the module at the beginning of your file:

.. code:: python

    from perceptron import mlp

Init the ``neural network``:

.. code:: python

    n = mlp.Net()

Example
-------

In this example the neurons in the first layer respont to the ids that
are used as input. If a id is present, then the neurons that are strongly
connected to that word become active. The second layer is fed by the
first layer, so it responds to combinations of ids. Finally, the neurons
feed their result to the outputs, and particular combinations may be
strongly or weakly associated with the possible results. In the end,
the final decision is whichever output is strongest classifying an id.

.. code:: python

    from perceptron import mlp

    def main():
      n = mlp.Net()

      for i in range(30):
        n.train([101,103],[201,202,203],201)
        n.train([102,103],[201,202,203],202)
        n.train([101],[201,202,203],203)

      print n.eval([101,103,],[201,202,203])
      print n.eval([102,103],[201,202,203])
      print n.eval([103],[201,202,203])

    if  __name__=='__main__': main()

That will give the following output.

.. code::

    [0.8435967735300776, 0.011059223531796199, 0.017992770688108367]
    [-0.028282207517584094, 0.8775955174169334, 0.0032322039490162353]
    [0.8459277961565395, -0.011590385221469553, -0.8361964445052618]

Licence
-------

Copyright © 2016 Roger Fernandez Guri. It is free software, and may be
redistributed under the terms specified in the
`LICENCE <https://github.com/rfguri/perceptron/blob/master/LICENSE>`__ file.

.. |PyPI version| image:: https://badge.fury.io/py/perceptron.svg
   :target: http://badge.fury.io/py/perceptron
.. |Build Status| image:: https://travis-ci.org/rfguri/perceptron.svg
   :target: https://travis-ci.org/rfguri/perceptron


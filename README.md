# COMP5118

This project is a updated version of X-Map: https://github.com/LPD-EPFL-ML/X-MAP/tree/master/code

Use 
```
pip install -r requirements.txt 
```
to install all required lib.

## Getting Started

### Prerequisites
X-MAP requires `Python >=3`, `Numpy 1.10.4`, `Apache Spark >=2.8` pre-installed on your machine.

#### Installation
Please refer to
[Anaconda](https://www.continuum.io/downloads), [Apache Spark](http://spark.apache.org/) for installation instructions.

## Build
Once you have modified the scripts in `X-MAP` folder, you should rebuild the package using the following command:

```
python setup.py install
```

We provide an egg file, located in `dist/xmap-0.1.0-py3.5.egg`, that you could use for your application.

## Running the tests
### Prerequisites
X-MAP is tested on real-traces from [Amazon](https://snap.stanford.edu/data/web-Amazon.html). For current implementation, the input data follows the below-mentioned format:
`<userid>\t<itemid>\t<rating>\t<timestamp>`.

Note that the timestamp is required if you want to implement algorithms incorporating temporal behaviour of users which is also supported by AlterEgos.

### Run X-MAP
We provide here two demonstrations: `twodomain_demo.py` and `multidomain_demo.py`. You can also tune the parameters in the file `parameters.yaml`.

Note that the scipt should run successfully using the docker image that we provided. Please check your local system settings (e.g., directory path) while working with the application.

#### Run X-MAP locally on a machine with 4 cores using docker
A simple example of how to run X-MAP on a local machine.

```
spark-submit --master local[4] \
    --py-files dist/xmap-0.1.0-py3.8.egg twodomain_demo.py

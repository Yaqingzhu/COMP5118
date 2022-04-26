# COMP5118

This project is a updated version of X-Map: https://github.com/LPD-EPFL-ML/X-MAP/tree/master/code

Use pip install -r requirements.txt to install all required lib.

X-MAP requires Python >= 3.5, Numpy 1.10.4, Apache Spark >=2.8 pre-installed on your machine.

You can download dataset from https://snap.stanford.edu/data/web-Amazon.html and use parser.py to convert compressed file to txt file with X-Map required format.

To run the code, 

spark-submit --master local[4] \
    --py-files dist/xmap-0.1.0-py3.8.egg twodomain_demo.py

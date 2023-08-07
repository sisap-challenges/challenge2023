# Preliminary results

Best running time for a parameter combination exceeding 90% recall.


## 10 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
HSP | 10M | 0.34
UTokyo | 10M  |  0.49
HIOB | 10M  |    35.89
CRANBERRY  | 10M  |  107.05
SWANN* | 10M | 512.31
LMI | 10M  |  582.55

## 30 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
HSP | 30M |  0.49
UTokyo | 30M  |   0.71
HIOB | 30M  |    89.97
CRANBERRY  | 30M  |  192.02
SWANN* | 30M | 1406.07
LMI | 30M  |  1872.42

## 100 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
HSP | 100M |0.51
HIOB | 100M  |    247.01
CRANBERRY  | 100M  |   589.76
SWANN* | 100M |  4866.21
UTokyo | 100M  |  OOM
LMI | 100M  |  DNF     

# Notes

- SWANN* works on the binary hamming embedding instead of the clip768 embedding

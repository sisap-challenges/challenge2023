# Preliminary results

Best running time for a parameter combination exceeding 90% recall.

# TASK A

## 10 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
HSP | 10M | 0.34
UTokyo | 10M  |  0.49
BASELINE-SearchGraph | 10M | 0.61
BASELINE-FAISSHNSW | 10M | 0.74
HIOB | 10M  |    35.89
CRANBERRY  | 10M  |  107.05
LMI | 10M  |  450.25
SWANN* | 10M | 512.31
Bruteforce | 10M | 2415.74

## 30 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
HSP | 30M |  0.49
UTokyo | 30M  |   0.71
BASELINE-FAISSHNSW | 30M | 0.86
BASELINE-SearchGraph | 30M | 1.09
HIOB | 30M  |    89.97
CRANBERRY  | 30M  |  192.02
SWANN* | 30M | 1406.07
Bruteforce | 30M | 9010.50

## 100 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
HSP | 100M |0.51
BASELINE-SearchGraph | 100M | 1.67
BASELINE-FAISSHNSW | 100M | 21.40
HIOB | 100M  |    247.01
CRANBERRY  | 100M  |   589.76
SWANN* | 100M |  4866.21
UTokyo | 100M  |  OOM


# Task B

## 10 Million

| Team | #bits | Recall 
| --- | --- | ---:|
| HIOB | 1024 | 0.55
| HIOB | 256 | 0.33
| Baseline | 1024 | 0.24

## 30 Million

| Team | #bits | Recall 
| --- | --- | ---:|
| HIOB | 1024 | 0.57
| HIOB | 256 | 0.24
| Baseline | 1024 | 0.24

## 100 Million

| Team | #bits | Recall 
| --- | --- | ---:|
| HIOB | 1024 | 0.58
| Baseline | 1024 | 0.25
| HIOB | 256 | 0.20



# Task C

Indexing binary vectors. Bruteforce recall is around 0.24, we show the best performing parameters exceeding recall 0.22.


## 10 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
BASELINE-SearchGraph | 10M | 0.10
Bruteforce | 10M | 0.24
HIOB | 10M | 36.56
SWANN | 10M |  159.82

## 30 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
BASELINE-SearchGraph | 30M | 0.36
HIOB | 30M | 90.35  
Bruteforce | 30M | 246.95
SWANN | 30M |  717.54

## 100 Million

| Team | Size | Query time (in _seconds_) | 
| ---  | ---- |-----:|
BASELINE-SearchGraph | 100M | 1.09
Bruteforce | 100M | 816.93
SWANN | 100M |  3795.05
HIOB | 100M | ----

HIOB achieved only recall .17 on 100M.


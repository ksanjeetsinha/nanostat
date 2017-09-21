# NanoStat

Calculate various statistics from an Oxford Nanopore dataset in fastq, bam or albacore sequencing summary format.

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/wouter_decoster.svg?style=social&label=Follow%20%40wouter_decoster)](https://twitter.com/wouter_decoster)
[![install with conda](https://anaconda.org/bioconda/nanostat/badges/installer/conda.svg)](https://anaconda.org/bioconda/nanostat)
[![Build Status](https://travis-ci.org/wdecoster/nanostat.svg?branch=master)](https://travis-ci.org/wdecoster/nanostat)
[![Code Health](https://landscape.io/github/wdecoster/nanostat/master/landscape.svg?style=flat)](https://landscape.io/github/wdecoster/nanostat/master)


### INSTALLATION
```bash
pip install nanostat
```
or  
[![install with conda](https://anaconda.org/bioconda/nanostat/badges/installer/conda.svg)](https://anaconda.org/bioconda/nanostat)
```
conda install -c bioconda nanostat
```


### USAGE
```
NanoStat [-h] [-v] [-o OUTDIR] [-p PREFIX] [-t THREADS]
                (--fastq FASTQ | --summary SUMMARY | --bam BAM)

Get statistics of Oxford Nanopore read dataset.

Mandatory one of the following data sources:
--fastq FASTQ         Data is in fastq format.
--summary SUMMARY     Data is a summary file generated by albacore.
--bam BAM             Data as a sorted bam file.


Optional arguments:
  --readtype              Specify read type to extract from summary file
                        Options: 1D (default), 2D or 1D2
  -h, --help            show this help message and exit
  -v, --version         Print version and exit.
  -o, --outdir OUTDIR   Specify directory in which output has to be created.
  -p, --prefix PREFIX   Specify an optional prefix to be used for the output files.
  -t, --threads THREADS Set the allowed number of threads to be used by the script
                        This only applies to bam and fastq format as data source
```

## STATUS
[![Build Status](https://travis-ci.org/wdecoster/nanostat.svg?branch=master)](https://travis-ci.org/wdecoster/nanostat)
[![Code Health](https://landscape.io/github/wdecoster/nanostat/master/landscape.svg?style=flat)](https://landscape.io/github/wdecoster/nanostat/master)


### Example output
```
Number of reads:	408254
Total bases:	3508315665
Median read length:	5168.0
Mean read length:	8593.46
Readlength N50:	39346

Top 5 read lengths and their average basecall quality score:
Length: 255821bp	Q: 6.84
Length: 254573bp	Q: 7.09
Length: 253711bp	Q: 6.96
Length: 245784bp	Q: 6.98
Length: 245776bp	Q: 7.06

Top 5 average basecall quality scores and their read lengths:
Length: 407bp	Q: 16.22
Length: 880bp	Q: 16.18
Length: 729bp	Q: 16.12
Length: 1057bp	Q: 16.08
Length: 841bp	Q: 15.84

Number of reads and fraction above quality cutoffs:
Q5:	406428	99.55%
Q10:	305509	74.83%
Q15:	124	0.03%
Q20:	0	0.0%
```

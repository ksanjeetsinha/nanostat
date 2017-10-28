#! /usr/bin/env python
# wdecoster
'''
Calculate various statistics from an Oxford Nanopore dataset
in fastq, bam or albacore sequencing summary format.


NanoStat [-h] [-v] [-o OUTDIR] [-p PREFIX] [-t THREADS]
                (--fastq FASTQ | --summary SUMMARY | --bam BAM)

Get statistics of Oxford Nanopore read dataset.

Mandatory one of the following data sources:
--fastq FASTQ         Data is in fastq format.
--summary SUMMARY     Data is a summary file generated by albacore.
--bam BAM             Data as a sorted bam file.


Optional arguments:
  --readtype            Specify read type to extract from summary file
                        Options: 1D (default), 2D or 1D2
  -h, --help            show this help message and exit
  -v, --version         Print version and exit.
  -o, --outdir OUTDIR   Specify directory in which output has to be created.
  -n, --name NAME       Specify a custom filename/path for the output,
                        <stdout> for printing to stdout.
  -p, --prefix PREFIX   Specify an optional prefix to be used for the output files.
  -t, --threads THREADS Set the allowed number of threads to be used by the script
                        This only applies to bam and fastq format as data source
'''


from nanomath import write_stats
import nanoget
from argparse import ArgumentParser, HelpFormatter
import os
from nanostat.version import __version__
import textwrap as _textwrap


class CustomHelpFormatter(HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ', '.join(action.option_strings) + ' ' + args_string

    def _fill_text(self, text, width, indent):
        return ''.join(indent + line for line in text.splitlines(keepends=True))

    def _split_lines(self, text, width):
        text = self._whitespace_matcher.sub(' ', text).strip()
        return _textwrap.wrap(text, 80)


def custom_formatter(prog):
    return CustomHelpFormatter(prog)


def main():
    args = get_args()
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    sources = [args.fastq, args.bam, args.summary]
    sourcename = ["fastq", "bam", "summary"]
    datadf = nanoget.get_input(
        source=[n for n, s in zip(sourcename, sources) if s][0],
        files=[f for f in [args.fastq, args.bam, args.summary] if f][0],
        threads=args.threads,
        readtype=args.readtype,
        combine="track")
    if args.name:
        output = args.name
    else:
        output = os.path.join(args.outdir, args.prefix + "NanoStats.txt")
    write_stats(datadf, output)


def get_args():
    epilog = """EXAMPLES:
    NanoStat --fastq reads.fastq.gz --outdir statreports
    NanoStat --summary sequencing_summary1.txt sequencing_summary2.txt sequencing_summary3.txt --readtype 1D2
    NanoStat --bam alignment.bam alignment2.bam
    """
    parser = ArgumentParser(
        description="Calculate statistics of Oxford Nanopore read dataset.",
        epilog=epilog,
        formatter_class=custom_formatter,
        add_help=False)
    general = parser.add_argument_group(
        title='General options')
    general.add_argument("-h", "--help",
                         action="help",
                         help="show the help and exit")
    general.add_argument("-v", "--version",
                         help="Print version and exit.",
                         action="version",
                         version='NanoStat {}'.format(__version__))
    general.add_argument("-o", "--outdir",
                         help="Specify directory in which output has to be created.",
                         default=".")
    general.add_argument("-p", "--prefix",
                         help="Specify an optional prefix to be used for the output file.",
                         default="",
                         type=str)
    general.add_argument("-n", "--name",
                         help="Specify a custom filename/path for the output, <stdout> for printing to stdout.",
                         default="",
                         type=str)
    general.add_argument("-t", "--threads",
                         help="Set the allowed number of threads to be used by the script.",
                         default=4,
                         type=int,
                         metavar="N")
    inputoptions = parser.add_argument_group(
        title='Input options.')
    inputoptions.add_argument("--readtype",
                              help="Which read type to extract information about from summary. \
                              Options are 1D, 2D, 1D2",
                              default="1D",
                              choices=['1D', '2D', '1D2'])
    target = parser.add_argument_group(
        title="Input data sources, one of these is required.")
    mtarget = target.add_mutually_exclusive_group(
        required=True)
    mtarget.add_argument("--fastq",
                         help="Data is in one or more default fastq file(s).",
                         nargs='+',
                         metavar="file")
    mtarget.add_argument("--summary",
                         help="Data is in one or more summary file(s) generated by albacore.",
                         nargs='+',
                         metavar="file")
    mtarget.add_argument("--bam",
                         help="Data is in one or more sorted bam file(s).",
                         nargs='+',
                         metavar="file")
    return parser.parse_args()


if __name__ == '__main__':
    main()

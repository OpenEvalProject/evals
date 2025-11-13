# RNA polymerase errors cause splicing defects and can be regulated by differential expression of RNA polymerase subunits

## Authors

- Lucas B Carey<sup>1</sup> †

### Affiliations

1. Department of Experimental and Health Sciences Universitat Pompeu Fabra Barcelona Spain

† Corresponding author

## Abstract

Errors during transcription may play an important role in determining cellular phenotypes: the RNA polymerase error rate is >4 orders of magnitude higher than that of DNA polymerase and errors are amplified >1000-fold due to translation. However, current methods to measure RNA polymerase fidelity are low-throughout, technically challenging, and organism specific. Here I show that changes in RNA polymerase fidelity can be measured using standard RNA sequencing protocols. I find that RNA polymerase is error-prone, and these errors can result in splicing defects. Furthermore, I find that differential expression of RNA polymerase subunits causes changes in RNA polymerase fidelity, and that coding sequences may have evolved to minimize the effect of these errors. These results suggest that errors caused by RNA polymerase may be a major source of stochastic variability at the level of single cells.

## Materials and methods

### Counting RNA polymerase errors in already aligned ENCODE data

Much existing RNA-seq data is available as bam files aligned to the human genome. In order to bypass alignment, which is the most computationally expensive step of the pipeline, I developed a method capable of using RNA-seq reads aligned with spliced aligners. First, in order to avoid increased mismatch rates at splice junctions due to alignment problems with both spliced and unspliced reads, I used SAMtools (Li et al., 2009) and awk to remove all alignments that do not align along the full length of the genome (e.g., for 76 bp reads, only reads with a CIGAR flag of 76 M). The remaining reads weretrimmed (bamUtil, trimBam) to convert the first and last 10 bp of each read to Ns and set the quality strings to ‘!’. I then used samtools mpileup (-q30 –C50 –Q30) and custom perl code to count the number of reads and number of errors at each position in genome. Positions with too many errors (e.g., more than one read of the same nonreference base) were not counted.

### Measurement of error rates at splice junctions

I used the University of California Santa Cruz (UCSC) table browser (Karolchik, 2004) to download two bed files: hg19 EnsemblGenes introns with -10 bp flanking from each side, and another file with the introns and +10 bp flanking on either side. I then used bedtools (Quinlan and Hall, 2010) (bedtools flank -b 20 -l 0 and bedtools flank -l 20 -b 0) to generate bed files with intervals that contain the splicing donor and acceptor sites, respectively. In addition, I used bedtools getfasta on the +10 bp flanking bed file to keep only introns flanked by GT and AG donor and acceptor sites. The final result is a pair of bam files with intervals centered on the splicing donor or acceptor sites. I used this new bed file to count error rates around each splice junction. The error rate at each position (e.g., -10, -9, -8, etc. from the G at the 5’ donor site) is the sum of all errors at that position, divided by the sum of all reads. Positions are relative to the splicing feature, not to the genome, as error rates at any single genomic position are dominated by sampling bias. Per mono-, di-, and trinucleotide background error rates were-calculated using the same scripts, but without limiting mpileup to the splice junctions.

### Strain construction and RNA sequencing for RPB9 and DST1 strains

The parental strain DBY12394 (Mcisaac et al., 2013) (GAL2 + s288c repaired HAP1, ura3∆, leu2∆0::ACT1pr-Z3EV-NatMX) was transformed with a polymerase chain reaction (PCR) product (KanMX-Z3EVpr) to generate a genomically integrated inducible RPB9 (LCY143) or DST1 (LCY142). To induce various levels of expression, strains were re-grown in YPD + 0-, 3-, 6-, 12-, or 25-nM β-estradiol (Sigma, St. Louis, MO, USA, E4389) for more than 12 hr to a final OD600 of 0.1 – 0.4. Cellular RNA was extracted using the Epicenter MasterPure RNA Purification Kit, and Illumina sequencing libraries were prepared using the Truseq Stranded mRNA kit, and sequenced on an HiSeq2000 with at least 20,000,000 50 bp sequencing reads per sample.

I used bwa (Li and Durbin, 2009) (-n 2, to permit no more than two mismatches in a read) to align the yeast RNA-seq reads to the reference genome, and trimBam from bamUtil to mask the first and last 10 bp of each read. I used samtools mpileup (Li et al., 2009) (-q 30 -d 100000 -C50 –Q39) to count the number of reads and mismatches at each position in the genome, discarding low confidence mapping, reads that map to multiple positions, and low quality reads. Duplicate reads can be removed from the fastq file if the coverage is low enough so that all reads that map to identical  genome coordinates are expected be PCR duplicates from the same RNA fragment. This is the case for low coverage paired-end reads with a variable insert size, but not for very high coverage datasets or single-ended reads.

### Pre-existing RNA-seq datasets

For the intron retention analysis in human cells, data are from NCBI SRA PRJNA253670. Data for the elc4 and spt4 analysis are from PRJNA167772 and PRJNA148851, respectively. For RPB9 correlation, undefined data (SRA PRJNA30709) are all from the Gingeras lab at CSHL.

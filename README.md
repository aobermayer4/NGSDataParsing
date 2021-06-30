# NGSDataParsing

**basescovered(S).py scripts:** These scripts are used in the directory of interest that contains the BAM and BAI files and run to gather read depth for the mitochindrial DNA. The resulting run gives you the fraction of reads greater than 5 or 10 depth as well as the average and median read depth. The script ending in 'S' is when the mitochondrial reads are labeled 'chrM' and the script without an 'S' is when the mitochondrial reads are labeled 'MT'.

**basedepthsamp(MT or chrM):** These scripts are similar to above. You input /path/to/bam/files/ referenceFASTA.fai bamfilelist.txt depthdict10.txt depthdict5.txt. the bamfilelist will contain all bam files being ran. The depthdict files will be text files of two numpy arrays containing read depth summaries of all the samples input. One showing fraction of read depths greater than 10 with mean and median per sample and the other with read depths greater than 5 per sample with mean and median.

**vcf_ChoiceSearch.py:** This is an interactive script that generates a list of specified variants. You may choose to extract SNPs, insertions, deletions, positions with more than one variation, or a total list. The output gives tab delimited list of: Chromosome, Position (start), Position (end), Alternate, ID.

**vcf_af_search.py:** This is similar to vcf_ChoiceSearch.py, but it was made with regard to 1000 genome project data and when vcf is input from this it includes region specific allele frequency data for each SNP.

**snptr_cluster.py:** This script with take an SNP file that was generated from vcf_ChoiceSearch.py and add if the SNP was a transition or transversion.

**sampfind.py:** This script take a specific list of samples and run it against a VCF file of interest and output a similar output of vcf_ChoiceSearch.py but include sample data for the samples requested.

**vcf_snpfinder.py:** This script take input of a specified list of SNP IDs and reads it with a specified VCF file and extracts only the data for the specified SNPs in a format similar to vcf_ChoiceSearch.py.

These scripts are actively being modified and adjusted.

# NGSDataParsing

**RenamerByMap.py:** While observing CPTAC data and samples, I noticed that the names are not very intuitive, and just a string of characters. While I understand the reasoning behind this to prevent any bias when looking at the samples, it can make it difficult when each patient has 2-3 samples per and my current goal is looking at the patients haplogroup and I wan to look at their samples together more easily. Thankfully, GDC does provide a sample sheet which contains some metadata information on the samples such as the FileID, FileName, CaseID, SampleID, and SampleType in particular. In this script I am renaming the folders based on the SampleID and the first letter of the SampleType (P-Primary Tumor, S-Solid Tissue Normal, and B-Blood Derived Normal). This will be followed by renaming the files within in the same format but with their respective file extensions. The Sample Sheet provided by the GDC when I obtain my controlled access data allows for a useful map if I need to map any changed names back to their original and for verification.

The script works as intended although adjustments need to be made to take the spaces out of the GDC Sample Sheet header (which I did manually) and take the white space out of the SampleIDs that contain two samples separated by a comma and whitespace.

**basescovered(S).py scripts:** These scripts are used in the directory of interest that contains the BAM and BAI files and run to gather read depth for the mitochindrial DNA. The resulting run gives you the fraction of reads greater than 5 or 10 depth as well as the average and median read depth. The script ending in 'S' is when the mitochondrial reads are labeled 'chrM' and the script without an 'S' is when the mitochondrial reads are labeled 'MT'.

**basedepthsamp(MT or chrM):** These scripts are similar to above. You input /path/to/bam/files/ referenceFASTA.fai bamfilelist.txt depthdict10.txt depthdict5.txt. the bamfilelist will contain all bam files being ran. The depthdict files will be text files of two numpy arrays containing read depth summaries of all the samples input. One showing fraction of read depths greater than 10 with mean and median per sample and the other with read depths greater than 5 per sample with mean and median.

**vcf_ChoiceSearch.py:** This is an interactive script that generates a list of specified variants. You may choose to extract SNPs, insertions, deletions, positions with more than one variation, or a total list. The output gives tab delimited list of: Chromosome, Position (start), Position (end), Alternate, ID.

**vcf_af_search.py:** This is similar to vcf_ChoiceSearch.py, but it was made with regard to 1000 genome project data and when vcf is input from this it includes region specific allele frequency data for each SNP.

**snptr_cluster.py:** This script with take an SNP file that was generated from vcf_ChoiceSearch.py and add if the SNP was a transition or transversion.

**sampfind.py:** This script take a specific list of samples and run it against a VCF file of interest and output a similar output of vcf_ChoiceSearch.py but include sample data for the samples requested.

**vcf_snpfinder.py:** This script take input of a specified list of SNP IDs and reads it with a specified VCF file and extracts only the data for the specified SNPs in a format similar to vcf_ChoiceSearch.py.

These scripts are actively being modified and adjusted.

# Genomic stability of self-inactivating rabies

## Authors

- Ernesto Ciabatti<sup>1</sup> ([ORCID: 0000-0001-9361-5992](https://orcid.org/0000-0001-9361-5992)) †
- Ana González-Rueda<sup>1</sup>
- Daniel de Malmazet<sup>1</sup>
- Hassal Lee<sup>1</sup>
- Fabio Morgese<sup>1</sup>
- Marco Tripodi<sup>1</sup> ([ORCID: 0000-0002-6827-6690](https://orcid.org/0000-0002-6827-6690))

### Affiliations

1. MRC Laboratory of Molecular Biology Cambridge United Kingdom ([ROR:00tw3jy02](https://ror.org/00tw3jy02))

† Corresponding author

## Abstract

Transsynaptic viral vectors provide means to gain genetic access to neurons based on synaptic connectivity and are essential tools for the dissection of neural circuit function. Among them, the retrograde monosynaptic ΔG-Rabies has been widely used in neuroscience research. A recently developed engineered version of the ΔG-Rabies, the non-toxic self-inactivating (SiR) virus, allows the long term genetic manipulation of neural circuits. However, the high mutational rate of the rabies virus poses a risk that mutations targeting the key genetic regulatory element in the SiR genome could emerge and revert it to a canonical ΔG-Rabies. Such revertant mutations have recently been identified in a SiR batch. To address the origin, incidence and relevance of these mutations, we investigated the genomic stability of SiR in vitro and in vivo. We found that “revertant” mutations are rare and accumulate only when SiR is extensively amplified in vitro, particularly in suboptimal production cell lines that have insufficient levels of TEV protease activity. Moreover, we confirmed that SiR-CRE, unlike canonical ΔG-Rab-CRE or revertant-SiR-CRE, is non-toxic and that revertant mutations do not emerge in vivo during long-term experiments.

## Introduction

The development of innovative technologies to record and manipulate the activity of large populations of neurons (Jun et al., 2017; Lin and Schnitzer, 2016; Stirman et al., 2016; Yizhar et al., 2011) has had a transformative impact on systems neuroscience leading to a deeper understanding of how specific networks control essential aspects of animal behaviour (Fadok et al., 2017; Kohl et al., 2018; Stuber and Wise, 2016). In particular, the latest generation of molecular sensors and actuators allow researchers to visualize (Abdelfattah et al., 2019; Dana et al., 2019) and perturb (Kato et al., 2018; Shemesh et al., 2017) the activity of individual neurons with unprecedented genetic, spatial, and temporal resolution. However, strategies to express these tools in any desired neuron within a neural network structure remain scarce. Viral vectors represent the primary approach to deliver genetic materials to mammalian brains, with adeno associated viruses (AAV) rapidly becoming the primary choice to target neurons based on anatomical location, genetic identity, or projection pattern (Chan et al., 2017; Tenenbaum et al., 2004; Tervo et al., 2016). Nonetheless, transsynaptic viruses are the only vectors that are able to label cells based on their synaptic connectivity, permitting the functional dissection of neural circuits. Among them, the retrograde monosynaptic G-deleted Rabies virus (ΔG-Rabies) is the most sensitive and efficient transsynaptic retrograde tracer, widely used to highlight the structural organization of neural networks in mammals (Callaway and Luo, 2015; Stepien et al., 2010; Tripodi et al., 2011; Wickersham et al., 2007b). However, its toxicity has limited its use for functional experiments. Indeed, in the past few years, several strategies have been applied trying to overcome the known toxicity of rabies vectors and extending their use for long-term functional interrogation of neural circuits: the use of different viral strains (CVS-N2c) (Reardon et al., 2016), the conditional destabilization of viral proteins (Self-inactivating Rabies, SiR; Ciabatti et al., 2017) or the deletion of essential genes other than G (ΔGL-Rabies; Chatterjee et al., 2018).

All these approaches have advantages and disadvantages and collectively represent important improvements in the Rabies design. For example, the use of different parental strains in ΔG-Rabies vectors provide delayed mortality and improved tropism (Reardon et al., 2016), but do not overcome the continuous viral replication that eventually leads to toxicity. The deletion of genes other than G gave origin to effective axonal retrograde tracers (Chatterjee et al., 2018) but requires the expression of multiple transgenes for transsynaptic tracing experiments via other viruses or using transgenic animals, which have yet to be fully implemented and that risk recreating a fully functional ΔG-Rabies in the starter cells. The addition of regulatory elements to the rabies genome, as in the SiR design in which the rabies nucleoprotein (N) is conditionally targeted to the proteasome by a PEST sequence, has the advantage of abolishing continuous viral replication (Ciabatti et al., 2017). On the other hand, the known high mutation rate of RNA viruses (Drake and Holland, 1999; Sanjuán et al., 2010) poses the risk that naturally occurring mutations could emerge to selectively inactivate the added genetic sequence, hence potentially giving origin to toxic revertant mutants.

In its original design, SiR is produced from cDNA in conditions where PEST is constantly removed by the tobacco etch virus protease (TEVp) cleavage, which should prevent accumulations of PEST-targeting mutations. While it was suggested that such PEST-targeting mutations might be an unavoidable outcome of the SiR design (Matsuyama et al., 2019), here we show that such mutations, in fact, only accumulate when SiR is extensively amplified in cells expressing suboptimal levels of TEVp. Conversely, minimizing the number of passages in vitro and using high-TEVp expressing production cell lines prevents any appreciable accumulation of such mutations during SiR production.

The reported findings that ΔG-Rabies-CRE showed an apparently reduced cytotoxicity (Chatterjee et al., 2018) led to the suggestion that the CRE expression alone could dampen the toxicity of all ΔG-Rabies vectors, and hence of the SiR-CRE as well (Matsuyama et al., 2019). However, the survival of a fraction of ΔG-Rabies-CRE-infected neurons in CRE-reporter mice might be explained by the presence of a few naturally occurring defective viral particles that lack one or more key viral genes (Wiktor et al., 1977), which could effectively recapitulate the self-inactivating behaviour purposefully engineered in the SiR virus. Indeed, here we show that CRE expression alone is ineffective in dampening toxicity and that while SiR-CRE is entirely non-cytotoxic in cortical and sub-cortical regions for several months, canonical ΔG-Rabies-CRE displays a significant toxicity in vivo.

In summary, here we investigated the genomic stability of SiR and found that when produced in cells with high levels of TEVp with few rounds of amplification PEST-targeting mutations do not accumulate to appreciable levels. As expected, revertant-free SiR-CRE viruses but not Rab-CRE or PEST-mutated SiR-CRE are entirely non-toxic. Moreover, we show that PEST-targeting mutations do not accumulate at appreciable rate in vivo.

## Results

### De novo SiR productions do not accumulate revertant mutations

SiR self-inactivation depends on the proteasomal targeting of N by the c-terminal addition of a PEST sequence. The high rate of mutation in RNA viruses (10−6 to 10−4 substitutions per nucleotide per round of copying) (Sanjuán et al., 2010) could lead to the emergence of mutations targeting PEST. If these mutations generate a premature stop codon just upstream of the c-terminal PEST sequence they could effectively revert the SiR to a canonical and cytotoxic ΔG-Rabies. To address the issue of whether and/or to what extent the emergence of such ‘revertant’ mutants occurs, we generated eight independent SiR productions from cDNA following the protocol we previously described (Ciabatti et al., 2017). We produced viral genomic libraries for each preparation (50 clones/batch) for Sanger sequencing using primers carrying random octamers in order to identify individual particles (Figure 1A–B). Out of the 8 independent preparations for a total of 400 individually analysed particles, we did not identify particles harbouring the nonsense mutations described by Matsuyama and colleagues (Figure 1B and Table 11). The sequences’ analyses showed the presence of sporadic mutations across other genomic locations (Table 1) as expected given the rabies mutational rate. Notably, several clones per preparation had point mutations within the N/P intergenic region, suggesting that the stoppolyadenylation signal is permissive to single base mutations (Table 1). These data confirm that SiRs generated from cDNA as described in Ciabatti et al., 2017 do not accumulate mutations upstream the PEST domain at appreciable levels.

![Figure 1.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig1-v2.jpg)

**Figure 1.:** (A) Scheme of experimental strategy to identify the emergence of “revertant” mutations during SiR production. 8 independent SiR preparations were rescued from cDNA and genomic RNA were extracted, treated with DNAse I, subjected to RT-PCR to amplify N-TEVs-PEST coding sequence and used to generate libraries for Sanger sequencing (50 clones per preparation were sequenced). (B) Example of sequencing results from one SiR preparation showing no mutations at the end of N. Symbols (#) show the position of previously identified mutations, marks on the sequences indicates the presence of mutations in different positions.

**Table 1.**
 List of detected mutations in SiR viruses rescued from cDNA divided by batch (50 individual clones per batch).The position of the mutations is calculated referring to +1 as the first base of the nucleoprotein N coding sequence.


<table>
  <thead>
    <tr>
      <th colspan="6">Sanger sequencing results of SiRs rescued from cDNA</th>
    </tr>
    <tr>
      <th></th>
      <th>Batch A</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>Clones</th>
      <th>Sequence</th>
      <th>Position</th>
      <th>Mutation</th>
      <th>Effect on CDS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Upstream N</td>
      <td>1/50</td>
      <td>GAT &gt;GAC</td>
      <td>–54</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;AAG</td>
      <td>–18</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>GCC &gt;GCT</td>
      <td>+186</td>
      <td>Substitution</td>
      <td>Synonymous A62</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTT &gt;TTTT</td>
      <td>+243</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAG &gt;A-G</td>
      <td>+485</td>
      <td>Deletion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ATG &gt;CTG</td>
      <td>+562</td>
      <td>Substitution</td>
      <td>Missense M188L</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GTG &gt;G--</td>
      <td>+677/8</td>
      <td>Deletion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ACG &gt;ACCG</td>
      <td>+983</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GAA &gt;AAA</td>
      <td>+1,093</td>
      <td>Substitution</td>
      <td>E365K</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TCA &gt;CCA</td>
      <td>+1,276</td>
      <td>Substitution</td>
      <td>S426P</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>4/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CCC &gt;CCA</td>
      <td>+1,581</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Batch B</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Clones</td>
      <td>Sequence</td>
      <td>Position</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>1/50</td>
      <td>AAC &gt;A-C</td>
      <td>–63</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CAA &gt;CA-</td>
      <td>–60</td>
      <td>Deletion</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CTA &gt;CTG</td>
      <td>-3</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>TTT &gt;TTTT</td>
      <td>+243</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GAC &gt;GAA</td>
      <td>+501</td>
      <td>Substitution</td>
      <td>D167E</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAT &gt;AAC</td>
      <td>+588</td>
      <td>Substitution</td>
      <td>Synonymous N196</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GCT &gt;GCC</td>
      <td>+1,002</td>
      <td>Substitution</td>
      <td>Synonymous A334</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,056</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>1/50</td>
      <td>TCC &gt;TGC</td>
      <td>+1,385</td>
      <td>Substitution</td>
      <td>Missense S462C in GSG linker after TEVs</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>1/50</td>
      <td>TAT &gt;TAA</td>
      <td>+1,554</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>2/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>1/50</td>
      <td>GAA &gt;GAG</td>
      <td>+1,671</td>
      <td>Substitution</td>
      <td>Synonymous E23</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CTG &gt;CCG</td>
      <td>+1,775</td>
      <td>Substitution</td>
      <td>Missense L58P</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GGA &gt;TGA</td>
      <td>+2014</td>
      <td>Deletion</td>
      <td>Nonsense G138&gt;STOP</td>
    </tr>
    <tr>
      <td></td>
      <td>Batch C</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Clones</td>
      <td>Sequence</td>
      <td>Position</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>2/50</td>
      <td>AAA &gt;AAAA</td>
      <td>–43</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>TGT &gt;TTT</td>
      <td>+212</td>
      <td>Substitution</td>
      <td>Missense C71F</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AGA &gt;AGG</td>
      <td>+1,074</td>
      <td>Substitution</td>
      <td>Synonymous R358</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GGT &gt;GAT</td>
      <td>+1,190</td>
      <td>Substitution</td>
      <td>Missense G397D</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>1/50</td>
      <td>AAA &gt;AAG</td>
      <td>+1,569</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>3/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;AA-</td>
      <td>+1,571</td>
      <td>Deletion</td>
      <td></td>
    </tr>
    <tr>
      <td>P</td>
      <td>1/50</td>
      <td>CAA &gt;AAA</td>
      <td>+1,720</td>
      <td>Substitution</td>
      <td>Missense Q40K</td>
    </tr>
    <tr>
      <td></td>
      <td>Batch D</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Clones</td>
      <td>Sequence</td>
      <td>Position</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>AAG &gt;AGG</td>
      <td>+113</td>
      <td>Substitution</td>
      <td>Missense K38R</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;CAA</td>
      <td>+295</td>
      <td>Substitution</td>
      <td>Missense K99Q</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CAT &gt;AAT</td>
      <td>+655</td>
      <td>Substitution</td>
      <td>Missense H219N</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TCA &gt;TCC</td>
      <td>+873</td>
      <td>Substitution</td>
      <td>Synonymous S291</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ACC &gt;AAC</td>
      <td>+1,196</td>
      <td>Substitution</td>
      <td>Missense T399N</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>3/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ATC &gt;ATT</td>
      <td>+1,596</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>1/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,671</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CGT &gt;CTA</td>
      <td>+1,878</td>
      <td>Substitution</td>
      <td>Synonymous L92</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AGA &gt;AGT</td>
      <td>+1941</td>
      <td>Substitution</td>
      <td>Missense R113S</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GGA &gt;GGG</td>
      <td>+2016</td>
      <td>Substitution</td>
      <td>Synonymous G138</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ACT &gt;ACA</td>
      <td>+2046</td>
      <td>Substitution</td>
      <td>Synonymous T148</td>
    </tr>
    <tr>
      <td></td>
      <td>Batch E</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Clones</td>
      <td>Sequence</td>
      <td>Position</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>1/50</td>
      <td>CCA &gt;CC-</td>
      <td>–57</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>CCT &gt;CAT</td>
      <td>+200</td>
      <td>Substitution</td>
      <td>Missense P67H</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTT &gt;TTTT</td>
      <td>+243</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GGA &gt;GAA</td>
      <td>+371</td>
      <td>Substitution</td>
      <td>Missense G124E</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ACA &gt;ACG</td>
      <td>+387</td>
      <td>Substitution</td>
      <td>Synonymous T129</td>
    </tr>
    <tr>
      <td></td>
      <td>2/50</td>
      <td>GAC &gt;GAT</td>
      <td>+393</td>
      <td>Substitution</td>
      <td>Synonymous D131</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CAC &gt;C--</td>
      <td>+551/2</td>
      <td>Deletion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ACT &gt;AAT</td>
      <td>+557</td>
      <td>Substitution</td>
      <td>T186N</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTT &gt;TTTT</td>
      <td>+779</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>1/50</td>
      <td>CAT &gt;CAC</td>
      <td>+1,560</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;AAC</td>
      <td>+1,570</td>
      <td>Substitution</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>4/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ATC &gt;ATT</td>
      <td>+1,596</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>1/50</td>
      <td>GAA &gt;GGA</td>
      <td>+1,667</td>
      <td>Substitution</td>
      <td>Missense E22G</td>
    </tr>
    <tr>
      <td></td>
      <td>Batch F</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Clones</td>
      <td>Sequence</td>
      <td>Position</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>1/50</td>
      <td>ACC &gt;AC-</td>
      <td>–58</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CAG &gt;CA-</td>
      <td>–56</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TCA &gt;TCG</td>
      <td>–52</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;AAAA</td>
      <td>–43</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAG &gt;AA-</td>
      <td>–22</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>TTT &gt;TTTTT</td>
      <td>+243/4</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTG &gt;TCG</td>
      <td>+434</td>
      <td>Substitution</td>
      <td>Missense L145S</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTT &gt;TT-</td>
      <td>+534</td>
      <td>Deletion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GCA &gt;GTA</td>
      <td>+767</td>
      <td>Substitution</td>
      <td>Missense A256V</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ACA &gt;ATA</td>
      <td>+836</td>
      <td>Substitution</td>
      <td>Missense T279I</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+908</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>321 bp</td>
      <td>+1041–1,362</td>
      <td>Deletion</td>
      <td>Deletion of C-terminal of N in frame with PEST domain</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GGA &gt;GGG</td>
      <td>+1,038</td>
      <td>Substitution</td>
      <td>Synonymous G346</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>4/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>1/50</td>
      <td>CCT &gt;CCC</td>
      <td>+1,626</td>
      <td>Substitution</td>
      <td>Synonymous P8</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GAA &gt;GGA</td>
      <td>+1,727</td>
      <td>Substitution</td>
      <td>Missense E42G</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTT &gt;TTC</td>
      <td>+1,845</td>
      <td>Substitution</td>
      <td>Synonymous F81</td>
    </tr>
    <tr>
      <td></td>
      <td>Batch G</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Clones</td>
      <td>Sequence</td>
      <td>Position</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>1/50</td>
      <td>CCA &gt;CC-</td>
      <td>–57</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;AA-</td>
      <td>–16</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>GCA &gt;GTA</td>
      <td>+290</td>
      <td>Substitution</td>
      <td>Missense A97V</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CAT &gt;GAT</td>
      <td>+409</td>
      <td>Substitution</td>
      <td>Missense H137D</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTT &gt;TT-</td>
      <td>+534</td>
      <td>Deletion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TAT &gt;TGT</td>
      <td>+1,271</td>
      <td>Substitution</td>
      <td>Missense Y424C</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GCC &gt;GTC</td>
      <td>+1,316</td>
      <td>Substitution</td>
      <td>Missense A439V</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>4/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>1/50</td>
      <td>AAA &gt;CAA</td>
      <td>+1,786</td>
      <td>Substitution</td>
      <td>Missense K62Q</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GAA &gt;GGA</td>
      <td>+1,823</td>
      <td>Substitution</td>
      <td>Missense E74G</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>CGA &gt;CAA</td>
      <td>+1,834</td>
      <td>Substitution</td>
      <td>Missense R78Q</td>
    </tr>
    <tr>
      <td></td>
      <td>Batch H</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Clones</td>
      <td>Sequence</td>
      <td>Position</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>1/50</td>
      <td>AAA &gt;AAAA</td>
      <td>–43</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAC &gt;AA-</td>
      <td>–42</td>
      <td>Deletion</td>
      <td></td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>1/50</td>
      <td>TTA &gt;CTA</td>
      <td>+145</td>
      <td>Substitution</td>
      <td>Synonymous L49</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>ATG &gt;ATA</td>
      <td>+234</td>
      <td>Substitution</td>
      <td>Missense M78I</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>TTT &gt;TTTT</td>
      <td>+243</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAA &gt;CAA</td>
      <td>+295</td>
      <td>Substitution</td>
      <td>Missense K99Q</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GAT &gt;AAT</td>
      <td>+301</td>
      <td>Substitution</td>
      <td>Missense D101N</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GGA &gt;AGA</td>
      <td>+622</td>
      <td>Substitution</td>
      <td>Missense G208R</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GCT &gt;TCT</td>
      <td>+838</td>
      <td>Substitution</td>
      <td>Missense A280S</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GGC &gt;G-C</td>
      <td>+1,028</td>
      <td>Deletion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>GAC &gt;AAC</td>
      <td>+1,132</td>
      <td>Substitution</td>
      <td>Missense D378N</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>1/50</td>
      <td>CTG &gt;CTA</td>
      <td>+1,437</td>
      <td>Substitution</td>
      <td>Synonymous L16 in PEST domain</td>
    </tr>
    <tr>
      <td>Intergenic N/P</td>
      <td>3/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,571</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>1/50</td>
      <td>AAC &gt;AAA</td>
      <td>+1,592</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>1/50</td>
      <td>AAA &gt;AAAA</td>
      <td>+1,788</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
  </tbody>
</table>

### Analysis of molecular mechanisms underpinning the potential emergence of SiR revertant mutants

Although we found no indication of emergence of PEST-targeting mutations when SiR is rescued from cDNA, a recent report finding two batches of PEST-mutated SiR (Matsuyama et al., 2019) unarguably points to the possibility of emergence of these mutations under certain conditions. Hence, we sought to determine which conditions might favour the accumulation of revertant mutants. In the SiR design, the PEST sequence is fused to the N protein through a cleavable linker that allows its efficient production from TEVp-expressing packaging cells (Ciabatti et al., 2017). The constant removal of PEST ensures that naturally occurring mutations that inactivate PEST do not provide advantage over non-mutated particles. However, we reasoned that with suboptimal TEVp activity PEST-mutants may display faster replication kinetics than SiR particles, and might eventually accumulate in the population, as in a directed-evolution experiment. Thus, we hypothesised that two factors might prominently affect the emergence of revertants: 1. low TEVp levels in packaging cells and 2. excessive rounds of amplification of SiR in vitro. First, we investigated TEVp activity in packaging cells over time by producing HEK293T cells expressing TEVp and Gsad (HEK-TGG) as previously described (Ciabatti et al., 2017). After selecting for TEVp-expressing cells with puromycin HEK-TGG where cultured for multiple passages in medium containing different level of antibiotic (puromycin 0 μg/ml, 1 μg/ml, 2 μg/ml; Figure 2A). TEVp activity was then assessed every 2 passages by transfecting a TEVp reporter (Gray et al., 2010) and analysing TEVp site (TEVs) cleavage by western blot (Figure 2B, Figure 2—figure supplement 1). We found that the TEVp-dependent cleavage of the overexpressed reporter decreased in HEK-TGG after amplification and by passage 6 (P6) was less than half the initial level (from 31.7±2.4% at P0 to 14.7 ± 1.7% and 13.8 ± 1.2% with 1 μg/μl and 2 μg/μl puromycin, respectively; Figure 2B–C). Importantly, amplification in the absence of antibiotic pressure quickly reduced TEVp activity, decreasing by one order of magnitude by P6 (31.7 ± 2.4% at P0; 7.7±1.3% at P2; 3.1±0.2% at P6 without puromycin; Figure 2B–C). This suggests that extensive amplification of HEK-TGG leads to selection of clones with suboptimal TEVp expression, particularly in absence of antibiotic pressure.

![Figure 2.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig2-v2.jpg)

**Figure 2.:** (A) HEK-TGG packaging cells were amplified for several passages in absence or presence (1 or 2 μg/ml) of puromycin selection. (B) TEVp-dependent cleavage of TEVp-activity reporter was analysed by western blot in HEK-TGG at different amplification passages. (C) Quantification of TEVp-activity in packaging cells over time in presence or absence of antibiotic pressure. (mean ± SEM, n=3) (D) Experimental design to assess emergence of mutations in SiR preparations after multiple passages of amplification in high TEVp (HEK-TGG P0) or low TEVp HEK-TGG (HEK-TGG P8, without puromycin selection). (E) Quantification of frequency of the accumulation of PEST-targeting mutations over time that prevent translation of PEST domain (mean ± SEM, n=4 independent viral preparation). (F) Summary of the single nucleotide polymorphisms (SNPs) in the coding sequence (CDS) of N-TEVsPEST that reached threshold at P8 (mean ± SEM, n=4; n.d. indicates that the mutations were not detected above threshold). Top scheme shows the position of PEST-inactivating mutations.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Scheme of the TEVp activity reporter. (B) Original western blots stained with an anti-V5 antibody with the representative lanes used to generate Figure 2B.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Scheme of the strategy to sequence SiR preparations using SMRT NGS technology from Pacbio. Amplicons of the entire coding sequence of N-TEVs-PEST gene are generated by RT-PCR. Unique Molecular Identifier (UMI) of 10 nucleotides is added during retrotranscription to each genomic molecule and sample specific barcodes of 16 nucleotides are added at the two ends during subsequent PCR. SMRT bell libraries are generated by ligating the provided adapters to generate circular DNA molecules that are sequenced continuously for multiple passages. Subreads are used to generate high-fidelity consensus sequences that are demultiplexed using the 16 nt barcodes, deduplicated using the UMIs and aligned to the reference for variant calling.

To test the dependence of the emergence of revertant mutations on TEVp activity in the packaging cells, and investigate the accumulation kinetics of potential mutants, we amplified four independent (sequenced) revertant-free SiR preparations in vitro in low- and high-TEVp conditions for several passages. Every two passages, genomic libraries for each viral preparation were produced by reverse-transcription of the RNA genomes using primers barcoded with unique molecular identifiers (UMI, random decamer) and PCR amplifying an amplicon containing the N-TEVs-PEST gene. Then, SiR libraries were analysed by long-read next generation sequencing (NGS) using single molecule, real-time (SMRT) PacBio technology (Rhoads and Au, 2015; Figure 2D and Figure 2—figure supplement 1). SMRT sequencing employs the generation of circular molecules from the N-TEVs-PEST amplicons that are replicated for several passages by a polymerase so that individual sub-reads can be combined to generate high-quality consensus sequences (sequencing accuracy ≥98% with 3 passages; Figure 2—figure supplement 2). Since SMRT technology is particularly prone to false-positive insertion and deletions (INDELs; Carneiro et al., 2012; Dohm et al., 2020) and all previously reported PEST-targeting mutations were substitutions (Matsuyama et al., 2019), we restricted our analysis to substitutions (single-nucleotide polymorphism, SNP) above 2% threshold. We considered a PEST-targeting mutation to be any non-synonymous substitution targeting either N or TEVs-PEST sequences. In accordance with our hypothesis, the extensive amplification of SiR in vitro led to the emergence of revertants that can accumulate within the SiR population, especially in lowTEVp packaging cells (16% ± 2% of sequences containing a revertant mutation at P8 in lowTEVp cells; Figure 2E, Table 2). On the other hand, PEST-targeting mutations remained below 5% even after 8 rounds of amplification when SiR was amplified in high-TEVp cells (4% ± 2% of sequences containing a revertant mutation at P8 in high-TEVp cells; Figure 2E, Table 2). Notably, all PEST-inactivating mutations detected in this experiment were single base substitutions introducing a premature stop codon prior to TEVs either at the last amino acid of N or immediately after (d.C1349G and d.G1357T, leading to stop insertion at S450 and G453, respectively; Figure 2F, Table 2), which also accounted for the large majority of revertant particles reported by Matsuyama et al., 2019. Thus, in order to avoid the accumulation of revertant mutants, SiR viruses should be only amplified in high-TEVp, low-passage packaging cells for the minimum required number of passages.

**Table 2.**
 List of detected mutations above 2% thresholds in SiR viruses amplified in high- and low-TEVp packaging cells sequenced by SMRT NGS sequencing.The position of the mutations is defined considering +1 the first base of the nucleoprotein N coding sequence.


<table>
  <thead>
    <tr>
      <th colspan="7">NGS sequencing results of SiRs amplified for multiple passages in vitro</th>
    </tr>
    <tr>
      <th colspan="3">SIR-A-P0 bc1—bc2</th>
      <th colspan="4"></th>
    </tr>
    <tr>
      <th></th>
      <th>Position</th>
      <th>Variant</th>
      <th>N (q&gt;20)</th>
      <th>Freq %</th>
      <th>Mutation</th>
      <th>Effect on CDS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>302/6608</td>
      <td>4.5%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>266/6598</td>
      <td>4.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>190/6595</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>732/6556</td>
      <td>11.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-P0 bc1—bc3</td>
      <td></td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>276/6045</td>
      <td>4.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>274/6037</td>
      <td>4.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>180/6036</td>
      <td>3.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,359</td>
      <td>A&gt;T</td>
      <td>246/5879</td>
      <td>4.2%</td>
      <td>Substitution</td>
      <td>Silent G453</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>729/6556</td>
      <td>12.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-P0 bc1—bc4</td>
      <td></td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>256/5137</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>227/5137</td>
      <td>4.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>167/5138</td>
      <td>3.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>598/5140</td>
      <td>11.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-P0 bc1—bc5</td>
      <td></td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>249/5419</td>
      <td>4.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>229/5419</td>
      <td>4.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>125/5422</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>612/5420</td>
      <td>11.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-HighTEVp-P2 bc2—bc4</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>245/5934</td>
      <td>4.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>297/5933</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>157/5938</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>634/5935</td>
      <td>10.7%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-HighTEVp-P2 bc2—bc5</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>281/5750</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>272/5752</td>
      <td>4.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>170/5752</td>
      <td>3.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>625/5749</td>
      <td>10.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-HighTEVp-P2 bc2—bc6</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>236/4773</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>241/4772</td>
      <td>5.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>137/4774</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>489/4776</td>
      <td>10.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-HighTEVp-P2 bc2—bc6</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>260/5591</td>
      <td>4.7%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>238/5595</td>
      <td>4.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>150/5597</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>550/5594</td>
      <td>9.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-LowTEVp-P2 bc1—bc6</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>197/3891</td>
      <td>5.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>194/3891</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>116/3892</td>
      <td>3.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>447/3891</td>
      <td>11.5%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-LowTEVp-P2 bc1—bc7</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>244/5050</td>
      <td>4.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>227/5055</td>
      <td>4.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>162/5055</td>
      <td>3.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>503/5055</td>
      <td>10.0%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-LowTEVp-P2 bc1—bc8</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>266/5050</td>
      <td>5.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>248/5050</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>146/5056</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>547/5054</td>
      <td>10.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-LowTEVp-P2 bc1—bc9</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>200/5295</td>
      <td>3.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>204/5295</td>
      <td>3.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>141/5297</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>456/5297</td>
      <td>8.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-HighTEVp-P4 bc2—bc8</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>225/5803</td>
      <td>3.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>154/5805</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>276/5806</td>
      <td>4.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>158/5807</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>134/5745</td>
      <td>2.3%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>536/5803</td>
      <td>9.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-HighTEVp-P4 bc2—bc10</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>270/5572</td>
      <td>4.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>223/5572</td>
      <td>4.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>155/5571</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>590/5576</td>
      <td>10.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-HighTEVp-P4 bc2—bc11</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>233/5581</td>
      <td>4.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>114/5581</td>
      <td>2.0%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>272/5499</td>
      <td>4.9%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>252/5582</td>
      <td>4.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>149/5581</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>248/5528</td>
      <td>4.5%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>573/5579</td>
      <td>10.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-HighTEVp-P4 bc2—bc12</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>200/6116</td>
      <td>3.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>219/6117</td>
      <td>3.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>160/6119</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>456/6120</td>
      <td>7.5%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-LowTEVp-P4 bc1—bc10</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>239/4681</td>
      <td>5.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>114/4682</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>242/4683</td>
      <td>5.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>131/4684</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+1,053</td>
      <td>+A</td>
      <td>97/4683</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>170/4650</td>
      <td>3.7%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>570/4683</td>
      <td>12.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-LowTEVp-P4 bc1—bc11</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>255/4757</td>
      <td>5.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>245/4758</td>
      <td>5.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>141/4758</td>
      <td>3.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>551/4757</td>
      <td>11.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-LowTEVp-P4 bc1—bc12</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>268/5461</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>160/5403</td>
      <td>3.0%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>231/5463</td>
      <td>4.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>156/5466</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>705/5286</td>
      <td>13.3%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>538/5464</td>
      <td>9.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-LowTEVp-P4 bc2—bc3</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>266/5841</td>
      <td>4.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>246/5838</td>
      <td>4.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+574</td>
      <td>-N</td>
      <td>140/5834</td>
      <td>2.4%</td>
      <td>Deletion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>156/5833</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>200/5737</td>
      <td>3.5%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>529/5818</td>
      <td>9.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-HighTEVp-P6 bc5—bc6</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>604/6567</td>
      <td>9.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>555/6349</td>
      <td>8.7%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>227/6565</td>
      <td>3.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>157/6565</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>543/6565</td>
      <td>8.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>132/6565</td>
      <td>2.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>175/6566</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>337/6569</td>
      <td>5.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>767/6317</td>
      <td>12.1%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>1032/6583</td>
      <td>15.7%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>155/6584</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-HighTEVp-P6 bc5—bc7</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>624/6752</td>
      <td>9.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>202/6754</td>
      <td>3.0%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>243/6754</td>
      <td>3.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>1180/6296</td>
      <td>18.7%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>216/6752</td>
      <td>3.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>185/6751</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>559/6751</td>
      <td>8.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>138/6751</td>
      <td>2.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>197/6753</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>147/6753</td>
      <td>2.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>330/6753</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>965/6766</td>
      <td>14.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>187/6769</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-HighTEVp-P6 bc5—bc8</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>578/6166</td>
      <td>9.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>205/6166</td>
      <td>3.3%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>298/6166</td>
      <td>4.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>3305/5625</td>
      <td>58.8%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>179/6166</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>171/6165</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>514/6164</td>
      <td>8.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>158/6166</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>318/6170</td>
      <td>5.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>436/5995</td>
      <td>7.3%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>1019/6184</td>
      <td>16.5%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>165/6185</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-HighTEVp-P6 bc5—bc9</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>562/6355</td>
      <td>8.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>228/6356</td>
      <td>3.6%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>314/6356</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>2816/5789</td>
      <td>48.6%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-9</td>
      <td>A&gt;T</td>
      <td>139/6104</td>
      <td>2.3%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-6</td>
      <td>C&gt;T</td>
      <td>176/6275</td>
      <td>2.8%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-5</td>
      <td>C&gt;A</td>
      <td>121/5995</td>
      <td>2.0%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>175/6357</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>474/6358</td>
      <td>7.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>131/6358</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>167/6359</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>316/6360</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>947/6365</td>
      <td>14.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>139/6365</td>
      <td>2.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-LowTEVp-P6 bc4—bc5</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>588/6703</td>
      <td>8.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>369/6525</td>
      <td>5.7%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>259/6704</td>
      <td>3.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>173/6704</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>584/6703</td>
      <td>8.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+246</td>
      <td>+G</td>
      <td>145/6703</td>
      <td>2.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>196/6704</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>366/6705</td>
      <td>5.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>681/6468</td>
      <td>10.5%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>1035/6711</td>
      <td>15.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>161/6711</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-LowTEVp-P6 bc4—bc6</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>550/6112</td>
      <td>9.0%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>317/5985</td>
      <td>5.3%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>186/6117</td>
      <td>3.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>131/6117</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>486/6116</td>
      <td>7.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>148/6118</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>125/6120</td>
      <td>2.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>303/6119</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>360/5983</td>
      <td>6.0%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>946/6133</td>
      <td>15.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>138/6133</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-LowTEVp-P6 bc4—bc7</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>494/5209</td>
      <td>9.5%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>123/5209</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>2864/4984</td>
      <td>5.7%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>167/5210</td>
      <td>3.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>136/5210</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>400/5210</td>
      <td>7.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>123/5210</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>146/5213</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>261/5214</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>546/5066</td>
      <td>10.8%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>816/5212</td>
      <td>15.7%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>120/5212</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-LowTEVp-P6 bc4—bc7</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>492/5279</td>
      <td>9.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>114/5279</td>
      <td>2.2%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>119/5279</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>1553/5049</td>
      <td>30.8%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-9</td>
      <td>A&gt;T</td>
      <td>104/5189</td>
      <td>2.0%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>163/5279</td>
      <td>3.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>129/5279</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>434/5279</td>
      <td>8.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>106/5279</td>
      <td>2.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>148/5281</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>120/5281</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>279/5281</td>
      <td>5.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>831/5281</td>
      <td>15.7%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>123/5281</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-HighTEVp-P8 bc6—bc7</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>541/6868</td>
      <td>7.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>299/6868</td>
      <td>4.4%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>431/6868</td>
      <td>6.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>3684/6150</td>
      <td>60.0%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>198/6867</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>157/6867</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>583/6867</td>
      <td>8.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>138/6867</td>
      <td>2.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>181/6868</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>342/6870</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>651/6620</td>
      <td>9.8%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>952/6896</td>
      <td>13.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>144/6898</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-HighTEVp-P8 bc6—bc8</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>571/6246</td>
      <td>9.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>182/6246</td>
      <td>2.9%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>319/6246</td>
      <td>5.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>3836/5763</td>
      <td>66.6%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–18</td>
      <td>A&gt;C</td>
      <td>171/5940</td>
      <td>2.9%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>197/6247</td>
      <td>3.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>167/6247</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>486/6247</td>
      <td>7.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>145/6248</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>149/6249</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>323/6251</td>
      <td>5.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>365/6068</td>
      <td>6.0%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>927/6259</td>
      <td>14.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>152/6259</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-HighTEVp-P8 bc6—bc9</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>598/6403</td>
      <td>9.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>6024/6304</td>
      <td>95.6%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>200/6404</td>
      <td>3.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>146/6404</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>518/6405</td>
      <td>8.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>158/6405</td>
      <td>2.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>172/6406</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>311/6407</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>986/6410</td>
      <td>15.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>139/6408</td>
      <td>2.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-HighTEVp-P8 bc6—bc10</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>482/5760</td>
      <td>8.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>5092/5625</td>
      <td>9.1%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–18</td>
      <td>A&gt;G</td>
      <td>155/5609</td>
      <td>2.8%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-9</td>
      <td>A&gt;T</td>
      <td>247/5402</td>
      <td>4.6%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-9</td>
      <td>A&gt;G</td>
      <td>449/5402</td>
      <td>8.3%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-9</td>
      <td>+G</td>
      <td>120/5761</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-6</td>
      <td>C&gt;T</td>
      <td>680/5586</td>
      <td>12.2%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-6</td>
      <td>+T</td>
      <td>167/5761</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-5</td>
      <td>C&gt;A</td>
      <td>153/5412</td>
      <td>2.8%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>163/5763</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>119/5763</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>414/5763</td>
      <td>7.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>119/5764</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>127/5764</td>
      <td>2.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>291/5764</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>861/5766</td>
      <td>14.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>137/5766</td>
      <td>2.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-A-LowTEVp-P8 bc4—bc9</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>646/7058</td>
      <td>9.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>252/7059</td>
      <td>3.6%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>417/7059</td>
      <td>5.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>2752/6358</td>
      <td>43.3%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-6</td>
      <td>C&gt;T</td>
      <td>171/6942</td>
      <td>2.5%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-5</td>
      <td>C&gt;A</td>
      <td>542/6530</td>
      <td>8.3%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>346/7058</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>178/7058</td>
      <td>2.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>622/7058</td>
      <td>8.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>161/7058</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>194/7059</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>150/7060</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>345/7060</td>
      <td>4.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+795</td>
      <td>T&gt;C</td>
      <td>1604/6265</td>
      <td>25.6%</td>
      <td>Substitution</td>
      <td>Silent F265</td>
    </tr>
    <tr>
      <td></td>
      <td>+795</td>
      <td>+C</td>
      <td>318/7061</td>
      <td>4.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>1122/6684</td>
      <td>16.8%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>1079/7085</td>
      <td>15.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>161/7090</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-B-LowTEVp-P8 bc4—bc10</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>647/6759</td>
      <td>9.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>-N</td>
      <td>242/6761</td>
      <td>3.6%</td>
      <td>Deletion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>371/6761</td>
      <td>5.5%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>2200/6168</td>
      <td>35.7%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–18</td>
      <td>A&gt;C</td>
      <td>400/6309</td>
      <td>6.3%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>224/6761</td>
      <td>3.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>157/6761</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>575/6760</td>
      <td>8.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>189/6764</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>353/6763</td>
      <td>5.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+1,349</td>
      <td>C&gt;A</td>
      <td>144/6671</td>
      <td>2.2%</td>
      <td>Substitution</td>
      <td>Missense S450X</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>1192/6372</td>
      <td>18.7%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>1026/6769</td>
      <td>15.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>173/6772</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="3">SIR-C-LowTEVp-P8 bc4—bc11</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>614/6893</td>
      <td>8.9%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>261/6893</td>
      <td>3.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>5317/6466</td>
      <td>82.2%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>215/6894</td>
      <td>3.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>564/6894</td>
      <td>8.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>207/6895</td>
      <td>3.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>364/6895</td>
      <td>5.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>1013/6551</td>
      <td>15.5%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>1053/6920</td>
      <td>15.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="3">SIR-D-LowTEVp-P8 bc4—bc12</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>541/5872</td>
      <td>9.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–20</td>
      <td>+G</td>
      <td>190/5872</td>
      <td>3.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–19</td>
      <td>A&gt;G</td>
      <td>4259/5565</td>
      <td>76.5%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>-9</td>
      <td>A&gt;T</td>
      <td>141/5738</td>
      <td>2.5%</td>
      <td>Substitution</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>168/5876</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>154/5876</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>491/5876</td>
      <td>8.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>133/5876</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+332</td>
      <td>+A</td>
      <td>123/5876</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>152/5876</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>134/5876</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>324/5876</td>
      <td>5.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>521/5707</td>
      <td>9.1%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>996/5881</td>
      <td>17.0%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>150/5882</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
  </tbody>
</table>

### Difference in cytotoxicity between ΔG-Rabies, PEST-mutant SiR and SiR

In the recent report of Matsuyama et al., 2019 the authors showed that PEST-mutant SiR is cytotoxic in vivo, which is the obvious consequence of the presence of a stop codon upstream PEST that transforms the SiR into a WT ΔG-Rabies. This is strikingly different to our results showing that SiR can permanently label neurons by recombinase-mediated activation of genetic cassettes before disappearing from the infected neurons without cytotoxicity (Ciabatti et al., 2017). To experimentally confirm that revertant-free and PEST-mutant SiR are different viruses we characterized them in vitro and in vivo and compared them to canonical ΔG-Rabies. In order to obtain a pure preparation of PEST-mutants we engineered each of the two nonsense mutations previously reported (Matsuyama et al., 2019) (d.C1349G and d.G1357T, leading to stop insertion at S450 and G453, respectively; Figure 2F) in the SiR cDNA, generating two viruses named SiR-S450X and SiR-G453X (Figure 3A, Figure 3—figure supplement 1). First, we confirmed the loss of functional TEVs in the PEST linker in the engineered-revertants by observing the TEVp-dependent virally driven GFP expression in vitro (Figure 3—figure supplement 1). Next, we assessed the in vivo cytotoxicity of SiR, SiR-G453X and ΔG-Rab expressing CRE by injecting them in the CA1 hippocampal region of CRE-dependent tdTomato reporter mice (Rosa26LSL-tdTomato) and analysing the number of infected neurons at different time points post injection (p.i.) as in our previous study (Ciabatti et al., 2017; Figure 3B). We detected no decrease of tdTomato+ neurons in SiR-infected hippocampi (4109±266 tdTomato +neurons at 1 week p.i.; 4458±739 tdTomato +neurons at 2 months p.i.; one-way ANOVA, F=0.08, p=0.92, Figure 3C–D) while only 44% of tdTomato +neurons were detected in Rabies-targeted and 60% in SiR-G453X-targeted hippocampi at 2 months p.i. (1422±184 at 1 week versus 624±114 at 2 months p.i. for ΔG-Rab; one-way ANOVA, F=11.55, p=0.003; 3052+508 at 1 week versus 1829+198 at 2 months p.i. for SiR-G453X; one-way ANOVA, F=4.27, p=0.05; Figure 3C–D). Additionally, we confirmed inactivation of revertant-free SiR by analysing the decrease of Rabies transcripts in the infected hippocampi over times (Figure 3—figure supplement 2). These results support the lack of toxicity of SiR on the infected neurons, in line with our previous findings (Ciabatti et al., 2017). Moreover, these data confirm the requirement for an intact PEST sequence to sustain the self-inactivating behaviour of SiR and suggest that PEST-targeting mutations do not occur in vivo. Notably, a fraction of tdTomato +neurons survived in ΔG-Rab-CRE-injected brains, differing from what we observed when injecting ΔG-Rab-GFP, where no cells were detected at 3 weeks p.i. (Figure 3C–D; Ciabatti et al., 2017). To experimentally confirm that revertant particles indeed do not emerge in vivo during long-term SiR experiments, we prepared NGS libraries of SiR genomes extracted from hippocampi of injected animals before SiR switch off and sequenced them by SMRT sequencing (Figure 3E and Figure 2—figure supplement 2). In all three independent experiments, no revertant mutations had accumulated in vivo above threshold prior to the switching off of the virus (Figure 3F, Table 3).

![Figure 3.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig3-v2.jpg)

**Figure 3.:** (A) Scheme of the engineered PEST-mutant SiR (SiR-G453X). (B) Experimental procedure. (C) Confocal images of hippocampal sections of Rosa26LSL-tdTomato mice infected with SiR-CRE, Rab-CRE, SiR-G453X and imaged at 1 week, 1 month and 2 months p.i. Scale bar, 50 μm. (D) Number of tdTomato positive neurons at 1 week, 1 months, and 2 months p.i. normalized to 1 week time point (mean ± SEM, n=4 animals per virus per time point). (E) Experimental procedure for the sequencing of SiR particles from injected hippocampi at 1 week p.i. (F) List of PEST-inactivating mutations above 2% thresholds with relative frequency in each animal (n.d. indicates that the mutation was not detected above threshold; n=3 animals).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) The conditional destabilization of N can be prevented by TEVp expression in the infected cells leading to cleavage of the TEVs-containing linker. (B) Engineered revertant SiR viruses containing the reporter PEST-inactivating substitutions in their cDNA. (C) Confocal images of HEK and HEK-TEVp at 48 hrs p.i. All images were acquired with same settings. Bottom panels have been equally adjusted in brightness in all conditions. Scale bar 100 μm.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Schematic of SiR-CRE injection in the hippocampus mice followed by total RNA extraction and RT-qPCR. (B) Levels of viral RNA normalized to 1 week RNA level (mean ± SEM, n=4 animals per time point).

**Table 3.**
 List of detected mutations above 2% threshold in purified SiR viruses recovered from injected hippocampi sequenced by SMRT NGS sequencing.The position of the mutations is defined considering +1 the first base of the nucleoprotein N coding sequence.


<table>
  <thead>
    <tr>
      <th colspan="7">NGS sequencing results of purified viruses used in vivo</th>
    </tr>
    <tr>
      <th colspan="3">SIR-CRE purified bc3—bc5</th>
      <th colspan="4"></th>
    </tr>
    <tr>
      <th></th>
      <th>Position</th>
      <th>Variant</th>
      <th>N (q&gt;20)</th>
      <th>Freq %</th>
      <th>Mutation</th>
      <th>Effect on CDS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>238/5196</td>
      <td>4.6%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>199/5196</td>
      <td>3.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>150/5200</td>
      <td>2.9%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>544/5205</td>
      <td>10.5%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="5">SIR-CRE purified, 1 week p.i. in vivo (A) bc5—bc10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>474/5211</td>
      <td>9.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>–21</td>
      <td>+A</td>
      <td>110/5211</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>176/5211</td>
      <td>3.4%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>132/5211</td>
      <td>2.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>389/5211</td>
      <td>7.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>108/5211</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>135/5211</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>108/5210</td>
      <td>2.1%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>288/5210</td>
      <td>5.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>773/5213</td>
      <td>14.8%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>128/5213</td>
      <td>2.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="5">SIR-CRE purified, 1 week p.i. in vivo (B) bc5—bc11</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>482/5542</td>
      <td>8.7%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>157/5543</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>125/5543</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>402/5543</td>
      <td>7.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>123/5543</td>
      <td>2.2%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>157/5543</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>112/5543</td>
      <td>2.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>276/5543</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>744/5542</td>
      <td>13.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>144/5542</td>
      <td>2.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="5">SIR-CRE purified, 1 week p.i. in vivo (C) bc5—bc12</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>481/5150</td>
      <td>9.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+108</td>
      <td>+A</td>
      <td>137/5150</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+166</td>
      <td>+T</td>
      <td>118/5150</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+237</td>
      <td>+T</td>
      <td>390/5150</td>
      <td>7.6%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+245</td>
      <td>+G</td>
      <td>104/5150</td>
      <td>2.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+466</td>
      <td>+A</td>
      <td>140/5150</td>
      <td>2.7%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+612</td>
      <td>+T</td>
      <td>116/5150</td>
      <td>2.3%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>255/5150</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>739/5148</td>
      <td>14.4%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>+1,669</td>
      <td>+A</td>
      <td>130/5148</td>
      <td>2.5%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td colspan="4">SIR-G453X-CRE purified bc3—bc11</td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td></td>
      <td>Position</td>
      <td>Variant</td>
      <td>N (q&gt;20)</td>
      <td>Freq %</td>
      <td>Mutation</td>
      <td>Effect on CDS</td>
    </tr>
    <tr>
      <td>Upstream N</td>
      <td>–49</td>
      <td>+A</td>
      <td>211/4886</td>
      <td>4.3%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>N gene</td>
      <td>+237</td>
      <td>+T</td>
      <td>244/4890</td>
      <td>5.0%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td></td>
      <td>+636</td>
      <td>+T</td>
      <td>138/4911</td>
      <td>2.8%</td>
      <td>Insertion</td>
      <td>Frameshift</td>
    </tr>
    <tr>
      <td>TEVs-PEST</td>
      <td>+1,357</td>
      <td>G&gt;T</td>
      <td>4780/4912</td>
      <td>97.3%</td>
      <td>Substitution</td>
      <td>Missense G453X</td>
    </tr>
    <tr>
      <td>Intergenic</td>
      <td>+1,564</td>
      <td>+A</td>
      <td>502/4924</td>
      <td>10.2%</td>
      <td>Insertion</td>
      <td>-</td>
    </tr>
    <tr>
      <td>P</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

To further confirm the lack of any toxic effect in SiR-targeted neurons we also performed longitudinal imaging of cortical neurons using 2-photon microscopy. These longitudinal experiments allowed us to follow the morphology and survival of the same identified SiRtargeted neurons over time in living mice, thereby giving more direct evidence of the potential cytotoxicity or lack thereof associated with SiR. We imaged SiR-CRE or ΔG-Rab-CRE labelled neurons in the cerebral cortex of Rosa26LSL-tdTomato mice for up to 5 months p.i. (Figure 4A–B). The total number of detectable tdTomato+ neurons increased in SiR injected animals between 1 and 2 weeks and remained constant for the entire duration of the experiment (Figure 4B), while ΔG-Rab–injected cortices show a decrease of total number of tdTomato+ neurons over time (Figure 4B). Importantly, nearly all the SiR-targeted neurons imaged at 1 week were detected in subsequent imaging sessions (97%±1 tdTomato+ at 21 weeks p.i.; Figure 4C) in contrast to ΔG-Rab-infected neurons, where ~70% of the neurons detected at 1 week had died by 9 weeks p.i. (29%±2 tdTomato+ at 21 weeks; Figure 4C). These results show virtually no loss of SiR-labelled neurons during the entire imaging period (5 months) and confirm the lack of any observable cytotoxic effect of SiR on the recipient neurons (Figure 4B–D and Figure 4—figure supplement 1).

![Figure 4.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of SiR-CRE or Rab-CRE injection in Rosa26LSL-tdTomato mice in V1 followed by in vivo imaging. (B) Two-photon maximal projection of the same field in SiR-CRE and RabCRE injected cortices at 1, 4, and 21 weeks p.i. or 1, 4, and 9 weeks, respectively. Red arrowheads mark tdTomato positive neurons detected at 1 week that disappear in later recordings. Scale bar 50 μm. (C) Survival of the tdTomato-positive cells recorded at 1 week over time. (ROIs = 6 per virus. n=2 animals per virus). (D) Two-photon maximal projection of the same large field in SiR-CRE injected cortices at 1 week and 21 weeks p.i. Scale bar 50 μm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Two-photon maximal projection of the same fields in SiR-CRE injected cortices at 1-2-3-4-21 weeks p.i.

### SiR transsynaptic spreading

We then tested the ability of revertant-free SiR to trace neural circuits transsynaptically in the mouse brain. ΔG-Rabies vectors can be pseudotyped with the chimeric EnvA glycoprotein to selectively infect neurons expressing the TVA receptor, which is not endogenously expressed by mammalian cells (Wickersham et al., 2007b). We injected the nucleus accumbens (NAc) of CRE-dependent tdTomato reporter mice with an AAV expressing either TVA and the rabies G or TVA only. After 3 weeks, we re-injected the NAc with EnvA-pseudotyped revertant-free SiR-CRE or EnvA-pseudotyped SiR-G453X-CRE and assessed the CRE-dependent tdTomato expression presynaptically, in the basolateral amygdala (BLA). At 1 month post SiR injection, we detected no tdTomato+ cells in the BLA in TVA-only-injected animals, confirming the G-dependency for SiR transsynaptic spreading (Figure 5B–C). In contrast, as expected, transsynaptic spreading was apparent in the TVA +G condition. We observed similar numbers of presynaptically traced neurons in both SiR-CRE and SiR-G453X-CRE injected brains (169±24 and 190±36 tdTomato+ neurons, respectively; two-tailed t-test, p=0.64; Figure 5B–C). However, tdTomato+ microglial cells were only detected in the SiR-G453X-CRE condition indicating the re-emergence of toxicity of the revertant mutants (Figure 5B). We also tested the effect of supplying TEV protease to the starting cells, as this has been suggested to be a necessary step to ensure transsynapitc spreading. While the previous experiments unambiguously show that TEVp is not necessary for the transsynaptic spreading of SiR, the injection of an AAV expressing TEVp in the NAc did lead to an increase in the number of transsynaptically labelled BLA neurons (366±69 tdTomato+ neurons; two-tailed t-test, P=0.04; Figure 5C), indicating that TEVp-dependent SiR reactivation in starter cells can improve its spreading (Jin et al., 2023).

![Figure 5.](https://cdn.elifesciences.org/articles/83459/elife-83459-fig5-v2.jpg)

**Figure 5.:** (A) Experimental design for the transsynaptic tracing of NAc inputs using EnvA-pseudotyped SiR-CRE or SiR-G453X-CRE in Rosa26LSL-tdTomato mice. (B) Confocal images of BLA area of Rosa26LSL-tdTomato mice infected with SiR-CRE or SiR-G453X-CRE. Arrows point to tdTomato+ microglia. (C) Number of tdTomato-positive neurons in the BLA at 1 month post SiR injection (mean ± SEM, n=4 animals per condition). (E) Number of tdTomato+ neurons in the BLA at 1 month post SiR injection (mean ± SEM, n=3 animals per condition). (F) Confocal images of BLA area of Rosa26LSL-tdTomato mice infected with SiR-CRE or SiR-N2c-CRE. Scale bar, 100 μm.

We recently showed that a novel SiR-N2c vector, derived from the neurotropic CVS-N2c Rabies strain, displays enhanced transsynaptic spreading and improved peripheral neurotropism over the original SAD B19-derived SiR (Lee et al., 2023). Hence, for completeness, we compared the transynaptic spreading efficacty of EnvA-pseudotyped revertant-free SiR-N2c and the original SiR. SiR-N2c labelled a greater number of BLA neurons at 1 month p.i. than what was detected with SiR (1691 ± 112 tdTomato+ neurons traced by SiR-N2c; two-tailed t-test, p=2 × 105; Figure 5D–E). Additionally, TEVp expression in the starter cells in SiR-N2c tracing experiments had a negligible effect on the overall transsynaptic spreading (1934±135 tdTomato+ neurons traced by SiR-N2c in presence of TEVp; two-tailed t-test, p=0.24; Figure 5D–E). Since the use of G from the CVS-N2c Rabies strain (G_N2c) has been shown to improve ΔG-Rabies (SAD-B19) retrograde tracing (Zhu et al., 2020), we tested if complementing EnvA-pseudotyped SiR with G_N2c in the NAc could increase its spreading. While we detected more BLA tdTomato+ neurons than in our previous experiments, complementing SiR with G_N2c still labelled less neurons than SiR-N2c, even when TEVp was provided to the starter cells (487±164 and 844±14 tdTomato+ neurons traced by SiR in absence or presence of TEVp, respectively; Figure 5D–E).

## Discussion

The development of technologies to record and perturb the activity of neurons within neural circuits has been instrumental for the recent progress in systems neuroscience. ΔG-Rabies viruses have been transformative in the study of neural circuit organization in animal models, especially mammals. The recent generation of a non-toxic SiR vector has opened the door to the long-term functional dissection of neural networks. One concern regarding its widespread use has been the risk that mutations could emerge and compromise SiR preparations by reverting the SiR vector to canonical and cytotoxic ΔG-Rabies.

Here we have investigated the genomic stability of SiR and showed that PEST-targeting mutations are rare and do not accumulate when SiR is produced directly from cDNA as previously described. However, we show that revertant mutants can emerge if SiR is extensively amplified in vitro, particularly in cells expressing suboptimal levels of TEVp, where revertant mutants have a specific replication advantage. Nonetheless, we also show that when production utilises HEK-TGG packaging cells expressing high levels of TEVp, even 8 rounds of amplification in vitro do not lead to the accumulation of PEST-targeting mutations above 5%. Notably, we found that TEVp activity inevitably decreases after several passages of amplification of HEK-TTG. thus fresh low passage packaging cells should always be used to produce SiR preparations. Our results suggest that stock for packaging cells should be made within a couple of passage after selection is established, and then used freshly defrosted to produce SiR viruses (equivalent to P0 cells in Figure 2B–C). Similarly, SiR supernatant stocks should be made directly from cDNA transfection and amplified for a maximum of 2 passages (equivalent to SiR P0 in Figure 2E) before being used for large scale SiR productions.

Another important question is, when revertant-free SiR is produced and used for tracing experiments, can PEST-targeting mutations emerge in vivo? Here we show that revertant-free SiR-CRE efficiently infect neurons in vivo without toxicity in cortical and subcortical regions for several months p.i. Importantly, PEST-mutant SiR is as toxic as canonical ΔG-Rabies, indicating that an intact PEST sequence is essential for SiR non-toxic behaviour and suggesting that revertant mutants do not emerge during in vivo experiments. We confirmed this by sequencing the SiR viral particles isolated from in vivo experiments and found no PEST-targeting mutations. Thus, the short lifetime of the SiR in the infected neurons does not permit PEST mutations to emerge and accumulate in vivo before viral disappearance when revertant-free SiR preparations are used.

ΔG-Rabies vectors are powerful tools for the dissection of neural circuit organization thanks to their ability to spread retrogradely to synpatically-connected neurons. Here, we show that EnvA-pseudotyped revertant-free SiR vectors effectively spread transsynpatically in the mouse brain. Importantly, the co-delivery of an AAV expressing TEVp in addition to G increase the number of traced neurons in presynaptic areas, likely due to the TEVp-dependent reactivation of SiR in vivo (Ciabatti et al., 2017), in line with recent results (Jin et al., 2023). This should be considered when planning transsynaptic tracing experiments using SiR. To improve SiR spreading efficiency, further studies should investigate the use of inducible TEVp, as we previously showed (Ciabatti et al., 2017), that could maximise spreading efficiency while minimising possible side effects of prolonged protease expression.

Interestingly, we found that the recently developed SiR-N2c vector, generated by applying the same proteasome-targeting modification to the genome of the CVS-N2c ΔG-Rabies strain (Lee et al., 2023), show a higher number of retrogradely labelled neurons compared to the original SiR (SAD-B19; Figure 5). Additionally, the co-delivery of TEVp had a smaller effect on the number of neurons transsynaptically traced by SiR-N2c. Interestingly, the gap in trassynaptic spreading efficacy between SiR (SAD-B19) and SiR-N2c could not be filled by complementing the SiR with the neurotropic G_N2c. This could be linked to a more efficient packaging of SiR-N2c by G_N2c (Reardon et al., 2016; Sumser et al., 2022) or by the particularly high speed of CVS-N2c strain propagation (~12 hr; Callaway, 2008; Hoshi et al., 2005). These results point to SiR-N2c as the vector of choice for transsynaptic experiments.

Although PEST-inactivating mutations can be prevented during production and do not accumulate in vivo, strategies to further reduce or entirely eliminate the risk of their appearance could simplify viral production in other laboratories and allow the use of SiR in sensitive applications, e.g. re-targeting the same starter cells multiple times. In our experiments only two specific revertant mutations were identified, single base substitutions that introduce a stop signal either at the last amino acid of N or in the linker prior to TEVs and PEST (d.C1349G and d.G1357T) which accounted for the large majority of revertant mutations found in Matsuyama et al., 2019. Future studies should focus on investigating if this and other potential hotspots in the SiR genome can be optimised to simplify the production of SiR.

## Methods

### Contact for Reagents and Resource Sharing

Further information and requests for resources and reagents should be directed to the corresponding author: Ernesto Ciabatti (ciabatti@mrc-lmb.cam.ac.uk).

### Experimental Model and Subject Details

#### Animal strains

C57BL/6 wild type (WT) mice and Rosa26LSL-tdTomato transgenic mice (Jackson: Gt(ROSA)26Sortm14(CAG tdTomato)) were used. All animal procedures were conducted in accordance with the UK Animals (Scientific procedures) Act 1986 and European Community Council Directive on Animal Care under project license PPL PCDD85C8A and approved by The Animal Welfare and Ethical Review Body (AWERB) committee of the MRC-LMB. Animals were housed in a 12 hours light/dark cycle with food and water ad libitum.

#### Cell lines

HEK293T cells were obtained from ATTC. HEK293T packaging cells expressing Rabies glycoprotein (HEK-GG) were generated by lentivirus infection with Lenti-H2BGFP-2A- GlySAD and after 3 passages GFP expressing cells were selected by fluorescent activated cell sorting (FACS). HEK293T packaging cells expressing Rabies glycoprotein and TEV protease (HEK-TGG) were generated from HEK-GG by lentivirus infection with Lenti-puro-2A-TEV and selected, after 3 passages, with 1 µg/ml of puromycin added to the media for 1 week. HEK293T expressing TEV protease (HEK-TEVp) were generated by lentivirus infection with Lenti-puro-2A-TEV and selected, after 3 passages, with 1 µg/mL of puromycin added to the media for 1 week.

### Method Details

#### Design and generation of ΔG-Rabies and SiR plasmids

All Rabies and SiR plasmids were generated by Gibson cloning starting from pSAD-ΔG-F3 plasmid (Osakada et al., 2011) or SiR vectors we previously generated (Ciabatti et al., 2017), respectively. Engineered SiR vectors carrying d.C1349G or d.G1357T PEST-targeting mutations were produced by PCR amplification of the Rabies genome in 2 fragments starting from the end of N assembled using Gibson master mix (NEB).

The lentiviral vectors used to generate the packaging cells have been previously described (Ciabatti et al., 2017).

#### TEVp activity in packaging cells

Low passage HEK-TGG packaging cells were produced as previously described (Ciabatti et al., 2017). Briefly, HEK293T cells were infected with Lenti-GFP-2A-G and after three passages GFP expressing cells were selected by fluorescent activated cell sorting (FACS). Cells were infected with Lenti-puro-2A-TEVp and amplified for two passages under 2 µg/ml of puromycin selection in 10% DMEM. This produced the HEK-TGG P0 line that was further amplified either in absence or presence of 1/2 µg/ml of puromycin selection for up to eight passages. Cells were split every 3 days at 1:6 dilution and every two passages TEVp activity was assessed by seeding 750 k cells in six-wells and transfecting a TEVp activity reporter (Gray et al., 2010) after 24 hr. Transfected cells were lysed in RIPA buffer after 24 hr and TEVp-dependent reporter cleavage was assessed by western blot staining for the V5 tag at the C-terminal of the TEVp activity reporter (monoclonal anti-V5 V8012, anti-mouse HRP-conjugated 32430). Western blots were imaged using a Chemidoc MP system (Bio-Rad) and the ratio of cleaved and uncleaved reporter was analysed using Image Lab software (Bio-Rad).

#### Viral productions

SiR and ΔG-Rabies viruses were rescued from cDNA by the co-transfection of rabies genome vectors with pcDNA-T7, pcDNA-SADB19N, pcDNA-SADB19P, pcDNA-SADB19L, and pcDNA-SADB19G (Osakada et al., 2011) in HEK-TGG and HEK-GG cells, respectively, as previously described (Ciabatti et al., 2017).

For the recovery of high titer SiR and ΔG-Rabies, HEK-TGG or HEK-GG respectively were infected in 15 cm dishes at ~80% confluence with 3 ml of viral supernatant obtained as described in the viral screening section. Cells were split the day after infection and maintained for 1 or 2 days at 37 °C and 5% CO2 checking daily the viral spreading when a fluorescent marker was present. Then, the media was replaced with 2% FBS DMEM and maintained for 2 days at 35 °C and 3% CO2. Viral supernatant was collected, cell debris removed by centrifugation at 2500 rpm for 10 min followed by filtration with 0.45 µm filter and the virus concentrated by ultracentrifugation on a sucrose cushion as previously described (Wickersham et al., 2007a).

#### Ontogenesis of revertant mutations during viral production

8 independent SiR viruses were rescued from cDNA as described in previous section. SiR RNA genomes were extracted from the infectious supernatants with RNeasy kit (Qiagen) following manufacturer’s instructions and used to generate plasmid libraries for Sanger sequencing. To investigate the emergence of mutations during subsequent viral amplification rounds in vitro low passage HEK-TGG (HEKTGG P0), or high passage cells amplified in absence of puromycin pressure (HEK-TGG P8) were seeded in 10 cm dishes. At 60–70% confluence cells were infected with SiR supernatants obtained from cDNA at MOI=~2–3. The next day, cells were split at 1:2 dilution and maintained for 1 day at 37 °C and 5% CO2 in 10% FBS DMEM. Then, media was replaced with 2% FBS DMEM and cells moved to incubation at 35 °C and 3% CO2. Viral supernatants were collected after 2–3 days and used to infect fresh HEK-TGG P0 or HEK-TGG P8. The entire process was repeated for a total of 8 rounds of viral amplification. At each passage, 1 ml of supernatant was used to extract viral RNA genomes and generate libraries for NGS.

#### Analysis of SiR accumulation of mutations during in vivo experiments

Sequence-verified revertant-free SiR virus was injected in CA1 region of the hippocampus of C57BL/6 wild type mice. After 1 week, mice were culled and the injected hippocampi manually dissected immediately. SiR genomes were obtained by homogenising the hippocampi with Tissuelyser II (Qiagen) and extracting the total RNA with RNeasy kit (Qiagen) according to manufacturer instructions. A total of 500 ng of RNA per hippocampus were reverse-transcribed using superscript IV kit (Invitrogen) and amplicons of N-TEVs-PEST were PCR-amplified to generate libraries for SMRT NGS sequencing.

#### Sanger sequencing of SiR genomes

SiR genomic copies were extracted by concentrating 1 ml of infectious supernatant with Amicon Ultra-4 10 K filters in an Eppendorf 5810 R centrifuge at 4°C, 2500 g for 20’ followed by RNeasy kit (Qiagen) extraction. RNA samples were treated with DNAse I (Invitrogen) for 15’ at RT followed by inactivation at 65°C for 10’. Genomes were reverse-transcribed with SuperScript IV Reverse Transcriptase (Invitrogen) following manufacturer instructions using a primer complementary to the 5’ leader sequence containing an 8 nt random barcode:

cDNA samples were subjected to RNAse H treatment (NEB) followed by PCR amplification of a fragment corresponding to the entire coding sequence of N-TEVs-PEST and part of the P gene with Platinum SuperFi II Master Mix polymerase (denaturation for 30 s at 98°C; 25 cycles of amplification with 5 s at 98°C, 10 s at 60°C and 60 s at 72°C; 3 min at 72 for final extension) using primers:

The obtained ~2 Kb amplicons were gel purified from 1% agarose gel using QIAquick Gel Extraction Kit (Qiagen) and cloned in pBluescript SK (+) (GenBank:X52325.1) digested KpnI – XbaI using Gibson assembly cloning method (NEB). 50 clones were purified and sequenced by Sanger method using M13_Fw and M13_Rv primers checking that each sequence carried a different 8 nt barcode.

#### Single molecule real-time (SMRT) sequencing of SiR genomes

SiR supernatant preparations were first concentrated by centrifuging 1 ml of infectious supernatant in Amicon Ultra-4 10 K filters in an Eppendorf 5810 R centrifuge at 4 °C, 2500 g for 20’, followed by RNA extraction using RNeasy kit (Qiagen). Purified viruses were directly extracted with RNeasy kit by adding 350 µl of RT lysis buffer to 5 µl of concentrated virus. RNA samples were treated with DNAse I (Invitrogen) for 15’ at RT followed by inactivation at 65 °C for 10’. Genomes were retro-transcribed with SuperScript IV Reverse Transcriptase (Invitrogen) following manufacturer instructions using a primer complementary to the 5’ leader sequence containing an adapter sequence and a 10 nt random barcode:

cDNA samples were subjected to RNAse H treatment (NEB) followed by PCR amplification of a fragment corresponding to the entire coding sequence of N-TEVs-PEST and a fragment of the P gene with Platinum SuperFi II Master Mix polymerase (denaturation for 30 s at 98 °C; 25 cycles of amplification with 5 s at 98 °C, 10 s at 60 °C and 60 s at 72 °C; 3 min at 72 for final extension) using primers asymmetrically barcoded as shown below (list of the barcodes used for each sample can be found in Tables 2 and 3):

Barcodes:

The obtained ~2 Kb amplicons were gel purified from 1% agarose gel using QIAquick Gel Extraction Kit (Qiagen) followed by clean-up with QIAquick PCR purification kit (Qiagen). Purified barcoded amplicons from different viral preparations were combined in a single tube to obtain equimolar ratio and final concentration of ~50 ng/µl. SMRTbell libraries of pooled amplicons (up to 29 samples per library) were prepared using SMRTbell Template Prep Kit 1.0 (Pacbio) and Sequel chemistry v3 and sequenced on a PacBio Sequel SMRT cell with a 10 hr movie.

#### Single-molecule real-time (SMRT) sequencing analysis

Pacbio Sequel II raw movies containing all subreads were used to generate high-fidelity circular consensus sequences (CCS) using pbccs program v4.2.0 (Pacific Biosciences,USA) (https://github.com/PacificBiosciences/ccs; Pacific Biosciences, 2022) with default settings (minimal number of passages 3, fidelity >98%). CCS reads were demultiplexed and assigned to each sample with the Lima program v1.11.0 (Pacific Biosciences,USA) (https://github.com/pacificbiosciences/barcoding/; Pacific Bioscience, 2017) using the asymmetric 16 nt barcodes added to the amplicons during PCR amplification (list of barcode combinations per sample in Tables 2–3). Duplicated sequences of the same genomic molecules were removed using the unique molecular identifiers (UMI) of 10 random nucleotides added during SiR genomes retrotransciption. Briefly, UMI tags were extracted from individual reads using UMI_tools v1.0.1 (https://github.com/CGATOxford/UMI-tools; Smith et al., 2017; CGATOxford, 2023) and used to generate families of reads from a single original genomic copy. For each family, the highest quality read was retained and the others discarded using dedup function of UMI_tools. Deduplicated reads were aligned to the reference using pbmm2 function v1.2.1 (Pacific Biosciences,USA) (https://github.com/PacificBiosciences/pbmm2/; Pacific Biosciences, 2023) and variants called using the ivar program v1.2.1 (https://github.com/andersen-lab/ivar; Grubaugh et al., 2019; Andersen Laboratory, 2023) using a minimum base quality of 20. Complete list of the identified mutations and number of reads above q>20 per base per sample can be found in Tables 2 and 3.

#### TEVp-dependency of viral transcription

HEK and HEK-TEVp were seeded in glass bottom wells (µ-Slide 8 Well Glass Bottom, Ibidi) and infected when at ~70% confluence with SiR-nucGFP, SiR-S450X-nucGFP, SiRG453X-nucGFP or ΔG-Rabies-nucGFP. Live infected cells were imaged 48 hr post infection in an inverted confocal microscope (SP8 Leica) using a 10 x air objective with identical settings for all conditions to evaluate GFP expression levels.

#### Immunohistochemistry

Mice were perfused with ice cold phosphate buffered saline (PBS) followed by 4% paraformaldehyde (PFA) in PBS. Brains were incubated in PFA overnight at 4 °C, rinsed twice with PBS followed by dehydration in 30% sucrose in PBS at 4 °C for 2 days. Then, brains were frozen in O.C.T. compound (VWR) and sliced at 35 μm on cryostat (Leica, Germany). Freefloating sections were rinsed in PBS and then incubated in blocking solution (1% bovine serum albumin and 0.3% Triton X-100 in PBS) containing primary antibodies for 24 hr at 4 °C. Sections were washed with PBS three times and incubated for 24 hr at 4 °C in blocking solution with secondary antibodies. Immuno-labelled sections were washed three times with PBS and mounted on glass slides. Antibodies used in this study were rabbit anti-RFP (Rockland, 600401–379, 1:2000) and donkey anti-rabbit Cy3 (Jackson ImmunoResearch, 711-165-152, 1:1000).

#### Viral injections

All procedures using live animals were approved by the Home Office and the LMB Biosafety committee. For all experiments, adult mice >8 weeks were used. Mice were anesthetized with 3% isofluorane in 2 L/min of oxygen for the initial induction and then maintained with a flow of 1–2% isofluorane in 2 L/min of oxygen. Anesthetized animals were placed into a stereotaxic apparatus (David Kopf Instruments) and Rimadyl (2 mg/kg body weight) was administered subcutaneously (s.c.) as an anti-inflammatory. A small hole (500 μm diameter) was drilled and viruses were injected using a WPI Nanofil syringe (35 gauge) for injections in the hippocampus or a glass capillary for injections in the cerebral cortex. The syringe was left in the brain for 5 min before being retracted. SiR and Rabies viruses were injected at 3–6x108 infectious units/ml. For transsynaptic experiments, AAV-CMV-nucGFP-2A-TVA (AAV-TVA), AAV-hSyn1-TVAmCherry-2A-oG (AAV-TVA-G), AAV-hSyn1-TVAmCherry-2A-G(N2c) (AAV-TVA-G_N2c), AAV-hSyn1-nucFLAG-2a-TEVp (AAV-TEVp) were injected at ~3 × 1012 genomic copies/ml. EnvA-pseudotyped SiR were injected at ~3 × 108 infectious units/ml for SAD-B19 strain and ~1–3 × 107 infectious units/ml for CVS-N2c strain. Up to a maximum volume of 500 nl of virus was injected in the following brain areas: hippocampus (AP: –2.45 mm, ML: 2 mm and DV: 1. 5 mm from bregma), cerebral cortex (AP: –2.5 mm, ML: 2 mm and DV: 0,3 mm from brain surface), nucleus accumbens (AP: –1.3 mm, ML: 1.35 mm and DV: 4.7 mm from bregma).

#### In vivo cytotoxicity analysis

SiR-CRE, SiR-G453X-CRE and ΔG-Rabies-CRE in vivo cytotoxicity was assessed by injecting 400 nl of purified viral preparations (at 3–6x108 infectious units/ml) in CA1 area of the hippocampus of Rosa26LSL-tdTomato mice. Animals were perfused at 1 week or 1–2 month p.i. and the brains were sectioned at the cryostat (35 μm). The entire hippocampus was sampled (by acquiring one slice every 4) by imaging infected neurons using a robot assisted Nikon HCA microscope mounting a 10 x (0.45NA) air objective and tdTomato positive hippocampal neurons counted using Nikon HCA analysis software. Cell survival was calculated by normalizing the total number of infected neurons to the 1 week time point.

#### Transsynaptic spreading analysis

SiR transsynaptic spreading was assessed by injecting 500 nl of helper AAVs (at ~3 × 1012 infectious units/ml) in the NAc of Rosa26LSL-tdTomato mice. After 3 weeks, animals were retargeted with 500 nl of purified EnvA-pseudotyped SiR-CRE, SiR-G453X-CRE or SiR-N2c-CRE. Animals were perfused at 1 month p.i. and the brains were sectioned at the cryostat (50 μm). The entire brain was sampled (by acquiring one slice every 4) by imaging infected neurons using a robot assisted Nikon HCA microscope mounting a 10 x (0.45NA) air objective and tdTomato+ BLA neurons counted using Nikon HCA analysis software.

#### Analysis of Rabies RNA in vivo

SiR-CRE genomic copies in vivo were evaluated over time by recovering the total RNA from SiR-injected hippocampi at different time points, as we previously described (Ciabatti et al., 2017). Briefly, the hippocampi were homogenized using a Tissuelyser II (QIAGEN) and processed accordingly to manufactory instruction with RNeasy kit (QIAGEN). A total of 500 ng of RNA per hippocampus were reverse-transcribed using superscript IV kit (Invitrogen) and analysed by quantitative PCR (Rotor-Gene Multiplex PCR) using probe assays against Actb and Rabies N gene. The Livak method was applied for quantification: the level of N at different time points was normalized to the expression of the Actb housekeeping gene (ΔCT = CTgene – CTActb) and the variation over time as fold change (2-ΔΔCT) to the 1 week time point (ΔΔCT = ΔCTTime point – ΔCT1 week).

#### In vivo two-photon imaging

Rosa26LSL-tdTomato mice aged 3–4 months were injected with Dexafort at 2 μg/g, one day prior to surgery. Mice were anesthetized with Isofluorane (induction and maintenance at 3% and 2% in 3 L/min of oxygen, respectively) and injected subcutaneously with Vetergesic at 0.1 mg/kg. A metal head-post was affixed to the skull with Crown & Bridge Metabond. Epivicaine was splashed on the skull, and a 3 mm craniotomy was performed on the left hemisphere, centred at 2 mm lateral of the midline and 2.5 mm posterior of bregma. A total of 500 nl of virus with a titer of 4x108 was then delivered at the centre of the craniotomy, at a depth of 300 µm, and at a rate of 100 nl per minute using a manual hydraulic micromanipulator (Narishige). The craniotomy was finally sealed with a 3 mm round coverslip pressing on the brain, and affixed using Crown & Bridge Metabond. Mice were imaged weekly after surgery, under Isofluorane anaesthesia at 1.5% in 3 L/min of oxygen, with a two-photon microscope (Bergamo II, Thorlabs), equipped with a 16 x - 0.8 NA objective (Nikon). Infected cells were excited with a Ti:Sapphire pulsed laser at 1030 nm, with a power of around 20 mW (Mai TaiDeepSee, Spectra Physics). Emitted fluorescence was collected through a 607±35 nm filter (Brightline). For each mouse, a Z-stack was recorded, centred at the same anterior-posterior coordinate as the injection, but 1 mm closer to the midline in the lateral-medial axis. Imaging planes’ pixel resolution was 2048x2048, and depth was sampled in steps of 1 µm. Z-stacks were 3d aligned across time points using a custom program written in Python, segmented into smaller fields of view, and filtered with a 3D mean filter of radius 2 pixels for x and y, and 5 pixels for z (Fiji). All cells at week 1 were labelled using FIJI, and their presence was manually assessed at later time points for the quantification of the survival rate.

#### Quantification and statistical analysis

Mean values are accompanied by SEM. No statistical methods were used to predetermine sample sizes. In the hippocampal survival experiments animals were randomly assigned to each time point. Next generation sequencing datasets were analysed blindly. Otherwise, data collection and analysis were not performed blind to the conditions of the experiments. Statistical analysis was performed in Graphpad Prism and/or Matlab. Paired t-test and one-way ANOVA test were used to test for statistical significance when appropriate. Statistical parameters including the exact value of n, precision measures (mean ± SEM) and statistical significance are reported in the text and in the figure legends (see individual sections). The significance threshold was placed at α=0.05.

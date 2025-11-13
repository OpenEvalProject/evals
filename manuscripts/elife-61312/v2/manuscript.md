# Escape from neutralizing antibodies by SARS-CoV-2 spike protein variants

## Authors

- Yiska Weisblum<sup>1</sup> ([ORCID: 0000-0002-9249-1745](https://orcid.org/0000-0002-9249-1745))
- Fabian Schmidt<sup>1</sup> ([ORCID: 0000-0001-7731-6685](https://orcid.org/0000-0001-7731-6685))
- Fengwen Zhang<sup>1</sup>
- Justin DaSilva<sup>1</sup>
- Daniel Poston<sup>1</sup>
- Julio CC Lorenzi<sup>2</sup>
- Frauke Muecksch<sup>1</sup> ([ORCID: 0000-0002-0132-5101](https://orcid.org/0000-0002-0132-5101))
- Magdalena Rutkowska<sup>1</sup>
- Hans-Heinrich Hoffmann<sup>3</sup>
- Eleftherios Michailidis<sup>3</sup> ([ORCID: 0000-0002-9907-4346](https://orcid.org/0000-0002-9907-4346))
- Christian Gaebler<sup>2</sup>
- Marianna Agudelo<sup>2</sup>
- Alice Cho<sup>2</sup>
- Zijun Wang<sup>2</sup>
- Anna Gazumyan<sup>2</sup>
- Melissa Cipolla<sup>2</sup>
- Larry Luchsinger<sup>4</sup> ([ORCID: 0000-0002-0063-1764](https://orcid.org/0000-0002-0063-1764))
- Christopher D Hillyer<sup>4</sup>
- Marina Caskey<sup>2</sup>
- Davide F Robbiani<sup>2</sup>
- Charles M Rice<sup>3</sup> ([ORCID: 0000-0003-3087-8079](https://orcid.org/0000-0003-3087-8079))
- Michel C Nussenzweig<sup>2</sup>
- Theodora Hatziioannou<sup>1</sup> †
- Paul D Bieniasz<sup>1</sup> ([ORCID: 0000-0002-2368-3719](https://orcid.org/0000-0002-2368-3719)) †

### Affiliations

1. Laboratory of Retrovirology, The Rockefeller University New York United States
2. Laboratory of Molecular Immunology The Rockefeller University New York United States
3. Laboratory of Virology and Infectious Disease The Rockefeller University New York United States
4. Lindsley F. Kimball Research Institute, New York Blood Center New York United States
5. Institute for Research in Biomedicine, Università della Svizzera italiana Bellinzona Switzerland
6. Howard Hughes Medical Institute, The Rockefeller University New York United States

† Corresponding author

## Abstract

Neutralizing antibodies elicited by prior infection or vaccination are likely to be key for future protection of individuals and populations against SARS-CoV-2. Moreover, passively administered antibodies are among the most promising therapeutic and prophylactic anti-SARS-CoV-2 agents. However, the degree to which SARS-CoV-2 will adapt to evade neutralizing antibodies is unclear. Using a recombinant chimeric VSV/SARS-CoV-2 reporter virus, we show that functional SARS-CoV-2 S protein variants with mutations in the receptor-binding domain (RBD) and N-terminal domain that confer resistance to monoclonal antibodies or convalescent plasma can be readily selected. Notably, SARS-CoV-2 S variants that resist commonly elicited neutralizing antibodies are now present at low frequencies in circulating SARS-CoV-2 populations. Finally, the emergence of antibody-resistant SARS-CoV-2 variants that might limit the therapeutic usefulness of monoclonal antibodies can be mitigated by the use of antibody combinations that target distinct neutralizing epitopes.

## Introduction

Neutralizing antibodies are a key component of adaptive immunity against many viruses that can be elicited by natural infection or vaccination (Plotkin, 2010). Antibodies can also be administered as recombinantly produced proteins or as convalescent plasma to confer a state of passive immunity in prophylactic or therapeutic settings. These paradigms are of particular importance given the emergence of SARS-CoV-2, and the devastating COVID19 pandemic that has ensued. Indeed, interventions to interrupt SARS-CoV-2 replication and spread are urgently sought, and passively administered antibodies are currently among the most promising therapeutic and prophylactic antiviral agents. Moreover, an understanding of the neutralizing antibody response to SARS-CoV-2 is critical for the elicitation of effective and durable immunity by vaccination (Kellam and Barclay, 2020).

Recent studies have shown that related, potently neutralizing monoclonal antibodies that recognize the SARS-CoV-2 receptor-binding domain (RBD) are often elicited in SARS-CoV-2 infection (Robbiani et al., 2020; Brouwer et al., 2020; Cao et al., 2020; Chen et al., 2020; Chi et al., 2020; Rogers et al., 2020; Shi et al., 2020; Wu et al., 2020a; Wec et al., 2020; Kreer et al., 2020; Hansen et al., 2020; Ju et al., 2020; Seydoux et al., 2020; Liu et al., 2020; Zost et al., 2020). These antibodies have great potential to be clinically impactful in the treatment and prevention of SARS-CoV-2 infection. The low levels of somatic hypermutation and repetitive manner in which similar antibodies (e.g. those based on IGHV3-53 Robbiani et al., 2020; Barnes et al., 2020; Yuan et al., 2020) have been isolated from COVID19 convalescents suggests that potently neutralizing responses should be readily elicited. Paradoxically, a significant fraction of COVID19 convalescents, including some from whom potent neutralizing antibodies have been cloned, exhibit low levels of plasma neutralizing activity (Robbiani et al., 2020; Wu et al., 2020b; Luchsinger et al., 2020). Together, these findings suggest that natural SARS-CoV-2 infection may often fail to induce sufficient B-cell expansion and maturation to generate high-titer neutralizing antibodies.

The degree to, and pace at which SARS-CoV-2 might evolve to escape neutralizing antibodies is unclear. The aforementioned considerations raise the possibility that SARS-CoV-2 evolution might be influenced by frequent encounters with sub-optimal concentrations of potently neutralizing antibodies during natural infection. Moreover, the widespread use of convalescent plasma containing unknown, and often suboptimal, levels of neutralizing antibodies might also increase the acquisition of neutralizing antibody resistance by circulating SARS-CoV-2 populations (Bloch et al., 2020; Al‐Riyami et al., 2020). Reinfection of previously infected individuals who have incomplete or waning serological immunity might similarly drive emergence of antibody escape variants. As human neutralizing antibodies are discovered and move into clinical development as therapeutics and prophylactics, and immunogens based on prototype SARS-CoV-2 spike protein sequences are deployed as vaccines, it is important to anticipate patterns of antibody resistance that might arise. Here, we describe a recombinant chimeric virus approach that can rapidly generate and evaluate SARS-CoV-2 S mutants that escape antibody neutralization. We show that mutations conferring resistance to convalescent plasma or RBD-specific monoclonal antibodies can be readily generated in vitro. Notably, these antibody resistance mutations are present at low frequency in natural populations. Importantly, the use of candidate monoclonal antibody combinations that target distinct epitopes on the RBD (and therefore have non-overlapping resistance mutations) can suppress the emergence of antibody resistance.

## Results

### Selection of SARS-CoV-2 S variants using a replication-competent VSV/SARS-CoV-2 chimeric virus

To select SARS-CoV-2 S variants that escape neutralization by antibodies, we used a recently described replication-competent chimeric virus based on vesicular stomatitis virus that encodes the SARS-CoV-2 spike (S) protein and green fluorescent protein (rVSV/SARS-CoV-2/GFP) (Schmidt et al., 2020). Notably, rVSV/SARS-CoV-2/GFP replicates rapidly and to high-titers (107 to 108 PFU/ml within 48 hr), mimics the SARS-CoV-2 requirement for ACE-2 as a receptor, and is neutralized by COVID19 convalescent plasma and SARS-CoV-2 S-specific human monoclonal antibodies (Schmidt et al., 2020). The replication of rVSV/SARS-CoV-2/GFP can be readily monitored and measured by GFP fluorescence and the absence of proof-reading activity in the viral polymerase (VSV-L) results in the generation of virus stocks with greater diversity than authentic SARS-CoV-2, for an equivalent viral population size. These features facilitate experiments to investigate the ability S protein variants to escape antibody neutralization.

We used two adapted, high-titer variants of rVSV/SARS-CoV-2/GFP, (namely rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1) (Schmidt et al., 2020) in attempts to derive antibody-resistant mutants. Virus populations containing 1 × 106 infectious particles were generated following three passages to generated sequence diversity. On the third passage, cells were infected at an MOI of ~ 0.5 and progeny harvested after as short a time as possible so as to minimize phenotypic mixing in the viral population and to maximize the concordance between the genome sequence and the S protein sequence represented in a given virion particle. Because the mutation rate of VSV is ~ 10−4 to 10−5/base per replication cycle (Steinhauer and Holland, 1986; Steinhauer et al., 1989; Combe and Sanjuán, 2014), we estimated that this procedure should generate a large fraction of the possible replication-competent mutants within a population size of 1 × 106. The viral populations were then incubated with antibodies to neutralize susceptible variants (Figure 1A). For monoclonal antibodies, viral populations were incubated with antibodies at 5 μg/ml or 10 μg/ml, (~1000 to 10,000 x IC50) so as to minimize the number of infection events by antibody sensitive variants, and enable rapid selection of the most resistant rVSV/SARS-CoV-2/GFP variants from the starting population. For plasma samples, the possibility existed that multiple different antibody specificities could be present, that might interfere with the outgrowth of rVSV/SARS-CoV-2/GFP variants that were resistant to the most prevalent or potent antibodies in the plasma. Therefore, in these selection experiments, viruses were incubated with a range of plasma dilutions (see materials and methods). Neutralized viral populations were then applied to 293T/ACE2(B) cells (Schmidt et al., 2020), which support robust rVSV/SARS-CoV-2/GFP replication, and incubated for 48 hr. We used three potent human monoclonal antibodies C121, C135, and C144 (Robbiani et al., 2020), that are candidates for clinical development (Table 1). In addition, we used four convalescent plasma samples, three of which were from the same donors from which C121, C135, and C144, were obtained (Robbiani et al., 2020; Table 1). Two of these plasmas (COV-47 and COV-72) were potently neutralizing while the third (COV-107) had low neutralizing activity. A fourth convalescent plasma sample (COV-NY) was potently neutralizing but did not have a corresponding monoclonal antibody (Table 1).

![Figure 1.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig1-v2.jpg)

**Figure 1.:** (A) Outline of serial passage experiments with replication-competent VSV derivatives encoding the SARS-CoV-2 S envelope glycoprotein and a GFP reporter (rVSV/SARS-CoV-2/GFP) in 293T/ACE2(B) cells in the presence of neutralizing antibodies or plasma. Each passage experiment was performed twice (once each with rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1.) (B) Representative images of 293T/ACE2(B) cells infected with 1 × 106 PFU of rVSV/SARS-CoV-2/GFP in the presence or absence of 10 μg/ml of the monoclonal antibody C121. (C) Expanded view of the boxed areas showing individual plaques of putatively antibody-resistant viruses.

**Table 1.**
 Plasma and monoclonal antibodies used in this study.


<table>
  <thead>
    <tr>
      <th>Donor</th>
      <th>Plasma NT50 (rVSV-SARSCoV2/GFP)</th>
      <th colspan="2">Plasma NT50 HIV/CCNGnLuc</th>
      <th>Monoclonal antibody</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>COV-47</td>
      <td>6622</td>
      <td colspan="2">8016</td>
      <td colspan="2">C144</td>
    </tr>
    <tr>
      <td>COV-72</td>
      <td>6274</td>
      <td colspan="2">7982</td>
      <td colspan="2">C135</td>
    </tr>
    <tr>
      <td>COV-107</td>
      <td>122</td>
      <td colspan="2">334</td>
      <td colspan="2">C121</td>
    </tr>
    <tr>
      <td>COV-NY</td>
      <td>12614</td>
      <td colspan="2">7505</td>
      <td colspan="2">ND</td>
    </tr>
  </tbody>
</table>

Infection with rVSV/SARS-CoV-2/GFP in the presence of the monoclonal antibodies C121 or C144 reduced the number of infectious units from 106 to a few hundred, as estimated by the frequency of GFP-positive cells (Figure 1B) a reduction of > 1000 fold. C135 reduced infection by ~ 100 fold. Imaging of wells infected with rVSV/SARS-CoV-2/GFP in the presence of C121 or C144 revealed a small number of foci (~10 to 20/well), that suggested viral spread following initial infection (Figure 1B). In the case of C135, a greater number of GFP-positive cells were detected, obscuring the visualization of focal viral spread following initial infection. Aliquots of supernatants from these passage-1 (p1) cultures were collected 48 hr after infection, diluted in the same concentrations of monoclonal antibodies that were initially employed, and used to infect fresh (p2) cultures (Figure 1A). For p2 cultures, almost all cells became infected within 48 hr, suggesting the possible outgrowth of monoclonal antibody escape variants that were present in the original viral populations.

For selection in the presence of plasma, p1 supernatants were harvested at 48 hr after infection in the presence of the highest concentrations of plasma that permitted infection of reasonable numbers (approximately 10%) of cells. Then, p2 cultures were established using p1 supernatants, diluted in the same concentrations of plasma used in p1. This approach led to clear ‘escape’ for the COV-NY plasma with prolific viral growth in p2 as evidenced by a large increase in the number of GFP-positive cells. For COV-47, COV-72, and CO107, plasma clearly retained at least some inhibitory activity in p2. Thereafter, p3 cultures and p4 cultures were established for COV-47, COV-72, and COV-107 plasmas at 5-fold higher concentrations of plasma than were used in p1 and p2 cultures (Figure 1A).

RNA was extracted from p2 supernatants (monoclonal antibodies and COV-NY plasma) as well as later passages for the COV-47, COV-72, and COV-107 plasma selections. Sequences encoding either the RBD or the complete S protein were amplified using PCR and analyzed by Sanger and/or Illumina sequencing. For all three monoclonal antibodies and two of the four plasmas, sequence analyses revealed clear evidence for selection, with similar or identical mutants emerging in the presence of monoclonal antibodies or plasma in both rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 cultures (Figure 2A–D, Figure 2—figure supplement 1A,B, Figure 2—figure supplement 2A,B, Table 2). In the case of C121, mutations E484K and Q493K/R within the RBD were present at high frequencies in both p2 selected populations, with mutation at a proximal position (F490L) present in one p2 population (Figure 2A, Table 2). Viruses passaged in the presence of monoclonal antibody C144 also had mutations at positions E484 and Q493, but not at F490 (Figure 2C, Table 2). In contrast, virus populations passaged in the presence of monoclonal antibody C135 lacked mutations at E484 or Q493, and instead had mutations R346K/S/L and N440K at high frequency (Figure 2C, Table 2).

![Figure 2.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig2-v2.jpg)

**Figure 2.:** (A–D) Graphs depict the S codon position (X-axis) and the frequency of non-synonymous substitutions (Y-axis) following the second passage (p2) of rVSV/SARS-CoV-2/GFP on 293T/ACE2(B) cells in the absence of antibody or plasma (A), or in the presence of 10 μg/ml C121 (B), C135 (C) or C144 (D). Results are shown for both rVSV/SARS-CoV-2/GFP variants (One replicate each for rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 - the frequency of 1D7 mutations is plotted as circles and 2E1 mutations as triangles).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A–B) Graphs depict the S codon position (X-axis) and the frequency of non-synonymous substitutions (Y-axis) following the second, third or fourth passage (p2–p4) of rVSV/SARS-CoV-2/GFP on 293T/ACE2(B) cells in the presence of COV-47 plasma (A), or COV-72 plasma (B). Results are shown for both rVSV/SARS-CoV-2/GFP variants (the frequency of 1D7 mutations is plotted as circles and 2E1 mutations as triangles).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A–B) Graphs depict the S codon position (X-axis) and the frequency of non-synonymous substitutions (Y-axis) following the second, third or fourth passage (p2–p4) of rVSV/SARS-CoV-2/GFP on 293T/ACE2(B) cells in the presence of COV-107 plasma (A), or second passage in the presence of COV-NY plasma (B). Results are shown for both rVSV/SARS-CoV-2/GFP variants (the frequency of 1D7 mutations is plotted as circles and 2E1 mutations as triangles).

**Table 2.**
 Mutations occurring at high frequency during rVSV/SARS-CoV-2 passage in the presence of neutralizing antibodies or plasma.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3">Mutant frequency</th>
    </tr>
    <tr>
      <th></th>
      <th>Mutation</th>
      <th>p2</th>
      <th>p3</th>
      <th>p4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Monoclonal antibodies</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>C121</td>
      <td>E484K*</td>
      <td>0.50, 0.39</td>
      <td>–†</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>F490L</td>
      <td>0.23</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Q493K</td>
      <td>0.12, 0.45</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>C135</td>
      <td>N440K</td>
      <td>0.31, 0.30</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>R346S</td>
      <td>0.30, 0.17</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>R346K</td>
      <td>0.22, 0.53</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>R346M</td>
      <td>0.16</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>C144</td>
      <td>E484K</td>
      <td>0.44, 0.18</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>Q493K</td>
      <td>0.31, 0.39</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Q493R</td>
      <td>0.17, 0.37</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Plasmas</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>COV47</td>
      <td>N148S</td>
      <td>0.16, 0.14</td>
      <td>0.29, 0.30</td>
      <td>0.72, 0.14</td>
    </tr>
    <tr>
      <td></td>
      <td>K150R</td>
      <td>0.10</td>
      <td></td>
      <td>0.18</td>
    </tr>
    <tr>
      <td></td>
      <td>K150E</td>
      <td>0.04</td>
      <td>0.16</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td></td>
      <td>K150T</td>
      <td></td>
      <td></td>
      <td>0.22</td>
    </tr>
    <tr>
      <td></td>
      <td>K150Q</td>
      <td></td>
      <td>0.16</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td></td>
      <td>S151P</td>
      <td>0.1</td>
      <td>0.18</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>COV-NY</td>
      <td>K444R</td>
      <td>0.20,0.19</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>K444N</td>
      <td>0.14</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>K444Q</td>
      <td>0.33</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>V445E</td>
      <td>0.18</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Values represent the decimal frequency with which each mutation occurs ass assessed by NGS, two values indicate occurrences in both rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 cultures, single values indicate occurrence in only one culture.† –, not done._

Mutations at specific positions were enriched in viruses passaged in the presence of convalescent plasma, in two out of four cases (Figure 2—figure supplement 1A,B, Figure 2—figure supplement 2A,B, Table 2). Specifically, virus populations passaged in the presence of COV-NY plasma had mutations within RBD encoding sequence (K444R/N/Q and V445E) that were abundant at p2 (Figure 2—figure supplement 2A,B, Table 2). Conversely, mutations outside the RBD, specifically at N148S, K150R/E/T/Q and S151P in the N-terminal domain (NTD) were present at modest frequency in COV-47 p2 cultures and became more abundant at p3 and p4 (Figure 2—figure supplement 1A,B, Table 2). Replication in the presence of COV72 or COV107 plasma did not lead to the clear emergence of escape mutations, suggesting that the neutralization by these plasmas was not due to one dominant antibody specificity. In the case of COV107, the failure of escape mutants to emerge may simply be due to the lack of potency of that plasma (Table 1). However, in the case of COV-72, combinations of antibodies may be responsible for the potent neutralizing properties of the plasma in that case.

### Isolation and characterization of rVSV/SARS-CoV-2/GFP antibody escape mutants

Based on the aforementioned analyses, supernatants from C121, C144, and C135 and COV-NY plasma p2 cultures, or COV47 p4 cultures, contained mixtures of putative rVSV/SARS-CoV-2/GFP neutralization escape mutants. To isolate individual mutants, the supernatants were serially diluted and individual viral foci isolated by limiting dilution in 96-well plates. Numerous individual rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 derivatives were harvested from wells containing a single virus plaque, expanded on 293T/ACE2(B) cells, then RNA was extracted and subjected to Sanger-sequencing (Figure 3—figure supplement 1). This process verified the purity of the individual rVSV/SARS-CoV-2/GFP variants and yielded a number of viral mutants for further analysis (Figure 3—figure supplement 1). These plaque-purified viral mutants all encoded single amino-acid substitutions in S-coding sequences that corresponded to variants found at varying frequencies (determined by Illumina sequencing) in the antibody-selected viral populations. Notably, each of the isolated rVSV/SARS-CoV-2/GFP mutants replicated with similar kinetics to the parental rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 viruses (Figure 3A), suggesting that the mutations that emerged during replication in the presence of monoclonal antibodies or plasma did not confer a substantial loss of fitness, at least in the context of rVSV/SARS-CoV-2/GFP. Moreover, for mutants in RBD sequences that arose in the C121, C135, C144, and COV-NY cultures, each of the viral mutants retained approximately equivalent sensitivity to neutralization by an ACE2-Fc fusion protein, suggesting little or no change in interaction with ACE2 (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig3-v2.jpg)

**Figure 3.:** (A) Replication of plaque-purified rVSV/SARS-CoV-2/GFP bearing individual S amino-acid substitutions that arose during passage with the indicated antibody or plasma. 293T/ACE2cl.22 cells were inoculated with equivalent doses of parental or mutant rVSV/SARS-CoV-2/GFP isolates. Supernatant was collected at the indicated times after inoculation and number of infectious units present therein was determined on 293T/ACE2cl.22 cells. The mean of two independent experiments is plotted. One set of WT controls run concurrently with the mutants are replotted in the upper and lower left panels, A different set of WT controls run concurrently with the mutants is shown in the lower right panel (B) Infection 293T/ACE2cl.22 cells by rVSV/SARS-CoV-2/GFP encoding the indicated S protein mutations in the presence of increasing amounts of a chimeric ACE2-Fc molecule. Infection was quantified by FACS. Mean of two independent experiments is plotted. The WT controls are replotted in each panel.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The upper panels show sequence traces from amplicons obtained from viral populations following replication in the presence of monoclonal antibodies, the bottom panels show sequence traces of amplicons obtained from mutants isolated by limiting dilution of the viral populations.

We next determined the sensitivity of the isolated RBD mutants to neutralization by the three monoclonal antibodies. The E484K and Q493R mutants that emerged during replication in the presence of C121 or C144, both caused apparently complete, or near complete, resistance to both antibodies (IC50 > 10 μg/ml, Figure 4A,B). However, both of these mutants retained full sensitivity (IC50 < 10 ng/ml) to C135. Conversely, the R346S and N440K mutants that emerged during replication in the presence of C135 were resistant to C135, but retained full sensitivity to both C121 and C144 (Figure 4A,B). The K444N, K444T, V445G, V445E, and V445L mutants that arose during replication in the presence of COV-NY plasma conferred partial resistance to C135, with IC50 values ranging from 25 to 700 ng/ml, but these mutants retained full sensitivity to both C121 and C144 (Figure 4A,B). The spatial distribution of these resistance-conferring mutations on the SARS-CoV-2 S RBD surface suggested the existence of both distinct and partly overlapping neutralizing epitopes on the RBD (Figure 4C). The C121 and C144 neutralizing epitopes appear to be similar, and include E484 and Q493, while a clearly distinct conformational epitope seems to be recognized by C135, that includes R346 and N440 residues. Antibodies that constitute at least part of the neutralizing activity evident in COV-NY plasma appear to recognize an epitope that includes and K444 and V445. The ability of mutations at these residues to confer partial resistance to C135 is consistent with their spatial proximity to the C135 conformational epitope (Figure 4C).

![Figure 4.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig4-v2.jpg)

**Figure 4.:** (A) Examples of neutralization resistance of rVSV/SARS-CoV-2/GFP mutants that were isolated following passage in the presence of antibodies. 293T/ACE2cl.22 cells were inoculated with WT or mutant rVSV/SARS-CoV-2/GFP in the presence of increasing amount of each monoclonal antibody, and infection quantified by FACS 16 hr later. Mean and SD from two technical replicates, representative of two independent experiments. (B) Neutralization sensitivity/resistance of rVSV/SARS-CoV-2/GFP mutants isolated following replication in the presence of antibodies. Mean IC50 values were calculated for each virus-monoclonal antibody combination in two independent experiments. (C) Position of neutralization resistance-conferring substitutions. Structure of the RBD (from PDB 6M17 Yan et al., 2020) with positions that are occupied by amino acids where mutations were acquired during replication in the presence of each monoclonal antibody or COV-NY plasma indicated.

To test whether neutralization escape mutations conferred loss of binding to the monoclonal antibodies, we expressed conformationally prefusion-stabilized S-trimers (Hsieh et al., 2020), appended at their C-termini with NanoLuc luciferase (Figure 5A). The S-trimers were incubated in solution with the monoclonal antibodies, complexes were captured using protein G magnetic beads, and the amount of S-trimer captured was measured using NanoLuc luciferase assays (Figure 5A). As expected, C121, C135, and C144 monoclonal antibodies all bound the WT S-trimer (Figure 5B). The E484K and Q493R trimers exhibited complete, or near complete loss of binding to C121 and C144 antibodies but retained WT levels of binding to C135 (Figure 5B). Conversely, the R346S and N440K mutants exhibited complete loss of binding to C135, but retained WT levels of binding to C121 and C144. The K444N and V445E mutants retained near WT levels of binding to all three antibodies, despite exhibiting partial resistance to C135 (Figure 5A,B). Presumably the loss of affinity of these mutants for C135 was sufficient to impart partial neutralization resistance but insufficient to abolish binding in the solution binding assay.

![Figure 5.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig5-v2.jpg)

**Figure 5.:** (A) Schematic representation of the binding assay in which NanoLuc luciferase is appended to the C-termini of a conformationally stabilized S-trimer. The fusion protein is incubated with antibodies and complexes captured using protein G magnetic beads (B) Bound Nanoluc luciferase quantified following incubation of the indicated WT or mutant Nanoluc-S fusion proteins with the indicated antibodies and Protein G magnetic beads. Mean of three technical replicates at each S-Nanoluc concentration.

Analysis of mutants that were isolated from the virus population that emerged during rVSV/SARS-CoV-2/GFP replication in the presence of COV-47 plasma (specifically N148S, K150R, K150E, S151P) revealed that these mutants exhibited specific resistance to COV-47 plasma. Indeed, the COV-47 plasma NT50 for these mutants was reduced by 8- to 10-fold (Figure 6A). This finding indicates that the antibody or antibodies responsible for majority of neutralizing activity in COV-47 plasma target an NTD epitope that includes amino acids 148–151, even though the highly potent monoclonal antibody (C144) isolated from COV-47 targets the RBD. Mutants in the 148–151 NTD epitope exhibited marginal reductions in sensitivity to other plasmas (Figure 6A), indicating that different epitopes are primarily targeted by plasmas from the other donors.

![Figure 6.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig6-v2.jpg)

**Figure 6.:** (A, B) Neutralization of rVSV/SARS-CoV-2/GFP mutants isolated following replication in the presence COV-47 plasma (A) or COV-NY plasma (B). 293T/ACE2cl.22 cells were inoculated with WT or mutant rVSV/SARS-CoV-2/GFP in the presence of increasing amounts of the indicated plasma, and infection quantified by flow cytometry, 16 hr later. Mean of two technical replicates, representative of two independent experiments (C) Plasma neutralization sensitivity/resistance of rVSV/SARS-CoV-2/GFP mutants isolated following replication in the presence of monoclonal antibodies or convalescent plasma. Mean NT50 values were calculated for each virus-plasma combination from two independent experiments.

The viral population that emerged during replication in COV-NY plasma yielded mutants K444N or T and V445G, E or L. Each of these mutations conferred substantial resistance to neutralization by COV-NY plasma, with ~ 10 to 30-fold reduction in NT50 (Figure 6B). Thus, the dominant neutralizing activity in COV-NY plasma is represented by an antibody or antibodies recognizing an RBD epitope that includes K444 and V445. As was the case with COV-47 resistant mutants, viruses encoding the mutations conferring resistance to COV-NY plasma retained almost full sensitivity to neutralization by other plasmas (Figure 6B).

Interestingly, the mutations that conferred complete or near complete resistance to the potent RBD-specific monoclonal antibodies C144, C135, and C121 conferred little or no resistance to neutralization by plasma from the same individual, or other individuals (Figure 6C). These RBD-specific antibodies represent the most potent monoclonal antibodies isolated from COV-47, COV-72, and COV-107, respectively, but the retention of plasma sensitivity by the monoclonal antibody-resistant mutants suggests that these antibodies contribute little to the overall neutralization activity of plasma from the same individual. This finding is consistent with the observation that memory B cells producing these antibodies are rare (Robbiani et al., 2020), and with the results of the selection experiments in which rVSV/SARS-CoV-2/GFP replication in the presence of COV-47, COV-72, and COV-107 plasma did not enrich for mutations that correspond to the neutralization epitopes targeted by the monoclonal antibodies obtained from these individuals (Figure 2—figure supplement 1A,B, Figure 2—figure supplement 2A,B. Table 2). Overall, analysis of even this limited set of monoclonal antibodies and plasmas shows that potent neutralization can be conferred by antibodies that target diverse SARS-CoV-2 epitopes. Moreover, the most potently neutralizing antibodies generated in a given COVID19 convalescent individual may contribute in only a minor way to the overall neutralizing antibody response in that same individual (see discussion).

### Natural occurrence of antibody-resistance RBD mutations

The aforementioned neutralizing antibody escape mutations were artificially generated during in vitro replication of a recombinant virus. However, as monoclonal antibodies are developed for therapeutic and prophylactic applications, and vaccine candidates are deployed, and the possibility of SARS-CoV-2 reinfection becomes greater, it is important both to understand pathways of antibody resistance and to monitor the prevalence of resistance-conferring mutations in naturally circulating SARS-CoV-2 populations.

To survey the natural occurrence of mutations that might confer resistance to the monoclonal and plasma antibodies used in our experiments we used the GISAID (Elbe et al., 2017) and CoV-Glue (Singer et al., 2020) SARS-CoV-2 databases. Among the 55,189 SARS-CoV-2 sequences in the CoV2-Glue database at the time of writing, 2175 different non-synonymous mutations were present in natural populations of SARS-CoV-2 S protein sequences. Consistent with the finding that none of the mutations that arose in our selection experiments gave an obvious fitness deficit (in the context of rVSV/SARS-CoV-2/GFP), most were also present in natural viral populations.

For phenotypic analysis of naturally occurring SARS-CoV-2 S mutations, we focused on the ACE2 interface of the RBD, as it is the target of most therapeutic antibodies entering clinical development (Robbiani et al., 2020; Hansen et al., 2020; Baum et al., 2020), and is also the target of at least some antibodies present in convalescent plasmas. In addition to the mutations that arose in our antibody selection experiments, inspection of circulating RBD sequences revealed numerous naturally occurring mutations in the vicinity of the ACE2 binding site and the epitopes targeted by the antibodies (https://www.gisaid.org, http://cov-glue.cvr.gla.ac.uk) (Figure 7A–D). We tested nearly all of the mutations that are present in the GISAID database as of June 2020, in the proximity of the ACE2 binding site and neutralizing epitopes, for their ability to confer resistance to the monoclonal antibodies, using an HIV-1-based pseudotyped virus-based assay (Figure 7A–C). Consistent with, and extending our findings with rVSV/SARS-CoV-2/GFP, naturally occurring mutations at positions E484, F490, Q493, and S494 conferred complete or partial resistance to C121 and C144 (Figure 7A,C). While there was substantial overlap in the mutations that caused resistance to C121 and C144, there were also clear differences in the degree to which certain mutations (e.g. G446, L455R/I/F, F490S/L) affected sensitivity to the two antibodies. Naturally occurring mutations that conferred complete or partial resistance to C135 were at positions R346, N439, N440, K444, V445 and G446. In contrast to the C121/C144 epitope, these amino acids are peripheral to the ACE2 binding site on the RBD (Figure 7D). Indeed, in experiments where the binding of a conformationally stabilized trimeric S-NanoLuc fusion protein to 293T/ACE2cl.22 cells was measured, preincubation of S-NanoLuc with a molar excess of C121 or C144 completely blocked binding (Figure 7E). Conversely, preincubation with C135 only partly blocked binding to 293T/ACE2cl.22 cells, consistent with the finding that the C135 conformational epitope does not overlap the ACE2 binding site (Figure 7D). C135 might inhibit S-ACE-2 binding by steric interference with access to the ACE two binding site. These results are also consistent with experiments which indicated that C135 does not compete with C121 and C144 for binding to the RBD (Robbiani et al., 2020).

![Figure 7.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig7-v2.jpg)

**Figure 7.:** (A–C) Neutralization of HIV-based reporter viruses pseudotyped with SARS-CoV-2 S proteins harboring the indicated naturally occurring substitutions. 293T/ACE2cl.22 cells were inoculated with equivalent doses of each pseudotyped virus in the presence of increasing amount of C121 (A) C135 (B) or C144 (C). Mean IC50 values were calculated for each virus-antibody combination from two independent experiments. (D) Position of substitutions conferring neutralization resistance relative to the amino acids close to the ACE2 binding site whose identity varies in global SARS-CoV-2 sequences. The RBD structure (from PDB 6M17 Yan et al., 2020) is depicted with naturally varying amino acids close to the ACE2 binding site colored in yellow. Amino acids whose substitution confers partial or complete (IC50 > 10 μg/ml) resistance to each monoclonal antibody in the HIV-pseudotype assays are indicated for C121 (red) C135 (green) and C144 (purple). (E) Binding of S-NanoLuc fusion protein in relative light units (RLU) to 293T or 293T/ACE2cl.22 cells after preincubation in the absence or presence of C121, C135, and C144 monoclonal antibodies. Each symbol represents a technical replicate.

All of the mutations that were selected in our rVSV/SARS-CoV-2/GFP antibody selection experiments as well as other mutations that confer resistance to C121, C144, or C135 are found in naturally circulating SARS-CoV-2 populations at very low frequencies (Figure 8). With one exception (N439K) that is circulating nearly exclusively in Scotland and is present in ~ 1% of COV-Glue database sequences, (and whose frequency may be overestimated due to regional oversampling) all antibody resistance mutations uncovered herein are present in global SARS-CoV-2 at frequencies of < 1 in 1000 sequences (Figure 8). The frequency with which the resistance mutations are present in naturally occurring SARS-CoV-2 sequences appeared rather typical compared to other S mutations, with the caveat that sampling of global SARS-CoV-2 is nonrandom. Therefore, these observations do not provide evidence that the neutralizing activities exhibited by the monoclonal antibodies or plasma samples used herein have driven strong selection of naturally circulating SARS-CoV-2 sequences thus far (Figure 8).

![Figure 8.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig8-v2.jpg)

**Figure 8.:** Global variant frequency reported by CoV-Glue in the SARS-CoV-2 S protein. Each individual variant is indicated by a symbol whose position in the S sequence is indicated on the X-axis and frequency reported by COV-Glue is indicated on the Y-axis. Individual substitutions at positions where mutations conferring resistance to neutralizing antibodies or plasma were found herein are indicated by enlarged and colored symbols: red for C121 and C144, green for C135, purple for COV-47 plasma and orange for COV-NY plasma. The common D/G614 variant is indicated.

### Selection of combinations of monoclonal antibodies for therapeutic and prophylactic applications

The ability of SARS-CoV-2 monoclonal antibodies and plasma to select variants that are apparently fit and that naturally occur at low frequencies in circulating viral populations suggests that therapeutic use of single antibodies might select for escape mutants. To mitigate against the emergence or selection of escape mutations during therapy, or during population-based prophylaxis, we tested whether combinations of monoclonal antibodies could suppress the emergence of resistant variants during in vitro selection experiments. Specifically, we repeated antibody selection experiments in which rVSV/SARS-CoV-2/GFP populations containing 106 infectious virions were incubated with 10 μg/ml of each individual monoclonal antibody, or mixtures containing 5 μg/ml of each of two antibodies (Figure 9). C121 and C144 target largely overlapping epitopes, and mutations conferring resistance to one of these antibodies generally conferred resistance to the other (Figure 7A–D). Therefore, we used mixtures of antibodies targeting clearly distinct epitopes (C121+C135 and C144+C135). As previously, replication of rVSV/SARS-CoV-2/GFP in the presence of a single monoclonal antibody enabled the formation of infected foci in p1 cultures (Figure 9A–C), that rapidly expanded and enabled the emergence of apparently resistant virus populations. Indeed, rVSV/SARS-CoV-2/GFP yields from p2 cultures established with one antibody (C121, C135 or C144) were indistinguishable from those established with no antibody (Figure 9D). Conversely, rVSV/SARS-CoV-2/GFP replication in the presence of mixtures of C121+C135 or C144+C135 led to sparse infection of individual cells in p1 cultures, but there was little or no formation of foci that would suggest propagation of infection from these infected cells (Figure 9A–C), Therefore, it is likely that infected cells arose from rare, non-neutralized, virions that retained sensitivity to at least one of the antibodies in mixture. Consequently, viral spread was apparently completely suppressed and no replication-competent rVSV/SARS-CoV-2/GFP was detected in p2 cultures established with mixtures of the two antibodies (Figure 9D).

![Figure 9.](https://cdn.elifesciences.org/articles/61312/elife-61312-fig9-v2.jpg)

**Figure 9.:** (A) Representative images of 293T/ACE2 (B) cells infected with the equivalent doses of rVSV/SARS-CoV-2/GFP in the absence or presence of 10 μg/ml of one (C144) or 5 μg/ml of each of two (C144 +C135) neutralizing monoclonal antibodies. (B) Expanded view of the boxed areas containing individual plaques from the culture infected in the presence of 10 μg/ml C144. (C) Expanded view of the boxed areas in A containing infected cells from the culture infected in the presence of 5 μg/ml each of (C144 and C135). (D) Infectious virus yield following two passages of rVSV/SARS-CoV-2/GFP in the absence or presence of individual neutralizing antibodies or combinations of two antibodies. Titers were determined on 293T/ACE2cl.22 cells. Each symbol represents a technical replicate and results from two independent experiments using rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 are shown.

## Discussion

The degree to which resistance will impact effectiveness of antibodies in SARS-CoV-2 therapeutic and vaccine settings is currently unclear (Baum et al., 2020). Notably, the inter-individual variation in SARS-CoV-2 sequences is low compared to many other RNA viruses (van Dorp et al., 2020; Rambaut et al., 2020; Dearlove et al., 2020; Rausch et al., 2020), in part because coronaviruses encode a 3’−5’ exonuclease activity. The exonuclease activity provides a proofreading function that enhances replication fidelity and limits viral sequence diversification (Denison et al., 2011).

However, replication fidelity is but one of several variables that affect viral population diversity (Duffy et al., 2008; Moya et al., 2000). One determinant of total viral diversity is population size. Many millions of individuals have been infected by SARS-CoV-2, and a single swab from an infected individual can contain in excess of 109 copies of viral RNA (Wölfel et al., 2020). It follows that SARS-CoV-2 genomes encoding every possible single amino-acid substitution are present in the global population, and perhaps in a significant fraction of individual COVID19 patients. Thus, the frequency with which particular variants occur in the global SARS-CoV-2 population is strongly influenced by the frequency with which negative and positive selection pressures that favor their propagation are encountered, as well as founder effects at the individual patient and population levels (Korber et al., 2020).

Fitness effects of mutations will obviously vary and will suppress the prevalence of deleterious mutations (Dolan et al., 2018; Andino and Domingo, 2015). However, otherwise neutral, or even modestly deleterious, mutations will rise in prevalence if they confer escape from selective pressures, such as immune responses. The prevalence of neutralizing antibody escape mutations will also be strongly influenced by the frequency with which SARS-CoV-2 encounters neutralizing antibodies. Peak viral burden in swabs and sputum, which likely corresponds to peak infectiousness and frequency of transmission events, appears to approximately correspond with the onset of symptoms, and clearly occurs before seroconversion (Wölfel et al., 2020). Thus, it is quite plausible that most transmission events involve virus populations that are yet to experience antibody-imposed selective pressure in the transmitting individual. Such a scenario would reduce the occurrence of antibody escape mutations in natural viral populations. It will be interesting to determine whether viral sequences obtained late in infection are more diverse or have evidence of immunological escape mutations.

There are situations that are anticipated to increase the frequency of encounters between SARS-CoV-2 and antibodies that could impact the emergence of antibody resistance. Millions of individuals have already been infected with SARS-CoV-2 and among them, neutralizing antibody titers are extremely variable (Robbiani et al., 2020; Wu et al., 2020b; Luchsinger et al., 2020). Those with weak immune responses or waning immunity could become re-infected, and if so, that encounters between SARS-CoV-2 and pre-existing but incompletely protective neutralizing antibodies might drive the selection of escape variants (Kk et al., 2020a; Van Elslande et al., 2020; Larson et al., 2020; Kk et al., 2020b). In a similar manner, poorly immunogenic vaccine candidates, convalescent plasma therapy, and suboptimal monoclonal antibody treatment, particularly monotherapy (Baum et al., 2020), could create conditions to drive the acquisition of resistance to commonly occurring antibodies in circulating virus populations.

The extent to which SARS-CoV-2 evasion of individual antibody responses would have pervasive effects on the efficacy of vaccines and monoclonal antibody treatment/therapy will also be influenced by the diversity of neutralizing antibody responses within and between individuals. Analysis of potent neutralizing antibodies cloned by several groups indicates that potent neutralizing antibodies are commonly elicited, and very similar antibodies, such as those containing IGHV3-53 and IGHV3-66 can be found in different individuals (Robbiani et al., 2020; Barnes et al., 2020; Yuan et al., 2020). These findings imply a degree of homogeneity the among neutralizing antibodies that are generated in different individuals. Nevertheless, each of the four convalescent plasma tested herein had distinct neutralizing characteristics. In two of the four plasma tested, selection experiments suggested that a dominant antibody specificity was responsible for a significant fraction of the neutralizing capacity of the plasma. However, the failure of single amino-acid substitutions to confer complete resistance to any plasma strongly suggests the existence of multiple neutralizing specificities in each donor. Indeed, in one example (COV47), viral mutants that were completely resistant to a potent monoclonal antibody from that donor (C144), retained near complete sensitivity to plasma from that same individual, Thus, in that individual other antibodies in the plasma, not the most potent monoclonal antibody, must dominate the neutralizing activity of the plasma. That COV47 plasma selected mutations at a different site in S (NTD) to that selected by C144 (RBD), is orthogonal supportive evidence that the C144 monoclonal antibody does not constitute the major neutralizing activity in the plasma of COV47.

The techniques described herein could be adapted to broadly survey the diversity of SARS-CoV-2 neutralizing specificities in many plasma samples following natural infection or vaccination, enabling a more complete picture of the diversity of SARS-CoV-2 neutralizing antibody responses to be developed. Indeed, the approach described herein can be used to map epitopes of potent neutralizing antibodies rapidly and precisely. It has an advantage over other epitope mapping approaches (such as array-based oligo-peptide scanning or random site-directed mutagenesis) (Greaney et al., 2020), in that selective pressure acts solely on the naturally formed, fusion-competent viral spike. While mutations outside the antibody binding sites might lead to resistance, the functional requirement will prohibit mutations that simply disrupt the native conformation. Indeed, we found that the neutralizing antibody escape mutations described herein did not detectably alter rVSV/SARS-CoV-2/GFP replication, did not affect ACE2-Fc sensitivity and were found in natural populations at unexceptional frequencies, consistent with the notion that they do not have large effects on fitness in the absence of neutralizing antibodies. That said, the selection/viral evolution scheme described herein approximates to but does not precisely recapitulate the evolutionary dynamics that would play out in natural SARS-CoV-2 infection. Differences in viral populations sizes, replication fidelity and fitness effects of mutations in SARS-CoV-2 versus rVSV/SARS-CoV-2/GFP, and the complexity and changing nature of evolving antibody responses could all affect the nature of, and response to, selection pressures. For example, one caveat is the utilization of plasma for selection experiments. Immunoglobulin subtypes (e.g. IgA versus IgG) are differentially represented in plasma versus the respiratory tract, and the concentrations of each immunoglobulin subtype or specificity precisely at the sites of SARS-CoV-2 replication is unknown. However, it is known that IgG that dominates plasma immunoglobulins is also present in lung secretions, albeit at lower levels than IgA (Burnett, 1986). Moreover, our recent work has indicated that at least some of the neutralizing activity in plasma is contributed by IgA and several of the antibody lineages that we have cloned from SARS-CoV-2 convalescents are class switched to both IgA and IgG (Wang et al., 2020). Overall, it is likely that the antibody specificities present in the respiratory tract broadly reflect, but perhaps do not precisely recapitulate, those present in the plasma used for the selection experiments described herein.

Human monoclonal antibodies targeting both the NTD and RBD of SARS-CoV-2 have been isolated, with those targeting RBD being especially potent. As these antibodies are used clinically (Hansen et al., 2020; Baum et al., 2020), in therapeutic and prophylactic modes, it will be important to identify resistance mutations and monitor their prevalence in a way that is analogous to antiviral and antibiotic resistance monitoring in other infectious diseases. Moreover, as is shown herein, the selection of antibody mixtures with non-overlapping escape mutations should reduce the emergence of resistance and prolong the utility of antibody therapies in SARS-CoV-2 infection.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>VSV/SARS-CoV-2/GFP1D7; WT1D7</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td>Recombinant chimeric VSV/SARS-CoV-2 reporter virus</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>rVSV/SARS-CoV-2/GFP2E1; WT2E1</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td>Recombinant chimeric VSV/SARS-CoV-2 reporter virus</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>E484K2E1</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>Q493R1D7</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>R346S1D7</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>R3462E1</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>N440K2E1</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>K444N1D7</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>K444T2E1</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>V445G2E1</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>V445E1D7</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>V445L2E1</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>N148S</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>K150R</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>K150E</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Strain, strain background (Vesicular Stomatitis Virus)</td>
      <td>S151P</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>mutant rVSV/SARS-CoV-2/GFP derivative Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Expi293F Cells</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# A14527</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>293T (embryonic, kidney)</td>
      <td>ATCC</td>
      <td>CRL-3216</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>293T/ACE2(B)</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td>293 T cells expressing human ACE2 (bulk population)</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>293T/ACE2cl.22</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td>293 T cells expressing human ACE2 (single cell clone)</td>
    </tr>
    <tr>
      <td>Biological sample (H. sapiens)</td>
      <td>COV-47</td>
      <td>Robbiani et al., 2020</td>
      <td></td>
      <td>Human plasma sample</td>
    </tr>
    <tr>
      <td>Biological sample (H. sapiens)</td>
      <td>COV-72</td>
      <td>Robbiani et al., 2020</td>
      <td></td>
      <td>Human plasma sample</td>
    </tr>
    <tr>
      <td>Biological sample (H. sapiens)</td>
      <td>COV-107</td>
      <td>Robbiani et al., 2020</td>
      <td></td>
      <td>Human plasma sample</td>
    </tr>
    <tr>
      <td>Biological sample (H. sapiens)</td>
      <td>COV-NY</td>
      <td>Luchsinger et al., 2020</td>
      <td></td>
      <td>Human plasma sample</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>C121 (Human monoclonal)</td>
      <td>Robbiani et al., 2020</td>
      <td></td>
      <td>Selection experiments (10 μg/ml, 5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>C135 (Human monoclonal)</td>
      <td>Robbiani et al., 2020</td>
      <td></td>
      <td>Selection experiments (10 μg/ml, 5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>C144 (Human monoclonal)</td>
      <td>Robbiani et al., 2020</td>
      <td></td>
      <td>Selection experiments (10 μg/ml, 5 μg/ml)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CSIB(ACE2)</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHIVNLGagPol</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCCNanoLuc2AEGFP</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSARS-CoV-2Δ19</td>
      <td>Schmidt et al., 2020</td>
      <td></td>
      <td>Epression plasmid containing a C-terminally truncated SARS-CoV-2 S protein (pSARS-CoV-2Δ19) containing a synthetic human-codon-optimized cDNA (Geneart)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>R346S</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>R346K</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V367F</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>N439K</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>rRcombinant DNA reagent</td>
      <td>N440K</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>K444Q</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>K444R</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>K444N</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V445I</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V445E</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V445L</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V445K</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>G446V</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>G446S</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>L455R</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>L455I</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>L455F</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>F456V</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>A475V</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>A475D</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>G476A</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>G476S</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>T487I</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V483I</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V483A</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V483F</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>E484Q</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>E484A</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>E484D</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>F490S</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>F490L</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Q493K</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Q493R</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>S494P</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>N501Y</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V503F</td>
      <td>Schmidt et al., 2020, and this paper</td>
      <td></td>
      <td>pSARS-CoV-2Δ19 containing the indicated mutation. Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>endof_M_for</td>
      <td>This paper</td>
      <td>PCR and sequencing primer</td>
      <td>CTATCGGCCACTTCAAATGAGCTAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>L_begin_rev</td>
      <td>This paper</td>
      <td>PCR and sequencing primer</td>
      <td>TCATGGAAGTCCACGATTTTGAGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>VSV-RBD-F primer</td>
      <td>This paper</td>
      <td>PCR and sequencing primer</td>
      <td>CTGGCTCTGCACAGGTCCTACCTGACA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>VSV-RBD-R primer</td>
      <td>This paper</td>
      <td>PCR and sequencing primer</td>
      <td>CAGAGACATTGTGTAGGCAATGATG</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>ACE2-Fc fusion protein</td>
      <td>This paper</td>
      <td></td>
      <td>Recombinant ACE2 extracellular domain fused to IgG1 Fc see Materials and Methods Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>S-6P-NanoLuc</td>
      <td>This paper</td>
      <td></td>
      <td>A conformationally stabilized (6P) version of the SARS-CoV-2 S protein fused to Nanoluciferase See materials and methods Inquiries should be addressed to P.Bieniasz</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Trizol-LS</td>
      <td>Thermo Fisher</td>
      <td>Cat# 10296028</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Superscript III reverse transcriptase</td>
      <td>Thermo Fisher</td>
      <td>Cat# 18080093</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Nextera TDE1 Tagment DNA enzyme</td>
      <td>Illumina</td>
      <td>Cat# 15027865</td>
      <td>0.25 µl</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TD Tagment DNA buffer</td>
      <td>Illumina</td>
      <td>Cat# 15027866</td>
      <td>1.25 µl</td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>Nextera XT Index Kit v2</td>
      <td>Illumina</td>
      <td>Cat# FC-131–2001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>KAPA HiFi HotStart ReadyMix</td>
      <td>KAPA Biosystems</td>
      <td>Cat# KK2601</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>AmPure Beads XP</td>
      <td>Agencourt</td>
      <td>Cat# A63881</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Expi293 Expression System Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# A14635</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Ni-NTA Agarose</td>
      <td>Qiagen</td>
      <td>Cat# 30210</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>HRV 3C Protease</td>
      <td>TaKaRa</td>
      <td>Cat# 7360</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>LI-COR Intercept blocking buffer</td>
      <td>Licor</td>
      <td>P/N 927–70001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Dynabeads Protein G</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 10004D</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Passive Lysis 5X Buffer</td>
      <td>Promega</td>
      <td>Cat# E1941</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Nano-Glo Luciferase Assay System</td>
      <td>Promega</td>
      <td>Cat# N1150</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geneious Prime</td>
      <td>https://www.geneious.com/</td>
      <td>RRID:SCR_010519</td>
      <td>Version 2020.1.2</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python programming language</td>
      <td>https://www.python.org/</td>
      <td>RRID:SCR_008394</td>
      <td>version 3.7</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pandas</td>
      <td>10.5281/zenodo.3509134</td>
      <td>RRID:SCR_018214</td>
      <td>Version 1.0.5</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>numpy</td>
      <td>10.1038/s41586-020-2649-2</td>
      <td>RRID:SCR_008633</td>
      <td>Version 1.18.5</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>matplotlib</td>
      <td>10.1109/MCSE.2007.55</td>
      <td>RRID:SCR_008624</td>
      <td>Version 3.2.2</td>
    </tr>
  </tbody>
</table>

### Plasmid constructs

A replication-competent rVSV/SARS-CoV-2/GFP chimeric virus clone, encoding the SARS-CoV-2 spike protein lacking the C-terminal 18 codons in place of G, as well as GFP immediately upstream of the L (polymerase) has been previously described (Schmidt et al., 2020). The pHIV-1NLGagPol and pCCNG/nLuc constructs that were used to generate SARS-CoV-2 pseudotyped particles have been previously described (Schmidt et al., 2020). The pSARS-CoV-2 protein expression plasmid containing a C-terminally truncated SARS-CoV-2 S protein (pSARS-CoV-2Δ19) containing a synthetic human-codon-optimized cDNA (Geneart) has been previously described (Schmidt et al., 2020) and was engineered to include BamHI, MfeI, BlpI and AgeI restriction enzyme sites flanking sequences encoding the RBD. Gibson assembly was used to introduce mutant RBD sequences into this plasmid, that were generated synthetically (g/eBlocks IDT) or by overlap extension PCR with primers that incorporated the relevant nucleotide substitutions.

### Cell lines

HEK-293T cells and derivatives were cultured in Dulbecco’s Modified Eagle Medium (DMEM) supplemented with 10% fetal bovine serum (FBS) at 37°C and 5% CO2. All cell lines have been tested negative for contamination with mycoplasma. Derivatives expressing ACE2 were generated by transducing 293T cells with CSIB(ACE2) vector and the uncloned bulk population 293T/ACE2(B) or a single-cell clone 293T/ACE2.cl22 (Schmidt et al., 2020) were used.

### Replication-competent VSV/SARS-CoV-2/GFP chimeric virus

The generation of infectious rVSV/SARS-CoV-2/GFP chimeric viruses stocks has been previously described (Schmidt et al., 2020). Two plaque-purified variants designated rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 that encode F157S/R685M (1D7) and D215G/R683G (2E1) substitutions were used in these studies. The rVSV/SARS-CoV-2/GFP chimeric virus was used under enhanced BSL-2 conditions. i.e in a BLS-2 laboratory with BSL-3 like precautions.

### HIV-1/CCNanoLuc2AEGFP-SARS-CoV-2 pseudotype particles

The HIV-1/NanoLuc2AEGFP-SARS-CoV-2 pseudotyped virions were generated as previously described (Schmidt et al., 2020). Briefly, 293T cells were transfected with pHIVNLGagPol, pCCNanoLuc2AEGFP and a WT or mutant SARS-CoV-2 expression plasmid (pSARS-CoV-2Δ19) using polyethyleneimine. At 48 hr after transfection, the supernatant was harvested, clarified, filtered, aliquoted and stored at −80°C.

### Infectivity assays

To measure the infectivity of pseudotyped or chimeric viral particles, viral stocks were serially diluted and 100 µl of each dilution added to 293T/ACE2cl.22 target cells plated at 1 × 104 cells/well in 100 µl medium in 96-well plates the previous day. Cells were then cultured for 48 hr (HIV-1 pseudotyped viruses) or 16 hr (replication-competent rVSV/SARS-CoV-2/GFP), unless otherwise indicated, and then photographed or harvested for NanoLuc luciferase or flow cytometry assays.

### Selection of viruses in the presence of antibodies

For selection of viruses resistant to plasma or monoclonal antibodies, rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 populations containing 106 infectious particles were used. To generated the viral populations for selection experiments,, rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 were passaged generate diversity, incubated with dilutions of monoclonal antibodies (10 μg/ml, 5 μg/ml) or COVID19 plasma (1:50, 1:250, 1:500) for 1 hr at 37 °C. Then, the virus-antibody mixtures were incubated with 2 × 105 293T/ACE2(B) cells in 12-well plates. Two days later, the cells were imaged and supernatant from the wells containing the highest concentration of plasma or monoclonal antibodies that showed evidence of viral replication (GFP-positive foci) or large numbers of GFP-positive cells was harvested. A 100 μl of the cleared supernatant was incubated with the same dilution of plasma or monoclonal antibody and then used to infect 2 × 105 293T/ACE2(B) cells in 12-well plates, as before. rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 were passaged in the presence of C121 or C144 two times before complete escape was apparent. rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 were passaged with C135 or plasma samples up to five times.

To isolate individual mutant viruses, selected rVSV/SARS-CoV-2/GFP1D7 and rVSV/SARS-CoV-2/GFP2E1 populations were serially diluted in medium without antibodies and individual viral variants isolated by visualizing single GFP-positive plaques at limiting dilutions in 96-well plates containing 1 × 104 293T/ACE2(B) cells. These plaque-purified viruses were expanded, and further characterized using sequencing, spreading replication and neutralization assays.

### Sequence analyses

For the identification of putative antibody resistance mutations, RNA was isolated from aliquots of supernatant containing selected viral populations or individual plaque-purified variants using Trizol-LS. The purified RNA was subjected to reverse transcription using random hexamer primers and Superscript III reverse transcriptase (Thermo Fisher Scientific, US). The cDNA was amplified using Phusion (NEB, US) and primers flanking RBD encoding sequences. Alternatively, a fragment including the entire S-encoding sequence was amplified using primers targeting VSV-M and VSV-L. The PCR products were gel-purified and sequenced either using Sanger-sequencing or NGS as previously described (Gaebler et al., 2019). Briefly, 1 µl of diluted DNA was used for the tagmentation reactions with 0.25 µl Nextera TDE1 Tagment DNA enzyme (catalog no. 15027865), and 1.25 µl TD Tagment DNA buffer (catalog no. 15027866; Illumina). Subsequently, the DNA was ligated to unique i5/i7 barcoded primer combinations using the Illumina Nextera XT Index Kit v2 and KAPA HiFi HotStart ReadyMix (2X; KAPA Biosystems) and purified using AmPure Beads XP (Agencourt), after which the samples were pooled into one library and subjected to paired-end sequencing using Illumina MiSeq Nano 300 V2 cycle kits (Illumina) at a concentration of 12pM.

For analysis of NGS data, the raw paired-end reads were pre-processed to remove adapter sequences and trim low-quality reads (Phred quality score < 20) using BBDuk. Filtered reads were mapped to the codon-optimized SARS-CoV-2 S sequence in rVSV/SARS-CoV-2/GFP using Geneious Prime (Version 2020.1.2). Mutations were annotated using Geneious Prime, with a P-value cutoff of 10−6. Information regarding RBD-specific variant frequencies, their corresponding P-values, and read depth were compiled using the Python programming language (version 3.7) running pandas (1.0.5), numpy (1.18.5), and matplotlib (3.2.2).

### Neutralization assays

To measure neutralizing antibody activity in plasma, serial dilutions of plasma beginning with a 1:12.5 or a 1:100 (for plasma COV-NY) initial dilution were five-fold serially diluted in 96-well plates over six or eight dilutions. For monoclonal antibodies, or an ACE2-IgG1Fc fusion protein the initial dilution started at 40 µg/ml. Thereafter, approximately 5 × 104 infectious units of rVSV/SARS-CoV-2/GFP or 5 × 103 infectious units of HIV/CCNG/nLuc/SARS-CoV-2 were mixed with the plasma or mAb at a 1:1 ratio and incubated for 1 hr at 37°C in a 96-well plate. The mixture was then added to 293T/ACE2cl.22 target cells plated at 1 × 104 cells/well in 100 µl medium in 96-well plates the previous day. Thus, the final starting dilutions were 1:50 or 1:400 (for COV-NY) for plasma and 10 µg/ml for monoclonal antibodies. Cells were then cultured for 16 hr (for rVSV/SARS-CoV-2/GFP) or 48 hr (for HIV/CCNG/nLuc/SARS-CoV-2). Thereafter, cells were harvested for flow cytometry or NanoLuc luciferase assays.

### Antibody-binding and ACE2-binding inhibition assay

A conformationally stabilized (6P) version of the SARS-CoV-2 S protein (Hsieh et al., 2020), appended at its C-terminus with a trimerization domain, a GGSGGn spacer sequence, NanoLuc luciferase, Strep-tag, HRV 3C protease cleavage site and 8XHis (S-6P-NanoLuc) was expressed and purified from the supernatant of 293T Expi cells. Mutants thereof were also expressed and purifies following substitution of sequences encoding the RBD that originated from the unmodified S-expression plasmids.

For antibody-binding assays, 20, 40, or 80 ng S-6P-NanoLuc (or mutants thereof) were mixed with 100 ng of antibodies, C121, C135, or C144, diluted in LI-COR Intercept blocking buffer, in a total volume of 60 μl/well in 96-well plate. After a 30 min incubation, 10 µl protein G magnetic beads was added to each well and incubated for 1.5 hr. The beads were then washed three times and incubated with 30 µl lysis buffer (Promega). Then 15 μl of the lysate was used to measure bound NanoLuc activity.

For ACE2-binding inhibition assays, 20 ng of S-6P-NanoLuc was mixed with 100 ng of antibodies, C121, C135, or C144, diluted in 3% goat serum/PBS, in a total volume of 50 μl. After 30 min incubation, the mixture was incubated with 1 × 105 293 T cells, or 293T/ACE2cl.22 cells for 2 hr at 4°C. The cells were then washed three times and lysed with 30 μl lysis buffer and 15 μl of the lysate was used to measure bound NanoLuc activity.

### Reporter gene assays

For the NanoLuc luciferase assays, cells were washed gently, twice with PBS and lysed in Lucifersase Cell culture Lysis reagent (Promega). NanoLuc luciferase activity in the lysates was measured using the Nano-Glo Luciferase Assay System (Promega) and a Modulus II Microplate Multimode reader (Turner BioSystem) or a Glowmax Navigator luminometer (Promega), as described previously (Schmidt et al., 2020). To record GFP+ cells, 12-well plates were photographed using an EVOS M7000 automated microscope. For flow cytometry, cells were trypsinized, fixed and enumerated using an Attune NxT flow cytometer. The half maximal inhibitory concentrations for plasma (NT50), and monoclonal antibodies (IC50) was calculated using 4-parameter nonlinear regression curve fit to raw or normalized infectivity data (GraphPad Prism). Top values were unconstrained, the bottom values were set to zero.

### Human plasma samples and monoclonal antibodies

The human plasma samples COV-47, COV-72 and COV-107 and monoclonal antibodies C144, C135 and C121 used in this study were previously reported (Robbiani et al., 2020). The human plasma sample COV-NY was obtained from the New York Blood Center (Luchsinger et al., 2020). All plasma samples were obtained under protocols approved by Institutional Review Boards at both institutions.

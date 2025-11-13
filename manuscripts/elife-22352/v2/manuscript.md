# Sloppy morphological tuning in identified neurons of the crustacean stomatogastric ganglion

## Authors

- Adriane G Otopalik<sup>1</sup> ([ORCID: 0000-0002-3224-6502](https://orcid.org/0000-0002-3224-6502)) †
- Marie L Goeritz<sup>1</sup>
- Alexander C Sutton<sup>1</sup>
- Ted Brookings<sup>1</sup>
- Cosmo Guerini<sup>1</sup>
- Eve Marder<sup>1</sup> ([ORCID: 0000-0001-9632-5448](https://orcid.org/0000-0001-9632-5448)) †

### Affiliations

1. Biology Department and Volen Center Brandeis University Waltham United States

† Corresponding author

## Abstract

Neuronal physiology depends on a neuron’s ion channel composition and unique morphology. Variable ion channel compositions can produce similar neuronal physiologies across animals. Less is known regarding the morphological precision required to produce reliable neuronal physiology. Theoretical studies suggest that moraphology is tightly tuned to minimize wiring and conduction delay of synaptic events. We utilize high-resolution confocal microscopy and custom computational tools to characterize the morphologies of four neuron types in the stomatogastric ganglion (STG) of the crab Cancer borealis. Macroscopic branching patterns and fine cable properties are variable within and across neuron types. We compare these neuronal structures to synthetic minimal spanning neurite trees constrained by a wiring cost equation and find that STG neurons do not adhere to prevailing hypotheses regarding wiring optimization principles. In this highly modulated and oscillating circuit, neuronal structures appear to be governed by a space-filling mechanism that outweighs the cost of inefficient wiring.

## Introduction

Neuronal physiology arises from a neuron’s ion channel distribution and its unique geometry. Numerous studies have shown that neurons and circuits can function despite remarkable variability in their ion channel composition (Prinz et al., 2004; Schulz et al., 2006; Goaillard et al., 2009; Norris et al., 2011; Roffman et al., 2012; Gutierrez et al., 2013; Sakurai et al., 2014; see Marder and Goaillard (2006), Calabrese et al. (2011) and Marder et al. (2015) for reviews). These observations suggest that neurons can generate robust, highly conserved firing patterns despite some degree of sloppiness in their underlying physiological parameters.

In contrast, it is often assumed that precise neuronal computations and plasticity rules arise from specialized neuronal morphologies (Mainen and Sejnowski, 1996; Stiefel and Sejnowski, 2007; Cuntz et al., 2010). Experimental and theoretical studies have argued that optimal wiring principles determine neuronal structure during development (Chklovskii, 2000, 2004; Chen et al., 2006; Wen and Chklovskii, 2008; Cuntz et al., 2007, 2010, 2012; Kim et al., 2012). Yet, surprisingly, few studies (Goodman, 1976, 1978; Miller and Jacobs, 1984; Wang et al., 2002; Cuntz et al., 2008, 2010) have reconstructed multiple neurons of the same type at high enough resolution to observe or quantify the stereotypy expected to arise during development, given such optimization principles. Thus, relatively little is known regarding the practical applications of such growth rules and the degree of morphological precision required to produce reliable neuronal physiology in varying circuit contexts.

Here, we present quantitative morphological analyses of macroscopic branching patterns and finer cable propertises, within and across four identified neuron types in the stomatogastric ganglion (STG) of the crab, Cancer borealis, a small central-pattern generating circuit. The 26 neurons of the crab STG have large somata (50–150 µm in diameter) situated around a dense neuropil region, wherein synaptic connections are made (Maynard, 1971; Maynard and Dando, 1974; King, 1976a, 1976b; Kilman and Marder, 1996). STG neurons have complex, highly branched structures that ramify throughout the neuropil region (Baldwin and Graubard, 1995; Wilensky et al., 2003; Bucher et al., 2007; Thuma et al., 2009) and are subject to modulation by numerous peptides and amines released diffusely in the hemolymph and by descending modulatory inputs (Christie et al., 1995a, 1995b, 1997; Goldberg et al., 1988; Marder et al., 1986; see Marder and Bucher (2007) and Nusbaum and Blitz, 2012 for reviews). The 14 identified STG neuron types are physiologically defined by their muscle innervation patterns (Maynard and Dando, 1974), highly conserved voltage waveforms, and participation in one or both of two rhythms: the fast, ongoing pyloric rhythm and the slow, episodic gastric mill rhythm (Harris-Warrick et al., 1992). STG circuit function is mediated predominately by slow oscillations (Graubard and Ross, 1985; Ross and Graubard, 1989) and graded inhibitory transmission (Eisen and Marder, 1982; Marder and Eisen, 1984; Maynard and Walton, 1975; Graubard et al., 1980; Manor et al., 1997, 1999). In fact, phase relationships between STG neurons can be maintained in the absence of spikes (Graubard, 1978; Raper, 1979; Graubard et al., 1983; Anderson and Barker, 1981).

Recent work demonstrated that, despite their morphological complexity, STG neurons are electrotonically compact (Otopalik et al., 2017). Thus, the slow voltage events arising from graded synaptic transmission undergo minimal electrotonic decrement across the neuronal structure. Such electrotonic structures could feasibly mask animal-to-animal variability in neuronal morphology within identified STG neuron types. Additionally, given their compact electrotonic structures, it is plausible that developmental growth of STG neurons may not be constrained by wiring optimization rules, but perhaps other rules that speak to their role in this highly modulated, oscillating circuit. In the present study, we quantitatively characterize the morphology of four STG neuron types across several animals. Then, we investigate whether these identified neurons adhere to prevailing wiring optimization principles.

## Results

The neurons of the STG of the crab Cancer borealis each have a primary neurite that branches extensively throughout the neuropil, forming synapses. This primary neurite also gives rise to one or multiple axons that project to specific stomach muscles or anterior ganglia (Maynard, 1971; Maynard and Dando, 1974; King, 1976a, 1976b; Kilman and Marder, 1996). Figure 1A shows an exemplar gastric mill (GM) neuron situated in the STG neuropil. The stomatogastric nerve (stn) contains dozens of descending neuromodulatory inputs that branch extensively throughout the neuropil and diffusely release a cocktail of peptides and amines (Marder and Bucher, 2007; Nusbaum and Blitz, 2012).The four neuron types examined here are motor neurons and send axons through either the anterior lateral nerve (aln) or dorsal ventricular nerve (dvn; Figure 1B). GM neurons (four copies in each STG) typically have 3–5 axons, with one or multiple axons projecting to the alns and dvn (Figure 1Bi). In contrast, the lateral gastric (LG, one copy in each STG), pyloric dilator (PD; two copies in each STG), and lateral pyloric (LP, one copy in each STG) neurons project single axons down the dvn (Figure 1Bii–iv).

![Figure 1.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig1-v2.jpg)

**Figure 1.:** Each neuron has a primary neurite that ramifies throughout the neuropil and sends one or more axons to peripheral muscles or ganglia via the anterior lateral (aln) or dorsal ventricular (dvn) nerves. (A) Schematic of a gastric mill (GM) neuronal dye-fill as situated in the intact ganglion and the aln, dvn, and stomatogastric nerve (stn). Other cell bodies are outlined in white. (B) Maximum-intensity projections of four Lucifer yellow dye-filled STG neurons. The GM neuron (i) has multiple axons that exit the neuropil bilaterally via the alns, and posteriorly via the dvn. The lateral gastric (LG, ii), lateral pyloric (LP, iii), and pyloric dilator (PD, iv) neurons, respectively, each project only one axon that leaves the neuropil via the dvn. (C) Locations of identified somata across different preparations. Within each preparation, positions were normalized to the ganglion center-of-mass (at origin) and oriented with the stomatogastric nerve (stn) at the top and dorsal ventral nerve (dvn) at the bottom (as described in Materials and methods). (D) Image of neuronal dye-fill (yellow) with path (purple dashed line) from soma to the first multi-furcation, or ‘hand-like’ structure (H).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Following physiological identification, Lucifer yellow dye-fills were amplified immunohistochemically and secondarily labeled with an Alexa Fluor 488 fluorophore (Molecular Probes); all images were collected at 63x magnification utilizing a Leica SP5 CLEM confocal microscope (as described in Materials and methods). This figure shows the maximum projections of the complete confocal image stacks of the four LP neurons used in this study. LP neurons have single axons projecting posteriorly to the dorsal ventral nerve (dvn).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Following physiological identification, Lucifer yellow dye-fills were amplified immunohistochemically and secondarily labeled with an Alexa Fluor 488 fluorophore (Molecular Probes); all images were collected at 63x magnification utilizing a Leica SP5 CLEM confocal microscope (as described in Materials and methods). This figure shows the maximum projections of the complete confocal image stacks of the four PD neurons used in this study. PD neurons have single axons projecting posteriorly to the dorsal ventral nerve (dvn).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Following physiological identification, Lucifer yellow dye-fills were amplified immunohistochemically and secondarily labeled with an Alexa Fluor 488 fluorophore (Molecular Probes); all images were collected at 63x magnification utilizing a Leica SP5 CLEM confocal microscope (as described in Materials and methods). This figure shows the maximum projections of the complete confocal image stacks of the four LG neurons used in this study. LG neurons have single axons projecting posteriorly to the dvn.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Following physiological identification, Lucifer yellow dye-fills were amplified immunohistochemically and secondarily labeled with an Alexa Fluor 488 fluorophore (Molecular Probes); all images were collected at 63x magnification utilizing a Leica SP5 CLEM confocal microscope (as described in Materials and methods). This figure shows the maximum projections of the complete confocal image stacks of the four GM neurons used in this study. GM neurons have multiple axons projecting to both the dvn and one or both of the anterior lateral nerves (aln; which exit the ganglion on either side).

To quantify and compare macroscopic and finer morphological properties within and across these four neuron types (N = 4 of each type), we manually traced high-resolution confocal image stacks of their Lucifer Yellow dye-fills (see Figure 1—figure supplement 1–4 for images of all 16 neurons) and then extracted the following measurements from either the confocal imaging stacks directly or skeletal reconstructions using a suite of quantitative morphology tools written in Python (see Materials and methods for in-depth description of our approach; all scripts are publicly available in the Marder Lab GitHub repository at github.org/marderlab). These data are presented in three sections: (1) Macroscopic Structure, which presents quantitative measures of somata size and location, hand-like features, and neuropil branching patterns; (2) Fine Structure, which describes neurite lengths, diameters, and branch point geometry—all features that are critical for the propagation of voltage signals across the neurite tree; and (3) an investigation of wiring optimization principles and whether they apply to STG neurons.

### I. Macroscopic structure

#### Somata, hand- and hair-like structures

Each of the 16 neurons had a relatively large soma diameter (pooled mean ± SD = 125.8 ± 47.5 µm across all neurons). Earlier work in lobster, Homarus americanus and Panulirus interruptus, STG suggested some stereotypy in soma positions of certain neuron classes (Bucher et al., 2007 and Thuma et al., 2009, respectively). Of the 16 neurons described here, 75% were situated on the posterior side of the neuropil (schematized as a gray shaded area). However, soma locations varied within and across cell types (Figure 1C).

Many STG neurite trees contain a ‘hand-like’ structure, defined as a thick segment that ‘sends off a number of secondary neurites’ and emerges from a comparatively thin primary neurite (Example indicated in Figure 1D as 'H'; Bucher et al., 2007). This hand-like structure was observed in every GM and LG neuron, but not in any LP neurons. Of the neurons used in this study, half of the PD neurons had something that could be considered hand-like. Thus, relative to the other three neuron types, LP neurons can be distinguished by their lack of hand-like structures. We also observed the presence of ‘hair-like’ neurites: very thin (<1 µm) neurites that are more than 50 µm in length in all neurons.

#### Expansive and complex neurite trees

Each of the neurons in Figure 1 exhibits an expansive and complex neurite tree that ramifies throughout the STG neuropil. All 16 neurons examined had more than 10 mm of neurite in their neurite trees (Table 1). Despite a high mean total wiring length across all neurons examined (pooled mean ± SD = 37515 ± 27498 µm; N = 16), there was quite a bit of variability across neurons (CV = 0.73; N = 16). Across neuron types, GM neurons presented significantly greater mean total wiring lengths relative to the other three neuron types (ANOVA; [F(3,12)=8.34, p=0.0029]; Tukey HSD) with a mean ± SD of 74, 890 ± 26581 µm. LG, LP, and PD neurons had within-cell-type mean (± SD) total wirings of 30,583 ± 18,346 µm, 24,321 ± 11,777 µm, and 20,266 ± 65,805 µm, respectively – all less than 50% of the mean GM total wiring length (Figure 2A). GM neurons also had a greater number of soma-to-tip neurite paths (Figure 2B, Table 1; ANOVA; [F(3,12)=7.14, p=0.0052]; Tukey HSD).

**Table 1.**
 Anatomical properties of GM, LG, LP, and PD neurons. Soma-to tip neurite lengths, tortuosities, and diameters are reported as a mean ± standard deviation, with the exception of the initial primary neurite (1°) diameters (for which there are single values for each neuron). Soma-to-tip neurite, branch point, and subtree values are counts for each neuron. These data are plotted in Figures 2, 4, 7, 8 and 10.


<table>
  <thead>
    <tr>
      <th>Cell type</th>
      <th>Soma-to-Tip neurites</th>
      <th>Branch points</th>
      <th>Subtrees</th>
      <th>Total wiring (µm)</th>
      <th>Tortuosity</th>
      <th>Soma-to-Tip neuritelength (µm)</th>
      <th colspan="4">Neurite diameters (µm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7"></td>
      <td>1°</td>
      <td>2°</td>
      <td>3°</td>
      <td>Tip</td>
    </tr>
    <tr>
      <td>GM</td>
      <td>2675</td>
      <td>2671</td>
      <td>30</td>
      <td>60,796</td>
      <td>2.6 ± 2.4</td>
      <td>420.7 ± 113.4</td>
      <td>14.7</td>
      <td>13.3 ± 10.4</td>
      <td>2.4 ± 1.3</td>
      <td>0.6 ± 0.3</td>
    </tr>
    <tr>
      <td>GM</td>
      <td>7109</td>
      <td>7125</td>
      <td>31</td>
      <td>89,148</td>
      <td>2.0 ± 1.3</td>
      <td>125.9 ± 26.0</td>
      <td>18</td>
      <td>6.3 ± 6.7</td>
      <td>2.8 ± 1.9</td>
      <td>3.1 ± 3.4</td>
    </tr>
    <tr>
      <td>GM</td>
      <td>2676</td>
      <td>2675</td>
      <td>47</td>
      <td>45,502</td>
      <td>1.6 ± 0.7</td>
      <td>501.7 ± 157.9</td>
      <td>5.5</td>
      <td>8.6 ± 5.1</td>
      <td>4.6 ± 3.9</td>
      <td>1.1 ± 0.3</td>
    </tr>
    <tr>
      <td>GM</td>
      <td>5985</td>
      <td>5984</td>
      <td>80</td>
      <td>104,115</td>
      <td>3.9 ± 2.1</td>
      <td>664.2 ± 323.9</td>
      <td>11.7</td>
      <td>15.8 ± 14.1</td>
      <td>17.6 ± 13.6</td>
      <td>3.4 ± 1.2</td>
    </tr>
    <tr>
      <td>LG</td>
      <td>2003</td>
      <td>2002</td>
      <td>25</td>
      <td>20,489</td>
      <td>6.8 ± 6.4</td>
      <td>399.7 ± 201.7</td>
      <td>12.6</td>
      <td>9.6 ± 6.4</td>
      <td>2.1 ± 1.2</td>
      <td>0.6 ± 0.7</td>
    </tr>
    <tr>
      <td>LG</td>
      <td>706</td>
      <td>705</td>
      <td>15</td>
      <td>10,061</td>
      <td>3.2 ± 1.9</td>
      <td>344.5 ± 127.9</td>
      <td>12.4</td>
      <td>7.3 ± 5.6</td>
      <td>3.0 ± 2.4</td>
      <td>0.4 ± 0.2</td>
    </tr>
    <tr>
      <td>LG</td>
      <td>2461</td>
      <td>2460</td>
      <td>19</td>
      <td>42,889</td>
      <td>1.8 ± 1.0</td>
      <td>372.9 ± 115.2</td>
      <td>11</td>
      <td>15.0 ± 8.6</td>
      <td>3.1 ± 1.6</td>
      <td>0.5 ± 0.2</td>
    </tr>
    <tr>
      <td>LG</td>
      <td>2310</td>
      <td>2311</td>
      <td>24</td>
      <td>48,894</td>
      <td>3.1 ± 1.5</td>
      <td>371.4 ± 139.3</td>
      <td>28.7</td>
      <td>11.8 ± 8.2</td>
      <td>3.3 ± 1.9</td>
      <td>0.6 ± 0.4</td>
    </tr>
    <tr>
      <td>LP</td>
      <td>2016</td>
      <td>2015</td>
      <td>22</td>
      <td>40,833</td>
      <td>2.7 ± 1.8</td>
      <td>402.4 ± 145.4</td>
      <td>16.4</td>
      <td>34.0 ± 17.0</td>
      <td>7.1 ± 4.8</td>
      <td>1.7 ± 1.1</td>
    </tr>
    <tr>
      <td>LP</td>
      <td>705</td>
      <td>704</td>
      <td>12</td>
      <td>17,914</td>
      <td>2.7 ± 1.6</td>
      <td>561.1 ± 119.2</td>
      <td>19</td>
      <td>11.5 ± 3.4</td>
      <td>7.0 ± 6.5</td>
      <td>2.2 ± 1.1</td>
    </tr>
    <tr>
      <td>LP</td>
      <td>500</td>
      <td>499</td>
      <td>9</td>
      <td>14,202</td>
      <td>1.4 ± 0.5</td>
      <td>567.5 ± 99.5</td>
      <td>20.6</td>
      <td>9.8 ± 5.6</td>
      <td>5.0 ± 2.9</td>
      <td>1.1 ± 0.9</td>
    </tr>
    <tr>
      <td>LP</td>
      <td>1709</td>
      <td>1708</td>
      <td>20</td>
      <td>24,335</td>
      <td>3.1 ± 2.6</td>
      <td>540.8 ± 163.5</td>
      <td>21.1</td>
      <td>8.0 ± 6.4</td>
      <td>3.9 ± 3.4</td>
      <td>1.3 ± 1.3</td>
    </tr>
    <tr>
      <td>PD</td>
      <td>425</td>
      <td>424</td>
      <td>2</td>
      <td>19,483</td>
      <td>3.4 ± 3.1</td>
      <td>414.9 ± 119.2</td>
      <td>15</td>
      <td>9.4 ± 4.6</td>
      <td>9.3 ± 6.1</td>
      <td>2.1 ± 1.9</td>
    </tr>
    <tr>
      <td>PD</td>
      <td>419</td>
      <td>418</td>
      <td>3</td>
      <td>15,113</td>
      <td>2.5 ± 1.2</td>
      <td>328.1 ± 67.2</td>
      <td>14.9</td>
      <td>4.5 ± 3.3</td>
      <td>9.3 ± 17.0</td>
      <td>2.0 ± 1.4</td>
    </tr>
    <tr>
      <td>PD</td>
      <td>1598</td>
      <td>1597</td>
      <td>15</td>
      <td>29,758</td>
      <td>2.8 ± 1.7</td>
      <td>329.8 ± 64.4</td>
      <td>54.8</td>
      <td>15.8 ± 15.7</td>
      <td>8.5 ± 16.3</td>
      <td>1.2 ± 0.7</td>
    </tr>
    <tr>
      <td>PD</td>
      <td>411</td>
      <td>410</td>
      <td>5</td>
      <td>16,710</td>
      <td>2.0 ± 1.1</td>
      <td>339.7 ± 71.0</td>
      <td>22.4</td>
      <td>20.6 ± 15.5</td>
      <td>13.1 ± 15.7</td>
      <td>1.7 ± 1.0</td>
    </tr>
  </tbody>
</table>

![Figure 2.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig2-v2.jpg)

**Figure 2.:** Total wiring lengths, soma-to-tip neurite path lengths, and Sholl intersections were calculated from three-dimensional skeletal reconstructions generated in KNOSSOS from high-resolution confocal image stacks of Lucifer yellow neuronal dye-fills. (A) Total wiring, excluding axons, was greater than 10,000 µm across all neurons (N = 16; pooled mean ± SD = 37515 ± 27498 µm). GM neurons had greater total wiring than LG, LP, and PD neurons (ANOVA; [F(3,12)=8.34, p=0.0029]; Tukey HSD). (B) Mean soma-to-tip neurite paths varied across neurons but were greater in GM neurons than the other three neuron types (ANOVA; [F(3,12)=7.14, p=0.0052]; Tukey HSD). (C) For each neuron, in order to count the number of Sholl intersections as a function of distance from the soma, we first linearized the neurite paths of the three-dimensional structure (top) relative to the soma. This can be thought of as simply stretching the neurite paths radially from the soma (bottom). The number of neurites per concentric sphere intersection (or Sholl intersections) were quantified as a function of distance from the soma. (D) Sholl intersection violin plots for each neuron. Across neurons, Sholl intersections or neurite densities (counts, normalized to maximum within each neuron, on x-axis) vary with distance from the soma (y-axis, also normalized to the range of neurite path lengths within each neuron; see Materials and methods).

We considered the complexity of these neurons’ neurite trees with two approaches: Sholl analysis and spatial density analysis. Each of these analyses provides a characterization of a neuron’s arborization patterns. Sholl analysis provides a measure of neurite density as a function of distance, from soma to terminating tips. Alternatively, spatial density analysis preserves the neuronal structure and provides a graphical depiction of neurite density.

In a somato-centric neuron where the neurite tree surrounds the soma, such as in starburst amacrine or stellate cells, Sholl analysis provides a characterization of neurite density as a function of distance from the soma. In this approach, concentric circles are overlaid on the image of a neuronal structure. Neurite density is characterized by counting the number of neurite intersections with increasing radius from the centroid, which is typically aligned with the neuronal soma (Sholl, 1953). This can be extended to three dimensions by using spheres instead of circles. Because STG neurons are unipolar rather than somato-centric, we adapted the three-dimensional Sholl analysis by linearizing the neurites and computing Sholl intersections for path length relative to the soma, rather than keeping the neurons in their innate three-dimensional conformation (Figure 2C). These data are shown in the violin plots in Figure 2D. Because somata are located at varying distances from the neuropil, the Sholl counts at each distance are normalized (described in Materials and methods). Across and within cell types, there are no apparent trends in this characterization of macroscopic branching patterns. It is interesting to note, however, that some distributions are multi-modal, suggesting that there is more branching at certain distances from the soma, within each neuron. For example, the fourth, right-most LG neuron (blue), has at least three distinct peaks in its distribution. In contrast, the first, left-most LG neuron appears to have primarily one broad peak in its distribution (Figure 2D).

Spatial density plots (Figure 3) illustrate neurite density. The skeletal reconstruction of each neuron is composed of points in the x, y, and z dimensions. For each neuron, the probability distribution function of these points was determined with Gaussian kernel density estimation. The color map represents these probabilities (between 0 and 1), which are scaled within each neuron. Based on these graphical representations, there appears to be no obvious patterning in neurite arborizations within each neuron type. Although GM neurons appear to have distinct regions of high neurite density, PD neurons are more uniformly distributed about the neuropil.

![Figure 3.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig3-v2.jpg)

**Figure 3.:** Spatial density profiles were generated using Gaussian kernel density estimation in the x and y dimensions. This calculation generated a probability distribution function for the points composing each skeletal reconstruction. The black-red-white color map is scaled within each neuron (see Materials and methods) and represents relative neurite density.White values indicate areas of high neurite density and black values indicate areas of low neurite density. White scale bars = 100 µm; black circles indicate somata locations. Each plot is oriented such that the stn is projecting upward and the dvn is projecting downward (as indicated).

#### Branching patterns

Cable theory suggests that the extent of branching across the neurite tree influences voltage signal propagation and, ultimately, a neuron’s input-output function (Rall, 1959; Rall and Rinzel, 1973; Rinzel and Rall, 1974). Neurite arborizations and sub-trees can also reflect the connectivity of the circuit and locations of pre-synaptic inputs. GM neurons had greater branch point numbers than the other three cell types (ANOVA, [F(3,12)=7.12, p=0.0053]; Tukey HSD; Figure 4A; Table 1).

![Figure 4.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig4-v2.jpg)

**Figure 4.:** Branch points numbers and angles were extracted from three-dimensional skeletal reconstructions generated in KNOSSOS from high-resolution confocal image stacks of Lucifer yellow neuronal dye-fills. (A) Branch point numbers were highly variable across neuron types and GM neurons presented higher branch point numbers than other cell types (letters are indicative of ANOVA results; [F(3,12)=7.12, p = 0.0053]; Tukey HSD). (B) Angles were calculated at bifurcating branch points as the angle (purple) between a given daughter branch (D1 or D2) and the hypothetical continuation of the parent (P) branch (dashed line). (C) Branch angle histograms show a wide range of branch point geometries within single neurons. Sets of four concentric histograms show the branch angle distributions of four neurons of a given neuron type (indicated by color in key on right). Solid lines indicate means, dashed lines indicate medians. Shaded ranges of histograms are indicative of the 25–75% confidence interval. There were no measurable statistical differences across individual neurons or neuron types).

Previous work in Purkinje (Wen and Chklovskii, 2008) and cortical neurons (Bielza et al., 2014), for example, has suggested neuritic arbors presenting branch angles of <90° minimize wiring cost, given the neuron’s circuit-level connectivity (Cherniak, 1992; Wen and Chklovskii, 2008). Branch angles were calculated across all branch points in each of the 16 neurons (Figure 4B). Branch angle distributions were similar across cell types and individual neurons (Figure 4C). The majority of branch angles fell between and 0 and 100 degrees. Mean GM branch angles were 70.7 ± 1.7 (median: 71.4 degrees). Similarly, LG branch angles averaged 70.6 ± 1.5 (median: 70.7 degrees), LP branch angles averaged 68.6 ± 0.6 (median: 68.8 degrees) and PD branch angles had an average value of 70.3 ± 0.8 (median: 70.0 degrees).

Previous studies characterizing neurite arborization in other neuron types, focused predominantly on bifurcating branch points (Wen and Chklovskii, 2008; van Pelt and Uylings, 2011; Kim et al., 2012). However, as is made evident by the presence of hand-like structures, branch points appear more complex in STG neurons. Across all neurons, we also quantified the frequency of bi-, tri-, and multi-furcating branch points (Figure 5A–C). Figure 5B shows scatter plots for each of the 16 neurons. To avoid visual bias against neurons with fewer total branch points, neurons of the same type were grouped and the proportions of bi-, tri-, and multi-furcations (quantified as the number of daughter neurites/branch point) were calculated. Bifurcations (daughter neurites/branch point = 2) were the most common across all neurons. Higher order multi-furcations were also present in each of the neurons examined here. GM neurons displayed more multi-furcations (with >4 daughter neurites) relative to other neuron types. That said, the differences in the proportions of bi-, tri-, and multi-furcations across cell types are quite small (Figure 5C).

![Figure 5.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig5-v2.jpg)

**Figure 5.:** Branch point types were detected in three-dimensional skeletal reconstructions generated in KNOSSOS from high-resolution confocal image stacks of Lucifer yellow neuronal dye-fills. (A) Examples of branch point types (right) are indicated as corresponding boxes (color-coded) in a single neuronal dye-fill (left). (B) Scatter plots show the number of daughter branches per branch point (or branch point type, where 2 = bifurcation, 3 = trifurcation, and >4 indicates a multi-furcation) for every branch point in the skeletal structure of an individual neuron (n = 4 for each neuron type, indicated on x-axis). (C) Stacked bars summarize the percentage of branch points that are bifurcations (# daughter branches = 2), trifurcations (# daughter branches = 3), and multi-furcations (# daughter branches ≥ 3), as indicated by gray-shaded key (right). The landscape of branch point types was relatively similar across cell types, wherein multi-furcations accounted for ~10% or less of the branch points within each neuron. Nonetheless, unconventional tri- and multi-furcating branch points were observed in all neurons characterized in this study. Neuron types (n = 4 of each) are color-coded throughout figure: gold = GM neuron, blue = LG neuron, green = LP neuron, red = PD neuron.

The symmetry of neurite lengths following bifurcating branch points may speak to whether neurite growth occurs in a proportional manner during development. We calculated the symmetry index (SI) across all bifurcating branch points in each neuron (N = 16), which is defined as the ratio of the sums of downstream neurite lengths on either side of the bifurcation (shorter neurite length as the numerator, longer as the denominator; Van Pelt et al., 1992; de Sousa et al., 2015). Therefore, SI = 1 indicates symmetric and SI <1 indicates asymmetric neurite lengths on either side of a given bifurcation (Figure 6A; an example neurite path is shown in Figure 6B). For GM, LG, LP, and PD neurons, SI values (mean ± SD) were 0.48 ± 0.11 (median: 0.51) 0.44 ± 0.11 (median: 0.42), 0.55 ± 0.05 (median: 0.55) and 0.66 ± 0.03 (median: 0.66), respectively (Figure 6C). Figure 6C shows the full distributions of SI values for each neuron. Qualitatively, the SI distributions in PD neurons appear to be positively shifted relative to the other three cell types. Analysis of mean SI values across cell types (Figure 6D) reveal that PD neurons present more symmetrical neurite arborizations relative to other cell types (ANOVA; F(3,12) = 5.45, p=0.01; Tukey HSD).

![Figure 6.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig6-v2.jpg)

**Figure 6.:** Symmetry indices (SI) were calculated for every branch point detected in the three-dimensional skeletal reconstructions generated in KNOSSOS from high-resolution confocal image stacks of Lucifer yellow neuronal dye-fills. For a given branch point, the SI was calculated as the ratio of the sums of downstream neurite lengths on either side of the bifurcation (shorter neurite length as the numerator, longer as the denominator). (A) Schematics of branch points with varying SI; SI decreases as neurite lengths on either side of the first branch point become increasingly asymmetrical in length (from left to right). (B) Traced neurite path (red) and its corresponding SI of 0.12, which is akin to the rightmost example in A. (C) Vertical histograms show the distributions of SI values across all branches for each neuron (cell type is indicated by color and labeled on the x-axis). The x-axis scales are normalized to the maximum count within each neuron. All neurons present SI values that span the range of possibilities, between 0 and 1. (D) Mean SI values plotted by cell type. Scatter points indicate mean SI values for individual cells, black line indicates mean SI for each cell type. Letters are indicative of ANOVA results across cell types (F(3,12) = 5.45, p=0.01; Tukey HSD). Neuron types (n = 4 of each) are color-coded in C and D: gold = GM neuron, blue = LG neuron, green = LP neuron, red = PD neuron.

#### Subtrees

We quantified the number of putative subtrees in each neuron. We intuitively defined a subtree as any collection of branches projecting from the same secondary branch; thus, the number of subtrees will be equal to the number of secondary branches emerging from the main, primary neurite. Across all neurons, the number of subtrees varied between 2 and 80 (Figure 7A; Table 1). GM neurons displayed more subtrees (47 ± 23) than LP (18 ± 6) and PD (6 ± 6) neurons. However, there were no other significant distinctions between the other neuron types (Figure 7A; ANOVA, [F(3,12)=7.6, p=0.0041], Tukey HSD). As is clear from this scatter plot, subtree numbers are quite variable within each neuron type.

![Figure 7.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig7-v2.jpg)

**Figure 7.:** Subtrees were defined as neurites sharing a common secondary neurite exiting the main path, or primary neurite, of the neuronal structure. Thus, for each neuron, the number of subtrees was equivalent to the number of secondary neurites in the neurons corresponding to the three-dimensional skeletal reconstruction generated in KNOSSOS. (A) The number of subtrees varied within and across neuron types, such that GM neurons presented more subtrees than LP and PD neurons (letters are indicative of ANOVA results; [F(3,12)=7.6, p=0.0041], Tukey HSD). (B) The neuritic field for a given subtree (example on left) was approximated as an elliptical volume fit (blue shaded area) and centered about the center of mass (dark blue point) of the subtree’s tip coordinates (light blue points; middle). A subtree’s neuritic field was visualized by projecting this elliptical volume into the x-y plane (right), which is representative of a birds-eye view of neuropil space. (﻿C–F) Subtree neuritic field plots for four representative STG neurons (left), juxtaposed to representative scrambled iterations (right). Three-dimensional scatter plots show the subtree root coordinates of individual subtrees (circular data points) and their corresponding neuritic fields projected onto the x-y plane. Left: plots display the subtree neuritic fields given the actual neuronal structure. Right: plots display the subtree neuritic fields for a representative scrambled iteration of tip coordinates for the same neuron on left, wherein tips were re-distributed into the same number of, but different subtrees, while maintaining the same root coordinates (see Materials and methods). For each neuron in C–F scale axes indicate the same x-y-z scale for both the actual and scrambled plots. (G) Scatter plots indicate the number of overlapping subtrees for each neuron (cell type indicated by color and labeled on the x-axis). Overlaid vertical histograms show the number of overlapping subtrees across the scrambled, synthetic population generated from the tip coordinates for each neuron (purple lines indicate the mean radii for each scrambled population). (H) Scatter plots indicate the mean subtree neuritic field radius for each neuron (cell type indicated by color and labeled on the x-axis). Overlaid vertical histograms show the range of subtree neuritic field radii across the scrambled, synthetic population generated from the tip coordinates for each neuron (purple lines indicate the mean radii for each scrambled population). Neuron types (n = 4 of each) are color-coded in A, G, and H: gold = GM neuron, blue = LG neuron, green = LP neuron, red = PD neuron.

We considered the neuritic field of each neuron’s subtrees to determine if they show any spatial specificity or tiling in the neuropil (Figure 7B). Using the three-dimensional coordinates of each subtree’s terminal tips, we calculated each subtree’s center of mass (consistent with analyses in Wilensky et al., 2003), and approximated each subtree’s neuritic field by fitting an elliptical volume to the tip coordinates and centering this ellipse to the subtree’s center of mass (Figure 7B, middle). This can be visualized when projected into the x-y plane, which represents a birds-eye view of each subtree’s elliptical neuritic field (Figure 7B, right). Figure 7C–F shows the root coordinates for all the subtrees of one neuron and their corresponding neuritic fields in the x-y plane (left axes). In the four examples shown, the actual subtree neuritic fields appear to be compact and confined to particular areas in the x-y plane, or tiles in neuropil space.

We completed a bootstrap analysis to test if such neuropil tiling would arise from a random distribution of subtree tip coordinates. In this approach, we scrambled the observed tip coordinates and reassigned them to any subtree, while maintaining the same number of tips per subtree as observed in the actual neuronal structure. Figure 7C–F (right axes) shows an example of one scrambled tip iteration of each of the four example neurons. In each of the scrambled iterations, there is a notable increase in overlap between subtree neuritic fields and neuritic field radius, relative to the actual subtree distributions.

We generated 2000 scrambled iterations for each of the 16 neurons. To compare within and across neuron types, we measured two metrics that characterize the degree of overlap between subtree neuritic fields. First, we simply counted the number of overlapping subtree neuritic fields across the 16 neurons (scatter plot points) and in their corresponding scrambled-tip populations (Figure 7G). For comparison, histograms showing the distributions of subtree neuritic field radii across the scrambled-tip populations are overlaid on these same axes. In 13/16 neurons, the subtree neuritic fields of the actual neurons show less overlap in space than the scrambled-tip populations.

Figure 7H shows the mean subtree neuritic field radii for each neuron (scatter plot points) relative to those of the scrambled-tip populations (histograms). Across all neurons, the mean subtree neuritic field radii observed in the actual neuronal subtree arrangements are smaller than those of the scrambled-tip population (bootstrap analyses yielded p-values <0.01 within each neuron). Thus, the actual subtree neuritic fields are more compact relative to those generated by random tip distributions. Taken together, this analysis suggests that STG neuronal subtrees may be organized to span the neuropil in a manner that minimizes overlap between subtrees and their neuritic fields. This arrangement is unlikely to arise from random distribution of terminal tips.

### II. Fine structure

A neuron’s fine geometrical properties: its neurites’ lengths, tortuosities, diameters, and branching patterns, are a reflection of the distributed cable properties influencing current flow and propagation of voltage signals throughout each neuron’s neurite tree (Rall, 1977). We found these metrics to be quite variable within and across neuron types, showing no obvious cell-type-specific rules in terms of neurite growth.

#### Neurite lengths

Across all 16 neurons examined, soma-to-tip neurite lengths ranged between 5 and 1778 µm, with the majority of branches ranging between 200 and 800 µm. Distributions of neurite lengths across all 16 neurons and the four cell types are shown in Figure 8A. There are no evident cell-type-specific trends in soma-to-tip neurite length distributions (ANOVA; [F(3,12)=1.48, p=0.2698]; Tukey HSD).

![Figure 8.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig8-v2.jpg)

**Figure 8.:** (A) Histograms for each neuron showing the distribution of neurite lengths across all soma-to-tip paths. Neurite path lengths were measured in three-dimensional skeletal reconstructions generated in KNOSSOS from high-resolution confocal image stacks of Lucifer yellow neuronal dye-fills. There were no cell-type-specific differences in neurite length distributions (ANOVA; [F(3,12)=1.48, p=0.2698]; Tukey HSD). Means are indicated by solid lines; medians are indicated with dashed lines; darker shaded regions indicate 25–75% confidence intervals. Neurite diameters were randomly sampled across primary (1°), secondary (2°), tertiary (3°), and terminating (tip) neurites and manually measured using ImageJ. (B) Illustration of 1° branch (red) and individual 2° (cyan) and 3° (white) branches on one neuron (z-projection of confocal micrograph at 60x magnification, neuron pseudo-colored in yellow). (C) Scatter plots of neurite diameters as a function of neurite order within neuron types show decreasing neurite diameters as a function of neurite order. ANOVA results are: [F(3,149)=14.77, p<<0.001; Tukey HSD)], [F(3,152)=67.16, p<<0.001; Tukey HSD)], [F(3,152)=33.92, p<<0.001; Tukey HSD)], [F(3,146)=16.43, p<<0.001; Tukey HSD)], for GM, LG, LP, and PD, respectively. (D) Scatter plot shows all measured diameters, across all cell types, as a function of neurite order. When all cell types are pooled are together, diameter decreases as a function of neurite order (ANOVA [F(3,611)=89.17, p<<0.001]; Tukey HSD; indicated with letters). ANOVA analyses within each neurite order, across cell types, revealed no significant differences across cell types. For C and D pooled mean ± SD within each neurite order indicated with black lines. In A, C, and D neuron types (n = 4 of each) are color-coded as in key.

#### Neurite diameters

We manually measured neurite diameters of primary (1°), secondary (2°), tertiary (3°), and terminating neurites (tips; schematized in Figure 8B). The 1° neurite refers to the neurite path extending from the soma, which is often the widest in diameter. 2° and 3° neurites branch sequentially from the 1° neurite. Grouping all neuron types together: 1°, 2°, 3°, and tips have diameters that decreased with each class, such that the mean 1° diameter across all neurons was 18.7 ± 11.1 µm, and the mean tip diameter across all neurons was 1.5 ± 1.5 µm (mean ± SD), respectively (Figure 8C). However, it should be noted that diameters varied within each neurite class: 1° neurites presented diameters with a CV = 0.6; 2° diameters varied with CV = 0.9; 3° diameters varied with CV = 1.4; and tip diameters varied with CV = 1.0. These same relationships can be observed within each neuron type (Figure 8D).

#### Rall power at branch points

We examined the parent-daughter neurite radius ratios at four branch point classes: initial (first branch point relative to the soma), primary-secondary (P-S), secondary-tertiary (S-T), and terminal (at least one daughter branch is a terminating tip) bifurcating branch points (Figure 9A). We quantified these parent-daughter ratios in terms of their Rall Power (X), which is defined as the exponent X required for ∑​radiusdaughtersX=radiusparentX (Rall, 1959). X = 3/2 is the optimal geometrical relationship between parent and daughter neurites for continuity of current (Rall, 1959).

![Figure 9.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig9-v2.jpg)

**Figure 9.:** Rall powers calculated for branch points sampled across different branch orders: initial branch points (or the first branch point relative to the soma), primary-secondary (P–S) branch points, secondary-tertiary (S–T) branch points, and branch points in which at least one daughter branch was a terminating branch (terminal). Parent and daughter neurite diameters were manually measured using ImageJ, directly from the high-resolution confocal image stacks of Lucifer yellow neuronal dye-fills. (A) Examples of initial (red), P-S (blue), and S-T (cyan) branch points are shown on a maximum projection of a neuronal dye-fill. (B–E) Scatter plots show the calculated Rall powers for each neuron (as in Materials and methods and text; N = 16; cell types indicated by color and labeled on x-axis; colored horizontal bars indicate the mean Rall power for each cell) across sampled initial, P-S, S-T, and terminal branch points, respectively (n = 18–20 branch points within each branch point type). The optimal Rall power for current transfer is 3/2 (Rall, 1959). This is indicated on each plot with purple horizontal lines. Mean Rall powers calculated within each cell type are shown in Table 2. There were no statistically significant cell-type-specific differences in this metric.

When X > 3/2, a given daughter neurite has a shorter radius than optimal. When X < 3/2, a given daughter neurite has a longer radius than optimal. These data are presented in Figure 9B–E and summarized in Table 2.

**Table 2.**
 Rall powers by cell type. Rall powers were derived from neurite diameters at different branch point categories. Initial-Secondary refers to the Rall power at the first branch point relative to the soma. Terminating tips refers to branch points wherein at least one daughter branch terminates. Pooled means ± standard deviations are shown for each branch point category, for each cell type. For each cell type, pooled means ± standard deviations were calculated from six branch points in each category, for each of four neurons of that cell type. The raw data and mean Rall powers for each neuron are plotted in Figure 9.


<table>
  <thead>
    <tr>
      <th>Branch point category</th>
      <th colspan="4">Rall power by cell type</th>
    </tr>
    <tr>
      <th>Parent-Daughter</th>
      <th>GM</th>
      <th>LG</th>
      <th>LP</th>
      <th>PD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>INITIAL-SECONDARY</td>
      <td>0.001 ± 0.001</td>
      <td>0.001 ± 0.001</td>
      <td>0.001 ± 0.001</td>
      <td>0.381 ± 0.658</td>
    </tr>
    <tr>
      <td>PRIMARY-SECONDARY</td>
      <td>2.132 ± 2.070</td>
      <td>1.667 ± 0.857</td>
      <td>4.296 ± 5.331</td>
      <td>2.215 ± 1.838</td>
    </tr>
    <tr>
      <td>SECONDARY-TERTIARY</td>
      <td>1.305 ± 0.682</td>
      <td>6.366 ± 10.098</td>
      <td>1.332 ± 0.575</td>
      <td>1.342 ± 0.453</td>
    </tr>
    <tr>
      <td>TERMINATING TIPS</td>
      <td>1.846 ± 1.449</td>
      <td>6.847 ± 10.737</td>
      <td>7.397 ± 10.820</td>
      <td>1.049 ±. 546</td>
    </tr>
  </tbody>
</table>

The calculated Rall powers across individual neurons, cell types, and branch point classes are quite variable and deviate from the optimal 3/2 power. Mean initial Rall powers were uniformly less than 3/2, across cell types, suggesting that the secondary branches projecting from the primary neurite tend to have large diameters relative to the primary neurite at the branch point junction. In contrast, P-S, S-T, and terminal branch points presented Rall powers that varied within and across cell types. Taken together, it does not appear that branch points present optimal parent-daughter radius ratios for current transfer, as predicted by Rall.

### III. Application of wiring optimization principles

A good deal of earlier work outlines a series of metrics that speak to putative optimization principles governing neuronal morphology in developing and adult animals (Cherniak, 1992; Chen et al., 2006; Chklovskii et al., 2002; Chklovskii, 2000, 2004; Wen and Chklovskii, 2008; Kim et al., 2012; Rivera-Alba et al., 2014; Cuntz et al., 2007, 2010, 2012, 2013). Most of these wiring rules stem from Ramón y Cajal’s anatomical principles of nerve cell organization, wherein he speculated that neuronal structures are optimized to conserve wiring material and conduction velocity (Cajal, 1995; Cuntz et al., 2010). In the following analyses, we have taken two approaches to quantify wiring efficiency in STG neurons.

#### Tortuosity

The neuronal dye-fills in Figure 1 illustrate the circuitous, winding nature of the neurites in each of these STG neurons. In each neuron, we compared the lengths of all soma-to-tip neurite paths to their minimal Euclidean distances. We measured this in terms of tortuosity (Wen and Chklovskii, 2008), which is defined as the actual neurite path length divided by the Euclidean distance (Figure 10A). A tortuosity of 1 is indicative of an efficient, minimal path length. A tortuosity greater than one is suggestive of a less efficient, winding path from soma to tip. Across all cell types, tortuosity distributions across all soma-to-tip neurite paths spanned beyond values of 3 (Figure 10B). Pooled mean tortuosities within each cell type were uniformly greater than 1, and were: 3.8 (median: 2.6), 4.7 (median: 2.9), 3.2 (median: 2.3), and 2.7 (median: 2.2) for GM, LG, LP, and PD, respectively (Table 1). Thus, by this metric, STG neurite paths are measurably longer than the optimal Euclidean length, given their terminal destinations. Analysis across cell types revealed no significant differences in mean tortuosities (ANOVA; [F(3,12): 1.2, p=0.3509]; Tukey HSD).

![Figure 10.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig10-v2.jpg)

**Figure 10.:** Tortuosities were calculated for every soma-to-tip neurite path detected from the three-dimensional skeletal reconstruction of each neuron (N = 16). (A) An example neurite path (red dashed line) from soma to terminal tip is shown on maximum projection image of an STG neuron section. The tortuosity of such a path is calculated as the ratio of the actual path length (red) over the Euclidean distance from soma to tip (purple). If the actual neurite path follows the most efficient Euclidean path, it will have a tortuosity of 1. If the neurite path deviates from this minimal path, its tortuosity will be >1. (B) Histograms of tortuosities for all neurite paths within each neuron (gold = GM neuron, blue = LG neuron, green = LP neuron, red = PD neuron). Darker shaded regions indicate 25–75% confidence intervals. In all cases, the distributions spanning tortuosities between 1 and 6 are shown (x-axis). In some cases, the distributions extend beyond values of 6 (not shown in this figure).

#### Wiring cost

The tortuous neurites of STG neurons suggest that they may not adhere to widely accepted wiring optimization principles proposed in previous work on cortical and fly visual neurons (Wen and Chklovskii, 2008; Cuntz et al., 2010, 2012). To investigate this possibility, we compared the anatomical features of these 16 STG neurons to those of synthetic, minimal spanning trees constrained by a simple wiring cost equation (as in Cuntz et al., 2010), using the TREES toolbox available at treestoolbox.org).

For each STG neuron, we generated corresponding minimal spanning trees (MSTs) that connect a root node to target nodes in three-dimensional space. Given the arbitrary nature of soma position in the STG (Figure 1C), the root node for a given MST was defined as the coordinates of the first branch point relative to the soma in the actual neuronal structure. The target nodes were randomly generated from points uniformly distributed in the three-dimensional elliptical volume approximating the space occupied by the actual neurons (Figure 11A). Construction of a MST connecting these nodes was constrained by a simple wiring cost equation: total cost = wiring cost + bf · path length cost. The only variable parameter in this model is the balancing factor, bf, which weighs: (1) a wiring cost associated with the Euclidean distance between nodes and (2) a path length cost associated with the minimal root-to-tip neurite lengths (Cuntz et al., 2010 describes this cost function in great detail).

![Figure 11.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig11-v2.jpg)

**Figure 11.:** Synthetic MSTs adhering to the wiring cost rule: total cost = wiring cost + bf * path length cost (where bf = balancing factor) were generated using the TREEs toolbox (described in Materials and methods and by Cuntz et al., 2010). (A) An example of four synthetic minimal spanning trees (right) with varying bf values generated from the first branch point (location indicated as red circle on actual skeleton of an LP neuron; left) as the root. The carrier points (blue) were randomly generated from points uniformly distributed across the elliptical volume approximating the actual volume occupied by the neuron. The number of carrier points was tuned such that the MSTs had branch point number within 20% of the actual neuron’s branch point number (Table 3). Scale bars apply to skeleton, carrier point, and MST plots. (B) Morphological features of synthetic trees generated with bf values between 0.1 and 0.6 plotted against measurements from four actual STG neurons (one of each type, indicated on left and by color). Features of actual neurons are shown with black lines, whereas synthetic neurite tree data are plotted in the color scale described in the key for each neuron. Total wiring lengths, branch order distributions, neurite length distributions, and tortuosity distributions were calculated excluding axons for all synthetic and actual neurite trees. Branch order, neurite length, and tortuosity distributions were normalized to the maximum within each data set (for each bf value and actual neurite tree) for direct comparison of distributions despite varying neurite path counts.

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig11-figsupp1-v2.jpg)

**Figure 11—figure supplement 1.:** MSTs were generated using the TREEs toolbox (described in Materials and methods and by Cuntz et al., 2010) and adhered to the wiring cost rule: total cost = wiring cost + bf * path length cost (where bf = balancing factor). For each of four GM neurons, MSTs with bf values between 0 and 0.6 were generated from the first branch point as the root. The terminal tip coordinates were randomly generated from points uniformly distributed across the elliptical volume approximating the actual volume occupied by the neuron (as in Figure 11A). The number of terminal tip coordinates was tuned for each neuron, such that the MSTs had branch point numbers within 20% of the actual neuron’s branch point number. A–D present plots comparing morphological features (total wiring, branch point (pts), neurite lengths, branch orders, and tortuosities) of the MSTs to those measured in each of four actual STG neurons. In scatter plots (left), thick lines are indicative of the total wiring or branch point number of the actual neuron, whereas colored points correspond with these metrics for the MSTs of the bf value (indicated in key). Thin black lines indicate 20% above or below the actual neuron’s total wiring or branch point number. For histograms (right), measurements from actual neurons are shown with black lines, whereas synthetic MST data are plotted in the color scale described in the key. Branch order, neurite length, and tortuosity distributions were normalized to the maximum within each data set (for each bf value and actual neurite tree) for direct comparison of distributions despite varying neurite path counts. It is evident that not one bf value capitulates all features of the actual GM neurons.

![Figure 11—figure supplement 2.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig11-figsupp2-v2.jpg)

**Figure 11—figure supplement 2.:** MSTs were generated using the TREEs toolbox (described in Materials and methods and by Cuntz et al., 2010) and adhered to the wiring cost rule: total cost = wiring cost + bf * path length cost (where bf = balancing factor). For each of four LG neurons, MSTs with bf values between 0 and 0.6 were generated from the first branch point as the root. The terminal tip coordinates were randomly generated from points uniformly distributed across the elliptical volume approximating the actual volume occupied by the neuron (as in Figure 11A). The number of terminal tip coordinates was tuned for each neuron, such that the MSTs had branch point numbers within 20% of the actual neuron’s branch point number. A–D present plots comparing morphological features (total wiring, branch point (pts), neurite lengths, branch orders, and tortuosities) of the MSTs to those measured in each of four actual STG neurons. In scatter plots (left), thick lines are indicative of the total wiring or branch point number of the actual neuron, whereas colored points correspond with these metrics for the MSTs of the bf value (indicated in key). Thin black lines indicate 20% above or below the actual neuron’s total wiring or branch point number. For histograms (right), measurements from actual neurons are shown with black lines, whereas synthetic MST data are plotted in the color scale described in the key. Branch order, neurite length, and tortuosity distributions were normalized to the maximum within each data set (for each bf value and actual neurite tree) for direct comparison of distributions despite varying neurite path counts. It is evident that not one bf value capitulates all features of the actual LG neurons.

![Figure 11—figure supplement 3.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig11-figsupp3-v2.jpg)

**Figure 11—figure supplement 3.:** MSTs were generated using the TREEs toolbox (described in Materials and methods and by Cuntz et al., 2010) and adhered to the wiring cost rule: total cost = wiring cost + bf * path length cost (where bf = balancing factor). For each of four LP neurons, MSTs with bf values between 0 and 0.6 were generated from the first branch point as the root. The terminal tip coordinates were randomly generated from points uniformly distributed across the elliptical volume approximating the actual volume occupied by the neuron (as in Figure 11A). The number of terminal tip coordinates was tuned for each neuron, such that the MSTs had branch point numbers within 20% of the actual neuron’s branch point number. A–D present plots comparing morphological features (total wiring, branch point (pts), neurite lengths, branch orders, and tortuosities) of the MSTs to those measured in each of four actual STG neurons. In scatter plots (left), thick lines are indicative of the total wiring or branch point number of the actual neuron, whereas colored points correspond with these metrics for the MSTs of the bf value (indicated in key). Thin black lines indicate 20% above or below the actual neuron’s total wiring or branch point number. For histograms (right), measurements from actual neurons are shown with black lines, whereas synthetic MST data are plotted in the color scale described in the key. Branch order, neurite length, and tortuosity distributions were normalized to the maximum within each data set (for each bf value and actual neurite tree) for direct comparison of distributions despite varying neurite path counts. It is evident that not one bf value capitulates all features of the actual LP neurons.

![Figure 11—figure supplement 4.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig11-figsupp4-v2.jpg)

**Figure 11—figure supplement 4.:** MSTs were generated using the TREEs toolbox (described in Materials and methods and by Cuntz et al., 2010) and adhered to the wiring cost rule: total cost = wiring cost + bf * path length cost (where bf = balancing factor). For each of four PD neurons, MSTs with bf values between 0 and 0.6 were generated from the first branch point as the root. The terminal tip coordinates were randomly generated from points uniformly distributed across the elliptical volume approximating the actual volume occupied by the neuron (as in Figure 11A). The number of terminal tip coordinates was tuned for each neuron, such that the MSTs had branch point numbers within 20% of the actual neuron’s branch point number. A–D present plots comparing morphological features (total wiring, branch point (pts), neurite lengths, branch orders, and tortuosities) of the MSTs to those measured in each of four actual STG neurons. In scatter plots (left), thick lines are indicative of the total wiring or branch point number of the actual neuron, whereas colored points correspond with these metrics for the MSTs of the bf value (indicated in key). Thin black lines indicate 20% above or below the actual neuron’s total wiring or branch point number. For histograms (right), measurements from actual neurons are shown with black lines, whereas synthetic MST data are plotted in the color scale described in the key. Branch order, neurite length, and tortuosity distributions were normalized to the maximum within each data set (for each bf value and actual neurite tree) for direct comparison of distributions despite varying neurite path counts. It is evident that not one bf value capitulates all features of the actual PD neurons.

Figure 11A shows examples of MSTs (right) generated from the root and tip coordinates of an LP neuron (left). Lower bf values result in MSTs with minimal total cable length at the expense of longer root-to-tip path lengths. Low-bf structures are consistent with relatively electrotonically compact neurons (Cuntz et al., 2010). Greater bf values result in lower root-to-tip path lengths at the expense of greater total cable length. High-bf structures are consistent with electrotonically compartmentalized neurons (Cuntz et al., 2010). It is qualitatively evident that the MSTs are not exact representations of the actual LP neuronal structure. However, if the synthetic MSTs recapitulate structural features of the actual STG, this would suggest that wiring cost is an important constraint in STG neuronal morphology. Furthermore, should a given bf value generate neurite trees consistent with the actual neurite trees, the bf value will be suggestive of the actual neuron’s electrotonic structure.

Bf values between 0.1 and 0.85 have been used to generate realistic neuronal structures (Cuntz et al., 2008, 2010, 2012). We generated minimal spanning neurite trees with bf values between 0.1 and 0.6 for each of the 16 STG neurons (simulation parameters shown in Table 3). We then compared a number of structural features across the synthetic MSTs and actual neuronal structures. These measures include neurite lengths, tortuosities, and total wiring as described previously. We also considered branch order distributions, which provide a quantitative characterization of neuritic arborizations (Figure 11B, Figure 11—figure supplements 1–4). In brief, branch order is a property of each branch point in the neuronal structure. It is equivalent to the number of branch points between the first branch point (relative to the soma, which has a branch order of 0), and a given branch point. The branch order distributions of many of the actual STG neurons (Figure 11B, in black) are skewed right, with branch orders of 100 or greater, suggesting that neurite paths may branch more than 100 times before terminating. In this way, the branch order distributions reflect the complex and highly branched nature STG neurons.

**Table 3.**
 Minimal spanning trees (MSTs) simulation parameters. 16 STG neuronal structures were simulated using MST analyses from the TREES toolbox (Cuntz et al., 2010). Carrier point numbers (column 4) were tuned to generate MSTs with branch point numbers within 20% of the branch point counts in the actual neurons (column 2, gray shaded). MSTs were generated for balancing factors between 0 and 0.6, at increments of 0.1. Columns 5–18 show branch point numbers and cable lengths for each of these MSTs. The MSTs often had cable lengths within 20% of that measured in the actual neurons (column 3), but in some cases, the MSTs were not a close approximation of the actual cable length.


<table>
  <thead>
    <tr>
      <th rowspan="3">Cell</th>
      <th colspan="2">Actual neuron</th>
      <th colspan="15">Minimum spanning trees</th>
    </tr>
    <tr>
      <th rowspan="2">Branch Points</th>
      <th rowspan="2">Cable length(x 104 µm)</th>
      <th rowspan="2">Carrier Points</th>
      <th colspan="7">Branch point numbers</th>
      <th colspan="7">Cable length (x 104 µm)</th>
    </tr>
    <tr>
      <th>0</th>
      <th>0.1</th>
      <th>0.2</th>
      <th>0.3</th>
      <th>0.4</th>
      <th>0.5</th>
      <th>0.6</th>
      <th>0</th>
      <th>0.1</th>
      <th>0.2</th>
      <th>0.3</th>
      <th>0.4</th>
      <th>0.5</th>
      <th>0.6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GM1</td>
      <td>2671</td>
      <td>6.1</td>
      <td>8500</td>
      <td>2416</td>
      <td>2477</td>
      <td>2512</td>
      <td>2576</td>
      <td>2727</td>
      <td>2916</td>
      <td>2971</td>
      <td>16.8</td>
      <td>17.2</td>
      <td>17.7</td>
      <td>18.2</td>
      <td>19.0</td>
      <td>19.9</td>
      <td>20.7</td>
    </tr>
    <tr>
      <td>GM2</td>
      <td>7125</td>
      <td>8.9</td>
      <td>23000</td>
      <td>6296</td>
      <td>6789</td>
      <td>7030</td>
      <td>7271</td>
      <td>7592</td>
      <td>7773</td>
      <td>7994</td>
      <td>2.5</td>
      <td>2.6</td>
      <td>2.7</td>
      <td>2.8</td>
      <td>2.9</td>
      <td>3.1</td>
      <td>3.3</td>
    </tr>
    <tr>
      <td>GM3</td>
      <td>2675</td>
      <td>4.6</td>
      <td>8800</td>
      <td>2384</td>
      <td>2537</td>
      <td>2665</td>
      <td>2749</td>
      <td>2827</td>
      <td>2959</td>
      <td>3026</td>
      <td>5.5</td>
      <td>5.7</td>
      <td>5.9</td>
      <td>6.1</td>
      <td>6.4</td>
      <td>6.8</td>
      <td>7.3</td>
    </tr>
    <tr>
      <td>GM4</td>
      <td>5984</td>
      <td>10.4</td>
      <td>19000</td>
      <td>5274</td>
      <td>5574</td>
      <td>5762</td>
      <td>5969</td>
      <td>6187</td>
      <td>6379</td>
      <td>6571</td>
      <td>14.3</td>
      <td>14.7</td>
      <td>15.2</td>
      <td>15.8</td>
      <td>16.6</td>
      <td>17.5</td>
      <td>18.8</td>
    </tr>
    <tr>
      <td>LG1</td>
      <td>2002</td>
      <td>2.0</td>
      <td>6500</td>
      <td>1746</td>
      <td>1860</td>
      <td>1976</td>
      <td>2092</td>
      <td>2154</td>
      <td>2209</td>
      <td>2302</td>
      <td>1.7</td>
      <td>1.8</td>
      <td>1.9</td>
      <td>1.9</td>
      <td>2.0</td>
      <td>2.1</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td>LG2</td>
      <td>705</td>
      <td>1.0</td>
      <td>2300</td>
      <td>641</td>
      <td>672</td>
      <td>696</td>
      <td>710</td>
      <td>750</td>
      <td>768</td>
      <td>815</td>
      <td>1.5</td>
      <td>1.5</td>
      <td>1.6</td>
      <td>1.7</td>
      <td>1.7</td>
      <td>1.8</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>LG3</td>
      <td>2460</td>
      <td>4.3</td>
      <td>8000</td>
      <td>2168</td>
      <td>2302</td>
      <td>2389</td>
      <td>2498</td>
      <td>2559</td>
      <td>2612</td>
      <td>2707</td>
      <td>4.3</td>
      <td>4.4</td>
      <td>4.6</td>
      <td>4.8</td>
      <td>5.0</td>
      <td>5.3</td>
      <td>5.7</td>
    </tr>
    <tr>
      <td>LG4</td>
      <td>2311</td>
      <td>4.9</td>
      <td>7500</td>
      <td>2050</td>
      <td>2189</td>
      <td>2282</td>
      <td>2346</td>
      <td>2430</td>
      <td>2502</td>
      <td>2603</td>
      <td>2.4</td>
      <td>2.4</td>
      <td>2.5</td>
      <td>2.6</td>
      <td>2.8</td>
      <td>2.9</td>
      <td>3.1</td>
    </tr>
    <tr>
      <td>LP1</td>
      <td>2015</td>
      <td>4.1</td>
      <td>6550</td>
      <td>1825</td>
      <td>1957</td>
      <td>1998</td>
      <td>2059</td>
      <td>2126</td>
      <td>2195</td>
      <td>2263</td>
      <td>3.3</td>
      <td>3.3</td>
      <td>3.5</td>
      <td>3.6</td>
      <td>3.8</td>
      <td>4.0</td>
      <td>4.3</td>
    </tr>
    <tr>
      <td>LP2</td>
      <td>704</td>
      <td>1.8</td>
      <td>2330</td>
      <td>649</td>
      <td>666</td>
      <td>706</td>
      <td>716</td>
      <td>748</td>
      <td>773</td>
      <td>788</td>
      <td>2.0</td>
      <td>2.1</td>
      <td>2.1</td>
      <td>2.2</td>
      <td>2.3</td>
      <td>2.5</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td>LP3</td>
      <td>499</td>
      <td>1.4</td>
      <td>1705</td>
      <td>452</td>
      <td>493</td>
      <td>509</td>
      <td>534</td>
      <td>531</td>
      <td>560</td>
      <td>574</td>
      <td>1.6</td>
      <td>1.7</td>
      <td>1.7</td>
      <td>1.8</td>
      <td>1.9</td>
      <td>2.0</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td>LP4</td>
      <td>1708</td>
      <td>2.4</td>
      <td>5650</td>
      <td>1574</td>
      <td>1639</td>
      <td>1697</td>
      <td>1743</td>
      <td>1819</td>
      <td>1883</td>
      <td>1921</td>
      <td>3.8</td>
      <td>3.9</td>
      <td>4.0</td>
      <td>4.2</td>
      <td>4.4</td>
      <td>4.6</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>PD1</td>
      <td>424</td>
      <td>1.9</td>
      <td>1400</td>
      <td>370</td>
      <td>398</td>
      <td>422</td>
      <td>444</td>
      <td>442</td>
      <td>464</td>
      <td>501</td>
      <td>1.6</td>
      <td>1.7</td>
      <td>1.8</td>
      <td>1.8</td>
      <td>1.9</td>
      <td>2.0</td>
      <td>2.2</td>
    </tr>
    <tr>
      <td>PD2</td>
      <td>418</td>
      <td>1.5</td>
      <td>1400</td>
      <td>383</td>
      <td>406</td>
      <td>426</td>
      <td>425</td>
      <td>455</td>
      <td>460</td>
      <td>477</td>
      <td>1.2</td>
      <td>1.2</td>
      <td>1.3</td>
      <td>1.3</td>
      <td>1.4</td>
      <td>1.5</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>PD3</td>
      <td>1597</td>
      <td>3.0</td>
      <td>5000</td>
      <td>1344</td>
      <td>1462</td>
      <td>1519</td>
      <td>1587</td>
      <td>1667</td>
      <td>1724</td>
      <td>1776</td>
      <td>3.3</td>
      <td>3.4</td>
      <td>3.5</td>
      <td>3.7</td>
      <td>3.8</td>
      <td>4.1</td>
      <td>4.3</td>
    </tr>
    <tr>
      <td>PD4</td>
      <td>410</td>
      <td>1.7</td>
      <td>1300</td>
      <td>363</td>
      <td>389</td>
      <td>397</td>
      <td>396</td>
      <td>429</td>
      <td>442</td>
      <td>451</td>
      <td>1.2</td>
      <td>1.3</td>
      <td>1.3</td>
      <td>1.4</td>
      <td>1.4</td>
      <td>1.5</td>
      <td>1.6</td>
    </tr>
  </tbody>
</table>

Figure 11B shows these metrics for four STG neurons (one of each type), and their corresponding synthetic minimal spanning neurite trees. Bf values between 0 and 0.6 produced neurite trees with neurite length, branch order, and tortuosity distributions that span realistic ranges. Yet, no single bf factor collectively recapitulates each of these distributions for each neuron. For example, a minimal spanning tree with bf = 0 recapitulates a similar branch order distribution to that of the actual LG neuron shown in Figure 11 (bottom). Yet, higher bf values are required to generate neurite length distributions similar to that of the actual LG neuron.

This discrepancy in best-fit bf values across morphological metrics can be observed in all 16 STG neurons (Figure 11B, Figure 11—figure supplements 1–4) and disallows a confident assignment of bf value within or across neuron types. Across the 16 STG neurons evaluated, tortuosity distributions were often quite broad and consistent with MSTs generated with bf = 0 or 0.1. Neurite distributions were less broad and consistent with MSTs generated with higher bf values. Branch order distributions varied widely across the 16 neurons. For many of the STG neurons, MSTs across the full range of bf values had total wiring lengths within 20% of the actual STG neuron (Figure 11—figure supplement 1–4). However, there are several cases wherein the MSTs had total wiring lengths that deviated quite a bit from the STG neuron’s total wiring length.

Taken together, this wiring cost equation alone appears insufficient to comprehensively recapitulate these structural features of STG neurons. It is plausible that STG neurite trees may simply not adhere to the wiring optimization principles enforced by this wiring cost equation.

## Discussion

Many neuron types present recognizable geometries. Yet, it remains unclear how tightly tuned or variable their macroscopic and fine structural features must be in order to generate reliable physiological output. In the present study, we carried out a detailed morphometric analysis of four STG neuron types. We found that their expansive and complex neuronal structures do not adhere to prevailing hypotheses regarding wiring optimization principles thought to govern developmental growth.

### Complex and variable morphologies

Studies in a variety of nervous systems have explored how macroscopic dendritic and axonal arborizations map to physiological function. Work in insect nervous systems showed that spatially distinct dendritic subtrees compute a weighted integration of sensory inputs (Miller and Jacobs, 1984; Cuntz et al., 2008). Studies in the mammalian retina (Bloomfield and Miller, 1986; Hong et al., 2011) and visual cortex (Martin et al., 1983; Martin and Whitteridge, 1984a, 1984b) have demonstrated that neurons receiving sensory inputs at distinct dendritic subtrees detect various visual stimulus features. In this way, large-scale dendritic and axonal arborization patterns reflect circuit-level connectivity and contribute to input-output functions in single neurons.

Some studies (Wang et al., 2002; Cuntz et al., 2008, 2010) have reported quantitative ranges, across many neurons of the same type, in the fine structural properties essential for current flow and integration of voltage signals arising across complex dendritic trees. The geometrical properties of any neurite path: its length, diameter, taper, and branch points, shape current flow. In this way, whether voltage events arising at disparate sites across a dendritic tree are integrated is highly dependent on neuronal geometry (Rall, 1977). Thus, a comprehensive understanding of how morphology maps to function requires examination of both macroscopic branching patterns and finer cable properties.

Our results suggest that STG neuronal morphologies are highly variable across animals. Additionally, our analyses did not reveal any single metric, or combination of metrics, that distinguish the four neuron types from each other. GM neurons presented significantly longer total cable lengths and branch point numbers than the other three neuron types and PD neurons showed slightly more symmetrical neurite arborizations; these are the only statistically significant cell-specific features.

Our investigation of macroscopic features such as soma position, total wiring, and branching patterns, revealed variability across neurons and within neuron types. Analysis of fine geometrical properties revealed that individual STG neurons have soma-to-tip neurite lengths that vary between 200 and 800 µm and diameters with high coefficients of variation within neurite class (primary, secondary, tertiary, or terminating neurites). Additionally, Rall powers at branch points were heterogeneous within and across neurons, suggesting variable continuity of current across the neurite tree. Given all these degrees of freedom, it is quite remarkable that these cell types show highly conserved physiological waveforms across animals.

Other studies (Wilensky et al., 2003; Bucher et al., 2007; Thuma et al., 2009) have described neuronal morphology in the STG. However, it is important to note that these works were completed in different species with different staining procedures, lower imaging resolution, and less precise reconstruction methods. Therefore, it is not surprising that the 16 neurons in this study are more expansive and have measurably greater neurite lengths than previously reported. This is likely due to visualization of smaller processes that may have been lost in these earlier studies. Yet, many of the take-home messages are consistent with these earlier studies: soma positions of given neuron types vary across animals (Bucher et al., 2007; Thuma et al., 2009), and most neuron types are indistinguishable by soma position, maximum branch order, and total cable lengths (Thuma et al., 2009). While these earlier works are suggestive of morphological variability, our image resolution and morphometric analyses have allowed us to quantitatively assess this across a broader range of macroscopic and fine structural features.

### Sloppy geometries that are suitable for circuit function

To date, a number of experimental and theoretical works have argued that neuron growth is governed by a series of optimization principles that serve to maximize conduction velocity and minimize wiring material (Cuntz et al., 2007, 2008, 2010, 2012, 2013; Chklovskii 2000, 2002; Chen et al., 2006; Wen and Chklovskii, 2008; Rivera-Alba et al., 2014). These studies have shown that many neuron types adhere to such optimization principles, suggesting that these are not only theoretical principles, but developmental rules that facilitate synaptic connections and circuit function.

Tortuosity measurements and comparison of STG neurons to minimal spanning trees provided within-neuron measures of wiring inefficiency. Across all 16 neurons, mean tortuosities ranged between one and seven, suggesting highly inefficient wiring. This is in contrast to other neuron types, such as mammalian pyramidal cells and GABAergic interneurons that show efficient tortuosities close to one (Stepanyants et al., 2004; Wen et al., 2009). Likewise, the neurons of the nematode Caenorhabditis elegans present a highly stereotyped and efficient connectome (Chen et al., 2006).

This sloppy morphological tuning of STG neurons is notable, but it is not the first exception to wiring optimality shown in the literature. For example, anatomical studies of motor axons at the interscutularis neuromuscular junction in mouse show a great deal of variability in branching topology of axonal arbors, as well as suboptimal wiring lengths (Lu et al., 2009). As suggested by Lu et al. (2009), such case studies do not imply that wiring optimization principles are not at play, but may simply suggest that other factors constrain morphology in these nervous systems.

STG circuit structure and anatomy are evidently resilient to this loose morphological tuning. STG circuit function relies predominantly on slow oscillations (Graubard and Ross, 1985; Ross and Graubard, 1989) and graded inhibitory transmission (Eisen and Marder, 1982; Marder and Eisen, 1984; Maynard and Walton, 1975; Graubard et al., 1980; Manor et al., 1997, 1999; Bose et al., 2014). Slow synaptic events undergo minimal electrotonic decrement and are resilient to the variable, complex, and extended neurite trees of STG neurons (Otopalik et al., 2017). This would effectively mask the physiological consequences of animal-to-animal variability in morphology.

Additionally, early electron microscopy studies describe the sparse distribution and tight apposition of synaptic input and outputs across the finer processes of the neurite tree, such that nearly every secondary process has both pre- and post-synaptic regions (King, 1976a, 1976b). Further, the connections between particular pairs of neurons are sparsely distributed over multiple neurites of their neurite trees (King, 1976a). King suggests that this sparse distribution of synaptic contacts on finer processes gives rise to some degree of synaptic democracy, wherein no one synaptic partner “exerts an overriding influence on the neuron" (King, 1976a). Such distribution of synaptic connections likely contributes to the masking of morphological variability at the physiological level. Slow postsynaptic voltage events arising across sparsely distributed sites may influence transmission globally or locally. Sparse, slow voltage events, resilient to electrotonic decrement, may have the capacity to sum and alter the net physiology of the neuron. Alternatively, small postsynaptic potentials may locally influence transmission at nearby postsynaptic sites on the same branch, influencing particular synaptic connections in the circuit. Regardless, the electrotonic compact nature of these neurons, along with this tight pairing of pre- and post-synaptic sites across the neurite tree, may effectively compensate for the complex and variable morphologies observed across animals.

Theoretical studies have described the direct consequences of neuronal morphology and neuronal firing patterns (Mainen and Sejnowski, 1996) and shed light on how neuronal structures may be optimized for Hebbian or spike-timing-dependent computations at faster time scales (Stiefel and Sejnowski, 2007). We suspect that minimization of wiring and morphological precision may be more critical when synaptic and circuit-level computations occur at faster time-scales. Yet, a recent study demonstrated a great deal of variability in dendritic morphology within one class of mammalian neocortical pyramidal neurons (Hamada et al., 2016). Interestingly, the distance between the soma and spike initiation zone co-varies with and compensates for variability in the dendritic tree. In this case, the pyramidal neuron achieves its target physiological properties by tuning ion channel distributions to the neuron’s geometry.

If developmental growth of STG neurons is not governed by the same wiring principles suggested in other neuron types, what constrains their growth? Consideration of the spatial relationships between subtrees within individual STG neurons suggests that subtrees grow to fill and tile distinct spatial fields in the neuropil. We speculate that this may be for the purpose of maximizing surface area for the reception of the numerous neuromodulatory substances that are diffusely released in the hemolymph and by the descending inputs of the stomatogastric nerve (Marder and Bucher, 2007; Blitz and Nusbaum, 2011). Thus, in development, space-filling of the neuropil may outweigh the wiring economy that might be expected if decrement of synaptic events were critical to circuit function.

## Materials and methods

### Animals and dissections

Adult male Jonah crabs (Cancer borealis; carapace lengths between 13 and 17 cm) were obtained from Commercial Lobster (Boston, MA). All animals were kept in artificial seawater tanks at 10–13°C on a 12 hr light/12 hr dark cycle without food. Prior to dissection, crabs were anesthetized on ice for 30 min. Dissections of the stomatogastric nervous system (STNS) were performed as previously described (Gutierrez and Grashow, 2009) in saline solution (440 mM NaCl, 11 mM KCl, 26 mM MgCl2, 13 mM CaCl2, 11 mM Trizma base, 5 mM maleic acid, pH 7.4–7.5). In brief: the stomach was dissected from the animal. The STNS was isolated from the stomach, including: the two bilateral commissural ganglia, esophageal ganglion, and STG, as well as the lateral ventral nerve (lvn), medial ventral nerve (mvn), lateral gastric nerve (lgn), and dorsal ganglion nerve (dgn). The STNS was pinned down in a Sylgard-coated petri dish (10 ml) and continuously superfused with chilled saline.

### Cell identification

A schematic of the full experimental workflow can be found in Figure 12. The STG was desheathed and intracellular recordings from the somata were made with 12–40 MΩ glass microelectrodes filled with 0.6M KSO4 and 20 mM KCl, amplified with 1x HS headstages and Axoclamp 2A and 2B amplifiers (Molecular Devices). For extracellular nerve recordings, Vaseline wells were built around the lvn, mvn, lgn, and dgn and stainless steel pin electrodes were used to monitor extracellular nerve activity. GM, LG, LP, and PD neurons were unambiguously identified by matching their intracellular activity with spike units on nerves containing their axons: dgn for GM, lgn for LG and the lvn for LP and PD.

![Figure 12.](https://cdn.elifesciences.org/articles/22352/elife-22352-fig12-v2.jpg)

**Figure 12.:** Neurons were identified physiologically and then filled with Lucifer yellow. Following fixation and immunohistochemical amplification with a rabbit anti-Lucifer yellow primary antibody and an Alexa Fluor 488-tagged secondary antibody, each dye-fill was imaged at 63x magnification as a series of z-stacks that tiled the neuronal structure across the x-y plane (z-stacks contained slices at increments of ~0.5 µm). These z-stacks were stitched together with custom software written in MATLAB. The image stack of each full three-dimensional neuronal structure was then manually traced (image shown is a screenshot from the KNOSSOS platform). The three-dimensional skeletal structures were then converted to hoc files that could be analyzed with a custom quantitative morphology toolbox composed in Python. All conversion and analytical scripts are freely available on the Marder Lab Github repository.

### Neuronal dye-fills

Following electrophysiological cell identification, somata were impaled with low-resistance glass electrodes (3–16 MΩ) backfilled with 2% Lucifer Yellow CH dipotassium salt (LY; Sigma, catalog number L0144) in filtered water. Lucifer Yellow was injected into somata for 20–50 min with negative pulses of between –3 and –7 nA of 0.5 s duration at 0.1–1 Hz. The dye-fill was performed until the fine neuropil processes of the cell were visible with a fluorescent microscope (Leica MF165 FC). Preparations were fixed with 3.5% paraformaldehyde in phosphate-buffered saline (PBS; 440 mM NaCl, 11 mM KCl, 10 mM Na2HPO4, 2 mM KH2PO4, pH 7.4) for 40–90 min at room temperature within 3 hr after LY dye-fill. Preparations were washed with 0.01M PBS-T (0.1–0.3% Triton X-100 in PBS) and stored for 0–7 days at 4°C before processing.

### Dye-fill amplification and immunohistochemistry

The LY signal was amplified by addition of a polyclonal rabbit anti-LY antibody (1:500; Molecular Probes, 16 hr), followed by secondary detection with a polyclonal Alexa Fluor 488-conjugated goat anti-rabbit antibody (IgG H+L chains, highly cross-absorbed; Molecular Probes1:500; 2 hr). Preparations were then washed 4 × 15 min in filtered PBS and mounted on pre-cleaned slides (25x75 × 1 mm, superfrost, VWR) in Vectashield (Vector Laboratories, Burlingame, CA), with 9 mm diameter, 0.12 mm depth silicone seal spacers (Electron Microscopy Sciences, Hatfield, PA) under #1.5 coverslips (Fisher Scientific).

### Confocal imaging and processing

Confocal image stacks of the neuronal dye-fills were acquired with a SP5 CLEM microscope using Leica Application Suite Advanced Fluorescence (LAS AF) software. Confocal images were acquired as tiles in the x-y plane with at 63x magnification with a glycerol objective (Leica HCX PL APO 63x/1.3 GLYC CORR CS (21°C)) at either 2048 x 2048 or 1024 × 1024 resolution. Stacks in the z-dimension were acquired in steps between 0.12 to 1.01 µm steps. These tile stacks were aligned and stitched with a GUI-based MATLAB tool (Goeritz et al., 2013) available at https://github.com/marderlabConfocal_Stitching.

Maximum projection images were generated from these confocal stacks using Imaris 7.0–8.1 software (Bitplane). These were filtered and down-sampled to a third of the resolution in the x and y dimensions. Imaris Slice and Surpass modules were used for adjusting contrast and brightness and to display stacks as maximum-intensity projections or as blend mode projections. Contrast and exposure were adjusted to provide maximum-intensity images.

### Three-dimensional skeletal reconstruction

Neuronal dye-fills were traced and skeletal three-dimensional skeletal reconstructions were generated using one of three software packages: Amira (FEI Visualization, Hillsboro, OR), Imaris (Bitplane), or KNOSSOS (Max Planck Institute, Heidelberg, Germany, http://www.knossostool.org). These techniques range from semi-automated (Amira) to manual (Imaris, KNOSSOS), and are reviewed elsewhere (Donohue and Ascoli, 2011). No major tracing differences were found between these methods in generating skeletal structures, although KNOSSOS was the fastest method.

In brief, a team of tracers generated skeletal reconstructions of neurite structures. They were instructed to place nodes at the thickest or most intense part of each neurite and to minimize the number of nodes while capturing as much curvature as possible. Tracers did not measure neurite diameters or volumes. In some cases, anastomoses appeared to be present but tracers were instructed to avoid tracing loops. The skeletons from Amira and Imaris were exported directly as hoc (extendable high-order calculator) files consistent with the NEURON simulation environment (Hines and Carnevale, 2001; Hines et al., 2007). KNOSSOS files were exported as xml collections of edges and nodes and were adapted into hoc (extendable high-order calculator) files by custom Python software, which is available at: https://github.com/marderlab/Quantifying_Morphology.

### Geometry objects

All quantitative analyses were built in Python using custom geometry objects generated from the hoc skeletons for each neuron. These geometry objects had the following features: terminating tips (non-soma, non-axonal terminal filaments), somata (manually tagged), paths (filaments connecting somata to tips), segments (any tracer-defined collection of nodes), branches (a collection of segments spanning branch points or multi-furcations), and axons (manually selected terminal filaments that do not branch for at least 20 µm; see Figure 12 for an example). Most of the properties examined in this study can be readily extracted from these geometry object attributes. Skeletal representations were generated by scatter plotting a subset of the geometry object's nodes. This and all code is available for download at github.org/marderlab/Quantifying_Morphology.

### Path length and tortuosity

Path lengths were calculated as the sum of the distances between the points that constitute a given branch. Geometry objects contain instances of branches and segments, each with a length attribute. The length of a path is simply the sum of the lengths of its constituent segments. Horizontal histograms were used to show the relative distributions underlying the data; means are indicated with solid black lines, medians with dashed lines (solid orange lines for radial histograms), and interquartile ranges with shaded regions. Path tortuosity is defined as path length divided by the Euclidean distance from the first node to the last node (the soma to a tip). A tortuosity of 1.0 indicates a perfectly straight path while values larger than 1.0 indicate a wandering or tortuous path.

### Branch angle

To compute branch angles, all the branch points and segments that contributed to the bifurcation were collected; in the case of a multi-furcation, the procedure was repeated with all possible combinations of branches. The endpoints of the segments were collected into groups containing a midpoint (Pmid, which is also the proximal endpoint of the parent and the daughter) and the distal endpoints of the parent (P1) and daughter (P2). Using the other two points as nodes of a triangle, branch angle is given by

$$
\theta_{mid}=cos^{−1}(\frac{P_{mid}^{2}−P_{1}^{2}−P_{2}^{2}}{2P_{1}P_{2}})
$$

where $P_{x}=$ magnitude of vector formed from points other than point x. Angles were reported in degrees and were taken as 180 - $\theta$mid to reference the angle against the continuation of the initial segment. Branch angles and torques were plotted on circular histograms with inter-quartile ranges indicated by shading; means and medians are indicated by the black and orange lines, respectively. These circular histograms were inspired by Bielza et al. (2014), although the code is original.

### Symmetry index

Length asymmetry is found by summing the lengths of all downstream segments originating from daughter segments of a bifurcation. Symmetry index measures this property by dividing the smaller summed length by the larger summed length. Formally, the symmetry index S is defined as

$$
S=\frac{min{d_{1},d_{2}}}{max{d_{1},d_{2}}}
$$

where d1 and d2 represent the sum of the lengths of all downstream segments for the two daughter branches of a bifurcation. Downstream branches are all the neighboring branches arising from the daughter and any of its subsequent daughters. Intuitively, a symmetry index of 1.0 indicates a perfectly symmetrical bifurcation in terms of downstream lengths, whereas values closer to 0 indicate highly asymmetrical bifurcations.

### Branch diameter

Manual measurements were made from 2D slices of the neuron to approximate soma and branch diameters using the measure tool in the ImageJ variant FIJI (www.fiji.sc). Most STG neurites, especially large-diameter neurites, are slightly flat (compressed in the z-dimension), rather than cylindrical. Therefore, the values given here should represent a fair assessment of the parent-daughter ratios (used to calculated Rall Power) of the neurons. The diameters of the soma, initial primary neurite leaving the soma (1°), secondary branches (2°), tertiary branches (3°), and branches where one of the daughters is a terminating tip (‘tip’) were measured.

### Soma position

Using the maximum projections of each image stack, the coordinates for the neuropil center and soma positions were measured in pixels and converted to microns using FIJI. These were plotted on the same set of axes and translated such that the neuropil center within each preparation was situated at the origin.

### Rall power

Rall power (Rall, 1959) is calculated as $parent^{X}=daughter_{1}^{X}+ daughter_{2}^{X}$, where the parent is the radius of the parent branch and daughter is the radius of the daughter neurites. Rall power values have been found to range from about 1.5 (Rall, 1959) to 3 (Chklovskii and Stepanyants, 2003). We calculated the Rall power of STG branches numerically by minimizing $parent^{X}−(daughter_{1}^{X}+ daughter_{2}^{X})$ and varying X.

### Sholl analysis

Sholl analysis typically superimposes concentric circles or spheres, centered at the soma, to quantify the spatial density of neurites by measuring the number of intersections of circles/spheres with neurite branches. Because STG somata are segregated from the neuropil and the neurite field, this approach was not logically consistent with the goal of Sholl analyses. Instead, we calculated an equivalent somatofugal Sholl distance by creating linearly spaced distances ranging from zero to the maximum path length and asked for each pair of nodes whether the traversing line crossed this distance. In this way, path lengths are the distances being measured and branching patterns can be elucidated. Equivalently, one could re-plot an STG neuron with the soma at the center of a 2D Sholl graph with filaments that conserve segment length branching out radially from the soma.

### Spatial density analysis

Spatial density analysis was used to visualize neurite density of individual neurons in the x-y plane. Geometry objects were generated from the hoc skeletons for each neuron using Python. A Gaussian kernel density estimation (from the SciPy statistics module, utilizing Scott’s Rule for bandwidth selection) was used to generate a probability distribution function for all points in the x and y dimensions composing each neuron’s geometry object. This resulted in a probability value (between 0 and 1) for each point that indicates its relative number of nearest neighbors. For each neuron, the geometry object points were plotted in the x-y plane and colored by the points’ probabilities. The color map was scaled to the range of probabilities within each neuron. In this way, the spatial density plots can be interpreted as visualizations of neurite density. This approach was adapted from http://stackoverflow.com/a/20107592 and can be found on the Marder Lab Github.

### Subtrees

The main path was defined as the segments connecting the soma to the axon(s). LP, PD, and LG neurons have only one axon (thus, only one main path), whereas GM neurons have 3–5 axons and, therefore, 3–5 main paths. Subtrees were defined by: (1) having a root segment that departed from the primary neurite and (2) containing at least one terminating tip segment. The terminating tips of a subtree form a tip cluster. The center of mass of a subtree was calculated as the mean x-y-z coordinates of its terminating tips. The radius of a subtree tip cluster was calculated as the mean distance from the center of mass coordinates to each tip’s coordinates. We used a design-based inference sampling strategy (Geuna, 2000) to randomly assign tips to any cluster, while maintaining the number of tips per cluster. The reassigned tips for a given subtree could originate from any subtree, consistent with an earlier study (Wilensky et al., 2003). We performed this randomization between 100 and 2000 times, depending on the number of possible tip configurations and subtrees. The subtree tip cluster radii and the number of overlapping subtree tip clusters from the randomized subtrees were compared to those of the original neuronal structure.

### General and statistical analysis of skeletal reconstructions

All analyses were carried out in R 3.2.2 or Python 3.4.2 with the assistance of open-source packages, chiefly NumPy and SciPy (van der Walt et al., 2011), NetworkX (Hagberg et al., 2008), and generally used interactively with IPython (Perez and Granger, 2007). Although the hoc data files are not large, some analyses required intensive computation. The computer used was a 2014 Dell Precision T3600 with 64 GB RAM and six i7 processors running Ubuntu 14.04. A similar computer was used for the image analysis and manual tracing. The interested user will find sample hoc data and all required programs on the Marder Lab GitHub site (http://github.com/marderlab/Quantifying_Morphology). Users are welcome to copy or adapt the analytic and plotting tools found there with attribution. A complete hoc dataset can be found in the Source Data file. One-way analysis of variance or Kruskal-Wallis (when homoscedasticity is not satisfied and data are not normally distributed) were performed for statistical comparisons between cell types and Tukey honest-significant difference was (HSD) used for post-hoc pairwise comparisons in all cases. These statistical analyses are reported in the text.

### Graphical presentation

Neuron images were captured with Imaris or Amira. Plots were made in Python with Matplotlib (Hunter, 2007) or MATLAB (MathWorks, Natick, MA). Plotting software is available on the Marder Lab Github repositories. Figures were assembled in InkScape (http://www.inkscape.org/) or Illustrator (Adobe).

### Minimal spanning neurite trees (MSTs)

Synthetic neurite trees were generated using the TREES toolbox developed by Hermann Cuntz (Ernst Strüngmann Institute, Frankfurt, Germany) and the Häusser Laboratory (University College London, UK). This MATLAB (Mathworks, Natick, MA) toolbox is freely available with an extensive user’s manual online: www.treestoolbox.org. The minimal spanning neurite trees were generated with similar methods as described in Cuntz et al. (2010). For each of the 16 STG neurons, synthetic trees were constructed to connect the root node (defined by the coordinates of the first branch point relative to the soma, in the actual neuronal structure) to the target nodes. Target nodes were randomly generated from points uniformly distributed in an elliptical volume approximating the space occupied by the actual neuronal structure. The number of target nodes was tuned such that branch point numbers of the MSTs were within 0–20% of the actual STG neuron. The lengths and paths of neurite segments connecting these nodes were constrained by the simple wiring cost equation: total cost = wiring cost + bf * path length cost (as described in Cuntz et al., 2010). The balancing factor (bf) is the only variable parameter in this model and weighs the cost of minimizing total cable length versus minimizing soma-to-tip path lengths. Seven corresponding synthetic trees were generated for each of the 16 STG neurons in the present study with a range of balancing factor values between 0.1 and 0.6 (at increments of bf = 0.1). Total wiring, branch point numbers, branch order distributions, neurite length distributions, and tortuosity distributions of the synthetic trees were plotted in comparison to those of the actual skeletal structures using MATLAB. This range of bf values was chosen because the resulting MSTs recapitulated realistic ranges in these morphological features that spanned those of the actual neurons. All data and structures pertaining to the actual and synthetic neurite trees used for this simulation are freely available on the Marder Lab Github repository: http://github.com/marderlab.

### Data accessibility

Raw confocal image stacks are over 100 GB but are available upon request. Skeletal reconstructions of these neuronal dye-fills are available as hoc files on the neuron morphology database Neuromorpho.org under Cancer borealis. Morphometric data sets, analytical scripts, and minimal spanning tree simulation data are available at github.org/marderlab.

# Predictive modeling reveals that higher-order cooperativity drives transcriptional repression in a synthetic developmental enhancer

## Authors

- Yang Joon Kim<sup>1</sup> ([ORCID: 0000-0003-1742-5657](https://orcid.org/0000-0003-1742-5657))
- Kaitlin Rhee<sup>2</sup>
- Jonathan Liu<sup>3</sup>
- Selene Jeammet<sup>4</sup>
- Meghan A Turner<sup>5</sup>
- Stephen J Small<sup>6</sup>
- Hernan G Garcia<sup>1</sup> ([ORCID: 0000-0002-5212-3649](https://orcid.org/0000-0002-5212-3649)) †

### Affiliations

1. Chan Zuckerberg Biohub San Francisco United States
2. Department of Chemical Biology, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
3. Department of Physics, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
4. Department of Biology, Ecole Polytechnique Paris France ([ROR:05hy3tk52](https://ror.org/05hy3tk52))
5. Biophysics Graduate Group, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
6. Department of Biology, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
7. Department of Molecular and Cell Biology, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
8. Institute for Quantitative Biosciences–QB3, University of California at Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))

† Corresponding author

## Abstract

A challenge in quantitative biology is to predict output patterns of gene expression from knowledge of input transcription factor patterns and from the arrangement of binding sites for these transcription factors on regulatory DNA. We tested whether widespread thermodynamic models could be used to infer parameters describing simple regulatory architectures that inform parameter-free predictions of more complex enhancers in the context of transcriptional repression by Runt in the early fruit fly embryo. By modulating the number and placement of Runt binding sites within an enhancer, and quantifying the resulting transcriptional activity using live imaging, we discovered that thermodynamic models call for higher-order cooperativity between multiple molecular players. This higher-order cooperativity captures the combinatorial complexity underlying eukaryotic transcriptional regulation and cannot be determined from simpler regulatory architectures, highlighting the challenges in reaching a predictive understanding of transcriptional regulation in eukaryotes and calling for approaches that quantitatively dissect their molecular nature.

## Introduction

During embryonic development, transcription factors bind stretches of regulatory DNA termed enhancers to dictate the spatiotemporal dynamics of gene expression patterns that will lay out the future body plan of multicellular organisms (Spitz and Furlong, 2012; Small and Arnosti, 2020). One of the greatest challenges in quantitative developmental biology is to predict these patterns from knowledge of the number, placement, and affinity of transcription factor binding sites within enhancers. The early embryo of the fruit fly Drosophila melanogaster has become one of the main workhorses in this attempt to achieve a predictive understanding of cellular decision-making in development due to its well-characterized gene regulatory network and transcription factor binding motifs, and the ease with which its development can be quantified using live imaging (Garcia et al., 2020; Small and Arnosti, 2020; Rivera et al., 2019).

Predictive understanding calls for the derivation of theoretical models that generate quantitative and experimentally testable predictions. Thermodynamic models based on equilibrium statistical mechanics have emerged as a widespread theoretical framework to achieve this goal (Ackers et al., 1982; Vilar and Leibler, 2003; Bolouri and Davidson, 2003; Bintu et al., 2005b; Bintu et al., 2005a; Segal et al., 2008; Fakhouri et al., 2010; Sayal et al., 2016; Phillips et al., 2019; Eck et al., 2020). For instance, over the last decade, a dialogue between these thermodynamic models and experiments demonstrated the capacity to quantitatively predict bacterial transcriptional regulation from knowledge of the DNA regulatory architecture (He et al., 2010; Garcia and Phillips, 2011; Brewster et al., 2014; Garcia et al., 2012; Sepúlveda et al., 2016).

The predictive power of these models is evident when inferring model parameters from simple regulatory architectures and using those parameters to make parameter-free predictions of more complex architectures (Boedicker et al., 2013a; Boedicker et al., 2013b, Razo-Mejia et al., 2018; Phillips et al., 2019). Consider, for example, that RNA polymerase II (RNAP)—which we take as a proxy for the whole basal transcriptional machinery—binds to a promoter with a dissociation constant $K_{p}$. When RNAP is bound, transcription is initiated at a rate $R$ (Figure 1A). In the absence of any regulation, a thermodynamic model will only have $K_{p}$ and $R$ as its free parameters which can be experimentally determined by, for example, measuring mRNA distributions (Razo-Mejia et al., 2020). Now, we assume that the parameters $K_{p}$ and $R$ inferred in this step do not just enable a fit to the data, but that their values represent physical quantities that remain unaltered as more complex regulatory architectures are iteratively considered. As a result, when we consider the case where a single repressor molecule can bind, our model calls for only two new free parameters: a dissociation constant for repressor to its binding motif $K_{r}$, and a negative cooperativity between repressor and RNAP, $\omega_{r⁢p}$, that makes the recruitment of RNAP to the DNA less favorable when the repressor is bound to its binding site (Figure 1B). Once again, after determining $K_{r}$ and $\omega_{r⁢p}$ experimentally (Phillips et al., 2019), we consider the case where two repressors can bind simultaneously (Figure 1C). If the repressors interact with RNAP independently of each other, then our model has no remaining free parameters such that we will have reached complete predictive power. However, protein-protein interactions between repressors could exist or even higher-order interactions giving rise to a repressor-repressor-RNAP ternary complex might be present. This extra complexity would require yet another round of experimentation to quantify these interactions represented by $\omega_{r⁢r}$ and $\omega_{r⁢r⁢p}$ in Figure 1C, respectively. Even after quantifying these parameters, predictive power might not be reached if, after adding yet another repressor binding site, a complex between all three repressors and RNAP can be formed (Figure 1D).

![Figure 1.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig1-v2.jpg)

**Figure 1.:** (A) In the absence of repressor binding, gene expression can be characterized by a dissociation constant between RNAP and the promoter $K_{p}$ and the rate of transcription initiation when the promoter is bound by RNAP $R$. (B) In the presence of a single repressor binding site, models need to account for two additional parameters describing the repressor dissociation constant $K_{r}$ and a repressor-RNAP interaction term $\omega_{r⁢p}$. (C) For two-repressor architectures, parameters accounting for repressor-repressor interactions $\omega_{r⁢r}$ and for interactions giving rise to a repressor-repressor-RNAP complex could also have to be incorporated. (D) For the case of three repressor binding sites, additional parameters $\omega_{r⁢r⁢r}$ and $\omega_{r⁢r⁢r⁢p}$ capturing the higher-order cooperativity between three repressor molecules and between three Runt molecules and RNAP, respectively, could be necessary. Note the nomenclature shown below each construct, which indicates which Runt binding sites are present in each construct.

While protein-protein cooperativity captured by $\omega_{r⁢r}$ has been studied both in bacteria (Ackers et al., 1982; Ptashne and Gann, 2002) and eukaryotes (Giniger and Ptashne, 1988; Ma et al., 1996; Lebrecht et al., 2005; Parker et al., 2011; Fakhouri et al., 2010; Sayal et al., 2016), the necessity of accounting for higher-order interactions such as those described in our example by the $\omega_{r⁢r⁢p}$ and $\omega_{r⁢r⁢r⁢p}$ terms had only been demonstrated in archeae (Peeters et al., 2013) and bacteria (Dodd et al., 2004). The need to invoke this higher-order cooperativity in eukaryotes only became apparent in the last few years (Estrada et al., 2016b; Park et al., 2019; Biddle et al., 2020). These higher-order cooperativities might be necessary in order to account for the complex interactions mediated by, for example, the recruitment of co-repressors (Courey and Jia, 2001; Walrad et al., 2011), mediator complex (Park et al., 2019), or any other element of the transcriptional machinery. As a result, while posing a challenge to reaching a parameter-free predictive understanding of transcriptional regulation, higher-order cooperativity provides an avenue for quantifying the complexity of the molecular processes underlying eukaryotic cellular decision-making.

In this paper, we sought to test whether an iterative and predictive approach, such as that outlined in Figure 1, was possible for transcriptional repression in the early embryo of the fruit fly Drosophila melanogaster or whether it is necessary to invoke higher-order cooperativities that challenge the reach of our predictive models as we add more complexity to the system. To make this possible, we engineered binding sites for the Runt repressor into the Bicoid-activated hunchback P2 minimal enhancer. We systematically varied the number and placement of Runt binding sites within this enhancer (Chen et al., 2012) in order to determine whether model fits to real-time transcriptional measurements from the enhancer constructs containing only one-Runt binding site could accurately predict repression in two- and three-Runt binding site constructs (Figure 1). We found that a thermodynamic model can recapitulate all our data. However, we also discovered that, while the model could describe repression by a single Runt repressor, protein-protein and higher-order cooperativities had to be invoked in order to quantitatively account for regulation by two or more repressor molecules. While these higher-order cooperativities limit the iterative bottom-up discourse between theory and experiment that has been successful in bacteria (Phillips et al., 2009), they also provide a concrete theoretical framework for quantifying the complexities behind eukaryotic transcriptional control, and call for the development of new theories and experiments specifically conceived to uncover the the molecular underpinnings of this complexity.

## Results

### Predicting transcription rate using a thermodynamic model of Bicoid activation and Runt repression

Inspired by the theory-experiment dialogue leading to predictive understanding of the lac operon in E. coli over the last four decades (Phillips et al., 2019; Razo-Mejia et al., 2018; Garcia and Phillips, 2011; Garcia et al., 2012; Ackers et al., 1982; Buchler et al., 2003), we built a predictive model of Runt repression on the Bicoid-activated hunchback P2 enhancer using the thermodynamic model framework (Phillips et al., 2019; Bintu et al., 2005b; Bintu et al., 2005a) with the goal of predicting the rate of transcription initiation as a function of input transcription factor concentration, and the number and placement of Runt repressor binding sites. Our model rests on the ‘occupancy hypothesis’ that states that the rate of mRNA production, $d⁢[m⁢R⁢N⁢A]/d⁢t$, is proportional to the probability of the promoter being bound by RNA polymerase II (RNAP), $p_{b⁢o⁢u⁢n⁢d}$, such that

$$
\frac{d⁢[m⁢R⁢N⁢A]}{d⁢t}=R⁢p_{b⁢o⁢u⁢n⁢d},
$$

where $R$ is the rate of mRNA production when the promoter is occupied by RNAP. Note that, throughout this study, we treat the rate of transcription initiation and the rate of RNAP loading interchangeably.

To generate intuition, we start by modeling the case of hunchback P2 with one Runt binding site. Figure 2A illustrates the possible states the system can be found in. Each state has an associated statistical weight which can be calculated as prescribed by equilibrium statistical mechanics (Bintu et al., 2005b; Bintu et al., 2005a). Here, we assume that there are six Bicoid binding sites with the same dissociation constant given by $K_{b}$, one Runt binding site with a dissociation constant specified by $K_{r}$, and a promoter with a dissociation constant for RNAP prescribed by $K_{p}$. In the absence of Runt, we consider four states as shown in the top two rows of Figure 2A. Here, we assume that Bicoid-Bicoid cooperativity is so strong that the enhancer can either be unoccupied or completely bound by Bicoid molecules (Gregor et al., 2007; Park et al., 2019). Further, we consider an interaction between Bicoid and RNAP given by $\omega_{b⁢p}$. For simplicity, we use the dimensionless parameters $b=[B⁢i⁢c⁢o⁢i⁢d]/K_{b}$, $r=[R⁢u⁢n⁢t]/K_{r}$ and $p=[R⁢N⁢A⁢P]/K_{p}$. These assumptions lead to a functional form reminiscent of a Hill function that explains the sharp step-like expression pattern along the embryo’s anterior-posterior axis of the hunchback gene (Gregor et al., 2007; Park et al., 2019; Driever and Nüsslein-Volhard, 1988; Driever et al., 1989). A full thermodynamic model in which we do not make this assumption of high Bicoid-Bicoid cooperativity is discussed in detail in Section ‘Derivation of the general thermodynamic model for the hunchback P2 enhancer’ and Section ‘Derivation of the general and simpler thermodynamic model for the hunchback P2 enhancer with one Runt binding site’.

![Figure 2.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig2-v2.jpg)

**Figure 2.:** (A) States and statistical weights for the regulation of hunchback P2 with one Runt binding site in the limit of strong Bicoid-Bicoid cooperativity. Here, we use the dimensionless parameters $b=[B⁢i⁢c⁢o⁢i⁢d]/K_{b}$, $r=[R⁢u⁢n⁢t]/K_{r}$, and $p=[R⁢N⁢A⁢P]/K_{p}$, where $K_{b}$, $K_{r}$, and $K_{p}$ are the dissociation constants of Bicoid, Runt, and RNAP, respectively. $\omega_{b⁢p}$ represents the cooperativity between Bicoid and RNAP, $\omega_{r⁢p}$ captures the cooperativity between Runt and RNAP, and $R$ represents the rate of transcription when the promoter is occupied by RNAP. The top two rows correspond to states where only Bicoid and RNAP act, while the bottom two rows represent repression by Runt. (B) Representative prediction of RNAP loading rate as a function of Bicoid and Runt concentrations for $\omega_{b⁢p}=3,\omega_{r⁢p}=0.001,p=0.001,R=1⁢(A⁢U/m⁢i⁢n)$.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) States, weights, and degeneracy considered for our thermodynamic model. (B) Simpler form of the thermodynamic model in the limit of $\omega_{b}≫1$.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Statistical weights and degeneracy of each state the system can be found in. (B) Simpler form of the model from (A) in the limit of strong Bicoid-Bicoid cooperativity.

The molecular mechanism by which Runt downregulates transcription of its target genes remains unclear (Chen et al., 2012; Hang and Gergen, 2017; Koromila and Stathopoulos, 2017; Koromila and Stathopoulos, 2019). Here, we assume the so-called ‘direct repression’ model (Gray et al., 1994) that posits that Runt operates by inhibiting RNAP binding to the promoter through a direct Runt-RNAP interaction term given by $\omega_{rp}<1$ independently of Bicoid. As a result, in the presence of Runt, we consider four additional states as shown in the bottom two rows of Figure 2A. Other potential mechanisms of Runt repression are further discussed in Supplementary Section ‘Comparison of different modes of repression’, where we also show that the choice of specific mechanism does not change our conclusions.

Given these assumptions, we arrive at the microstates and corresponding statistical weights shown in Figure 2A. The probability of finding RNAP bound to the promoter, $p_{b⁢o⁢u⁢n⁢d}$, is calculated by dividing the sum of all statistical weights featuring RNAP by the sum of the weights of all possible microstates. The calculation of $p_{b⁢o⁢u⁢n⁢d}$ combined with Equation 1 leads to the expression

$$
Rate=Rp_{bound}=R\frac{p+b^{6}p\omega_{bp}+rp\omega_{rp}+b^{6}rp\omega_{bp}\omega_{rp}}{1+b^{6}+r+b^{6}r+p+b^{6}p\omega_{bp}+rp\omega_{rp}+b^{6}rp\omega_{bp}\omega_{rp}},
$$

which makes it possible to predict the output rate of mRNA production as a function of the input concentrations of Bicoid and Runt (Figure 2B). With this theoretical framework in hand, we experimentally tested the predictions of this model.

### Measuring transcriptional input-output to test model predictions

The transcriptional input-output function in Figure 2B indicates that, in order to predict the rate of RNAP loading and to test our theoretical model, we need to first measure the concentration of the input Bicoid and Runt transcription factors. In order to quantify the concentration profile of Bicoid, we used an established eGFP-Bicoid line (Gregor et al., 2007) and measured mean Bicoid nuclear concentration dynamics along the anterior-posterior axis of the embryo over nuclear cycles 13 and 14 (nc13 and nc14, respectively) as shown in Movie Figure 3—video 1 (Eck et al., 2020). An example snapshot and time trace of Bicoid nuclear concentration dynamics at 40% of the embryo length appear in Figure 3A and B.

![Figure 3.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-v2.jpg)

**Figure 3.:** (A) Snapshot of an embryo expressing eGFP-Bicoid spanning 20–60% of the embryo length. (For a full time-lapse movie, see Movie Figure 3—video 1) (B) Bicoid nuclear fluorescence dynamics taken at 40% of the embryo. (C) Snapshot of an embryo expressing eGFP:LlamaTag-Runt spanning 20–60% of the embryo length. (For a full time-lapse movie, see Movie Figure 3—video 2) (D) Runt nuclear concentration dynamics in males and females. (E) Measured transcription factor concentration profiles along the anterior-posterior axis of the embryo. The concentration profiles are averaged over the gray shaded regions shown in (B) and (D) which corresponds to a time window between 5 and 10min into nc14. (F) Predicted RNAP loading rate for hunchback P2 with one Runt binding site over the anterior-posterior axis generated for a reasonable set of model parameters $K_{b}=30$ AU, $K_{r}=100$ AU, $\omega_{b⁢p}=100$, $p=0.001$, and $R=1$ AU/min for varying values of the Runt-RNAP interaction term $\omega_{r⁢p}=[10^{-2},1]$. (G) Schematic of the MS2 system where 24 repeats of the MS2 loop sequence are inserted downstream of the promoter followed by the lacZ gene. The MS2 coat protein (MCP) fused to GFP binds the MS2 loops. (H) Example snapshot of an embryo expressing MCP-GFP and Histone-RFP. Green spots correspond to active transcriptional loci and red circles correspond to nuclei. Spot intensities are proportional to the number of actively transcribing RNAP molecules. (I) Representative MS2 fluorescence averaged over a narrow window (2.5% of the embryo length) along the anterior-posterior axis of the embryo. The initial rate of RNAP loading was obtained by fitting a line (brown) to the initial rise of the data and the x-intercept is defined as the onset of transcription ($T_{ON}$). (J) Measured initial rate of RNAP loading (over a spatial bin of 2.5% of the embryo length) across the anterior-posterior axis of the embryo, from the hunchback P2 enhancer. (B, D, E, and J, error bars represent standard error of the mean over $\geq3$ embryos; I, error bars represent standard error of the mean over the spatial averaging corresponding to roughly ten nuclei; A, C, and H, white scale bars represent 20 μm.).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Instantaneous predicted rate of transcription calculated using dynamic transcription factor concentration profiles at each time point (blue) and resulting averaged rate of transcription averaged over the time window of 5–10 minutes from the 13th anaphase (green) compared to the predicted rate of transcription obtained using the static transcription factor concentrations of Bicoid and Runt shown in Figure 3E (red). (Illustrative predictions calculated at 30% of the embryo length using $K_{b}=30⁢(A⁢U)$, $K_{r}=100⁢(A⁢U)$, $\omega_{b⁢p}=100$, $\omega_{r⁢p}=0.1$, $p=0.001$, $R=300⁢(A⁢U/m⁢i⁢n)$.) (B) Spatial profile of the predicted rate of transcription calculated by averaging the instantaneous transcription rate (green) or by using the averaged input transcription factor concentrations as inputs (red). (A, B, error bars and shaded areas represent the standard error of mean over embryos 42 embryos generated from making pairs of independently measured six eGFP-Bicoid embryo and seven GreenLlamaTag-Runt embryo.).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Schematic showing how the initial rate of RNAP loading is measured by extracting the slope resulting from a linear fit to the MS2 time traces at the beginning of nuclear cycle 14. (B) Initial rate of RNAP loading along the embryo length for each construct in the presence and absence of Runt for each of our synthetic enhancer construct. (B, Error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) An example MS2 time trace in nuclear cycle 14. The decay regime is defined from the peak of the signal to the end of the measurement. $T_{O⁢N}$ is defined by the x-intercept of the slope of the fitted line. $T_{o⁢f⁢f}$ is determined by the decay time in the exponential function. The gray shaded region from $T_{O⁢N}$ to $T_{O⁢F⁢F}$ is defined as the transcriptional time window. (B) The decay time can be extracted from the accummulated mRNA signal obtained by integrating the MS2 fluorescence. Here, decay time is defined as the time it takes to reach (1–1/e) of that maximum accumulated mRNA. (C) Transcriptional time window along the anterior-posterior axis for each construct with and without Runt protein. (A, error bars represent standard error of the mean over the spatial averaging corresponding to roughly ten nuclei; C, error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) Heatmap showing the transcriptional signal from the hunchback P2 enhancer for individual nuclei (rows) demonstrating that there are two populations of loci: transcriptionally active and inactive loci. (B) Fraction of transcriptionally active loci along the embryo for each construct for wild-type and runt null backgrounds. (B, error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** (A) An illustrative MS2 time trace in nuclear cycle 14. The accumulated mRNA is calculated by integrating the MS2 time traces during nuclear cycle 14, indicated by the purple area under the MS2 trace. (B) Accumulated mRNA along the embryo for each construct for the wild-type and runt null backgrounds. (B, error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** (A) An example MS2 time trace averaged over MS2 spots in a spatial window of 2.5% of the embryo length in nuclear cycle 14. The accumulated mRNA is calculated by integrating the MS2 time traces during nuclear cycle 14, indicated by the purple area under the MS2 trace. (B) Accumulated mRNA as a function of Runt concentration (as reported by Figure 3E) for each construct for wild-type and runt null backgrounds. Bicoid concentration at each corresponding Runt concentration (as shown in Figure 3E) is shown as a black curve to note that the activator concentration changes as Runt concentration changes along the anterior-posterior axis of the embryo. (B, error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** (A) Snapshots of an embryo for eGFP:LlamaTag-Runt (top) and Histone-iRFP (bottom) spanning 20–60% of the embryo length in nuclear cycle 14. The scale bars represent 50 μm.

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig3-figsupp8-v2.jpg)

**Figure 3—figure supplement 8.:** Correlation between the initial RNAP loading rates and accumulated mRNA levels at each position along the embryo length for all constructs for the wild-type and runt null backgrounds. A Pearson’s correlation coefficient between these two quantities of 0.90 is found.

Quantification of the Runt concentration using standard fluorescent protein fusions is not possible due to the slow maturation times of these proteins (Bothma et al., 2018). We therefore measured Runt concentration dynamics using our recently developed LlamaTags, which are devoid of such maturation dynamics artifacts (Bothma et al., 2018). Specifically, we generated a new fly line harboring a fusion of a LlamaTag against eGFP to the endogenous runt gene using CRISPR/Cas9-mediated homology-directed repair (Materials and Methods; Harrison et al., 2010, Gratz et al., 2015).

Using this LlamaTag fusion, we measured the mean Runt nuclear fluorescence along the anterior-posterior axis of the embryo over nc13 and nc14 (Materials and Methods; Figure 3B; Movie Figure 3—video 2). As expected due to the location of the runt gene on the X chromosome (Lott et al., 2011), there is a sex dependence in the nuclear concentration levels in nc13, with males displaying lower Runt levels than females; this difference is compensated by early nc14 (Figure 3C and D). As a result, for ease of analysis, we focused subsequent quantitative dissection on nc14.

We used the measured input protein concentration profiles to predict the output transcription rate. To make this possible, we invoked previous observations stating that the concentration dynamics of input transcription factors does not significantly affect the initial rate of RNAP loading (Garcia et al., 2013; Eck et al., 2020). As a result, we decided to use the time-averaged concentration dynamics of Bicoid and Runt over a time window spanning 5 min after the 13th anaphase to 10 min after this anaphase (gray shaded region in Figure 3B and D) as inputs to our model, resulting in the static spatial concentration profiles shown in Figure 3E. We then used these time-averaged concentration profiles of input transcription factors to calculate the time-averaged rate of transcription initiation over the same time window. In the Supplementary Information Section ‘Comparing using static versus dynamic transcription factor concentrations as model inputs’ we compare this methodology with one that acknowledges input transcription factor concentration dynamics and show that the prediction stemming from both approaches leads to equivalent theoretical predictions. Specifically, the time-averaged rate of transcription predicted by the dynamic inputs was similar to the rate of transcription predicted by the static inputs.

Along the anterior-posterior axis of the embryo, the measured Bicoid and Runt concentration profiles define a trajectory through the input-output function (Figure 2B). Given a set of parameters, this trajectory predicts the initial rate of RNAP loading. This quantitative prediction can be directly compared with experimentally measured transcription initiation rates. For example, given the concentration profiles shown in Figure 3E, we calculate the RNAP loading rate as a function of the position along the embryo for different values of the Runt-RNAP interaction, captured by $\omega_{r⁢p}$. Figure 3F illustrates how $\omega_{r⁢p}$ shapes the predicted profiles for the RNAP loading rate. As expected, the prediction shows that the rate of transcription decreases as the strength of the Runt-RNAP interaction decreases.

Next, we sought to experimentally test these predictions by measuring the rate of RNAP loading using the MS2 system (Bertrand et al., 1998; Lucas et al., 2013; Garcia et al., 2013). Here, we inserted 24 repeats of the MS2 loop sequence following the hunchback P2 enhancer and even-skipped promoter in our reporter construct, which leads to the fluorescent labeling of sites of active transcription in living embryos (Figure 3G and H; Movie Figure 3—video 3). The fluorescence intensity of each MS2 spot is proportional to the number of actively transcribing RNAP molecules (Garcia et al., 2013). In order to quantify the transcriptional activity reported by MS2, we measured the mean MS2 spot fluorescence over nuclei in a narrow spatial window (Figure 3I; Garcia et al., 2013; Eck et al., 2020). To measure the initial rate of RNAP loading, we obtained the slope of the initial rise in the number of actively transcribing RNAP molecules over the same time window used to average input transcription factor concentration (Figure 3I, brown line). The resulting RNAP loading rate plotted over the anterior-posterior axis is in qualitative agreement with the classic pattern driven by the hunchback P2 minimal enhancer (Figure 3J; Garcia et al., 2013, Chen et al., 2012, Park et al., 2019).

While we chose the initial rate of transcription as the experimental measurable to confront against our model predictions, the MS2 technique can also report on other dynamical features of transcription such as the time window over which transcription occurs and the fraction of loci that engage in transcription at any point over the nuclear cycle. Although these two quantities have been shown to be relevant in shaping gene expression patterns in other regulatory contexts (Garcia et al., 2013; Lammers et al., 2020; Eck et al., 2020; Dufourt et al., 2018; Reimer et al., 2021), we found that the transcription time window was not significantly regulated in the presence of Runt (Figure 3—figure supplement 3). As described in Section ‘Quantitative interpretation of MS2 signals’, we did find some modulation of the fraction of transcriptionally engaged loci for a subset of our synthetic enhancer constructs but, as we could not detect a clear trend in how this fraction of active loci was modulated, we did not pursue a theoretical dissection of the control of this quantity by Runt.

### Enhancer sequence dictates unrepressed transcription rates by determining RNAP-promoter interactions

With these theoretical models and our experimental platform in hand, we designed a set of synthetic enhancer constructs with differing number and placement of Runt binding sites as shown in Figure 4A (top) , and Figure 4—figure supplement 1. Our enhancer sequences are identical to those created and validated by Chen et al., 2012, which kept the length of the enhancer sequence consistent and inserted experimentally validated Runt binding sites (Melnikova et al., 1993; Lewis et al., 1999; Chen et al., 2012; Koromila and Stathopoulos, 2017) by mutating the base pairs within the enhancer that are not mapped to binding sites for any known transcripiton factor in the early fruit fly embryo (Hertz et al., 1990; Hertz and Stormo, 1999).

![Figure 4.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig4-v2.jpg)

**Figure 4.:** (A) Measured initial rates of RNAP loading across the anterior-posterior axis of the embryo for all synthetic enhancer constructs in the absence of Runt protein. (The [111] synthetic enhancer construct with the position of Bicoid (red) and Runt (green) binding sites is shown in genomic length scale on top as a reference.) (B) Representative best MCMC fit and (C) associated corner plot for the [001] construct in the runt null background. (D) Inferred model parameters for all synthetic enhancers in the absence of Runt repressor. Note the large spread in $\omega_{b⁢p}$, consistent with the corner plot shown in (C), which indicates that our model does not constrain this parameter well compared to the other parameters. (E) Coefficient of variation of inferred parameters. (A, B), shaded regions represent the standard error of the mean over>3 embryos; (B) error bars from MCMC fit represent 95% confidence interval; (D) error bars represent standard deviations calculated from the MCMC posterior chains; (E) error bars are calculated by propagating the standard deviation of individual parameters from their MCMC chains.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) PATSER scores for Bicoid and Zelda for hunchback P2 (blue) and hunchback P2 with three Runt sites (brown). The binding motifs with PATSER scores higher than three are shown. We concluded that neither Bicoid nor Zelda binding sites were created or removed by the introduction of these three Runt binding motifs. (B) A schematic diagram of hunchback P2 minimal enhancer with three Runt binding sites with mapped binding sites for Bicoid and Zelda from (A) and Runt binding sites from Chen et al. [2012]. The position of Runt binding sites are noted with their distance from the promoter (marked as 0).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Schematic showing how the initial rate of RNAP loading is measured for an individual embryo by extracting the slope resulting from a linear fit to the averaged MS2 time traces at the beginning of nuclear cycle 14. Here, the MS2 traces are averaged over a set of nuclei that are in the same spatial bin along the anterior-posterior axis of the embryo (2.5% of the embryo length). (B) Initial rate of RNAP loading along the embryo for individual embryos (indicated by the different colors, such as red, blue, or yellow) for each construct in the absence of Runt protein. The average obtained by taking the mean over these multiple embryos is shown in black. (C) Comparison between the inferred parameter values of from Equation 3 for the [010] construct for different averaging strategies. The averaged parameters inferred from the initial rate of RNAP from individual embryos, shown in color in (B), are shown in red. The parameters inferred from the mean initial rate of RNAP averaged over multiple embryos, shown in black in (B), are shown in black. There is no significant difference between these inferred values. Note that the [010] construct was chosen because it exhibits the largest dynamic range in the initial rate of RNAP loading across multiple embryos. (A, error bars represent standard error of the mean over 3 embryos; B, error bars for individual embryos represent the 95% confidence interval from the linear fit and error bars for black line represents the standard error of the mean over 3 embryos; C, red error bars represent the standard error of the mean over 3 embryos, while blue error bars indicate the 95% confidence interval.).

A major assumption of our theoretical approach is that the model parameters obtained from simple regulatory architectures can be used as inputs for more complex constructs. For instance, we assume that the Runt-independent model parameters for Bicoid and RNAP action—$K_{b}$, $\omega_{b⁢p}$, $p$ and $R$ (Figure 2A)—are conserved for all constructs containing Runt binding sites regardless of their number and placement in the enhancer. If model parameters can be shared across constructs, then our model should predict the same profile for the rate of transcription across all synthetic enhancer constructs.

To test this assumption, we measured the initial rate of RNAP loading in all of our reporter constructs, in runt null embryos (Materials and Methods). Notably, unrepressed transcription rates varied significantly across synthetic enhancers (Figure 4A). For example, despite no Runt being present, the [001] construct had almost twice the unrepressed rate of [000].

This large construct-to-construct variability in unrepressed transcription rates likely originates from the Runt binding site sequences interfering with some combination of Bicoid and RNAP function. To uncover the mechanistic effect of these Runt binding sites sequences on unrepressed activity, we sought to determine which parameters in our thermodynamic model varied across constructs. In the absence of Runt repressor, only four states remain corresponding to the two top rows of Figure 2A. In this limit, the predicted rate of transcription is given by

$$
 Rate=R\frac{p+(\frac{[Bicoid]}{K_{b}})^{6}p\omega_{bp}}{1+p+(\frac{[Bicoid]}{K_{b}})^{6}+(\frac{[Bicoid]}{K_{b}})^{6}p\omega_{bp}},
$$

where we have invoked the same parameters as in Figure 2 and Equation 2. For clarity, the free parameters in this equation are marked using the red color.

To obtain the model parameters for each construct measured in Figure 4A, we invoked the Bayesian inference technique of Markov Chain Monte Carlo (MCMC) sampling that has been widely used for inferring the biophysical parameters from theoretical models (Liu et al., 2021, Razo-Mejia et al., 2018, Geyer and Thompson, 1992; Supplementary Section ‘Markov Chain Monte Carlo inference protocol’). A representative comparison of the MCMC fit to the experimental data reveals a good agreement between theory and experiment (Figure 4B). MCMC sampling also gives the distribution of the posterior probability for each parameter as well as their cross-correlation (Figure 4C). These corner plots reveal relatively unimodal posterior distributions, suggesting that a unique set of parameters can explain the data.

Note that, while the Bicoid dissociation constant $K_{b}$ and the Bicoid-RNAP interaction term $\omega_{b⁢p}$ remain largely unchanged regardless of enhancer sequence, there is considerable variability in the inferred mean RNAP-dependent parameters $p$ and $R$ (Figure 4D). This variability can be further quantified by examining the coefficient of variation,

$$
C⁢V=\frac{\sigma}{\mu},
$$

where $\sigma$ and μ are the standard deviation and the mean of each parameter, respectively, calculated over all constructs. The coefficients of variation for the RNAP and promoter-dependent parameters are much higher than those for Bicoid-dependent parameters (≈ 40% versus < 10%; Figure 4E). This suggests that the variability in unrepressed transcription rates due to the presence of Runt binding sites stems from differences in the behavior of RNAP at the promoter rather than differences in Bicoid binding or activation. As a result, as we consider increasingly more complex regulatory architectures, we associated each construct with its own specific Bicoid- and RNAP-dependent parameters as inferred in Figure 4D. In contrast, as we will show below, we will conserve Runt-dependent parameters as we consider increasingly more complex constructs featuring more Runt binding sites.

### The thermodynamic model recapitulates repression by one Runt binding site

Next, we asked whether our model recapitulates gene expression for the hunchback P2 enhancer with a one-Runt binding site in the presence of Runt repressor as predicted by Equation 2. We posited that, since the binding site sequence remains unaltered throughout our constructs (Figure 4—figure supplement 1), the value of the Runt dissociation constant $K_{r}$ would also remain unchanged across these enhancers regardless of Runt binding site position; however, we assumed that, as the distance between Runt and the promoter varied, so could the Runt-RNAP interaction term $\omega_{r⁢p}$.

We measured the initial rate of transcription along the embryo for all our constructs containing one Runt binding site in the presence of Runt protein. In this case of a single Runt binding site, Equation 2 predicts that the initial rate of RNAP loading will be given by

$$
Rate=Rp_{bound}=R\frac{p+b^{6}p\omega_{bp}+\frac{[Runt]}{K_{r}}p\omega_{rp}+b^{6}\frac{[Runt]}{K_{r}}p\omega_{bp}\omega_{rp}}{1+b^{6}+\frac{[Runt]}{K_{r}}+b^{6}r+p+b^{6}p\omega_{bp}+\frac{[Runt]}{K_{r}}p\omega_{rp}+b^{6}\frac{[Runt]}{K_{r}}p\omega_{bp}\omega_{rp}}.
$$

Here, we have have rewritten Equation 2 to clarify which parameters are fixed and which parameters are inferred using color coding. Specifically, we took Runt-independent parameters ($K_{b}$, $\omega_{b⁢p}$, $p$ and $R$), shown in black, as given by the inference from our previous experiments in the absence of Runt (Figure 4). Further, Runt-dependent parameters ($K_{r}$ and $\omega_{r⁢p}$) which we will infer, are shown in red. We then used MCMC sampling to infer these Runt-dependent parameters for each of our constructs while retaining the mean values of Runt-independent parameters.

The resulting MCMC fits show significant agreement with the experimental data (Figure 5A), confirming that, within our model, the same dissociation constant $K_{r}$ can be used for all Runt binding sites regardless of their position within the enhancer. Further, the corner plot yielded a unimodal distribution of posterior probability of the inferred parameters (Figure 5B), indicating the existence of a unique set of most-likely model parameters. We challenged our assumption of constant $K_{r}$ across our constructs in Section Figure 5—figure supplement 3, where we show that, even if we posit that each construct has a different Runt dissociation constant, the obtained $K_{r}$ values are comparable.

![Figure 5.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig5-v2.jpg)

**Figure 5.:** (A) Initial transcription rate as a function of position along the embryo for the three constructs containing one Runt binding site in the presence and absence of Runt repressor, together with their best MCMC fits. (B) Corner plots from MCMC inference for all constructs with one Runt binding site. (C) Inferred $\omega_{r⁢p}$ value as a function of distance between the promoter and the Runt binding site. (A, data points represent mean and standard error of the mean over the embryos and shaded error bars represent 95% confidence intervals for the best MCMC fits for Runt WT datasets; C, data and error bars represent the mean and standard deviation of the posterior chains, respectively.).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** States and statistical weights corresponding to the hunchback P2 enhancer with one Runt binding site for the (A) direct repression, (B) competition, and (C) quenching mechanisms.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A,B,C) MCMC fits for three modes of repression, (i) direct repression, (ii) competition, and (iii) quenching, for our three one-Runt site constructs, (A) [100], (B) [101], and (C) [001]. (D) Corner plots resulteing from MCMC inference on the three one-Runt site constructs for each model. (E) Inferred parameters from MCMC fitting. (A,B, and C, error bars represent standard error of the mean over $\geq3$ embryos; E, error bars represent standard deviation of the posterior chain.).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A) A schematic of three synthetic enhancers with one Runt binding site at different positions in the enhancer (proximal, intermediate and distal) and their key parameters $K_{r}$ and $\omega_{r⁢p}$. (B,C,D,E) Best MCMC fits to the data for the one-Runt binding site constructs for models with varying assumptions of how $K_{r}$ and $\omega_{r⁢p}$ vary across constructs. (B) Model assuming that both $K_{r}$ and $\omega_{r⁢p}$ are constant across constructs. (C) Model assuming that $K_{r}$ remains constant and $\omega_{r⁢p}$ varies across constructs. (D) Model assuming that $\omega_{r⁢p}$ remains constant and that $K_{r}$ varies across constructs. (E) Model assuming that both $K_{r}$ and $\omega_{r⁢p}$ vary across constructs. (F) Akaike Information Criterion for all four models. The parameters kept constant across constructs are shown on the x-axis, and the AIC value is shown on the y-axis. (G) Inferred parameter values ($K_{r}$ and $\omega_{r⁢p}$) from (E) for all three one-Runt binding site constructs ([100],[010],[001]). (B-E, data points represent mean and standard error of the mean over >3 embryos, shaded regions represent 95% confidence intervals for the best MCMC fits for the datasets in the presence of Runt protein.).

The observed trend in the Runt-RNAP interaction captured by $\omega_{r⁢p}$ qualitatively agrees with the “direct repression” model. Specifically, because the model assumes that Runt interacts directly with RNAP, it predicts that, the farther apart Runt and the promoter are, the lower this interaction should be (Gray et al., 1994). In agreement with this prediction, the mean value of $\omega_{r⁢p}$ obtained from our fits changes from high repression ($\omega_{r⁢p}≈0.1$) in the [001] construct to almost no repression ($\omega_{r⁢p}≈1$) in the [100] construct as the Runt site is moved away from the promoter (Figure 5C). Thus, the direct repression model recapitulates repression by a single Runt molecule using the the same dissociation constant regardless of Runt binding site position, and displays the expected dependence of the Runt-RNAP interaction term on the distance between these two molecules.

### Predicting repression by two-Runt binding sites requires both Runt-Runt and Runt-Runt-RNAP higher-order cooperativity

Could the parameters inferred in the preceding section be used to accurately predict repression in the presence of two Runt binding sites? An extra Runt binding site enables new protein-protein interactions between Runt molecules and RNAP (Figure 6A). First, we considered individual Runt-RNAP interaction terms, $\omega_{r⁢p⁢1}$ and $\omega_{r⁢p⁢2}$, whose values were already inferred from the one-Runt binding site constructs as $\omega_{r⁢p_{[001]}},\omega_{r⁢p_{[010]}},a⁢n⁢d⁢\omega_{r⁢p_{[100]}}$ (Figure 5D). Second, we considered protein-protein interactions (positive or negative) between two Runt molecules, $\omega_{r⁢r}$. Third, following recent studies of Bicoid activation of the hunchback P2 minimal enhancer (Estrada et al., 2016a; Park et al., 2019), we also posited the existence of simultaneous Runt-Runt-RNAP higher-order cooperativity $\omega_{r⁢r⁢p}$. Given these different cooperativities, and as shown in detail in Figure 6—figure supplement 6B, the predicted rate of transcription is

$$
Rate=R(p+b^{6}p\omega_{bp}+rp(\omega_{rp1}+\omega_{rp2})+r^{2}p\omega_{rp1}\omega_{rp2}\omega_{rr}\omega_{rrp}+b^{6}rp\omega_{bp}(\omega_{rp1}+\omega_{rp2})+b^{6}r^{2}p\omega_{bp}\omega_{rp1}\omega_{rp2}\omega_{rr}\omega_{rrp})(1+b^{6}(1+2r+p\omega_{bp})+2r+p+rp(\omega_{rp1}+\omega_{rp2})+r^{2}(\omega_{rr}+p\omega_{rp1}\omega_{rp2}\omega_{rr}\omega_{rrp})+b^{6}rp\omega_{bp}(\omega_{rp1}+\omega_{rp2})+b^{6}r^{2}\omega_{rr}+b^{6}r^{2}p\omega_{bp}\omega_{rp1}\omega_{rp2}\omega_{rr}\omega_{rrp})^{−1}.
$$

![Figure 6.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-v2.jpg)

**Figure 6.:** (A) Direct repression model for hunchback P2 with two Runt binding sites featuring Runt-RNAP interaction terms given by $\omega_{r⁢p⁢1}$ and,$\omega_{r⁢p⁢2}$ Runt-Runt cooperativity captured by $\omega_{r⁢r}$, and Runt-Runt-RNAP higher-order cooperativity accounted for by $\omega_{r⁢r⁢p}$. (B) Parameter-free model prediction for two Runt binding sites when the two Runt molecules bind the DNA and interact with RNAP independently of each other. (C,D,E) Best MCMC fits for the data for two-Runt binding site constructs for models with various combinations of cooperativity parameters. (C) Model incorporating Runt-Runt cooperativity. (D) Model incorporating Runt-Runt-RNAP higher-order cooperativity. (E) Model accounting for both Runt-Runt cooperativity and Runt-Runt-RNAP higher-order cooperativity. (F) Fixed or inferred parameters $\omega_{r⁢r}$ and $\omega_{r⁢r⁢p}$ for all two-Runt binding site constructs. Note that $\omega_{r⁢r}$ is fixed to 1 for [011] and [101] constructs due to the fact that no Runt-Runt cooperativity is necessary to quantitatively describe the expression driven by these constructs; only the [110] construct is used to infer both $\omega_{rr}$ and $\omega_{r⁢r⁢p}$. The horizontal line of $\omega=1$ denotes the case of no cooperativity. (G) Akaike Information Criterion (AIC) for all four scenarios of different free parameters shown throughout (B–E). (B-E, data points represent mean and standard error of the mean over the embryos. C-E, shaded error bars represent 95% confidence intervals for the best MCMC fits for the Runt WT datasets; F, data and error bars represent the mean and standard deviation of the posterior chain, while the standard deviation for the fixed $\omega_{r⁢r}$ is set to 0.).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The model assumes no interactions between Runt molecules. (A,B, and C, error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) Schematic of cooperativity terms considered: Runt-Runt cooperativity given by $\omega_{r⁢r}$ and Runt-Runt-Bicoid complex higher-order cooperativity captured by $\omega_{b⁢r⁢r}$, in addition to the competition terms $\omega_{b⁢r⁢1}$ and $\omega_{b⁢r⁢2}$. (B) Zero-parameter prediction using the inferred parameters from zero- and one-Runt binding site constructs. (C,D,E) Best MCMC fits for our three two-Runt binding sites constructs considering (C) Runt-Runt cooperativity, (D) Runt-Runt-Bicoid complex higher-order cooperativity, and (E) both Runt-Runt cooperativity and Runt-Runt-Bicoid complex higher-order cooperativity. (B,C,D, and E, error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** (A) Schematic of additional cooperativities considered: Runt-Runt cooperativity $\omega_{r⁢r}$ and Runt-Runt-Bicoid-RNAP complex higher-order cooperativity $\omega_{b⁢r⁢r⁢p}$. (B) Zero-parameter prediction using the inferred parameters from one-Runt binding site constructs. (C,D,E) Best MCMC fits for our three two-Runt binding sites constructs considering (C) Runt-Runt cooperativity, (D) Runt-Runt-Bicoid-RNAP higher-order cooperativity, and (E) both Runt-Runt cooperativity and Runt-Runt-Bicoid-RNAP higher-order cooperativity. (B,C,D, and E, error bars represent standard error of the mean over $\geq3$ embryos.).

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** (A) Model schematic where we add a new $\omega_{r⁢r}$ parameter representing Runt-Runt cooperativity. (B) Corresponding states and weights for hunchback P2 with two Runt binding sites in the presence of Runt-Runt cooperativity. (C) Prediction of the initial rate of RNAP loading profiles over a range of Runt-Runt cooperativity strength,,$\omega_{r⁢r}=[10^{-6},10^{24}]$ for all constructs of hunchback P2 with two Runt binding sites. The sole presence of Runt-Runt cooperativity is not enough to recapitulate the data corresponding to the [110] construct. (C, error bars represent standard error of the mean over $\geq3$ embryos).

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-figsupp5-v2.jpg)

**Figure 6—figure supplement 5.:** (A) Schematic of a model where we add Runt-Runt-RNAP higher-order cooperativity represented by $\omega_{r⁢r⁢p}$. (B) Thermodynamic model states and weights for hunchback P2 with two Runt binding sites in the presence of Runt-Runt-RNAP higher-order cooperativity. (C) Histograms showing the posterior distribution of the inferred $\omega_{r⁢r⁢p}$ parameter from the best MCMC fit shown in Figure 6D. The black line represents the mean and the dotted lines represent standard deviation from the mean.

![Figure 6—figure supplement 6.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-figsupp6-v2.jpg)

**Figure 6—figure supplement 6.:** (A) Schemati showing Runt-Runt cooperativity and higher-order cooperativity. (B) States and weights for hunchback P2 with two Runt binding sites with Runt-Runt cooperativity and higher-order cooperativity. (C) Corner plots associated with the MCMC inference performed on two-Runt binding sites data from the best MCMC fit shown in Figure 6E. While $\omega_{r⁢r}$ is not very well constrained, $\omega_{h⁢o}$ shows a unique optimal value.

![Figure 6—figure supplement 7.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig6-figsupp7-v2.jpg)

**Figure 6—figure supplement 7.:** Sensitivity test for $K_{r}$ by repeating the MCMC inference for different scenarios of cooperativities with different values of $K_{r}$.(A) Direct repression model for hunchback P2 with two-Runt binding sites featuring Runt-RNAP interaction terms given by $\omega_{r⁢p⁢1}$ and $\omega_{r⁢p⁢2}$, Runt-Runt cooperativity captured by $\omega_{r⁢r}$, and Runt-Runt-RNAP higher-order cooperativity accounted for by $\omega_{r⁢r⁢p}$. (B) Parameter-free model prediction for a two-Runt binding site construct ([110]) with different $K_{r}$ values (Left: $K_{r}$ inferred from Figure 5; Center: $K_{r}^{′}=10⁢K_{r}$; Right: $K_{r}^{′′}=0.1⁢K_{r}$) in the case where the two Runt molecules bind the DNA and interact with RNAP independently of each other. (C,D,E) Best MCMC fits to the data for a two-Runt binding site construct ([110]) with different $K_{r}$ values for models with various combinations of cooperativity parameters (Left: $K_{r}$ inferred from Figure 5; Center: $K_{r}^{′}=10⁢K_{r}$; Right: $K_{r}^{′′}=0.1⁢K_{r}$). (C) Model incorporating Runt-Runt cooperativity. (D) Model incorporating Runt-Runt-RNAP higher-order cooperativity. (E) Model accounting for both Runt-Runt cooperativity and Runt-Runt-RNAP higher-order cooperativity.

Here, once again, we have color-coded parameters to be inferred in red to differentiate them from fixed parameters that were already inferred in previous sections. Despite the complexity of this equation, note that its only free parameters are the cooperativity parameters $\omega_{r⁢r}$ and $\omega_{r⁢r⁢p}$. As a result, we sought to determine whether the Runt-RNAP cooperativity terms, $\omega_{r⁢p⁢1}$ and $\omega_{r⁢p⁢2}$, are sufficient to predict repression by two Runt molecules, or whether the cooperativities given by $\omega_{r⁢r}$ and $\omega_{r⁢r⁢p}$ also need to be invoked.

Consider the simplest case where two Runt molecules bind and interact with RNAP independently from each other. Here, $\omega_{r⁢r}=1$, and $\omega_{r⁢r⁢p}=1$. This model has no free parameters; all parameters have already been determined by the inferences performed on Runt null datasets and one-Runt binding site constructs (Figure 4 and Figure 5, respectively). While there was some agreement between the model and the data for the [101] construct (Figure 6B, center), significant deviations from the prediction occurred for the other two constructs. These deviations ranged from less repression than predicted for [011] (Figure 6B, left) to more repression than predicted for [110] (Figure 6B, right). Thus, this simple model of Runt independent repression is not supported by the experimental data, suggesting additional regulatory interactions between the Runt molecules and RNAP.

A first alternative to the independent repression model is the consideration of Runt-Runt cooperative interactions such as those that characterize many transcription factors (Park et al., 2019; Estrada et al., 2016b; He et al., 2010; Segal et al., 2008; Ptashne, 2004). However, adding a Runt-Runt cooperativity term, $\omega_{r⁢r}$, was insufficient to account for the observed regulatory behavior (Figure 6C; Figure 6—figure supplement 4 more thoroughly analyzes this discrepancy). A second alternative consists in incorporating a Runt-Runt-RNAP higher-order cooperativity term, $\omega_{r⁢r⁢p}$. While the best MCMC fits revealed significant improvements in predictive power, important deviations still existed for the [110] construct (Figure 6D, right; Figure 6—figure supplement 5 more thoroughly analyzes the MCMC inference results).

Not surprisingly, given the agreement of the higher-order cooperativity model with the data for the [011] and [101] constructs (Figure 6D, left and center), this agreement persisted when both Runt-Runt cooperativity and Runt-Runt-RNAP higher-order cooperativity were considered (Figure 6E, left and center). However, including these two cooperativities also significantly improved the ability of the model at explaining the [110] experimental data (Figure 6E, right). Thus, while higher-order cooperativity is the main interaction necessary to quantitatively describe repression by two Runt repressors, pairwise cooperativity also needs to be invoked. This conclusion is supported by our MCMC sampling: posterior distributions for the Runt-Runt cooperativity term are not well constrained for the [011] or [101] constructs, whereas Runt-Runt-RNAP higher-order cooperativity is constrained very well across all constructs (Figure 6—figure supplement 6D; Figure 6—figure supplement 6 more thoroughly analyzes the MCMC inference results). As a result, accounting for both pairwise and higher-order cooperativity is necessary for the model to explain the observed rate of RNAP loading of all three constructs.

The higher-order cooperativity revealed by our analysis can lead to more or less repression than predicted by the independent repression model, motivating us to determine the magnitude of this cooperativity across constructs. To make this possible, we inferred the magnitude of the Runt-Runt cooperativity $\omega_{r⁢r}$ and the Runt-Runt-RNAP higher-order cooperativity $\omega_{r⁢r⁢p}$. As shown in Figure 6F, depending on the spatial arrangement of Runt binding sites, the Runt-Runt-RNAP higher-order cooperativity term $\omega_{r⁢r⁢p}$ can be below or above 1. Note that, in doing these fits, we first set the Runt-Runt cooperativity, $\omega_{r⁢r}$, values for [011] and [101] to 1 because, as we had demonstrated in Figure 6D, only the higher-order Runt-Runt-RNAP cooperativity was necessary. Thus, different placements of Runt molecules on the enhancer lead to distinct higher-order interactions with RNAP which, in turn, can result in less or more repression than predicted by a model where Runt molecules act independently of each other.

### Repression by three-Runt binding sites also requires higher-order cooperativity

Building on our success in deploying thermodynamic models to explain repression by one- and two-Runt binding sites, we investigated repression by three-Runt binding sites. First, we accounted for pairwise interactions between Runt and RNAP, which were inferred from measurements of the one-Runt binding site constructs (Figure 1B), yielding $\omega_{r⁢p_{[001]}},\omega_{r⁢p_{[010]}}$, and $\omega_{r⁢p_{[100]}}$ from [001], [010], and [100]. Second, we considered pairwise protein-protein interactions between Runt molecules (Figure 1C), which were inferred from the two-Runt binding sites constructs through the parameters $\omega_{r⁢r_{[011]}},\omega_{r⁢r_{[101]}}$, and $\omega_{r⁢r_{[110]}}$. Finally, we incorporated Runt-Runt-RNAP higher-order cooperativity acquired from the two-Runt binding sites constructs (Figure 1C) captured by $\omega_{r⁢r⁢p_{[011]}},\omega_{r⁢r⁢p_{[101]}}$, and $\omega_{r⁢r⁢p_{[110]}}$. we tested our model predictions using a similar scheme to that described in the previous section: we generated a parameter-free prediction for the initial rate of transcription by using the inferred parameters from the one- and two-Runt binding sites constructs, including the pairwise and higher-order interactions described above.

Figure 7A shows the resulting parameter-free prediction. As seen in the figure, our model could not qualitatively recapitulate the experimental data as it predicted too much repression. Such disagreement suggests that additional regulatory interactions are at play. Building on the need for higher-order cooperativity in the two-Runt binding site case, we propose the existence of higher-order cooperativities necessary to describe regulation by three Runt molecules—Runt-Runt-Runt higher-order cooperativity, $\omega_{r⁢r⁢r}$ and Runt-Runt-Runt-RNAP higher-order cooperativity, $\omega_{r⁢r⁢r⁢p}$ (Figure 1D). The resulting expression for the predicted rate of transcription in the presence of all these sources of cooperativity is shown in Equation S10 in Section ‘Derivation of the general and simpler thermodynamic model for the hunchback P2 enhancer with one Runt binding site’. For simplicity, we assumed that the Runt-Runt-Runt cooperativity is one, and only determined the Runt-Runt-Runt-RNAP higher-order cooperativity. By including only a Runt-Runt-Runt-RNAP higher-order cooperativity parameter, our model recapitulated the experimental data (Figure 7B). Thus, our results further support the view in which the addition of Runt repressor binding motifs in an enhancer calls for the incorporation of cooperativities of increasingly higher-order.

![Figure 7.](https://cdn.elifesciences.org/articles/73395/elife-73395-fig7-v2.jpg)

**Figure 7.:** (A) Prediction using previously inferred Runt-RNAP, Runt-Runt, and Runt-Runt-RNAP cooperativity parameters. (B) Best MCMC fit obtained by incorporating an additional Runt-Runt-Runt-RNAP higher-order cooperativity parameter of $\omega_{r⁢r⁢r⁢p}=857$, corresponding to roughly $7⁢k_{B}⁢T$ of free energy. (A,B, data points represent mean and standard error of the mean over>3 embryos; B, shaded regions represent 95% confidence intervals for the best MCMC fit.).

## Discussion

One of the challenges in generating predictions to probe thermodynamic models is that, often, these models are contrasted against experimental data from endogenous regulatory regions (Segal et al., 2008; Sayal et al., 2016; Park et al., 2019). Here, the presence of multiple binding sites for several transcription factors—known and unknown (Vincent et al., 2016)—leads to models with a combinatorial explosion of free parameters. Like the proverbial elephant that can be fit with four parameters (Mayer et al., 2010), experiments with endogenous enhancers typically contain enough parameters to render it possible to explain away apparent disagreement between theory and experiment (Garcia et al., 2020).

To close this gap, synthetic minimal enhancers have emerged as an attractive alternative to endogenous enhancers (Fakhouri et al., 2010; Sayal et al., 2016; Park et al., 2019; Crocker et al., 2016). Here, the presence of only a handful of transcription factor binding sites and the ability to systematically control their placement and affinity dramatically reduce the number of free parameters in the model (Garcia et al., 2020). Inferences performed on these synthetic constructs could then inform model parameters that would make it possible to quantitatively predict transcriptional output of de novo enhancers (Sayal et al., 2016).

Building on these works, we sought to predict how the Runt repressor, which counteracts activation by Bicoid along the anterior-posterior axis of the early fly embryo (Chen et al., 2012), dictates output levels of transcription. To dissect repression, a strong and detectable level of expression in the absence of the repressor was needed, prompting us to choose a simple system of synthetic enhancers based on the strong hunchback P2 minimal enhancer (Garcia et al., 2013; Chen et al., 2012). This enhancer has been carefully studied in terms of its activator Bicoid and the pioneer-like transcription factor Zelda in the early embryo (Driever and Nüsslein-Volhard, 1988; Garcia et al., 2013; Park et al., 2019; Eck et al., 2020), making it easier to identify neutral sequences within the enhancer for introducing Runt binding sites (Chen et al., 2012). Further, when inserted into hunchback P2, Runt binding site number determines the level of transcription incrementally (Chen et al., 2012). Thus, hunchback P2 provided an ideal scaffold for quantitatively and systematically dissecting repression by Runt.

Previous studies using synthetic enhancers relied on measurements of input transcription factor patterns using fluorescence immunostaining, and of cytoplasmic mRNA patterns using fluorescence in situ hybridization (FISH) or single-molecule FISH. These fixed-tissue techniques have key differences from the live-imaging approach adopted here. First, given the dynamical nature of development, it is necessary to know when data were acquired. Doing so with high temporal resolution using FISH is challenging, although it can be accomplished to some degree by synchronizing embryo deposition before fixation (Park et al., 2019). Second, while most transcription factors directly dictate the rate of RNAP loading, and hence the rate of mRNA production (Spitz and Furlong, 2012; Garcia et al., 2013; Eck et al., 2020), typical FISH measurements report on the accumulated mRNA in the cytoplasm, which is a convolution of all processes of the transcription cycle—initiation, elongation, and termination (Liu et al., 2021; Alberts et al., 2015)—as well as mRNA nuclear export dynamics, diffusion, and degradation. These processes could be modulated in space and time, potentially confounding measurements. Here, we overcame these challenges by using the MS2 technique to precisely time our embryos and acquire the rate of transcription initiation. Of course, despite the ease of measuring the rate of transcription initiation using MS2, the accumulated mRNA is presumably a more relevant quantity for predicting downstream cellular decision making. Previous studies have shown that the MS2-MCP technique can also be used to quantify such patterns of accumulated mRNA, and that this quantification leads to results comparable to those obtained by smFISH (Garcia et al., 2013; Lammers et al., 2020). Following the same quantification method, we assessed the relationship between the initial rate of RNAP loading and the accumulated mRNA (Figure 3—figure supplement 5, Figure 3—figure supplement 6) by plotting them against each other. Reassuringly, as shown in Figure 3—figure supplement 8, our analysis revealed a strong correlation (with Pearson’s correlation coefficient of 0.90), supporting our claim that higher-order cooperativity is essential for explaining the action of multiple transcription factors during the development.

Interestingly, our initial dissection of constructs containing various combinations of Runt binding sites, but in the absence of Runt protein, revealed that unrepressed gene expression levels depend strongly on the number and placement of the binding sites within the enhancer (Figure 4A). These results challenge previous assumptions that unregulated gene expression levels stay unchanged as enhancer architecture is modulated (Sayal et al., 2016; Fakhouri et al., 2010; Barr et al., 2017), but they are in accordance with observations in bacterial systems (Garcia et al., 2012). As a result, our measurements call for accounting for unregulated levels in future quantitative dissections of eukaryotic enhancers, or to study relative magnitudes such as the fold-change in gene expression that has driven the dissection of bacterial transcriptional regulation (Phillips et al., 2019).

Using the thermodynamic model shown in Equation 3, we determined that the Bicoid-dependent parameters remain constant while RNAP-dependent parameters vary across these synthetic enhancer constructs. We speculate that the overall enhancer sequence, which changed as a result of the placement of different combinations of Runt binding sites within it, might affect the binding of the transcriptional machinery. Specifically, since the enhancer is proximal to the promoter, the transcriptional machinery might see slightly different DNA sequences in the vicinity of the promoter as suggested by published structures of the transcriptional machinery assembled on DNA (Louder et al., 2016).

Once we accounted for this difference in unrepressed gene expression levels, we determined that the repression profiles obtained for constructs bearing one-Runt binding site could be described by a simple thermodynamic model (Figure 2). Specifically, we showed that the same dissociation constant described Runt binding regardless of the position of its binding site along the enhancer (Figure 5A). Further, the Runt-RNAP interaction terms describing repressor action decreased as the binding site was placed farther from the promoter (Figure 5C), qualitatively consistent with a ‘direct repression’ model in which Runt needs to physically contact RNAP in order to realize its function (Jaynes and O’Farrell, 1991; Gray et al., 1994; Hewitt et al., 1999).

Although our model recapitulated repression by a one-Runt binding site, the inferred parameters were insufficient to quantitatively predict repression by two-Runt binding sites (Figure 6B). These results suggest that multiple repressors do not act independently of each other. Instead, new parameters describing both Runt-Runt cooperativity and Runt-Runt-RNAP higher-order cooperativity had to be incorporated into our models to quantitatively describe Runt action in these constructs (Figure 6—figure supplement 1C–E). An examination of the various cooperativity values inferred in the language of interaction energies (Table 1) revealed that these energies were of a magnitude comparable to protein-protein interaction energies previously measured in bacterial systems (Dodd et al., 2004; Bintu et al., 2005a; Amit et al., 2011). Interestingly, these interaction energies were both positive and negative, suggesting that both cooperativity or anti-cooperativity are at play depending on enhancer architecture (Amit et al., 2011). Additionally, the [101] construct showed a closer agreement with the parameter-free prediction, without invoking higher-order cooperativity, than the other two constructs ([110] or [011]). This further supports a picture where higher-order cooperativity is sensitive to the placement and orientation of transcription factor binding sites within regulatory regions.

**Table 1.**
 Interaction energies for the Runt-related cooperativity parameters from one-, two-, and three-Runt sites constructs.Note that we used the Boltzmann relation of $\omega=e⁢x⁢p⁢(-E/(k_{B}⁢T))$, where the $E$ is the interaction energy, $k_{B}$ is the Boltzmann constant, and $T$ is the temperature.


<table>
  <thead>
    <tr>
      <th colspan="3">Interaction energies for the Runt-related cooperativity parameters</th>
    </tr>
    <tr>
      <th>model parameter</th>
      <th>construct</th>
      <th>interaction energy (KBT)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Runt-RNAP interaction,ωr⁢p</td>
      <td>[001]</td>
      <td>2.34 ± 0.63</td>
    </tr>
    <tr>
      <td>[010]</td>
      <td>1.36 ± 0.36</td>
    </tr>
    <tr>
      <td>[100]</td>
      <td>0.18 ± 0.24</td>
    </tr>
    <tr>
      <td rowspan="3">Runt-Runt interaction,ωr⁢r</td>
      <td>[011]</td>
      <td>0 (manually set)</td>
    </tr>
    <tr>
      <td>[110]</td>
      <td>-0.95 ± 0.12</td>
    </tr>
    <tr>
      <td>[101]</td>
      <td>0 (manually set)</td>
    </tr>
    <tr>
      <td rowspan="3">Runt-Runt-RNAP interaction,ωr⁢r⁢p</td>
      <td>[011]</td>
      <td>-2.09 ± 0.27</td>
    </tr>
    <tr>
      <td>[110]</td>
      <td>4.15 ± 1.14</td>
    </tr>
    <tr>
      <td>[101]</td>
      <td>1.12 ± 0.51</td>
    </tr>
    <tr>
      <td>Runt-Runt-Runt-RNAP interaction,ωr⁢r⁢r⁢p</td>
      <td>[111]</td>
      <td>-2.12 ± 0.14</td>
    </tr>
  </tbody>
</table>

While we have long known about protein-protein cooperative interactions (Ackers et al., 1982), in the last few years it has become clear that higher-order cooperativity can also be at play in eukaryotic systems (Estrada et al., 2016a; Park et al., 2019; Biddle et al., 2020) as well as in bacteria (Dodd et al., 2004) and archaea (Peeters et al., 2013). The existence of this higher-order cooperativity suggests that, to predict gene expression from DNA sequence, it might be necessary to build an understanding of the many simultaneous interactions that precede transcriptional initiation. Our discovery of higher-order cooperativity in the action of multiple Runt molecules opens up new avenues to uncover the molecular nature of this phenomenon. For example, following an approach developed in Park et al., 2019, it could be possible to determine whether and how these cooperativity parameters are modulated upon perturbation of molecular players such as the Groucho or CtBP co-repressors, Big-brother, a co-factor facilitating the Runt binding to DNA, and components of the mediator complex (Park et al., 2019; Courey and Jia, 2001; Walrad et al., 2011). Indeed, Park et al., 2019 recently showed that co-activators and mediator units are involved in dictating the magnitude of similar higher-order cooperativity terms in activation by Bicoid. Thus, our thermodynamic models provide a lens through which to dissect the molecular underpinnings of Runt interactions with itself and with the transcriptional machinery.

Notably, the need to invoke cooperative interactions as more Runt binding sites are being added opposes our goal of predicting complex regulatory architectures from experiments with simpler architectures without the need to invoke new parameters. However, it will be interesting to determine whether more parameters need to be invoked as the number of Runt binding sites increases beyond three, or whether the parameters already inferred are sufficient to endow our models with parameter-free predictive power.

Importantly, while our model adopted a ‘direct repression’ view of the mechanism of Runt action, other mechanisms of repression such as ‘quenching’ could also describe the data. While all such models call for higher-order cooperativity to describe the data (Supplementary Section ‘Comparison of different modes of repression’), our data cannot differentiate among those models. Thus, we did not attempt to distinguish different molecular mechanisms of Runt transcriptional repression.

Finally, even though the work presented here has relied exclusively on thermodynamic models, it is important to note that a much more general approach based on kinetic models that are not in thermodynamic equilibrium could also be appropriate for describing our data. Indeed, an increasing body of work over the last few years has provided evidence for the necessity of invoking these more complex models in the context of transcriptional regulation in eukaryotes (Estrada et al., 2016a; Li et al., 2018; Park et al., 2019; Eck et al., 2020). In future work, it will be interesting to determine whether, when our data is viewed through the lens of these non-equilibrium models, invoking higher-order cooperativity is still necessary or whether, instead, simple pairwise protein-protein interactions suffice to reach an agreement between theory and experiment.

Overall, the work presented here establishes a framework for systematically and quantitatively studying repression in the early fly embryo. As showcased here, synthetic enhancers based on the hunchback P2 minimal enhancer constitute an ideal scaffold for the study of other repressors in early fly embryos. For example, we envision that this approach could be used to dissect repression by other transcription factors such as Capicua or Krüppel (Löhr et al., 2009; Sauer and Jäckle, 1991; Papagianni et al., 2018; Chen et al., 2012), and to probe observations of multiple repressors working together to oppose activation by Bicoid in establishing gene expression patterns along the anterior-posterior axis (Chen et al., 2012; Briscoe and Small, 2015). We anticipate that a similar approach could be used to dissect repression along the dorso-ventral axis of the embryo, by for example, adding repressor binding sites to well-established reporter constructs that are only regulated by the Dorsal activator (Jiang and Levine, 1993). Critically, we need to understand not only how one species of repressor works in concert with an activator, but also how multiple species of repressors work together as a system. The approach presented here provides a way forward for predictively understanding the complex gene regulatory network that shapes gene expression patterns in the early fly embryo.

## Materials and methods

### Generation of synthetic enhancers with MS2 reporter

The synthetic enhancer constructs used in this study are based off of Chen et al., 2012. In summary, the hunchback P2 enhancer was used as a scaffold to introduce Runt binding sites at different positions that are thought to be neutral (i.e. these Runt binding sites do not interfere with any other obvious binding sites for other transcription factors in the early Drosophila embryos as shown in Figure 4—figure supplement 1). For the three positions chosen to introduce Runt binding sites in Chen et al., 2012, the Gene Synthesis service from Genscript was used to generate synthetic enhancers with all possible configurations of zero-, one-, two-, and three-Runt binding sites in hunchback P2 as shown in Figure 1A. The enhancer sequences were placed into the original plasmid pIB backbone (Chen et al., 2012) using the Gene Fragment Synthesis service in Genscript, followed by the even-skipped promoter, and 24 repeats of the MS2v5 loop (Wu et al., 2015), the lacZ coding sequence, and the $\alpha$-Tubulin 3’UTR sequence (Chen et al., 2012) as shown in Table 2. These plasmids were injected into the 38F1 landing site using the RMCE method (Bateman et al., 2006) by BestGene Inc Flies were screened by selecting for white eye color and made homozygous. The orientation of the insertion was determined by genomic PCR to ensure a consistent orientation across all of our constructs. Specifically, we used two sets of primers that each amplified one of these two possible orientations: ‘Upward’, where the forward primer binds to a genomic location outside of 38F1 (TTCTAGTTCCAGTGAAATCCAAGCA) and the reverse primer binds to a location in our reporter transgene (ACGCCAGGGTTTTCCCAG), and ‘Downward’, where the forward primer remains the same as the ‘Upward’ set and the reverse primer binds to a location in our reporter transgene (CTCTGTTCTCGCTATTATTCCAACC) when the insertion is the opposite orientation to the ‘Upward’ orientation. As a result, only amplicons from either one of the orientations of insertion in the 38F1 landing site can be obtained. We chose the ‘Downward’ orientation for all our constructs.

**Table 2.**
 List of plasmids used to create the transgenic fly lines used in this study.


<table>
  <thead>
    <tr>
      <th colspan="2">Plasmids</th>
    </tr>
    <tr>
      <th>Name (hyperlinked to Benchling)</th>
      <th>Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pIB-hbP2-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[000]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pIB-hbP2+r1-far-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[100]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pIB-hbP2+r1-mid-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[010]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pIB-hbP2+r1-close-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[001]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pIB-hbP2+r2-2+3-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[011]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pIB-hbP2+r2-1+3-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[101]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pIB-hbP2+r2-1+2-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[110]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pIB-hbP2+r3-evePr-MS2v5-LacZ-Tub3UTR</td>
      <td>[111]-MS2v5 reporter construct</td>
    </tr>
    <tr>
      <td>pHD-scarless-LlamaTag-Runt</td>
      <td>Donor plasmid for LlamaTag-Runt CRISPR knock-in fusion for the N-terminal</td>
    </tr>
    <tr>
      <td>pU6:3-gRNA(Runt-N-2)</td>
      <td>gRNA plasmid for LlamaTag-Runt CRISPR knock-in fusion for the N-terminal</td>
    </tr>
    <tr>
      <td>pCasper-vasa-eGFP</td>
      <td>vasa maternal driver for ubiquitous eGFP expression in the early embryo</td>
    </tr>
  </tbody>
</table>

### CRISPR-Cas9 knock-in of the green LlamaTag in the endogenous runt locus

We used CRISPR-Cas9 mediated Homology Directed Repair (HDR) to insert the LlamaTag against eGFP into the N-terminal of the runt endogenous locus (Bothma et al., 2018; Gratz et al., 2015). The donor plasmid was constructed by stitching individual fragments—PCR amplified left/right homology arms from the endogenous runt locus roughly 1 kb in length each, LlamaTag, and pHD-scarless vector—using Gibson assembly (Gratz et al., 2015). The PAM sites in the donor plasmid were mutated such that the Cas9 only cleaved the endogenous locus, not the donor plasmid, without changing the amino acid sequence of the Runt protein. The final donor plasmid contained the 3xP3-dsRed marker such that dsRed is expressed in the fly eye and ocelli for screening. Positive transformant flies were screened using a fluorescence dissection scope and set up for single fly crosses to establish individual lines that were then verified with PCR amplification and Sanger sequencing (UC Berkeley Sequencing Facility). Importantly, this llamaTag-runt allele rescues development to adulthood as a homozygous. Thus we concluded that the LlamaTag-Runt allele can be used to monitor the behavior of endogenous Runt protein.

### Fly strains

Transcription from the synthetic enhancer reporter constructs was measured by using embryos from crossing yw;his2av-mRFP1;MCP-eGFP(2) females and yw;synthetic enhancer-MS2v5-lacZ;+ males as described in Garcia et al., 2013; Eck et al., 2020; Lammers et al., 2020.

eGFP-Bicoid measurements were performed using the fly line from Gregor et al., 2007. The LlamaTag-Runt measurements were done using the fly line LlamaTag-Runt; +; vasa-eGFP, His2Av-iRFP illustrated in Table 3. Briefly, eGFP was supplied by a vasa maternal driver. Females carrying both the LlamaTag-Runt and the vasa-driven eGFP were crossed with males carrying the LlamaTag-Runt, the progeny from this cross were imaged and then recovered to determine the embryo’s sex using PCR. PCR was run with three sets of primers: Y chr1 (Forward: CGATCCAGCCCAATCTCTCATATCACTA, Reverse: ATCGTCGGTAATGTGTCCTCCGTAATTT), Y chr2 (Forward: AACGTAACCTAGTCGGATTGCAAATGGT, Reverse: GAGGCGTACAATTTCCTTTCTCATGTCA), and Auto1 (Forward: GATTCGATGCACACTCACATTCTTCTCC, Reverse: GCTCAGCGCGAAACTAACATGAAAAACT). Two of primers in the set (Y chr1 and Y chr2) bind to the Y chromosome while the other one (Auto1) binds to one of the autosomes and constitutes a positive control (Lott et al., 2011). The Histone-iRFP fly line was from Pan et al., 2022, and was used for nuclei segmentation to extract nuclear flourescence from the eGFP channel.

**Table 3.**
 List of fly lines used in this study and their experimental usage.


<table>
  <thead>
    <tr>
      <th colspan="2">Fly lines</th>
    </tr>
    <tr>
      <th>Genotype</th>
      <th>Use</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LlamaTag-Runt; +; vasa-eGFP, His2Av-iRFP</td>
      <td>Visualize LlamaTagged Runt protein and label nuclei</td>
    </tr>
    <tr>
      <td>LlamaTag-Runt; +; MCP-eGFP(4F), His2Av-iRFP</td>
      <td>Visualize LlamaTagged Runt protein, nascent transcripts and label nuclei</td>
    </tr>
    <tr>
      <td>run3/FM6; +; +</td>
      <td>Visualize LlamaTagged Runt protein, nascent transcripts and label nuclei</td>
    </tr>
    <tr>
      <td>yw; His2Av-mRFP; MCP-eGFP</td>
      <td>Females to label nascent RNA and nuclei</td>
    </tr>
    <tr>
      <td>yw; [000]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
    <tr>
      <td>yw; [100]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
    <tr>
      <td>yw; [010]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
    <tr>
      <td>yw; [001]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
    <tr>
      <td>yw; [011]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
    <tr>
      <td>yw; [101]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
    <tr>
      <td>yw; [110]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
    <tr>
      <td>yw; [111]-MS2v5; +</td>
      <td>Males carrying the MS2 reporter transgene</td>
    </tr>
  </tbody>
</table>

To generate the embryos that are zygotic null for the runt allele, we used a fly cross scheme consisting of two crosses. In the first generation, we crossed LlamaTag-Runt;+;+ males with run3/FM6;+;MCP-eGFP(4 F),his2av-mRFP1 females. run3 is the null allele for runt, missing around 5 kb including the coding sequence of the runt locus (Gergen and Butler, 1988; Chen et al., 2012). The MCP-eGFP(4 F) transgene expresses approximately twice the amount of MCP protein than the MCP-eGFP(2) (Garcia et al., 2013; Eck et al., 2020) and thus results in similar levels of MCP to those of MCP-eGFP(2) in the trans-heterozygotes. The female progeny from this cross, LlamaTag-Runt/run3;+;MCP-eGFP(4 F),his2av-mRFP1/+ was then crossed with males whose genotype was LlamaTag-Runt/Y;synthetic enhancer-MS2v5-lacZ;+ to produce the embryos that we used for live imaging. The resulting embryos carried maternally supplied MCP-eGFP and His-RFP for visualization of nascent transcripts and nuclei. The X chromosome contained a LlamaTag-Runt allele or run3 null allele. We could differentiate between these two genotypes because, when the embryo had the Runt allele, a stripe pattern would appear in late nc14. We imaged all embryos until late nc14 to make sure that we were capturing the nulls.

### Sample preparation and data collection

Sample preparation was done following the protocols described in Garcia et al., 2013. Briefly, embryos were collected, dechorionated with bleach for 1–2 min, and then mounted between a semipermeable membrane (Lumox film, Starstedt, Germany) and a coverslip while embedded in Halocarbon 27 oil (Sigma-Aldrich). Live imaging was performed using a Leica SP8 scanning confocal microscope, a White Light Laser and HyD dectectors (Leica Microsystems, Biberach, Germany). Imaging settings for the MS2 experiments with the presence of MCP-eGFP and Histone-RFP were the same as in Eck et al., 2020 except that we used a 1024x245 pixel format to image a wider field of view along the anterior-posterior axis. The settings for the eGFP-Bicoid measurements were the same as described in Eck et al., 2020.

The settings for the eGFP:LlamaTag-Runt measurements were similar to that of eGFP-Bicoid except for the following. To increase our imaging throughput, we utilized the ‘Mark and Position’ functionality in the LASX software (Leica SP8) to image 5–6 embryos simultaneously. To account for the decreased time resolution, we lowered the z-stack size from 10 μm to 2.5 μm, keeping the 0.5 μm z-step. By doing this, we could maintain 1-min frame rate for each imaged embryo. Additionally, these flies expressed Histone-iRFP, instead of Histone-RFP as in Eck et al., 2020, so that we used a 670 nm laser at 40 μW (measured at a 10x objective) for excitation of the histone channel, and the HyD detector was set to a 680 nm-800 nm spectral window (Figure 3—figure supplement 7).

### Image analysis

Images were analyzed using custom-written software (MATLAB, mRNA Dynamics Github repository; Garcia Lab @ UC Berkeley, 2022) following the protocol in Garcia et al., 2013 and Eck et al., 2020. Briefly, this procedure involved segmentation and tracking of nuclei and transcription spots. First, segmentation and tracking of individual nuclei were done using the histone channel as a nuclear mask. Second, segmentation of each transcription spot was done based on its fluorescence intensity and existence over multiple z-stacks. The intensity of each MCP-GFP transcriptional spot was calculated by integrating pixel intensity values in a small window around the spot and subtracting the background fluorescence measured outside of the active transcriptional locus. When there was no detectable transcriptional activity, we assigned NaN values for the intensity. The tracking of transcriptional spots was done by using the nuclear tracking and proximity of transcriptional spots between consecutive time points. The nuclear protein fluorescence intensities from the eGFP-Bicoid and LlamaTag-Runt fly lines, which we use as a proxy for the protein nuclear concentration, were calculated as follows. Using the nuclear mask generated from the histone channel, we performed the same nuclear segmentation and tracking as described above for the MS2 spots. Then, for every z-section, we extracted the integrated fluorescence over a $2⁢\mu⁢m$ diameter circle on the xy-plane centered on each nucleus. For each nucleus, the recorded fluorescence corresponded to the z-position where the fluorescence was maximal. This resulted in an average nuclear concentration as a function of time for each single nucleus. These concentrations from individual nuclei were then averaged over a narrow spatial window (2.5% of the embryo length) to generate the spatially averaged protein concentration reported in the main text. For the eGFP:LlamaTag-Runt datasets, we had to subtract the background eGFP fluorescence due to the presence of an unbound eGFP population (Bothma et al., 2018). We used the same protocol described in Bothma et al., 2018 and in the Supplementary Section ‘Quantifying the nuclear concentration of LlamaTag-Runt’ to extract this background.

### Bayesian inference procedure: Markov Chain Monte Carlo sampling

Parameter inference was done using the Markov Chain Monte Carlo (MCMC) method. We used a well-established package MCMCstat that uses an adaptive MCMC algorithm (Haario et al., 2006; Haario et al., 2001). A detailed description on how we performed the MCMC parameter inference, for example setting the priors and bounds for parameters, can be found in Supplementary Section ‘Markov Chain Monte Carlo inference protocol’.

# Region of Attainable Redaction, an extension of Ellipse of Insignificance analysis for gauging impacts of data redaction in dichotomous outcome trials

## Authors

- David Robert Grimes<sup>1</sup> ([ORCID: 0000-0003-3140-3278](https://orcid.org/0000-0003-3140-3278)) †

### Affiliations

1. School of Medicine, Trinity College Dublin Dublin Ireland ([ROR:02tyrky19](https://ror.org/02tyrky19))
2. School of Physical Sciences, Dublin City University Dublin Ireland ([ROR:04a1a1e81](https://ror.org/04a1a1e81))

† Corresponding author

## Abstract

In biomedical science, it is a reality that many published results do not withstand deeper investigation, and there is growing concern over a replicability crisis in science. Recently, Ellipse of Insignificance (EOI) analysis was introduced as a tool to allow researchers to gauge the robustness of reported results in dichotomous outcome design trials, giving precise deterministic values for the degree of miscoding between events and non-events tolerable simultaneously in both control and experimental arms (Grimes, 2022). While this is useful for situations where potential miscoding might transpire, it does not account for situations where apparently significant findings might result from accidental or deliberate data redaction in either the control or experimental arms of an experiment, or from missing data or systematic redaction. To address these scenarios, we introduce Region of Attainable Redaction (ROAR), a tool that extends EOI analysis to account for situations of potential data redaction. This produces a bounded cubic curve rather than an ellipse, and we outline how this can be used to identify potential redaction through an approach analogous to EOI. Applications are illustrated, and source code, including a web-based implementation that performs EOI and ROAR analysis in tandem for dichotomous outcome trials is provided.

## Introduction

Despite the crucial importance of biomedical science for human well-being, the uncomfortable reality is that swathes of published results in fields from psychology to cancer research are less robust than optimum (Ioannidis, 2005; Krawczyk, 2015; Loken and Gelman, 2017; Grimes et al., 2018; Errington et al., 2021). In cases when findings are spurious, inappropriate or errant statistical methods are often the primary cause of untrustworthy research, from incorrect interpretations of p-values to unsuitable tests to data redaction and under-reporting of overtesting, leading to research waste and unsound conclusions (Hoffmann et al., 2013; Altman and Krzywinski, 2017; Colquhoun, 2014; Glasziou et al., 2014; Grimes and Heathers, 2021a; Itaya et al., 2022; Baer et al., 2021a; Baer et al., 2021b). Across biomedical sciences, dichotomous outcome trials and studies are of paramount importance, forming the basis of everything from preclinical observational studies to randomized controlled trials. Such investigations contrast experimental and control groups for a given intervention, comparing the numbers experiencing a particular event in both arms to infer whether differences between the intervention and control arm might exist.

Such investigations are vital, but concern has been raised over the fragility of many published works, where small amounts of recoding from event to non-event in experimental arms or vice versa in control arms can create an illusion of a relationship where none truly exists. In previous work by the author (Grimes, 2022), Ellipse of Insignificance (EOI) analysis was introduced as a refined fragility index capable of handling even huge data sets analytically with ease, considering both control and experimental arms simultaneously, which traditional fragility analysis cannot. EOI analysis is robust and analytical, suitable not only for Randomized Controlled Trial (RCT) analysis but for observational trials, cohort studies, and general preclinical work. Additionally, it also links the concept of fragility to test sensitivity and specificity when these are known for the detection of events, enabling investigators to probe not only whether a result is arbitrarily fragile, but to truly probe whether consider certain results are even possible. Accordingly, it yields both objective metrics for fragility and can be employed to detect inappropriate manipulation of results if the statistical properties of the tests used are known. A web implementation of this is available at https://drg85.shinyapps.io/EOIanalysis/, replete with code in $R$ and other popular languages for general application.

While EOI analysis is a powerful method for ascertaining trial robustness, it does not explicitly consider the scenario where data is redacted. Data redaction in biomedical science creates spurious results and untrustworthy findings (Grimes and Heathers, 2021b), and can be difficult to detect. Data redaction can be accidental due to some systematic error in analysis, due to missing data, or arise through deliberate cherry-picking, and there are currently few tools for gauging its likely impact outside of direct simulation. In this technical note, we unveil a novel and powerful method for quantifying how much redaction would be required to explain a seemingly significant finding in dichotomous outcome trials, automatically finding the degree of redaction required to yield spurious results, and objective metrics for defining this. While EOI analysis produced a conic section in the form of an inclined ellipse where significance disappeared, this new tool instead produces a bounded region where significance disappears attainable by redaction and calculates the minimal vector to this regions. This technical note outlines the methodology of Region of Attainable Redaction (ROAR) analysis, including examples, R and MATLAB code for user implementations, and a web implementation for ease of deployability.

## Methods

The underlying geometrical and statistical basis for EOI analysis has been previously derived and described. In brief, EOI arises from chi-squared analysis, ascertaining how many participants in experimental and control groups could be recoded from events to non-events and vice versa before apparently significance was lost. This is a powerful approach for determining robustness of outcomes, and a web implementation and code are available at https://drg85.shinyapps.io/EOIanalysis/. EOI in its current form, however, does not consider the situation where a significant result might be obtained by data redaction, where an experimenter censors or neglects observations in the final analysis.

Defining $a$ as the reported data of endpoint positive cases in the experimental or exposure arm, $b$ as the reported experimental endpoint negative, $c$ as reported endpoint positive cases in the control arm, and $d$ as the reported endpoint negative cases in the control arm, we may define $x$ and $y$ as hypothetical redacted data in the experimental and control arm, respectively. We further define the total reported sample as $n=a+b+c+d$. To account for the impact of redaction, consider that an experimenter may obtain a significant result in favour of the experimental group in several ways. When relative risk is given by $\frac{a(c+d)}{c(a+b)}$ with no significant difference, the experimental arm could still yield a greater relative risk ($RR_{E}>1$) than the control arm if either $x$ endpoint negative events had been jettisoned from the experimental arm, $y$ endpoint positive events jettisoned from the control or comparison arm, or a combination of both. Equally, if there is no significant difference but a lower relative risk in the experimental group is sought ($RR_{E}<1$), such a finding can be manipulated by either jettisoning $x$ endpoint positive cases from the experimental arm, $y$ endpoint negative cases from the control arm, or a combination of both. These situations are given in Table 1. Risk ratio is used in this work for simplicity in gauging the relative impact of an ostensibly significant effect in the experimental arm and can be readily converted to odds ratio if preferred.

**Table 1.**
 Reported groups and related variables.


<table>
  <thead>
    <tr>
      <th colspan="3">Redaction for RRe&gt;1</th>
    </tr>
    <tr>
      <th></th>
      <th>Endpoint positive</th>
      <th>Endpoint negative</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Experimental group</td>
      <td>a</td>
      <td>b+x</td>
    </tr>
    <tr>
      <td>Control group</td>
      <td>c+y</td>
      <td>d</td>
    </tr>
    <tr>
      <td colspan="3">Redaction for RRe&lt;1</td>
    </tr>
    <tr>
      <td></td>
      <td>Endpoint positive</td>
      <td>Endpoint negative</td>
    </tr>
    <tr>
      <td>Experimental group</td>
      <td>a+x</td>
      <td>b</td>
    </tr>
    <tr>
      <td>Control group</td>
      <td>c</td>
      <td>d+y</td>
    </tr>
  </tbody>
</table>

Applying the chi-square statistic outlined previously with a threshold critical value for significance of $ν_{c}$, the resulting identity when $RR_{E}>1$ is

$$
\frac{(n+x+y)(ad−(b+x)(c+y))^{2}}{(a+b+x)(c+d+y)(a+c+y)(b+d+x)}−ν_{c}=0
$$

and when $RR_{E}<1$, the identity is

$$
\frac{(n+x+y)((a+x)(d+y)−bc)^{2}}{(a+b+x)(c+d+y)(a+c+x)(b+d+y)}−ν_{c}=0
$$

Similar to EOI analysis, these forms can be expanded. However, the resultant equations in either case are not the conic sections of an inclined ellipse as with EOI analysis, but a more complicated cubic curve also in two variables. The resultant identity is $g(x,y)$, polynomial in $x$ and $y$, with the list of 15 coefficients in either case in given in the mathematical appendix (Supplementary file 1, Table S1). The region bound by this equation is the ROAR, and any $g(x,y)\leq0$ changes an ostensibly significant finding to the null one, with $x$ and $y$ respectively yielding the redaction from the experimental and control group required.

### ROAR derivation and FOCK vector

In EOI analysis, we derived an analytical method for finding the minimum distance from the origin to the EOI. This point and vector, the Fewest Experimental/Control Knowingly Uncoded Participants (FECKUP) vector, allowed us to ascertain the minimal error which would render results insignificant. The resultant curve and bound region are inherently more complex in ROAR analysis, but the general principle remains. We seek the minimum distance from the origin to the region bound by $g(x,y)=0$, defining the vector to this point $(x_{e},y_{e})$ as the Fewest Observations/Censored Knowledge (FOCK) vector. Unlike EOI analysis, we cannot exploit geometric arguments to solve this analytically, and instead we proceed by the method of Lagrange multipliers. The minimum distance from the origin to a point is given by

$$
D(x,y)=\sqrt{x^{2}+y^{2}}
$$

Defining the polynomial defined in Supplementary file 1, Table S1 as $g(x,y)$, we can exploit the properties of Lagrange multipliers to write

$$
\frac{∂D}{∂x}=\lambda\frac{∂g}{∂x}
$$



$$
\frac{∂D}{∂y}=\lambda\frac{∂g}{∂y}.
$$

As we know $\lambda\neq0$, we can rearrange these equations for the constant scalar $\lambda$ and equate them, subject to the constraint $g(x,y)=0$. After rearrangement, we deduce that

$$
y\frac{∂g}{∂x}−x\frac{∂g}{∂y}=0.
$$

This yields another unwieldy polynomial in two variables with 18 coefficients, listed in the mathematical appendix (Supplementary file 1, Table S2) for both cases. If we define the resultant function as $h(x,y)$, we seek to solve the simultaneous equations

$$
g(x_{e},y_{e})=0
$$



$$
h(x_{e},y_{e})=0.
$$

While analytical solutions are likely intractable, this can be readily solved numerically subject to the constraints that $x_{e}>0$ and $y_{e}>0$. By Bézout’s theorem, there are potentially up to 25 solutions to this simultaneous equation, so we restrict potential solution pairs to the real domain and select the pair yielding the minimum length FOCK vector, corresponding to ($x_{e}.y_{e}$) as illustrated in Figure 1. Additionally, we solve $g(x_{c},0)=0$ and $g(0,y_{c})=0$ as simple cubic equations to find the minimum number of observations redacted in exclusively the experimental and control groups to lose significance. The resolution of the FOCK vector yields the minimum redacted combination of experimental and control groups, given by

$$
r_{min}=⌊x_{e}+y_{e}⌋.
$$

![Figure 1.](https://cdn.elifesciences.org/articles/93050/elife-93050-fig1-v2.jpg)

**Figure 1.:** (a) A simulated example of the Region of Attainable Redaction (ROAR) for $a=70$, $b=30$, $c=50$, $d=50$ ($RR_{E}>1$) with all points bounded by the shaded region depict a degree of redaction which would not lead to the null being rejected. (b) Relevant vectors for ascertaining possible redaction thresholds in $RR_{E}>1$ case. (c) ROAR analysis of the similar data but with ($RR_{E}<1$) ($a=50$, $b=50$, $c=70$, $d=30$). Note that $RR_{E}>1$ case is a transform of $RR_{E}<1$ situation. (d) Relevant vectors for ascertaining possible redaction thresholds in case $RR_{e}<1$.

### Metrics for degree of potential redaction

In EOI analysis, we established objective metrics to characterize the degree of potential miscoding required to sustain the null hypothesis. In this technical note, we establish analogous parameters. Considering only potential redaction in the experimental group, we define the degree of potential redaction that can be sustained while the null hypothesis remains rejected, given by

$$
ρ_{E}=1−\frac{a+b}{a+b+x_{c}}.
$$

For example, a ROAR analysis with $ρ_{E}=0.1$ would inform us that at least 10% of experimental participants would have to be redacted for the result to lose significance. By similar reasoning, the tolerance threshold for error allowable in the control group is then

$$
ρ_{C}=1−\frac{c+d}{c+d+y_{c}}.
$$

Finally, errors in both the coding of the experimental and control group can be combined with FECKUP point knowledge. While $f_{min}$ gives a minimum vector distance to the ellipse, we instead take the length of the vector components to reflect to yield an absolute accuracy threshold of

$$
ρ_{A}=1−\frac{n}{n+r_{min}}.
$$

Unlike the EOI case, there is no direct relationship between test sensitivity/specificity and potential redaction.

### Application to large data sets and meta-analyses

ROAR is also highly effective with large data sets, and with certain caveats can be applied to even meta-analyses results. For a meta-analyses of $i$ dichotomous outcome trials, the crude pool risk ratio is given by

$$
RR_{C}=\frac{\sum1ia_{i}\sum1i(c_{i}+d_{i})}{\sum1ic_{i}\sum1i(a_{i}+b_{i})}
$$

whereas the Cochran–Mantel–Haenszel adjusted risk ratio accounts for potential confounding between studies and adjusts for sample size, given by

$$
RR_{CMH}=\frac{\sum1i\frac{a_{i}(c_{i}+d_{i})}{n_{i}}}{\sum1i\frac{c_{i}(a_{i}+b_{i})}{n_{i}}}.
$$

The magnitude of confounding between studies is given by $|1−\frac{RR_{CMH}}{RR_{C}}|$. If this is small (typically <10%), confounding can be assumed minimal and the crude ratio used, allowing ROAR to be deployed directly on pooled meta-analyses results if these conditions are met. When confounding is significant between studies, direct ROAR is not applicable and these caveats are expanded upon in discussion.

## Results

### Example deployment and ROAR behaviour

To demonstrate the usage of ROAR, we consider a simple twin example with the following arrangement of data.

**Table 2.**
 ROAR-derived metrics for published data (see ‘Results’ for details).


<table>
  <thead>
    <tr>
      <th colspan="3">Statistics for simulated example case</th>
    </tr>
    <tr>
      <th>ROAR statistic (α=0.05)</th>
      <th>Calculated ROAR value (simulated RRE&gt;1 data)</th>
      <th>Calculated ROAR value (simulated RRE&lt;1 data)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total subjects reported N</td>
      <td>200</td>
      <td>200</td>
    </tr>
    <tr>
      <td>Relative risk (95% CI) RRE</td>
      <td>1.40 (1.11–1.77)</td>
      <td>0.60 (0.46–0.76)</td>
    </tr>
    <tr>
      <td>FOCK point</td>
      <td>(xe,ye)=(6.89,4.79)</td>
      <td>(xe,ye)=(4.79,6.89)</td>
    </tr>
    <tr>
      <td>rmin</td>
      <td>12 subjects</td>
      <td>12 subjects</td>
    </tr>
    <tr>
      <td>Experimental redaction tolerance ρE</td>
      <td>9.51% (⌈xc⌉ = 10 subjects)</td>
      <td>14.32% (⌈xc⌉ = 14 subjects)</td>
    </tr>
    <tr>
      <td>Control redaction tolerance ρC</td>
      <td>14.32% (⌈yc⌉ = 16 subjects)</td>
      <td>9.51% (⌈yc⌉ = 10 subjects)</td>
    </tr>
    <tr>
      <td>Total redaction tolerance ρA</td>
      <td>5.66% (12 subjects)</td>
      <td>5.66% (12 subjects)</td>
    </tr>
    <tr>
      <td colspan="3">Statistics for large meta-analysis</td>
    </tr>
    <tr>
      <td>ROAR statistic (α=0.05)</td>
      <td>Calculated ROAR value</td>
      <td></td>
    </tr>
    <tr>
      <td>Total subjects reported N</td>
      <td>39,197</td>
      <td></td>
    </tr>
    <tr>
      <td>Relative risk (95% CI)</td>
      <td>0.85 (0.74–0.97)</td>
      <td></td>
    </tr>
    <tr>
      <td>FOCK point</td>
      <td>(xe,ye)=(14.17,0.32)</td>
      <td></td>
    </tr>
    <tr>
      <td>rmin</td>
      <td>14 subjects</td>
      <td></td>
    </tr>
    <tr>
      <td>Experimental redaction tolerance ρE</td>
      <td>0.07% (13 subjects)</td>
      <td></td>
    </tr>
    <tr>
      <td>Control redaction tolerance ρC</td>
      <td>3.21% (649 subjects)</td>
      <td></td>
    </tr>
    <tr>
      <td>Total redaction tolerance ρA</td>
      <td colspan="2">0.04% (14 subjects)</td>
    </tr>
  </tbody>
</table>

_FOCK, Fewest Observations/Censored Knowledge; ROAR, Region of Attainable Redaction._

As can be seen from Figure 1, the cases $RR_{E}>1$ and $RR_{E}<1$ are essentially geometrical rotations and reflections of one another, with $r_{min}$ the same in both the values of $ρ_{E}$ and $ρ_{C}$ being transposed on reflection, as it evident from Table 2. This showcases the general behaviour of ROAR analysis, and in this example, it would require a redaction of between 10 and 16 subjects to lose apparent significance in either case, requiring at least 5.66% of the total subjects to have been redacted. Note that the real values of $x_{e}$ and $y_{e}$ are employed in calculating $ρ_{E}$ and $ρ_{C}$, whereas the integer value $r_{min}$ is used in $ρ_{A}$. For $x_{c}$ and $y_{c}$, integer ceiling values yield the greatest possible redaction.

### Application to large data sets and meta-analyses

We consider a published meta-analysis of vitamin D supplementation on cancer mortality (Zhang et al., 2019), comprising of $N=39,197$ patients from five RCTs, with $a=397$ deaths in the experimental group (supplementation) versus $b=19,204$ non-deaths and $c=468$ deaths in the control group versus $d=19,128$ non-deaths. Although the authors did not see reduction in all-cause mortality, subanalysis for the cancer population yielded an odds ratio of 0.85 (95% confidence interval: 0.74–0.97 for supplementation), reporting an ≈ 15% reduction in cancer mortality risk. With $RR_{C}=0.8481$, $RR_{CMH}=0.8474$, the magnitude of confounding is < 0.09% and thus we can apply ROAR to the pooled data. In this case, ROAR is illustrated in Figure 2, and the degree of redaction required is given in Table 2. Despite the ostensible strength of the result and large sample size, redaction of a mere 14 subjects (0.036%) or a small fraction of missing data would be sufficient to nullify the apparent finding, despite it stemming from a large meta-analysis.

![Figure 2.](https://cdn.elifesciences.org/articles/93050/elife-93050-fig2-v2.jpg)

**Figure 2.:** (a) A simulated example of the Region of Attainable Redaction (ROAR) for a meta-analysis of $N=39,197$ as described in the text. (b) Relevant vectors for ascertaining possible redaction thresholds.

### Browser-based implementation and source code

A browser-based implementation combining both EOI and ROAR is hosted at https://drg85.shinyapps.io/EOIROAR/, and relevant source code is hosted online for languages including $R$, MATLAB/OCTAVE, and Mathematica at https://github.com/drg85/EOIROAR_code, copy archieved at Grimes, 2023.

## Discussion

ROAR analysis outlined in this technical note extends the functionality and usefulness of EOI analysis, allowing users to estimate the likely impacts of missing data. EOI analysis and related fragility methods had the limitations that while they handled potential miscoding, they were unsuitable for inferences or quantification of impacts of redacted data or subjects lost to follow-up. Accordingly, ROAR is a powerful method of gauging the potential impacts of missing data. While more mathematically complex than EOI analysis, ROAR remains deterministic and rapid, but shares the limitation that it is only currently applicable to dichotomous outcome trials and studies, and should be applied very cautiously to time-to-event data, where it may not be suitable. Like EOI analysis, ROAR differs from typical fragility metrics by avoiding Fisher’s exact test as this is not suitable for large data sets which EOI and ROAR can readily handle. This is typically not a problem as the chi-squared test employed approximates Fisher’s test in most circumstances. However, like EOI analysis, p-values for small trials can differ slightly from chi-squared result. ROAR analysis is built upon chi-squared statistics, and it is thus possible for edge cases of small numbers to yield discordant results with Fisher’s exact test also. This can be shown from a theoretical standpoint to not typically make any appreciable difference except for rare events in very small trials (Grimes, 2022; Baer et al., 2021a).

Application of ROAR analysis is inherently context specific. For clinical trials, preregistration in principle reduces the potential for experimenter choices like redaction bias changing the outcome. But the implementation of preregistered protocols does not exclude the possibility of data dredging in the form of p-hacking or HARKing (hypothesizing after the results are known). Researchers rarely follow the precise methods, plan, and analyses that they preregistered. A recent analysis found that pre-registered studies, despite having power analysis and higher sample size than non-registered studies, do not a priori seem to prevent p-hacking and HARKing (Bakker et al., 2020; Singh et al., 2021; El‐Boghdadly et al., 2018; Sun et al., 2019), with similar proportions of positive results and effect sizes between preregistered and non-preregistered studies (van den Akker et al., 2023). A survey of 27 preregistered studies found researchers deviating from preregistered plans in all cases, most frequently in relation to planned sample size and exclusion criteria (Claesen et al., 2021). This latter aspect lends itself to potential redaction bias (Grimes and Heathers, 2021b), which can be systematic rather than deliberate and thus a means to quantify its impact is important. More importantly, EOI analysis has application for dichotomous beyond clinical trials. In preclinical work, cohort, and observational studies, the scope for redaction bias greatly increases as reporting and selection of data falls entirely on the experimenter, and thus methods like ROAR to probe potential redaction bias are important. ROAR also has potential application in case–control studies, where selection of an inappropriately fragile control group could give spurious conclusions. This again comes with caveats as studies adjusted for potential confounders and predictors might make ROAR inappropriate in such cases.

As demonstrated in this work, ROAR is under certain circumstances applicable even to large meta-analysis. In this instance, a potential redaction of just 14 subjects from over 39,000 was sufficient to overturn the null hypothesis, despite a relative risk reduction of 15% being widely reported on the basis of this meta-analysis. This of course is not to say that any redaction occurred only to quantify the vulnerability of such a study to missing data. While beyond the scope of this technical note, it is worth noting that a subsequent 2022 meta-analysis (Zhang et al., 2022) of 11 RCTS (including those in the 2019 [Zhang et al., 2019] meta-analysis) found no significant reduction in cancer mortality with vitamin D supplementation, a potential testament to the need to consider the fragility of results to missing or miscoded data, even with ostensibly large samples. There are however important caveats to applying ROAR to meta-analyses. In its naive form, it is only suitable when there is minimal confounding between studies so that the crude relative risk differs minimally from the adjust risk ($RR_{C}≈RR_{CMH}$), such as in the illustrative work considered herein. When this is not the case, results from individual studies cannot be crudely pooled and ROAR is not valid in these instances. As ROAR applied to meta-analyses pools studies into a simple crude measure, it does not identity the particular study or studies where hypothetical redaction might have occurred, only the global fragility metric. A full theoretical extension of ROAR and EOI for specifically for meta-analyses is beyond the scope of this work, and accordingly, ROAR must be cautiously implemented and carefully interpreted in investigations of meta-analyses.

As discussed in the EOI paper (Grimes, 2022), poor research conduct including inappropriate statistical manipulation and data redaction are not uncommon, affecting up to three quarters of all biomedical science (Fanelli, 2009). Like EOI analysis, the ROAR extension has a potential role in detecting manipulations that nudge results towards significance, and identifying inconsistencies in data and adding invaluable context. It is a demonstrable reality that even seemingly strong results can falter under inspection, and tools like ROAR and EOI analysis have a potentially important role in identifying weak results and statistical inconsistencies, with wide potential application across meta-research with the goal of furthering sustainable, reproducible research.

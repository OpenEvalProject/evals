# Design principles of autocatalytic cycles constrain enzyme kinetics and force low substrate saturation at flux branch points

## Authors

- Uri Barenholz<sup>1</sup> ([ORCID: 0000-0002-3097-9681](https://orcid.org/0000-0002-3097-9681)) †
- Dan Davidi<sup>1</sup>
- Ed Reznik<sup>2</sup> ([ORCID: 0000-0002-6511-5947](https://orcid.org/0000-0002-6511-5947))
- Yinon Bar-On<sup>1</sup>
- Niv Antonovsky<sup>1</sup>
- Elad Noor<sup>4</sup>
- Ron Milo<sup>1</sup> ([ORCID: 0000-0003-1641-2299](https://orcid.org/0000-0003-1641-2299)) †

### Affiliations

1. Department of Plant and Environmental Sciences The Weizmann Institute of Science Rehovot Israel
2. Computational Biology Program Memorial Sloan Kettering Cancer Center New York United States
3. Center for Molecular Oncology Memorial Sloan Kettering Cancer Center New York United States
4. Institute of Molecular Systems Biology ETH Zurich Zurich Switzerland

† Corresponding author

## Abstract

10.7554/eLife.20667.001 A set of chemical reactions that require a metabolite to synthesize more of that metabolite is an autocatalytic cycle. Here, we show that most of the reactions in the core of central carbon metabolism are part of compact autocatalytic cycles. Such metabolic designs must meet specific conditions to support stable fluxes, hence avoiding depletion of intermediate metabolites. As such, they are subjected to constraints that may seem counter-intuitive: the enzymes of branch reactions out of the cycle must be overexpressed and the affinity of these enzymes to their substrates must be relatively weak. We use recent quantitative proteomics and fluxomics measurements to show that the above conditions hold for functioning cycles in central carbon metabolism of E. coli . This work demonstrates that the topology of a metabolic network can shape kinetic parameters of enzymes and lead to seemingly wasteful enzyme usage. DOI: http://dx.doi.org/10.7554/eLife.20667.001

## Introduction

An essential trait of living systems is their ability to reproduce. This fundamental ability makes all living organisms autocatalytic by definition. Moreover, autocatalytic metabolism is considered to be one of the essential components of life (Ganti et al., 2003).

In this work, we focus on autocatalytic cycles in chemical reaction systems, in the context of metabolic networks. The components we consider are the metabolites of the system, with autocatalytic cycles being formed using the reactions of the metabolic network. An illustrative example for a metabolic autocatalytic cycle is glycolysis. In glycolysis, 2 ATP molecules are consumed in the priming phase, in order to produce 4 ATP molecules in the pay off phase. Therefore, in order to produce ATP in glycolysis, ATP must already be present in the cell. Subsequently, autocatalysis of ATP in glycolysis (also referred to as ‘turbo design’) results in sensitivity to mutations in seemingly irrelevant enzymes (Teusink et al., 1998). Autocatalytic cycles have also been shown to be optimal network topologies that minimize the number of reactions needed for the production of precursor molecules from different nutrient sources (Riehl et al., 2010).

Metabolic networks often require the availability of certain intermediate metabolites, in addition to the nutrients consumed, in order to function. Examples of obligatorily autocatalytic internal metabolites in different organisms, on top of ATP, are NADH, and coenzyme A (Kun et al., 2008). We find that other central metabolites, such as phospho-sugars and organic acids, are autocatalytic under common growth conditions. The requirement for availability of certain metabolites in order to consume nutrients implies metabolic processes must be finely controlled to prevent such essential metabolites from running out; in such cases metabolism will come to a halt. Autocatalytic cycles present control challenges because the inherent feed-back nature of autocatalytic cycles makes them susceptible to instabilities such as divergence or drainage of their intermediate metabolites (Teusink et al., 1998; Fell et al., 1999; Reznik and Segrè, 2010). The stability criteria typically represent one constraint among the parameters of the cycle enzymes. For large cycles, such as the whole metabolic network, one such constraint adds little information. For compact autocatalytic cycles embedded within metabolism, one such constraint is much more informative. We thus focus our efforts on analyzing small autocatalytic cycles. Finding the unique constraints that metabolic autocatalytic cycles impose is essential for understanding the limitations of existing metabolic networks, as well as for modifying them for synthetic biology and metabolic engineering applications.

A key example of an autocatalytic cycle in carbon metabolism is the Calvin-Benson-Bassham cycle (CBB) (Benson et al., 1950). The carbon fixation CBB cycle, which fixes CO2 while transforming five-carbon compounds into two three-carbon compounds, serves as the main gateway for converting inorganic carbon to organic compounds in nature (Raven et al., 2012). The autocatalytic nature of the CBB cycle stems from the fact that for every 5 five-carbon compounds the cycle consumes, 6 five-carbon compounds are produced (by the fixation of 5 CO2 molecules). Beyond the CBB cycle, we show that most of the reactions and metabolites in the core of central carbon metabolism are part of compact (i.e. consisting of around 10 reactions or fewer) metabolic autocatalytic cycles. Some of the autocatalytic cycles we find are not usually considered as such. The span of autocatalytic cycles in central carbon metabolism suggests that the constraints underlying their stable operation have network-wide biological consequences.

In this study, we present the specific requirements metabolic autocatalytic cycles must meet in order to achieve at least one, non-zero, steady state which is stable in respect to fluctuations of either metabolites or enzyme levels close to the steady state point. The mathematical tools we use are part of dynamical systems theory (Strogatz, 2014). We identify the kinetic parameters of enzymes at metabolic branch points out of an autocatalytic cycle as critical values that determine whether the cycle can operate stably. We show that the affinity of enzymes consuming intermediate metabolites of autocatalytic cycles must be limited to prevent depletion of these metabolites. Moreover, we show that the stable operation of such cycles requires low saturation, and thus excess expression, of these enzymes. Low saturation of enzymes has previously been suggested to stem from a number of reasons in different contexts: (A) to achieve a desired flux in reactions close to equilibrium, for example in glycolysis (Staples and Suarez, 1997; Eanes et al., 2006; Flamholz et al., 2013); (B) to provide safety factors in the face of varying nutrient availability, for example in the brush-border of the mouse intestine (Weiss et al., 1998); (C) to accommodate rapid shifts in demand from the metabolic networks in muscles with low glycolytic flux (Suarez et al., 1997); (D) to allow fast response times, for example to pulses of oxidative load in erythrocytes, resulting from their adherence to phagocytes (Salvador and Savageau, 2003). Our findings add to these reasons the essential stabilizing effect of low saturation of branch reactions on the stability of fluxes through autocatalytic cycles.

We use recent fluxomics and proteomics data to test the predictions we make. We find them to hold in all cases tested where autocatalytic cycles support flux. Our analysis demonstrates how the requirement for stable operation of autocatalytic cycles results in design principles that are followed by autocatalytic cycles in-vivo. The results and design principles presented here can be further used in synthetic metabolic engineering applications that require proper functioning of autocatalytic cycles.

## Results

## Compact autocatalytic cycles are common and play important roles in the core of central carbon metabolism

Different definitions exist for autocatalytic sets in the context of chemical reaction networks (

![Figure 1.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig1-v2.jpg)

**Figure 1.:** .δDOI: http://dx.doi.org/10.7554/eLife.20667.003

While rarely discussed as such, a systematic search in the central carbon metabolism core model of

![Figure 2.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig2-v2.jpg)

**Figure 2.:** I) The Calvin-Benson-Bassham cycle (yellow); (II) The glyoxylate cycle (magenta); (III) A cycle using the phosphotransferase system (PTS) to assimilate glucose (cyan).Assimilation reactions are indicated in green. Arrow width in panels represent the relative carbon flux.DOI: http://dx.doi.org/10.7554/eLife.20667.004

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** This cycle contains a direct input reaction (rpi, dashed line) allowing the cycle to operate with broader sets of kinetic parameters than cycles missing this feature. A knockout strain where rpi is eliminated, does not grow under ribose despite having the theoretical ability to do so.DOI: http://dx.doi.org/10.7554/eLife.20667.005

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** This cycle contains a direct input reaction (tpi, dashed line) allowing the cycle to operate with broader sets of kinetic parameters than cycles missing this feature. According to fluxomics data this cycle does not operate in vivo as a more energy efficient alternative in growth under glycerol is to use the tpi reaction and proceed in the glycolitic direction in the lower part of glycolysis. A knockout strain where tpi reaction is eliminated, does not grow under glycerol despite having the theoretical ability to do so.DOI: http://dx.doi.org/10.7554/eLife.20667.006

Two additional examples are presented in Figure 2—figure supplements 1 and 2 and discussed below.

The ubiquity of compact autocatalytic cycles in the core of central carbon metabolism motivates the study of unique features of autocatalytic cycles, as derived below, which may constrain and shape the kinetic parameters of a broad set of enzymes at the heart of metabolism.

## Steady state existence and stability analysis of a simple autocatalytic cycle

To explore general principles governing the dynamic behavior of autocatalytic cycles, we consider the simple autocatalytic cycle depicted in

![Figure 3.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig3-v2.jpg)

**Figure 3.:** (A) A simple autocatalytic cycle induces two fluxes,  and fa as a function of the concentration of fb. These fluxes follow simple Michaelis-Menten kinetics. A steady state occurs when X, implying that fa=fb. The cycle always has a steady state (i.e. X˙=0) at X˙=0. The slope of each reaction at X=0 is X=0. A steady state is stable if at the steady state concentration Vmax/KM. (dX˙dX<0B) Each set of kinetic parameters,  determines two dynamical properties of the system: If Vmax,a,Vmax,b,KM,a,KM,b, then a stable steady state concentration must exist, as for high concentrations of Vmax,b>Vmax,a the branching reaction will reduce the concentration of X (cyan domain, cases (XI) and (II)). If , implying that Vmax,bKM,b<Vmax,aKM,a, then zero is a non-stable steady state concentration as if Vmax,bVmax,a<KM,bKM,a is slightly higher than zero, the autocatalytic reaction will carry higher flux, further increasing the concentration of X (magenta domain, cases (XI) and (IV)). At the intersection of these two domains a non-zero, stable steady state concentration exists, case (I).DOI: http://dx.doi.org/10.7554/eLife.20667.007

For simplicity in the derivation, we assume irreversible Michaelis-Menten kinetics for the two reactions. Even though fa should follow bisubstrate velocity equation, assuming constant concentration of A reduces the bisubstrate equation to a simple Michaelis-Menten equation. The apparent kinetic constants of the equation depend on the constant value of A (see Materials and methods section "Connecting bisubstrate reaction kinetic constants with simple Michaelis-Menten constants"). We extend our analysis to bisubstrate reaction equations in the next section. We therefore assume that:fa=Vmax,aXKM,a+Xfb=Vmax,bXKM,b+X

where Vmax is the maximal flux each reaction can carry and KM is the substrate concentration at which half the maximal flux is attained. Physiologically, these kinetic parameters must be positive. Using these simple forms allows us to obtain an analytic solution. We discuss more general cases below.

We characterize the metabolic state of this system by the concentration of the metabolite X. We note that knowing the concentration of X suffices in order to calculate the fluxes originating from it, fa and fb, thus fully defining the state of the system. A steady state of the system is defined as a concentration, X*, which induces fluxes that keep the concentration constant, such that the total in-flux to X is exactly equal to the total out-flux from it. In our example, the outgoing flux from X is fa+fb and the incoming flux to X is 2⁢fa, so at steady state it holds that:(1)X˙=d⁢Xd⁢t=2⁢fa-(fa+fb)=0

Intuitively, at steady state, the branch reaction must consume all the excess intermediate metabolite that is produced by the autocatalytic reaction. Indeed, expanding the condition above gives:fa=fb⇒Vmax,aX∗KM,a+X∗=Vmax,bX∗KM,b+X∗

which is satisfied either if X*=0 or if:(2)X*=Vmax,b⁢KM,a-Vmax,a⁢KM,bVmax,a-Vmax,b

implying that:(3)X*KM,a=Vmax,bVmax,a-KM,bKM,a1-Vmax,bVmax,a

The concentration of X cannot be negative, and thus we get a constraint on the kinetic parameters for which a positive steady state exists. Either both the numerator and the denominator of Equation 3 are positive, such that:1 > Vmax,bVmax,a > KM,bKM,a,

or both are negative, such that:1 < Vmax,bVmax,a < KM,bKM,a

These constraints are graphically illustrated in Figure 3B, cases (III) and (I).

In order to gain intuition for this relationship we note that VmaxKm is the slope of the Michaelis Menten function at X=0. The existence of a positive steady state can be used to get that:X∗ > 0⇒Vmax,bKM,a−Vmax,aKM,bVmax,a−Vmax,b > 0⇒Vmax,bKM,b−Vmax,aKM,aVmax,a−Vmax,b > 0

The last inequality above implies that in order for a positive steady state to exist, the reaction with higher maximal flux must have a shallower slope at X=0. Mathematically, the constraint states that if Vmax,a > Vmax,b then Vmax,aKM,a < Vmax,bKM,b. Alternatively, if Vmax,a < Vmax,b then Vmax,aKM,a > Vmax,bKM,b. This condition can be intuitively understood, as the reaction with shallower slope at X=0 has smaller fluxes for small values of X compared with the other reaction, so unless it has higher fluxes than the other reaction for large values of X (meaning that its maximal flux is higher), the two will never intersect (see Figure 3B).

While having a steady state at positive concentration is an essential condition to sustain flux, it is not sufficient in terms of biological function. The steady state at positive concentration must also be stable to small perturbations. Stability with respect to small perturbations is determined by the response of the system to small deviations from the steady state, X* (at which, by definition X˙=0). Assuming X=X*+Δ⁢X, stability implies that if Δ⁢X is positive then X˙ needs to be negative at X*+Δ⁢X, reducing X back to X*, and if Δ⁢X is negative, X˙ will need to be positive, increasing X back to X*. It then follows that in order for X* to be stable, dX˙dX < 0 at X=X*, implying that upon a small deviation from the steady state X* (where X˙=0), the net flux X˙ will oppose the direction of the deviation.

For the simple kinetics we chose, the stability condition dictates that:(4)dX˙dX|X=X∗=Vmax,aKM,a(KM,a+X∗)2−Vmax,bKM,b(KM,b+X∗)2 < 0

The analysis is straightforward for the case of X*=0, yielding that 0 is a stable steady state concentration if Vmax,bKM,b > Vmax,aKM,a, corresponding to the area above the diagonal in Figure 3B, where Vmax,bVmax,a > KM,bKM,a. These cases are denoted as cases (II) and (III). If the relation is reversed (i.e. Vmax,bKM,b < Vmax,aKM,a), then 0 is an unstable steady state. The criterion that is of interest, however, is the criterion for stability of the non-zero steady state, X*=Vmax,b⁢KM,a-Vmax,a⁢KM,bVmax,a-Vmax,b. In this case, substituting X* in Equation 4 gives the opposite condition to that of X*=0. This steady state is thus stable if Vmax,bKM,b<Vmax,aKM,a, corresponding to the magenta domain in Figure 3B, containing cases (I) and (IV), and unstable otherwise.

The stability criterion can be generally stated in metabolic control terms (Fell, 1997) using the notion of elasticity coefficients of reactions, defined as:εXf=∂⁡f∂⁡X⁢Xf

In these terms, stability is obtained if and only if the elasticity of the branch reaction at the positive steady state concentration is greater than the elasticity of the autocatalytic reaction:dfbdX|X=X∗ > dfadX|X=X∗⇒εXfb > εXfa

The complete analysis is summarized in Figure 3B. Domain (I) is the only domain where a positive, stable steady state exists. Domains (I) and (III) are the domains at which a positive steady state concentration exists, but in domain (III) that steady state is not stable. The domains below the diagonal (cases (I) and (IV)) are the domains where X*=0 is an unstable steady state concentration, so that if another steady state exists, it is stable, but in domain (IV) no positive steady state exists. The domains above the diagonal (cases (II) and (III)) are the domains where X*=0 is a stable steady state concentration, so that the other steady state, if it exists, is unstable.

Aside from existence and stability, a quantitative relationship between the affinity of the biomass generating, branching reaction and the flux it carries can be obtained. This relationship is opposite to the standard one, meaning that unlike the common case where the flux f increases when the affinity becomes stronger, in this case, because the steady state concentration increases when KM,b becomes weaker (Equation 7 in Materials and methods section "Steady state concentration dependence on kinetic parameters of autocatalytic and branch reactions"), fb also increases when KM,b becomes weaker.

To conclude, for this simple cycle, we get that in order for a positive-concentration stable steady state to exist (case (I)), two conditions must be satisfied:(5){Vmax,b > Vmax,aVmax,bKM,b <Vmax,aKM,a

The first requirement states that the maximal flux of the biomass generating, branching reaction should be higher than the maximal flux of the autocatalytic reaction. This requirement ensures a stable solution exists, as large concentrations of X will result in its reduction by the branch reaction. The second requirement states that for concentrations of X that are close enough to 0, the autocatalytic reaction is higher than the branch reaction (as can be inferred from the slopes). This requirement implies that the two fluxes will be equal for some positive concentration of X, ensuring a positive steady state exists. As this requirement further implies that below the positive steady state the branch reaction will carry less flux than the autocatalytic reaction, it follows that small deviations of the concentration of X below the steady state will result in an increase in its concentration by the autocatalytic reaction, driving it back to the steady state. Meeting the second constraint has another consequence.

Interestingly, these conditions imply that if KM,b < KM,a then no positive stable steady state can be achieved. Specifically, changes to the expression levels of the enzymes catalyzing fa and fb only affect Vmax,a and Vmax,b, and therefore do not suffice to attain a stable positive steady state. This indicates that stability of autocatalytic cycles, that are represented by the model analyzed above, depends on inherent kinetic properties of the enzymes involved and cannot always be achieved by modulating expression levels. We suggest this property to be a design principle that can be critical in metabolic engineering.

## Integrating the bisubstrate nature of the autocatalytic reaction into the simple model

In the model above, to keep the analysis concise, we neglected the bisubstrate nature of the autocatalytic reaction. We extend the analysis to the most common classes of bisubstrate reaction mechanisms in the Materials and methods, sections "Connecting bisubstrate reaction kinetic constants with simple Michaelis-Menten constants", "Constraints on concentration of assimilated metabolite and kinetic constants of bisubstrate reactions", and "Dependence of steady state concentration on assimilated metabolite". All bisubstrate reaction schemes analyzed take a Michaelis-Menten like form once the concentration of the assimilated metabolite is kept constant (Equations 8, 10, 12, and 14 in Materials and methods section "Connecting bisubstrate reaction kinetic constants with simple Michaelis-Menten constants").

For any set of kinetic parameters, under all ternary enzyme complex schemes, a lower bound on the concentration of A exists, under which the conditions for the existence and stability of a positive steady state cannot be satisfied (Equations 18 and 23 in Materials and methods section "Constraints on concentration of assimilated metabolite and kinetic constants of bisubstrate reactions"). The exact value of the minimal concentration of A depends on the specific bisubstrate reaction scheme and the kinetic parameters of it.

In the simplified model analyzed above, stability implied the affinity of the branch reaction towards its substrate was limited. A similar limit exists in most cases of bisubstrate reaction schemes (Equations 16, 19, and 21 in Materials and methods section "Constraints on concentration of assimilated metabolite and kinetic constants of bisubstrate reactions"). Interestingly, if the bisubstrate reaction is ordered with the internal metabolite binding first, then no strict constraints exist on KM,b and a stable steady state solution can always be achieved by setting appropriate values to Vmax,b and Vmax, the maximal flux of the bisubstrate autocatalytic reaction.

Finally, regarding the dynamic behavior of the system when the concentration of A varies, we note that in all three ternary enzyme complex cases, as the concentration of A approaches its lower bound, the steady state concentration of X approaches 0, reducing both the autocatalytic and the branch fluxes (Equations 24, 25, and 26 in Materials and methods section "Dependence of steady state concentration on assimilated metabolite"). In the substituted enzyme mechanism, the lower bound on the concentration of A is 0, at which the steady state concentration of X is trivially 0 as well. In all cases, if the maximal flux of the autocatalytic reaction is higher than the maximal flux of the branch reaction, an upper bound on the concentration of A may also exist, to satisfy the condition that Vmax,a < Vmax,b. However, this bound can be removed by increasing Vmax,b or reducing Vmax.

## Extensions of the simple autocatalytic cycle model

## Generalizing for different autocatalytic stoichiometries

Our didactic analysis considered an autocatalytic reaction with 1:2 stoichiometry, such that for every substrate molecule consumed, two are produced. Real-world autocatalytic cycles may have different stoichiometries. For example, the CBB cycle has a stoichiometry of 5:6 so that for every 5 molecules of five-carbon sugar that the autocatalytic reaction consumes, 6 five-carbon molecules are produced. We can generalize our analysis by defining a positive δ such that for every molecule of X that fa consumes, it produces 1+δ molecules of X, where δ may be a fraction. This extension implies that Equation (1) becomes:X˙=dXdt=(1+δ)fa−(fa+fb)=0⇒δ⋅fa=fb⇒δ⋅Vmax,aXKM,a+X=Vmax,bXKM,b+X

Therefore, all of the results above can be extended to different stoichiometries by replacing Vmax,a with δ⋅Vmax,a. As a result, the qualitative conditions and observations from the 1:2 stoichiometry case remain valid but with a constant factor that changes the quantitative relations according to the relevant stoichiometry.

## Input flux increases the range of parameters for which a stable steady state solution exists

Autocatalytic cycles are embedded within a larger metabolic network. Specifically, such cycles may have independent input fluxes to some of their intermediate metabolites, not requiring the use of other intermediate metabolites of the cycle. For example, in the glucose based, PTS-dependent autocatalytic cycle, the existence of alternative transporters can generate flux of glucose 6-phosphate into the cycle without the use of pep (Ferenci, 1996).

When adding a constant input flux,

![Figure 4.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig4-v2.jpg)

**Figure 4.:** (A) The effect of a fixed input flux, , on the possible steady states of a simple autocatalytic cycle. A steady state occurs when fi. If fa+fi=fb then there is always a single stable steady state (Vmax,b>Vmax,a+fiI). If  then there can either be no steady states (Vmax,b<Vmax,a+fiII), or two steady states where the smaller one is stable (III).DOI: http://dx.doi.org/10.7554/eLife.20667.008

In this situation, at X=0, X˙=fi > 0 so the concentration of X increases and there is no steady state at zero. If Vmax,b > fi+Vmax,a then at a large enough value of X, X˙ will be negative, implying that at some value of X between these two extremes, X˙ attains the value of zero, such that under this condition a positive stable steady state concentration exists (Figure 4I). This case therefore differs from the case with no input flux analyzed above, as now a positive stable steady state can always be achieved by modifying only Vmax,a and/or Vmax,b. In this setup, cells can therefore tune the expression levels of enzymes to meet the needs of a stable steady state flux.

In cases where Vmax,b < fi+Vmax,a either no steady states exist (Figure 4II), or two positive steady states exist (Figure 4III). The latter case implies that there exists a positive concentration X that satisfies:X˙=0⇒fi+fa(X)−fb(X)=0⇒fi+Vmax,aXKM,a+X=Vmax,bXKM,b+X

In this case, the lower concentration steady state will be stable.

To conclude, input fluxes change the steady state(s) of autocatalytic cycles. When an input flux is present, an autocatalytic cycle can always achieve a non zero, stable steady state by tuning the expression levels of the enzymes forming the cycle.

Interestingly, we find that in the two autocatalytic cycles shown in Figure 2—figure supplements 1 and 2, reactions that generate direct input flux into the cycle exist. In the ribose-5P assimilating autocatalytic cycle (Figure 2—figure supplement 1), the rpi reaction serves as a shortcut, allowing input flux directly from ribose-5P into the cycle. In the glycerone-phosphate assimilating cycle (Figure 2—figure supplement 2), the tpi reaction similarly serves as such a shortcut. Interestingly, in these two cases, these shortcuts relax the constraints imposed by the strict use of the corresponding autocatalytic cycles as they prevent zero from being a stable steady state concentration. Another example of the effects of the addition of an input flux to an autocatalytic cycle is the input flux of fructose-6-phosphate from the catabolism of starch into the CBB cycle. This input flux can be used to ’kick start’ the cycle even without using the intermediate metabolites of the cycle.

## Reversible branch reaction can either be far from equilibrium, resulting in the simple case, or near equilibrium, pushing the stability conditions down the branch pathway

The simple model assumed both the autocatalytic and the branch reactions are irreversible under physiological conditions. Assuming the branch reaction, fb, can be reversible, with a product Y, the system can be analyzed in two extreme cases.

If Y is consumed very rapidly by subsequent reactions, keeping its concentration low, then fb operates far from equilibrium. In this case, the reversible reaction equation reduces to an irreversible Michaelis-Menten equation, resulting in the same constraints as in the simple, irreversible case analyzed above.

If Y is consumed very slowly, and if the maximal consumption of Y is larger than Vmax,a, then, as long as Vmax,b > Vmax,a, a stable steady state exists both when Vmax,b→∞, making fb operate near equilibrium, and when Vmax,b→Vmax,a. A mathematical analysis is provided in the Materials and methods section "Reversible branch reaction analysis". The assumptions on the consumption of Y in this case are analogous to the constraints in Equation 5, namely that the reaction downstream of Y is less saturated than the autocatalytic reaction, and that it consumes Y at a lower rate than the rate at which the autocatalytic reaction produces X near X=0.

## Analysis of a reversible autocatalytic cycle reaction

The simple model assumed both the autocatalytic and the branch reactions are irreversible under physiological conditions. The autocatalytic reaction in the simple model represents an effective overall reaction for all of the steps in autocatalytic cycles found in real metabolic networks. In order for the combined autocatalytic reaction to be physiologically reversible, all of the reactions in the real metabolic network must be reversible under physiological conditions. We note that this is not the case in any of the cycles we identify in central carbon metabolism. Nevertheless, this case can be mathematically analyzed.

If the autocatalytic reaction is reversible, then it must be driven by the displacement from thermodynamic equilibrium of the concentration of A versus the concentration of X. Therefore, for any fixed concentration of A, A^, a concentration of X exists such that fa(X,A^)=0 < fb(X). It then follows that a sufficient condition for a positive steady state to exist is that at X=0, X˙(A^) > 0, which implies that∂fa∂X|X=0,A=A^ > Vmax,bKM,b

This condition can always be satisfied by high expression of the autocatalytic enzyme, increasing Vmax,a. For this case, it therefore follows that for any concentration of A, a minimal value for Vmax,a exists, above which a positive steady state is achieved.

## Stability analysis for multiple-reaction cycles

Even the most compact real-world autocatalytic cycles are composed of several reactions. It is thus useful to extend the simple criteria we derived to more complex autocatalytic cycles. In such cycles the criteria for the existence of a steady state become nuanced and detail specific. We therefore focus on evaluating stability of such cycles, under the assumption that a non-zero steady state exists, which is usually known based on experimental measurements.

We analyze the stability criteria for the autocatalytic cycles depicted in

![Figure 5.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig5-v2.jpg)

**Figure 5.:** (A) A two reaction system. (B) A generic -reaction system. The system is at steady state when the total consumption of intermediate metabolites by the branch reactions is equal to the flux through the autocatalytic reaction, because the autocatalysis is in a 1:2 ratio. A sufficient condition for the stability of a steady state in these systems is that the derivative of at least one branch reaction with respect to the substrate concentration is larger than the derivative of the equivalent autocatalytic reaction at the steady state concentration. Given the connection between derivatives of fluxes and saturation levels of reactions (see methods), this condition implies that at a stable steady state, the saturation level of at least one branch reactions is smaller than the saturation level of the corresponding autocatalytic reaction.nDOI: http://dx.doi.org/10.7554/eLife.20667.009

Using the connection between derivatives of reactions and saturation levels (Materials and methods section "Inverse relationship between derivatives, affinities, and saturation levels"), we conclude that if βi>αi for some i at the steady state point, then the saturation of the branch reaction, denoted S⁢(f), must be lower than the saturation of the corresponding cycle reaction at Xi:(6)S⁢(fbi)<S⁢(fai)

This condition also dictates that the affinity of the branch reaction to the intermediate metabolite of the cycle it consumes must be weaker than the affinity of the corresponding recycling reaction of the cycle.

While having a single branch point at which βi > αi is a sufficient condition for stability, we note that the larger the number of branch points satisfying this condition, the more robust the steady state point will be to perturbations, as such branch points reduce the propagation of deviations along the cycle (see Materials and methods section "Multiple unsaturated branch reactions increase convergence speed and dampen oscillations"). As we show below, these predictions hold for functioning autocatalytic cycles.

## Using different kinetic equations

Although we utilized the widely-used irreversible Michaelis-Menten kinetics equation to model enzyme kinetics, our results can be extended to different kinetic equations. Generally, two conditions must be met for a stable flux through an autocatalytic cycle to exist: (A) there should be a positive concentration of the intermediate metabolites for which the outgoing fluxes balance the autocatalytic fluxes, resulting in a steady state, and, (B) at the steady state point at least one derivative of an outgoing reaction out of the cycle should be higher than the derivative of the corresponding cycle reaction, as is implied by Equation 31, to enforce stability in the presence of small perturbations. Therefore, these two conditions should be explicitly evaluated for every case with different kinetic equations and autocatalytic cycles topologies to assert whether it can carry stable fluxes or not.

## Testing the predictions of the analysis with experimental data on functioning autocatalytic cycles

To evaluate the validity of our analysis of autocatalytic cycles we searched for growth conditions under which the autocatalytic cycles we identified in central carbon metabolism carry substantial flux in-vivo. We used recent in-vivo flux measurements in E. coli from Gerosa et al. (2015). According to the data, two autocatalytic cycles carry substantial flux under at least one of the growth conditions measured: a cycle using the PTS carries significant fluxes in growth on glucose and on fructose; the glyoxylate cycle carries significant flux in growth on acetate and on galactose.

As noted above, we predict a design principle for functioning autocatalytic cycles: that at least one branch reaction should have a steeper response than the corresponding autocatalytic reaction at steady state. This requirement is sufficient, but not necessary, for the autocatalytic cycle to be at a stable steady state point. Moreover, having more than one branch point at which the branch reaction has a steeper response than the autocatalytic reaction increases the robustness of the steady state flux in the cycle as shown in the Materials and methods section "Multiple unsaturated branch reactions increase convergence speed and dampen oscillations". An outcome of the relationship between the steepness’s of responses is a reverse relationship between the saturation levels of the corresponding reactions (Equation 35). In order to evaluate the saturation level of a reaction under a given condition, two values must be obtained:

To estimate the maximal capacity of a reaction we followed the procedure described in (

![Figure 6.](https://cdn.elifesciences.org/articles/20667/elife-20667-fig6-v2.jpg)

**Figure 6.:** Solid arrow width represents carbon flux per unit time. Shaded arrow width represents the maximal carbon flux capacity per unit time, given the expression level of the catalyzing enzyme. In all cases there is enough excess capacity in the branching reactions to prevent the cycle from overflowing. A  flux from pep to biomass was neglected in growth under glucose and fructose. Only in one out of the nine branch points observed (the branch point at fbp in growth under fructose), the outgoing reaction is significantly more saturated than the autocatalytic reaction. (*) A branch point at which the branching reaction is more saturated than the autocatalytic reaction, which may result from neglecting fructose transport directly as f6p when deriving fluxes (see text).4%DOI: http://dx.doi.org/10.7554/eLife.20667.010

Our results show that for any of the four functioning autocatalytic cycle cases, in at least one branch point the biomass generating branch reaction has a larger maximal flux capacity, and is considerably less saturated than the respective autocatalytic reaction, in accordance with our predictions. Moreover, out of nine branch points analyzed, in six branch points the branching reactions were significantly less saturated than the autocatalytic reactions, in two branch points the saturation levels were similar, and only in one branch point the autocatalytic reaction was less saturated than the branching reaction.

The branch point at which the autocatalytic reaction is less saturated than the branch reaction is the branch point from fructose-1,6-bisphosphate in growth on fructose as the carbon source. The high saturation of the branch reaction arises as a large flux is reported for the fbp reaction, whereas the corresponding enzyme is not highly expressed under this condition. The large reported flux through fbp arises due to assuming a single transport pathway for fructose, entering the cycle as fructose-1,6-bisphosphate. However, an alternative fructose transport pathway is known to occur for the concentration at which the measurements were made (Kornberg, 1990). The alternative transport pathway produces fructose-6-phosphate from external fructose. Therefore, any flux through the alternative transport pathway should be directly deducted from the flux through fbp. Assuming 20% of the consumed fructose uses this pathway suffices in order to balance the saturation levels at the fructose-1,6-bisphosphate branch point.

We made two negative control analyses to examine whether other reasons do not underlie the trend we find. First, we compared the saturation levels at the same branch points in growth conditions at which the autocatalytic cycles do not function, but the reactions carry flux. We find that for these cases, only 4 out of 9 cases satisfy the low branch saturation condition (Supplementary file 1). Second, we searched for branch points out of non-autocatalytic cycles and tested whether in such points branch reactions are also consistently less saturated than their corresponding cycle reactions. We found two flux-carrying cycles: the TCA cycle, carrying flux in glucose, fructose, and glycerol growth, and a cycle consisting of the pentose-phosphate pathway combined with gluconeogenesis, carrying flux in acetate, glycerol, and succinate growth. Out of the total six conditions-branch points cases, in three the branch reaction was less saturated than the cycle reaction, and in three the cycle reaction was less saturated than the branch reaction (Supplementary file 1). We therefore conclude that, for cases that do not involve autocatalysis, the saturation of branch versus cycle reactions seems evenly distributed.

The consistently lower saturation values of biomass generating branch reactions demonstrate that the expressed enzymes have enough capacity to prevent the autocatalytic cycle from increasing the concentration of intermediate metabolites infinitely. Moreover, the lower saturation values of the biomass generating reactions suggest that at the steady state point their derivatives are higher, ensuring stable operation of the cycle.

Another demonstration of the autocatalytic mechanism being at play is in the CBB cycle, which is not a part of the metabolic network of wild type E. coli, and for which no flux measurements are available. This cycle has been recently introduced synthetically into E. coli and was shown to carry flux in it, given further metabolic engineering of central carbon metabolism (Antonovsky et al., 2016). The experimentally observed key evolutionary event enabling the functioning of the CBB cycle, was a mutation affecting the kinetic properties of the main branching reaction out of the CBB pathway, prs, weakening its affinity to its substrate, ribose-5p. The observed weakening of affinity of prs is directly in line with our predictions on the relationship between the affinity of branch reactions and the affinity of the corresponding cycle reactions (see Materials and methods section of Antonovsky et al., 2016).

The other examples of autocatalytic cycles we found did not carry flux in any of the conditions for which data were available. The pentose-phosphate cycle variants do not carry flux in any of the measured conditions, which is expected given that growth on ribose was not measured. The gluconeogenic FBA with ED pathway cycle also did not carry flux in any of the measured conditions. Although glycerol could have been a potential carbon source to use this pathway, the metabolic network allows for a more energy efficient growth by using the tpi reaction, as was indeed observed.

To conclude, existing data supports predictions made by our model, given the requirement for stable steady state operation of autocatalytic cycles. This agreement between predictions and measurements is especially encouraging given the highly limited information on kinetic properties, concentrations, and fluxes under various growth conditions.

## Analysis of allosteric regulation potential for cycle improvement

Allosteric regulation can modulate the kinetic properties of enzymes at branch points, and of the cycle in general. As such, the relevant condition for the existence of a stable positive steady state should hold for the updated kinetic properties as defined following the effect of allosteric regulation.

We further analyze the ability of specific allosteric interactions to support fast convergence and stability of autocatalytic cycles in the Materials and methods section "Allosteric regulation can improve network performance". We compare the expected beneficial allosteric interactions against the allosteric regulation network of the two functioning autocatalytic cycles we identified, the PTS-using autocatalytic cycle and the glyoxylate cycle (Supplementary file 1, regulation data were taken from Keseler et al. (2013) and Schomburg et al. (2004)).

For the PTS cycle, we find that there are a total of 12 allosteric interactions, 7 inhibitions and five activations. Out of these 12 interactions, 11 interactions follow our expectations in terms of the type of the regulating metabolite (assimilated metabolite, cycle intermediate, or branch product), the regulated reaction (cycle reaction, branch reaction, or the reverse of a branch reaction), and the direction of the regulation (activation or inhibition). One interaction, the activation of fba by pep, does not follow our expectation.

For the glyoxylate cycle, we find that there are a total of 13 interactions, 12 inhibitions and one activation. Out of these 13 interactions, 8 interactions follow our expectations and 5 do not. The lack of significant agreement between the expected regulation direction and the actual regulation found for this cycle is consistent with the observation in Gerosa et al. (2015) that TCA cycle fluxes are regulated mainly by transcription and not by reactants levels.

It is important to note that allosteric regulation serves many roles, and that the metabolic network faces many more challenges than just the support of stable autocatalysis. Therefore, the agreement we find between existing allosteric interactions and the expected regulation scheme supporting autocatalysis does not suggest that the autocatalytic nature of the PTS is the only, or even main underlying reason for these allosteric interactions.

## Discussion

Our study into the dynamics and stability of autocatalytic cycles suggests design principles applicable to both systems biology, that aims to understand the function of natural networks, and in the context of synthetic biology, in the effort to express novel heterologous cycles.

While autocatalytic cycles are often overlooked in the study of metabolism, we find that such cycles are at the heart of central carbon metabolism. Our autocatalytic modeling framework gives concrete predictions on saturation levels of branch reactions for operating autocatalytic cycles. We find these predictions agree well with empirically measured fluxomics and proteomics data sets. Given that there are other suggestions (Staples and Suarez, 1997; Weiss et al., 1998; Suarez et al., 1997) that may underlie the low saturation of branch reactions, we compare the saturation levels of branch reactions versus their corresponding cycle reactions both under conditions when the autocatalytic cycle does not function, and for branch points out of non-autocatalytic cycles. Both tests show no bias towards low saturation of branch reactions out of non-autocatalytic cycles, contrary to the clear trend we find for reactions branching out of autocatalytic cycles. Our findings thus support the addition of stability of intermediate metabolites of autocatalytic cycles as an explanation for the seemingly wasteful expression of enzymes (Salvador and Savageau, 2003, 2006). The model we present can also highlight metabolic branch points at which the kinetic efficiency of enzymes is constrained due to stability requirements of a corresponding autocatalytic cycle.

A common concept in synthetic biology is that the successful implementation of novel pathways requires the expression of functional enzymes in the correct amounts in the target organism. Here we show that in the context of autocatalytic cycles, such expression modulation may not suffice. Specifically, changes to the substrate affinity of enzymes at branch points of the cycle may be required in order for the novel pathway to function.

Another aspect of our findings is that while it is common to assume that strong affinity and high catalytic rate are desirable traits for enzymes, such seeming improvements may actually lead to instability and thus to non functional metabolic cycles. Furthermore, for reactions branching out of autocatalytic cycles, weaker affinities increase the steady state concentration of intermediate metabolites, resulting in higher fluxes both through the cycle, and through the branch reaction, suggesting an unconventional strategy for optimizing fluxes through such reactions. We note that because allosteric regulators modify the affinity of the enzymes they target, such regulators can potentially be used to restrict the affinity of branch reactions only when the autocatalytic cycle functions.

An experimental demonstration of these principles in-vivo is the recent implementation of a functional CBB cycle in E. coli by introducing the two genes missing for its function (Antonovsky et al., 2016). The successful introduction of the genes did not suffice to make the cycle function, and further directed evolution was needed in order to achieve successful operation of the cycle. Strikingly, most evolutionary changes occurred in branch points from the cycle (Antonovsky et al., 2016). The change which was biochemically characterized in the evolutionary process was the decrease of the value of kcatKM of phosphoribosylpyrophosphate synthetase (prs), one of the enzymes responsible for flux out of the CBB cycle, corresponding to the branch reaction in our simple model. This is beautifully in line with the predictions of our analysis that suggest that decreasing VmaxKM of branch reactions can lead to the existence of a stable flux solution.

Our observation regarding the stabilizing effect of input fluxes into an autocatalytic cycle can provide means to mitigate the stability issue in synthetic biology metabolic engineering setups. In such setups, conducting directed evolution under gradually decreasing input fluxes, such as those achieved in a chemostat, allows for a pathway to gradually evolve towards sustainable, substantial flux.

Finally, while our work focuses on cycles increasing the amount of carbon in the system, we note that autocatalysis can be defined with respect to other quantities such as energy (e.g. ATP investment and production in glycolysis [Teusink et al., 1998]), non-carbon atoms, reducing power, or other moieties (Reich and Selkov, 1981). As autocatalysis is often studied with relation to the origin of life, our analysis may be useful in studying synthetic autocatalytic systems such as the one recently described in Semenov et al. (2016). The analysis we present here can thus be of relevance for the analysis of metabolic networks in existing organisms and for the design of novel synthetic systems.

## Materials and methods

## Formal definition of an autocatalytic metabolic cycle

Given a metabolic network composed of a set of reactions and metabolites, the following criteria can be used to define a subset of the network that is an autocatalytic cycle: First we define a metabolic cycle. A set of irreversible reactions (for reversible reactions only one direction can be included in the set) and metabolites forms a cycle if every metabolite of the set can be converted, by sequential application of reactions in the set (where two reactions can be chained if a metabolite in the set is a product of the first reaction and a substrate of the second reaction), to every other metabolite in the set. A cycle is autocatalytic if the reactions of the cycle can be applied, each reaction at an appropriate, positive number of times, such that the resulting change in the amount of each of the metabolites forming the cycle is non-negative, with at least one metabolite of the cycle having a strictly positive change.

The same definition can be stated in terms of reaction vectors and a stoichiometric matrix. If a metabolic network has n metabolites, indicated by the numbers 1 to n, then every reaction, r, in the network can be described as a vector Vr in ℤn, such that the i’th coordinate of Vr specifies how much of metabolite i the reaction r produces (if r consumes a metabolite, then the value at the coordinate representing the metabolite is negative).

With this notation, a set of metabolites: M=m1⁢⋯⁢mj and a set of reactions, R=r1⁢⋯⁢rk form an autocatalytic cycle if:

## Systematic identification of autocatalytic cycles in metabolic networks

We implemented an algorithm to systematically search for autocatalytic cycles in metabolic networks. The algorithm is not comprehensive, in the sense that there may be autocatalytic cycles that will not be identified by it. Further work will enable a more advanced algorithm to identify additional autocatalytic cycles in full metabolic networks. We used the algorithm on the core carbon metabolism network of E. coli (Orth et al., 2010).

In our framework, a metabolic network is defined by a set of reactions, (R¯). Each reaction is defined by a set of substrates and a set of products, with corresponding stoichiometries Ri=(S,P,NS,NP), such that Ri describes the reaction ∑jNjS⁢Sj→∑kNkP⁢Pk. The algorithm works as follows:

The algorithm assumes reactions consume exactly one molecule of any of their substrates and produce exactly one molecule of any of their products, an assumption that holds for the core model of E.coli, but not in metabolic networks in general.

## Steady state concentration dependence on kinetic parameters of autocatalytic and branch reactions

The simple cycle steady state concentration, X*, is given in Equation 2. Taking the derivative of this expression with respect to KM,a, KM,b, Vmax,a, and Vmax,b, under the assumption that the kinetic parameters satisfy the stability conditions in Equation 5 gives:(7)∂X∗∂KM,a=Vmax,bVmax,a−Vmax,b < 0∂X∗∂KM,b=−Vmax,aVmax,a−Vmax,b > 0∂X∗∂Vmax,a=Vmax,b(KM,b−KM,a)(Vmax,a−Vmax,b)2 > 0∂X∗∂Vmax,b=Vmax,a(KM,a−KM,b)(Vmax,a−Vmax,b)2 < 0

So that X* increases when KM,a decreases or Vmax,a increases (or both) corresponding to activation of fa. On the other hand, X* decreases when KM,b decreases or Vmax,b increases (or both) corresponding to activation of fb.

## Connecting bisubstrate reaction kinetic constants with simple Michaelis-Menten constants

Three standard equations are commonly used to describe the flux through irreversible bisubstrate reactions (Leskovac, 2003). We show that, under the assumption that the assimilated metabolite maintains constant concentration, these equations reduce to simple Michaelis-Menten equations. We derive the expressions for the apparent Michaelis-Menten constants, KM and Vmax, as functions of the kinetic constants of the bisubstrate reaction and the concentration of the assimilated metabolite. While the substrates in these equations are generally denoted as A and B, here, to keep the notation consistent, we will denote by A the assimilated metabolite and by X the internal metabolite of the cycle.

The simplest equation describing a bisubstrate reaction assumes substituted enzyme (Ping Pong) mechanism (Imperial and Centelles, 2014). As this equation is symmetric with respect to the two substrates, we can arbitrarily decide which of the two substrates is the assimilated metabolite, and which is the internal metabolite. We get that the flux through the reaction is:f=Vmax⁢A⁢XKX⁢A+KA⁢X+A⁢X

Rearranging to get the dependence of the flux on X in a Michaelis-Menten like form we get that:(8)f=Vmax⁢AKA+A⁢XKX⁢AKA+A+X

which gives apparent Michaelis-Menten kinetic constants of:(9)V~max=VmaxAKA+AK~M=KXAKA+A

The second bisubstrate reaction mechanism we consider is the ternary enzyme complex with random binding order of the two substrates. As this equation is also symmetric with respect to the two substrates, we can again arbitrarily decide which of the two substrates is the assimilated metabolite, and which is the internal metabolite. We get that the flux through the reaction is:f=Vmax⁢A⁢XKi,A⁢KX+KX⁢A+KA⁢X+A⁢X

Rearranging to get the dependence of the flux on X in a Michaelis-Menten like form we get that:(10)f=Vmax⁢AKA+A⁢XKi,A+AKA+A⁢KX+X

which gives apparent Michaelis-Menten kinetic constants of:(11)V~max=VmaxAKA+AK~M=Ki,A+AKA+AKX

The other equation describing a ternary enzyme complex bisubstrate reaction assumes ordered binding of the substrates. Because in ordered binding the equation is asymmetric with respect to the two substrates, analyzing this reaction is further split according to which of the two substrates is assumed to be the assimilated metabolite with constant concentration.

If the first binding metabolite is assumed to be the assimilated metabolite we get that:(12)f=Vmax⁢A⁢XKi,A⁢KX+KX⁢A+A⁢X=Vmax⁢XKi,A+AA⁢KX+X

which gives apparent Michaelis-Menten kinetic constants of:(13)V~max=VmaxK~M=Ki,A+AAKX

If the first binding metabolite is assumed to be the internal metabolite we get that:(14)f=Vmax⁢A⁢XKi,X⁢KA+KA⁢X+A⁢X=Vmax⁢AKA+A⁢XKi,X⁢KAKA+A+X

which gives apparent Michaelis-Menten kinetic constants of:(15)V~max=VmaxAKA+AK~M=Ki,XKAKA+A

To summarize, the most common equations describing bisubstrate reactions reduce to equations of the same form as Michaelis-Menten equations, under the assumption that one of the metabolites maintains a constant concentration. The apparent kinetic constants of the Michaelis-Menten equivalent equations depend on the kinetic constants of the bisubstrate reactions, as well as on the concentration of the assimilated metabolite.

## Constraints on concentration of assimilated metabolite and kinetic constants of bisubstrate reactions

In Equation 5 we obtain constraints on the kinetic parameters of Michaelis-Menten reactions that ensure the existence and stability of a positive steady state. We observe that these constraints imply that even if the maximal rates of the two reactions can be easily modified, if KM,b<KM,a then such changes cannot suffice in order to satisfy the existence and stability constraints.

Here, we map the same constraints from Equation 5 onto bisubstrate autocatalytic reactions. This mapping results in constraints on the assimilated metabolite concentration, as well as on the kinetic parameters of the bisubstrate autocatalytic reactions. We show that in all ternary enzyme complex bisubstrate reaction schemes, there is a lower bound on the concentration of the assimilated metabolite, below which the system cannot attain a stable positive steady state. We further show that the nature of the bisubstrate reaction qualitatively affects the ability to satisfy the stability constraints by changing expression levels alone. In the cases of substituted enzyme mechanism, random binding order ternary complex, and ordered binding ternary complex, with the assimilated metabolite binding first, unless the kinetic parameters of the participating enzymes satisfy specific inequalities, changes to the maximal reaction rates alone cannot suffice in order to satisfy the existence and stability constraints. However, in the case of ordered binding ternary complex with the internal metabolite binding first, changes to the maximal reaction rates alone suffice in order to allow for stable steady state to occur, given high enough concentration of the assimilated metabolite. We analyze each of the four possible bisubstrate reaction schemes separately below.

## Substituted enzyme (Ping Pong) mechanism

The case of substituted enzyme mechanism is the simplest case to analyze. We can substitute Equation 9 into the conditions from Equation 5 to get:(16){Vmax,b>VmaxAKA+A=VmaxAKA+AVmax,bKM,b<VmaxKX

As AKA+A < 1, the first inequality can always be satisfied if Vmax,b > Vmax, which is equivalent to the first condition in Equation 5. The second condition is identical to the second condition from Equation 5. Therefore, this case imposes equivalent conditions to those derived for the simple, single substrate case.

## Random binding order

In the case of a random binding order, we can substitute Equation 11 into the conditions from Equation 5 to get:(17){Vmax,b > VmaxAKA+A=VmaxAKA+AVmax,bKM,b < VmaxA(Ki,A+A)KX=VmaxAKi,A+AKX

We first note that from the second inequality we get that:(18)Vmax,bKXKM,bVmax < AKi,A+A⇒Ki,AKM,bVmaxVmax,bKX−1 < A

Giving a lower bound on the concentration of the assimilated metabolite for which a stable steady state is attainable.

We now wish to obtain a lower bound on KM,b. In order to obtain such a lower bound, we need an upper bound on Vmax⁢AKi,A+A. However, we only have an upper bound on Vmax⁢AKA+A. We use the first inequality in Equation 17 to get that:Vmax,b>VmaxAKA+A⇒Vmax,bAKi,A+A>VmaxAKA+AAKi,A+A⇒Vmax,bKA+AKi,A+A>VmaxAKi,A+A

We note that for positive A, KA+AKi,A+A < max(1,KA/Ki,A) and therefore:Vmax,bmax(1,KA/Ki,A) > VmaxAKi,A+A

Substituting this inequality in the second inequality of Equation 17 therefore gives us that:(19)Vmax,bKM,b<VmaxAKi,A+AKX< Vmax,bmax(1,KA/Ki,A)KX⇒KXmax(1,KA/Ki,A)< KM,b

We have therefore obtained a lower bound on the affinity of the branch reaction, KM,b, in this case.

For the random binding order we can thus conclude that, like in the single-substrate case, a lower bound exists on the affinity of the branch reaction, below which a positive steady state is not attainable, even if the expression levels of the enzymes, and the concentration of the assimilated metabolite are modified. Furthermore, for any set of kinetic parameters, there is a lower bound on the concentration of A for which a positive steady state is attainable.

## Ordered binding with the assimilated metabolite binding first

In the case of ordered binding, with the assimilated metabolite binding first, we can substitute Equation 13 into the conditions from Equation 5 to get:(20){Vmax,b> VmaxVmax,bKM,b< VmaxA(Ki,A+A)KX=VmaxAKi,A+AKX

As the second inequality is identical to the one in the random binding order case, we can immediately conclude that the same lower bound on the concentration of A from Equation 18 holds in this case as well.

Regarding a lower bound on KM,b, following a similar reasoning as in the previous case, we first note that for any value of A:AKi,A+A < 1

Therefore, we can deduce, by using the first inequality from Equation 20 in the second inequality from that equation, that:Vmax,bKM,b < VmaxAKi,A+AKX < VmaxKX < Vmax,bKX

which immediately yields:(21)KX < KM,b

setting an absolute lower bound on KM,b.

We thus arrive at the same conclusions in this case, as we have arrived to in the previous case, namely that a lower bound exists on the affinity of the branch reaction, and that, for any set of kinetic parameters, there is a lower bound on the concentration of the assimilated metabolite, below which a positive stable steady state cannot be obtained.

## Ordered binding with the internal metabolite binding first

In the case of ordered binding, with the internal metabolite binding first, we can substitute Equation 15 into the conditions from Equation 5 to get:(22){Vmax,b> VmaxAKA+AVmax,bKM,b< VmaxAKi,XKA

As in the previous two cases, the second inequality can be used to obtain a lower bound on the concentration of A:(23)Vmax,bKi,XKAKM,bVmax < A

However, unlike in the previous two cases, in this case if Vmax < Vmax,b, then the first inequality in Equation 22 holds for any concentration of A, and, for any concentration of A that is larger than its lower bound, the second inequality is also satisfied, resulting in a stable steady state. This case is therefore more robust than the other cases as it allows for the conditions to be satisfied, at least for high concentrations of A, given any set of kinetic parameters.

## Dependence of steady state concentration on assimilated metabolite

Equation 2 shows the dependency between the steady state concentration of the internal metabolite X, X*, and the kinetic parameters of the reactions in the system. Substituting the dependencies of the apparent kinetic parameters from Equations 11, 13, and 15 into Equation 2 gives the dependency of X* on the kinetic parameters of the bisubstrate reactions and the concentration of the assimilated metabolite, A. We get for these three cases respectively that:(24)X∗=VmaxAKA+AKM,b−Vmax,bKi,A+AKA+AKXVmax,b−VmaxAKA+A(25)X∗=VmaxKM,b−Vmax,bKi,A+AAKXVmax,b−Vmax(26)X∗=VmaxAKA+AKM,b−Vmax,bKi,XKAKA+AVmax,b−VmaxAKA+A

Assuming the kinetic parameters satisfy the stable steady state conditions derived in Equations 17, 20, and 22, we note that when A is equal to its lower bound, the numerator in all three cases is 0, resulting in X*=0. Furthermore, as A decreases towards its lower bound, X* decreases resulting in a decrease in both fb and fa (for the two latter cases this is trivial to show, as the terms involving A increase and decrease monotonically in accordance with their effect on X*. In the first case, taking the derivative of the numerator w.r.t. A shows the derivative is always positive, resulting in the same conclusion). Interestingly, in the first and last cases, if Vmax > Vmax,b, then an upper bound on the concentration of A also exists. As the concentration of A approaches this upper bound, the denominator approaches 0 resulting in an increase in the concentration of X* towards infinity.

## Reversible branch reaction analysis

The simple model assumed both the autocatalytic and the branch reactions are irreversible. Here we assume the branch reaction is reversible, and let Y denote its product. For simplicity, we further assume that Keq=1, noting that this assumption can always be satisfied by measuring the concentration of Y in units of Keq⁢X. We recall that the reversible Michaelis-Menten equation states that:fb=Vmax,b⁢(X-Y)KX+X+KXKY⁢Y

We assume that a third reaction, fc, irreversibly consumes Y. While assuming fc follows irreversible Michaelis-Menten kinetics is analytically tractable, the analysis is simpler, and as informative, under the assumption that fc=D⁢Y for some constant D. This simplification is equivalent to assuming fc follows Michaelis-Menten kinetics with Vmax,cKM,c≈D, and Vmax,c >> max(Vmax,a,Vmax,b).

We start by deriving the necessary conditions for steady state existence. Because at steady state fa=fc, it follows that:(27)Vmax,a⁢X*KM,a+X*=D⁢Y*⇒Y*=Vmax,aD⁢X*KM,a+X*

Furthermore, as at the steady state fa=fb, we get that:Vmax,a⁢X*KM,a+X*=Vmax,b⁢(X*-Y*)KX+X*+KXKY⁢Y*

Substituting Y* from Equation 27 gives:Vmax,a⁢X*KM,a+X*=Vmax,b⁢(X*-Vmax,aD⁢X*KM,a+X*)KX+X*+KXKY⁢Vmax,aD⁢X*KM,a+X*

Which is satisfied when X*=0 (implying that X*=Y*=0 is a steady state), or when X* satisfied the quadratic equation:0=(X∗)2+2KM,aVmax,b−(KM,a+KX)Vmax,a−KXVmax,a2KYD−Vmax,aVmax,bDVmax,b−Vmax,aX∗+KM,a(Vmax,bKM,a−Vmax,aKX−Vmax,aVmax,bD)Vmax,b−Vmax,a

Albeit intimidating, this quadratic equation can be used to derive the conditions for the existence of a positive steady state. Only if both of the roots of this equation are negative, no positive steady state exists. We recall that the two roots of a quadratic equation of the form 0=a⁢X2+b⁢X+c are negative iff:{b=2KM,aVmax,b−(KM,a+KX)Vmax,a−KXVmax,a2KYD−Vmax,aVmax,bDVmax,b−Vmax,a > 0c=KM,a(Vmax,bKM,a−Vmax,aKX−Vmax,aVmax,bD)Vmax,b−Vmax,a > 0

As in the irreversible case, the sign of Vmax,b-Vmax,a determines the required condition on the numerators. We assume that Vmax,b > Vmax,a, noting that if Vmax,b < Vmax,a, a positive steady state cannot be globally stable because for X such that fa(X) > Vmax,b, the system will diverge regardless of the value of Y.

Under the assumption that Vmax,b > Vmax,a, the denominator of both b and c is positive, meaning a positive steady state exists only if the nominators of b or c (or both) are negative. Thus, two options may arise.

We now turn to analyze the stability of the steady state. For a steady state to be stable, the eigenvalues of the Jacobian matrix must have negative real values. In our system it holds thatX˙=fa-fbY˙=fb-fc

We use the following notation:α=d⁢fad⁢X=Vmax,a⁢KM,a(KM,a+X)2βx=∂⁡fb∂⁡X=Vmax,b⁢(KX+Y⁢(1+KXKY))(KX+X+KX⁢YKY)2βy=∂⁡fb∂⁡Y=-Vmax,b⁢(KX+X⁢(1+KXKY))(KX+X+KX⁢YKY)2d⁢fcd⁢Y=D

We can use this notation to write the Jacobian matrix as:J=(α-βx-βyβxβy-D)

which gives a characteristic polynomial of:(α-βx-λ)⁢(βy-D-λ)+βy⁢βx=0

In order for the real values of the roots of the characteristic polynomial to be negative it must hold that b>0 and c>0, where b and c are now the coefficients of the quadratic equation a⁢λ2+b⁢λ+c=0. We therefore get that:{b=βx−α−βy+D > 0c=(α−βx)(βy−D)+βyβx=βxD+αβy−αD > 0

We denote by f* the steady state flux in the system, such that f*=fa=fb=fc We note that for MM kinetics and positive concentrations it holds that:α > 0βx > 0−βy > βxβx+βy=−f∗1+KXKYKX+X+KXYKY

First, we note that if α≥βx then the steady state cannot be stable as, looking at the value of c, we see that in such a case (βx−α)D < 0 and since αβy < 0, c<0 violating the stability conditions. However, because we assume that Vmax,b>Vmax,a, then for Y=Y*, at X=0, fb<fa, but for X→∞, fb→Vmax,b and fa→Vmax,a, so that fb>fa. It then follows that, because the two fluxes can only intersect once for positive X and fixed Y, at the steady state point, where fa=fb, α<βx, so this condition is satisfied. We note that this condition is sufficient to ensure that b>0. We also note that as α<βx, a large enough value of D exists at which the steady state is stable, concluding that if D is large enough, then a stable steady state exists if:{Vmax,b>Vmax,aVmax,bKX<Vmax,aKM,a

If D is small, such that D<Vmax,a/KM,a, and Vmax,b>Vmax,a (implying that α<βx), we need to check what other conditions are necessary in order to ensure that βxD+αβy−αD>0. We look at the limit Vmax,b→∞. At this limit, the quadratic equation for X* converges to:0=(X∗)2+(2KM,a−Vmax,aD)X∗+KM,a2−Vmax,aKM,aD

For this equation, c<0, implying that one of the roots is negative and one is positive. The positive root is:X*=Vmax,aD-KM,a

As this X* is finite, we get that when Vmax,b→∞, Y* also converges to Vmax,aD-KM,a. At this limit, βx increases infinitely and βy decreases infinitely, but βx+βy converges to:-f*⁢(1+KXKY)KX+(Vmax,aD-KM,a)⁢(1+KXKY)

that is constant. Therefore, rearranging c such that:c=(βx+βy)D−βy(D−α)−αD>0

we note that as Vmax,b increases, the dominant term becomes −βy(D−α)>0 ensuring that c>0 and therefore stability.

On the other hand, when Vmax,b→Vmax,a, we note that because fc<Vmax,a, Y* is bounded by Y∗<Vmax,aD, but X*→∞. Thus, both α and βx diminish like 1X*2, and βy diminishes like 1X. The dominant term in c=βx⁢D+βy⁢α-α⁢D therefore becomes (βx−α)D>0 so again stability is maintained.

Therefore, for small values of D, as long as Vmax,b>Vmax,a, a positive stable steady state exists both in the lower limit of Vmax,b→Vmax,a, and in the upper limit of Vmax,b→∞.

Our conclusions are therefore as follows: As in the irreversible case, Vmax,b>Vmax,a is a necessary condition for the existence of a globally stable steady state. For large values of D, the reversible reaction is far from equilibrium, resulting in an additional condition, equivalent to the condition we obtained for the irreversible case, namely that Vmax,b/KX is upper bounded by a term that is larger than Vmax,a/KM,a, but approaches it as D increases. This condition is sufficient for the existence and stability of the steady state. For small values of D, a steady state always exists (given that Vmax,b>Vmax,a). We can show that this steady state is stable both when Vmax,b→∞, and when Vmax,b→Vmax,a. We therefore conclude that in this case, no further restrictions apply on KX, KY, or KM,a but rather that a steady state can always be achieved at most by changing Vmax,b.

Qualitatively, the cases we analyze show that, on top of the required Vmax,b>Vmax,a condition, the second condition is that either the slope of fc=D is smaller than Vmax,a/KM,a, or that the maximal slope of fb, Vmax,b/KX, is smaller than Vmax,a/KM,a.

## Extending the stability analysis from single to multiple reaction cycles

We analyze the stability criteria for the autocatalytic cycles depicted in Figure 5A and B. We start by writing the relevant equations for the autocatalytic cycle depicted in Figure 5A. In this system, there are two intermediate metabolites, X1 and X2, two reactions that form the cycle, fa1 and fa2, and two branch reactions, fb1 and fb2. We assume, without loss of generality, that the autocatalytic reaction (the reaction that increases the amount of carbon in the cycle) is fa2 and that the autocatalysis is in a 1:2 ratio. The equations describing the dynamics of the system are thus:X1˙=2fa2−fa1−fb1X2˙=fa1−fa2−fb2

We note that in steady state, where X.1=X.2=0, because the autocatalysis is in a 1:2 ratio, it must hold that fb1+fb2=fa2, meaning the total outgoing flux balances the total increase of intermediate metabolites due to autocatalysis. Given that a steady state of the system exists for some value (X1*,X2*), we can evaluate the condition for stability. In multi-variable systems, stability dictates that the real part of the eigenvalues of the Jacobian matrix must all be negative. We define αi=∂⁡fai∂⁡Xi and βi=∂⁡fbi∂⁡Xi for i=1,2. We note that as we assume Michaelis Menten kinetics, αi>0 and βi≥0, where βi=0 is the case where there is no flux branching out at i. We then get that the Jacobian matrix is:J=(-(α1+β1)2⁢α2α1-(α2+β2))

Solving for the characteristic polynomial gives:0=(λ+α1+β1)(λ+α2+β2)−2α1α2=λ2+(α1+β1+α2+β2)λ+(α1+β1)(α2+β2)−2α1α2

that has two negative roots when:(α1+β1)(α2+β2)−2α1α2>0⇒(1+β1α1)(1+β2α2)>2

which is satisfied if β1>α1 or β2>α2. Therefore, if either β1>α1 or β2>α2 at the steady state, then the steady state is stable.

The two-metabolites cycle case can be easily extended to a larger number of intermediate metabolites and reactions, as is depicted in Figure 5B. For this extension, we again assume, without loss of generality, that the autocatalytic reaction is the last reaction, fan, and that the autocatalysis is in a 1:2 ratio.

In this case, steady state implies that the concentration of each intermediate metabolite is conserved, meaning that for all i>1:(28)Xi˙=0⇒fai−1−fai−fbi=0⇒fai−1≥fai

(for i=1, as fan is the autocatalytic reaction, we get that 2⋅fan≥fa1). Also, because at steady state the total outgoing flux from the cycle must balance the total incoming flux into the system, which is the amount of autocatalysis carried out by fan, we get that:∑i=1nfbi=fan

(due to our assumption of a 1:2 autocatalytic ratio) implying that for all i:(29)fbi≤fan

We stress that Equation 29 is only valid if the autocatalysis is in up to a 1:2 ratio. Deriving a stability criterion for the multiple-reaction case, we get that in this case a steady state is stable if there exists i such that βi>αi (see section 9 below).

To conclude, for the straightforward extension of the simple model to multiple reactions with a single autocatalytic reaction, steady state implies that for all i:(30)fbi≤fan≤fai

Where the left inequality is due to Equation 29 and the right inequality is due to Equation 28.

A sufficient condition for such a steady state point to be stable is that at the steady state point there exists at least one branching point i at which the derivative of the branch reaction is larger than the derivative of the equivalent autocatalytic reaction:(31)βi>αi

## Limits on derivatives of branch reactions for complex autocatalytic cycles

Stability analysis of a model complex autocatalytic cycle with n reactions in the cycle results in the following Jacobian matrix:(32)J=(-(α1+β1)0⋯02⁢αnα1-(α2+β2)⋯00⋮⋮⋱⋮⋮00⋯-(αn-1+βn-1)000⋯αn-1-(αn+βn))

The characteristic polynomial of this matrix is given by:(33)0=∏i=1n(λ+αi+βi)-2⁢∏i=1nαi

To extract the conditions under which all the roots of the characteristic polynomial have negative real parts we use Rouche’s theorem. Our strategy will be as follows: We will define a contour that contains only numbers with negative real parts. We will show that all the roots of the polynomial 0=∏i=1n(λ+αi+βi) lie within the area this contour encloses. We will find the conditions for which |∏i=1n(λ+αi+βi)|>2⁢∏i=1nαi on the contour, satisfying the premise of Rouche’s theorem. We will then claim that under these conditions all the roots of the polynomial in Equation 33 must also lie inside the contour, and therefore must have negative real parts. Given that all the roots of this polynomial have negative real parts, we will conclude that the eigenvalues of the Jacobian matrix at the steady state point all have negative real parts, making the steady state point stable.

## Proof

We pick a large parameter R, such that R>3 maxj(αj+βj). We look at the closed half circle contour, K, composed of the segment [(0,-i⁢R),(0,i⁢R)] and the half circle arc (x,i⁢y) such that x≤0 and x2+y2=R2. We defineg⁢(λ)=2⁢∏j=1nαj

noting that it is constant over all of ℂ and specifically over K. We definef⁢(λ)=∏j=1n(λ+αj+βj)

noting that all of f’s roots lie inside K as the roots are 0>−(αj+βj)>−R for all j. We check the conditions under which |f⁢(λ)|>|g⁢(λ)| over the contour K.

For the arc segment we note that, as for complex numbers it holds that |x⁢y|=|x|⁢|y|, then|f⁢(λ)|=∏j=1n|λ+αj+βj|

From the triangle inequality we know that |x+y|≥|x|-|y| and therefore for all j it holds that|λ+αj+βj|≥R-(αj+βj)

As we picked R such that R>3 maxj(αj+βj) we get thatR−(αj+βj)>2(αj+βj)

and therefore∏j=1n|λ+αj+βj|>∏j=1n2|αj+βj|>∏j=1n2|αj|=|g(λ)|

concluding that over the arc, |f(λ)|>|g(λ)|.

For the part of K on the imaginary axis, we note that λ=i⁢y where y∈[-R,R]. For this segment we therefore get that|f⁢(λ)|=∏j=1n|αj+βj+i⁢y|=∏j=1n((αj+βj)2+y2)≥∏j=1n(αj+βj)2

and, as before, that|g⁢(λ)|=2⁢∏j=1nαj2

To meet the condition that |f(λ)|>|g(λ)|, which is equivalent to: |f(λ)||g(λ)|>1, it is sufficient to find the conditions under which:∏j=1n(αj+βj)22∏j=1nαj2>1

Simplifying this inequality gives:12∏j=1n(αj+βj)2αj2=12∏j=1nαj+βjαj=12∏j=1n(1+βjαj)>1⇒∏j=1n(1+βjαj)>2

A sufficient condition to satisfy this inequality, given that all the αj are positive and all the βj’s are non negative, is that there exists j such that βj>αj.

We therefore get that if there exists j such that βj>αj, then |f(λ)|>|g(λ)| over the contour K. In this case, by Rouche’s theorem, we deduce that, as all of f’s roots lie inside K, then it follows that all of f-g’s roots lie inside K, concluding that the real part of all of the eigenvalues of the characteristic polynomial of the Jacobian matrix of the complex autocatalytic cycle are negative, making any steady state that meets this criterion stable.

## Multiple unsaturated branch reactions increase convergence speed and dampen oscillations

Using the Jacobian matrix from Equation 32 we can analyze the effect of multiple low saturation branch points on convergence to steady state. The analysis shows that the more i’s exist for which βi>0, and the larger βi is (resulting in lower saturation of fbi), the faster the convergence of the cycle to steady state will be.

We denote by X*→ the steady state vector of the concentrations of the intermediate metabolites. We denote by X→=X*→+Δ⁢Xj a state where for all the intermediate metabolites that are not Xj, their concentration is the same as the steady state concentration, and Xj differs by a small amount, Δ⁢Xj, from its steady state concentration. We let F denote the fluxes function of the system such that F⁢(X)=X˙|X→. Evaluating the dynamics of the system at X→ by noting that F⁢(X→)≈F⁢(X*→)+J⋅Δ⁢Xj=J⋅Δ⁢Xj (where F⁢(X*→)=0 as X*→ is a steady state) results in F⁢(X→)k=0 for all k≠j,j+1. For Xj such that j≠n we get F⁢(X→)j≈-(αj+βj)⁢Δ⁢Xj and for Xj+1 we get F⁢(X→)j+1≈αj⁢Δ⁢Xj. Therefore, the difference from the steady state decreases proportionally to βj (and cycles to the next intermediate metabolite, Xj+1). For j=n, we get that F⁢(X→)j≈-(αj+βj)⁢Δ⁢Xj, as for j≠n, but F⁢(X→)1≈2⁢αj⁢Δ⁢Xj where the factor of 2 is due to the effect of the assimilating reaction, that causes an amplification of the deviation from steady state (an amplification that is dampened by subsequent reactions along the cycle if the conditions for stable steady state are satisfied).

It therefore follows that any increase in βj, for any j, increases the speed of convergence to steady state and reduces the propagation of deviations from steady state for Xj. Because of the linearity of matrix multiplication, an arbitrary deviation from X*→ can always be decomposed to individual deviations with respect to every intermediate metabolite, making the analysis above valid for such deviations as well. Thus, to keep deviations from steady state at check, it is beneficial to increase βj, for all j, which implies decreasing the saturation of fbj.

## Inverse relationship between derivatives, affinities, and saturation levels

It turns out that for the Michaelis-Menten kinetics equations, the following useful lemma can be used to connect theoretical observations on the relationships of derivatives to physiological observations on affinities and saturation levels.

We define the saturation level of a reaction as the ratio between the flux it carries, and the maximal flux it can carry, given the expression level of the relevant enzyme, that is:S⁢(X)=f⁢(X)Vmax=XKM+X

Given this definition we can show that if two Michaelis-Menten reactions consume the same metabolite, X, and at a given concentration, X*, it holds that fa⁢(X*)≥fb⁢(X*), then if:(34)dfbdX|X=X∗>dfadX|X=X∗

then it follows that:(35){KM,b>KM,aSb(X∗)<Sa(X∗)

Proof: expanding the condition that fa⁢(X*)≥fb⁢(X*), we get that:(36)Vmax,b⁢X*KM,b+X*≤Vmax,a⁢X*KM,a+X*⇒Vmax,bKM,b+X*≤Vmax,aKM,a+X*

Expanding the premise of the lemma in Equation 34 gives us that:dfbdX|X=X∗>dfadX|X=X∗⇒Vmax,bKM,b(KM,b+X∗)2>Vmax,aKM,a(KM,a+X∗)2

Because Equation 36 holds, it follows that:KM,bKM,b+X∗>KM,aKM,a+X∗⇒11+X∗KM,b>11+X∗KM,a⇒KM,b>KM,a

setting the affinity of the autocatalytic enzyme as a lower bound for the affinity of the branch enzyme. Finally, given this relation of affinities it follows that:KM,b>KM,a⇒X∗+KM,b>X∗+KM,a⇒X∗X∗+KM,b<X∗X∗+KM,a⇒Sb(X∗)<Sa(X∗)

concluding the proof.

We note that a multiple reaction autocatalytic cycle at a stable steady state point satisfies Equations 30 and 31, so the lemma applies.

## Evaluating maximal flux capacity of reactions under a given condition

To evaluate the maximal flux capacity of a reaction under a prescribed growth condition, given expression level and flux data for a set of conditions, we follow the procedure described in Davidi et al. (2016). For each reaction, under every condition, we divide the flux the reaction carries (obtained from Gerosa et al., 2015) by the amount of the corresponding enzyme expressed under that condition (obtained from Schmidt et al., 2016). We thus get a flux per enzyme estimate for the given reaction under each of the conditions. We define the enzyme maximal in-vivo catalytic rate as the maximum flux per unit enzyme it carries across all conditions analyzed (noting that this is actually only a lower bound on this rate). Multiplying the enzyme maximal catalytic rate by the enzyme amount at each condition results in an estimate of the maximal possible flux through the given reaction under the relevant condition.

## Allosteric regulation can improve network performance

In this section we touch upon the potential (in somewhat simplified and naively non-rigorous terms) of allosteric regulation to improve the properties of autocatalytic cycles. The constraint on the affinity of the branch reaction imposed by the stability requirement (Equation 35) may be suboptimal under other flux modes. Furthermore, allosteric regulation can be used to accelerate the rate at which an autocatalytic cycle converges to its stable steady state mode. While many allosteric regulation schemes exist (Leskovac, 2003), all of these schemes affect the affinity of the regulated enzyme, and some of these schemes also affect the maximal rate. We qualitatively analyze the expected regulation benefits for autocatalytic cycles.

From the perspective of the simple model, we recall that X˙=fa-fb. If the cycle is such that some steady state concentration, X*, is the desired value for biological function, then for levels of X below X* convergence will be faster if fa is increased and fb is decreased, compared with their values at X*. Conversely, for levels of X above X*, convergence will be faster if fa is decreased and fb is increased, compared with their values at X*. Convergence to X* can therefore be accelerated if, for example, X activates the branch reactions and inhibits the cycle reactions.

The assimilated metabolite can also allosterically regulate the reactions of the cycle. We assume that the desired steady state, denoted X^, does not depend on the concentration of the assimilated metabolite, A. Under this assumption, we further assume that X^ is attained for some constant concentration of the assimilated metabolite, A^. It then follows that because the autocatalytic activity is higher when A>A^, then in order to maintain X* close to its desired level, when A>A^, fa should be inhibited, and fb should be activated, but when A<A^, fa should be activated, and fb should be inhibited. Therefore, to increase the robustness of the steady state concentration to changes in the concentration of the assimilated metabolite, the assimilated metabolite should inhibit the cycle reactions and activate the branch reactions.

Another possible class of regulators are the products of the branch reactions. Taking a somewhat simplistic view, if the level of Y, the product of a branch reaction is low, this can indicate that the cycle does not carry sufficient flux to supply the demand for Y. Regulation can then be used to increase X*. From Equation 7, we get that the steady state concentration, X*, increases as KM,b increases and Vmax,b decreases, corresponding to inhibition of fb, and that X* decreases as KM,a increases and Vmax,a decreases, corresponding to inhibition of fa. So, to tune autocatalytic fluxes to match the demands of Y, regulation should increase X* when Y is low, by activating the recycling and autocatalytic reactions and inhibiting the branch reactions. On the other hand, regulation should decrease X* when Y is high, by inhibiting the autocatalytic reactions and activating the branch reactions. Therefore, to synchronize the demand of the cycle product with the cycle flux, the cycle branch products should inhibit the cycle reactions and activate the branch reactions.

Finally, we note that in the autocatalytic cycles we identify in central carbon metabolism, there are also reactions that operate in the reverse direction to the branch reactions, such that they consume products of the cycle and produce intermediate metabolites of the cycle. As such reactions are mirror images of branch reactions, we expect them to be oppositely regulated to branch reactions.

We find that these predictions hold for the cycle using the PTS, that is known to be allosterically controlled, but not for the glyoxylate cycle, which is known to be transcriptionally controlled (Gerosa et al., 2015).

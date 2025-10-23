# Peer review - Round 1

Editors:
- Silke Hauf, Virginia Tech United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65654.sa1](https://doi.org/10.7554/eLife.65654.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper uses a light-induced, synthetic gene expression system in mammalian cells to show that mean gene expression and variability ('noise') of expression can be independently tuned by modulating the light input. This expands this general strategy from yeast to mammalian cells and provides a tool to study the functional consequences of expression variability in mammalian cells. The paper also reports an impressive amount of single-cell data on gene expression and chromatin state which suggest that variations in histone acetylation state contribute to the expression variability.

Decision letter after peer review:

Thank you for submitting your article "Quantitative Control of Noise in Mammalian Gene Expression by Dynamic Histone Regulations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

This paper offers two main results:

(1) proposed model of bistability via CBP/p300 positive feedback

(2) reducing bimodality via PWM of light.

Result #2 is new for the mammalian system but has previously been shown in yeast. Result #1 requires additional data to be shown conclusively.

Essential revisions:

1) The proposed model has weaknesses that need to be addressed: (i) the model is conceptually not clear enough, (ii) the corresponding mathematical model is not calibrated with experimental data, (iii) some of the existing data seem to contradict the model, (iv) the model needs to be more thoroughly tested.

(i) Conceptual consistency and clarity should be improved: in a deterministic setting, bistability in positive feedback loops is well-defined, but the effect of PWM would be a stabilization of an unstable steady-state, as in https://www.nature.com/articles/s41467-017-01498-0. In the stochastic setting, stochastic promoter switching would be sufficient, and bistability is ill-defined, as demonstrated in https://www.nature.com/articles/s41467-018-05882-2#Sec25. Positive feedback via histone modifications could be consistent with either scenario, and depends on the experimental evidence for alternate, deterministically stable steady states. The experimental data in Figures 1D and 3D only weakly support the notion of 'low' and 'high' alternate states (especially because protein abundances are bounded from below and potentially also from above due to general expression capacity or simply applied input ranges), compared to the simulated data in Figure 2F. More direct evidence for bistability would be given by experiments that demonstrate hysteresis, which should be considered-see (iv).

(ii) The ODE model presented is not calibrated with experimental data and therefore of limited value for data interpretation. The authors should either (1) de-emphasize the mathematical model, acknowledging its limitations, or (2) include a calibrated mathematical model-for example, using a stochastic model as in Benzinger and Khammash. The inclusion of multiple reporters (see iii) would be a benefit. The authors could fit to their flow/genomic data to obtain further insights into how/why PWM of light suppresses noise. The current model represents cell-to-cell variability by cell-specific parametrization, and hence only contains extrinsic noise components.

(iii) Multiple copies of GAVPO-mRuby reporter in HeLa-AB1 strain and the measured bimodal response suggest that the current model is wrong. According to the authors' proposed model, each integrated GAVPO reporter gene (mRuby) should be independently bistable because local GAVPO binding and chromatin modifications regulate mRuby expression in cis. Figure 3—figure supplement 1 shows that there are 9 copies of GAVPO-mRuby plasmid B1 integrated at different locations in HeLa-AB1 strain. Thus, at intermediate AM light intensity, the mRuby gene expression should be deca-modal (10 modes), not bimodal (as shown in Figures 1 – 2). Something seems inconsistent between the local chromatin positive feedback model and the observed data.

The mathematical model used to validate the observations does not model the total expression from 9 independent promoters, which is a critical omission given the cis-nature of the positive feedback loop. The fact that these 9 promoters generate 2 peaks at intermediate light intensity suggests that the GAVPO bistability likely originates from a trans-effect, i.e., either all 9 promoters are OFF or all 9 promoters are ON, not a cis-effect.

In addition, from Figure 1—figure supplement 2G, it appears that when cells are exposed to light, it is mostly the cells containing a higher amount of GFP-GAVPO that switch into the mRuby ON state. Is it possible that the bistability simply comes from the dimerization event caused by light?

(iv) A bimodal response is consistent with bistability, but it does not prove bistability. To unambiguously show bistability, the authors should (1) measure and show dynamic signatures of bistability (e.g., hysteresis and/or following single cell dynamics to prove signature of two stable basins of attraction with transitions at some threshold GAVPO concentration) and (2) test their proposed model with precise, mechanistic mutations. The most compelling evidence in favor of their model is the use of the A-485 inhibitor of HAT activity of p300/CBP (i.e., prevent positive feedback loop) to convert the bimodal profile into a unimodal and graded profile. However, this is a crude perturbation because A-485 likely affects the expression of many genes, including any cis- and trans-factors that affect mRuby gene expression. Mutations specific to GAVPO and mRuby promoter that destroy positive feedback would be the cleanest perturbation.

Suggestions:

1. Replace the p65A activation domain with mutants that activate transcription by recruiting RNA Pol II but which cannot recruit CBP/p300 and modify histones, e.g. "Minimal activators that bind to the KIX domain of p300/CBP identified by phage display screening", Frangioni et al., Nature Biotechnology (2000). If such p65A mutants don't exist, there are VP16 activation domains that can separate p300/CBP-recruiting versus TFII-recruiting functions, e.g. "The H1 and H2 regions of the activation domain of herpes simplex virion protein 16 stimulate transcription through distinct molecular mechanisms, Ikeda et al., Genes to Cells (2002). Prediction: If p300/CBP recruitment is essential for positive feedback, then you will no longer see a bistable response. If you see bistability, then an alternative should be considered more seriously.

2. Use a monomeric transcription factor regulated by a chemical (e.g. Zinc-finger-ER-p65) and engineer a mRuby promoter with a single binding site. Prediction: This system should exhibit bistable mRuby response at intermediate hormone concentrations, if your model is correct. NOTE: The authors already use an rtTA doxycycline-inducible system in Figure 2—figure supplement 2, which has VP16 activation domain, and exhibits a bimodal distribution at intermediate doxycycline concentrations. The authors could modify VP16 to abolish p300/CBP recruitment of the rtTA construct.

2) In its current form, Figure 5 does not convincingly show that PWM reduces noise:

(i) In Panel E, at time 0 (no light induction), AM 100 uW, 25 uW and PWM start at different CV values. It is unclear why this is the case especially since this is not observed in the mRuby CV. This needs to be addressed.

(ii) The authors should add a panel to Figure 5 showing the mean mRNA levels for the three respective cases, AM 100 uW, 25 uW and PWM 200m.

(iii) A discussion should be included about the large number of cells showing almost no mRNA for AM 25 uW and PWM 200m, does this means that there are cells trapped in the off state, and how do these cells impact the CV calculations?

(iv) Since the pulsatile behavior appears in ~15% of the cells (Figure 5C), how does the CV time course behave if CV is only calculated for these cells exhibiting pulsatile behavior.

3) Figure 1E/F and around line 120: The argument of 'limited noise of GFP-GAVPO' requires more details, namely a quantitative analysis of this noise and the effects of noise propagation – the current analysis focuses on relations between means and it is not clear what the effect of GAVPO expression noise on mRuby noise is. In addition, TetR-GFP-nuc may not accurately reflect GAVPO noise if the stabilities of the two proteins are different.

4) TetR-noise reducing circuit (or Plasmid A1). The design or purpose of this plasmid is a little confusing. The TetR-GFP-nuc synthetic transcription factor binds to its CMV promoter to repress its own transcription (negative feedback loop). This should repress mean gene expression and "squeeze" the expression variance about the mean (ref: Becskei et al., Nature 2000), i.e. noise reducing. However, the authors added doxycycline one day before the start of light induction and then maintained it throughout the experiment. This would destroy the negative feedback loop and, thus, increase the TetR and GAVPO mean and variance back to unrepressed CMV promoter levels. Are the authors using this circuit to keep TetR and GAVPO low until the start of the experiment (conditional expression) or are the authors using this circuit to reduce variance in TetR and GAVPO levels (noise-reduction)? Please clarify how and why you are using this circuit.

5) Although not essential in a revised manuscript, testing systems beyond light-regulated GAVPO would strengthen the generality of the authors' conclusions. The good news is that their rtTA system (which has a VP16 trans-activation domain that recruits both p300/CBP and RNA Poll II) exhibits bimodal distribution at intermediate concentrations of doxycycline (Figure 2—figure supplement 2), so they have a different system, strains, and preliminary results to test the generality of their model.

Presentation:

6) The text requires thorough language editing throughout. Widespread grammatical mistakes-in particular on verb tense and singular/plural-make it difficult to follow the arguments.

7) If the authors decide to include a calibrated mathematical model, the model should be more clearly described in the main text (not only in the Supplementary Material).

8) A brief description of how the light inducible GAVPO system works would be helpful either in the introduction or the beginning of the Results section. Perhaps adding Figure 1—figure supplement 1 to Figure 1.

9) Please add a schematic in Figure 1 or the supplement that clearly illustrates how the light is pulsed (i.e., duration of on time and off time), the light intensity used per pulse, and the mean light intensity. Something similar to Figure 4 D-E, yet for all period lengths.

10) Please explain and/or motivate the use of different PWM regimes to provide evidence for different aspects of the work, e.g., line 137 400min period, line 261 600min, line 296, 200min).

11) Figure 2—figure supplement 1 is a confusing figure because it makes two different points. The first half (A-F) shows that LMK-235 has a minor impact on noise reduction. The second half (G-L) shows that a different strain F9-AB2 shows identical signatures to the HeLa-AB1 strain, i.e. bimodality at intermediate levels of AM light, which is reduced to unimodal by FM light. Perhaps split these data into separate supplementary figures? In lines 205 – 207, these data are referred to as "figure supplement 2".

12) In mouse embryonic stem cells (Figure 1—figure supplement 3), there is only a clear noise reduction effect with 200 and 400 minutes, yet for these there is also a decrease in mean GFP levels. Therefore, the ability to modulate noise independent of mean seems not to hold in mouse embryonic stem cells. Please state this more clearly (text lines 149-154).

13) Please provide more detailed explanations of the somewhat puzzling chromatin state dynamics in Figure 4 where a longer-term drift (denoted as epigenetic 'memory') is apparent. How do these dynamics relate to the data presented in Figure 1 (the Methods seem to suggest a measurement time at 48h, but this is not specified in the captions).

14) The title 'RNA dynamics flattens PWM-induced pulsatile chromatin opening' implies an influence of RNA dynamics on chromatin state, which is not plausible given the construction of the synthetic system (the mRNA does not encode a protein that could modify chromatin state) and the postulated model (positive feedback is established via TF binding, not mRNA expression). mRNA dynamics will impact protein dynamics, and the title and text should reflect this aspect.

15) Figure 2B and Line 943: If there are only 4 data points from 4 independent experiments, why not show them rather than summarize their statistics with a box-whisker plot?

16) Line 303/Figure 5C: The export of mRNA from the nucleus to the cytoplasm, which is mentioned in the text, is not shown in the figure that is cited.

17) Line 248: cite Figure 3H in addition to Figure 3—figure supplement 1A.

18) Please write out "min" instead of "m" for the pulse periods in the figure legends.

19) Prior work on the use of PWM and available explanations for its noise-reducing effect should be mentioned and discussed more explicitly.

20) A publication that came out recently and also describes independent control of mean expression and variability could be cited: https://doi.org/10.1038/s41467-020-20467-8.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Quantitative Control of Noise in Mammalian Gene Expression by Dynamic Histone Regulations" for further consideration by eLife. Your revised article has been evaluated by all three original reviewers, Kevin Struhl as the Senior Editor, and a Reviewing Editor.

Thank you for performing additional experiments. The manuscript has been improved but remaining issues make the paper not acceptable for publication in eLife in its current form.

In particular, all reviewers felt that bistability of the system is still not well enough supported to make this a major claim of the paper.

On the other hand, your findings on PWM-mediated noise suppression in mammalian cells and the link to histone modifications are interesting and large enough an advance for publication. Your data strongly support the idea that CBP/p300 recruitment via chromatin acetylation leads to bimodal gene expression at intermediate GAVPO activity and that PWM of GAVPO activity via light can sculpt the bimodal output to be unimodal.

While you could perform additional experiments to attempt to demonstrate bistability (see under point 2 below), we recommend to remove this claim from the paper, replace "bistable" with "bimodal", remove the ODE model, and discuss your findings in a more balanced way that leaves room for alternative interpretations.

If you want to maintain your conclusion regarding bistability with the current data, you will need to submit to another journal as a home for your paper.

Necessary changes for a revision of your paper for eLife include:

– Re-writing the second half of the abstract, lines 23 – 29.

– Re-writing the end of the Introduction, lines 83 – 96.

– Considering the criticism of the data in Figure 1H (see below) and modify that section (line 123-137).

– Line 227 – 236: Make it clear that this is a working model, but other models are possible. (This may then be better suited for the discussion.)

– Line 237 – 273: Please see comments under point 2 below. These experiments do not strongly support bistability and the conclusions need to be re-phrased. The model (lines 284-295) could be removed.

– Modify the discussion in lines 493 – 507 and 518-539, since these conclusions are not well supported.

– Discussion paragraph starting in line 540 needs an introduction.

– More of the limitations in the experiments that you discuss in the response to the reviewers (e.g. point 2, 3, 10, 13 in the previous decision letter) could show up in the paper itself, so that readers are made aware of those.

– Generally, re-assess all mentions of bistability, hysteresis and positive feedback loop.

Note that, while we point out specific passages to modify, you may want to re-consider the structure of your paper given these major changes.

Specific criticisms:

(1) Figure 1H aims to demonstrate that bistability and not cooperativity in gene expression (as in Benzinger and Khammash) underlies the observed population distributions by propagating GAVPO distributions through empirical (from Figure 1G data) and hypothetical high-cooperativity transfer functions to predict mRuby distributions. Details on methods are missing (and should be provided), but clearly the mRuby monomodal distribution for the empirical transfer function does not match (approximately) the distribution for AM, 20\muW/cm2 in Figure 1F and it is unclear if it does so for the mRuby marginal in Figure 1G (the raw data for this panel is not available), as would be expected. Furthermore, it is unclear, how the predicted mRuby marginal for high cooperativity was obtained. Very approximate simulations for both scenarios (Matlab code below) rather indicate the opposite of the authors' conclusions when compared to data in Figure 1F,G.

Matlab code on point (1):

%% cooperativity simulations (x: GAVPO, y: mRuby)

ns = 1e4;

d0 = table2array(readtable('88763_1_data_set_2024261_qtg66v.xlsx','sheet','Fig1H-3','range','a2:b122'));

cdf = cumsum(d0(:,2));

[~,idx] = unique(cdf);

x = interp1(cdf(idx),d0(idx,1),rand(ns,1));

% loop: cooperativity

hill = {@(x,k,n) 3 + 1*(x-4.5);.…

@(x,k,n) 3 + 2*x.^n./(k.^n+x.^n)};

n = 70;

k = 5.7;

figure();

for z = 1:length(hill)

subplot(3,2,z)

xi = linspace(4.5,6.5,100);

plot(xi,hill{z}(xi,k,n));

subplot(3,2,z+2)

y = hill{z}(x,k,n) +.25*randn(size(x));

ksdensity([x,y]);

view(2);

axis([4.5 6.5 2 6])

subplot(3,2,z+4);

histogram(y,'Normalization','pdf');

hold on;

histogram(x,'Normalization','pdf');

end

(2) Figure 2 aims to demonstrate bistability and hysteresis as proposed by the ODE model via single-cell time lapse microscopy (2F-H) and FACS (2I,J). The single-cell trajectories in Figure 2G, however, do not represent the population distribution. They were selected according to 'low' or 'high' mRuby signal at 24h; the data only demonstrates the dynamics for reaching the target state, and not bistability. For experiments demonstrating hysteresis, in the regime of bistability, one would expect distinct (bimodal under noise) distributions close to the 'low' or 'high' starting state. This is clearly not the case given the data in Figure 2I,J. The slight shift to higher mRuby in the intermediary regime (10-25 light intensity) used as an argument for hysteresis in the manuscript can be easily explained by the population not being in steady-state because the distribution for the predicted monostable 0 light input case is right-shifted by prior stimulation as well.

In brief, the single-cell experiments (Figure 2F-H) show a bimodal induction response. The OFF cells stay OFF and the ON cells stay ON. It would have been more convincing to see an induced ON cell stochastically cross a threshold and then return to the OFF state. Or the authors could have started with a fully induced population (100% ON with 100 uW/cm2 induction) then put at intermediate light and filmed single cells. The expectation would be that a fraction of the cells crosses the threshold and goes to the stable OFF state. Alternatively, the authors could have sorted ON and OFF cells, and then measured the time evolution of mRuby/mCardinal distribution of the OFF population and ON population.

# Author response - Round 1

Authors:
- Asuka Takeishi ([ORCID: 0000-0003-2485-867X](https://orcid.org/0000-0003-2485-867X))
- Jihye Yeon ([ORCID: 0000-0001-9995-1129](https://orcid.org/0000-0001-9995-1129))
- Nathan Harris ([ORCID: 0000-0002-7856-520X](https://orcid.org/0000-0002-7856-520X))
- Wenxing Yang
- Piali Sengupta ([ORCID: 0000-0001-7468-0035](https://orcid.org/0000-0001-7468-0035))

## Response text

DOI: [10.7554/eLife.61167.sa2](https://doi.org/10.7554/eLife.61167.sa2)

Reviewer #1:

[…] My only major quibble, which can be easily fixed, is that the elegant Cre/lox-mediated knockout of ins-1, very rigorous in principle, is not well enough described, particularly in regard to the negative controls. The authors state: "Knocking out ins-1 in all or a majority of ins-1-expressing cells, but not in AIA or AIZ/AIB, was sufficient to restore negative thermotaxis in starved animals (Figure 4A)." This sentence needs to be extended to state exactly what drivers were used to knock-out ins-1 where. The figure shows which cells were targeted, but does not show the driver.

We have now indicated the exact drivers used for each cell and tissue type both in the main text of the Results, as well as in the Figure 4A legend.

I would also like to see the specificity of these drivers (incl. the intestinal driver) being tested by an available "tester" strain in which a ubiquitous rfp transgene is excised, allowing expression of a gfp reporter (heIs105 from Van der Heuvel, Cell, 2015 paper). Based on unpublished lore, Cre is extremely effective even at very low concentrations and spurious expression of Cre drivers can result in very misleading results.

This is an important control and we thank the reviewer for the suggestion. To address this issue, we expressed Cre under ifb-2 (intestine), gcy-28d (AIA) and odr-2b(3a) (AIB and AIZ) promoters in the heIs105 recombination reporter strain. To allow for the identification of Cre-expressing neurons, we also expressed CFP under the gcy-28d and odr-2b(3a) promoters. As shown in a new Figure 4—figure supplement 1B, we observe robust GFP expression in the gut but not in neurons in strains expressing ifb-2p::Cre. Conversely, we observe co-expression of CFP and GFP in AIA and AIB/AIZ interneurons in strains expressing gcy-28dp::Cre and odr-2b(3a)p::Cre, respectively. The positions of the soma and axonal trajectories of these interneurons are consistent with their cell identification.

Reviewer #3:

• Earlier studies of AIY (Clark et al., 2006) indicate that calcium signals in these neurons faithfully follow those in AFD sensory neurons. It is not clear why in this study the authors see less faithful activation of AIYs (Figure 1F) by stimuli that consistently activate AFDs. The authors should explain this discrepancy.

AIY responses are different depending on the type of thermal stimulus that is used for activation. Clark et al., 2006, as well as other papers including those from our lab (Biron et al., 2006, Matsuyama and Mori, 2020) use a rising oscillatory temperature stimulus. AIY responses are time-locked to these stimuli (and correlated with AFD responses at least in some temperature ranges – see Matsuyama and Mori, 2020). In contrast, AIY responses are more probabilistic and follow AFD responses less faithfully in response to a linear rising temperature stimulus, particularly in the T>Tc or negative thermotaxis behavioral range (also see Hawk et al., 2018). The AIY calcium signals reported in this work in response to a linear rising temperature stimulus resemble those in the Hawk et al. paper (although we note that we use a shallower temperature ramp to more closely mimic the temperature changes experienced by animals navigating the thermal gradients in our behavioral assays).

• It is not clear that 'total response duration per neuron' is the best way to describe thermoresponses. This statistic does not capture the magnitude of a neuron's response, which probably matters as much as the duration of that response. The authors should analyze their data of neuronal responses in a way that also considers the magnitude of responses. This comment applies to multiple figure panels.

We describe three metrics for the calcium signals in each imaged neuron type: total response duration per neuron, average response duration per neuron, and response probability. Since with the exception of AFD calcium signals, temperature responses in all other examined neurons are stochastic, it is difficult to meaningfully quantify response amplitude. We also note that small differences in response amplitude can be artifactual, since response amplitude can be quite significantly affected by the expression level of the sensor.

• The authors' claim that fasting increases the temperature responses of AWCs (subsection “The AWC olfactory neurons integrate feeding state information into the thermotaxis circuit”, last sentence) requires a control showing that under isothermal conditions there is no difference in the activity of AWCs in fed and starved animals. It remains possible that feeding-state-dependent changes in neural activity are independent of temperature.

• Along the same line, the authors' discussion of AIA responses describes them as temperature responses, but there are no data from before or after the temperature ramp shown, nor are there data showing neural activity under isothermal conditions. As shown, these data do not support the claim that these cells are responding to temperature stimuli. This comment applies also to imaging data from ins-1 mutants shown in Figure 4.

In response to these very valid comments, we have now added a new Figure 2D and Figure 2—figure supplement 1D showing that AWC neuron responses are similar in fed and starved animals when held at a constant temperature of 20°C. We have also included a new Figure 3—figure supplement 1B and added new data to Figure 3—figure supplement 1C, showing that similar to the AWC neurons, AIA interneurons also do not exhibit differences in their calcium signals in fed and starved animals when held at a constant temperature of 20°C.These findings are consistent with our observation that the movement of fed and starved animals is largely indistinguishable under isothermal conditions, and is altered only on a thermal gradient (new Figure 1—figure supplement 1A).

• More analysis of the insulin signaling pathway is warranted. The authors should test whether loss of genes encoding daf-2 effectors, e.g. age-1 and pdk-1, show the same behavioral phenotype as daf-2 mutants.

Behavioral data from akt-1, age-1 and pdk-1 mutants are shown in Figure 4—figure supplement 2A.

• The authors' model predicts that fasting will not affect the activity of AIA interneurons in animals that either lack AWC neurons or whose AWC neurons are defective for insulin signaling. This should be tested.

While these are excellent suggestions, these are complex experiments to perform technically, and are challenging to complete under the current restrictions. We hope that the behavioral experiments demonstrating the role of glutamatergic signaling from AWC (Figure 3I) together with additional behavioral and imaging experiments described here support our model sufficiently.

• The authors' discussion of their study does not clearly put forth explanations of why thermotaxis and feeding state are coupled as they are. Is there some benefit to shutting down thermotaxis behavior when starved? Does thermotaxis occur at the expense of chemotaxis used to find food? This interesting phenomenon deserves some speculation.

We speculate on this briefly at the end of the first paragraph in the Discussion. In short, based on our previous observations that prolonged starvation increases olfactory responses in AWC (Neal et al., 2015), we propose that the altered sensory responses in AWC allow animals to prioritize food-finding over optimal thermoregulation.

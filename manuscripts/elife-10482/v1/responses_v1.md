# Author response - Round 1

Authors:
- Jeremy S Treger
- Michael F Priest
- Francisco Bezanilla

## Response text

DOI: [10.7554/eLife.10482.019](https://doi.org/10.7554/eLife.10482.019)

Essential revisions: 1) Remove the single-molecule studies from the paper.

Thank you for this comment, and we agree that it is too early to draw conclusions about voltage sensor function based on the data presented. Accordingly, in consultation with the editors, we have substantially revised the presentation of the single-molecule work. We have eliminated entirely the discussion of using ArcLight to learn about voltage sensor function. However, we strongly feel that the fluctuation noise discovered here has substantial implications for future GEVI use and development. In particular, the macroscopic summation of the noise, as well as the corresponding decrease in effective quantum yield compared to a non-fluctuating fluorophore, very likely serve to decrease the signal-to-noise ratio of many GEVI-derived signals, thus decreasing the resolving power of these tools for small signals. In addition to this, correctly-modulated pulsing may be of benefit for increasing signal from many GFP-based GEVIs, as previous work has demonstrated that this can improve signal form many fluorophores that visit dark states. Thus the discovery of this noise may serve to motivate new avenues of GEVI optimization that are distinct from and complementary to current directions. We hope you agree with us that this describes an important phenomenon that likely afflicts many current GEVIs and that it should remain a part of this manuscript in its revised form.

2) The authors demonstrate a close correlation between Q and F changes for the wt S4 construct, as well as the R217Q and R217E constructs, which is great to see, but then don't carefully analyze (or at least present) the multiexponential kinetics of either measure and look to see which match and which don't. It would be nice to show integrated Q traces, analyze those, and compare them with what is seen for F. With the two other mutants, it would be interesting to see how these change. The lag in F is also interesting, and it would be nice to show measure V traces as well as integrated Q traces so the reader can see how both V and Q change relative to F.

Thank you for these insightful suggestions. We have added two new figures to the section titled “ArcLight Fluorescence Changes are Slower than Gating Currents and Possess a Lag” that address these points. First, we compare the two time constants of both integrated gating charge and fluorescence and show that there are no obvious kinetic correlations between the two. We then show a pair of representative examples of overlaid V, Q, and F traces to more clearly show how they change in time relative to each other. Finally, we do a kinetics analysis of gating currents, fluorescence lags, and fluorescence kinetics for the R217R and R217E constructs and show that they have the same general behavior as the wild-type construct.

3) Please provide a comparison of the advantages and disadvantages of ArcLightning with other versions of optical voltage sensors (e.g. Mermaid, ElectricPk, VSFP).

The toolbox available to researchers interested in measuring changes in membrane potential grows larger each year and we are happy to compare our tool to those currently available. Additional information has been added in the last paragraph of the Discussion. Briefly, ElectricPk is faster but much smaller, and Mermaid and VSFP (and other closely related FRET based probes) are comparable in their abilities but take up a larger fraction of the visible light spectrum, making optical measurement of additional parameters challenging.

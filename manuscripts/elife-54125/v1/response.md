# Author response - Round 1

Authors:
- Ryan J Vaden ([ORCID: 0000-0001-8544-4003](https://orcid.org/0000-0001-8544-4003))
- Jose Carlos Gonzalez ([ORCID: 0000-0003-4612-1943](https://orcid.org/0000-0003-4612-1943))
- Ming-Chi Tsai ([ORCID: 0000-0002-6216-8672](https://orcid.org/0000-0002-6216-8672))
- Anastasia J Niver
- Allison R Fusilier
- Chelsea M Griffith
- Richard H Kramer ([ORCID: 0000-0002-8755-9389](https://orcid.org/0000-0002-8755-9389))
- Jacques I Wadiche ([ORCID: 0000-0001-8180-2061](https://orcid.org/0000-0001-8180-2061))
- Linda Overstreet-Wadiche ([ORCID: 0000-0001-7367-5998](https://orcid.org/0000-0001-7367-5998))

## Response text

DOI: [10.7554/eLife.54125.sa2](https://doi.org/10.7554/eLife.54125.sa2)

Essential revisions:

1) Co-localization for ChR2/PV should be done in the PV-ChR2 mice using immunostaining.

We now added images of PV immunostaining in PV-ChR2 mice to Figure 4A and Figure 4—figure supplement 1, as well as co-localization numbers to the text.

2) Please show that the slow GPSCs in adult are blocked by a GABAA receptor antagonist.

We have added new traces and data showing blockade of PV-GPSCs with gabazine in Figure 1 and Figure 6—figure supplement 1.

3) Paired PV-immature GC recordings (currently n=5 with 2 that showed spillover) could offer some additional insights into spillover transmission, namely in terms of whether it is somewhat cell-specific vs. "volume" transmission, etc.

To address the request for additional insight into whether PV spillover signaling is cell-specific versus “volume transmission”, we have now provided new experiments directly comparing volume and spillover transmission to newborn and mature GCs and additional discussion of the comparison. Volume transmission refers signaling from neurogliaform/ivy interneurons that release GABA into the extracellular space rather than at conventional postsynaptic anatomical specializations (Szabadics, 2007; Olah, 2009; Karayannis, 2010). We previously described electrically-evoked and unitary volume transmission to Pomc-EGFP newborn GCs (Markwardt et al., 2009, 2011) and now have confirmed optogenetic-evoked volume transmission from nNos-expressing neurogliaform interneurons (new Figure 3C, D, new Figure 3—figure supplement 1). We consider this to be cell type-specific signaling because it represents the normal mode of transmission for neurogliaform interneurons and thus GPSCs in newborn and mature GCs have similar characteristics indicative of volume transmission. In contrast, PV signaling to newborn and mature GCs has distinct characteristics that result from GABA released at mature GC synapses “spilling over” to act on newborn neurons. We consider this a form of non-specific signaling because spillover GABA is acting beyond the target established by anatomical synaptic connectivity. Discussion added in the subsection “Slow GPSCs from multiple interneuron subtypes”.

We think the direct demonstration of spillover versus volume transmission (Figure 3C, D, new Figure 3—figure supplement 1) is more informative than adding more n’s using paired recordings. The description of paired PV-immature GCs recordings (2/5 successes) might mistakenly give the impression that unitary GPSCs were frequent. However, we previously tested a large number of unlabeled interneurons for connectivity with newborn GCs and found a very low success rate (2.3%; 11 of 498 attempts), with none from PVs (Markwardt et al., 2011). Thus, the goal of experiments in Figure 6 was to illustrate that light-evoked GPSCs arise from multiple PVs as expected for transmitter “pooling” from multiple axons and release sites. We were surprised to find that in 2 recordings (on the same day), we evoked a unitary GPSC by direct stimulation of the PV. We’ve added rise and decay times for those unitary GPSCs to the text. But as other attempts at paired recordings have been unsuccessful, we don’t think this is a useful approach. Rather we conclude that it is possible to generate a spillover GPSC from a single PV, but optogenetic activation results from cooperative GABA pooling from many interneurons. We have altered the text to clarify these points.

4) One surprising result in Figure 2G is that full blockade of the α1 subunit responsible for the fast kinetics produces no change in the rise time in new or mature GCs, in contrast to what would have been expected, an increase in rise time. This inconsistency must be addressed.

While at first glance this might be surprising, our negative results are fully consistent with known determinants of compound or multi-synaptic responses in which additional factors, like asynchrony of release and transmitter pooling, make substantial contribution to the time course of evoked currents. This is why evoked IPSCs (and EPSCs) have slower rise and decay phases than mIPSCs/mEPSCs generated at the same synapses (i.e. Diamond and Jahr, 1995; Overstreet- and Westbrook, 2003). Further, the time course of GPSCs evoked by dendritic-projecting neurogliaform interneurons is dictated primarily by the spatial-temporal profile of [GABA] rather than receptor subunit composition (i.e. Szabadics et al., 2007; Karayanis et al. 2010). We have provided additional explanation of these points and cited some reviews addressing them (subsections “Differential Expression of α1 subunit cannot account for slow GPSCs” and “Mechanisms underlying slow GPSCs from PVs”).

Another way to confirm that factors other than subunit composition contribute to the difference in GPSCs between newborn and mature GCs is to compare the isolated α1 receptor-mediated GPSCs (since young GAD67-GPF cells have low levels of α1 receptors). If receptor kinetics dominant the IPSC kinetics, we would expect that α1 mediated currents will have the same kinetics regardless the transmitter profile. However, we observed that α1 mediated GPSC in young GCs have slower kinetics compared to that in mature GCs (new Figure 2—figure supplement 1). This result also indicates that differences in other subunits expression cannot account for the kinetic differences.

5) IPSC decay was faster after pre-conditioning pulses, presumably due to less GABA release. By this argument, the second IPSC during paired-pulse experiments in which there is paired-pulse depression should also be faster – is this the case?

This is a good point. We now report that the decay of the second IPSC in paired-pulse experiments is indeed faster than the decay of the first IPSC in both mature and newborn GCs. We have added this data to the subsection “PVs generate spillover to mature GCs”.

This should be addressed convincingly, using either new experiments (TPMPA) or with reanalysis of existing data if they are convincing. E.g., one might expect that the second response (in immature neurons) would be more sensitive to TPMPA than the first one.

We agree that fewer vesicles released following the second stimulus will likely generate a lower average [GABA] at receptors on newborn GCs compared to the first stimulus. However, TPMPA is insufficient to detect an expected 2-3-fold difference in [GABA]. To put this in perspective, we found that TPMPA generates a <20% differential block between GPSCs in mature and newborn GCs (Figure 3). Previous work indicates that a 20% differential block by TPMPA corresponds to ~ 100x difference in peak [GABA] between IPSCs at conventional synapses (est. peak [GABA] of 2-3 mM) and spillover-like transients from neurogliaform interneurons (est. peak [GABA] of 20-40 µM; Karayannis et al., 2010). Thus, if a 20% differential block corresponds to a 100x difference in peak [GABA], TPMPA would not be able to differentiate a much smaller difference in the [GABA] mediating the first and second spillover GPSC. Assessing the effect of TPMPA on the PPR is further complicated by evidence that TPMPA reduces frequency-dependent depression of spillover-like transients by protecting postsynaptic GABAA receptors from entering slow desensitized states that enhance frequency-dependent depression (Karayannis et al., 2010). We thank reviewers for reminding us to also make the point that the strong PPD at newborn synapses is consistent with a contribution of postsynaptic desensitization (now included in the subsection “Mechanisms underlying slow GPSCs from PVs”).

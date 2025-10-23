# Peer review - Round 1

Editors:
- Volker Dötsch, Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65620.sa1](https://doi.org/10.7554/eLife.65620.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Complementary biosensors reveal different G-protein signaling modes triggered by GPCRs and non-receptor activators" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Volker Dötsch as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jonathan Cooper as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sudarshan Rajagopal (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

One issue that was discussed in particular between the reviewers is the relevance of the proposed method to normal function in light of the overexpression used and the truncation of full-length proteins.

Essential revisions:

1) It would be good to somehow get a handle at how "out of range" the expression levels for these proteins are. How much more GIV is being produced compared to native? How much native GIV is membrane targeted as opposed to elsewhere? Has a CRISPR knock-in of the FA mutant of GIV been tested?

2) Although the BRET reporter system has been described before, it would be good still to describe it in Figure 1, so we don't have to dig in the experimentals to get a sense of how the various players are labeled.

3) The complex formation should not be described as "irreversible": "In one, the GDI R12 GL reduces the availability of Gα(GDP)-Gβγ by irreversibly binding to Gα-GDP." Unless it is covalent, it is reversible. It could be effectively irreversible if the affinities and protein concentrations are high enough (unclear that is the case here although reported affinities are order of magnitude better than that of GIV).

4) In Figure 6C the GIV data need some clarification. It appears because carbachol induces a similar shift in BRET in the presence of GIV compared to the GPCR alone, it is said that GIV does not hinder activation of the GPCR. It would seem that the pool of Gbg being released by GIV (before addition of carbachol) would be different than the pool of Gbg that the receptor liberates? This is different from the other three cases where the total BRET signal ends up being the same regardless of the protein. Why the difference?

5) It would be better to report SD rather than SE. SD measures the amount of variability, or dispersion, from the individual data values to the mean, while the standard error measures how far the sample mean (average) of the data is likely to be from the true population mean. In these experiments, one is more interested in the SD.

6) Gbg is also required for recruitment of GRK2. Has the author assessed GRK2 activity in this setting?

Reviewer #1:

Mikel Garcia-Marcos describes in this manuscript two different aspects: First he introduces a new method that can be used to investigate the effect of cellular effector proteins on the activation of G-proteins. This method is based on induced hetero-dimerization using the small drug rapamycin that has been established many years ago. He uses this system to recruit proteins with a presumed GEF activity to the membrane where they can interact with heterotrimeric G-proteins. The effect he measures on identifying the concentration of Gbeta/γ and Galpha-GTP.

In the second part he uses this system to investigate the effect of three GEF proteins on membrane-anchored Gi protein. He finds that within the group of three GEF proteins (GIV, AGS1 and Ric-8a), GIV promotes activation by dissociation of the Gbeta/γ dimer but not by formation of Galpha-GTP despite its in vitro GEF function. This result is surprising but the data are compelling.

Overall, the method is interesting, enlarging the tool box for investigating the activation mechanism of G-proteins. The data on the different GEF proteins are likewise interesting and within the framework of this assay plausible.

Reviewer #2:

This is an interesting manuscript that addresses a very important question in the field of G-protein signaling – whether their activation by G protein-coupled receptors (GPCRs) is similar to other activators of G protein signaling such as GIV, AGS1, etc. Such an analysis has previously been limited by a lack of tools to detect free Gbg and Ga-GTP formation. The author uses novel biosensors of Gai-GTP and Gbg to probe this system. The author finds that GIV, unlike other GBA proteins, activates G protein signaling in cells primarily through the formation of free Gbg rather than through the formation of Gai-GTP, although it has GEF activity in vitro. This is unlike AGS1, which triggers the formation of Gai-GTP. Notably, both R12 and AGS1 hinder activation of G proteins while GIV does not. This clearly demonstrates that activation of heterotrimeric G proteins can occur through multiple mechanisms with different signaling outcomes. Notably, a larger role for Gbg is appreciated in promoting signaling through a variety of pathways, including inhibition of adenylyl cyclase.

Reviewer #3:

In this paper, the author sought to study the ability of a series of non-receptor GEFs, in particular GIV/girdin, to activate both Galpha subunits and Gbg subunits under more physiological settings. About 11 years ago the lead author reported GEF activity by GIV using purified components, although this activity was lower than that mediated by GPCRs and at orders of magnitude higher EC50. Because GIV and some other non-receptor regulators (i.e. AGS1, and RGS12) can possess the ability to displace Gbg subunits, a key question that could be addressed with these experiments is whether it is the released Gbg subunits or the GEF activity that is important for GIV function in cells.

The strength of the approach used here is that the author can trigger recruitment of the G protein binding domains of GIV and other proteins by addition of rapamycin, which allows one to study that binding interaction in the absence of the many other interactions that could be formed by these proteins in cells. The setting is more physiological than when using purified components but key weaknesses remain in that (a) all the proteins in the system are being over expressed relative to native levels, and (b) it requires truncations that have fewer competing interactions that could arguably prevent the proteins from interacting at all if they were present at native concentrations. The bottom line is that the experiments are still far from physiological.

That said, the BRET assay data look clean, reasonable control experiments are run, and they together give a surprising result in that, within the context of these experiments, there is little or no GEF activity provided by GIV, but that it can release Gbg. This is a bit of a paradigm shift for the GIV non-receptor GEF field , which has lately been the domain of two alumni from the Fahrquar lab where studies of the protein originated. In many papers to date, the underlying hypothesis from these labs, even in 2020, has been that the GEF activity of GIV drives its physiological effects. Thus it is quite admirable to perform and publish a more definitive experiment even when it goes against the standard mantra. That's good science. The data in Figure 3 was particularly illuminating, where inhibition of cAMP production was eliminated by GRK2ct, showing in this context that it is not a result of GIV GEF activity on Gi.

The methods deployed in this study should be useful to the field, in particular the rapamycin-based recruitment which could add a new dimension to cell based studies where one normally just overexpresses the proteins of interest. Its impact however is questionable because one is now potentially targeting the domains to regions they would not necessarily go because the proteins are not full length, especially when they have many other reported interaction partners and furthermore when they are being over expressed so one can measure significant BRET signal in the first place.

Impact is somewhat further diminished by some backpedalling on the GEF story based on data in Figures 5 and 6. The author concludes that there may still be meaningful GEF activity mediated by GIV in vitro that serves to prevent GIV from holding on to Galpha subunits too long (they do not bind Ga-GTP). This is an attempt to explain why GIV has no effect on GPCR signaling function, while other proteins tested (AGS1, R12) do. A more parsimonious conclusion would be that GIV just doesn't have meaningful GEF activity in cells, even when overexpressed as a membrane-recruitable fragment. This seems particularly likely considering that GIV has lower affinity for Galpha subunits relative to GPCRs by orders of magnitude, and with a high nM EC50 that seems unlikely to function at physiological concentrations of these proteins.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Complementary biosensors reveal different G-protein signaling modes triggered by GPCRs and non-receptor activators" for further consideration by eLife. Your revised article has been evaluated by Jonathan Cooper (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #2:

The revisions have addressed my concerns.

Reviewer #3:

Dr. Garcia-Marcos has addressed many of the concerns brought up by my prior review. The paper is now easier to interpret and the figures are first class.

I have mixed feelings about impact. I like the fact that the work represents a paradigm shift, straight from the lab of the world leader on this topic. The observation that this fragment of GIV can efficiently release Gbg subunits could be a game changer. On the other hand, this is a bit of a niche field in the realm of heterotrimeric G protein signaling, and many are agnostic about the ability of GIV to serve as a GEF in the first place. This is in part because a lot of the evidence comes from studies that use fragments or overexpression etc. The killer in vivo experiment has not yet been performed (a GIV knock-in that eliminates the proposed function of the GIV domain in question at physiological levels). And if one is agnostic about this issue, and if one thinks of it as more "niche", then it is not much of a paradigm shift.

A real strength from a technical perspective here is the parallel examination of different soluble regulators of heterotrimeric G proteins using the same rapamycin membrane recruitment system. The author has done a good job describing the caveats in interpreting the data because it is true that the system, especially for GIV, is a long way from physiological…GIV has many proposed interaction partners in the cell. However, the results are interesting because of the dramatically different effects on observes in the system with the various proteins and the potential for their use, at the very least, and chemical biological tools to probe G protein signaling. I agree with the author that the best way to sell this work is as an effort to characterize possible mechanisms in a cellular context. One might argue this is still "in vitro", but the fact that quite different answers are achieved here versus the test tube is interesting.

Only one major remaining concern. I understand the author's desire in trying to incorporate the GEF activity that has been observed with purified fragments at high concentrations in the test tube or at low levels in living cells into a working model. However, upon examining all the data in this paper, there seems to be little or no evidence here that this fragment of GIV is leading to any nucleotide exchange on Gi in the cell. And this is even after overexpression of a fragment free from other interactions in the cell. The rapamycin treatments with the Gi sensor are completely inert when it comes to GIV. Unless one argues that the Gi sensor is just not that great and the signal gets lost in the noise (and I am not sure it is wise to make that argument). Regardless, the data in this paper just doesn't support a model where GEF activity factors in (Figure 6). The GIV fragment just seems really good at liberating Gbg by some other mechanism than GTP loading, at least when it is membrane targeted in this way.

The thoughtful discussion does come up with a few ideas about how weak GEF activity might still play into the GIV system; it is just that to me the paper seems to make such speculation unnecessary. I would be comfortable with a much more simple conclusion that membrane recruitment of GIV by any mechanism could lead to Gbg release in the absence of GPCRs. That's interesting and simple.

It could be that the previously observed low "GEF activity" in living cells is a consequence of release of the tonic GDI activity of Gbg, allowing Gi to exchange on its own. But I'd have to dig into the papers to figure out what the controls were. I am just speculating.

Typos. line 375: nor should be "not". Line 370: "in controlled" should be "is controlled".

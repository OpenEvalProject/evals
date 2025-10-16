# Author response - Round 1

Authors:
- Geoff P O'Donoghue
- Rafal M Pielak
- Alexander A Smoligovets
- Jenny J Lin
- Jay T Groves

## Response text

DOI: [10.7554/eLife.00778.017](https://doi.org/10.7554/eLife.00778.017)

1) This manuscript follows others (Huppa et al., 2010; Huang et al., 2010) that have tried to address this problem and come away with interesting insights. The current study takes a unique approach using low intensity light for longer time periods, which selects against short-term interactions to track TCR-PMHC interactions and comes up with some contradictions with the published work. These differences to the previously published results are puzzling and need to be discussed.

The differing results with respect to in situ pMHC:TCR kinetics observed by tracking in our experiments and by smFRET in the Huppa et al., 2010 paper are indeed puzzling. Several key points regarding this issue are contained in the original manuscript. We highlight these below and have made additional clarifications in the text (e.g., paragraph 1 in “Single molecule agonist pMHC:TCR binding kinetics”).

The variable exposure times used in our experiments allow observations to be directed at different time scales. Thus although much of the data presented was acquired under conditions that do indeed select against short-term interactions, we have also done the corresponding high-speed measurements (see, for example, the single molecule trace in Figure 1C). The fast pMHC:TCR kinetics reported in Huppa et al., are still an order of magnitude slower than our fastest time resolution (17.5 ms); such fast events are not likely to be missed in these tracking experiments using the fast exposure times.

We devote several analyses in the manuscript towards possible differences in what is measured by tracking vs. smFRET. Specifically, we consider (and rule out) serial rebinding of a single pMHC to multiple TCR in a TCR cluster (“Stochastic reaction-diffusion simulations”). In the Discussion (paragraphs 3 and 4) we suggest structural flexibility within the pMHC:TCR complex could explain the differing observations, particularly since the fast kinetics are only observed when the pMHC:TCR complexes are under strain. This could easily obliterate a smFRET signal even without the complex fully disengaging (Majumdar et al., 2007). Such flexibility is supported by recent structural analyses of pMHC:TCR (Adams et al., 2011; Hawse et al., 2012; Reboul et al., 2012). Therefore, with the information at hand, we suggest this is the most likely explanation. It is important to note that our measurements agree with solution SPR measurements (Corse et al. 2010 & ; Newell et al. 2011) and with in vivo requirements for negative selection (Williams et al., 1999; Palmer & Naeher, 2009) for two different TCR. We do not analyze measurements made with a different pMHC:TCR combination (Huang et al., 2010) in detail because they are not directly comparable.

2) There is not much of a difference between 24 and 37 degrees. This is surprising and should be discussed.

There is only a modest difference between dwell times measured at 24 and 37°C. The difference is more pronounced for the MCC-AND interaction, 54 s vs 81 s at 24 and 37°C, respectively. We observe a slight temperature effect in the 5c.c7 system; however, the intrinsic experimental error in comparing the dwell time distributions at 24 and 37°C is higher for shorter interactions. The effect is also easier to see for the MCC-AND interaction because there are more MCC-AND complexes per T cell (data not shown). It is also possible that changes in cellular behavior in response to temperature could also affect these measurements in ways that are not observed in solution measurements with purified components. At 24°C T cells have a smaller surface area on the supported membrane than at 37°C, are slower to land, and also have decreased lamellipodial motion. These factors could affect the environment of the pMHC:TCR interaction in unpredictable ways and perhaps could compensate for the direct temperature effect on molecular interactions.

3) The Introduction could be improved for a general audience. Currently it reads like a longer version of the Abstract (or a shorter version of the Results). This section would be a good place to set up the main issues of the paper, e.g., why off-rates are important and what attempts have been made to measure this in the past.

We have expanded and clarified the Introduction to better introduce the importance of quantitative single molecule measurements (e.g., of kinetic off-rate, stoichiometry, etc.) to the understanding of TCR signaling mechanisms.

Also a few small points – are all pMHC-TCR-Zap70 complexes attached to actin or is there evidence of them being formed, diffusion, and then joining onto the actin treadmill? Can one detect variability or successive recruitment of Zap70? It is stated that there is an average of 6 but we are wondering if one could extract additional information at the single molecule level of clear variability (particularly for two different pMHC) or accumulation of Zap70 over time.

All observed pMHC:TCR:ZAP70 complexes are transported radially towards the geometric cell center (Videos 1, 2, and 3; Figure 3A) of the 2-dimensional cell-supported membrane interface. We do not observe evidence for pMHC:TCR:ZAP70 random diffusion prior to radial transport on these timescales – such sequential events could occur on faster timescales.

Clear variability does exist in the number of ZAP70-EGFP per pMHC:TCR complex. This is most clearly shown in Figure 3D, where the intensity distribution of ZAP70-EGFP puncta is symmetric and unimodal with an average of 2.9 ZAP70-EGFP/puncta. The distribution of ZAP70-EGFP intensities (from single ZAP70 molecules up to ∼10) implies that time-dependent ZAP70-EGFP accumulation must occur, but we have not definitively observed accumulation of ZAP70-EGFP over time in one intensity trace. The observation of single molecule ZAP70-EGFP accumulation in a single intensity trace (i.e., several consecutive step intensity increases) is technically challenging due to the convolution of several time-dependent processes: MCC-Atto647N bleaching, ZAP70-EGFP bleaching, pMHC:TCR unbinding, ZAP70-ITAM binding, and ZAP70-ITAM unbinding. We do, however, make the bulk observation that the brightest ZAP70-EGFP features are observed at later time points. The text has been clarified accordingly (“TCR triggering monitored by ZAP70 recruitment”).

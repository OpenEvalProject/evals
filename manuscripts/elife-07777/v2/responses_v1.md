# Author response - Round 1

Authors:
- Zhengjian Zhang ([ORCID: 0000-0002-2840-0837](https://orcid.org/0000-0002-2840-0837))
- Zarko Boskovic
- Mahmud M Hussain
- Wenxin Hu
- Carla Inouye
- Han-Je Kim ([ORCID: 0000-0002-0305-259X](https://orcid.org/0000-0002-0305-259X))
- A Katherine Abole
- Mary K Doud
- Timothy A Lewis
- Angela N Koehler
- Stuart L Schreiber ([ORCID: 0000-0003-1922-7558](https://orcid.org/0000-0003-1922-7558))
- Robert Tjian

## Response text

DOI: [10.7554/eLife.07777.021](https://doi.org/10.7554/eLife.07777.021)

Reviewer #1: My main concern is the assumption that the difference between minus and plus Sarkosyl is due to reinitiation. The original Hawley paper used it to block subsequent initiation in a crude system and the mechanism was assumed to be disruption of protein/protein and/or protein/DNA interactions which Sarkosyl does. The fully formed PIC is fairly resistant to low concentrations, but subsequent PIC formation is blocked.

As suggested by the reviewer, we have now performed continuous labeling experiments using the G-less cassette DNA template, and observed transcripts of different lengths that provides independent and complementary evidence for transcription reinitiation in our system. We also confirmed that reinitiation is resistant to the inhibitor (Figure 8C). We have now included additional controls for this experiment and the Sarkosyl experiments in Figure 8–figure supplement 1.

The amount of Sarkosyl is critical since it will disrupt preformed PICs. This is especially important in a defined system that does not have high protein concentrations like the extracts did in the original Hawley paper.

We have performed titrations of Sarkosyl at different stages of transcription initiation as tested in the original Hawley and Roeder paper (1985, JBC, Figure 2A) and observed very similar dose responses with our highly purified system (Figure 8–figure supplement 1A). Basically 0.02% Sarkosyl added at the beginning is sufficient to inhibit both initiation and reinitiation; a pre-assembled preinitiation complex (PIC) may be resistant to 0.02% Sarkosyl, but completely inhibited by 0.04% Sarkosyl (this is about 2 fold more sensitive than their 1987 paper, which might reflect some differences in our system and/or experimental procedures). On the other hand, after the addition of ribonucleoside triphosphate (NTP) substrates that allow productive elongation, the system becomes resistant to a broad range of Sarkosyl, up to 0.64% as tested.

Why was it added after NTPs? Initiation takes only seconds.

As mentioned above, if added right before NTPs, the concentration range for Sarkosyl to only prevent reinitiation is very narrow (in fact 0.02% may not be sufficient to prevent reinitiation, while 0.04% would inhibit the function of pre-assembled PIC), which are conditions that we felt were not robust and could compromise the reproducibility of our experiments. On the other hand, when added immediately after NTPs, a broad range of Sarkosyl concentrations from 0.04% to at least 0.64%, give the same result of preventing reinitiation. Therefore we chose to add 0.1% Sarkosyl within 30 seconds after NTPs addition to restrict transcription to a single round.

How long after NTPs were added was the Sarkosyl added?

The answer is within ∼30 seconds. This much incubation time is sufficient for the formation of the first 1∼2 phosphodiester bonds which will render much stronger Sarkosyl resistance (Hawley and Roeder, 1985, JBC, Figure 6).

Why were the reactions carried out for 30 minutes?

This allows elongation (and reinitiation in the absence of Sarkosyl). Under our experimental setup, this 30 min incubation time might allow some additional de novo PIC assembly (which can explain the 1.5∼1.7 fold difference between lanes 1 and 2, or between lanes 5 and 6 in Figure 8–figure supplement 1B), but the majority of transcription in this period is from reinitiation (comparing lanes 1-4 with lanes 5-8 of the same panel). Reducing this time may prevent additional de novo PIC assembly, at the cost of some reinitiation (as is shown in the Szentirmay and Sawadogo, 1994, NAR paper Figure 1 and 2).

If reinitiation is occurring in the absence of Sarkosyl what factor is responsible for resistance to the inhibitor?

As illustrated in the new Figure 7, the chemical appears to block an isomerization of the TFIID-promoter complex that is required for full engagement of Pol II. The factor that makes reinitiation resistant to the chemical inhibitor is the TFIID complex that becomes isomerized during the first round of transcription, which allows reinitiation to by-pass this inhibitor-sensitive stage. It is also possible that some other factor(s) may facilitate maintenance of this isomerized functional state of TFIID that we have not yet identified.

Reviewer #2:

First, it is critical to establish at what stage of transcription the inhibitor actually acts.

We have examined the synthesis of the first dinucleotide and found that transcription is inhibited at or before this step (Figure 6A). We further demonstrated that functional PIC assembly is blocked at the stage of Pol II engagement by footprinting assays (new Figure 7). Since we detected the action of the inhibitor at these very early stages of transcription initiation well before the involvement of TFIIE and TFIIH (i.e. promoter melting), we have not pursued the potential for the inhibitor to also influence promoter melting and elongation.

The authors interpret the footprint alterations resulting from the inhibitor as evidence for an enhanced or stabilized binding of IID to the promoter. I don't think this interpretation is justified.

This concern is well appreciated, so we have further investigated the mechanisms of inhibition using additional footprinting assays to monitor potential conformational changes during PIC assembly. In new footprinting data included in the revised manuscript, we have detected strong global (not “localized”) changes in the protection patterns consistent with conformational changes and “isomerization” over an extended region of the promoter that is arrested by the inhibitor (Figure 7). Please also see our response to the same concern from Reviewer #1 on Figure 5C.

It would have been useful to see if these changes persisted even when IIB and IIF were present, since these factors partially rescue transcription from the effect of the inhibitor.

Actually, TFIIB doesn’t rescue transcription from the inhibition, while TFIIF does so only partially (Figure 6C). Since TFIIF usually functions together with Pol II, the engagement of which completely rescued transcription from inhibition and correlated tightly with the dramatic “global” isomerization at the footprinting assay, we haven’t focused on the “local” changes in these new experiments. Instead, we have performed the step-wised perturbation assays described in Figure 7B, adding the inhibitor after TFIID and TFIIB, but before TFIIF and Pol II. The results we obtained were consistent with arrest of the proposed conformational isomerization required for Pol II engagement during assembly of a functional PIC (before promoter melting).

Another point about the footprints – as best as I can tell the TATA box is not protected. Can the authors comment on that?

It has been previously reported that TFIID fails to efficiently protect the TATA box at the super core promoter (Juven-Gershon et al., 2006, Nat. Meth., 3:917), and that TFIIA can facilitate a structural transition to cause TATA box protection (Cianfrocco et al., 2013, Cell, 152:120). In our transcription assays, TFIIA had no detectable effect. However, we noticed that TATA box protection became increasingly evident upon the addition of TFIIB and TFIIF, and complete protection occurred once Pol II was included in the system, which is consistent with PIC assembly in the absence of TFIIA (Figure 7A).

Finally, a central point of the paper is the differential effect of the inhibitor on re-initiation versus the first round of transcription. I am afraid I am skeptical of the assay.

To address this reservation, we have now performed an independent assay to verify the occurrence of reinitiation in our system and its resistance to the inhibitor (Figure 8C).

I suspect that the extra transcription seen when Sarkosyl is left out simply represents the failure of the otherwise late-starting complexes to initiate.

In addition to the independent validation of reinitiation, we have also performed titrations of Sarkosyl at different time points to compare with the original Hawley and Roeder (1985 JBC) results. We observed very similar responses to Sarkosyl as previously reported (Figure 8–figure supplement 1A). In that JBC paper (Figure 6), the formation of the first 1∼2 phosphodiester bond(s) is sufficient for high Sarkosyl resistance, which is mostly completed within half a minute (no difference from 20-minute incubation). Therefore we believe the slow-starting complexes observed by Reviewer #2 could either reflect variations among experimental systems, or correlates with a stage after the synthesis of the first 2∼3 nucleotides (but before ∼20 nucleotides).

Does Sarkosyl affect that isomerization?

The TFIID-DNA complex isomerization described by Yakovchuk et al. (the Yudkovsky paper is on reinitiation) (also see the new Figure 7A) occurs during PIC assembly (which should be near completion with our 30-minute incubation), before the addition of NTPs, and thus should not be affected by Sarkosyl treatment.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

My biggest concern focuses on how the proposed mechanism is described. The authors assume (Figure 9, for example) that Pol II is recruited to the inhibited complex but somehow cannot function. However, they don't actually demonstrate that Pol II is recruited- couldn't the inhibitor work to change TFIID's conformation so that Pol II cannot join the nascent PIC? I think an argument in this direction can be made based on the right-most panel of Figure 7 – it would seem that the downstream (+16 through about +40) footprint changes characteristic of the complete complex still appear when Pol II is added after the inhibitor, but the TATA to +1 changes are reduced. This seems, at least to me, to suggest that Pol II is present in the inhibited complex even though it cannot access the transcription start site.

We agree with Reviewer #2 and thank him/her for the cautious and accurate assessment of the potential Pol II interaction with downstream promoter DNA in the presence of the inhibitor. We have modified the corresponding Results section (see the subsection “The inhibitor arrests an isomerization step required for full Pol II engagement”) and Figure 9 legend (panel B) to incorporate this helpful suggestion.

# Peer review - Round 1

Editors:
- Charles L Sawyers, Memorial Sloan-Kettering Cancer Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04034.002](https://doi.org/10.7554/eLife.04034.002)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Registered report: Tumour micro-environment elicits innate resistance to RAF inhibitors through HGF secretion” for consideration at eLife. Your Registered report has been reviewed by Charles Sawyers, Ravid Straussman as one of the original authors, and a biostatistician.

Charles Sawyers has assembled the following comments to help you prepare a revised submission.

All the reviewers agree that you have appropriately identified the most salient features of Straussman et al. for replication and that the replication experiments are well designed. Protocols 3, 4 and 5 are the key experiments (stromal conditioned media rescue, recombinant HGF rescue and inhibition of rescue with crizotinib). One reviewer felt that protocol 6 (survey of other signaling pathways activated by HGF) was optional.

1) Two reviewers felt that more attention should be given to the Lezcano et al., 2014 publication that reportedly failed to confirm a correlation between HGF expression and outcome (Figure 3 in Straussman et al.).

Specifically:

a. It should be noted in the text that the same group did replicate some other key findings of Straussman et al. – the presence of HGF in human melanoma tumors (in both melanoma cells and stromal cells) and the finding that HGF is significantly enhanced in disease progression.

b. The testing for a correlation between pre-treatment HGF and clinical outcome was done by Lezcano et al. using a cohort of 23 pre-treatment samples. While we fully support the claim by Lezcano et al. that “rigorous validation studies are thus indicated for approaches that seek to personalize such therapies to maximize therapeutic efficacy,” we wonder if testing of 23 samples can be considered as rigorous. As no power calculations are mentioned in Lezcano et al., we would like to see some discussion of whether Lezcano et al. were sufficiently powered to make positive or negative associations. If not, how large would the sample sizes need to be?

c. Wilson et al. (PMID: 22763448) tested the correlation between plasma HGF and PFS/OS on 126 melanoma patients and did find a statistically significant negative correlation that supports the findings in Straussman et al. As this is the only available big cohort testing HGF and clinical outcome on BRAFi, this should be adding it to the literature summary in the introduction.

2) We are aware of 2 groups that have directly replicated several of the in vitro experiments of the paper and have published some results. These should be added these to the literature summary.

a. A group from Amgen attempted to directly replicate the key findings from Straussman et al. Their findings can be found here: http://cancerres.aacrjournals.org/cgi/content/meeting_abstract/73/8_MeetingAbstracts/3405. They show that HGF can rescue melanoma cell lines from BRAFi and MEKi and that this rescue is attenuated by METi.

b. A group from the University of Illinois was able to demonstrate that c-MET inhibition is synergistic with BRAF inhibition in melanoma cell lines: http://cancerres.aacrjournals.org/cgi/content/meeting_abstract/73/8_MeetingAbstracts/2078

3) Regarding statistical power, we also have the following suggestion:

While it is very useful for you to leverage the previously reported effects to compute minimum power a priori, what you really need is to guarantee a minimum power on your own data. This can be done, a priori, by including some cross-study variation. This will be helpful for you to plan on the number of replicates and so forth. Papers by Giovanni Parmigiani and collaborators at the Dana Farber provide some estimates about cross-study variation that could be used for this purpose. Worst case, you should budget some additional variability because of cross-study reproducibility, and increase the sample size as appropriate. We also want you to compute and report power post-hoc/on-the-fly on your own data. Some minimum power should be guaranteed using summaries of your own data.

Comments on the specific protocols:

Protocols 1 and 2 - We think that the protocols are mixed and experiment detailed in protocol 2 should be protocol 1 and vice versa. This should be corrected. Below we refer to the protocols as they appear in the file that we received.

Protocol 1

• When growing SK-MEL-5-GFP cells make sure that >85% of cells are GFP labeled. If number of GFP positive cells are dropping one can use FACS or antibiotics to enrich again for GFP positive cells. We did not grow the cells under antibiotic selection on a regular basis.

• Microplate reader used is different from original and should be labeled with a *.

• We used Corning #3712 plates and did specify that in the methods section. Please remove the * and remove the comment: “Original unspecified”.

• 1c – as specified in the methods section we maintained cells in DMEM from Invitrogen (#10569-010). While using phenol-red free DMEM for the screens is a good idea (we did the same) I would recommend supplementing it with sodium pyruvate as the DMEM that we used had Sodium pyruvate in it. When using Phenol-red free media we used to add Sodium pyruvate from Cellgro (Cat #25-000-CI) to a final of 1 mM.

• 1d - we have plated cells on 384-well plates using the Combi cell platter (http://www.thermo.com.cn/Resources/201306/21143420640.pdf). This resulted in very accurate plating. I don't know how the replicating lab is planning to plate cells on 384-well plates. If manual plating is planned make sure that no air bubble is present at the bottom of the well after plating as this can frequently occur for those unexperienced with manual plating of 384-well plates.

Protocol 2

• Read GFP only after cells have completely settled down. As indicated in the paper we used to plate cells on day 0 and read GFP for the first time on day 1.

• Read GFP from wells with media and no cells as well. Before analyzing results subtract reading from clear–media wells from wells that have cells. We noticed that reading from media-only wells can change from day from day and thus subtract the reading from media-only wells from wells with cells. To this end we always make sure to have media-only wells on each plate with a total volume that is equivalent to test-wells. This remark is true to all experiments in all protocols.

Protocol 3

• 2b - Seems like 50ul and not 60ul is a better control for the wells that will have 20ul of cancer cells +20ul of PCM +10ul of drug.

• From the protocol it seems like stromal cells are plated once. I have plated stromal cells 3 times (each time 3 days before I needed it) to make sure that I have fresh PCM on days 0,1 & 4.

• This protocol involves a few cycles of media change in 384-well plates. We have done so using a CyBi robotic liquid handler. Do the replicating lab plan to use a robotic liquid handler? From my experience it is not easy to take out the exact same amount of media from 384-wells manually making sure not to touch the bottom and disturb the cells. If a robotic plate handler can be used I would recommend using it, as manual handling of hundreds of 384-wells might be a source of a lot of noise in the experiment. Lastly - both extraction and addition of liquid from the wells should be done gently. Cells are under the treatment of BRAFi and might be displaced more easily that non-treated cells. If using a robotic system please do not exceed a rate of 5-10μl/s and do not let the tip end closer than 1 mm to the well bottom.

• 8a - Subtract the reading from media only wells first and only then subtract reading of day 1 from day 7. This remark is true for all protocols.

Protocol 4

• 1a – please correct number to match your planned 2500 cells/well.

• 5 – I think a step is missing in which all media will be taken out, 40ul of fresh media added and only then HGF and drugs are added again.

Protocol 5

• 4 – PLX4720 must be diluted to 20 mM or less before diluted into media. This remark is true to all other planned experiments.

Protocol 6

• We used media with phenol-red for these experiments.

• 2 – On day 1 we did not change media to fresh. We only added drugs/HGF as indicated.

• Again – Make sure that stocks of PLX4720 are not over 20 mM when added to media.

• 3 – Cells were washed with cold PBS quickly on ice. Lysis buffer was added to the wells on ice. Cells were scraped and cell extract moved into Eppendorf tube.

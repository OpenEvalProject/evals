# Author response - Round 1

Authors:
- Li He ([ORCID: 0000-0003-2155-606X](https://orcid.org/0000-0003-2155-606X))
- Richard Binari
- Jiuhong Huang
- Julia Falo-Sanjuan
- Norbert Perrimon ([ORCID: 0000-0001-7542-472X](https://orcid.org/0000-0001-7542-472X))

## Response text

DOI: [10.7554/eLife.46181.040](https://doi.org/10.7554/eLife.46181.040)

Essential revisions:

1) When Transtimer is used as a direct reporter construct under the control of a gene's promoter and enhancer, it directly reflects the expression dynamics of that gene. It is more complex when Transtimer is used as a UAS construct. This use employs GAL4 which is a stable intermediary. The authors should model how using a stable intermediary such as GAL4 affects detection of signaling dynamics. This would strengthen the conclusion that can be reached using the Transtimer as a UAS construct. If there are already GAL4 reagents (e.g. generated as part of Flylight project) for any of the genes for which the authors have a direct reporter, a head to head comparison would be beneficial.

We agree with the reviewer that adding the intermediary Gal4 will significantly affect the reporter dynamics. To test that, we modeled the change of reporter dynamics after adding Gal4 (Figure 6—figure supplement 1A-F), and compared the dGFP and RFP driven directly by the Notch responding element Su(H)Gbe vs. a UAS-dGFP-2A-RFP (TransTimer) driven by Su(H)Gbe-Gal4 (Figure 6—figure supplement 1G,H). The modeling result suggests that the response time (time to reduce the signal to half of the original when the promoter is off) is generally proportional to the TG1/2 (half-life of Gal4) + TFP1/2 (half-life of fluorescent protein). This suggests that adding Gal4 will generally slow down the dynamic of the reporter. This is particularly clear in Figure 6—figure supplement 1E,H: the dGFP driven directly by the enhancer is more restricted in neuroblast cells (NB) than the dGFP driven by enhancer-Gal4 due to the retention of Gal4 intermediary. However, because the Gal4/UAS can amplify the signal, the system may reveal cells that weakly express the reporter and may be missed by reporter driven directly by the enhancer: in Figure 6—figure supplement 1F,G, the pattern driven by Gal4/UAS system is significantly broader.

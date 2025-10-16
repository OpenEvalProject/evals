# Peer review - Round 1

Editors:
- Arjun Raj, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31657.050](https://doi.org/10.7554/eLife.31657.050)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A simple open-source method for highly multiplexed imaging of single cells in tissues and tumours" for consideration by eLife. Your article has been reviewed by Arup Chakraborty as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Carsten Marr (Reviewer #2); Péter Horváth (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Overall, the reviewers appreciated the ability to multiplex immunofluorescence in FFPE samples using cyclic chemistry to measure expression and localization of several proteins in single cells. The open-source tools for the image processing pipeline were also thought to be of much interest to the community.

Essential revisions:

As discussed in our earlier correspondence, one concern that arose during deliberations was the lack of a clear discussion of the advance described in this manuscript relative to other contributions in the field, in particular that of Gerdes et al. We appreciate the arguments about lack of adoption of the method described by Gerdes et al., and its proprietary nature, and ultimately believe that for methodological improvements like this, the research community may be the best judge of the relative merits. Nevertheless, we do think it's very important to clearly delineate the contributions of the previous work in the field and precisely what the advance is in this present manuscript relative to those contributions, both in the Introduction and Discussion section.

Technically, the reviewers felt that the work lacked sufficient testing to show that order of antigen staining is not affected by cycle number, noting "This is a well known issue for multiplexed tissue staining and should be analyzed beyond just 4 cycles with 3 antigens. Tissue integrity is compromised after 5 cycles and only quantified to 10 cycles (Figure 1H); the authors claim their methods work to 20 cycles but descriptions of tissue integrity are lacking." The recommendation was: "Retention of antigenicity is only showed up to cycle 4 and for only 3 antigens, although data from higher cycles are used in other figures (20 cycles in Figure S3). Gerdes et al. demonstrates that 8/59 antibodies tested did not maintain full antigenicity after the tissue had been exposed 10 times to dye inactivation solution. We recognize that an experiment to test all possible orders/combinations of antibodies would be time and labor intensive, but we believe antibody validation must include how long antigenicity is preserved through cycles. We suggest the following tests of the methods:

* Two adjacent tissue slices are stained for 20 cycles with antibodies 1->20 and 20->1, respectively. The results are shown to be at least qualitatively similar.

* Maintenance of antigenicity for most, if not all, single antibodies up to 10-20 cycles."

Another reviewer noted "As a quantitative method, I would appreciate an evaluation of the robustness of the single cell measurements over cycles. It would be interesting to see how single cell intensities correlate when stained for the same antigens in cycle 1, cycle 2, cycle 3 etc., maybe even using different fluorophores, or a staining in cycle 1 and again in cycle 10, with other antigen stainings in between. This would add a quantitative level to Figure 2B."

Also: "Would be great to know the authors' experiences regarding the degradation after 8-20 t-CyCIF cycles, which is only partially discussed. For basic biology discovery studies, it would be great to have a stopping criteria where the number of washing steps saturate and noise takes over the signal, and in potential clinical practice a cycle number until quality is guaranteed would also be desired."

We feel that these technical points are important to fully address in a revision.

# Peer review - Round 1

Editors:
- Timothy W Nilsen, https://ror.org/051fd9666 Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75186.sa0](https://doi.org/10.7554/eLife.75186.sa0)

This paper is of interest to scientists from the field of origin of life or RNA synthesis in general, especially those interested in the "RNA world" scenario. The data analysis is rigorous and the conclusions are justified by the data. The key claims of the manuscript are directly related to, and support, previous findings.


---

# Peer review - Round 1

Editors:
- Timothy W Nilsen, https://ror.org/051fd9666 Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75186.sa1](https://doi.org/10.7554/eLife.75186.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Rolling Circle RNA Synthesis Catalysed by RNA" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Timothy Nilsen as Reviewing Editor and James Manley as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jiri Sponer (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewer #1:

In the origin of life scenario where RNA is assumed to be the first replicator, a key problem is how RNA can replicate itself. Or how can RNA polymerase copy itself, since copying requires an open flexible structure that can be read. While the polymerase needs to be a topological rigid structure in order to catalyse the RNA polymer.

The manuscript describes how a special kind of synthesis of the RNA, rolling circle synthesis on small pieces of circular RNA, could template and build RNA strands. The method apparently could help in avoiding the strand inhibition problem where stable RNA duplex in long strands hinders replication.

It is a bit unclear how, but I suspect this i down to the size of the ring, since the problem increase with the length of the polymer. The authors also touch on this themselves in their MD simulations, since the entropically unfavourable confinement of a string onto a circle can alleviate part of the problem. Nevertheless, the authors also show by MD that the rings become small tight structures that actually hinders replication.

The study depends on trinucleotide triphosphates (triplets) as substrates. They demonstrate a viroid like replication that show how a template (-) is able to make a mirror copy (+) of circular RNA by a rolling circle synthesis with out the need for enzymes or other catalyst apart from RNA itself.

While the conclusion of the work becomes a bit muddled, but honest, the work is a very important piece that demonstrates the huge potential role of circular RNA in the very early stages of life.

I must confess I am very far off my field of competences. I have tried my best to understand the paper, and the methods involved, but obviously I cannot give much feedback on the methods used. So, I cannot suggest improvements on that part.

For the most part, the paper is well written, and the structure is sound. I would strongly recommend publication.

It was unclear to me how it was certain that it was actually rings. There is the MD simulations, but apart from the principle drawing they are obviously not circular in shape.

There are some parts of the manuscript that too me is very difficult to understand. Some statements seem to reflect a community understanding that might be obvious for those working with similar system on a day to day basis, but for the general reader (where I put myself) this becomes gibberish. for instance:

RCS has potentially unique properties with regards to the strand inhibition problem where RNA duplex melting in principle can be effected by continuous toehold strand displacement driven by nucleotide hybridization and the ratchet of nascent strand extension by triphosphate hydrolysis. In an idealized RCS mechanism, such strand invasion and displacement processes are both isoenergetic and coordinated to nascent strand extension (Blanco et al., 1989; Daubendiek et al., 1995), with rotation of the single-stranded RNA (ssRNA) preventing the build-up of topological tension (Kuhn et al., 2002). Thus, RCS is a potentially open-ended process leading to the synthesis of single-stranded multiple repeat products (concatemers) with an internally energized strand displacement circumventing the "strand inhibition problem" (Tupper and Higgs, 2021).

It might not be possible to rephrase this so that everyone can understand. But I think the clarity of manuscript could be improved.

But also because there is references to previous work where long statements does not make it more clear what is actually meant. for instance:

Similar to what was described previously, RNA synthesis by the TPR best in the eutectic phase of water ice, due to beneficial reaction conditions for ribozyme catalysis such as reduced RNA hydrolysis and high ionic and RNA substrate concentrations (Attwater et al., 2010). This was also the case on scRNA templates.

That said, I think the overall message is clear and the paper is very interesting, I expect to reference it when it comes out.

Reviewer #2:

The RNA World theory is one of the most widely-believed explanations for the origin of life. This relies on the idea that there were self-replicating RNA systems in the early stages of life. Usually ,it is supposed that there were polymerase ribozymes that were able to use another RNA strand as a template for synthesis of the complementary strand. As there are no naturally-occurring polymerase ribozymes, there has been a sustained effort over several decades to develop polymerase ribozmes in the lab by in vitro selection. This paper contributes to this by presenting a polymerase ribozyme that can copy a circular template. Circular templates are thought to be important because replication of a circular template can occur via the rolling circle mechanism, in which a polymerase continues multiple times around the same circle, and the far end of the growing strand is displaced from the template at the same time as new bases are added to the growing end. This avoids the problem of strand inhibition (i.e the difficulty of separation of stable double strands that are expected to form when copying linear templates).

This paper considers rolling circle replication on very short circles of around 36 nucleotides. It is shown that replication proceeds by addition of triplets beyond the full length of the circle. As the circle is short, and the double-stranded part is stiff, it is not possible for the whole of the circular template to be double-stranded at the same time. It is shown that roughly half of the circle is double-stranded, and that the separation of the two strands occurs at a point which is on the opposite side of the circle from the point of primer extension.

The rolling circle mechanism involves cleavage of the growing strand by a self-cleaving hammerhead ribozyme that is encoded in its sequence. The mechanism also requires the reconnection of the ends of the new strand in order to form a new circular template. Both the cleavage and re-circularization steps are demonstrated in this paper.

This experiment still falls short of a fully self-replicating ribozyme system, because in order for continued replication to occur, both plus and minus strands of the circle would have to encode a hammerhead ribozyme, and in order for the system to be self-sustaining, the circles would also have to encode the polymerase ribozyme itself (which is supplied separately in this paper and is not replicated). Nevertheless, this paper makes an important step, and continues to bring us closer to developing self-replicating RNA systems.

Lines 122-126 – It is implied that triplets are better than monomers for rolling circle replication because triplets help to open up other double stranded regions. However, it is not obvious that this should be the case. To put a new triplet down you have to displace three bases from the displaced strand, whereas to put a monomer down you only have to displace one base. It is not easy to predict which of these is faster without measuring it. Furthermore, in the actual mechanism occurring here, there is no prior strand to be displaced at the point of attachment, because the displacement is occurring at the other side of the circle and it does not directly interfere with the attachment. So it is not clear whether this argument applies. Has replication of a circular strand actually been attempted with a monomer ribozyme? Is it known whether a triplet ribozyme is better than a monomer ribozyme on circular templates? If not, it would be better to avoid implying this.

Figure 1 – the periodic effect seen in 1E is claimed to be due to the difference of accessibility of template bases on the inside and outside of the circle. However, the results are measured by averaging over many different circular templates. I would expect that different copies of a circular template would have different configurations and would not always have the same bases on the inside. So the inside-outside difference should average out. Could the variability of 1E be explained by variation in rates of addition according to the sequence of the template rather than an inside-outside effect? The sequence effect would be the same in multiple copies of the same template sequence. Is there a similar variability seen when copying linear templates?

Figure 1C shows a TPR dimer. Is the polymerase actually in two parts? Is this important?

Line 213 – It is not clear why the 9 bp primer goes straight to 18 bp. What happened to the lengths in between?

Line 220 – The word "extended" is used to mean that the unhybridized portion is stretched. There is a possible confusion with extending a strand by ligation of a triplet. Maybe the use of a word like stretched is better?

Line 226 – The simulations show that the double-stranded part of the circle is stiff and only covers roughly half of the circle. The point at which the primer extension occurs is therefore far away from the point at which the two strands separate. This is important for very short circles. For longer circles, the stiffness should be less relevant, and there will come a point where the whole circle becomes double stranded. There will then need to be a true strand displacement occurring very close to the point of primer extension. How long would we need the circle to be before it switches to a double-stranded circle? Does the stiffness effect seen here with the short circles make the primer extension reaction easier or more difficult than a true strand displacement reaction on a double stranded circle?

Lines 228-33 – This paragraph is not very clear. The meaning is not coming through.

Line 288 – "orbit" is an odd word. Is there a better one?

Figure 4 – Overall Figure 4 is not clear.

– I have not understood the notation n: 3E5, 2E5 etc.

– For sequence A Pos 4, GAA is the darkest shade, so I am presuming the template is CUU (in the reverse direction). But the second darkest shade is GGC. Why should GGC bind to CUU more strongly than others (for example GGA)? I am not sure whether I have understood this diagram correctly.

– Part C shows fold difference. It would be easier if rates where shown for linear and circular strands separately. Why is sequence D a worse template? Or maybe it is not worse – it's just that the ratio of circular to linear templates is lower? It is not easy to understand this.

– Part D Figure 2 seems to show a double-stranded triplet being added. Why not just a single-stranded triplet.

Figure 6D – It is unclear what is happening at each step. Particularly the backwards and forwards diagrams in step 4. Also, shouldn't the red strand be still attached to the blue circle before the cleavage occurs? The chemical structure in the middle is a bit distracting. I think the structure drawn in A is the same as D step 6. Maybe put parts A and D together and make B and C a separate figure?

Line 436 – The reference to the virtual circular genome is misleading at this point. In the proposal of Zhou et al., there are no real circles, there are simply linear fragments that can be aligned to form a virtual circle. This does not fit with the rest of this paragraph. Either the reference to Zhou et al. should be omitted or it should be explained properly what the virtual circle proposal is.

Reviewer #3:

Technically the experiments are sound, really comprehensive, convincing and the paper is well written. The documentation (the composed Figures etc.) is very nice. The MD simulations nicely complement the experiments. Strong point is that the simulations address a qualitative question and are clearly directed to solve it. It is a preferable application of the MD technique. The basic methodology is correct, the standard AMBER OL3 force field appears appropriate, as the first choice multipurpose RNA version. It is known to lead to over-compacted unstructured ssRNA ensembles, as all biomolecular force fields that are good for folded biopolymers. For the double strand, the circle and their flexibility it should be an optimal choice. The simulations are quite short by contemporary standards, though I do not think their prolongation would change the essence of the findings.

As noted above, I consider the experiments as very convincing. Strong point is that the accompanying simulations address a qualitative question and are clearly directed to solve it. It is a preferable application of the MD technique. So, I really like it, though I have some ideas for potential minor improvements, may be explanatory comments, all for supporting information.

There are some occasional typos, e.g. l. 180 stand displacement, l. 182 this suggest. I think on l. 56. where progress in non-enzymatic synthesis is overviewed, the reference could be more balanced. Appears to me that some groups are represented by duplicate citations while some research is omitted, for example a recent progress in template-free non-enzymatic RNA polymerization of 3',5' cyclic nucleotides , https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/syst.202100017.

The short "jumping" supplementary movies are difficult to follow, I assume it is because of the size of the movies. Would it be possible to create a few SI Figures showing details of the most interesting parts of the structure, to focus on the key details, to accompany the movie?

In the simulations, lot of emphasis is paid on the Mg2+ simulations up to 500 mM MgCl. First point, is this condition relevant to the origin of life? Second, inclusion of divalents into MD is always risky, as they sample poorly (which is further exacerbated by the lack of bulk background due to the small periodic box, which may lead to glassy-like ion behavior around the solute). 400 ns is not sufficient to converge Mg2+. In addition, divalents, especially the high charge density Mg2+, are beyond the pair-additive MM approximation. It is impossible to simultaneously balance ion hydration and inner vs. outer shell binding to different coordination sites with the simple MM models. Could the authors briefly comment on initial placement of the ions after equilibration and during MD? Was it always hexacoordinated outer-shell binding to the RNA? Could the authors in SI briefly comment on it, and also comment if they had some specific reasons to choose the Duboue-Dijon parameters over parameters that have been more commonly used in biomolecular simulations? As I am not sure these specific parameters were tested/calibrated for RNA interactions (but I am not fully familiar with the work). Again, as the results are qualitative, I do not expect any effect on basic outcome of the work, so I am not suggesting any new computations.

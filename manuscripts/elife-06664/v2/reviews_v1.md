# Peer review - Round 1

Editors:
- Sjors HW Scheres, Medical Research Council Laboratory of Molecular Biology , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06664.013](https://doi.org/10.7554/eLife.06664.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Low cost, high performance processing of single particle cryo-electron microscopy data in the cloud” for consideration at eLife. Your Tools and Resources article has been favorably evaluated by John Kuriyan (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The following individuals responsible for the peer review of your submission have agreed to reveal their identity: Sjors Scheres (Reviewing editor); Steven Ludtke (peer reviewer). A further reviewer remains anonymous.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

All three reviewers agreed that this paper represents a novel and original way of alleviating the high computational burdens that many cryo-EM labs face with the advent of huge amounts of data from new direct electron detectors. As this paper has the potential to accelerate discovery, and to change how many labs operate, publication was recommended by all three.

The following concerns (in order of importance) were raised:

Firstly, one of the reviewers had actually recently performed the EC2 cost analysis himself and was surprised to see the estimates in this paper less expensive than his own. He writes: “The first issue is an Amazon trick. The r3.8xlarge instances are marketed as “32 vCPUs”. Actually this is 32 threads running on 16 cores when you read the fine print. For image processing this is generally 18-20 “CPUs” worth of compute power for the “32 vCPUs”. CPU-hr/mo/yr normally measure core-hours, not thread hours. This is a factor of ∼1.8. If the authors disagree, I would encourage them to run a scalability test on a small problem on a single 32 vCPU instance. Perusing the Amazon site, the cost of a single r3.8xlarge instance with 16 physical cores is currently $2.80 for on demand use, rather than the $0.35 quoted by this manuscript. While it is possible to reduce this by up to ∼50% through contract prepurchase, the only mechanism I can see for getting the price anywhere close to the cited level is by bidding on unused hours, which can mean substantial delays. Currently the purchase price for an equivalent cluster is ∼$350/core ($175/thread), or ∼$7500 for a node almost identical to the $2.80/hr instance. Anyway, by my calculation, when you take all expenses into account, EC2 is about 3-5x more expensive than owning a cluster. However, if the Amazon price were suddenly 10x lower, this would be compelling. If my cost analysis is in error, I would be honestly grateful to see a correction, as it would substantially alter how we operate.”

Secondly, in Table 1, the reported times for the other 3 cases are incorrect. They are merely the same of the values reported for the old and the new movie processing in the Scheres, 2014 eLife paper. There are no reported CPU costs for the entire processing procedures of these structures in the literature. However, on the RELION wiki (http://www2.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#Computational_issues) it is stated: “We do 3.x Angstrom ribosome reconstructions from say 100-200 thousand particles in approximately two weeks using around 200-300 cores in parallel”. This would result (given current cost estimates) in about $800 per structure, which is still very reasonable.

Thirdly, the authors are encouraged to base their analysis on Amdahl's Law instead of the “near-linear increase” stated in the paper. While I would normally consider this a minor concern, this analysis will yield numbers which will be interesting to consider.

[Editors’ note: the decision letter after resubmission follows.]

Thank you for choosing to send your work entitled “Low cost, high performance processing of single particle cryo-electron microscopy data in the cloud” for consideration at eLife. Your revised submission has been evaluated by John Kuriyan (Senior editor) and Sjors Scheres (Reviewing editor). Based on our discussions and the individual reviews sent previously, we regret to inform you that your work will not be considered further for publication in eLife.

It is unfortunate that the standard prices for Amazon's cloud are so high. We feel that bidding on unused hours is likely to be unpredictable in the future and this lack of predictability makes it less appropriate as a means of evaluating the costs of the calculations described in the paper. The true cost of doing an entire structure determination project (not only a single refinement run) at standard Amazon prices would probably quite substantially higher than the value mentioned in the Abstract. We fear that this could more expensive than buying a local cluster. Although some smaller labs may still benefit from the cloud setup, this paper will not likely change the way cryo-EM labs work in general.

[Editors’ note: after an appeal against the decision, further revisions were requested before acceptance.]

In order to give a fair and transparent view to the casual reader, we feel that the addition of a discussion on the costs of a “typical” structure determination project would add value to the paper. The phrase “as we illustrate here by determining a near-atomic resolution structure of the 80S yeast ribosome for $28.89 USD in ∼10 hours” in the current Abstract is not representative of a typical case. Many data sets will contain several hundreds of thousands of particles, and each 2D or 3D classification or refinement run will cost in the order of 100-200$ each (based on your estimates for gamma-secretase and mitoribosome). As in a typical project one would run multiple of these jobs, real costs will quickly reach more than a thousand dollars per structure, even when using the $0.35/hour bidding rate. This is perfectly well acceptable and still competitive with buying a local cluster. But discussing such values in the paper will prevent unpleasant surprises when PIs start receiving EC2 bills.

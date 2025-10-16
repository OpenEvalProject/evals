# Peer review - Round 1

Editors:
- Michael Herzog, EPFL Switzerland

Reviewers:
- Michael Herzog, EPFL Switzerland
- John Caas

## Review text

DOI: [10.7554/eLife.42512.030](https://doi.org/10.7554/eLife.42512.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Image content is more important than Bouma's Law for scene metamers" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Michael Herzog as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: John Caas (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors show that summary statistics models cannot easily explain crowding. In previous studies, only "metameric" images were compared with each other by human observers. In the present study, the original image was compared with two images created by either the FS-model or a deep network. For all scale factors tested, observers could well tell the original from the other images arguing against summary statistic approaches.

The topic is timely, the experiment was conducted in an expert fashion, and the presentation is clear and well structured. However, there are aspects which need to be taken care before a final decision can be made.

Essential revisions:

The failure of FS images to metameric to regular scenes could be a function of many things: The specific size of the pooling regions as a function of eccentricity, the statistics that are measured inside pooling regions, or the contribution of mechanisms for perceptual organization that are not explicitly modeled in the FS approach. The demonstration that metamerism breaks down is important, but the current study does not allow us to clearly distinguish between these various alternatives. Please consider discussing these various accounts of the data in more depth, especially with regard to how we might differentiate between these explanations.

The authors note, "It is the image content, not retinal eccentricity, that is the primary determinant of the visibility of at least some summary statistic distortions." The reviewers agree that global processes may well contribute to the higher spatial resolution observed in this study in response to the real-world images. Exactly what these might be is not specified, nor is the possibility that local interactions may also be at play. Two papers (Robol, Casco and Dakin, 2012; and Van der Burg, Cass and Olivers, 2017) showing that local orthogonal structure is capable of driving perceptual segmentation speak to this. One of the reviewers wonders whether such local interactions might at least partially explain performance differences between the different classes of stimuli (real vs. synthetic; texture-like vs. scene-like)?

Could the authors provide a more detailed description of the criteria they used to categorise the real-world images as either texture-like or scene-like? How and why might metametric sensitivity depend upon this classification criterion?

Reviewer #1:

1) The TTM model was used by Freeman and Simoncelli to show that different textures generated from the same image are metamers (i.e., cannot be differentiated by subjects).

2) Wallis et al. correctly claim: if the summary statistics in this model truly mimic the statistics extracted by the brain, subjects should not be able to differentiate texturized images from the original image.

3) However, they show that this is not the case with natural images: subjects can well discriminate between the original and associated textures (using both Simoncelli statistics and statistics from CNN simulations).

4) They claim that the global visual scene must be taken into account and perceptual organization is important. Compressibility by summary statistics depends on image content.

5) They link their results to the debate about the richness of experience. Cohen, Dennett and Kanwisher proposed summary statistics to explain the richness in the periphery. Here, they discuss that summary statistics in fact doesn't seem to be able to do the job.

Although it is not the most groundbreaking experiment ever, I still quite like this paper because:

1) It is good to highlight that texturized images are in fact not metamers of the original images.

2) The discussion is interesting bringing together crowding and the debate on using summary statistics to explain the richness of perception in the periphery.

Reviewer #2:

The authors describe a single experiment designed to test the hypothesis that natural scenes will be metameric to synthetic scenes created using a model that implements a summary-statistic model of texture-like pooling of visual information in peripheral vision (what the authors call the Freeman-Simoncelli or FS model). Critically, the model allows the scale of pooling regions to increase at different rates as a function of eccentricity, making it possible to examine the specific hypothesis that Bouma's Law (which predicts a scale factor of 0.5) governs pooling across the visual field. The authors rightly point out that the key comparison between natural scenes and synthetic scenes has not been done, and the key contribution here is to do just that. Also, the authors examine performance for scenes that they classify as "texture-like" and "scene-like," which should be equally subject to the metameric treatment if the strong FS-model hypothesis is correct. Briefly, they find that scene type does change the critical scale at which participants can reliably tell natural scenes from synthetic ones, and that the critical scale for scene-like images appears to be a good bit lower than the 0.5 value predicted by Bouma's Law.

The task the authors use is appropriate (a 3AFC oddball judgment applied to images presented in sequence), and I don't have any concerns about the implementation of the FS model. I don't love the fact that the entire stimulus set was comprised of only 20 images (10 per scene type), however. I understand the practical constraints the authors mention regarding the long rendering time for synthetic images, but there's a real concern here: Do these results generalize? The authors emphasize that if we find any image that can be discriminated with a scale factor that's lower than 0.5, then that determines the minimal scale of pooling. If we accept this logic, we have no need to worry about generalizability because all we're looking for is the existence of any image that fits the bill. I think I'd feel better about accepting this logic if the authors' task didn't involve distinguishing two physically identical images from an oddball. While an ideal version of the FS-model would (I think) predict that there should be no measurements at scales coarser than the critical scale that would support discrimination of these images, practically, the model one actually runs is not ideal, and thus the images it produces might not completely meet this standard. To be clear, I'm not saying I disagree with the authors' main conclusions, but I do think it's worth qualifying some of the stronger statements about what you can conclude from 10 images per condition produced by a model that doesn't have clear convergence properties.

More broadly, while I think the discrimination task is a good place to start, I also thought that extending the task beyond the identical-foils version of the design could provide some useful context. For example, suppose instead of 3AFC oddball detection, the authors included a version of the task that was a 2AFC real/synthetic judgment? This obviously is no longer a test for metamerism, but whether or not individuals can reliably tell if a synthesized image looks strange is an important indicator of whether or not they can solve your task without actually trying to discriminate the images (are there two strange images and a non-strange one?). Really what I'd like is a more thorough discussion of how observers might try to accomplish the task when distractors are physically identical, and what that might imply about the strength of the conclusions the authors can draw regarding spatial pooling in the model.

Finally, I like the authors discussion of gestalt properties a great deal, but there's also a competing argument that I think is hard to dismiss: What if the critical scale of 0.5 really is sufficient to make metamers out of natural scenes, but the set of statistics being computed within those regions in the FS-model is inadequate? This is a "God-of-the-gaps" argument to be sure, but again, the issue is that we can't hold a specific implementation of a model to the standard of an ideal. I tend to agree with the authors that there are probably grouping and segmentation processes (or global processes) that contribute to perceptual appearance, but it's an open question whether some of these properties might fall out of a model that incorporated different summary statistics that more closely approximate our own perceptual codes in peripheral vision. Again, this is a place where what I'm looking for is some more nuance – perceptual organization is an interesting thing to think about, but refining our ideas about what texture statistics might be computed in the periphery is also interesting to pursue.

Reviewer #3:

This paper uses a 3AFC peripheral distortion detection task to measure the human visual system's spatial resolution for images of real world scenes and synthesised versions of these images. Results indicate that the critical scale with which participants were able to reliably detect distortions was significantly smaller for real world images. A further comparison of the results pertaining to ten "scene-like" and ten "texture-like" images was conducted. Results of this analysis demonstrate that distortions in "scene-like" images ("those containing inhomogeneous structures") could be made at significantly finer scales than are distortions in "texture-like" images ("those containing more homogenous or periodically patterned content").

The authors explain that the critical spatial scale implied by performance regarding the synthesised images is broadly consistent with Freeman and Simoncelli, (2011) V2-like texture pooling model of peripheral visual performance. Given the higher spatial resolution performance implied by performance with the real-world images, and most strikingly, the scene-like images, a convincing argument is mounted that performance in these conditions must be based on either additional information, or at least finer grained information, not available in the FS synthesised images.

These results contribute to the burgeoning literature demonstrating that the deleterious effects of visual clutter can – under certain image-based circumstances – be much smaller than is predicted by Bouma-like pooling. As the authors note, "It is the image content, not retinal eccentricity, that is the primary determinant of the visibility of at least some summary statistic distortions."

This begs the question of 'what types of image content enable the relative high spatial resolution shown here and elsewhere?'. The authors cite some studies relevant to this issue (Saarela et al., 2009; Manassi et al., 2013; Vickery et al., 2009; Herzog et al., 2015), and suggest that "early global segmentation processes influence local perceptual sensitivity" and that "global scene organisation needs to be considered if one wants to capture appearance-yet current models that texturise local regions do not explicitly include perceptual organisation (Herzog et al., 2015)."

Whilst I agree that global processes may well contribute to the higher spatial resolution observed in this study in response to the real-world images, this overlooks the recent finding by Van der Burg, Olivers and Cass (2017) showing that local geometric interactions can profoundly improve peripheral performance (i.e. to break crowding) in densely cluttered heterogenous displays. Specifically, they find that the presence of local T-junction-like orthogonal structure reduces the effects of deleterious pooling to almost zero. I would suggest that these or similar high-order local interactions may be at play here. That result and the possibility that local interactions might play a role here should at least be proposed. Given the (somewhat vaguely defined) criteria used by the authors to categorise the real-world images as either texture-like or scene-like, I wonder what specific information the authors believe the visual system might use extract peripheral real world image content.

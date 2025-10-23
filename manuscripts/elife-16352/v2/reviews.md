# Peer review - Round 1

Editors:
- Gaudenz Danuser, UT Southwestern Medical Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16352.050](https://doi.org/10.7554/eLife.16352.050)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "A hyperspectral method to assay the microphysiological fates of nanomaterials with single-particle sensitivity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Gaudenz Danuser as the Reviewing Editor and Sean Morrison as the Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

As you will see from the full reviews below, all reviewers praise the quality of the study and its relevance and timeliness. However, all three reviewers raised from different angles the same concern: How new and versatile is the technique. Reviewer #1 provides a number of papers that your approach should be carefully compared to – potentially with additional validation experiments. Similarly, Reviewer #3, an expert in machine learning, is not convinced that the approaches taken are all state-of-the-art. Some cross-validation with other methods would help easing this concern for a future reader of a publication. Reviewer #2 raises the most critical point: although the claim of generality is made, the data presented relies on a single type of nano-particles. In the discussion among the reviewers following the initial evaluation it became clear that manuscript could only be considered if data from multiple nano-particles were shown. We suppose that acquisition of such complementary data will exceed the typical time eLife grants for a revision. Therefore, we have decided at this point to reject the manuscript. That said, there is significant merit in the combination of approaches, leading to a significant result. Thus, with a more thorough comparison of your approaches to others and a demonstration of applicability to other nano-particles we would consider a new submission of this work and make our best effort to send the manuscript back to the same editor and reviewers.

Reviewer #1:

In their work the authors propose a technique for quantifying nanoparticles distribution in histological samples. Hyperspectral imaging is based on the collection of images containing spectral information across a large (relatively speaking) range of the electromagnetic spectrum. Typical applications are found for military, geoscience, or environmentally studies. Here for each pixel within an image for example the signal across the visible or infrared spectrum is collected and hyperspectral data cubes are built and analyzed. Because different objects possess different optical properties, knowing a priori specific signatures allow classifying the information present within a scene.

In recent years this technique has found quite some success within the biomedical imaging field. Because metallic nanoparticles scatter light quite strongly at specific "resonant" wavelengths, the combination of darkfield microscopy and an hyperspectral approach has made it possible to successfully detect nanoparticles at high imaging speed and to separate them from the cellular background. Also the technique offers greater resolution when compared to other tools for studying biodistributions.

In the manuscript the authors report specifically on an imaging processing method to quantify nanoparticles distributions in tissue samples. The imaging setup is a standard one from CytoViva for "enhanced darkfield microscopy" equipped with a CCD camera for hyperspectral imaging. Previous work in the field is already present in my opinion. See for example a review paper from Brenner's group detailing recent works ("Hyperspectral microscopy as an analytical tool for nanomaterials"). Different groups have also presented several works demonstrating single-nanoparticle detection. See for example "Single-nanoparticle detection and spectroscopy in cells using a hyperspectral darkfield imaging technique" and others from Musken's group, and also another nice paper from Meunier group "Hyperspectral darkfield microscopy of PEGylated gold nanoparticles targeting CD44-expressing cancer cells" where 3D nanoparticles tracking is also demonstrated.

Because the authors concentrate on ex vivo tissue sections I found strange that very recent intriguing work from Brenner's group is not cited considering it is focusing basically on a very similar subject (i.e. "Identification of Metal Oxide Nanoparticles in Histological Samples by Enhanced Darkfield Microscopy and Hyperspectral Mapping" on JoVE 2015). It would have been nice to see a discussion and analysis of this work and in which respect the presented work differs from the cited one.

Having said that, I found the paper very interesting and very well written. There is a lot of work and data are very compelling. Also I think it could be of great interest. My only concern deals with the novelty of it (specifically see the paper mentioned above from JoVE).

Also, because the paper deals with the development of a machine learning algorithm I found myself a little bit in difficulty giving a judgement in this regard because I'm not a specialist of this particular field and I'm familiar with only the most common and basic approaches. From what I've seen a lot of sophisticated work has been done for hyperspectral classification in areas outside from the biological one (e.g. recently deep-learning based approaches for feature extraction for hyperspectral imaging have been implemented from different groups). Therefore, I honestly cannot judge in this regard and perhaps maybe someone with a specific imaging processing background in the field of hyperspectral classification (not necessarily limited to biomedical microscopy, but a more broad one) could perhaps provide more insights into it and comment on the novelty of the computational approach used here.

Reviewer #2:

Overall, this is an interesting paper that seems to have been executed with significant care. The figures are of high quality and the text is well written.

Strengths:

The authors use hyperspectral imaging to detect large gold nanorods (100 x 30 nm) in ex vivo tissues with single particle detection capabilities and single micron resolution.

They analyze histologically stained tissue slices from various organs, and the appropriate controls. From a technical standpoint, everything looks fine. I was expecting this technique to not work for aggregated NPs, especially in liver Kupfer cells, and they report exactly that, the honesty of which I appreciate.

Unlike many papers that provide descriptive multivariate models for their data, in this one, they use a training dataset to build the model, and then they use the model on unknown samples. This shows that the model has a high predictive power. I would be curious to see how well this method could distinguish between different types of plasmonic particles. Also, the particles used are ~30x100 nm2.

Weaknesses:

In my opinion the biggest weakness of this paper is that the technique is only demonstrated for one single nanoparticle type, and especially one that is not commonly used, i.e. large gold nanorods that are 100 x 30 nm in size.

However, in the Discussion the authors specifically claim that their technique is applicable to many nanoparticle shapes "(for example, gold nanospheres, nanorods, nanocages, etc.)" […]. "ABIDE is capable of distinguishing such NPs from each other by spectral differences, enabling biodistribution studies of multiplexed NPs." This is not only a bold claim, which importantly is not supported by any data.

The technique is only interesting enough for a broad audience if multiple different nanoparticle shapes such as spheres, cages, regular sized nanorods etc., can be analyzed with this method.

And my concern is that the technique will run into issues with discriminating some of the other shapes from cellular components, as can already be predicted when considering the curves in "Figure 1—figure supplement 4". The large gold nanorods have a plasmonic peak in the near infrared, which may be much easier to discriminate by the machine-learning algorithm than for shapes such as e.g. spheres.

The authors need to show convincingly that this technique works for the other nanoparticle shapes as they claim.

Reviewer #3:

The paper presents methods and results of combining mathematical modeling, data analysis, hyper spectral imaging, related to imaging of nano materials with applications in cancer, angiogenesis, and others. I find this area really interesting, and the potential impact large, although tissue and cell physiology are not my area of expertise. Though I find the ideas very stimulating, the main issue that I have is that the mathematical modeling/data analysis used here is not very clear, and may not be near top shelf work. Combined with certain choices of validation expanded below, my understanding is that the contributions to imaging methodology is not sufficiently novel, nor inspire a lot of confidence that results are as best as possible. See below for detailed comments.

Regarding modeling and data analysis, a few questions. The topic of discerning the contributions of different elements (in this case nano materials versus others such as Eosin, Hematoxylin, etc.) from spectral measurements is a well studied one. While I understand the intricacies of this imaging experiment are not the same as other more well studied spectral unmoving problems, I'm not convinced that the wealth of other methods for linear and nonlinear unmixing don't apply here. In the paper I did not find any discussion related to this. Classification methods of the type authors claim to have attempted (nearest neighbor, SVMs, etc.) could be applied on such unmixed data, and to me this would constitute a more standard way of doing things. As is, the methodology regarding data analysis coupled to imaging does not seem very novel, and it is not presented in a way that can be related to many other already proposed methods to other seemingly similar applications.

Regarding the data analysis for validation, a couple of things seemed unclear to me. For the detection of false positives and false negatives, were these evaluations performed separately? And if so, is the validation criterion computed by checking whether there is one single pixel indicating nonmaterial (in case of false positives) present? Similar comments for the reverse situation (false negatives). It would be necessary to know the specifics of these details better, and even better have the data (e.g. histograms and if pixel counts are used, how thresholds are utilized). Also, how is the user defined parameter (it seems a manually selected threshold is used to initially determine if a pixel is potentially LGNR) handled during validation? Is data used in the validation stage also used by the user when selecting this parameter? It is a little confusing when in the subsection “Data processing and automatic biodistribution detection” the authors comment "We then manually (and in a manner blind to algorithmic classification)…". How is this possible given that for a positive detection the pixel must be classified as potential LGNR first? Am I missing something, or is it possible that authors are mixing training and testing data?

A few more comments below:

The Results section reads more like a Methods section. If format is to be followed, I'd suggest only describing results in the Results section.

Results, second paragraph: K-means is most commonly referred as a clustering algorithm. Once clusters are identified, one can use this information to design a multitude of classification methods, but authors must specify which they used. Presumably the simplest would be the nearest neighbor cluster center. Are the cluster centers utilized as ground truth?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "A hyperspectral method to assay the microphysiological fates of nanomaterials with single-particle sensitivity" for further consideration at eLife. Overall, your revised article has been favorably evaluated by Sean Morrison (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance. They mainly concern the tendency of 'over-selling' some of the approaches and accomplishments of the work. We especially encourage you to reconsider the use of an acronym for this technology. We are concerned about the use of acronyms as cheap eye-catchers. Moreover, a new expert in machine learning has been brought to the panel because previous Reviewer #3 was unavailable. Given the rapid pace of the machine learning field it seems inappropriate to call the application of a clustering method (and even a very classic one, which is taught in undergraduate computer science course) 'machine learning'. It is perfectly fine to use standard methods if they solve the task, but there is a discomfort among reviewers that machine learning is merely used as a catchy phrase in this case. This could fire back on your work. We thus encourage you to revise some of the language in your manuscript, including the Abstract, and to address the few other comments listed below.

Reviewer #1:

I've found that the authors’ comments are very appropriate and to the point even though in some cases I'm not too familiar with some of the points discussed. My major concern is always related to my original comment. Previous similar work from Brenner using a basically identical setup hardware is already present in the literature. Because the scientific contribution of the submitted paper consists in proposing an analysis procedure based on a machine learning algorithm with the intent of extending the work of Brenner and co-workers and others, it is critical to determine the novelty of the proposed algorithm. Overall I found the data provided by the authors very compelling and particularly interesting.

Reviewer #2:

The authors are now showing feasibility data from two other nanoparticle shapes, and have therefore satisfactorily addressed my previous main concern whether ABIDE may be versatile enough with regards to different nanoparticle shapes and sizes.

There are a few remaining issues.

General comment: The revised version does not include any tracked changes or other markings to indicate where changes were made, which made the review of the paper quite difficult. I am making this comment not because I want to review another version with track changes, but to make it clear that this limitation may have reduced my ability to catch all remaining or new issues.

Specific comments:

1) In the PowerPoint slides the authors provided in their rebuttal (for the reviewers only), it says "Example of new in vivo data". I find this misleading, as I could not find any data in the entire paper that was acquired "in vivo". A reviewer who does not carefully examine the manuscript may be misled by the rebuttal summary slides that this is in fact all acquired in vivo and not catch this discrepancy between the summary and the actual paper. I am not expecting the authors to provide true in vivo data, but would like to clarify what the authors meant by that.

2) The title of the paper is overstated with regards to claiming "single particle sensitivity" and this needs to be changed or else would be misleading. Figure 2—figure supplement 8 is the only figure that shows any data that would support that, and only in the very large gold nanorods (which by some definitions would not represent a nanoparticle). "Likely" as is stated in the figure legend is probably an honest assessment by the authors, but not enough to make such a major claim, and there is no evidence for this to work in the other two nanoparticles that are now included. I suggest replacing "…with single particle sensitivity" with "… in tissue sections" or "… in histological slices".

I would be willing to accept the manuscript pending these clarifications/changes if the other reviewers agree that their areas of expertise were addressed sufficiently as well.

Reviewer #4:

This revised manuscript describes an interesting and straightforward development of an approach for detecting nanoparticles in hyperspectral dark field images. It has been significantly improved based on comments in the initial reviews. The results presented demonstrate an impressive ability to detect and quantify these nanoparticles in tissue images. From an image processing/analysis/machine learning point of view, the approach is not novel or instructive (clustering spectra, especially with manual tuning, barely qualifies to be called machine learning, and does not seem to warrant a new acronym). Hence the significance of the manuscript must derive from the future importance of the method's application, something this reviewer is not qualified to judge.

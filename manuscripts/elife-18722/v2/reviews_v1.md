# Peer review - Round 1

Editors:
- Sriram Subramaniam, National Cancer Institute , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18722.023](https://doi.org/10.7554/eLife.18722.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Accelerated cryo-EM structure determination with parallelisation using GPUs in RELION-2" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom, Sriram Subramaniam, is a member of our Board of Reviewing Editors, and the evaluation has been overseen by John Kuriyan as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Steven J Ludtke and J Bernard Heymann. A further reviewer remains anonymous.

Following extensive discussions with the reviewers, we are willing to re-review a revised version of your manuscript. The revised version must address all of the technical comments from the reviewers and include a substantive technical section with more details of the software implementation, as well as a more extensive description of suitable platforms with a credible comparison of performance.

The main points of this discussion are noted below:

1) There was agreement that the main point of this manuscript was to advertise the existence of a GPU port of Relion, which many people in the field will likely wish to use. The changes to Relion described in the manuscript do not improve the scientific results, but improve computational efficiency that could potentially accelerate discoveries. Nevertheless, the reviewers expressed doubts that the increase in computational efficiency would stand out as a significant advance technologically or methodologically.

2) The reviewers also noted that the extent of the performance improvement with GPU was exaggerated and potentially misleading; this is an important parameter because this would lead to users making purchasing decisions without the correct facts. While the reviewers felt it is not possible to be completely equitable when comparing completely different hardware platforms, the views was that this manuscript is more strongly skewed towards GPU for the following reasons:

a) Very different generations of hardware were compared (the CPUs are 4 years older than the GPUs, and many changes have been made to CPUs in that time)

b) The code in Relion 2.0 was substantially optimized in the GPU version; it seems that many of these optimizations could be easily included in the CPU version of Relion 2.0. A better comparison would be to compare equivalent generations of GPU/CPUs, and equivalent versions of Relion.

3) There was concern that the specific improvements to the code that helped improve GPU performance were not identified clearly and that it was difficult to tell which are only of interest for GPU and which can be implemented for CPU. A portion of the community may have strong interest in the details of these improvements, while others will likely only be interested in the question of which platform is more likely to be cost efficient and remain relevant over a relatively extended lifetime. However, this manuscript does not lay out these improvements clearly for the first group, but also does not provide fully controlled comparison of comparable platforms for the second group.

The suggestions from the reviewers follow:

1) The manuscript needs to include a paragraph discussing previous EM work that used GPU implementations, encompassing the references listed below. Pubmed /26592709 is cited in section 2.1 in another context, but not for GPU implementation.

http://www.ncbi.nlm.nih.gov/pubmed/20538058http://www.ncbi.nlm.nih.gov/pubmed/24060989http://www.ncbi.nlm.nih.gov/pubmed/26370395http://www.ncbi.nlm.nih.gov/pubmed/23644547http://www.ncbi.nlm.nih.gov/pubmed/20558298http://www.ncbi.nlm.nih.gov/pubmed/26592709

2) It would be beneficial to include significantly more algorithmic details in the paper. The way it is currently written seems to present mainly the benchmark tests, while leaving largely absent the explanation of what was important for the development of the GPU code.

3) On a technical note, regarding the experiments made for comparing CPU and GPU code and between single and double precision, one would assume that the authors used the same initial model, parameters and random seed in all cases (--random_seed option in RELION) to initialize all the runs, but this is not mentioned anywhere in the text. If this was actually done, a fairly thorough analysis of the assigned orientations and orientational probabilities could've been done where the single difference between the runs would've been the different program implementations.

4) In paragraph one of the Results section, the mention of what the authors believe to have the most prominent influence on performance is only vaguely explained:

"To overcome this, our implementation instead stores oversampled Fourier transforms of every class-reference in GPU memory, and extracts 2D-slices (in any orientation) on demand. By utilising fast-access data structures known as textures (normally used to project images on 3D objects), on-demand projection in fact achieves faster execution compared to reading pre-calculated projections from memory."

i) The authors claim to store oversampled Fourier transforms of every class-reference in GPU memory. What kind of transforms are being referred to, 3D or 2D? If this is a 3D oversampled FFT volume, then it should be mentioned and the sentence needs to be corrected to have one FFT transform per class-reference. On the other hand, if the authors mention 2D reference FFT slices (which is less likely because it is not consistent with the on-demand projection statement), they need to elaborate on how many such slices they used and on angular sampling strategies.

ii) The authors need to expand upon using texture operations for the on-demand projection. Specific citation(s) would be helpful.

5) There are inconsistent statements regarding the differences between the methods used in RELION 1.4 and the new accelerated version of RELION. On one side the authors state: "Neither method nor behaviour of RELION has changed from that of version 1.4.", but later on they describe algorithmic changes to the particle picking strategy in Section 2.2. The only tangible difference appears to be the discarding of resolution information in micrographs beyond that of search templates, but this has to be properly highlighted and the statement in Section 2.1 revised to reflect the fact that there are changes, albeit subtle, between versions 1.4 and 2.0 other than the GPU speedup. It will save end-users time and confusion if all of the changes are documented.

Is it correct that Relion adopts a maximum-likelihood approach, and not a Bayesian approach because all the priors (distributions) it uses are refined? It would be good that a person familiar with the difference between "Bayesian" and "Maximum Likelihood" could clarify this point to get it right in the published version.

6) There are several comparisons noted in the paper that need to be clarified.

i) The comparison draw between overall processing time and the time it took the authors to download the data from EMPIAR is meaningless, there are many factors that can influence data download speed of large datasets and to use that as a benchmark can be misleading. The typical RELION user will probably not be downloading data from a database for processing but instead would be collecting and processing their own data. A comparison against the time it takes to collect data would therefore be more appropriate and provide the reader with a better reference point about what the other rate limiting steps in single particle cryo-EM. Another useful comparison is to estimate the number of CPUs required to process the data in the same time (115h) that it took for a GPU-driven solution.

ii) Distributing a job across a cluster leads to substantial overhead (e.g. network traffic) that will not be present when running on a single workstation. While it may be justified to look at the overhead as one reason for the slower execution of jobs on CPU systems, this should ideally be separated in benchmark tests from the actual CPU hours needed to complete the job. Maybe some of the tests could be rerun on a single workstation to exclude cluster-related overhead.

7) It is not clear who might be the intended reader of the manuscript. It is clearly not meant for an average user of Relion package, who most likely is a structural biologist oblivious to intricacies of computer code and its dependence on hardware platform. The problems mentioned are immediately apparent at the beginning of the Results section. The fact that "class" is used to mean "3D structure" took me by surprise, particularly that one has to compare Figure 1 with Figure 2 to realize that. Some formulations are cryptic – "Even individual image pixels are evaluate independently from on another". Specifically how one evaluates individual pixels, for what purpose, and why doing it independently would constitute an advantage?

Results section, first paragraph; what is "class-reference"? What follows is difficult to understand – if, as stated, 2D slices are extracted from a presumably 3D volume, this constitutes a projection operation, but next sentence casts it in doubt, as it is stated this is being done using textures "normally used to project images on 3D objects". So it is not a projection? Or some other projection is meant?

Subsequently, much is made of the number of classes, but it is not clear what these classes are and why one would want to have them. How their number is decided? What if one wants to preform analysis without any classes, is it possible? What would be the speed up?

The most cryptic is the closing sentence of the section: Neither method nor behaviour of relion has changed from that of version 1.4. First, what is so special about version 1.4? How a casual reader is supposed to know that or worse, care about this number? It would also appear the statement is contradicted by what follows, as much is made of single precision GPU implementation as opposed to double precision of the general purpose original code. On a side, why double precision is "so-called"? I am not sure what is meant here.

Finally, section on Limited precision does not offer much outside of generalities and ends at a surprising statement: "Execution of the iterative gridding algorithm.… appeared to show significant loss of information." Appeared? How carefully was it investigated? What is "significant"?

8) Figures are microscopic, which probably reflects authors' interest in atomic-scale objects, but at the same time they are filled with details essential for the understanding of the text. In the very least, they should be properly referenced in the text in key places. The final maps should also be deposited as is customary in the field, this intent is not indicated in the manuscript.

9) As this manuscript may entice people to spend tens to hundreds of thousands of dollars in research funds, it is incumbent upon the authors and reviewers to insure that this study is as balanced and fair as possible. There was a similar pro-GPU move ~8 years ago, Frealign, EMAN2 and SPARX were all parallelized for the GPU, achieving typically 20-80x speedups, and many purchased hardware, but few made effective use of it for very long. While the reviewers do not dispute the accuracy of the presented results, they believe that the results are highly biased based on the specific hardware selection, and on issues not discussed in the manuscript.

10) There is some price/performance advantage in GPUs, but the current estimate is simply ludicrous, and many people reading this manuscript will not understand the technical differences. Primary issues that occur immediately are:

– The processors used on the 120 core test is a 4 year-old processor considered "end of life" by Intel. These are being compared to a set of 4 GPUs so new they are difficult to acquire at most vendors. The vectorization and architecture changes made by intel in recent years, major hyperthreading improvements, and other factors will come into play. Specifically:

–- CPU optimization for the specific processors in use? Image processing code compiled for specific current generation CPUs with -march=native often see 30% or more speedups, without any coding changes.

–hyperthreading use. This likely will not have an impact the older processors in the 120 core test, but Xeon v3 processors can often see speedups of ~30% even on compute-intensive loads with moderate thread oversubscription.

– Were the core parallelism improvements made for the GPU (those which were applicable) also compiled into the CPU version?

– Running on 120 cores implies use of MPI, and brings many other factors (network, available I/O) into play when comparing speed.

– Was the CPU computation done with single precision at similar points to make the comparison fair?

In Figure 4D, the authors are claiming a 10-40x price-performance improvement. One reviewer notes that he/she configured two machines at a reputable, but inexpensive vendor. Both machines had 64 GB of RAM, a 1.2 TB SSD. One was configured with 4x 1080 GPU cards and 8 CPU cores at 2.6 GHz. The other was configured with a base-level GPU for display and 2x E5-2697Av4 -> 32 cores @ 2.6 GHz. Both machines come in at ~$9000. As compared to their "one node", this machine has 32 rather than 12 cores, and with improvements in the CPU, each is ~1.5x more powerful than their test machine. This would already bring their price/performance comparison down by 4x, ignoring other issues.

11) The reviewers do not believe the current comparison in the manuscript is fair without at least some attempt to test on current generation CPUs with some real attempt to insure things are compiled and executed optimally. This need not be a month-long test, but at least a few iterations of a single model refinement to establish a baseline for modern hardware. As the major point of the manuscript is benchmarking, this is a minimum requirement for publication.

12) The following statements are not clear:

"In fact, using GPU-enabled relion, the time needed for classification is only weakly dependent on the number of classes used, whereas the CPU-based implementation has a much steeper linear dependence (Figure 3)"

and:

"In the CPU-only version, the computational time scales linearly with increased number of classes (Figure 3B) due to the serialised single image calculations, whereas GPU-enabled execution can show better-than linear scaling."

Looking at Figure 3B, this is not clear. The GPU curve also visually appears to be following a linear trend, and rough estimates show a similar scaling to the GPU curve.

The values on the GPU curve are small enough compared to the size of the dots, this is difficult to assess quantitatively, but this figure certainly doesn't illustrate the point being made.

13) In Figure 3E, the prominent lump in the middle is quite odd. The statement "GPU's ability to parallelise the drastically increased number of tasks" does not really explain it. If N independent tasks need to be completed in iteration 10, and 30N need to be completed in iteration 15, the only way this curve makes sense is if the GPU is massively underutilizing resources during iteration 10. It also would make no sense that going from 7.5 to 3.8 degree sampling would increase the number of tasks 30-fold. Something very peculiar is going on here, and it seems important to understand it.

"While relion-1.4 only exploited parallelism over images (left), in the new implementation classes and all orientations of each class are expressed as tasks that can be scheduled independently on the accelerator hardware (e.g. GPUs)"

Could the same change not be tested on CPUs as well?

14) Figure 4 – Why is this test suddenly shown for a ribosome? How does this compare on the benchmark ΒGal data set?

15) The use of GPU's is usually problematic because of rapid progress in GPU technology. This means that many different GPU's are available and in particular older one's suffer from poor feature support. The authors need to explain exactly what is required in a GPU and which GPU's are too old or inadequate.

16) The loss of information in the gridding reconstruction algorithm using single precision is not explained clearly. Typically, this indicates very small or very large values that could be avoided by some normalization approach. This could also indicate that the iterative refinement in the gridding algorithm is too fast, generating instabilities with single precision.

17) In the Introduction, the authors mention some other software packages giving the impression of a comprehensive list. However, some software packages are left out. Either be comprehensive or be more general in referring to the wiki showing software packages.

18) "This allows high-resolution structure determination with minimal bias or user input." The impression is that a Bayesian approach is less biased than other methods. This is incorrect, as Bayesian methods are just as biased as any other when it is fed erroneous data (such as poorly picked particles) or an inappropriate starting reference (prior) is used.

19) There is no information about the availability of the package (web site and license) or about deposition of the maps.

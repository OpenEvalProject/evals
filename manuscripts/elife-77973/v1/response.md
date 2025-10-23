# Author response - Round 1

Authors:
- Alexej Schatz ([ORCID: 0000-0002-2664-2103](https://orcid.org/0000-0002-2664-2103))
- York Winter

## Response text

DOI: [10.7554/eLife.77973.sa2](https://doi.org/10.7554/eLife.77973.sa2)

[Editors’ note: what follows is the authors’ response to the second round of review.]

– Remove language about other packages not meeting their claims re: stress test (as they were not tested).

I have removed "unlike others" in line 17. This did not refer to performance, but to the number of IOs that can be controlled simultaneously. For example, Bpod natively has only 2 inputs and 2 outputs, more only via module ports. Also, monitoring and simultaneous reaction to multiple events is possible, but relatively complicated (not only in Bpod). This has to do with the state machine. That is why other packages were not subjected to the stress test: number of IOs is not comparable. Nevertheless, my statement was misleading and has been adjusted.

– Clarify wording on stress test results (see R#2 review).

The description of the “stress” test is reworked. All y axes have a label.

– Describe means of measuring timings on both LabNet and other packages.

A diagram is added as an illustration. Tests description of the “read and set GPIO” is reworked.

– Link to specific versions of code for each of the tests.

Source code for Autopilot, Bpod and pyControl tests is inside the article’s data and source code repositoty. See the “key resources table” and “Code availability” sections. Previously inside the zip archive, now as clear text inside extra folders (autopilot, bpod and pyControl).

– Describe versions (with git hashes or semver) of all software, LabNet and other packages.

See “key resource table”.

– Respond to R#1 questions about example tests for other packages.

All tests for other tools are runnable. The measurement for all tools (including LabNet) was done in same way.

– Describe an example experiment done within the lab using LabNet and how it fits into the rest of the experimental setup.

A description of some so far built systems is now at the beginning of the discussion chapter.

– Label the axes in all figures.

Done

– Clarify the benchmarking protocol well, with a diagram.

Done

– Please include a key resource table.

“key resource table” is now included at the beginning of the “Materials and methods” section. It contains links to repositories of all tested packages with SHA hashes and versions if available.

Reviewer #1 (Recommendations for the authors):

General comments:

– Many of these will read as negative, so I want to start by saying I appreciate the author's work, apologize for the lateness of my review (life has been hectic pre- and post-dissertation!), and thank them for writing this package! All that I don't comment on here I think is good.

– In general I like to see software timestamp measurements supplemented with hardware measurements (from eg. an oscilloscope), even just to confirm that the software timestamps are close. I don't think it's of huge importance here, but I wanted to make that future recommendation to the authors, especially when taking timestamps from an interpreted language like Python.

We can verify the results very easily. We know that the Bpod state machine is running at 10kHz. My test result for Bpod is 0.1ms with nearly 0 STD. Which is exactly the same as 10kHz. My test result for pyControl is very close to the results reported in the pyControl article in eLife. Additionally, I connected on the RasPi used for the measurements two pins together; this was to verify how fast the measurement software can detect input events. The result was 1 microsecond (also reported in the paper). And, of course, this measurement software was written in C++ (not Python) and ran on its own RasPi with no other software running on it. Thus, the RasPi functioned as a 1MHz oscilloscope and we can be sure that the measurements are correct. In addition, all software packages were tested in the same way. If there was a time offset, it was the same for pyControl, Bpod, Autopilot and LabNet.

– The mismatch between L84-L88 and the results is made more salient with the addition of L143-L147 – L84-88 say Python is intrinsically slow and thus C++ was chosen, but then L143-147 say that Python has an advantage because the C++ implementations are more complex. L84-88 thus read like theoretical concerns that were demonstrated here to not be true because of additional details in the C++ implementation, right?

The statement that Python is slower than C++ is of a more general nature. Python is normally executed by CPython. Critical and most important parts in CPython are implemented in C. This is also true for many important packages like NumPy. Thus, as long as a Python program does not require multithreading, has very few calculations directly in the Python code (outsource to C, e.g. via NumPy) and does not have a complex program flow, it can be just as performant as C++. Unfortunately, this is only true for simple programs, like our client implementation used for the article.

– I appreciated the expanded discussion of the intended uses for the package, like the discussion of the potential for using multiple pis together, etc. I think that and the brief descriptions of potential tasks help the paper!

The discussion now contains an overview and description of systems that have already been built using LabNet.

– I don't see a discussion of documentation in the main text, I don't think it's worth holding the paper up over, but I again make the recommendation to the authors to at least discuss their plans for documentation and future maintenance, as that is really the critical factor for whether a package like this will be adoptable by other labs. The authors briefly address this in their response, but yes this is important information for prospective users to have!

The documentation is now addressed at the end of the discussion. It is planned with much more detail for the next major version of LabNet, which is also already in development.

– Some of the other concerns that I raised in the prior recommendations for the authors were not addressed, perhaps that was my fault in not understanding how the public review. vs recommendations to authors work at eLife.

We have been careful to consider all points raised. With that in mind we have again carefully checked the manuscript.

Figure comments:

Additional comments on new text:

– Listings: The inline comments and in-text descriptions are much appreciated!

– Figure 1: You designed that in TikZ? I am amazed. I would love to see that code. I checked out the TikZ code for the other figures and am very impressed.

source code for all figures is now included.

– Figure 2b-d: The y-axes are unlabeled.

now all y-axes have labels

– L17-18: I don't see stress test comparisons for the other packages, so the "unlike others" doesn't seem to be supported by the text.

removed, more in first response

– L18: typo, latenies -> latencies.

– L61-63: This seems like an odd definition of openness to me, which typically means either that the source is inspectable. I would call the "control an experimental chamber on its own" part independence or modularity, and the "or together with a number of other nodes" interoperability or scalability. I am unsure how one would use multiple LabNet nodes in the same task, as an example doesn't seem to be in the text! This also seems to contradict L66-67 "However this comes with the restriction that at most one experimental system can be connected to each RasPi" – what counts as an experimental system here? are the authors just referring to a particular set of hardware components which could be combined in a single experimental chamber? that clarification would resolve the conflict to me.

The definition of openness and scalability refers to the distributed network and not to the source code. The definition also comes from Tanenbaum's book. Anyway, I adjusted the text here a little, hopefully it makes it clearer.

Examples of experimental systems are shown in Figure 1. Now also in Figure 4. The discussion contains now a brief description of so far built and with LabNet controlled system. But actually, anything can be an “experimental chamber”. Even Listings 1-3 already describe a system; a poke sensor, a valve and an LED. Small and simple experiments can already be realised with this hardware.

What is actually described here is that we want to bring any number of experimental systems into a network and then control them simultaneously. With one or multiple clients.

– L71-72: I am not sure what this means, the client is the controlling computer, but not sure what a task is in this context. And I thought that the hardware control happened on the raspi (server?).

Changed “task” to “duty”. Actually, the “task” or “duty” is in the first part of the sentence: “hardware control in the context of the experiments”. I added a new sentence.

– L72-73: from what I recall you also provide clients in these languages? might be worth some clarification describing what you mean by writing clients in multiple languages – eg. that clients written in multiple languages can interact with the underlying C++ library?

The sentence was moved to the end of the paragraph and now explicitly refers to Protobuf.

– L171: I found the description of the new crossover-based tests a bit hard to follow and it took me a few reads, I think a diagram would be helpful here :

The description is reworked. A diagram is added as an illustration.

– L210-221: I can't really tell how the code works for the new tests, it would be really helpful to link to the source code for each of the tests in the main text so we know what you're referring to! for example, the stress test looks like it does not send instructions of the network but operates on local logic as well: https://github.com/WinterLab-Berlin/LabNet/blob/3963f3371610d828e44af1e27ba6374cacc79748/examples/cpp/perf_test/main.cpp

The link leads to the measurement software that ran on the second RasPi. It generates the test signal and waits for the reaction from the LabNet, Autopilot, etc and saves the measured latencies locally in a csv file. It has no LabNet dependencies.

I see the data availability statement and found the repo, but it would be nice to have those separated out instead of inside of a zip file so you could link to them.

Source code for Autopilot, Bpod and pyControl tests is now inside extra folders in the repository (autopilot, bpod and pyControl).

– L228-229: The inclusion of whisker now reads as odd, since I think assuming latencies based on polling frequency is probably a pretty bad assumption in most cases.

Polling frequency normally gives the worst-case times. But of course, there may be other factors which can impact the latencies.

– L218-241: I am not sure how the latencies are measured for the other systems, as it looks like you were taking software timestamps for the LabNet tests, but I don't see timestamps being taken in any of the other comparison tests, so I assume that external timestamps were being taken? It also seems like some external trigger would be needed in some of these tests as well (see below)? It is also important to validate any software timestamps with external hardware timestamps, and they shouldn't be mixed without validation (eg. software timestamps could either exaggerate or underestimate latencies depending on where they are taken). Some additional clarification is needed here.

Latency measurements with Autopilot, Bpod and pyControl were done in exactly the same way as with LabNet. The second RasPi with the same measurement software was used for all tools. The description at the beginning of “Comparison” chapter is changed to reflect this. And yes, an external trigger is needed in all tests, this was provided by the second RasPi. The second RasPi is also the time reference. And because it runs completely independently from all tools, the measurements are comparable and just as good as with an oscilloscope. The measured latency data for Autopilot, Bpod and pyControl are also a part of the second repository.

From my reading it doesn't look like the pycontrol or autopilot tests would work, but I am out of the lab and don't have a π to run them on myself.

All tests are runnable. After the latency time tests, the source code was added to the repository without modifications. The pyControl test is very simple, see my short description below, but needs a bit of pyControl API knowledge. The Autopilot test is a simplified version of the “free water task”, from the official Autopilot repository.

For the pycontrol test, it seems like it would go

- on_state(event='entry') -> p_off

- off_state(event='p_off') -> goto on_state

- on_state(event='entry') …

and if the 'on' state was triggered manually from an external trigger it would go like

- on_state(event='p_on') -> goto off_state

- off_state(event='entry') -> switch p_out.on()

- on_state(event='p_on') -> goto off_state

- off_state(event='entry') …

But I admit I am not altogether familiar with pycontrol. Some comments in the source would be lovely.

The pyControl test is very simple. “p_out” is a digital output, acts as response to the external event. “p_in” is digital input with “p_on” as rising and “p_off” falling events. “p_in is also the external trigger event which comes from the measurement RasPi. Short state machine description:

– enter “on_state” -> turn “p_out” off

– wait until external trigger “p_on” -> go to the state “off_state”

– enter “off_state” -> turn p_out on

– wait until external trigger “p_off” -> go to the state “on_state”

– repeat from beginning

For the Autopilot test, there are two stage methods in a cycle, water() and response(). the water method clears the stage_block which would cause the running pilot to wait for any set triggers. A trigger is set for the 'sig_in' pin that should set the 'sig_out' pin high. When the sig_in trigger is received, that should cause the response() method to be called which sets 'sig_out' low after some delay and then return to the water stage immediately. This would require some external input to trigger the sig_in event, and then the timestamps of the external input and the sig_out pin would be compared. If the sig_out pin were wired to sig_in, the test wouldn't work, as the sig_out pin would never be set high. Having the `prefs.json` file from the pilot would be useful to include here to avoid ambiguity in system configuration, as I am assuming the default polarity configuration settings are used on the digital input and output classes.

The file “prefs.json” is now included and inside the “autopilot” folder. As with other tools Autopilot’s RasPi needs to be connected with 2 pins to the measurement RasPi. Autopilot needs to wait for the external events and reacts to them. The time is only measured on the second RasPi, not on Autopilot’s RasPi.

A set of tests that are more similar to the tests described for labnet are available in the plugin accompanying our manuscript: https://github.com/auto-pi-lot/plugin-paper/blob/c6263a4890b7d6101688158d8acb3aaeb9199533/plugin_paper/scripts/test_gpio.py documented here: https://wiki.auto-pi-lot.com/index.php/Plugin:Autopilot_Paper We find the roundtrip (oscilloscope measurement of input to output) latency to be 400us.

These tests contains nearly no Autopilot functionality. E.g. in the "test_readwrite" test, a function is simply assigned to the pigpio callback and pigpio automatically calls this function when a signal is present. Thus, it tests only the speed of pigpio and its Python interface. I don't think real experiments in Autopilot work that way.

The “read and set GPIO” in our paper produces much more realistic latencies. Simply because all tools, including LabNet, have to use their regular logic like they would to run experiments.

I don't doubt the authors ran the tests, and please correct where my read of the code is wrong, but I think some additional detail is needed in the reporting of the results in any case.

I think that the test description in the previous version of the manuscript was misleading. It has now been rewritten. The former version arose because I wanted to describe the connection between the measuring RasPi and LabNet/Bpod/pyControl/Autopilot very precisely. Unfortunately, it became too complicated. Actually, there are only two pins connected. One as an external trigger and the second as a response. The tests as described now should be understandable.

Reviewer #2 (Recommendations for the authors):

The manuscript introduces LabNet as a network-based platform for the control of hardware in Neuroscience. The authors recognize and attempt to address two fundamental problems in constructing systems neuroscience experiments: on one hand the importance of precise timing in the measurement and control of behavior; on the other hand, the need for flexibility in experimental design. These two goals are often at great odds with each other. Precise timing is more easily achieved when using fewer, dedicated homogeneous devices, such as embedded microcontrollers. Conversely, flexibility is more easily found in the diversity of devices and programming languages available in personal computers, but this often comes at the cost of a non-real-time operating system, where timing can be much harder to predict accurately. There is also a limitation on the number of devices which can be simultaneously controlled by a single processor, which can be an impediment for high-throughput behavior studies where the ability to run dozens of experiments in parallel is desirable.

LabNet proposes to address this tension by focusing on the design of a hardware control and instrumentation layer for embedded systems implemented on top of the Raspberry π family of microprocessors. The idea is to keep coordination of experimental hardware in a central computer, but keep time-critical components at the edge, each node running the same control software in a Raspberry π to provide precise timing guarantees. Flexibility is provided by the ability to connect an arbitrary number of nodes to the central computer using a unified message passing protocol by which the computer can receive events and send commands to each node.

The authors propose the use of the C++ programming language and the actor-model as a unifying framework for implementing individual nodes and present a series of benchmarks for evaluating the performance of LabNet in the Raspberry Pi, followed by a series of benchmarks comparing LabNet against other established hardware control platforms.

The first set of benchmarks is presented in Figure 2 and is used to understand how LabNet retains its performance across a variety of different Raspberry π hardware, and clients written in different languages (C++, C# and Python). Different tests are used to measure latency over the network (Set digital out test), and full round-trip latency by using a digital input event to directly trigger a digital output through LabNet (Read and set GPIO test).

A new stress test is also introduced in this revised manuscript to evaluate how many pins in parallel can be monitored by LabNet. Unfortunately, the plot in panel C is confusing, since the text mentions a measure in events per second, but the plot seems to have the same range of values as the other panels in the figure, and the axes are not labelled, so it is not clear whether we are watching a drop in processed events per second, or a drop in latency. This should be clarified, and all axes labelled accordingly.

The text has now been modified: the results in the figure are described briefly first, then the events per second.

All y axes now have a label.

The methodology of the tests is hard to follow from the text description alone. It would be useful to have a schematic diagram of the wiring used in the test, as well as an example interaction diagram with a timeline of how the different events in each component (PC and Raspberry Pis) trigger each other and which time intervals are being measured.

The test descriptions have been changed and simplified. They should now be easier to understand. A time signal diagram is now included.

A second set of benchmarks is then presented in Figure 3 comparing LabNet to other established hardware control platforms. These are used to inform how well LabNet running over the network compares to different platforms running on local hardware.

In the revised manuscript, the authors use the same "read and set GPIO" test used for Figure 2. The authors demonstrate that LabNet achieves similar latencies to the local platforms despite hardware control running over the network. The tests are fair, and the results support the authors' conclusion, although it would have been preferable to include an independent measure of electrical signal timing for the Read and set GPIO test through an oscilloscope to exclude possible confounds with different software timestamping strategies of events in the different platforms tested (see for example Akam et al., 2022).

See my responses above to the first reviewer.

The manuscript concludes with a Discussion section highlighting the possibilities for interfacing with different hardware using existing LabNet adaptors for the Raspberry Pi. Here I remain at odds with the authors as I don't believe they have convincingly demonstrated their stated aim of ease of extensibility either in the client or in the server, which I feel is crucial to introduce LabNet as a platform for the open-source community.

Some examples of operant boxes for rodent experiments controlled by LabNet are presented in Figure 1. A variety of different devices are represented in the example schematics, mostly digital inputs and outputs, but also a visual display monitor and a tone generator, both mentioned in the discussion, the latter also in the code listings. The variety and heterogeneity of hardware components in such tasks is typically challenging to coordinate and synchronize in a full experiment so it would be great to understand how exactly the authors envision LabNet to play a part in the assembly of such experiments.

The synchronisation is automatically given from the order in which the events (also from several RasPis) arrive. The coordination is given through the experiment logic.

Unfortunately, none of these complete examples are developed in the body of the text, and it is unclear whether these are actual experiments collecting data in the lab. The authors have argued that listings 1-3 present code examples of a simple "experiment". However, these seem to be mostly restricted to setting up and configuring individual modules and single commands in LabNet. It is not clear how these basic building blocks are expected to be used to coordinate multiple devices in the context of an application running a full experimental protocol, and what are the caveats and limitations in such a case from a developer's perspective.

Unfortunately, it would be beyond the scope of this article to describe the client side of the experiments. The focus of the current article is clearly the core LabNet functionality that is independent of specific client implementations. With listings 1-3 we describe exactly what a developer of client software has to do: open TCP/IP connections to all LabNet/RasPi devices, initialize hardware, communicate with hardware. It does not matter how much hardware is connected on how many RasPis the logic is always the same.

Specifically, it would have been important to see how well the code listings 1-3 would scale up or integrate the control of a full behaviour task with multiple conditions, or how to synchronize and benchmark the system when integrating with other hardware, such as cameras or physiology recordings. Even if LabNet is just a small component of the final system, it would be important to describe more fully a few examples as this would allow the non-technical reader to make a quick assessment of the versatility of LabNet for different types of experiments and to make it clear where exactly LabNet fits in the design of an experimental rig.

A description of some so far built systems is now at the beginning of the discussion chapter.

Is the system targeting only rodent tasks or is it reasonable to adapt the system to work for Drosophila or zebrafish? Can nodes easily support the simultaneous generation of pulse trains, visual stimulation, and video capture, and if yes how many tasks should each node be responsible for to optimize control bandwidth? Given the generality of the Raspberry π platform, I feel it would be important for readers to find some of these answers in the manuscript, even if just in the form of suggestive examples, to clarify how LabNet might be positioned in the space of open-source hardware in neuroscience, now and in future versions. A table listing exactly which modules are available would also help to make users aware of the possibilities of the platform.

We think that the large advantage of LabNet is that it can be used universally for laboratory experimental automation, both within and beyond neuroscience. It is agnostic to the species under study and we have used it from bats to flies. A description of some so far built system is now at the beginning of the discussion chapter.

The LabNet architecture with actors targets explicitly the execution of multiple tasks. The Discussion chapter contains now a small discussion about performance and bandwidth. So far, we never had performance or bandwidth issues with LabNet/RasPi. But this excludes applications with video acquisition. A list with already available interfaces is in the “Implementation” subchapter.

Alternatively, given the experience of the authors in developing embedded animal behaviour platforms for several years, taking a few samples from that pool of experiments redesigned in LabNet would be very valuable to evaluate how this new software can help to address and alleviate common implementation bottlenecks.

We wanted to address two points with LabNet: performance and the possibility to control a large number of experimental systems. We succeeded (as we think) in both and both points are now discussed in more detail in the paper.

Finally, the ease of the framework SObjectizer in extending LabNet is discussed. The reorganization of the document to move the implementation details into the Materials and methods section has overall made everything easier to read and follow.

I would have preferred, however, to see more examples on how to extend LabNet for a new custom device, compared to existing platforms such as Arduino or pyControl, in addition to the lengthier discussion of actor models. Even though a software plug-in system is not currently supported, it is possible to extend LabNet by modifying its source code. However, all listings in the paper currently target only the PC client side of LabNet. It would be great to see a few examples of the server side, or a schematic discussion on how to integrate new hardware. This would give a more practically grounded introduction to the actor model and help the reader more easily understand how to leverage and modify the LabNet open-source code for their specific purposes.

Unfortunately, this would have become very technical. Readers would need to know C++ and treating the topic comprehensively would need about 5-10 more pages. In the case of actors, this would also just be a repetition of the many books written about this. In the case of the extensibility of LabNet, I would only describe the current status, which may already be different in the next version. In any case, that will be the case as soon as the plug-in system has been implemented. We fully agree that this information should be available. However, our decision has been to place this information in the online documentation. This is the main reason that we have remained more general in the methods section.

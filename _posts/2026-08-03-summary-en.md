---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
lang: en
---

> From 29 items, 20 important content pieces were selected

---

1. [Qwen Releases 3.8-Max: 2.4T-Parameter Open-Weight Model](#item-1) ⭐️ 9.0/10
2. [Karpathy's AI-Generated 3D Pelican Sparks Physical Understanding Debate](#item-2) ⭐️ 8.0/10
3. [Open Letters on AI Development: Microsoft, Anthropic, and Frontier Employees Weigh In](#item-3) ⭐️ 8.0/10
4. [Kakehashi: Experimental Userspace Runs macOS Binaries on Linux ARM](#item-4) ⭐️ 7.0/10
5. [F*: A General-Purpose Proof-Oriented Programming Language](#item-5) ⭐️ 7.0/10
6. [LLM Context Degradation: What Papers Show and Practical Habits](#item-6) ⭐️ 7.0/10
7. [How Essential English Vocabulary Lists Have Changed, 1953–2023](#item-7) ⭐️ 6.0/10
8. [Twin: Open-Source Project Reimagines AI Context as Reusable Understanding](#item-8) ⭐️ 6.0/10
9. [Apple Limits Vulnerability Report Submissions to Curb AI-Generated Spam](#item-9) ⭐️ 6.0/10
10. [Chinese Police AI Detects Bitcoin Money Laundering with ~90% Accuracy](#item-10) ⭐️ 6.0/10
11. [WeChat Quake Alert Adds Crowdsourced Shaking and Location Updates](#item-11) ⭐️ 6.0/10
12. [Microplastics Found in 92% of Animals Near Deep-Sea Hydrothermal Vents](#item-12) ⭐️ 6.0/10
13. [Rumor: AMD Zen 6 Per-Core Optimizations Aim to Fix Gaming Micro-Stutters](#item-13) ⭐️ 6.0/10
14. [U.S. States Move to Repeal Data Center Tax Breaks, Raising AI Infrastructure Costs](#item-14) ⭐️ 6.0/10
15. [RISC OS Open Marks 20 Years of Community Development](#item-15) ⭐️ 5.0/10
16. [condense-json 1.0 Released: Trimming Redundant JSON Strings](#item-16) ⭐️ 5.0/10
17. [Shenzhen Adds E-Bike Traffic Violations to Personal Credit Records](#item-17) ⭐️ 5.0/10
18. [JD Delivery launches AI smart helmet with voice assistant for riders](#item-18) ⭐️ 5.0/10
19. [Karpathy stars sqliteai/waste for stream-running 2.78T Kimi K3 from NVMe](#item-19) ⭐️ 4.0/10
20. [July 2026 Newsletter Recaps New AI Model Releases and MCP](#item-20) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [Qwen Releases 3.8-Max: 2.4T-Parameter Open-Weight Model](https://qwen.ai/blog?id=qwen3.8) ⭐️ 9.0/10

Qwen released Qwen 3.8-Max, its largest and strongest model to date, with 2.4 trillion total parameters and 95 billion active parameters. The model is now available via QwenCloud's API, and its weights will be open-sourced next week, marking the first time Qwen has open-sourced a Max-level model. This is a major milestone because it brings a frontier-scale model with 2.4 trillion parameters into the open-weight ecosystem, enabling researchers and enterprises to self-host a model comparable to top proprietary offerings. By open-sourcing a Max-level model, Qwen is dramatically lowering the barrier for high-end AI experimentation and deployment across the industry. Qwen 3.8-Max is built on the Qwen 3.5 architecture and shows improvements in coding, work, research, and long-horizon tasks. In an internal coding test, the model autonomously ran for more than 10 days to complete a project and improve itself, and within 24 hours it beat 458 out of 526 teams in the WWW2025 multimodal dialogue intent recognition competition.

telegram · zaihuapd · Aug 3, 02:31

**Background**: Qwen 3.8-Max likely uses a Mixture-of-Experts (MoE) architecture, where total parameters include all experts but only a subset are activated per token, which explains the large gap between its 2.4T total and 95B active parameters. Open-weight models publish the trained weights so users can download, inspect, and run them anywhere, though this does not necessarily include training data or unrestricted licenses. Understanding the difference between total and active parameters is crucial when evaluating model scale and inference cost.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical...</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weights-models-why-infra-people-need-understand-suellen-ferreira-qeehf">Open Weights Models : why Infra people need to understand this</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters : What’s the Difference?</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Qwen`, `#Open Source`, `#Model Release`

---

<a id="item-2"></a>
## [Karpathy's AI-Generated 3D Pelican Sparks Physical Understanding Debate](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

Andrej Karpathy shared an AI-generated 3D pelican animation on X, created from a text prompt, which quickly became a talking point about whether generative models demonstrate physical-world understanding. The post attracted strong community discussion about the significance of such demos as benchmarks. This matters because 3D animation generation is emerging as a qualitative benchmark for evaluating whether AI models understand physical reality, beyond just generating static images. The debate could influence how researchers and developers assess frontier models and what progress they expect in physical reasoning. Commenters noted that the exact prompt was not shared, making the demo non-reproducible, and one commenter argued that LLM-generated three.js code may reflect training on three.js rather than genuine physical understanding. Others pointed to simpler benchmark tasks like 'create a pinball game' that still trip up frontier models.

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: The pelican demo belongs to a growing line of work in which large language models generate 3D scenes and animations from natural-language prompts, often using JavaScript libraries such as three.js. Evaluating whether these outputs reflect genuine physical understanding has become an active research area, with new benchmarks such as PAI-Bench and PhysicalRealismBench designed to test physical AI generation and video-world-model realism. Research projects such as SayMotion and LLM_animation similarly explore text-to-3D animation, but the question of whether such demos prove world-modeling ability remains contested.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/datasets/shi-labs/physical-ai-bench-understanding">shi-labs/ physical - ai - bench - understanding · Datasets at Hugging Face</a></li>
<li><a href="https://reka.ai/old-reka-pages/unused-labs-pages/rekalabs/blogs/physicalrealismbench-attributable-physical-realism-evaluation-for-video-world-models">PhysicalRealismBench: Attributable Physical Realism Evaluation for...</a></li>
<li><a href="https://github.com/Whalefishin/LLM_animation">GitHub - Whalefishin/LLM_animation: A showroom for various animations generated by large language models (LLM). Our method takes a rigged 3D model and produces novel animations specified via natural language descriptions in a matter of seconds. · GitHub</a></li>

</ul>
</details>

**Discussion**: Discussion was lively and divided. Some commenters defended the demo, arguing that even imperfect outputs are useful as qualitative benchmarks for physical understanding, while others were skeptical, suggesting the model may simply be good at writing three.js code rather than understanding physics. Several people also noted that the prompt was not shared, making the result hard to reproduce, and pointed to simpler tests like pinball games that frontier models still fail.

**Tags**: `#AI`, `#3D animation`, `#LLM`, `#three.js`, `#generative models`

---

<a id="item-3"></a>
## [Open Letters on AI Development: Microsoft, Anthropic, and Frontier Employees Weigh In](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 8.0/10

In late July 2026, Microsoft shepherded an open letter signed by 235 AI-adjacent companies, including NVIDIA, Amazon, and OpenAI, urging the US government to avoid restricting open-weight AI models. Anthropic declined to sign and released its own cautionary position, followed by a 'Pacing the Frontier' letter signed by 1,324 frontier AI employees. This series of open letters reflects a pivotal policy debate over regulating open-weight AI models, with major industry players split on safety risks versus innovation and competition. The outcome could shape US AI policy, international AI development, and the future openness of advanced models. The July 24 Microsoft-backed letter explicitly defends distillation as a legitimate model-development technique, a position Anthropic opposes. The July 28 'Pacing the Frontier' letter, signed by OpenAI chief scientist Jakub Pachocki and others, calls for international governance tools to deliberately pace automated AI development.

rss · Simon Willison · Aug 2, 04:16

**Background**: Open-weight models are AI systems whose trained parameters (weights) are publicly released, allowing others to run, fine-tune, and study them without access to the full dataset, code, or training process. This differs from fully open-source AI, which also includes training data, source code, and documentation. The debate is heightened by US-China AI competition, as Chinese models like Moonshot AI's Kimi are often cited as evidence that restrictions could hurt American competitiveness without stopping overseas development. Distillation, in this context, is training a model using outputs from another model, a common but sometimes controversial technique.

<details><summary>References</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights : not quite what you’ve been told – Open Source Initiative</a></li>
<li><a href="https://infercom.ai/blog/open-weight-models-explained/">Open - Weight AI Models : Why They're a Strategic Advantage | Infercom</a></li>
<li><a href="https://www.linkedin.com/pulse/kimi-ai-redefining-future-artificial-intelligence-sandeep-mahindra-xq0zf">Kimi AI : Redefining the Future of Artificial Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open weights`, `#open source`, `#regulation`, `#industry`

---

<a id="item-4"></a>
## [Kakehashi: Experimental Userspace Runs macOS Binaries on Linux ARM](https://github.com/wie-project/kakehashi) ⭐️ 7.0/10

The Hacker News post introduces Kakehashi, an experimental userspace translation layer that loads Darwin Mach-O binaries and runs macOS command-line tools natively on Linux ARM64. Working prototypes include 7-Zip, curl, and the Xcode-tools Git, with automated tests passing a substantial command set. Kakehashi tackles a difficult compatibility problem—running macOS binaries outside Apple's ecosystem—opening the door to running Mac command-line tools on Linux ARM hardware such as Apple Silicon and ARM servers. If matured, it could complement efforts like Darling and, long-term, follow the Wine/Proton path for macOS applications. The project is CLI-first and has no JIT yet; it loads Darwin Mach-O executables on Linux aarch64, maps a freestanding libSystem, and translates BSD syscalls to Linux equivalents. Early performance is limited—7-Zip is about 5.2x slower than native Linux—but the author has a stated optimization plan, and curl already passes more than 200 commands/options in Docker tests.

hackernews · vlad_kalinkin · Aug 2, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49145937)

**Background**: macOS applications are compiled to Mach-O binaries and rely on Darwin's libSystem and BSD syscalls, whereas Linux uses ELF binaries and Linux syscalls, making direct execution impossible. A userspace translation layer like Kakehashi bridges this gap without kernel modules, similar in spirit to Wine for Windows binaries; Darling is a broader project with a similar goal, and Asahi Linux has made Linux on Apple Silicon viable, increasing interest in such compatibility tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux - Wikipedia</a></li>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation layer for Linux ARM64 · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=49145937">Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters are generally interested and encouraging but note the project is early-stage; one recommends coordinating with the Darling project and points to its open ARM64 support PR. Others jokingly criticize the name 'Kakehashi' and ask whether the approach could instead require original binaries as inputs, like ROM-based decompilation projects. Overall sentiment is cautiously optimistic.

**Tags**: `#macOS`, `#Linux`, `#ARM`, `#binary compatibility`, `#userspace`

---

<a id="item-5"></a>
## [F*: A General-Purpose Proof-Oriented Programming Language](https://fstar-lang.org/) ⭐️ 7.0/10

The F* programming language homepage presents it as a general-purpose proof-oriented language, and a Reddit post about it drew 167 points and 74 comments. The discussion highlighted both enthusiasm for formal verification and criticism that the homepage lacks immediate syntax examples. F* is a mature formal-verification language that lets developers write programs together with machine-checked proofs. The engaged discussion indicates growing interest in proof-oriented languages and formal verification beyond academia. F* supports dependent types, monadic effects, and refinement types, and can extract code to OCaml, F#, C, WebAssembly, and assembly via tools like KaRaMeL and Vale. Some commenters noted the official homepage lacks code examples, which they considered a barrier for newcomers.

hackernews · ducktective · Aug 2, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49143925)

**Background**: F* (pronounced 'F star') is a joint project of Microsoft Research and Inria, first introduced in 2011. It uses a type system with dependent types and refinement types, and relies on SMT solving plus manual proofs to verify that programs meet their specifications. F* is often used for verifying cryptographic implementations and security-sensitive software.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language)</a></li>
<li><a href="https://github.com/FStarLang/FStar">GitHub - FStarLang/FStar: A Proof-oriented Programming Language · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters generally showed interest but criticized the homepage for not showing syntax examples upfront. One developer praised F* for supporting incremental migration of existing C codebases, while another asked whether it is used in industry and for which software; a Haskell fan found it useful for functional programming beginners. A few quips about side effects and stylesheets were also present.

**Tags**: `#formal verification`, `#programming language`, `#proof assistant`, `#functional programming`

---

<a id="item-6"></a>
## [LLM Context Degradation: What Papers Show and Practical Habits](https://www.reddit.com/r/MachineLearning/comments/1vdsgcj/context_degradation_in_llms_what_the_papers/) ⭐️ 7.0/10

This r/MachineLearning post synthesizes recent research on LLM context degradation and lays out personal habits the author developed for long analysis sessions. It argues that context quality—not just token limits—degrades during extended conversations, affecting output coherence. Context degradation is an under-discussed practical bottleneck that affects anyone doing long, multi-turn work with LLMs, from coding to research. Surfacing both the academic evidence and mitigation habits helps practitioners design more robust workflows and set realistic expectations. The post is grounded in papers such as arXiv:2512.20662, which quantifies laziness, decoding suboptimality, and context degradation in LLMs. Practical habits likely include summarizing/compacting prior context, externalizing state to files or notes, and monitoring context fill levels — approaches echoed in context-window management guides.

reddit · r/MachineLearning · /u/usernamehere93 · Aug 2, 20:20

**Background**: Context degradation refers to the gradual breakdown in coherence and utility that occurs during long-running conversations with large language models, sometimes called Context Degradation Syndrome. It affects any AI system with a finite context window, and even very large windows (e.g., 2M tokens) do not eliminate it because models do not attend equally to all information. Researchers and practitioners recommend strategies such as token trimming, summarization, server-side compaction, and using external artifacts to keep long sessions productive.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2512.20662">Quantifying Laziness, Decoding Suboptimality, and Context ...</a></li>
<li><a href="https://jameshoward.us/2024/11/26/context-degradation-syndrome-when-large-language-models-lose-the-plot">Context Degradation Syndrome: When Large Language Models ...</a></li>
<li><a href="https://logicity.in/en/blog/why-your-llm-s-2m-token-context-window-is-mostly-useless">Why Your LLM 's 2M Token Context Window Is Mostly Useless | Logicity</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#context-window`, `#machine-learning`, `#practical-usage`, `#analysis`

---

<a id="item-7"></a>
## [How Essential English Vocabulary Lists Have Changed, 1953–2023](https://pudding.cool/2026/07/essential-words/) ⭐️ 6.0/10

The Pudding analyzed how the essential vocabulary recommended for English language learners changed between 1953 and 2023. Nearly a quarter of the old list's words were dropped, while 39% of the current words are new. Vocabulary lists shape what millions of English learners study, so this shift affects teaching materials and classroom priorities. The word changes also reveal broader cultural movement from personal virtues like loyalty and politeness toward abstract identity and community concepts. The 'Social-Communicative' category stayed roughly the same size, but about a quarter of its 1953 words disappeared. Everyday items such as apple, fork, soap, umbrella and leaf were removed, while words like community, identity, ethnic, gender and narrative took their place.

hackernews · c-oreills · Aug 2, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49145590)

**Background**: The 1953 list is the General Service List (GSL), compiled by Michael West and containing roughly 2,000 high-frequency words selected by frequency from written English. Modern lists, such as the New General Service List (NGSL), are built from much larger corpora — one version uses a 273-million-word subsection — and claim better coverage of contemporary English. The article uses this contrast to show how language teaching has moved from concrete everyday objects to more abstract social vocabulary.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_Service_List">General Service List - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/New_General_Service_List">New General Service List - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were divided. Some questioned the analysis, noting that a word like 'fork' is still essential for everyday learners, while others saw the shift as meaningful evidence of societal change. One commenter also stressed that any 'essential' list depends heavily on learners' goals, such as travel, TV, or reading newspapers.

**Tags**: `#linguistics`, `#data-analysis`, `#education`, `#vocabulary`

---

<a id="item-8"></a>
## [Twin: Open-Source Project Reimagines AI Context as Reusable Understanding](https://www.reddit.com/r/MachineLearning/comments/1vdz02j/twin_a_possible_solution_to_ai_context_rebuilding/) ⭐️ 6.0/10

A Reddit post introduces Twin, an open-source research project that continuously observes distributed events such as GitHub activity and Slack conversations to form reusable situation models. A demonstration with Claude Sonnet 4.6 showed a fresh conversation correctly understanding project state using only Twin's MCP server, without custom memory or project-specific prompts. This approach targets a major pain point in LLM usage: repeatedly reconstructing the same context in every new conversation, which costs time and money. If viable, it could shift AI memory from retrieval and reconstruction toward continuous cognitive continuity, affecting how AI assistants, agents, and developer tools are built. Twin works at a layer distinct from retrieval or memory optimization, pre-synthesizing understanding through event correlation and reflection rather than merely storing or retrieving information. The demonstration used Claude Sonnet 4.6, an MCP server, and automatic context injection; the project is open source at github.com/caribeedu/twin, with a video demo linked in the post.

reddit · r/MachineLearning · /u/VicentVanCock · Aug 3, 01:00

**Background**: LLM conversations typically rely on prompts that gather relevant documents, chat logs, and code snippets, forcing the model to reconstruct context that may have already been understood in earlier sessions. Context engineering is an emerging discipline focused on how to shape and maintain context for AI agents, with techniques ranging from tool design to memory systems. Several open-source projects are exploring similar memory-reuse ideas, such as TencentDB Agent Memory, which aims to help agents learn workflows and reuse past experience. The MCP (Model Context Protocol) is an open standard that lets models access external data and tools, and Twin uses it for automatic context injection.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>
<li><a href="https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus">Context Engineering for AI Agents: Lessons from Building Manus</a></li>
<li><a href="https://github.com/CoeusInstitute/tencentdb-agent-memory">GitHub - CoeusInstitute/tencentdb-agent- memory : TencentDB Agent...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#context`, `#memory`, `#open-source`

---

<a id="item-9"></a>
## [Apple Limits Vulnerability Report Submissions to Curb AI-Generated Spam](https://www.ft.com/content/4532122d-90f2-4433-9df6-ca99d8a141d2?syn-25a6b1a6=1) ⭐️ 6.0/10

Apple has acknowledged that since June it has limited how many vulnerability reports researchers can submit at once, with a 30-day cooldown period, in response to a flood of low-quality AI-generated security reports. The Italian startup Bynario said it used ChatGPT to discover more than 50 vulnerabilities in the latest macOS within three weeks, including a privilege escalation chain that could allow full control of a computer, but was unable to report them all due to the cap. This situation illustrates the growing conflict between AI-accelerated security research and platform submission policies. If limits discourage legitimate AI-assisted researchers, important vulnerabilities may go unreported; at the same time, unfiltered AI-generated reports can bury security teams in false positives. Apple said it has contacted Bynario and reviewed its submissions. Apple is also using AI defensively: this week's system security update fixed roughly five times the usual number of issues, with credit given to Anthropic's and OpenAI's tools.

telegram · zaihuapd · Aug 2, 05:50

**Background**: Vulnerability reports are how security researchers alert companies to flaws in software, often through bug bounty programs that reward valid findings. The rise of generative AI has led to a flood of plausible-looking but frequently false or low-quality submissions, which security teams call 'AI slop'. Privilege escalation is a class of attack in which a user or process gains higher access rights than intended, often a key step in a chain of exploits that can lead to full system compromise.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/ai-polluting-bug-bounty-platforms/">AI Polluting Bug Bounty Platforms with Fake Vulnerability Reports</a></li>
<li><a href="https://www.beyondtrust.com/blog/entry/privilege-escalation-attack-defense-explained">What Is Privilege Escalation? Attacks & Defense Guide | BeyondTrust</a></li>
<li><a href="https://wellfound.com/company/bynario">Bynario Careers - Insights and Opportunities - Wellfound</a></li>

</ul>
</details>

**Tags**: `#ai`, `#security`, `#apple`, `#vulnerability reporting`, `#chatgpt`

---

<a id="item-10"></a>
## [Chinese Police AI Detects Bitcoin Money Laundering with ~90% Accuracy](https://www.scmp.com/news/china/science/article/3362493/chinese-police-ai-algorithm-tracks-bitcoin-money-laundering-90-accuracy) ⭐️ 6.0/10

Researchers from People's Public Security University of China published a peer-reviewed study in the May issue of the journal Intelligence Journal describing an AI framework that combines memory modules with large language models to detect illegal cryptocurrency transactions with nearly 90% accuracy. This matters because it shows a practical, explainable use of large language models for financial forensics, giving regulators a new tool against cryptocurrency money laundering. China's Supreme People's Procuratorate reported that prosecutors indicted 3,259 suspects in 2025 for laundering money through virtual currencies and underground banks. The framework combines memory-augmented neural networks, which use an external memory bank to store and recall information, with large language models, enabling it to trace anonymous and cross-border Bitcoin transactions. The researchers emphasize that the approach is interpretable and generalizable for law enforcement applications.

telegram · zaihuapd · Aug 2, 08:22

**Background**: Memory-augmented neural networks (MANNs) are architectures that give a neural network an external memory module it can read from and write to, going beyond a fixed context window. In parallel, researchers have begun applying large language models to blockchain security; for example, Berkeley's BlockGPT trains an LLM from scratch to detect anomalous blockchain transactions in real time. AI-based anti-money-laundering systems have long faced pressure to be not only accurate but also explainable, since regulators need to justify why a transaction is flagged.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/memory-augmented-neural-networks">Memory - Augmented Neural Networks</a></li>
<li><a href="https://rdi.berkeley.edu/blockchain-llm/">Blockchain Large Language Models | Berkeley RDI</a></li>
<li><a href="https://asenion.ai/blog/algorithmic-fairness-and-explainability-assessment-of-anti-money-laundering-detection-ai-models-using-fairly-ais-compliance-in-a-box-simple-start-plan">Algorithmic Fairness and Explainability Assessment of Anti- Money ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cryptocurrency`, `#money laundering`, `#LLM`, `#forensics`

---

<a id="item-11"></a>
## [WeChat Quake Alert Adds Crowdsourced Shaking and Location Updates](https://news.cctv.com/2026/08/02/ARTIrixWuCmLM2TuZigvQ8rX260802.shtml) ⭐️ 6.0/10

On August 2, 2026, the China Earthquake Networks Center, National Emergency Broadcasting, and Tencent launched two new WeChat earthquake early warning features: 'Shaking Aggregation' for user-reported shaking intensity and 'Location Update' for refreshing alert subscription areas. The mini-program has already issued over 700 alerts with more than 60 million subscribers since August 2024. This makes earthquake early warning more participatory and precise, using crowdsourced intensity feedback to supplement instrument data and location-aware push to target travelers. With a cumulative user base of over 400 million across WeChat and phone vendors, the feature can improve public safety response on a massive scale. The 'Shaking Aggregation' feature processes user reports after an earthquake into a shaking intensity distribution map, while 'Location Update' prompts users to refresh their subscription location when they move. Huawei, Xiaomi, vivo, and others have embedded early warning capabilities into their operating systems, forming a broader public service network alongside the WeChat mini-program.

telegram · zaihuapd · Aug 2, 10:16

**Background**: Earthquake early warning systems detect initial seismic waves and issue alerts before strong shaking arrives, typically relying on dense sensor networks. Crowdsourcing is a complementary approach: platforms such as USGS 'Did You Feel It?' and UC Berkeley's MyShake use online reports or smartphone accelerometers to measure shaking intensity and detect quakes. WeChat's new features apply this crowdsourcing model inside a widely used social app, while the location-update feature ensures alerts match the user's current activity area.

<details><summary>References</summary>
<ul>
<li><a href="https://news.engin.umich.edu/2026/01/did-you-feel-it-expanding-use-of-an-earthquake-crowdsourcing-tool/">Did You Feel It? Expanding use of an earthquake crowdsourcing tool</a></li>
<li><a href="https://news.berkeley.edu/2016/02/12/new-app-turns-smartphones-into-worldwide-seismic-network/">New app turns smartphones into worldwide seismic ... - Berkeley News</a></li>
<li><a href="https://www.citizenscience.gov/assets/files/did-you-feel-it.pdf">Did You Feel It?: Crowdsourcing Earthquake Maps</a></li>

</ul>
</details>

**Tags**: `#earthquake early warning`, `#WeChat`, `#public safety`, `#crowdsourcing`, `#location services`

---

<a id="item-12"></a>
## [Microplastics Found in 92% of Animals Near Deep-Sea Hydrothermal Vents](https://www.yahoo.com/news/science/articles/most-isolated-environments-microplastics-finding-020000452.html) ⭐️ 6.0/10

A Korean research team found microplastics in 11 of 12 snails and mussels collected near deep-sea hydrothermal vents at about 2,000 meters depth in the Southwest Pacific and Indian Oceans, a 92% detection rate. The study was published in Water Research. This shows that even one of Earth's most isolated ecosystems has been contaminated by plastic pollution, underscoring that microplastics are pervasive and difficult to remove. The findings support the argument that cutting plastic waste at the source is essential, informing deep-sea monitoring and conservation policies. The team examined four species, mainly detecting polystyrene, with an average of 3.42 particles per animal. Filter-feeding mussels showed uniform distribution of microplastics, while herbivorous snails had them concentrated in digestive organs, and concentrations were higher in Indian Ocean samples than the Pacific.

telegram · zaihuapd · Aug 2, 11:00

**Background**: Hydrothermal vents are deep-sea hot springs that support unique ecosystems based on chemosynthesis rather than sunlight, located around volcanically active seafloor areas. Microplastics are tiny plastic particles less than 5 millimeters in size that have spread throughout the ocean, and their presence in deep-sea organisms highlights how far-reaching plastic pollution has become.

**Tags**: `#microplastics`, `#deep-sea`, `#environmental science`, `#marine biology`, `#pollution`

---

<a id="item-13"></a>
## [Rumor: AMD Zen 6 Per-Core Optimizations Aim to Fix Gaming Micro-Stutters](https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets) ⭐️ 6.0/10

According to a new rumor, AMD's next-generation Zen 6 processors will introduce several per-core optimizations, including enhanced CPPC Performance Priority, FloorPerf, and HighestFreq. These features are designed to reduce game micro-stutters and improve 1% low frame rates by managing power and thermal budgets more intelligently. If real, these optimizations address a major source of gaming frustration: stutters that don't show up in average FPS but hurt perceived smoothness. They could give AMD processors a more consistent gaming experience and set a new focus on OS-level CPU scheduling rather than raw core-count or clock-speed gains. The reported features include CPPC Performance Priority to favor foreground tasks, FloorPerf to downclock background cores before the game cores, and HighestFreq to let the OS see true per-core boost frequencies. Zen 6 is also said to support per-core EPP boost, PQOS, and a new IBS memory analyzer to limit background memory and L3 cache usage; AMD has not officially confirmed any of this.

telegram · zaihuapd · Aug 2, 14:05

**Background**: Micro-stutters are short frame-time hitches that make games feel uneven, and they are often captured by 1% low or p99 frame-time metrics rather than average FPS. AMD's CPPC (Collaborative Power and Performance Control) is an existing mechanism that tells the OS which cores can boost highest, but matching those hints to real-time power/thermal state has been imperfect. The rumored Zen 6 changes would tighten this coordination at the per-core level; tests of a FloorPerf-like concept on a Steam Deck reportedly improved 1% lows by 31.8%.

<details><summary>References</summary>
<ul>
<li><a href="https://hwbusters.com/news/amd-zen-6-gets-cppc-performance-priority-per-core-floors-aimed-at-1-lows/">AMD Zen 6 Gets CPPC Performance Priority — Per-Core Floors ...</a></li>
<li><a href="https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets">AMD's upcoming Zen 6 processors could fix microstutters and improve 1% lows in games — Next-gen CPUs tipped to feature per-core optimizations for thermal and power budgets</a></li>
<li><a href="https://wccftech.com/amd-new-cppc-highestfreq-ends-os-frequency-guesswork-letting-os-see-true-ryzen-boost-clocks/">AMD's New CPPC HighestFreq Ends OS Frequency Guesswork, Letting Windows And Linux See True Ryzen Boost Clocks - Wccftech</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Zen 6`, `#CPU`, `#gaming performance`, `#hardware rumors`

---

<a id="item-14"></a>
## [U.S. States Move to Repeal Data Center Tax Breaks, Raising AI Infrastructure Costs](https://theinformation.com/articles/exclusive-data-center-costs-set-rise-u-s-states-move-repeal-tax-breaks) ⭐️ 6.0/10

Several U.S. states are reportedly considering repealing or tightening tax incentives for large data centers, responding to rising electricity demand and fiscal pressure. The shift could raise data center construction and operating costs. The tax policy change could significantly raise the cost of AI infrastructure in the U.S., affecting hyperscale cloud providers and AI startups. It may also reshape where future data centers are built, as states compete to attract investment while managing public budgets. Historically, many states exempted server equipment, electricity, and other costs from sales and property taxes to lure data center investment. Now, as AI drives computing demand, governments are pressuring companies to bear more of the costs of grid upgrades and local infrastructure.

telegram · zaihuapd · Aug 3, 00:42

**Background**: Data centers are facilities that house servers and computing equipment, and their rapid expansion has been a core part of the AI boom. To attract these large projects, U.S. states have long offered tax incentives, but the explosive growth in electricity consumption and the need for new power infrastructure have made those incentives increasingly controversial. This creates a policy tension between economic development and the fiscal and environmental costs of data centers.

**Tags**: `#AI infrastructure`, `#data centers`, `#tax policy`, `#cloud computing`

---

<a id="item-15"></a>
## [RISC OS Open Marks 20 Years of Community Development](https://www.riscosopen.org/news/articles/2026/06/20/twenty-years-of-risc-os-open) ⭐️ 5.0/10

RISC OS Open, the community-led initiative that preserves and develops the RISC OS operating system, is celebrating its twentieth anniversary in June 2026. The milestone marks two decades since the project launched in 2004 to keep the platform alive as open-source software. This anniversary underscores the persistence of a niche retrocomputing community that has kept RISC OS alive long after Acorn Computers ceased operations. The project's work also provides a lightweight, fast-booting operating system option for modern ARM hardware such as the Raspberry Pi, preserving a unique piece of computing history for new generations. RISC OS was originally designed by Acorn Computers in 1987 for its ARM-based Archimedes computers. RISC OS Open was launched in 2004, and version 5.0 of the operating system was finally released as open source in 2018, with development managed by the volunteer-run RISC OS Open Limited.

hackernews · AlexeyBrin · Aug 2, 12:36 · [Discussion](https://news.ycombinator.com/item?id=49143967)

**Background**: RISC OS is a modular operating system that takes its name from the reduced instruction set computer (RISC) architecture it supports, and it features a graphical user interface and windowing system. After Acorn's breakup, development forked among several companies, including RISCOS Ltd and Castle Technology, while the RISC OS Open initiative emerged to preserve and continue the platform. Today, RISC OS runs on a variety of ARM-based hardware, including older Acorn machines and the Raspberry Pi series, with the exception of the Raspberry Pi 5.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS">RISC OS - Wikipedia</a></li>
<li><a href="https://www.riscosopen.org/content/">RISC OS Open : Welcome</a></li>
<li><a href="https://dreamridiculous.com/productivity/the-tech-operations-timeline-20-years-with-risc-os-open/">The Tech Operations Timeline: 20 Years With RISC OS Open</a></li>

</ul>
</details>

**Discussion**: Commenters shared nostalgic memories, with one developer noting that RISC OS was where they cut their teeth as an open-source developer, writing an ARM-assembler application called !Director. Others praised the OS's fast boot speed on the Raspberry Pi, highlighted Sibelius as a famous surviving RISC OS application, and pointed newcomers to the RISC OS Programmer's Reference Manual for learning to program on the platform. Overall sentiment was warm and appreciative of the project's longevity.

**Tags**: `#RISC OS`, `#retrocomputing`, `#open source`, `#ARM`, `#operating systems`

---

<a id="item-16"></a>
## [condense-json 1.0 Released: Trimming Redundant JSON Strings](https://simonwillison.net/2026/Aug/2/condense-json/#atom-everything) ⭐️ 5.0/10

Simon Willison announced the 1.0 release of condense-json, a Python library that condenses JSON by replacing repeated strings with placeholder references. The release includes non-disruptive fixes after a year and a half of development. This library helps reduce storage and token usage when working with large JSON documents, particularly in LLM-related workflows where duplicated data can bloat logs. It demonstrates a practical approach to optimizing data representation for AI applications. The condense_json function scans for strings or substrings in a replacements dictionary and outputs a special syntax using {"$r": ...} and {"$": ...} markers. The uncondense_json function reverses the process, and Simon uses it to save space in SQLite logs generated by the LLM tool.

rss · Simon Willison · Aug 2, 22:19

**Background**: JSON is a common data format, but large documents often contain duplicated strings that waste space. condense-json replaces those repeated values with compact references, and can restore them later. This is especially useful for LLM applications that generate large structured logs, where reducing storage can lower costs and speed up processing.

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/project/condense-json/">Python function for condensing JSON using replacement strings</a></li>

</ul>
</details>

**Tags**: `#JSON`, `#Python`, `#LLM`, `#libraries`, `#release`

---

<a id="item-17"></a>
## [Shenzhen Adds E-Bike Traffic Violations to Personal Credit Records](https://news.qq.com/rain/a/20260801A0BXUV00) ⭐️ 5.0/10

Shenzhen has formally begun reporting electric bicycle traffic violations to personal credit agencies, and Bao'an district has already logged 50 riders. The move follows the Shenzhen Special Economic Zone Road Traffic Safety Violations Punishment Regulations and kicked off with the "Thunder Shield" special enforcement action in July 2026. This marks one of the first concrete uses of personal credit scoring for non-motorized traffic enforcement in a major Chinese city. It could affect loan eligibility and social standing for e-bike riders, and set a precedent for other cities integrating traffic fines with credit data. Under the rules, riders face credit reporting if they are fined five or more times in a year, or have three or more unresolved violations within a year. The campaign targets six violation types, including running red lights (300 yuan fine) and riding in motor vehicle lanes or on sidewalks (50 yuan fine).

telegram · zaihuapd · Aug 2, 09:02

**Background**: China's personal credit system, operated by the central bank, compiles financial and behavioral data that banks and lenders use to evaluate loan applications. Shenzhen's local traffic regulations allow traffic violations to be treated as credit-relevant behavioral records, and the city has been expanding automated enforcement through electronic monitoring and online processing via the "Shenzhen Traffic Police" WeChat account. Bao'an district serves as a pilot area for online handling of camera-captured violations.

<details><summary>References</summary>
<ul>
<li><a href="http://m.jianbiaoku.com/webarbs/book/172148/4863356.shtml">深 圳 经 济 特 区 道 路 交 通 安 全 违 法 行 为 处 罚 条 例 2024年修订 建标库</a></li>
<li><a href="https://www.maigoo.com/goomai/197935.html">如何查询 个 人 征 信 记录 人 民银行 征 信 中心网上查询方法 榜中榜知识</a></li>
<li><a href="https://www.163.com/dy/article/K0KQ19N005564S43.html">整治电鸡还得看 深 圳 ！闯红灯直接来张300元，一天多工资就不见了</a></li>

</ul>
</details>

**Tags**: `#policy`, `#credit system`, `#traffic enforcement`, `#data privacy`, `#China`

---

<a id="item-18"></a>
## [JD Delivery launches AI smart helmet with voice assistant for riders](https://www.ctdsb.net/s114_202608/1571814.html) ⭐️ 5.0/10

On August 3, JD Delivery announced an AI-powered smart helmet that integrates an AI voice assistant, route guidance from top riders, one-touch emergency help, and merchant environment verification. The first batch will be given free to full-time JD riders, with wider rollout planned later. This is a practical application of AI in the logistics industry that could improve delivery efficiency and rider safety. It reflects a broader trend of platforms using AI and hardware to upgrade last-mile delivery services and food safety oversight. The 'single-king navigation' feature converts veteran riders' delivery experience into real-time voice guidance, with internal tests showing about 3 minutes saved per order. The helmet supports full voice control, automatically parses order remarks, reminds before delivery, and assists in verifying merchant environment during pickup.

telegram · zaihuapd · Aug 3, 03:22

**Background**: Smart helmets are a growing category in logistics tech, aiming to free riders' hands and reduce phone distraction while riding. Food safety concerns such as 'ghost restaurants' have pushed delivery platforms to add merchant environment verification as part of their quality-control systems.

<details><summary>References</summary>
<ul>
<li><a href="https://app.myzaker.com/news/article.php?pk=6a2a19d4b15ec049845239e2">app.myzaker.com/news/article.php?pk=6a2a19d4b15ec049845239e2</a></li>
<li><a href="https://news.qq.com/rain/a/20260609A06R8J00">news.qq.com/rain/a/20260609A06R8J00</a></li>
<li><a href="https://news.bjd.com.cn/2026/02/26/11602708.shtml">防“幽灵 外 卖 ”， 外 卖 平台应“实地 核 查”登记店铺_京报网</a></li>

</ul>
</details>

**Tags**: `#AI`, `#smart helmet`, `#delivery`, `#logistics`, `#JD`

---

<a id="item-19"></a>
## [Karpathy stars sqliteai/waste for stream-running 2.78T Kimi K3 from NVMe](https://github.com/sqliteai/waste) ⭐️ 4.0/10

Andrej Karpathy starred the GitHub repository sqliteai/waste. The project runs the full 2.78-trillion-parameter Kimi K3 model by streaming activated weights directly from NVMe, avoiding the need to load all weights into RAM. Karpathy's star is a notable signal because he is a highly influential AI researcher, drawing attention to practical methods for running trillion-scale local models. This technique could make extremely large open-weights models usable on mainstream consumer hardware. The Kimi K3 model is 2.78 trillion parameters and does not fit in the RAM of current mainstream consumer systems; it is 1.42 TB as published and 982 GB after conversion. WASTE specifically addresses this by streaming only the activated weights from NVMe storage to memory as needed.

github · karpathy · Aug 2, 17:19

**Background**: Large language models typically require weights to be resident in GPU memory or system RAM during inference, which limits very large models to data-center hardware. WASTE, created by the SQLite AI organization, is a technique purpose-built for Kimi K3: it streams activated weights from NVMe drives, trading storage bandwidth for memory capacity. Andrej Karpathy is a prominent AI researcher known for work at OpenAI and Tesla, and his GitHub stars are often interpreted as endorsements or points of interest.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sqliteai/waste">GitHub - sqliteai / waste : Run the full 2.78-trillion-parameter Kimi...</a></li>
<li><a href="https://huggingface.co/sqliteai/Kimi-K3-WASTE-VQ3">sqliteai /Kimi-K3- WASTE -VQ3 · Hugging Face</a></li>
<li><a href="https://trendshift.io/repositories/96638">sqliteai / waste — GitHub trending stats & insights | Trendshift</a></li>

</ul>
</details>

**Tags**: `#karpathy`, `#github`, `#sqliteai`, `#waste`, `#ai`

---

<a id="item-20"></a>
## [July 2026 Newsletter Recaps New AI Model Releases and MCP](https://simonwillison.net/2026/Aug/2/july-newsletter/#atom-everything) ⭐️ 4.0/10

Simon Willison announced the release of his sponsors-only July 2026 monthly newsletter, covering accidental cyberattacks by OpenAI and Anthropic test models, GPT-5.6 Sol/Terra/Luna, Claude Opus 5, Kimi K3, and DeepSeek-V4-Flash-0731. The newsletter also touches on open letters about AI development, a fireside chat and podcast, and his renewed interest in MCP. As a widely followed AI blogger, Willison's monthly recap serves as a practical roundup of the latest large language model releases and trends, such as Claude Opus 5 and DeepSeek's Flash model, for developers and enthusiasts. The mention of MCP indicates the ongoing relevance of standardized AI-tool integration protocols. The full newsletter is available only to GitHub sponsors, at $10 per month, with a free June edition linked as a preview. The newsletter lists multiple model releases, including GPT-5.6 Sol, Terra, and Luna — three variants — plus Kimi K3 and DeepSeek-V4-Flash-0731.

rss · Simon Willison · Aug 2, 04:12

**Background**: Simon Willison is a well-known developer and long-time blogger who publishes a monthly newsletter summarizing AI research and releases. MCP, or Model Context Protocol, is an open standard introduced by Anthropic in November 2024 that standardizes how AI applications connect to external data sources and tools. DeepSeek-V4-Flash-0731, mentioned in the newsletter, is a sparse mixture-of-experts model with 284B total parameters and 13B active, built for efficient reasoning across a 1M-token context window.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek-ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#newsletter`, `#AI`, `#LLM`, `#model releases`, `#MCP`

---
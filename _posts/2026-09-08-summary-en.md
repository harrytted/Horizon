---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 35 items, 20 important content pieces were selected

---

1. [Factoring a 1990s Certificate Authority's RSA Keys on Consumer GPU](#item-1) ⭐️ 8.0/10
2. [TPU Inference Externalization Accelerates; Up to 50% Perf/$ Lead](#item-2) ⭐️ 8.0/10
3. [Rustuna: High-Performance Rust Implementation of Optuna Released](#item-3) ⭐️ 8.0/10
4. [Huawei unveils Kirin 9050 Pro with LogicFolding architecture after six years](#item-4) ⭐️ 8.0/10
5. [China's Top Court Clarifies AI Liability in New 24-Article Judicial Interpretation](#item-5) ⭐️ 8.0/10
6. [ByteDance Founder Zhang Yiming Oversees Real-Time Spatial Video Model](#item-6) ⭐️ 8.0/10
7. [Jellyfin 12.0 Launches with Performance Gains and Migration Improvements](#item-7) ⭐️ 7.0/10
8. [Interactive Map Traces LA Building Construction from 1880 to 2026](#item-8) ⭐️ 7.0/10
9. [Abusive crawlers consume more CPU on git.kernel.org than all legitimate access](#item-9) ⭐️ 7.0/10
10. [OpenAI Chief Scientist Advocates Aligned AI for Defense, Warns Against Reckless Race](#item-10) ⭐️ 7.0/10
11. [Generating Bad Apple autonomously from a single initial state using a tiny recurrent dynamical system (417k params) (P)](#item-11) ⭐️ 7.0/10
12. [Zero-Downtime Embedding Model Migration Method Released](#item-12) ⭐️ 7.0/10
13. [LLM-guided program evolution improves 10 best-known circle-packing solutions](#item-13) ⭐️ 7.0/10
14. [OpenAI discloses internal AI token costs: median $600, top spenders $7,000 per day](#item-14) ⭐️ 7.0/10
15. [Europe's Top Carriers in Talks for Satellite-to-Phone Alliance to Counter Starlink](#item-15) ⭐️ 7.0/10
16. [Malaysia Eyes Huawei Ascend 910C for Sovereign AI Project, First to Shun US Chips](#item-16) ⭐️ 7.0/10
17. [Caltech Students Launch First Research-Math Hackathon With LLMs](#item-17) ⭐️ 6.0/10
18. [Mercator to Equal Earth: AI-Built D3 Map Transition](#item-18) ⭐️ 6.0/10
19. [KV Cache as an Agent Runtime: A New Path to Interactive LLMs](#item-19) ⭐️ 6.0/10
20. [China's MIIT Plan Calls for Timely 6G Commercial Launch and eSIM Adoption](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Factoring a 1990s Certificate Authority's RSA Keys on Consumer GPU](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

A researcher detailed factoring the 512-bit RSA keys of a certificate authority from the 1990s using only a consumer GPU. The effort took about two days and required no cluster, exposing how weak such historical keys have become. This demonstration shows that 512-bit RSA keys once used by trusted CAs are now trivially breakable by individuals, not just nation-states. It also raises alarm about archived encrypted traffic from the 1990s, which could be retroactively decrypted. The key belonged to a certificate authority from 1999, and the target client was Netscape Communicator 4.51, which required a custom TLS implementation because SSLv3 has been dropped from modern libraries like Go's crypto/tls. The factoring run reportedly took around two days on consumer hardware.

hackernews · ahlCVA · Sep 8, 01:16 · [Discussion](https://news.ycombinator.com/item?id=49604637)

**Background**: RSA is a public-key cryptosystem whose security rests on the practical difficulty of factoring large composite numbers. A certificate authority (CA) issues TLS certificates after verifying a domain owner, and browsers trust the CA's signature. In the 1990s, 512-bit RSA keys were considered normal, but advances in factoring algorithms and cheaper computing power mean they are now breakable in days. This matters because TLS traffic recorded before such keys were deprecated could be decrypted retroactively.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RSA_cryptosystem">RSA cryptosystem - Wikipedia</a></li>
<li><a href="https://eitca.org/cybersecurity/eitc-is-ccf-classical-cryptography-fundamentals/introduction-to-public-key-cryptography/the-rsa-cryptosystem-and-efficient-exponentiation/examination-review-the-rsa-cryptosystem-and-efficient-exponentiation/why-is-the-security-of-the-rsa-cryptosystem-dependent-on-the-difficulty-of-factoring-large-composite-numbers-and-how-does-this-influence-the-recommended-key-sizes/">Why is the security of the RSA cryptosystem dependent on the ...</a></li>
<li><a href="https://elsolitario.org/en/2026/09/07/512-bit-rsa-key-1999-ca-factored-cado-nfs/">512-bit RSA: 1999 Netscape CA Key Factored - elsolitario.org</a></li>

</ul>
</details>

**Discussion**: Commenters have mixed feelings: some call the achievement 'amazing news' for hyper-compatible website work, while others criticize the author for leaving interesting analysis to an LLM. Several also point out the surveillance implication of retroactively decrypting old traffic, and one finds the SSL report's four automatic F's an amusing punchline.

**Tags**: `#RSA`, `#cryptography`, `#TLS`, `#security`, `#history`

---

<a id="item-2"></a>
## [TPU Inference Externalization Accelerates; Up to 50% Perf/$ Lead](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

The latest SemiAnalysis InferenceX report finds Google is rapidly externalizing its TPU inference stack, with TPUv8i-based systems delivering up to 50% more performance per dollar than competing GPU offerings. The report also highlights a growing external customer base and argues that this momentum is eroding NVIDIA's CUDA software moat. Google is using its custom silicon and expanding software tooling to challenge NVIDIA's dominance in AI inference, where CUDA's ecosystem lock-in has long been a barrier. If this TPU externalization sustains such a performance-per-dollar advantage, cloud AI costs could fall and enterprises would gain a credible second source for production inference workloads. InferenceX, formerly named InferenceMAX, benchmarks production-style disaggregated serving with wide expert parallelism, the deployment pattern now used by Frontier AI labs like OpenAI, Anthropic, xAI, Google DeepMind, and DeepSeek, as well as API providers such as TogetherAI and Fireworks. On the hardware side, Google's TPUv8i introduces a new interconnect topology called 'Boardfly', while the earlier Ironwood generation (TPUv7) scales 64-chip 3D Torus cubes to 9,216 chips via optical circuit switches.

rss · Semianalysis · Sep 7, 20:00

**Background**: Google's Tensor Processing Units (TPUs) are custom AI accelerators that compete with NVIDIA GPUs in the cloud machine learning market. Externalization means Google is opening up the entire TPU stack—hardware, serving frameworks, and models—to outside customers instead of using it only internally in products like Gemini. NVIDIA's CUDA software platform is widely considered a moat because its mature libraries and ecosystem lock in millions of developers. Google is countering with open-source tools such as vLLM and JAX/PyTorch support, while also compressing its chip release cadence: TPUv8 arrived roughly a year after Ironwood (TPUv7), compared with multi-year gaps between earlier generations.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs">InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper - Formerly InferenceMAX</a></li>
<li><a href="https://x.com/SemiAnalysis_/status/2089472653350306080">SemiAnalysis on X: "With Ironwood (TPUv7), Google kept the 3D ...</a></li>
<li><a href="https://xpu.pub/2026/05/04/tpuv8/">Google TPUv8: Early Specs and Performance Gains - XPU.pub</a></li>

</ul>
</details>

**Tags**: `#TPU`, `#InferenceX`, `#AI hardware`, `#Google`, `#NVIDIA`

---

<a id="item-3"></a>
## [Rustuna: High-Performance Rust Implementation of Optuna Released](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 8.0/10

Rustuna, a new Rust-based implementation of the Optuna hyperparameter optimization framework, was released on GitHub by the Optuna team. The release promises high-speed and memory-efficient performance while remaining API-compatible with Optuna and free of Python dependencies. Because Optuna is among the most widely adopted Python hyperparameter optimization libraries in ML, a Rust-native reimplementation can significantly reduce memory footprint and execution time for tuning jobs. It also addresses supply-chain risks by eliminating Python dependencies, and expands hyperparameter tuning into the growing Rust ML ecosystem. Rustuna is hosted at github.com/optuna/rustuna and keeps Optuna's familiar API and concept rather than inventing a new interface. Its native Rust memory management reduces footprint compared with Python implementations, and the absence of Python dependencies removes a common target for supply-chain attacks.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is an automatic hyperparameter optimization software framework particularly designed for machine learning, with an imperative define-by-run style API. Hyperparameter optimization (HPO) is the process of automatically searching for a good set of hyperparameters, such as learning rate, batch size, or network depth, instead of relying on manual trial and error or exhaustive methods like grid search. Rustuna brings this framework to Rust, a systems programming language notable for performance and memory safety, opening the door to lower-overhead ML pipelines and reducing exposure to Python dependency attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optuna">Optuna - Wikipedia</a></li>
<li><a href="https://github.com/optuna/optuna">GitHub - optuna/optuna: A hyperparameter optimization framework · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperparameter_optimization">Hyperparameter optimization - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Rust`, `#Hyperparameter Optimization`, `#Optuna`

---

<a id="item-4"></a>
## [Huawei unveils Kirin 9050 Pro with LogicFolding architecture after six years](https://www.news.cn/20260907/adf46c5c003240d28cc3cf6de54f9b5f/c.html) ⭐️ 8.0/10

On September 7, Huawei released the Mate XT 2 trifold smartphone in Guangzhou, equipped with the new Kirin 9050 Pro chip — the first high-performance processor built with LogicFolding technology. The launch marks Huawei's first new flagship Kirin chip since the Mate 40 global event six years ago. The release signals Huawei's return to the flagship chip race after a six-year gap, introducing a 'LogicFolding' approach that stacks logic vertically instead of relying on conventional transistor shrinking. If successful, the architecture could reduce Huawei's dependence on EUV-based advanced manufacturing and support China's broader push for semiconductor self-sufficiency. Kirin 9050 Pro reportedly uses a 9-core CPU design with one 3.1GHz prime core, a redesigned LinxiCore CPU with simultaneous multi-threading, delivering up to 24% higher single-core and 52% higher multi-core performance. The LogicFolding design stacks logic units in layers inside a single chip and connects them with vertical interconnects, shortening signal paths and reducing latency.

telegram · zaihuapd · Sep 7, 08:20

**Background**: Huawei has been under strict U.S. export controls since 2019, cutting off its access to leading-edge chip-making tools that rely on extreme ultraviolet (EUV) lithography. LogicFolding is a proposed 3D design approach that folds conventional 2D circuit layouts into vertical stacks to shorten wiring distances and raise transistor density without requiring EUV lithography. Huawei has projected it can reach 1.4-nanometer-class equivalents by 2031 and plans to extend the architecture to its Ascend AI processors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/huawei-claims-sanctions-busting-breakthrough-with-1-4nm-class-chips-by-2031-claims-55-percent-higher-transistor-density-firm-claims-new-logicfolding-chip-architecture-can-bypass-euv-restrictions-introduces-tau-scaling-law-to-replace-moores-law">Huawei claims sanctions-busting breakthrough with 1.4nm-class chips by 2031, claims 55% higher transistor density — firm claims new LogicFolding chip architecture can bypass EUV restrictions, introduces 'Tau Scaling Law' to replace Moore's Law | Tom's Hardware</a></li>
<li><a href="https://www.huaweicentral.com/kirin-9050-pro/">Kirin 9050 Pro Chip: Architecture, Performance and More</a></li>
<li><a href="https://english.news.cn/20260907/566d283cf6704be9879f7a27506b9d38/c.html">Huawei unveils high-performance Kirin 9050 Pro chip-Xinhua</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Huawei Chip`, `#Semiconductor`, `#Kirin`, `#Technology`

---

<a id="item-5"></a>
## [China's Top Court Clarifies AI Liability in New 24-Article Judicial Interpretation](https://www.cnr.cn/news/20260907/t20260907_527806795.shtml) ⭐️ 8.0/10

On September 7, China's Supreme People's Court issued a judicial interpretation on artificial intelligence disputes, containing 24 articles across five parts. It clarifies liability for unauthorized AI face-swapping, algorithmic price discrimination, AI-generated fake endorsements, autonomous driving, and intellectual property issues. This provides clearer legal standards for AI-related civil disputes in China, directly affecting AI developers, platform operators, and consumers. It signals stronger regulatory accountability for AI misuse and algorithmic practices, potentially shaping business compliance and technology deployment across the country. The interpretation states that creating recognizable faces or voices with AI without consent may constitute infringement of personality rights. It also holds algorithmic price discrimination liable, supports punitive damages for AI impersonation that induces consumption, and regulates use of AI for online doxxing or privacy violations.

telegram · zaihuapd · Sep 7, 09:32

**Background**: AI face-swapping, often using deepfake technology, can replace a person's face in videos without consent, leading to fraud or reputation damage. Algorithmic price discrimination, known as 'sharen' or algorithm-based price gouging, means loyal or existing customers may be shown higher prices than new users. 'Open box' (kaihe) is a Chinese internet slang for maliciously exposing someone's private information online, also known as doxxing. This judicial interpretation addresses growing public concern over these AI-related harms and provides concrete legal guidance for courts.

<details><summary>References</summary>
<ul>
<li><a href="https://news.bjd.com.cn/2025/03/15/11097249.shtml">“懂你”的 算 法 里，藏着 什 么 算 计？_ 京报网</a></li>
<li><a href="https://baike.baidu.com/item/开盒/58943997">开盒（网络热词）_百度百科</a></li>
<li><a href="https://www.thecover.cn/news/88LAfmyL6KqH90qSdq8Jkw==">封面深镜｜防不胜防的“ AI 换 脸 + AI ...”</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#legal liability`, `#privacy`, `#China`, `#algorithmic governance`

---

<a id="item-6"></a>
## [ByteDance Founder Zhang Yiming Oversees Real-Time Spatial Video Model](https://www.bloomberg.com/news/articles/2026-09-07/bytedance-founder-joins-ai-elite-in-race-to-perfect-world-models) ⭐️ 8.0/10

ByteDance founder Zhang Yiming is personally overseeing development of a real-time spatial video generation model based on Seedance, targeting Pico VR headsets, with a possible launch in October 2026. This marks a rare case of a top Chinese tech founder directly driving a world-model project, signaling ByteDance's push into immersive AI. If delivered, it could lower VR hardware barriers and accelerate interactive virtual world applications. According to sources, the model generates video at about 0.05 seconds of latency and 20 frames per second, while offloading heavy computation to the cloud to ease demands on headset hardware. The reported launch window is still subject to change.

telegram · zaihuapd · Sep 8, 04:05

**Background**: Seedance is ByteDance's family of video-generation models; Seedance 2.0 is described as a multimodal model for text, image, audio, and video inputs. Spatial video generation focuses on producing temporally coherent frames with spatial consistency, which is essential for creating immersive 3D visuals in VR/AR. Pico is ByteDance's VR headset brand, and this model reportedly responds to Pico users' voice or actions. Such interactive generation aligns with the broader industry trend toward 'world models' that simulate dynamic, responsive virtual environments.

<details><summary>References</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/seedance">Seedance</a></li>
<li><a href="https://www.seeddance.io/models/seedance-2-0">Seedance 2.0 Free: AI Video Generator | 1080P, No Watermark</a></li>
<li><a href="https://genra.ai/blog/how-spatial-intelligence-is-transforming-video-generation">How Spatial Intelligence Is Transforming Video Generation</a></li>

</ul>
</details>

**Tags**: `#ByteDance`, `#Spatial Video`, `#Zhang Yiming`, `#VR`, `#AI Model`

---

<a id="item-7"></a>
## [Jellyfin 12.0 Launches with Performance Gains and Migration Improvements](https://jellyfin.org/posts/jellyfin-release-12.0/) ⭐️ 7.0/10

Jellyfin 12.0 has been released, focusing on improved performance and smoother library migration. The update follows seven release candidates between June and July, indicating a mature stabilization cycle. As a widely used open-source media server, this major release strengthens Jellyfin as an alternative to proprietary options like Plex, giving self-hosters improved performance and less painful upgrades. It also signals the continued maturing of the self-hosted media ecosystem. The release addresses performance regressions seen in 10.11.x and introduces a new migration path that may require a media rescan after upgrading. Community reports suggest the Android-to-Chromecast subtitle workflow remains a weak point.

hackernews · 0xC0ncord · Sep 8, 01:56 · [Discussion](https://news.ycombinator.com/item?id=49604861)

**Background**: Jellyfin is a free, volunteer-built media system that lets users stream their own media from a dedicated server to devices like smart TVs, phones, and web browsers. It is an open-source alternative to proprietary media servers such as Plex and Emby. The server component runs on Linux, Windows, and macOS, while client apps are available for many platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jellyfin">Jellyfin - Wikipedia</a></li>
<li><a href="https://jellyfin.org/">The Free Software Media System | Jellyfin</a></li>
<li><a href="https://github.com/jellyfin/jellyfin">GitHub - jellyfin/jellyfin: The Free Software Media System - Server Backend & API · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters were generally upbeat about the 12.0 upgrade experience, with one noting a painless migration of a 40TB library after skipping 10.11, while another expressed confidence that the performance bugs are fixed. However, subtitle handling on Android-to-Chromecast remains a recurring complaint, and at least one user is skeptical that the upgrade is worth the trouble.

**Tags**: `#Jellyfin`, `#media server`, `#open source`, `#self-hosted`, `#release`

---

<a id="item-8"></a>
## [Interactive Map Traces LA Building Construction from 1880 to 2026](https://lax-skyline.parcelscope.net/) ⭐️ 7.0/10

An interactive map at lax-skyline.parcelscope.net lets viewers watch Los Angeles grow parcel by parcel, visualizing building construction years from 1880 through 2026. It turns public property records into a timeline of the city’s physical development. The visualization gives ordinary residents an intuitive way to grasp how zoning, housing policy, and infrastructure choices shaped LA’s landscape and affordability crisis. It has already sparked substantive public debate about downzoning and transit history. The map is built from current LA County Assessor parcel data, so it only shows buildings that still stand; demolished structures are invisible. This means some older neighborhoods that were entirely redeveloped, like Palms, can appear falsely empty or recent in the timeline.

hackernews · rustywasm · Sep 7, 18:52 · [Discussion](https://news.ycombinator.com/item?id=49601655)

**Background**: Parcel-level maps color each property by the year it was built, using county assessor records originally maintained for property tax purposes. Because assessor data tracks existing improvements, the map is affected by survivorship bias: older buildings that were torn down leave no visible trace. LA’s development context also includes restrictive zoning policies from the 1980s and an early-20th-century streetcar system that was once the largest in the United States.

**Discussion**: Commenters broadly enjoyed the map but warned that it likely undercounts older buildings, because demolished structures are absent and some neighborhoods, like Palms, were completely replaced. Several viewed the visualization as evidence that 1980s downzoning created artificial housing scarcity and unaffordability, while others used it to reflect on LA’s once extensive but later removed rail transit network. One commenter also noted that they had built a similar mobile map visualization with Mapbox GL about ten years ago.

**Tags**: `#data-visualization`, `#urban-planning`, `#history`, `#los-angeles`, `#housing`

---

<a id="item-9"></a>
## [Abusive crawlers consume more CPU on git.kernel.org than all legitimate access](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev reported that on git.kernel.org, the Linux kernel's official Git hosting service, CPU cycles spent rendering commits for abusive crawlers now outnumber those for all legitimate access combined. Across five geo-distributed nodes, 14 CPU cores are constantly occupied rendering Git commits as HTML for scrapers. This report provides concrete evidence that low-value bot traffic has become a significant operational and cost burden for major public web infrastructure. Maintainers of public repositories and data-heavy sites may need better bot detection, rate limiting, or alternative serving strategies to protect limited CPU resources. Ryabitsev's TL;DR states that more CPU is spent rendering commits for scrapers than on all other legitimate access, including git clones. Simon Willison linked the issue to his own concern about Datasette, which serves a huge number of crawlable web pages.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository hosting site for the Linux kernel. cgit is a fast, lightweight web front-end for Git repositories, written in C, that displays repositories and commits as browsable HTML pages. Abusive crawlers and scrapers automatically request such pages en masse to collect code and data, and since rendering each HTML commit page is far more CPU-intensive than serving ordinary git clone traffic, this 'background radiation' severely skews CPU usage. Simon Willison's Datasette tool similarly publishes many crawlable HTML pages, which is why he finds this warning directly relevant to his own work.

<details><summary>References</summary>
<ul>
<li><a href="https://git.zx2c4.com/cgit/about/">cgit - A hyperfast web frontend for git repositories written ...</a></li>

</ul>
</details>

**Tags**: `#web scraping`, `#crawlers`, `#linux kernel`, `#server performance`, `#git`

---

<a id="item-10"></a>
## [OpenAI Chief Scientist Advocates Aligned AI for Defense, Warns Against Reckless Race](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 7.0/10

Jakub Pachocki, OpenAI's Chief Scientist, published a statement arguing that the strongest reason to continue training much smarter models is to build defensive AI systems against other AI. He also cautioned that this need must not become an excuse for recklessness or an AI arms race. This frames rapid AI capability advancement as a defensive necessity, potentially influencing AI policy and safety debates. It highlights the ongoing tension between accelerating AI development and ensuring safety in the broader industry. Pachocki cited securing infrastructure, protecting against rogue agents in real time, and inventing entirely new protective measures as core defensive tasks. He acknowledged uncertainty about broad AI progress but insisted that racing forward at all costs is absurd given the seriousness of the stakes.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment refers to the process of encoding human values and goals into AI models to make them helpful, safe, and reliable, even in novel situations. The concept of 'scalable defense' is emerging in AI safety and cybersecurity, focusing on automated defenses against AI-driven threats such as jailbreaks or rogue agent misuse. These remarks reflect an ongoing policy debate about whether AI labs should prioritize rapid capability advancement or stronger safety measures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-alignment">What is AI alignment? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#AI policy`, `#AGI`, `#quotes`

---

<a id="item-11"></a>
## [Generating Bad Apple autonomously from a single initial state using a tiny recurrent dynamical system (417k params) (P)](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 7.0/10

A tiny recurrent dynamical system with 417k params learns to autonomously generate the full Bad Apple video from a single initial state, without per-frame timing inputs.

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Tags**: `#recurrent neural networks`, `#video generation`, `#dynamical systems`, `#implicit neural representations`, `#machine learning`

---

<a id="item-12"></a>
## [Zero-Downtime Embedding Model Migration Method Released](https://www.reddit.com/r/MachineLearning/comments/1wabmm7/my_lab_found_a_way_to_migrate_between_embedding/) ⭐️ 7.0/10

A research lab shared embedflow, a method for switching embedding models without re-embedding the entire document store. It reranks a small number of documents from the old index with the new model and claims retrieval quality matches native re-indexing once K is large enough. For RAG systems with millions or billions of documents, upgrading an embedding model normally requires days or months of backfill on expensive GPUs. Embedflow makes model upgrades a lightweight reranking operation, potentially removing a major barrier to adopting better embeddings. They tested 63 migrations on corpora up to 1 million documents; the best case, upgrading Qwen 4B to 8B, reached native-level retrieval with K=50. Determining the optimal K remains difficult, and the implementation currently integrates with Qdrant via a pip-installable package and open GitHub repo.

reddit · r/MachineLearning · /u/Potential_Low_1183 · Sep 8, 02:16

**Background**: Embedding models convert text into numeric vectors so that documents can be searched by semantic similarity, which is the foundation of retrieval-augmented generation (RAG). Upgrading to a newer embedding model requires re-vectorizing all existing documents, a costly and time-consuming backfill process. Embedflow compares old and new model scores on a small candidate set and reranks them, avoiding a full re-computation. This trades a small accuracy calibration step for a massive reduction in compute time.

**Tags**: `#embedding-models`, `#RAG`, `#vector-search`, `#model-migration`, `#retrieval`

---

<a id="item-13"></a>
## [LLM-guided program evolution improves 10 best-known circle-packing solutions](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 7.0/10

A researcher used an LLM-guided program-evolution loop to improve 10 best-known Packomania csqv circle-packing solutions for N=101 to 114. The method iteratively asked an LLM to mutate optimizer code, scored each candidate with an independent verifier, and gained 2.4% to 5.4% at a total LLM cost of $27.72. This demonstrates that LLM-guided code evolution can cheaply improve long-standing optimization benchmarks instead of merely solving problems end-to-end. It suggests LLM-driven algorithm discovery could become a practical tool, especially for researchers with limited compute budgets. The improved cases span N=101 to 114 on the csqv benchmark, which maximizes the sum of radii of unequal circles inside a unit square, and Packomania independently accepted the new results. The author highlighted the plateau-detection stopping rule as the part they would most want criticized; code, solutions, and paper are all publicly available.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Packing circles in a square is a classic geometric optimization problem, and Packomania maintains a widely used catalog of best-known benchmark solutions. The csqv variant uses unequal circles and sum-of-radii as the objective, making existing best-known results difficult to beat. LLM-guided program evolution is an emerging approach in which a large language model proposes code-level changes to a seed algorithm, automatic tests keep improvements, and discarded failures guide future iterations; similar ideas underpin systems such as DeepMind's AlphaEvolve.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.05093v1">LLM-Guided Program Evolution for Circle Packing:Breaking 10 ...</a></li>
<li><a href="https://packomania.com/cciuneq/">The best known solutions of benchmark instances for the ...</a></li>
<li><a href="https://arxiv.org/abs/2403.11446">[2403.11446] LLM Guided Evolution -- The Automation of Models ... LLM Guided Evolution - The Automation of Models Advancing Models GitHub - clint-kristopher-morris/llm-guided-evolution: LLM ... LLM Guided Evolution - The Automation of Models Advancing ... LLM Guided Evolution - The Automation of Models Advancing Models LLM Guided Evolution - The Automation of Models Advancing Models llm-guided-evolution/README.md at main · clint-kristopher ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program evolution`, `#optimization`, `#circle packing`

---

<a id="item-14"></a>
## [OpenAI discloses internal AI token costs: median $600, top spenders $7,000 per day](http://gigazine.net/gsc_news/en/20260907-ai-use-inside-openai/) ⭐️ 7.0/10

OpenAI disclosed internal data showing that as of August 2026, the median daily AI token cost for its researchers exceeds $600, while the top 10% spend more than $7,000 per day. Researcher output tokens have increased 124-fold since November 1, 2025, and about 70% of researchers now run at least four AI agents at once. This is one of the few concrete, quantitative looks at how heavily AI is embedded in a top AI lab's own workflow, and it signals that frontier-model usage—and cost—is scaling extremely fast. It also highlights the central role of multi-agent workflows in driving enterprise AI token consumption, a trend other companies will likely follow. The figures come from OpenAI's internal usage tracking as of August 2026, with output-token growth measured relative to November 1, 2025. Roughly 70% of researchers simultaneously run at least four AI agents, which helps explain the massive jump in token consumption.

telegram · zaihuapd · Sep 7, 13:53

**Background**: In large language models, tokens are the basic units of text that the model reads and generates; costs are typically calculated per token, covering both input and output. Multi-agent systems break complex tasks into subtasks handled by several specialized AI agents that collaborate, which naturally consumes far more tokens than a single-model query. These two concepts explain why aggressive AI use inside a lab like OpenAI can produce daily costs in the hundreds or thousands of dollars per researcher.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pongo.com.tw/ai-token-explained/">AI token 是 什 麼？ 搞懂中英文差異、計費與記憶上限 - 龐果設計</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1928636720796136414">Multi-Agent System，一篇就够了。 - 知乎</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI adoption`, `#token usage`, `#multi-agent`, `#industry data`

---

<a id="item-15"></a>
## [Europe's Top Carriers in Talks for Satellite-to-Phone Alliance to Counter Starlink](https://www.bloomberg.com/news/articles/2026-09-07/europe-s-top-carriers-in-talks-for-satellite-to-mobile-venture) ⭐️ 7.0/10

Deutsche Telekom, Orange, Vodafone, and Telefónica are in preliminary talks to form a European satellite-to-mobile alliance, aiming to jointly bid for EU spectrum reserved for European-controlled operators. The initiative is intended to offer direct-to-phone satellite services and counter Starlink's dominance in Europe. This strategic alliance could reshape Europe's satellite communications landscape by providing a homegrown alternative to Starlink's direct-to-cell services. If successful, it would help European operators secure valuable spectrum and maintain sovereignty over critical communications infrastructure. The EU plans to set aside a portion of the approximately 2 GHz band for operators majority-owned by European companies, with existing licenses expiring in May 2027. The satellite-to-mobile service would deliver calls, SMS, and data services directly to unmodified ordinary smartphones.

telegram · zaihuapd · Sep 8, 02:35

**Background**: Direct-to-mobile satellite communication lets ordinary smartphones communicate directly with satellites, which act as cell towers in space, providing connectivity in remote or underserved areas without traditional cellular coverage. The 2 GHz band is allocated for mobile-satellite services (MSS) in several regions, and interest is growing in using it for consumer direct-to-phone offerings such as text, voice, and data. Starlink's 'Direct to Cell' is a prominent example of this approach, and the European carriers' initiative responds to such services gaining global traction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.itedgenews.africa/direct-to-satellite-mobile-access-goes-mainstream/">Direct - to - Satellite mobile access goes mainstream - ITEdgeNews</a></li>
<li><a href="https://sciencenigeria.com/direct-mobile-connectivity-to-satellite/">Direct Mobile Connectivity To Satellite | Science Nigeria</a></li>
<li><a href="https://www.acma.gov.au/2-ghz-mss-band-allocation">2 GHz MSS band allocation | ACMA</a></li>

</ul>
</details>

**Tags**: `#satellite`, `#telecom`, `#spectrum`, `#Starlink`, `#Europe`

---

<a id="item-16"></a>
## [Malaysia Eyes Huawei Ascend 910C for Sovereign AI Project, First to Shun US Chips](https://www.businesstimes.com.sg/international/malaysia-eyes-huawei-chips-ai-project-despite-us-warning) ⭐️ 7.0/10

Malaysia is seriously evaluating Huawei's Ascend 910C chips for a sovereign AI project worth 2 billion ringgit (about $494 million). If completed, it would become the first official case of a foreign government choosing Chinese AI accelerators over US products. This could mark the first government-level official rejection of US AI chips, showing Huawei can compete on the global stage despite US export controls. The decision may reshape AI supply chains and influence how other countries choose sides in the AI chip race. Sources say it is still unclear how many chips Malaysia would purchase. The Trump administration previously warned that using Huawei's AI accelerator could violate US export rules, but the Malaysian government considers the decision purely commercial.

telegram · zaihuapd · Sep 8, 03:35

**Background**: Sovereign AI refers to a country or government retaining control over its AI models, data, and infrastructure rather than relying on external cloud providers. The Huawei Ascend 910C is Huawei's HiSilicon high-end accelerator, widely seen as a Chinese alternative to Nvidia's A100/H100 series. Due to US export controls, Huawei's access to advanced manufacturing is limited, and most performance figures for the chip come from third-party estimates and teardowns rather than official specifications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unite.ai/huaweis-ascend-910c-a-bold-challenge-to-nvidia-in-the-ai-chip-market/">Huawei’s Ascend 910C: A Bold Challenge to NVIDIA in the AI ...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-research-suggests-huaweis-ascend-910c-delivers-60-percent-nvidia-h100-inference-performance">DeepSeek research suggests Huawei's Ascend 910C delivers 60% ...</a></li>
<li><a href="https://www.cloudmagazin.com/en/2026/06/01/sovereign-ai-as-an-infrastructure-issue-why-open-source-decides-on-sovereignty/">Sovereign AI as an Infrastructure Issue: Why Open Source Decides on...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#AI chips`, `#Malaysia`, `#geopolitics`, `#AI infrastructure`

---

<a id="item-17"></a>
## [Caltech Students Launch First Research-Math Hackathon With LLMs](https://mathathonchallenge.com/index.html) ⭐️ 6.0/10

A team of Caltech undergraduates is organizing the Caltech Mathathon, described as the first hackathon devoted to research-level mathematics. The event encourages participants to use AI tools such as LLMs responsibly to explore mathematical problems. This event could help shape how mathematicians integrate AI into their work, signaling growing interest in combining large language models with mathematical discovery. It may also provide students with hands-on AI learning opportunities at a time when some commenters say Caltech's CS department offers limited ML breadth. The organizers are unpaid volunteers who do not represent Caltech, and all raised funding goes toward paying the judges and participants. The format is unusual for a hackathon: teams reportedly work for around 40 hours waiting on LLM outputs, which some commentators say clashes with the traditional short, high-intensity hacking experience.

hackernews · astroanax · Sep 7, 09:26 · [Discussion](https://news.ycombinator.com/item?id=49596055)

**Background**: A hackathon is an intensive event where participants collaborate over a short period to build or prototype solutions, often in software development. The Caltech Mathathon applies this format to mathematical research, using large language models—AI systems trained on massive text data—as reasoning aids for proposing conjectures, testing ideas, or assisting theorem discovery, while emphasizing that outputs must be carefully checked.

**Discussion**: One organizer, brian-bfz, hosted an AMA and stressed that the team is independent and focused on responsible AI use. Commenters were split: some called the idea exciting and applied to participate, while one argued that waiting on LLM outputs for 40 hours conflicts with the spirit of traditional hackathons, and a recent Caltech grad noted the event partly compensates for the CS department's perceived weaknesses in AI education.

**Tags**: `#hackathon`, `#mathematics`, `#LLM`, `#AI`, `#Caltech`

---

<a id="item-18"></a>
## [Mercator to Equal Earth: AI-Built D3 Map Transition](https://simonwillison.net/2026/Sep/7/equal-earth/) ⭐️ 6.0/10

Simon Willison created an animated D3-based transition between the Mercator and Equal Earth map projections, using OpenAI's GPT-6 Astra (medium) in ChatGPT Work. The interactive tool was released on simonwillison.net after the UN voted on a resolution encouraging equal-area map projections. This demonstrates how AI-assisted coding (vibe coding) can quickly produce polished interactive visualizations for current events. It also highlights the shift from Mercator to equal-area projections, which affects how world maps are perceived and taught. The transition uses D3 (Data-Driven Documents) to morph between the two map projections, and was built with GPT-6 Astra medium in ChatGPT Work. It was released in September 2026 following a UN General Assembly resolution that specifically noted the Equal Earth projection.

rss · Simon Willison · Sep 7, 16:24

**Background**: The Equal Earth projection is an equal-area pseudocylindrical map projection invented in 2018, inspired by the Robinson projection but preserving relative sizes of areas. The Mercator projection preserves angles and shapes but distorts areas near the poles, making regions like Greenland and Africa appear incorrectly sized. 'Vibe coding' is AI-assisted software development in which the developer describes a task in plain language and the AI generates code, often with minimal review. GPT-6 Astra is a large language model from OpenAI released on September 3, 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Equal_Earth_map_projection">Equal Earth map projection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>

</ul>
</details>

**Tags**: `#geospatial`, `#d3`, `#map projections`, `#visualization`, `#AI-assisted coding`

---

<a id="item-19"></a>
## [KV Cache as an Agent Runtime: A New Path to Interactive LLMs](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 6.0/10

Yandex researchers published a blog post proposing to treat the KV cache as an agent runtime, manipulating the model's inference state rather than only its weights or harness for more interactive LLM systems. The post builds on the lab's previous work (Hogwild! Inference and AsyncReasoning) and previews a Qwen3.8-27B agent interactively playing DOOM. Framing the inference state as a runtime opens a relatively unexplored axis for improving agent capabilities: instead of changing the harness or model weights, developers could directly modify or share the KV cache. If developed further, this could lead to cheaper, low-latency interactive applications such as real-time game agents and more responsive collaborative agents. The post positions model inference and runtime design itself as an under-explored capability axis, arguing that harnesses are too abstract while changing the model is too costly, leaving a middle ground. It references Hogwild! Inference, which showed that modern reasoning-capable LLMs can share a concurrent KV cache out of the box without additional fine-tuning by exploiting RoPE, and AsyncReasoning, with the DOOM demo presented as future work.

reddit · r/MachineLearning · /u/_puhsu · Sep 7, 09:03

**Background**: During decoding, LLMs store the Keys and Values of previously processed tokens in a KV cache to avoid recomputing attention, making the cache a core component of efficient inference. An agent runtime is typically the software layer that executes an agent's perception, planning, and action loop. By 'KV cache as an agent runtime,' the authors suggest treating that cache as a live control surface: modifying or sharing it between concurrent model instances could create immediate responsiveness and inter-agent collaboration. Hogwild! Inference provides grounding for the idea by demonstrating that parallel LLM instances can collaborate through shared cache blocks without fine-tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.06261">[2504.06261] Hogwild! Inference: Parallel LLM Generation via ... Hogwild! Inference: Parallel LLM Generation via Concurrent ... Hogwild! Inference GitHub - eqimp/hogwild_llm: Official PyTorch implementation ... hogwild_llm/inference_lib/python/hogwild at main · eqimp ... Hogwild! Inference: Parallel LLM Generation via Concurrent ... Async and Hogwild! Inference | AI Engineering from Scratch</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**Tags**: `#KV cache`, `#LLM inference`, `#agent runtime`, `#interactive LLMs`, `#research`

---

<a id="item-20"></a>
## [China's MIIT Plan Calls for Timely 6G Commercial Launch and eSIM Adoption](https://36kr.com/newsflashes/3973030022541575) ⭐️ 6.0/10

China's Ministry of Industry and Information Technology (MIIT) has issued its 15th Five-Year Plan for the information and communications industry. The plan says the country will start 6G commercial services at an appropriate time and advance application and business registration of new technologies such as eSIM and network-free communication in an orderly manner. The plan is a high-level regulatory roadmap that tells China's telecom operators, equipment vendors and chipmakers how to move from 5G-Advanced toward 6G. It also signals that eSIM and network-free communication are being taken seriously as commercial services, which will influence handset design, network investment and service approval policies in the country. The plan calls for urban and hotspot networks to evolve toward 'dual 10-gigabit' capability, with city hotspots able to reach 10 Gbps downlink and 1 Gbps uplink peak rates, and for continuous 5G-Advanced coverage from county-level urban areas to key towns. It also proposes domestic rules for satellite Internet equipment accessing networks, live-network tests for next-generation mobile intelligent terminals, and regulatory capability for intelligent terminal agents.

telegram · zaihuapd · Sep 7, 07:58

**Background**: 5G-Advanced, also known as 5G-A or 5.5G, is the intermediate step beyond the first phase of 5G, focusing on performance improvements, greater efficiency and support for specific use cases. An eSIM is an embedded SIM that replaces the physical SIM card and allows users to switch operators remotely. In the plan, 'network-free communication' generally refers to emerging communication capabilities that can provide services without relying on conventional operator network coverage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gsma.com/solutions-and-impact/technologies/networks/5g-network-technologies-and-solutions/5g-advanced/">What is 5G Advanced? | Networks | GSMA</a></li>
<li><a href="https://www.gsma.com/solutions-and-impact/technologies/esim/">What is an eSIM? Guide to eSIM technology & use cases</a></li>
<li><a href="https://en.wikipedia.org/wiki/ESIM">eSIM - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#6G`, `#eSIM`, `#telecom policy`, `#China`, `#5G-A`

---
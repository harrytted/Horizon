---
layout: default
title: "Horizon Summary: 2026-08-01 (EN)"
date: 2026-08-01
lang: en
---

> From 38 items, 20 important content pieces were selected

---

1. [QM: A Multiplayer Agent Harness for Scoped Work Collaboration](#item-1) ⭐️ 8.0/10
2. [Tailscale Post-Mortem: Reusable Auth Key Enabled Hugging Face Intrusion](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4 Flash 0731: 304B-Parameter Model Boasts Agentic Gains and Top Value](#item-3) ⭐️ 8.0/10
4. [Stateless MCP 2.0 Spec Reignites Interest, Inspires Two New Tools](#item-4) ⭐️ 8.0/10
5. [MiniMax to Open-Source Multimodal Video Model H3 on August 3](#item-5) ⭐️ 8.0/10
6. [German Court Rules AI Music Firm Suno Infringed Copyright](#item-6) ⭐️ 8.0/10
7. [Qwen Releases Audio-3.0-ASR-Flash with 95% Medical Term Accuracy](#item-7) ⭐️ 7.5/10
8. [Elevator Scheduling Algorithms: A Deep Dive into Inefficiencies and Disk Scheduling Analogies](#item-8) ⭐️ 7.0/10
9. [Getting 25 Gbps Thunderbolt Ethernet Working on a Mac Studio](#item-9) ⭐️ 7.0/10
10. [Run Kimi K3 on 29GB RAM at 0.50 tok/s](#item-10) ⭐️ 7.0/10
11. [Open Weight Revolution: Simon Willison on Oxide and Friends](#item-11) ⭐️ 7.0/10
12. [smevals: A Small Eval Suite for Models, Prompts, and Harnesses](#item-12) ⭐️ 7.0/10
13. [OpenAI Bans Scam Network Using ChatGPT in Cambodia](#item-13) ⭐️ 7.0/10
14. [Major Labels Propose AI Songs Need Human Authorship for Charts](#item-14) ⭐️ 7.0/10
15. [Google to Exempt Sanctioned Countries from Android Developer Verification](#item-15) ⭐️ 7.0/10
16. [NIST's Official Standard Water Costs $120,000 a Gallon](#item-16) ⭐️ 6.0/10
17. [datasette-agent 0.4a0 adds browser_task for custom JavaScript](#item-17) ⭐️ 6.0/10
18. [Trained transformer models predict blood glucose levels](#item-18) ⭐️ 6.0/10
19. [Meituan and Suzhou Launch Riders' 'Traffic Light Wait Timer'](#item-19) ⭐️ 6.0/10
20. [Simon Willison Releases llm-mcp-client 0.1a0 Alpha](#item-20) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [QM: A Multiplayer Agent Harness for Scoped Work Collaboration](https://github.com/yc-software/qm) ⭐️ 8.0/10

QM, a new multiplayer agent harness for work, has been introduced on GitHub by YC-software, enabling scoped, company-wide collaboration among AI agents and humans. It centers on per-person scopes and shared rooms, a design directly addressing the challenge of coordinating multiple agents in a workplace. QM is significant because scoping is widely considered the hardest problem in multiplayer agent systems, and QM's per-person scopes plus shared rooms offer a pragmatic pattern for company-wide assistants. It represents a notable step toward collaborative agent infrastructure, complementing standards like the Model Context Protocol (MCP) for interconnecting AI agents with tools and data. The design emphasizes per-person scopes and shared rooms, which community members praise as a sane answer for company-wide assistance. However, some commenters note that a true multiplayer harness should also support other agents and any MCP clients, and that making agents multiplayer is largely a context-sharing problem.

hackernews · tosh · Jul 31, 18:04 · [Discussion](https://news.ycombinator.com/item?id=49126604)

**Background**: An agent harness is the software infrastructure surrounding a large language model that enables it to function as an AI agent, managing tools, memory, state persistence, execution environments, and feedback loops. MCP (Model Context Protocol) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems connect to external tools and data sources, making agent interoperability a key piece of the multiplayer puzzle.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://www.databricks.com/blog/ai-harness">What is an AI Agent Harness? | Databricks Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community reaction is largely positive and validating: builders of adjacent projects such as AQ and gstack see QM as confirming the direction of multiplayer agent harnesses. Some commenters raise the need for broader interoperability with MCP clients and other agents, while one user humorously describes an agent scheduling meetings with other agents without human involvement.

**Tags**: `#AI agents`, `#multiplayer`, `#harness`, `#collaboration`, `#MCP`

---

<a id="item-2"></a>
## [Tailscale Post-Mortem: Reusable Auth Key Enabled Hugging Face Intrusion](https://tailscale.com/blog/hugging-face-intrusion) ⭐️ 8.0/10

Tailscale published a post-mortem analyzing the Hugging Face intrusion, revealing that an attacker abused a reusable Tailscale auth key to enroll 181 rogue nodes into Hugging Face's tailnet. The post emphasizes that no Tailscale vulnerability was exploited. This matters because it shows that even with a mesh VPN, insecure credential handling (e.g., committing a reusable auth key to an env file) can compromise an entire network. It also highlights the need for better alerting, key scoping, and security checkups in identity-based networking tools. According to the post-mortem, 136 credentials were exposed, one of which was a reusable Tailscale auth key. The attacker used it over several days to enroll 181 nodes, each tagged with a CI node identity that granted the same access as legitimate CI nodes; Tailscale itself had no vulnerabilities found or exploited.

hackernews · bluehatbrit · Jul 31, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49127306)

**Background**: Tailscale is a software-defined mesh VPN that lets organizations securely connect devices and services across the internet with zero-configuration networking. Tailscale auth keys are meant to automate device provisioning, but a reusable key can be a standing credential; if leaked, it allows anyone to join the network and receive any tags assigned to it. The Hugging Face incident underscores that even robust zero-trust networking tools rely on proper credential hygiene and monitoring.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/">Tailscale | Secure Connectivity for AI, IoT & Multi-Cloud</a></li>
<li><a href="https://tailscale.com/docs/features/access-control/auth-keys">Auth keys · Tailscale Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tailscale">Tailscale</a></li>

</ul>
</details>

**Discussion**: Comments on the post were mostly positive, with some praising Tailscale for its transparency and 'owning' the incident. Others saw it as clever marketing, and several users suggested concrete improvements such as alerting on long-lived key use, binding credentials to specific origins/destinations, and offering a 'security checkup' feature.

**Tags**: `#security`, `#tailscale`, `#access-control`, `#incident-response`, `#key-management`

---

<a id="item-3"></a>
## [DeepSeek V4 Flash 0731: 304B-Parameter Model Boasts Agentic Gains and Top Value](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek released DeepSeek-V4-Flash-0731, a 304-billion-parameter model with substantially enhanced agentic capabilities. It ranks ahead of MiniMax M3 on the Artificial Analysis Intelligence Index, with pricing at $0.14 per million input tokens and $0.27 per million output tokens. This release suggests that cost-effective, high-performing models are becoming a key competitive frontier, especially for agentic workflows that require repeated model calls. It could pressure other providers on price-performance and expand access to capable AI for a broader range of developers and applications. The model at default reasoning level delivered disappointing results in Simon Willison's pelican riding a bicycle test, but setting reasoning_effort to high produced a much better image. It appears as a strong outlier on the cost-vs-intelligence Pareto chart, sitting alone in the most attractive quadrant.

rss · Simon Willison · Jul 31, 23:59

**Background**: Agentic AI refers to AI systems that can pursue goals, use tools, and take actions with varying degrees of autonomy, often operating within human-defined objectives and constraints. The Artificial Analysis Intelligence Index is an aggregate benchmark score that combines multiple tests to compare model intelligence, and it is often used alongside cost measures to evaluate value.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence , Performance, and Price</a></li>

</ul>
</details>

**Tags**: `#deepseek`, `#llm`, `#ai-model`, `#agentic-ai`, `#cost-performance`

---

<a id="item-4"></a>
## [Stateless MCP 2.0 Spec Reignites Interest, Inspires Two New Tools](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

The 2026-07-28 Model Context Protocol specification (MCP 2.0) introduces a stateless mode that eliminates the need for session IDs and initialization handshakes, and Simon Willison has built two new tools—mcp-explorer and datasette-mcp—taking advantage of it. The new spec reduces a tool call from two HTTP requests to one. This is the most significant change to MCP since its launch, making it much easier to implement clients and servers and improving scalability for web applications. It could reinvigorate MCP adoption among AI developers, especially for smaller models and serverless environments, by offering an auditable and controlled alternative to giving agents a terminal. In the stateless protocol, requests use headers like MCP-Protocol-Version, Mcp-Method, and Mcp-Name instead of a session ID, with client info passed via the _meta field. mcp-explorer is an interactive CLI for probing MCP servers, while datasette-mcp provides three read-only tools (list_databases, get_database_schema, execute_sql) that let agents query Datasette instances.

rss · Simon Willison · Jul 31, 23:13

**Background**: MCP (Model Context Protocol) is a standard introduced by Anthropic in November 2024 for connecting LLM-powered agents to external tools and data sources. It gained enormous popularity throughout 2025 but was later partly overshadowed by Anthropic's "Skills" concept, since an agent with shell and curl access could do much of the same work. Stateless protocols like HTTP do not retain session state between requests, which improves visibility, reliability, and scalability compared with stateful alternatives. Simon Willison's renewed interest reflects the new spec's reduced implementation complexity and better fit for auditable AI tool use.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/31/stateless-mcp/">Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>
<li><a href="https://www.linkedin.com/pulse/new-mcp-stateless-here-what-actually-changes-arnold-cartagena-dpcte">The new MCP is stateless . Here is what actually changes.</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#Model Context Protocol`, `#AI`, `#Agents`, `#Protocol`

---

<a id="item-5"></a>
## [MiniMax to Open-Source Multimodal Video Model H3 on August 3](https://modelscope.cn/models/MiniMax/MiniMax-H3) ⭐️ 8.0/10

MiniMax announced that its next-generation general-purpose multimodal video model H3 will be open-sourced on August 3, 2026 via ModelScope. The model natively supports understanding and generation of text, images, audio, and video, and is available for commercial use. H3 is an open-weights model that combines understanding and generation across text, images, video, and audio, lowering the barrier for commercial video creation in fields such as film, advertising, e-commerce, gaming, and UI demos. Its release strengthens the open-source multimodal ecosystem and provides developers with a powerful alternative to proprietary video models. H3 supports precise multi-dimensional editing controls and can combine multiple reference materials to produce coherent, continuous creations, including subtitles, brand information, special effects, product showcases, and dynamic UI presentations. According to fal.ai, the model supports up to 2K video generation and will be hosted on ModelScope.

telegram · zaihuapd · Jul 31, 12:37

**Background**: MiniMax is an AI company developing multimodal foundation models, and H3 is its new general-purpose omni-modal generation model that can jointly understand contexts spanning text, images, video, and audio. ModelScope is Alibaba's model-as-a-service platform that hosts open-source models and offers tools for exploration, inference, training, and deployment. Open-weights multimodal video models allow developers and businesses to run and customize state-of-the-art video generation capabilities locally or in their own infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks ...</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video ...</a></li>
<li><a href="https://www.modelscope.ai/">Home Page · ModelScope</a></li>

</ul>
</details>

**Discussion**: Reddit discussions on r/StableDiffusion express strong interest in the open-weight release and ask about release dates, noting the model's combined text-image-video-audio context handling. Overall sentiment is positive, with users anticipating practical applications and comparisons to existing video generation models.

**Tags**: `#multimodal`, `#video model`, `#open-source`, `#MiniMax`, `#ModelScope`

---

<a id="item-6"></a>
## [German Court Rules AI Music Firm Suno Infringed Copyright](https://www.dw.com/en/german-court-rules-that-ai-music-firm-suno-violated-copyrights/a-78152227) ⭐️ 8.0/10

The Munich Regional Court ruled on Friday that AI music company Suno infringed copyright by using protected music to train its models. The court ordered Suno to disclose its illegal gains and pay damages, the amount of which is yet to be determined. This is one of the first major court rulings to test how copyright law applies to AI music training, setting a significant legal precedent for the AI industry. It signals that AI developers may need to obtain licenses before using copyrighted works as training data, affecting companies worldwide. The lawsuit was filed by GEMA, a German music copyright collective, in January 2025. During the trial, GEMA demonstrated that songs generated by Suno were highly similar to original works; Suno said it disagrees with the ruling and will consider appealing.

telegram · zaihuapd · Jul 31, 13:11

**Background**: GEMA is a German collective management organization that represents over 95,000 musicians in Germany and more than 2 million rights holders worldwide, managing copyright royalties for musical works. Suno is an AI music generation platform that creates complete songs with vocals and instrumentation from text descriptions in under a minute. The core dispute is whether AI models can be trained on copyrighted recordings without permission or compensation, which this ruling now addresses under German law.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Suno_(platform)">Suno (platform) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GEMA_(German_organization)">GEMA ( German organization) - Wikipedia</a></li>
<li><a href="https://www.gema.de/en/about-gema">GEMA : Purpose, role and relevance</a></li>

</ul>
</details>

**Tags**: `#AI`, `#copyright`, `#music`, `#legal`, `#Suno`

---

<a id="item-7"></a>
## [Qwen Releases Audio-3.0-ASR-Flash with 95% Medical Term Accuracy](https://x.com/Alibaba_Qwen/status/2083111834123407825) ⭐️ 7.5/10

Alibaba's Qwen team released the Qwen-Audio-3.0-ASR-Flash speech recognition model on July 31, 2026. Internal tests show medical term recall of 95.36% and industrial term recall of 93.24%. This release brings domain-specific ASR with strong accuracy for technical terminology, which is critical for healthcare, manufacturing, and other specialized industries. By offering streaming and batch modes with custom hotwords, it lowers the barrier for building real-time voice applications in Chinese and other languages. The model supports three deployment forms: real-time streaming recognition, recorded-file transcription, and non-real-time recognition, all available through Alibaba Cloud Model Studio. It features context consistency, custom hotwords, and output of polished, structured text from speech.

telegram · zaihuapd · Aug 1, 03:29

**Background**: Automatic speech recognition (ASR) converts spoken audio into text. Streaming ASR processes audio in small chunks (often 100-200 ms) to deliver low-latency output, while batch/offline transcription processes entire files. Custom hotwords allow users to boost recognition of specific business terms such as product names or proper nouns. Qwen is Alibaba's large language and multimodal model family, with Qwen-Audio variants focused on audio understanding and generation.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/qwen/qwen3-asr-flash-2026-02-10">Qwen3 ASR Flash - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.alibabacloud.com/help/en/model-studio/custom-hot-words/">Improve Speech Recognition Accuracy with Custom Hotwords ...</a></li>
<li><a href="https://deepgram.com/learn/streaming-speech-recognition-api">Streaming Speech Recognition API for Real-Time Transcription</a></li>

</ul>
</details>

**Tags**: `#ASR`, `#Qwen`, `#Speech Recognition`, `#AI Model`, `#Domain-Specific`

---

<a id="item-8"></a>
## [Elevator Scheduling Algorithms: A Deep Dive into Inefficiencies and Disk Scheduling Analogies](https://john.fun/elevators) ⭐️ 7.0/10

The article provides an engaging technical exploration of elevator scheduling algorithms, comparing real-world inefficiencies and drawing parallels to disk scheduling (SCAN/LOOK). It is a deep dive that has generated substantial Hacker News discussion. This piece connects two classic systems problems—elevator control and disk scheduling—showing how a common algorithmic pattern plays out in different physical contexts. It is valuable for developers and systems engineers interested in scheduling trade-offs, and its high community engagement shows it resonates with practitioners. The article discusses algorithms such as SCAN (elevator algorithm) and LOOK, noting that destination dispatch systems are often worse in practice. It uses the analogy of a spinning hard drive being like an elevator wrapped around a spindle, and notes that LOOK is what most people expect elevators to do.

hackernews · Jrh0203 · Jul 31, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49124218)

**Background**: Elevator scheduling algorithms determine how elevators respond to floor calls, balancing efficiency and fairness. The SCAN algorithm, also called the elevator algorithm, is a disk-scheduling technique where the disk arm moves in one direction servicing requests until the end, then reverses. LOOK is a variant that stops at the last pending request instead of going to the physical end, reducing unnecessary travel.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elevator_algorithm">Elevator algorithm - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/operating-systems/disk-scheduling-algorithms/">Disk Scheduling Algorithms - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal experiences and resources: one recalled implementing elevator simulations in high school and noted SCAN is a disk-scheduling algorithm; another working in a destination dispatch building observed that most traffic is to/from the ground floor, which may explain the article's findings. Others linked to the Elevator Saga game, questioned paternoster lift safety, and mentioned a mobile game that uses LOOK.

**Tags**: `#algorithms`, `#elevators`, `#scheduling`, `#systems`, `#HN discussion`

---

<a id="item-9"></a>
## [Getting 25 Gbps Thunderbolt Ethernet Working on a Mac Studio](https://www.jeffgeerling.com/blog/2026/getting-25g-ethernet-mac-thunderbolt/) ⭐️ 7.0/10

Jeff Geerling's blog post details how to achieve 25 Gbps Ethernet on a Mac Studio using Thunderbolt-attached PCIe networking gear, including hardware choices and performance results. The post also signals a likely limitation: macOS lacks SMB Direct (RDMA) support, which may cap real-world throughput. This is significant because it demonstrates a viable path to 25 GbE on Apple silicon Macs, which lack built-in high-speed Ethernet ports beyond 10GbE options. It also highlights the trade-offs and protocol bottlenecks that pro users must consider when pushing Mac networking beyond 10 Gbps. The setup involves a Thunderbolt-to-PCIe chassis (e.g., Sonnet) with a 25GbE SFP28 NIC, and comments mention real-world bidirectional throughput around 25–27 Gbps. A noted caveat is a 15W upstream power limit on some Thunderbolt devices, and one commenter suggests a cheaper eGPU enclosure with a standard PCIe NIC as an alternative.

hackernews · speckx · Jul 31, 16:15 · [Discussion](https://news.ycombinator.com/item?id=49125034)

**Background**: 25 Gigabit Ethernet (25GbE) is a networking standard that uses single-lane 25 Gbit/s technology derived from 100GbE's four 25 Gbit/s lanes (IEEE 802.3bj), and was promoted by a consortium including Arista, Microsoft, Google, and Mellanox. Thunderbolt networking is another high-speed option, turning Thunderbolt ports into a bridge for fast Mac-to-Mac transfers. SFP28 transceivers and Direct Attach Cables (DACs) are common physical-layer options for 25GbE connections.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/introduction-25g-40g-ethernet-network-fancy-wang">Introduction to 25 G and 40G Ethernet Network</a></li>
<li><a href="https://www.lannerinc.com/news-and-events/eagle-lanner-tech-blog/how-25-gigabit-ethernet-meet-today-s-network-demands">How 25 Gigabit Ethernet Meet Today’s Network Demands - Lanner...</a></li>
<li><a href="https://appleinsider.com/inside/mac/tips/how-to-transfer-files-between-two-macs-with-a-cable">How to transfer Mac files with a cable instead of AirDrop</a></li>

</ul>
</details>

**Discussion**: Commenters shared mixed but practical experiences: one found the Sonnet adapter reliable but expensive and noted its 15W upstream power limit, while another proposed a cheaper eGPU-enclosure approach. Several agreed that the likely bottleneck is macOS's lack of SMB Direct (RDMA) support, and one commenter joked that 10GbE is already enough for their workflow but enjoyed seeing the push further.

**Tags**: `#Thunderbolt`, `#Ethernet`, `#Mac`, `#Networking`, `#Hardware`

---

<a id="item-10"></a>
## [Run Kimi K3 on 29GB RAM at 0.50 tok/s](https://github.com/sqliteai/waste) ⭐️ 7.0/10

A GitHub project named 'waste' demonstrates running Kimi K3, a 2.8-trillion-parameter open-weight model, on just 29GB of RAM using memory optimization techniques, albeit at a slow generation speed of 0.50 tokens per second. This is significant because it shows frontier open-weight models can run on consumer hardware without expensive GPUs, broadening access to advanced AI. However, the impractical speed raises important questions about the trade-offs between memory savings and real-world usability. According to a commenter's estimate, sustained power draw of 42W at $0.20/kWh translates to about $5 per million tokens, excluding hardware costs. Another commenter warns that the maintainer organization sqliteai has a history of using non-open-source licenses such as the Elastic License, advising caution despite the current open license.

hackernews · marcobambini · Jul 31, 14:12 · [Discussion](https://news.ycombinator.com/item?id=49123386)

**Background**: Kimi K3 is Moonshot AI's open-weight multimodal reasoning model with 2.8 trillion parameters, the first open model to reach that scale, and it scores 57 on the Artificial Analysis Intelligence Index. Running such a huge model typically requires multi-GPU servers, but techniques like aggressive quantization, layer-wise inference, and using unified memory on modern hardware can drastically reduce the memory footprint, at the cost of slower generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K 3 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://dev.to/alanwest/how-to-actually-run-an-llm-on-almost-no-ram-con">How to Actually Run an LLM on Almost No RAM - DEV Community</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: one commenter provides a cost analysis suggesting the approach is uneconomical, while another says they could tolerate the slow speed if outputs were concise. Several commenters question whether the README and code are LLM-generated, and one warns about the maintainer's licensing history, advising against using their projects despite the current open license.

**Tags**: `#LLM inference`, `#memory optimization`, `#open source`, `#performance`, `#AI engineering`

---

<a id="item-11"></a>
## [Open Weight Revolution: Simon Willison on Oxide and Friends](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 7.0/10

Simon Willison joined Bryan Cantrill and Adam Leventhal on the Oxide and Friends podcast to discuss the open-weight model revolution, focusing on the release of Kimi K3 and the open-weights AI policy letters signed by major AI companies. The episode also touched on accidental cybersecurity attacks and revisited predictions for 2026. This discussion matters because Kimi K3 demonstrates that open-weight models can now compete head-to-head with proprietary frontier models, potentially reshaping the AI industry's competitive landscape. The policy letters and the notable absence of Anthropic highlight ongoing debates about AI openness, security, and American leadership. Kimi K3 is the first open model to reach 2.8 trillion parameters, scoring 57 on the Artificial Analysis Intelligence Index, comparable to Opus 4.8 and GPT-5.5. DeepSeek V4 Flash, released right after the recording, is a Mixture-of-Experts model with 284B total and 13B activated parameters supporting a 1M-token context window.

rss · Simon Willison · Jul 31, 21:33

**Background**: Open-weight models make their trained weights available under stated terms, but unlike fully open-source AI, they may not include all freedoms to study, modify, and share. The podcast episode occurred during a particularly eventful week for AI, with Kimi K3 competing with proprietary frontier models and public letters about open weights and American AI leadership being signed by major companies, with Anthropic as a notable exception.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K 3 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#AI`, `#podcast`, `#cybersecurity`, `#deepseek`

---

<a id="item-12"></a>
## [smevals: A Small Eval Suite for Models, Prompts, and Harnesses](https://simonwillison.net/2026/Jul/31/smevals/#atom-everything) ⭐️ 7.0/10

Simon Willison and Prime Radiant introduced smevals, a new tool for running small eval suites across different model configurations and grading the results. It is run via uvx, uses YAML-based eval directories, and supports commands like run, grade, serve, and build. This tool provides AI/ML practitioners with a lightweight, configurable way to compare models, prompts, and agent harnesses, addressing the growing need for practical evaluation infrastructure in the LLM ecosystem. Simon Willison's endorsement adds credibility and visibility to the project. smevals separates running evals from grading them: runs are executed per config and then graded against defined checks, which can be simple string checks or custom model-based checkers. The tool also generates static HTML reports for easy sharing, and the vocabulary includes evals, tasks, configs, runs, runners, graders, checks, and checkers.

rss · Simon Willison · Jul 31, 21:15

**Background**: Evals are structured benchmarks used to measure and compare the capabilities of large language models, helping practitioners identify edge cases and regressions. Existing frameworks like EleutherAI's LM Evaluation Harness offer broad multi-task evaluation, while tools like uvx run Python executables in ephemeral environments, making smevals easy to invoke from coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents">Demystifying evals for AI agents \ Anthropic</a></li>
<li><a href="https://aiwiki.ai/wiki/lm_evaluation_harness">LM Evaluation Harness | AI Wiki</a></li>
<li><a href="https://docs.astral.sh/uv/">uv is an extremely fast Python package and project manager, written in...</a></li>

</ul>
</details>

**Tags**: `#evals`, `#AI`, `#machine learning`, `#tooling`, `#LLM`

---

<a id="item-13"></a>
## [OpenAI Bans Scam Network Using ChatGPT in Cambodia](https://openai.com/index/disrupting-malicious-uses-of-ai-criminal-scam-operation/) ⭐️ 7.0/10

On August 4, 2026, OpenAI announced it had banned a network of ChatGPT accounts likely based in Poipet, Cambodia, used for multiple types of fraud including investment scams, pig-butchering schemes, gambling fraud, and impersonation of law enforcement. OpenAI acted on leads from WhatsApp and shared threat information with industry partners and relevant authorities. This action demonstrates a concrete real-world case of AI tools being weaponized for large-scale fraud and human trafficking-related content, highlighting the growing importance of proactive AI safety measures. It also shows how AI companies can cooperate with messaging platforms to disrupt criminal operations, which may set a precedent for future abuse prevention. The accounts generated fake personas, translated conversations with victims, and forged images of passports and legal documents, following a three-step scheme of contact, emotional bonding, and money extraction. Some accounts also generated content suspected of being related to human trafficking and forced labor, such as recruiting 'chat workers' in Poipet with promises of airfare and accommodation, matching public reports of trafficking in Southeast Asia. OpenAI said the network may have targeted hundreds of people, with individual victims losing thousands of dollars, though exact figures could not be verified.

telegram · zaihuapd · Jul 31, 23:41

**Background**: AI-powered chatbots like ChatGPT can be misused by malicious actors to automate and scale fraudulent operations, reducing the cost and effort needed to deceive victims. 'Pig-butchering' scams combine fake romantic relationships with investment fraud, and have become a major form of cybercrime. OpenAI has established safety and misuse monitoring mechanisms, and this disruption is part of its broader efforts to combat the criminal use of AI.

**Tags**: `#OpenAI`, `#AI safety`, `#cybercrime`, `#fraud`, `#ChatGPT`

---

<a id="item-14"></a>
## [Major Labels Propose AI Songs Need Human Authorship for Charts](https://www.theverge.com/ai-artificial-intelligence/973741/ai-music-major-record-labels-charts) ⭐️ 7.0/10

Universal, Sony, and Warner have jointly proposed that AI-generated songs require substantial human authorship to qualify for official music charts, going beyond the existing AI labeling initiatives from RIAA and IFPI. This proposal could reshape how AI-generated music is distributed and monetized, affecting artists, AI music startups, and streaming platforms. It also intensifies the industry debate over copyright, training data rights, and creative authenticity in the AI era. The proposal also requires AI services to be fully authorized, model training data to be copyrighted, and tracks to comply with copyright and personality rights laws. Key terms like "substantial human authorship" remain loosely defined, and no chart organization has yet adopted the rules.

telegram · zaihuapd · Aug 1, 02:53

**Background**: The music industry has been grappling with how to handle AI-generated tracks. In July 2026, RIAA, IFPI, and other organizations proposed a labeling system distinguishing "AI-Generated" from "AI-Assisted" tracks. That approach focused on transparency, whereas the new record-label proposal goes further by setting entry barriers for charts, reflecting growing concerns about unlicensed AI training data and chart manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ifpi.org/music-community-introduces-new-labelling-program-to-distinguish-generative-ai-in-sound-recordings/">Music community introduces new labelling program to... - IFPI</a></li>
<li><a href="https://www.aimusicpreneur.com/ai-music-news/riaa-ifpi-ai-music-labelling-system/">RIAA and IFPI propose AI music labels</a></li>
<li><a href="https://www.ecoustics.com/news/ai-music-rules/">Why Should AI Created Music Be Allowed on the... - ecoustics.com</a></li>

</ul>
</details>

**Tags**: `#AI music`, `#copyright`, `#music industry`, `#AI regulation`, `#creative authenticity`

---

<a id="item-15"></a>
## [Google to Exempt Sanctioned Countries from Android Developer Verification](https://arstechnica.com/gadgets/2026/07/google-plans-to-exempt-sanctioned-nations-from-android-developer-verification/) ⭐️ 7.0/10

Google will exempt developers in sanctioned countries from its upcoming Android developer verification system, allowing them to distribute apps without identity checks or fees. The new verification system is scheduled to launch by the end of August 2026, after which unverified apps will be blocked from sideloading on Google-equipped Android devices. This policy creates a notable exception in Google's crackdown on sideloading, balancing platform security with sanctions compliance. Developers and users in affected regions (Iran, Cuba, North Korea, and occupied Ukrainian territories) can keep distributing apps, but they will not receive the enhanced security protections of verification. According to Google's FAQ, devices in sanctioned countries will be excluded from verification checks, so any developer can distribute there. However, users in those regions will not benefit from the verification program's enhanced security protections, and the US sanctions list currently includes Iran, Cuba, North Korea, and occupied Ukrainian territories.

telegram · zaihuapd · Aug 1, 03:08

**Background**: Android developer verification is a new Google system that links real-world identities to Android apps, requiring all apps to be registered by verified developers before they can be installed on certified Android devices. Sideloading refers to installing apps from outside Google Play, such as via APK files, a practice the verification system is designed to restrict. The exemption for sanctioned countries means those regions remain outside the verification system's security umbrella.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/developer-verification/guides">Android developer verification | Android Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sideloading">Sideloading - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Android`, `#developer-verification`, `#sanctions`, `#policy`, `#security`

---

<a id="item-16"></a>
## [NIST's Official Standard Water Costs $120,000 a Gallon](https://signoregalilei.com/2026/07/26/the-most-official-water-costs-120000-a-gallon/) ⭐️ 6.0/10

An article on SignoreGalilei highlights that NIST's official standard reference water, used for calibrating stable-isotope measurements, costs roughly $120,000 per gallon. The article explains that this incredibly expensive water is a certified calibration material, not a consumer beverage. The story draws attention to how specialized scientific reference materials can carry enormous costs because they require exact production and certification. It matters for isotope laboratories in fields like hydrology, climate science, and forensic testing, all of which depend on such standards for accurate measurements. The water is tied to the VSMOW (Vienna Standard Mean Ocean Water) scale, the international zero point for reporting oxygen and hydrogen stable-isotope ratios. In practice, laboratories buy only tiny amounts of the reference water, so the per-gallon price is a dramatic extrapolation of a small certified sample.

hackernews · surprisetalk · Jul 31, 15:00 · [Discussion](https://news.ycombinator.com/item?id=49124042)

**Background**: Stable isotope measurements rely on comparing very small variations in isotope ratios, such as 18O/16O and D/H, which are expressed relative to defined reference materials because absolute ratios are hard to measure from first principles. VSMOW, an isotopic water standard defined by the International Atomic Energy Agency, is the global zero point for water-isotope reporting. Laboratories calibrate isotope-ratio mass spectrometers (IRMS) against such standards, and NIST distributes certified versions of these waters; the high price reflects the production and certification costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wikidoc.org/index.php/Vienna_Standard_Mean_Ocean_Water">Vienna Standard Mean Ocean Water - wikidoc</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isotope-ratio_mass_spectrometry">Isotope-ratio mass spectrometry</a></li>

</ul>
</details>

**Discussion**: Commenters offered both humor and context: one compared NIST cigarette standards, another mentioned a peanut-butter reference material, and some explained why isotope calibration needs such standards. A few also discussed alternatives, such as using pure 1H2 16O, and shared price estimates for deuterium and tritium water.

**Tags**: `#metrology`, `#NIST`, `#calibration`, `#water`, `#standards`

---

<a id="item-17"></a>
## [datasette-agent 0.4a0 adds browser_task for custom JavaScript](https://simonwillison.net/2026/Jul/31/datasette-agent/#atom-everything) ⭐️ 6.0/10

Datasette Agent 0.4a0 introduces a new await context.browser_task() mechanism, allowing agent tool plugins to execute custom JavaScript directly in the user's browser. The change is implemented in pull request #33. This expands the capabilities of Datasette Agent plugins, enabling richer browser-side automation and interactive data exploration. It makes Datasette Agent more flexible for building AI-powered tools that can manipulate the user's current page or browser state. The feature is currently in an alpha release (0.4a0), so the API may change before a stable release. The mechanism uses a browser_task context that gives plugin tools access to the user's browser session, but no further technical details or security implications are provided in the release notes.

rss · Simon Willison · Jul 31, 14:14

**Background**: Datasette Agent is an AI assistant for exploring, querying, and charting data in Datasette, built on the LLM project. It allows users to ask questions about their data and the agent writes and runs SQL queries to find answers. The new browser_task mechanism is part of the ongoing development of Datasette Agent plugins, which extend the agent's capabilities with custom tools. In this context, browser automation refers to AI systems performing tasks inside a web browser, often by controlling the browser or executing scripts in the page.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette/ datasette - agent : An LLM-powered agent for...</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#datasette-agent`, `#LLM tool use`, `#browser automation`, `#JavaScript`

---

<a id="item-18"></a>
## [Trained transformer models predict blood glucose levels](https://www.reddit.com/r/MachineLearning/comments/1vc1txc/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 6.0/10

A Reddit user trained up to 17M-parameter encoder-only transformer models that predict blood glucose up to two hours ahead using past glucose, carb, and insulin data, plus announced meals. They released the source code, weights, and evaluation data on GitHub under the MIT license. This is an accessible, open-source example of applying modern transformer architectures to a real-world health time-series problem, which could encourage more experimentation in glucose forecasting and personalized medicine. However, it is a self-experiment without clinical validation, so its immediate impact on medical practice is limited. The model uses variable context lengths of 8–24 hours, DILATE loss for the median prediction and pinball loss for uncertainty bands, and operates in Kovatchev risk space reparameterized to a [40, 400] range. Four model sizes (nano to large) were trained, with the largest having about 17M parameters (16 layers, 16 heads); pretraining took roughly 48 hours while finetuning on public datasets like OhioT1DM took under 10 minutes.

reddit · r/MachineLearning · /u/0xdeadf1sh · Jul 31, 20:09

**Background**: Blood glucose prediction is important for diabetes management, as it helps patients and clinicians anticipate dangerous high or low episodes. The OhioT1DM dataset is a widely used public dataset containing eight weeks of glucose, insulin, and meal data from people with type 1 diabetes. DILATE is a differentiable loss function that penalizes both shape and temporal distortions in multi-step time series forecasts. The Kovatchev risk space is a nonlinear transformation of glucose values that emphasizes clinically risky extremes, making errors near hypo- or hyperglycemia more important.

<details><summary>References</summary>
<ul>
<li><a href="https://proceedings.neurips.cc/paper/2019/file/466accbac9a66b805ba50e42ad715740-Paper.pdf">Shape and Time Distortion Loss for Training Deep Time Series ...</a></li>
<li><a href="https://ceur-ws.org/Vol-2148/paper09.pdf">The OhioT 1 DM Dataset for Blood Glucose Level Prediction</a></li>
<li><a href="https://core.ac.uk/download/pdf/51291729.pdf">Blood glucose monitoring and metabolic control in youth with type...</a></li>

</ul>
</details>

**Tags**: `#transformer`, `#time series`, `#healthcare ML`, `#blood glucose prediction`, `#deep learning`

---

<a id="item-19"></a>
## [Meituan and Suzhou Launch Riders' 'Traffic Light Wait Timer'](https://www.meituan.com/news/NN260731177009116) ⭐️ 6.0/10

On July 31, Meituan and Suzhou public security officially launched a 'traffic light wait timer' (等灯停表) for food-delivery riders, starting with a road test in Suzhou. When riders wait at red lights, the system records the wait and extends the latest delivery deadline accordingly, initially covering about 1,100 intersections in Gusu District and the Suzhou Industrial Park. It is a practical smart-city improvement that uses real-time traffic-signal data to ease time pressure on riders, and its planned expansion to more than 20 cities could push the delivery industry to incorporate traffic-light wait time into scheduling algorithms. It also shows how traffic data collaborations between platform companies and city governments can produce rider-friendly policy changes. The feature uses rider location trajectories plus real-time signal light data to determine waiting states, and when a rider is delivering multiple orders at once, the wait time is credited to every order. Beijing and Wuxi have already started integrated tests, and Shanghai, Hangzhou, and more than 20 other cities are evaluating deployment.

telegram · zaihuapd · Jul 31, 11:00

**Background**: Real-time signal light data is normally obtained through cooperation with traffic-management authorities; for example, map providers such as Amap directly integrate police signal data in partner cities, including red-light remaining seconds, with errors under one second. This kind of data also powers V2X (vehicle-to-everything) systems, which let vehicles and riders receive signal-phase and timing information. Meituan's feature is an application of such data to last-mile delivery scheduling, compensating for wait times riders cannot control.

<details><summary>References</summary>
<ul>
<li><a href="https://juejin.cn/post/7619885691574009898">juejin.cn/post/7619885691574009898</a></li>
<li><a href="https://m.elecfans.com/article/6988528.html">1分钟秒懂 v 2 x 车 联网 技 术 -电子发烧友网</a></li>

</ul>
</details>

**Tags**: `#delivery`, `#logistics`, `#smart-city`, `#Meituan`, `#traffic-data`

---

<a id="item-20"></a>
## [Simon Willison Releases llm-mcp-client 0.1a0 Alpha](https://simonwillison.net/2026/Jul/31/llm-mcp-client/#atom-everything) ⭐️ 5.0/10

Simon Willison released the initial alpha version 0.1a0 of llm-mcp-client, a Python library that lets LLM users access tools exposed by Model Context Protocol (MCP) servers. The release is accompanied by a blog post explaining stateless MCP usage. This release is significant because MCP is becoming the open standard for connecting AI applications to external tools, and this plugin brings MCP tool access to the LLM command-line ecosystem. It lowers the barrier for developers to use MCP servers with LLM's plugin system. llm-mcp-client is installed as an LLM plugin, and MCP tool errors are surfaced as MCPToolError exceptions that the LLM model receives as error messages. The project is in early alpha, so the API may change; development uses 'uv run pytest'.

rss · Simon Willison · Jul 31, 23:03

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems integrate with external tools and data sources. It has since been adopted by major AI providers such as OpenAI and Google DeepMind. This library connects the 'llm' command-line tool, a popular way to run LLMs from the terminal, to MCP servers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://github.com/simonw/llm-mcp-client">GitHub - simonw/ llm - mcp - client : Access tools from MCP servers as...</a></li>
<li><a href="https://pypi.org/project/llm-mcp-client/">llm - mcp - client · PyPI</a></li>

</ul>
</details>

**Tags**: `#llm`, `#model-context-protocol`, `#release`, `#tools`

---
---
layout: default
title: "Horizon Summary: 2026-09-04 (EN)"
date: 2026-09-04
lang: en
---

> From 31 items, 20 important content pieces were selected

---

1. [OpenAI Unveils GPT-6 Astra With Record ARC-AGI-3 Score](#item-1) ⭐️ 10.0/10
2. [OpenAI announces GPT-6 Astra with ARC-AGI-3 benchmark gains](#item-2) ⭐️ 10.0/10
3. [.name Termination](#item-3) ⭐️ 8.0/10
4. [1993 Amiga game ported to Godot via LLM reading 68000 assembly](#item-4) ⭐️ 8.0/10
5. [Google Antigravity's Terms Can Trigger Full Account Suspension for Third-Party Tool Use](#item-5) ⭐️ 8.0/10
6. [Cerebras Adds Qwen 3.8 27B, Promising 1,500 Tokens/s](#item-6) ⭐️ 7.0/10
7. [IFM unveils K2 Horizon, a family of six fully open AI models](#item-7) ⭐️ 7.0/10
8. [Mol-JEPA: A Multimodal JEPA Model for Molecules](#item-8) ⭐️ 7.0/10
9. [Any Human Ever: Draws One Random AI Life from 100 Billion People](#item-9) ⭐️ 6.0/10
10. [GPT-6 Astra Shows Limited Progress on ARC-AGI-3 Benchmarks](#item-10) ⭐️ 6.0/10
11. [Can JEPA World Models Trained in Simulation Ground LLMs in Physics?](#item-11) ⭐️ 6.0/10
12. [AAAI-27 Desk Rejection Over Minor Abstract Edits Sparks Policy Questions](#item-12) ⭐️ 6.0/10
13. [Dating Apps Double Down on Face Recognition; Tinder Mandates User Verification](#item-13) ⭐️ 6.0/10
14. [OpenCode: Go Tools Missing x-opencode-session Header to Fail from Sept 6](#item-14) ⭐️ 6.0/10
15. [KEPCO Proposes $18.4B Prepaid Power Fees from Samsung, SK Hynix for Chip Cluster Grid](#item-15) ⭐️ 6.0/10
16. [HarmonyOS 7 Restricts Third-Party Use of Immersive Light Material to Save Power](#item-16) ⭐️ 6.0/10
17. [YYeTs Returns as Licensed Streaming App with Huashu Media, Targeting 30M Users](#item-17) ⭐️ 6.0/10
18. [Senator Asks NSA to Clarify Which VPNs Resist Foreign Surveillance](#item-18) ⭐️ 6.0/10
19. [NeurIPS 2026 Sydney Tickets Sell Out Within Minutes](#item-19) ⭐️ 5.0/10
20. [Tmall Launches AI Token Recharge Center, Selling Subscriptions from Alibaba Cloud, Zhipu, Kimi, MiniMax](#item-20) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils GPT-6 Astra With Record ARC-AGI-3 Score](https://openai.com/index/gpt-6-astra/) ⭐️ 10.0/10

OpenAI has announced GPT-6 Astra, a major new flagship model, and published a system card for it. The model reportedly achieves a near-perfect 99.9% score on the ARC-AGI-3 benchmark and makes major gains on the Artificial Analysis Coding Agent Index. GPT-6 Astra is positioned as a significant step toward AGI, and the near-perfect ARC-AGI-3 result suggests real progress in interactive reasoning and continuous learning, not just skill acquisition. This could reshape expectations for frontier AI and intensify the debate over whether such benchmarks truly demonstrate general intelligence. The system card is hosted on OpenAI's deployment-safety page and details the model's safety evaluations. Community commentators caution that the ARC-AGI-3 score depends on a 'responses API' harness and note that other benchmark improvements may be modest compared with previous iterative updates.

hackernews · kibae · Sep 3, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49554643)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that challenges AI agents to explore novel environments, acquire goals on the fly, build adaptable world models, and learn continuously. OpenAI has a pattern of publishing system cards alongside major model releases, as it did for GPT-4 and GPT-5. Coding-agent indexes such as the Artificial Analysis Coding Agent Index combine results from multiple software-engineering benchmarks to measure real-world autonomous coding performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://openai.com/index/gpt-5-system-card/">GPT-5 System Card | OpenAI</a></li>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks & Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical: one argues that the ARC-AGI-3 scorecard is misleading because GPT-5.6 Sol would score roughly 30% under the same responses-API harness used for GPT-6 Astra, while another questions the emphasis on autonomous shopping in demos. A third commenter notes that outside ARC-AGI-3, improvements look modest, and asks whether this truly represents AGI, echoing François Chollet's view that much frontier progress is still skill acquisition.

**Tags**: `#AI`, `#GPT-6`, `#OpenAI`, `#machine learning`, `#language models`

---

<a id="item-2"></a>
## [OpenAI announces GPT-6 Astra with ARC-AGI-3 benchmark gains](https://simonwillison.net/2026/Sep/3/gpt6-astra/) ⭐️ 10.0/10

On September 3, 2026, OpenAI announced GPT-6 Astra, rolling out initially to a limited set of organizations and soon to all ChatGPT Plus, Pro, Business, and Enterprise users via ChatGPT, the OpenAI API, and AWS. API pricing is set at $10 per million input and $50 per million output, matching Claude Fable 5 and 5.1, and the model label will be gpt-6-astra. This is OpenAI's flagship model release and an explicit competitor to Anthropic's Claude Fable line, launched at the same price point. Its headline 99.9% ARC-AGI-3 score and strong security and long-context results could reset industry expectations, though third-party intelligence benchmarks show rivals remain competitive. OpenAI reports Astra scores 99.9% on ARC-AGI-3 using its custom Provider Adapter harness for $19K, while the default ARC-AGI-3 harness produced 62.7% for $26K; the custom harness preserves opaque reasoning state between requests and uses compaction. On security tasks Astra hits 100% on ExploitBench, 42.4% on ExploitGym, and 99.2% on SRE-Bench binary reverse engineering, and on long context it scores 100% at 256K-512K tokens and 96.3% at 512K-1M tokens; Artificial Analysis still places it 5 points below Claude Fable 5.1 on its Intelligence Index.

rss · Simon Willison · Sep 3, 20:18

**Background**: ARC-AGI-3 is an interactive reasoning benchmark released in March that challenges AI agents to explore novel environments, acquire goals on the fly, build adaptable world models, and learn continuously. Claude Fable 5 is Anthropic's Mythos-class model made available for general use in June 2026 with safeguards, alongside a restricted-access Claude Mythos 5 with fewer restrictions. OpenAI's custom Provider Adapter harness differs from the default harness by maintaining reasoning state across requests and using compaction, which helps explain why Astra's reported ARC-AGI-3 score varies so much by harness.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>

</ul>
</details>

**Tags**: `#AI`, `#OpenAI`, `#GPT-6`, `#language models`, `#ARC-AGI`

---

<a id="item-3"></a>
## [.name Termination](https://neil.fraser.name/news/2026/09/03/) ⭐️ 8.0/10

ICANN/Verisign plans to terminate existing third-level .name registrations (x.y.name), releasing the parent second-level domains, causing widespread concern among affected owners.

hackernews · pavel_lishin · Sep 3, 14:54 · [Discussion](https://news.ycombinator.com/item?id=49550772)

**Tags**: `#ICANN`, `#DNS`, `#domain names`, `#internet governance`, `#.name`

---

<a id="item-4"></a>
## [1993 Amiga game ported to Godot via LLM reading 68000 assembly](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 8.0/10

A developer ported his 1993 Amiga game, originally written in MC68000 assembly in Baghdad, to the Godot engine in a single evening using Anthropic's Claude LLM. He also released the original game for free. This demonstrates a practical workflow for preserving and modernizing legacy software: LLMs can translate decades-old assembly code into modern engines, making vintage games playable on current platforms. It highlights a broader trend of AI-assisted retrocomputing and code archaeology. Claude used the vasm assembler on a Mac and iterated until the produced binary was byte-identical to the original shipped files; a residual 108-byte difference came from the fact that the originals were saved as an AsmOne memory snapshot after the game had been running, not clean assembler output. The port took one evening to reach a playable state, with extra weekends spent refining the feel and shipping.

hackernews · rabahs · Sep 3, 14:28 · [Discussion](https://news.ycombinator.com/item?id=49550375)

**Background**: The Amiga was a popular 1980s–90s personal computer whose games were often written in Motorola 68000 assembly for performance. AsmOne was an Amiga assembler that assembled directly into memory, and the developer saved that running memory as his shipped game file. vasm is a modern portable and retargetable assembler used in this workflow, while Godot is an open-source game engine. This context explains why the developer verified parity by reassembling with vasm and why byte-identical output was significant.

<details><summary>References</summary>
<ul>
<li><a href="http://sun.hasenbraten.de/vasm/">vasm portable and retargetable assembler</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amiga_programming_languages">Amiga programming languages - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed admiration for the original feat of writing an Amiga game in assembly in 1993 and shared their own AI-assisted retro-porting experiments, such as converting a ZX81 memory dump to Go and building 68k console recompilation frameworks. Some also asked about the author's debugging experiences and the game's inspirations.

**Tags**: `#retrocomputing`, `#LLM`, `#game-development`, `#Godot`, `#68000-assembly`

---

<a id="item-5"></a>
## [Google Antigravity's Terms Can Trigger Full Account Suspension for Third-Party Tool Use](https://twitter.com/GergelyOrosz/status/2095453567955968398) ⭐️ 8.0/10

A viral post by Gergely Orosz highlights Google Antigravity's terms of service, which state that suspected use of third-party AI tools via an Antigravity session can lead to suspension of the entire Google account. The Antigravity team responded on X, saying the account referenced is the Antigravity account and that they will clarify the ToS wording. Since Google accounts often hold years of email, calendars, photos, and even government digital ID integrations, a suspension triggered by an AI classifier can have disproportionate consequences. This fuels user concerns about relying on Google AI products when one false positive could lock users out of critical services. Google Antigravity is Google's agentic development platform—a chat-oriented environment, IDE, CLI, and SDK for orchestrating autonomous AI coding agents. One community member reported being banned from Antigravity for 'suspected' ToS violations with a notification hinting at OpenClaw, a tool they said they had never used; the team says the clarified wording will limit such bans to the Antigravity account.

hackernews · tosh · Sep 3, 11:01 · [Discussion](https://news.ycombinator.com/item?id=49548452)

**Background**: Google Antigravity is an AI-powered software development platform designed for the 'agent-first era,' allowing developers to build and orchestrate autonomous AI agents for coding tasks. Its terms of service govern usage of the platform, and concerns arose when users realized that a ToS violation could theoretically affect their broader Google account. Community discussion has highlighted that false positives from AI-based enforcement are particularly dangerous because Google support is often hard to reach and bans can disrupt far more than just AI tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>

</ul>
</details>

**Discussion**: Comments were largely negative, with users sharing anecdotes of surprise bans and warning about escalation to government ID lockouts. A notable counterpoint came from a comment quoting Antigravity team member Varun Mohan, who clarified that the banned account is the Antigravity account and that the ToS will be reworded to avoid confusion.

**Tags**: `#Google`, `#Antigravity`, `#Terms of Service`, `#Account Ban`, `#AI`

---

<a id="item-6"></a>
## [Cerebras Adds Qwen 3.8 27B, Promising 1,500 Tokens/s](https://inference-docs.cerebras.ai/models/overview) ⭐️ 7.0/10

Cerebras has added the Qwen 3.8 27B model to its inference lineup, advertising generation speeds up to 1,500 tokens per second. The listing appears to offer one of the fastest hosted endpoints for this model. At the advertised speed, Qwen 3.8 27B could become an attractive hosted choice for token-hungry tasks like code generation and large codebase analysis. But if rate limits and billing problems persist, users may still prefer slower local models or other providers for sustained workloads. Community testing shows the headline speed can collide with caps: one user reports a 450,000-token-per-minute limit and burned through $1.10 in about 90 seconds because cached tokens count toward it, while another cites 150k tokens per minute on the public endpoint. Enterprise accounts can also be blocked from self-serve billing, and users are still waiting for an OpenRouter integration.

hackernews · altertable · Sep 3, 18:32 · [Discussion](https://news.ycombinator.com/item?id=49554520)

**Background**: Qwen is a family of large language models developed by Alibaba Cloud, with releases distributed through Hugging Face and GitHub. Cerebras Systems is an AI hardware and cloud company known for its Wafer-Scale Engine, which the company positions as a platform for very fast LLM training and inference.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/?ref=completecsm.ai">Cerebras is the go-to platform for fast and effortless AI training.</a></li>

</ul>
</details>

**Discussion**: Reaction is mixed: users appreciate the raw speed but question whether restrictive rate limits make the service practical for large coding tasks. One user hit a token cap in about 90 seconds and spent $1.10, while another noted local tools can already deliver hundreds of tokens per second. Several also want Cerebras to offer the model through OpenRouter.

**Tags**: `#AI inference`, `#LLM`, `#Cerebras`, `#Qwen`, `#performance`

---

<a id="item-7"></a>
## [IFM unveils K2 Horizon, a family of six fully open AI models](https://ifm.ai/blog/k2/) ⭐️ 7.0/10

IFM has introduced K2 Horizon, a connected fleet of six open AI models spanning from a 3.7B model to a 375B flagship with 512K context. The release is notable for being fully open, sharing training data, code, checkpoints, and evaluation artifacts. Open-weight families are common, but fully open stacks are still rare, so K2 Horizon gives developers a verifiable alternative to opaque models. It also targets the crucial self-hosted model segment, where users choose models based on real, open benchmark results. The lineup includes six model sizes; the flagship has 375B parameters and a 512K context window, and the project provides an unusually open training stack including code, data/recipes, checkpoints, and evaluation artifacts. On Hugging Face, accessing the models currently requires agreeing to share your contact information.

hackernews · karimf · Sep 3, 15:36 · [Discussion](https://news.ycombinator.com/item?id=49551760)

**Background**: Most 'open' LLMs are open-weight only: the trained parameters are public, but the training data and code remain secret. K2 Horizon is instead a connected family of models designed for reasoning, coding, agentic workflows, edge devices, and enterprise deployment, with sizes suited to different hardware. IFM frames the release as 'radically open' so that users can inspect exactly what goes into a model.

<details><summary>References</summary>
<ul>
<li><a href="https://ifm.ai/blog/k2/">Introducing K 2 Horizon : Frontier Performance, Radically Open</a></li>
<li><a href="https://www.datastudios.org/post/k2-horizon-375b-parameters-512k-context-fully-open-training-data-code-and-ai-models">K 2 Horizon : 375B Parameters, 512K Context, Fully Open Training...</a></li>
<li><a href="https://huggingface.co/IFM/K2-Horizon-7B">IFM/ K 2 - Horizon -7B · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Commenters broadly welcomed a fully open stack, especially since Nvidia's Nemotron is one of the few comparable efforts, but many challenged IFM's headline performance claims. One tester said the 3.7B model failed basic coding tasks and hallucinated nonexistent APIs, while another complained of model fatigue from the rapid release pace.

**Tags**: `#AI`, `#Open Source`, `#LLM`, `#Models`

---

<a id="item-8"></a>
## [Mol-JEPA: A Multimodal JEPA Model for Molecules](https://www.reddit.com/r/MachineLearning/comments/1w6i8pr/moljepa_multimodal_molecular_foundation_model_r/) ⭐️ 7.0/10

The author shared a paper introducing Mol-JEPA, a multimodal molecular foundation model based on JEPA, alongside a website summarizing its key results. The model was developed over roughly one year and is presented as still having room for performance improvement. Mol-JEPA extends JEPA, a self-supervised learning paradigm popularized by Yann LeCun, to molecular data, predicting in latent space instead of reconstructing raw inputs. This offers a potentially more efficient and robust alternative for molecular representation learning, which could benefit drug discovery and related fields. The announcement is brief and points to a summary website rather than a full paper, so architecture details and benchmark numbers live off-site. The author indicates performance is not yet optimal and explicitly solicits feedback and collaboration ideas.

reddit · r/MachineLearning · /u/TerribleAntelope9348 · Sep 3, 19:56

**Background**: JEPA (Joint Embedding Predictive Architecture) is a self-supervised learning paradigm popularized by Yann LeCun. Instead of reconstructing raw inputs like pixels or graphs, a JEPA model predicts missing information in an abstract latent representation space, which can be more robust and sample-efficient. Multimodal molecular foundation models pre-train on more than one data modality, such as molecular graphs and biomedical text, to learn generic representations for downstream tasks like property prediction and drug discovery. Mol-JEPA applies this JEPA-style latent prediction idea to the molecular domain, an approach that appears less explored than prior multimodal efforts like MolFM.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/jepa/">JEPA - GeeksforGeeks</a></li>
<li><a href="https://www.tomorrowstacklab.com/p/the-enterprise-world-model-why-ai-agents-need-a-semantic-layer">The Enterprise World Model : Why AI Agents Need a Semantic Layer</a></li>
<li><a href="https://arxiv.org/abs/2307.09484">[2307.09484] MolFM: A Multimodal Molecular Foundation Model</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#molecular`, `#JEPA`, `#foundation model`, `#drug discovery`

---

<a id="item-9"></a>
## [Any Human Ever: Draws One Random AI Life from 100 Billion People](https://anyhumanever.com/) ⭐️ 6.0/10

A new interactive website, Any Human Ever, selects a random person from the estimated 100 billion humans who have ever lived, then presents an AI-generated biography with details such as a birth year, location, life story, and cause of death. Visitors are guided through draws of a year, a place, and a life, each said to be sampled from real demographic data. This project turns the abstract scale of human existence into a personal, tangible story, making history more approachable for general audiences. It also highlights the wider challenge of AI hallucination and the need for clear citations and caveats when generative tools are used to present factual-sounding information about the past. The site explains that because population has grown exponentially, a randomly drawn birth is far more likely to fall near the present than in the remote past, although one commenter reported that most of their five draws were pre-modern. Other users found contradictory statistics about women's mortality and marriage rates, and citations that were either difficult to verify or seemingly unrelated to the claims.

hackernews · thinkingemote · Sep 3, 14:51 · [Discussion](https://news.ycombinator.com/item?id=49550698)

**Background**: Over an estimated 100 billion humans have been born throughout history, and because global population has grown rapidly, most of those births happened in recent times; this is why a random draw on Any Human Ever should favor modern eras. The site treats those population statistics as the real part of the experience, then uses a large language model to invent or embellish personal details about an anonymous individual. Large language models are known to produce 'hallucinations'—plausible-sounding but false information or fabricated citations—so the resulting life stories should be treated with caution even when the framing data is accurate.

<details><summary>References</summary>
<ul>
<li><a href="https://anyhumanever.com/">Any Human Ever : one life from over 100 billion</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_hallucination">AI hallucination</a></li>

</ul>
</details>

**Discussion**: Reactions are divided between fascination and skepticism: some users found the experience emotionally resonant or proposed using it as a prompt for tabletop RPGs like Thousand Year Old Vampire, while others flagged statistical inconsistencies and questioned whether the year-selection process actually follows the stated probability distribution. A recurring sentiment is that the project is both impressive and misleading, described by one commenter as cool yet dubious about the accuracy of the AI-generated data.

**Tags**: `#interactive`, `#history`, `#AI`, `#data-quality`

---

<a id="item-10"></a>
## [GPT-6 Astra Shows Limited Progress on ARC-AGI-3 Benchmarks](https://arcprize.org/blog/astra) ⭐️ 6.0/10

OpenAI's GPT-6 Astra has posted only limited gains on the ARC-AGI-3 benchmark, according to an ARC Prize blog post, disappointing those hoping for a breakthrough. The results have triggered 117 comments debating whether the performance is worth the compute cost and whether the benchmark truly measures general intelligence. ARC-AGI-3 is designed to be 'easy for humans, hard for AI,' so limited progress signals that frontier models still struggle with fluid, few-shot generalization. The debate matters because it questions whether scaling large language models is the right path toward artificial general intelligence. Community comments cite related FrontierMath Erdos results in which GPT-6 Astra solved 2 of 68 problems directly, at an electricity-equivalent cost of $218 and $247 respectively, though across all attempts it solved 5 of 68. One commenter estimates a cost of about $360 per puzzle, compared with roughly 10 minutes per puzzle for human testers.

hackernews · vignesh_warar · Sep 3, 19:45 · [Discussion](https://news.ycombinator.com/item?id=49555691)

**Background**: ARC-AGI is a benchmark suite that measures AI's ability to perform fluid, systematic, and few-shot generalization across diverse tasks not seen during training. GPT-6 Astra is OpenAI's large language model released on September 3, 2026 as a limited preview; OpenAI reports it reaches 64.6% on an internal comparison versus 52.6% for Claude Fable 5.1 at lower estimated API cost. The benchmark results are under discussion because performance on ARC-AGI often does not translate directly to real-world capability.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT - 6 Astra : A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some praise FrontierMath/Erdos as a benchmark and note models continue to solve them, while others question whether puzzles are a true measure of intelligence. Cost concerns dominate, with one user extrapolating that falling price/performance could make GPT-6 Astra cheaper than minimum-wage humans within two years. Another joked about whether an 'Astra hacker swarm' compromised the ARC Prize servers to achieve a 99% score, reflecting skepticism about result integrity.

**Tags**: `#AI`, `#ARC-AGI`, `#OpenAI`, `#benchmarking`, `#AGI`

---

<a id="item-11"></a>
## [Can JEPA World Models Trained in Simulation Ground LLMs in Physics?](https://www.reddit.com/r/MachineLearning/comments/1w69gvd/grounding_llms_with_jepabased_world_models/) ⭐️ 6.0/10

On Reddit, a user proposed combining JEPA-style latent world models trained in physics simulators such as MuJoCo with large language models to supply grounded physical intuition, and asked whether prior work or a simple prototype already exists. The proposal is a conceptual discussion, with no implementation or experiments attached. If successful, this line of research could push LLMs beyond token-level correlations toward physically grounded reasoning, improving planning and sample efficiency in embodied AI. It also connects two prominent research directions—Yann LeCun's JEPA vision and latent world models—into a concrete, testable setup. The user explicitly references V-JEPA for future-frame-representation prediction and DreamerV3 for latent world models, but says the specific combination of JEPA-style prediction, simulated physics grounding, and LLM attachment has not been done cleanly. Open questions include whether the simulator's representations transfer to the real world and whether the LLM interface should be prompt concatenation or cross-attention.

reddit · r/MachineLearning · /u/Full_Promotion4522 · Sep 3, 14:45

**Background**: Large language models describe physical phenomena fluently because they learn statistical relationships between words, but they do not have the embodied experience that allows humans to 'run' intuitions about objects, force, and trajectories; this is compared to Mary's Room thought experiment. JEPA (Joint Embedding Predictive Architecture), proposed by Yann LeCun, aims to learn by predicting future representations in a latent embedding space rather than reconstructing pixels or tokens. MuJoCo is a free, open-source physics engine commonly used in robotics and reinforcement learning for fast, accurate contact-rich simulation.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@tahirbalarabe2/what-is-jepa-085ca776013a">What is JEPA ? Joint Embedding Predictive Architecture ... | Medium</a></li>
<li><a href="https://mujoco.org/">MuJoCo — Advanced Physics Simulation</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#world models`, `#JEPA`, `#grounding`, `#AI research`

---

<a id="item-12"></a>
## [AAAI-27 Desk Rejection Over Minor Abstract Edits Sparks Policy Questions](https://www.reddit.com/r/MachineLearning/comments/1w6kcp6/aaai27_desk_rejection_over_incredibly_minor/) ⭐️ 6.0/10

A researcher reports being desk-rejected by AAAI-27 after making only minor changes to the title and abstract between the abstract-registration and full-paper deadlines. The rejection notice states that the decision is final and appeals will not be considered. This case highlights ambiguity in how AAAI-27 enforces its abstract-modification policy, a concern shared by many researchers preparing submissions. The outcome could affect authors who inadvertently violate the subjective “substantive change” rule, prompting calls for clearer guidance and fairer review processes in AI conferences. The AAAI-27 guidelines allow editing the title and abstract after abstract registration while warning against substantive changes, and they describe rejection in terms of changes that make the submission describe qualitatively different research. The affected researcher says nearly everything was identical and the modifications were “incredibly minor,” yet the rejection was still issued.

reddit · r/MachineLearning · /u/Dansilly · Sep 3, 21:12

**Background**: The AAAI conference series aims to promote research in artificial intelligence and foster exchange among researchers, practitioners, and engineers across the field. The 41st AAAI Conference on Artificial Intelligence (AAAI-27) is scheduled to be held February 16–23, 2027 in Montréal, Canada. A desk rejection in academic publishing occurs when an editor rejects a manuscript without sending it to peer reviewers, often because the submission fails to meet scope, quality, or formatting requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://aaai.org/conference/aaai/aaai-27/">AAAI - 27 - AAAI</a></li>
<li><a href="http://wikicfp.com/cfp/servlet/event.showcfp?eventid=200036&copyownerid=692">AAAI 2027 : The Forty-First AAAI Conference on Artificial Intelligence</a></li>
<li><a href="https://manusights.com/blog/desk-rejection-reasons">Desk Rejection : 7 Reasons & Exactly What to Do Next</a></li>

</ul>
</details>

**Tags**: `#AAAI`, `#desk rejection`, `#conference policy`, `#machine learning`, `#academic publishing`

---

<a id="item-13"></a>
## [Dating Apps Double Down on Face Recognition; Tinder Mandates User Verification](https://www.wired.com/story/face-recognition-is-becoming-the-norm-for-dating-apps/) ⭐️ 6.0/10

Tinder is now requiring existing users in the U.S., U.K., and other major markets to pass its Face Check video-selfie verification, after making the check mandatory for new users in 2025. At least a dozen major dating apps and websites have introduced face recognition or biometric checks that use liveness detection and video selfies to filter out AI-generated fake accounts. As AI-generated profiles and romance scams multiply, biometric checks are shifting from optional trust signals to mandatory gatekeeping on dating platforms. This creates a significant privacy benchmark for consumer biometric data and raises open questions about whether face verification can truly prevent account takeover or AI-driven identity fraud. Tinder and similar platforms say they do not store users' original photos, but they do process facial features and other biometric information during verification. Security researchers caution that facial verification only proves that a real person was present during registration, not that an account cannot later be taken over by a scammer or linked to an AI-fabricated identity.

telegram · zaihuapd · Sep 3, 10:20

**Background**: These checks rely heavily on liveness detection, which asks users to take a video selfie or follow head-movement prompts so the system can distinguish a live person from a photo, mask, or deepfake. Instead of storing a plain image, most face-recognition systems convert the captured face into a feature template, which is why companies claim original photos are not retained. The same technology is increasingly used outside dating apps in banking, access control, and other sensitive applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/news/story/tinders-new-face-check-feature-aims-to-combat-spam-build-trust-7919106/">Tinder 's new ' Face Check ' feature aims to combat spam... | Linked...</a></li>
<li><a href="http://jidasmart.com/article/6165317777.html">人 脸 识 别 活 体 检 测 ：揭秘其 原 理 与优缺点 - 深圳智能有限公司</a></li>

</ul>
</details>

**Tags**: `#face-recognition`, `#dating-apps`, `#privacy`, `#AI-fraud`, `#biometric-verification`

---

<a id="item-14"></a>
## [OpenCode: Go Tools Missing x-opencode-session Header to Fail from Sept 6](https://x.com/opencode/status/2095410501400289576) ⭐️ 6.0/10

OpenCode has alerted users that some tools using OpenCode Go are not sending the x-opencode-session request header, which is required for prompt-caching optimization. From September 6, requests missing this header may start being rejected; affected users will receive emails with personalized fix recommendations. The x-opencode-session header enables session-based prompt caching, which significantly lowers token costs and response latency for LLM calls. Because enforcement begins September 6, this is a breaking change: developers who embed OpenCode Go into tools must add the header to their HTTP requests before the deadline, or their integrations may begin failing. OpenCode says it will contact affected users by email with tailored guidance on fixing their setup. The header directly relates to prompt caching: the session ID lets the upstream LLM provider reuse a cached prefix, so omitting the header also silently forfeits those caching benefits even before any errors appear.

telegram · zaihuapd · Sep 3, 10:34

**Background**: OpenCode is an AI-assisted coding tool that works with sessions, and its ecosystem includes a Go-facing implementation (OpenCode Go) used by other tools when making requests to LLM providers. The x-opencode-session request header carries the current session ID, allowing providers to do session-based caching: tokens from earlier turns in a session are reused so identical prefixes are not processed again. Prompt caching of this kind is a widely adopted way to cut both cost and latency for model calls, and community plugins already exist to inject the header into outgoing requests. OpenCode also stores session data locally, and its official documentation covers troubleshooting for requests and related issues.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/iwaller/opencode-session-header">GitHub - iwaller/ opencode - session - header : OpenCode plugin that...</a></li>
<li><a href="https://opencode.ai/docs/troubleshooting/">Troubleshooting | OpenCode</a></li>
<li><a href="https://www.datadoghq.com/blog/monitor-prompt-caching-optimize-token-usage/">Monitor prompt caching to optimize your token usage | Datadog</a></li>

</ul>
</details>

**Tags**: `#OpenCode`, `#API`, `#请求头`, `#开发者工具`

---

<a id="item-15"></a>
## [KEPCO Proposes $18.4B Prepaid Power Fees from Samsung, SK Hynix for Chip Cluster Grid](https://mp.weixin.qq.com/s/HgZUrbwwGGGGBh1-qiyLFQ) ⭐️ 6.0/10

Korea Electric Power Corp (KEPCO) has proposed that Samsung Electronics and SK Hynix prepay a combined 25 trillion won (about $18.4 billion) in electricity fees over the next five years to fund grid construction for semiconductor clusters. Samsung would contribute roughly $14.7 billion and SK Hynix about $3.7 billion. This marks an unusual shift where chipmakers would directly fund power infrastructure, reflecting the enormous electricity demands of semiconductor mega-clusters. If accepted, it could set a precedent for how energy costs are shared between utilities and industrial consumers in Korea and affect the economics of Samsung's and SK Hynix's expansion plans. The exact interest rate, prepayment amount, and duration have not been finalized, and the two companies are still reviewing the proposal. KEPCO's total debt stood at 210.7 trillion won by the end of June 2026, with daily interest costs of about 11.5 billion won.

telegram · zaihuapd · Sep 3, 12:01

**Background**: South Korea is building a massive semiconductor mega-cluster in Gyeonggi Province, anchored by Samsung Electronics and SK Hynix, with total investment reportedly exceeding 600 trillion won. The cluster is projected to require power capacity of 3 gigawatts initially, growing to 10 gigawatts, comparable to the output of South Korea's largest nuclear reactors (over 7.6 GW each). The prepayment plan is a response to the financial strain of building grid infrastructure for this national project.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=N--iai78MBQ">Korea ’s Yongin Silicon Valley Plan: Not Just Factories - YouTube</a></li>
<li><a href="https://constructionreviewonline.com/south-korea-to-build-us471-billion-chip-making-cluster/">South Korea Semiconductor Mega - Cluster Expands as Global AI...</a></li>
<li><a href="https://techgolly.com/news/south-korea-launches-25-billion-ai-semiconductor-mega-cluster-to-secure-future">South Korea Launches $25 Billion AI Semiconductor Mega - Cluster ...</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#energy`, `#infrastructure`, `#Samsung`, `#SK Hynix`

---

<a id="item-16"></a>
## [HarmonyOS 7 Restricts Third-Party Use of Immersive Light Material to Save Power](http://7.0.0.105/) ⭐️ 6.0/10

Huawei confirmed that HarmonyOS 7 (build 7.0.0.105) now restricts third-party apps from using the immersive light-sensitive material, citing power consumption. The effect's availability was narrowed from all components to only Navigation/NavDestination title bars and the bottom TabBar of horizontal Tabs with barPosition set to BarPosition.End, except for pop-up components/methods, Slider, and Toggle. This is a breaking change for HarmonyOS developers who have already applied the immersive light-sensitive material across multiple components, and it requires migration planning. It also signals that Huawei prioritizes power efficiency and system performance over visual richness for third-party apps. Under the adjusted rules, non-exempt components only display the material in the Navigation/NavDestination title bar, or in a bottom TabBar within horizontal Tabs when barPosition is BarPosition.End. Developers who already adapted to the previous behavior were told to evaluate their use cases and perform the necessary migration and fixes.

telegram · zaihuapd · Sep 4, 01:31

**Background**: Immersive light-sensitive material is a visual effect introduced with HarmonyOS 6 (API 23) as part of the HarmonyOS Design System (HDS); it makes interfaces such as Gallery, notifications, and Control Center look more transparent and vivid. The effect is intended to deliver a refined and immersive viewing experience on supported devices. According to Huawei's response, the current restriction targets only third-party apps and is meant to reduce background rendering overhead and thus extend battery life.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ihonker.com/thread-34564-1-1.html">HarmonyOS 6 HDS...</a></li>
<li><a href="https://harmonyos.cool/docs/setting/immersive-light">全新 沉 浸 光 感 ，让界面更通透 - HarmonyOS NEXT</a></li>

</ul>
</details>

**Tags**: `#HarmonyOS`, `#API changes`, `#power consumption`, `#developer update`, `#UI components`

---

<a id="item-17"></a>
## [YYeTs Returns as Licensed Streaming App with Huashu Media, Targeting 30M Users](https://weibo.com/1744332207/RgvaanItV) ⭐️ 6.0/10

The Chinese video brand YYeTs has relaunched its app under the new name Renren Yingshi Fenxiang Jingcai, partnering with Huashu Media to offer licensed overseas titles on iOS and Android. Operators aim to reactivate 30 million legacy users this month, with memberships priced at 25 yuan per month or 175 yuan per year. The move shows a well-known online media brand trying to convert a large legacy fan base into a legitimate, licensed streaming business, an unusual evolution for a service associated with fansubbing. It also points to the industry's AI-driven localization push, as the company plans to export content across more than 50 countries and regions, starting with Southeast Asia. The operating firm, Fenxiang Jingcai Network Technology, says it will begin point-to-point promotion this month and is developing AI-based video localization, with plans to cover more than 50 countries and regions and prioritize exporting Chinese content to Southeast Asia. The current service remains focused on overseas film and TV titles, and old users who received the return email get one free month of membership.

telegram · zaihuapd · Sep 4, 02:48

**Background**: YYeTs is a Chinese online video and subtitle community that has been active since the mid-2000s, best known for volunteer-produced Chinese subtitles for overseas dramas, films and anime. The commercial relaunch is distinct from the original nonprofit subtitle group, reflecting an effort to turn community popularity into a licensed distribution business.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dujin.org/18447.html">人 人 影 视 （ YYeTs ）归来，官方字幕组发布新网址-缙哥哥</a></li>
<li><a href="https://ai.openi.cn/sites/373.html">YYeTs 人 人 影 视 - OpenI</a></li>
<li><a href="https://yysub.cc/resource/43865">鼠惑들쥐(2026) | 第1季连载中 | YYeTs ...</a></li>

</ul>
</details>

**Discussion**: The accompanying note in the original post cautions that although this YYeTs app and the original Renren Subtitle Group share roots, they are now basically separate; the subtitle group still publishes subtitles on a volunteer basis, e.g., via subHD. The comment reinforces the distinction between the commercial relaunch and the nonprofit fansubbing side.

**Tags**: `#YYeTs`, `#legal streaming`, `#AI localization`, `#Chinese media`, `#media reboot`

---

<a id="item-18"></a>
## [Senator Asks NSA to Clarify Which VPNs Resist Foreign Surveillance](https://arstechnica.com/security/2026/09/us-senator-calls-on-the-nsa-to-give-guidance-for-use-of-vpns/) ⭐️ 6.0/10

US Senator Ron Wyden has formally requested that the NSA update its public VPN guidance, asking whether commercial single-hop VPNs suffice against foreign surveillance of internet backbone traffic and whether multi-hop tools like Apple Private Relay, Tor, and Nym are preferable. The NSA must respond by October 14. The request targets high-risk users such as government personnel, defense contractors, and journalists, who need trustworthy guidance on choosing surveillance-resistant tools. If the NSA issues clear recommendations, it could significantly influence both individual choices and the broader VPN market. The senator specifically asked the NSA to assess whether random delay and traffic padding techniques add meaningful protection, and to compare single-node VPNs against multi-hop architectures. The request also asks for clarification on whether Apple Private Relay, which is not a full commercial VPN, should be preferred in certain contexts.

telegram · zaihuapd · Sep 4, 03:51

**Background**: A traditional VPN creates an encrypted tunnel between the user and a single server, hiding the user's IP from the destination website but leaving the VPN provider able to see both the user's identity and online activity. Multi-hop tools like Tor route traffic through several relays, while Nym adds a mixnet layer that uses delay and shuffling to obscure traffic patterns. Apple Private Relay sends Safari requests through two separate proxies so that no single party sees both who the user is and which sites they visit. These differing architectures matter because foreign state actors with backbone access can often observe or interfere with single-hop VPN connections.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/en-us/102602">About iCloud Private Relay - Apple Support</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nym_(mixnet)">Nym ( mixnet ) - Wikipedia</a></li>
<li><a href="https://www.comparitech.com/blog/vpn-privacy/multi-hop-vpn/">What is a multi - hop VPN and do you need one?</a></li>

</ul>
</details>

**Tags**: `#VPN`, `#NSA`, `#surveillance`, `#privacy`, `#security`

---

<a id="item-19"></a>
## [NeurIPS 2026 Sydney Tickets Sell Out Within Minutes](https://www.reddit.com/r/MachineLearning/comments/1w6gwni/neurips_sydney_sold_out_in_minutes_n/) ⭐️ 5.0/10

Passes for NeurIPS 2026 in Sydney reportedly sold out within minutes of going on sale. Reddit user alrojo posted that this happened about three weeks before paper decisions and wondered how many buyers are from industry and venture-capital-funded AI labs. The extremely rapid sell-out shows the overwhelming demand for the world's premier machine learning conference, especially its Sydney edition. It also underscores the growing presence of industry and VC-funded AI labs, which can affect who gets to attend and how the conference community evolves. NeurIPS 2026 is the fortieth annual Conference on Neural Information Processing Systems, scheduled for Sydney (Main) from December 6 to 12. The Reddit post provides no official ticket allocation numbers or exact sell-out duration, so the "minutes" claim is based on the poster's account.

reddit · r/MachineLearning · /u/alrojo · Sep 3, 19:09

**Background**: NeurIPS (Conference on Neural Information Processing Systems) is one of the most prestigious annual conferences for machine learning and computational neuroscience. It is organized by the NeurIPS Foundation and draws researchers and practitioners from academia and industry. According to the official website, NeurIPS 2026 in Sydney is the fortieth annual edition of the event. The intense ticket demand reflects the rapid growth of the AI field and the strong appetite for in-person networking and recruiting.

<details><summary>References</summary>
<ul>
<li><a href="https://neurips.cc/">2026 Conference</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems">Conference on Neural Information Processing Systems - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#NeurIPS`, `#conference`, `#machine learning`, `#community`

---

<a id="item-20"></a>
## [Tmall Launches AI Token Recharge Center, Selling Subscriptions from Alibaba Cloud, Zhipu, Kimi, MiniMax](https://www.jiemian.com/article/15050499.html) ⭐️ 5.0/10

Tmall launched an AI space station (Token Recharge Center) on September 3, allowing users to directly purchase subscription products from Alibaba Cloud, Zhipu, Kimi, MiniMax, and other major model vendors. The platform supports periodic subscription plans such as Token Plan and Coding Plan, as well as pay-as-you-go usage, with delivery via card codes or direct recharge. This marks AI model subscriptions entering mainstream e-commerce, making large language model services more accessible to consumers and small teams that may lack technical expertise. It also opens a new distribution channel for AI vendors beyond traditional developer-focused platforms. The day before the launch, Zhipu opened a flagship store on Tmall and began selling Coding Plan packages, with search volume jumping 40-fold on the first day. The offerings combine both periodic subscription plans and usage-based billing, with card-code and direct-recharge delivery methods.

telegram · zaihuapd · Sep 3, 13:11

**Background**: In large language models, tokens are small units into which text is broken down for processing; they serve as the foundation for both model understanding and API billing. AI vendors typically price API access and subscription products by token usage or through fixed plans. A Token Recharge Center centralizes these purchase scenarios in an e-commerce storefront, making it easier for non-technical users to buy AI services.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>
<li><a href="https://blog.openreplay.com/count-tokens-llm-api-costs/">How to Count Tokens and Estimate LLM API Costs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#E-commerce`, `#LLM`, `#Business`, `#China`

---
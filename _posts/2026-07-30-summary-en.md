---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 38 items, 20 important content pieces were selected

---

1. [AI Startups Are Increasingly Withholding Research Publications](#item-1) ⭐️ 8.0/10
2. [Open-source engine runs Gemma 4 26B in 2GB RAM on M-series Mac](#item-2) ⭐️ 8.0/10
3. [Mitchell Hashimoto Launches Superlogical on libghostty](#item-3) ⭐️ 8.0/10
4. [Kimi Launches K3-256k with Half-Price 256K Context](#item-4) ⭐️ 8.0/10
5. [Long policy documents fail to govern LLM agents reliably](#item-5) ⭐️ 8.0/10
6. [AI Worm Replicates via Prompt Injection in Microsoft Word](#item-6) ⭐️ 8.0/10
7. [Matthew Green Highlights Post-Quantum Shift and AI Cryptanalysis](#item-7) ⭐️ 8.0/10
8. [Vulkan-based ncnn speeds ML inference on any GPU](#item-8) ⭐️ 8.0/10
9. [Russia charges Telegram founder Durov with aiding terrorism, issues warrant](#item-9) ⭐️ 8.0/10
10. [Hugging Face Models Widely Used for Deepfake Nudes, Report Finds](#item-10) ⭐️ 8.0/10
11. [Moonshot AI Raises $3.5B at $35B Valuation After K3 Model](#item-11) ⭐️ 8.0/10
12. [China drafts anti-cyberbullying law, targets AI-generated abuse](#item-12) ⭐️ 8.0/10
13. [OpenAI Offers Free Frontier Models to 100K Researchers](#item-13) ⭐️ 8.0/10
14. [ByteDance's biggest To B restructuring: Feishu merged into Doubao and Volcano Engine](#item-14) ⭐️ 8.0/10
15. [Vision Pro for architectural proportion assessment](#item-15) ⭐️ 7.0/10
16. [AI Companies Hiring Thousands of Electricians and Carpenters for Data Centers](#item-16) ⭐️ 7.0/10
17. [D. Richard Hipp on SQL replacing COBOL programmers](#item-17) ⭐️ 7.0/10
18. [Modular Data Centers: Solving Labor and Scalability Challenges](#item-18) ⭐️ 7.0/10
19. [China Telecom Halts Third-Party Online SIM Card Sales](#item-19) ⭐️ 7.0/10
20. [UK Regulator Proposes Apple Allow External App Store Payments](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI Startups Are Increasingly Withholding Research Publications](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) ⭐️ 8.0/10

A recent article highlights that top AI startups, including OpenAI and Anthropic, are publishing fewer research papers, reducing transparency in the field. This trend threatens the open science culture that has driven AI progress, potentially slowing innovation and making it harder for the broader community to build on their work. The article uses cumulative citations as a proxy for research significance, noting that OpenAI leads the chart, followed by companies like Megvii and Hugging Face, but overall publication numbers are declining.

hackernews · YeGoblynQueenne · Jul 29, 21:25 · [Discussion](https://news.ycombinator.com/item?id=49103285)

**Background**: Historically, AI research has thrived on open publication and sharing of code and data, with major breakthroughs often appearing as conference papers or preprints. However, as AI startups face competitive pressures and intellectual property concerns, many are choosing to keep their findings proprietary to maintain a competitive edge.

**Discussion**: Commenters share personal experiences: one notes that after struggling to publish in tier-1 journals, their startup switched to preprints; another deliberately avoids publishing to prevent companies like OpenAI and Anthropic from copying their work. A third commenter criticizes the 'blogification' of AI research, arguing that it leads to unverified claims and a lack of rigor.

**Tags**: `#AI research`, `#startups`, `#open science`, `#publications`

---

<a id="item-2"></a>
## [Open-source engine runs Gemma 4 26B in 2GB RAM on M-series Mac](https://github.com/drumih/turbo-fieldfare) ⭐️ 8.0/10

A developer released TurboFieldfare, an open-source inference engine written in Swift and Metal that runs the 4-bit quantized Gemma 4 26B-A4B-IT model on any M-series Mac using only about 2 GB of RAM by streaming routed experts from SSD. This breakthrough enables running large language models on low-memory devices, significantly expanding accessibility for on-device AI, especially for Mac users with limited RAM. It demonstrates a practical approach to overcoming memory constraints without sacrificing performance, achieving 5-35 tok/s depending on the Mac model. The model's 4-bit weights occupy about 14 GB, but TurboFieldfare keeps only the shared part and KV cache in RAM, streaming experts from SSD using a small expert cache and bounded parallel pread. It currently generates 5-6 tok/s on an 8 GB M2 MacBook Air and 31-35 tok/s on an M5 MacBook Pro, and includes an experimental OpenAI-compatible server with streaming and tool calls.

hackernews · gitpusher42 · Jul 29, 15:05 · [Discussion](https://news.ycombinator.com/item?id=49098510)

**Background**: Mixture-of-Experts (MoE) models like Gemma 4 use multiple sub-networks (experts) and activate only a few per token via a gating network, reducing computation. KV cache stores intermediate key-value states from previous tokens to speed up inference. 4-bit quantization reduces model weight precision to 4 bits, cutting memory usage. TurboFieldfare exploits MoE's sparsity by streaming experts from SSD rather than loading all weights into RAM.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/not-lain/kv-caching">KV Caching Explained: Optimizing Transformer Inference Efficiency</a></li>
<li><a href="https://arxiv.org/pdf/2103.13630">A Survey of Quantization Methods for Efcient</a></li>

</ul>
</details>

**Discussion**: Community members praised the novel approach, with one user noting the efficiency of not loading the entire model into memory. Another user provided a workaround to compile on older macOS versions. A comparison to plain mmap in llama.cpp was raised, highlighting the synchronized SSD reads with inference activity as a key differentiator. Another developer with a related DiffusionGemma project expressed interest in collaboration.

**Tags**: `#on-device AI`, `#inference engine`, `#Mac`, `#Gemma`, `#model streaming`

---

<a id="item-3"></a>
## [Mitchell Hashimoto Launches Superlogical on libghostty](https://www.superlogical.com/) ⭐️ 8.0/10

Mitchell Hashimoto announced Superlogical, a company that builds terminal applications on the open-source libghostty library, with a commitment to upstream contributions. This marks a sustainable open-source business model where the founder transfers the core project to a non-profit and builds a commercial product on top, potentially inspiring similar approaches in the developer tools ecosystem. Ghostty's terminal core, libghostty, is MIT-licensed and available to all; Superlogical will use it as a public building block and continue to send improvements upstream.

hackernews · yan · Jul 29, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49098965)

**Background**: Ghostty is a fast, feature-rich terminal emulator that uses platform-native UI and GPU acceleration, built in Zig. libghostty is a cross-platform, zero-dependency C and Zig library that provides terminal emulation functionality. Mitchell Hashimoto is the creator of Ghostty and co-founder of HashiCorp.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty-org/ghostty: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.</a></li>
<li><a href="https://ghostty.org/docs/about">About Ghostty</a></li>

</ul>
</details>

**Discussion**: Commenters praised the open-source business model, with one noting the transfer of Ghostty to a non-profit and building Superlogical as an open-source dependency. Some drew parallels to agentic multiplexers and historical technologies like OLE, while a few criticized the cryptic title.

**Tags**: `#terminals`, `#open-source`, `#company`, `#ghostty`, `#mitchell-hashimoto`

---

<a id="item-4"></a>
## [Kimi Launches K3-256k with Half-Price 256K Context](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 8.0/10

Moonshot AI released Kimi K3-256k, a lower-cost variant of the K3 model with a 256k-token context window at half the price of the full 1M-token version. This pricing change makes long-context AI more accessible for developers and applications that do not need the full 1M-token window, potentially expanding use cases in code analysis and document processing. The K3-256k model is the same underlying model as K3 (1M) but with a hard context cutoff at 256k tokens, consuming roughly half the quota. It is not quantized; only the context length differs.

hackernews · monneyboi · Jul 29, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49101852)

**Background**: Context window refers to the number of tokens (roughly words or subwords) an AI model can process at once; larger windows allow handling longer documents but incur higher computational costs. Kimi K3 is Moonshot AI's flagship model with 2.8 trillion parameters and a 1M-token context, using hybrid linear attention. The new K3-256k variant offers a cost-effective option for users who need less than full context.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://www.userightai.com/ai-context-window-comparison">AI Context Window Comparison 2026 — Which Models Handle the Most Tokens ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the step pricing is similar to OpenAI's approach and is surprising as a hard cutoff rather than a smooth gradient. Some see the half-price reduction as massive for users under 256k, while others clarified it is an API-level change with the same model, not quantized.

**Tags**: `#AI`, `#models`, `#pricing`, `#context-length`

---

<a id="item-5"></a>
## [Long policy documents fail to govern LLM agents reliably](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

A new paper titled 'Handbook.md' empirically demonstrates that long policy documents fail to reliably govern LLM-based agents, highlighting a fundamental limitation of current long-context models. This finding has direct implications for AI agent deployment and safety, as practitioners often rely on lengthy policy documents to guide agent behavior. The results align with anecdotal experiences and challenge the assumed reliability of long-context models in governance tasks. The paper shows that even state-of-the-art models struggle with policy adherence as document length increases, with community discussion attributing failures to KV cache quantization and limited working memory. Local inference is suggested as a partial remedy.

hackernews · spIrr · Jul 29, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49096969)

**Background**: Many large language models (LLMs) claim support for very long contexts (e.g., 1M tokens), but research shows they struggle to effectively use that information. The KV cache, which stores attention keys and values during inference, becomes heavily quantized at long lengths, degrading performance. Additionally, working memory constraints limit how many instructions a model can follow simultaneously, similar to human cognitive limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2404.02060">[2404.02060] Long-context LLMs Struggle with Long In-context ... Efficient Solutions For An Intriguing Failure of LLMs: Long ... Efficient Solutions For An Intriguing Failure of LLMs: Long ... [2510.05381] Context Length Alone Hurts LLM Performance ... LLMs and Long Contexts: Where It Starts to Go Wrong Evaluating Long Context Lengths in LLMs: Challenges and ... Efficient Solutions For An Intriguing Failure of LLMs: Long ...</a></li>
<li><a href="https://aclanthology.org/2025.coling-main.128/">Efficient Solutions For An Intriguing Failure of LLMs: Long ...</a></li>

</ul>
</details>

**Discussion**: Community comments largely agree with the findings, with users sharing anecdotal evidence that Claude ignores long instructions over time. Discussions highlight KV cache quantization, poor samplers, and working memory limits as root causes. Some argue that local inference mitigates the issue, while others note that achieving superhuman performance on such benchmarks would require extraordinary capabilities.

**Tags**: `#LLM`, `#AI safety`, `#long-context`, `#agent`, `#policy`

---

<a id="item-6"></a>
## [AI Worm Replicates via Prompt Injection in Microsoft Word](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 8.0/10

Security researcher Håkon Måløy demonstrated a self-replicating prompt injection worm that targets Microsoft Word's Copilot feature by embedding hidden instructions in documents, causing Copilot to propagate the malicious instructions to new documents. This novel attack turns AI assistants into unwitting accomplices in spreading malware, highlighting a critical security gap in AI-integrated productivity tools that could affect millions of users. The worm works by copying its hidden instructions into the output document, so any subsequent Copilot session using that document triggers the attack again, achieving self-replication without the attacker's original file.

rss · Simon Willison · Jul 29, 18:43

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs cause AI models to behave unintendedly. Self-replicating AI worms, like the Morris II proof-of-concept, use adversarial prompts to propagate across AI-powered systems. This attack combines both techniques in a Word document context.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/">AI Worms Explained: Adaptive Malware Threats - SentinelOne</a></li>

</ul>
</details>

**Tags**: `#prompt injection`, `#security`, `#AI`, `#Microsoft Word`, `#self-replicating worm`

---

<a id="item-7"></a>
## [Matthew Green Highlights Post-Quantum Shift and AI Cryptanalysis](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

Matthew Green, a renowned cryptographer, comments on the historic transition from traditional public-key algorithms like RSA and ECC to post-quantum algorithms such as HAWK, and emphasizes that this is an ideal time for AI to advance cryptanalysis. This transition is critical because quantum computers could break existing cryptography, and AI-driven cryptanalysis could either strengthen or undermine new standards, affecting global cybersecurity infrastructure. Matthew Green's insight highlights the convergence of AI and post-quantum cryptography at a pivotal moment. HAWK is a candidate for NIST's post-quantum signature standard, and Anthropic recently found a weakness in it, though the flaw is specific to HAWK and does not affect other lattice-based schemes. Green also references Impagliazzo's Minicrypt, a theoretical world where only symmetric cryptography is possible, as a possible outcome if AI undermines all hard problems.

rss · Simon Willison · Jul 29, 18:18

**Background**: Post-quantum cryptography aims to develop algorithms resistant to quantum computers, which would break widely used public-key systems like RSA and elliptic curve cryptography. NIST is currently running a competition to standardize these algorithms, with HAWK being a signature candidate. Impagliazzo's Five Worlds is a conceptual framework categorizing possible computational complexity worlds, where Minicrypt assumes one-way functions exist but public-key encryption does not. AI's potential role in cryptanalysis could help validate the security of new algorithms or expose vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.csoonline.com/article/4202920/mythos-takes-its-first-shot-at-post-quantum-cryptography.html">Anthropic finds weakness in Hawk post - quantum digital signature ...</a></li>
<li><a href="https://fanpu.io/blog/2022/impagliazzos-five-worlds/">Impagliazzo ' s Five Worlds, or The Computational... | Fan Pu Zeng</a></li>

</ul>
</details>

**Tags**: `#post-quantum cryptography`, `#AI cryptanalysis`, `#public-key algorithms`, `#Matthew Green`, `#cryptography standards`

---

<a id="item-8"></a>
## [Vulkan-based ncnn speeds ML inference on any GPU](https://www.reddit.com/r/MachineLearning/comments/1v9s4mz/vendoragnostic_ml_inference_on_production_edge/) ⭐️ 8.0/10

PostSlate uses ncnn's Vulkan backend to run ML models like face detection and embedding on any GPU without vendor-specific runtimes, achieving up to 10x speedup over ONNX CPU inference. This approach eliminates dependency on vendor-specific SDKs like CUDA, enabling seamless cross-platform ML inference on edge devices. It lowers deployment complexity and broadens the reach of on-device AI. ncnn is a high-performance neural network inference framework by Tencent, with no third-party dependencies. The Vulkan backend leverages compute shaders for GPU acceleration, and the Reddit post reports ArcFace R50 dropping from 30 ms (ONNX CPU) to 3 ms (ncnn Vulkan).

reddit · r/MachineLearning · /u/ppchaos · Jul 29, 10:22

**Background**: Edge ML inference often faces challenges with hardware diversity. Vendor-specific runtimes like CUDA limit portability. Vulkan is a cross-platform GPU API supported by all major GPU vendors, making it an ideal choice for vendor-agnostic inference. ncnn is an open-source framework optimized for mobile and embedded platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent/ncnn">GitHub - Tencent/ncnn: ncnn is a high-performance neural network inference framework optimized for the mobile platform · GitHub</a></li>
<li><a href="https://docs.vulkan.org/tutorial/latest/11_Compute_Shader.html">Compute Shader :: Vulkan Documentation Project</a></li>

</ul>
</details>

**Tags**: `#ML inference`, `#Vulkan`, `#edge devices`, `#cross-platform`, `#ncnn`

---

<a id="item-9"></a>
## [Russia charges Telegram founder Durov with aiding terrorism, issues warrant](https://www.interfax.ru/russia/1106228) ⭐️ 8.0/10

The Russian Federal Security Service (FSB) announced on July 29 that it has filed criminal charges against Telegram founder Pavel Durov under Article 205.1, Paragraph 1.1 of the Criminal Code (aiding terrorism) and placed him on the international wanted list. This marks a significant escalation in state action against a major tech founder, with implications for platform liability, privacy rights, and international legal norms. It could set a precedent for prosecuting technology executives for user-generated content on their platforms. The FSB alleges that Telegram's management refused to delete channels, groups, and bots used by Ukrainian intelligence and terrorist organizations to plan and coordinate sabotage, terrorist attacks, mass killings, and online fraud within Russia, resulting in numerous casualties and billions of rubles in damages.

telegram · zaihuapd · Jul 29, 05:56

**Background**: Telegram is an encrypted messaging platform founded by Pavel Durov, who left Russia in 2014 after disputes with authorities. The Russian government previously attempted to block Telegram in 2018 for refusing to hand over encryption keys. These new criminal charges represent a further intensification of the conflict between Durov and Russian state authorities.

**Tags**: `#Telegram`, `#Pavel Durov`, `#Russia`, `#terrorism`, `#tech regulation`

---

<a id="item-10"></a>
## [Hugging Face Models Widely Used for Deepfake Nudes, Report Finds](https://www.theverge.com/ai-artificial-intelligence/971723/hugging-face-nudify-deepfake-undress-women-children) ⭐️ 8.0/10

A report by AI Forensics released July 28 reveals that seven of the top nine image editing models on Hugging Face can easily generate non-consensual deepfake pornography, including targeting children, with minimal safeguards. This highlights critical gaps in platform governance for open-source AI, where abuse can flourish despite content policies, threatening privacy and safety especially for women and minors. The researchers set up a honeypot that received over 1,000 requests in seven days, of which 73% were sexually explicit and nearly 7% targeted children. No prompt engineering was needed to bypass restrictions.

telegram · zaihuapd · Jul 29, 08:20

**Background**: Hugging Face is a leading open-source platform for sharing machine learning models, including image generation tools. Deepfakes are realistic synthetic media created using AI, often used maliciously to create non-consensual explicit content. A honeypot is a decoy system that lures attackers to gather data on abuse.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Honeypot_(computing)">Honeypot (computing)</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#deepfake`, `#HuggingFace`, `#ethics`, `#content moderation`

---

<a id="item-11"></a>
## [Moonshot AI Raises $3.5B at $35B Valuation After K3 Model](https://www.bloomberg.com/news/articles/2026-07-29/china-s-moonshot-ai-passes-funding-goal-to-hit-35-billion-value) ⭐️ 8.0/10

Moonshot AI has raised $3.5 billion in a funding round, surpassing its initial target, achieving a post-money valuation of $35 billion. The round was driven by the breakthrough Kimi K3 model, which approaches the performance of frontier models from OpenAI and Anthropic. This massive funding round signals strong investor confidence in Chinese AI startups, challenging the dominance of US AI giants. Moonshot AI's rapid revenue growth and planned IPO could reshape the global AI landscape. The Kimi K3 model has 2.8 trillion parameters, uses a hybrid linear attention mechanism called Kimi Delta Attention, and was released with open-source weights. Moonshot AI has started a new funding round at a $50 billion pre-money valuation and plans an IPO in Hong Kong as early as this year.

telegram · zaihuapd · Jul 29, 10:12

**Background**: Moonshot AI is a Chinese AI company known for its large language models. The Kimi K3 is their flagship model, with 2.8 trillion parameters and a 1M-token context window. The release of K3 caused a 'DeepSeek moment' — a reference to when DeepSeek's R1 model briefly crashed US tech stocks by demonstrating competitive performance at low cost.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**Tags**: `#AI funding`, `#Moonshot AI`, `#large language models`, `#China AI`, `#startup valuation`

---

<a id="item-12"></a>
## [China drafts anti-cyberbullying law, targets AI-generated abuse](https://mp.weixin.qq.com/s/PrzKFhbwjgFEGBPADvFD6Q) ⭐️ 8.0/10

On July 29, 2026, China's Cyberspace Administration released a draft Anti-Cyberbullying Law for public comment, which for the first time includes specific provisions regulating AI-generated cyberbullying content. This marks a significant step in China's AI governance, addressing emerging harms from automated harassment. The law could reshape how tech platforms monitor and mitigate AI-driven abuse, affecting both domestic companies and global platforms operating in China. The 60-article draft introduces platform obligations for abuse detection, protective features, and multi-agency government coordination. Victims can seek injunctions and mental damages, reflecting a comprehensive approach to online violence.

telegram · zaihuapd · Jul 29, 10:59

**Background**: Cyberbullying involves repeated online attacks on reputation, privacy, or personal information. AI tools can amplify abuse through deepfakes, bot-driven harassment, and automated content generation. China has been tightening online governance, and this law extends protections to AI-generated harms.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cac.gov.cn/2026-07/29/c_1787072711938509.htm">国家互联网信息办公室关于《中华人民共和国反网络暴力法（征求意见稿...</a></li>
<li><a href="https://www.news.cn/politics/20260729/c7c9efa1710c45a78e443ced3a4def93/c.html">反网络暴力法公开征求意见 - 新华网</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#online violence`, `#China`, `#cybersecurity policy`, `#digital rights`

---

<a id="item-13"></a>
## [OpenAI Offers Free Frontier Models to 100K Researchers](https://openai.com/index/chatgpt-for-academic-researchers/) ⭐️ 8.0/10

On July 29, 2026, OpenAI announced the ChatGPT for Academic Researchers program, which will provide 100,000 researchers in science, math, and engineering with free access to its GPT-5.6 frontier models by 2027. The first cohort of 10,000 participants opens this summer. This initiative could significantly accelerate scientific discovery by giving researchers powerful AI tools for tasks like literature review, hypothesis testing, and grant writing. It also strengthens OpenAI's ties with academia and may influence other AI companies to offer similar programs. Participants can use GPT-5.6 models, including the Sol, Terra, and Luna variants, and invite up to four institutional collaborators. The workspace defaults to not using data for model training. The program is part of OpenAI's $250 million commitment to external research by 2027.

telegram · zaihuapd · Jul 30, 00:17

**Background**: GPT-5.6 is a family of large language models released by OpenAI on July 9, 2026, with three tiers of capability: Luna, Terra, and Sol. It was initially limited due to government restrictions but later made generally available. OpenAI has previously offered free access to researchers through programs like ChatGPT for Nonprofits, but this new program scales up dramatically.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/chatgpt-for-academic-researchers/">Accelerating scientific discovery with ChatGPT for Academic ...</a></li>
<li><a href="https://www.axios.com/2026/07/29/openai-academics-research-chatgpt-sol">OpenAI launches free AI access program for academic researchers</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#学术研究`, `#AI模型`, `#免费`, `#GPT-5.6`

---

<a id="item-14"></a>
## [ByteDance's biggest To B restructuring: Feishu merged into Doubao and Volcano Engine](https://news.qq.com/rain/a/20260730A03CAP00) ⭐️ 8.0/10

ByteDance has restructured its enterprise software business by merging the Feishu product team with the Doubao AI team to form a new 'Doubao Product Team', and integrating Feishu's marketing, sales, and customer service teams into Volcano Engine to create a 'Creativity Service Platform'. This is ByteDance's largest organizational change in its To B business since the company was founded, signaling a deeper integration of AI with enterprise collaboration and cloud services, which could reshape the competitive landscape of China's enterprise software market. Feishu's existing products and services will remain unchanged, but will deepen collaboration with Doubao on productivity scenarios; the Doubao Enterprise Edition, co-developed by both teams, is already being tested internally with some Feishu customers.

telegram · zaihuapd · Jul 30, 02:55

**Background**: Feishu is ByteDance's enterprise collaboration platform (known as Lark internationally), Doubao is ByteDance's leading AI chatbot and multimodal assistant with over 50 million active users, and Volcano Engine is ByteDance's cloud service platform offering AI and data analytics solutions. This restructuring aims to align ByteDance's To B offerings more closely with its AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lark_(software)">Lark (software) - Wikipedia</a></li>
<li><a href="https://moge.ai/product/doubao">豆包:Advanced multimodal AI platform by ByteDance offering... - MOGE</a></li>
<li><a href="https://baike.baidu.com/en/item/Volcano+Engine/1423148">Volcano Engine（ByteDance's cloud service platform）_Baiduwiki</a></li>

</ul>
</details>

**Tags**: `#ByteDance`, `#enterprise software`, `#AI`, `#restructuring`, `#Feishu`

---

<a id="item-15"></a>
## [Vision Pro for architectural proportion assessment](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 7.0/10

Christian Selig's article highlights using Apple Vision Pro for architectural visualization, allowing users to walk through 3D models of buildings to intuitively assess proportion and scale. This demonstrates a practical, productivity-focused use case for mixed reality headsets, offering significant value for architects, designers, and clients by enabling virtual walkthroughs before construction. The approach uses real-scale rendering and spatial computing, with tools like Rhino3D, Revit, and Enscape supporting the workflow. Both Apple Vision Pro and other headsets like Quest 3 and HTC Vive have been successfully used.

hackernews · robbiet480 · Jul 29, 20:39 · [Discussion](https://news.ycombinator.com/item?id=49102774)

**Background**: Apple Vision Pro is a mixed-reality headset released in 2024, running visionOS and supporting eye, hand, and voice control. Spatial computing merges digital models with the real world, enabling immersive architectural walkthroughs. This technology helps clients and designers evaluate scale and proportion intuitively, reducing costly design errors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Vision_Pro">Apple Vision Pro</a></li>
<li><a href="https://www.bulbapp.io/p/67f1f3c9-e06e-45ce-a930-b9f0dec96afc/the-future-of-architecture-through-the-lens-of-spatial-computing">The Future of Architecture Through the Lens of Spatial Computing</a></li>

</ul>
</details>

**Discussion**: Commenters share personal experiences: a design firm uses Quest 3 daily with Rhino3D/Revit; another used HTC Vive a decade ago with IrisVR. Suggestions include simulating sun angles for lighting analysis and, after construction, tracing wiring/plumbing through existing walls. Christian Selig is praised for earlier work on the Apollo Reddit client.

**Tags**: `#Vision Pro`, `#AR/VR`, `#Architecture`, `#Spatial Computing`, `#Design`

---

<a id="item-16"></a>
## [AI Companies Hiring Thousands of Electricians and Carpenters for Data Centers](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html) ⭐️ 7.0/10

AI companies are recruiting thousands of electricians, carpenters, and other tradespeople to build data centers, signaling a major shift in labor demand toward skilled trades. This trend highlights the tangible infrastructure required for AI expansion and could offer stable, well-paying careers for tradespeople, with implications for the broader economy and workforce development. The hiring surge is driven by the need for physical construction of data centers that house AI servers, and these jobs are not easily automated or outsourced.

hackernews · thm · Jul 29, 14:43 · [Discussion](https://news.ycombinator.com/item?id=49098198)

**Background**: Data centers are facilities that house large numbers of servers and computing equipment, essential for running AI models and cloud services. They require extensive electrical and carpentry work during construction. As AI demand grows, so does the need for new data centers, creating a boom in construction-related trades.

**Discussion**: Commenters expressed caution about the boom-and-bust nature of data center construction work, noting that career stability may be uncertain. Some welcomed the increased pay and opportunities for tradespeople.

**Tags**: `#labor`, `#data centers`, `#AI infrastructure`, `#trades`, `#economy`

---

<a id="item-17"></a>
## [D. Richard Hipp on SQL replacing COBOL programmers](https://simonwillison.net/2026/Jul/29/d-richard-hipp/#atom-everything) ⭐️ 7.0/10

D. Richard Hipp, creator of SQLite, drew a historical parallel between SQL's emergence displacing COBOL programmers and current trends in programming automation, suggesting that programming jobs evolve rather than disappear. This insight provides a reassuring perspective on the impact of AI and automation on software engineering careers, emphasizing that the role of programmers adapts rather than vanishes, which is highly relevant to ongoing debates about AI replacing jobs. The quote comes from a YouTube talk where Hipp simplifies the history: before SQL, querying large datasets required writing custom code, a job done by COBOL programmers; SQL allowed specifying queries declaratively, eliminating that need but shifting programmers to higher-level tasks.

rss · Simon Willison · Jul 29, 21:15

**Background**: COBOL was a dominant business programming language in the 1960s-80s, used extensively for data processing and reporting. Programmers had to manually write algorithms to traverse files and generate reports. SQL (Structured Query Language), invented in the 1970s and popularized by relational databases, allowed users to specify what data they wanted without writing procedural code, drastically reducing the effort needed for data retrieval tasks.

**Tags**: `#sql`, `#d-richard-hipp`, `#career`, `#automation`, `#software-history`

---

<a id="item-18"></a>
## [Modular Data Centers: Solving Labor and Scalability Challenges](https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters) ⭐️ 7.0/10

A Semianalysis article explores how modularization, akin to LEGO construction, is being adopted to address labor shortages and scalability issues in modern data centers. As data center demand surges due to AI and cloud computing, traditional construction cannot keep up; modularization offers faster deployment and reduced reliance on skilled labor, which is critical for the infrastructure industry. Modular data centers use prefabricated modules (power, cooling, IT) built in factories and assembled on-site, reducing construction time from months to weeks. This approach also enables repeatable designs and easier scalability.

rss · Semianalysis · Jul 29, 22:09

**Background**: Traditional data center construction faces labor shortages, high costs, and long timelines. Modularization, already used in other industries like healthcare, applies prefabrication to data centers, delivering speed, cost predictability, and quality. Companies like Schneider Electric and Vertiv offer prefabricated modular solutions for high-density AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://encoradvisors.com/modular-data-center/">The Modular Data Center Ultimate Guide [2025] - ENCOR Advisors</a></li>
<li><a href="https://www.moduledge.com/blog/modular-data-center-guide">Modular Data Center Guide: Types & When It Wins | ModulEdge</a></li>
<li><a href="https://www.se.com/us/en/product-category/7550-prefabricated-data-center-modules/">Prefabricated Data Center Modules - Schneider Electric USA</a></li>

</ul>
</details>

**Tags**: `#datacenters`, `#modularization`, `#infrastructure`, `#labor`, `#construction`

---

<a id="item-19"></a>
## [China Telecom Halts Third-Party Online SIM Card Sales](https://www.189.cn/web/notice/detail?order=1&amp;offerCode=519526800001&amp;provinceCode=600304) ⭐️ 7.0/10

China Telecom announced on July 31 that starting August 1, it will no longer sell SIM cards through third-party internet channels. A community member discovered the official notice on the company's website. This policy shift by a major state-owned telecom could significantly alter the online distribution landscape for SIM cards in China, affecting e-commerce platforms and potentially impacting fraud prevention or channel control strategies. The notice bears an effective date of August 1 and was posted on July 31, but a community member also found another link with a date of July 29 and a different province code, suggesting possible local variations or corrections.

telegram · zaihuapd · Jul 29, 12:45

**Background**: China Telecom is one of China's three major state-owned telecom operators. Third-party internet channels, such as e-commerce platforms like Taobao or JD.com, have been common outlets for selling SIM cards. This move may be part of broader efforts to regulate online sales and reduce fraud.

**Discussion**: Community members discovered the notice and noted a discrepancy: another similar notice was dated July 29 with a different province code, raising speculation about localized implementation or earlier versions.

**Tags**: `#China Telecom`, `#Telecommunications`, `#Regulation`, `#Internet Sales`, `#Policy Change`

---

<a id="item-20"></a>
## [UK Regulator Proposes Apple Allow External App Store Payments](https://www.macrumors.com/2026/07/29/app-store-uk-rules-highly-intrusive/) ⭐️ 7.0/10

The UK Competition and Markets Authority (CMA) has proposed requiring Apple to allow developers to steer users to external payment methods, reducing reliance on Apple's in-app purchase system. Apple has responded that the proposal is 'highly intrusive' and amounts to price regulation. This regulatory move could reshape App Store economics by lowering the 30% commission developers pay, potentially leading to lower prices for consumers. It also sets a precedent for other jurisdictions like the EU's Digital Markets Act, influencing global app store regulation. The CMA's proposed Conduct Requirements would allow developers to include links to external payment options, but Apple could still charge a 'fair and reasonable' fee lower than current commissions. The proposal also applies to Google, and the CMA is still reviewing responses before a final decision.

telegram · zaihuapd · Jul 30, 02:10

**Background**: Apple's App Store requires developers to use its in-app purchase system, with commissions of up to 30% on digital goods and services. Critics argue this stifles competition and inflates prices for consumers. The UK's new digital markets competition regime, effective since January 2025, designates Apple and Google as having 'strategic market status' in mobile ecosystems, subjecting them to tailored conduct requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gov.uk/government/news/cma-secures-commitments-from-apple-and-google-to-improve-fairness-in-app-store-processes-and-enhance-ios-interoperability">CMA secures commitments from Apple and Google to improve ...</a></li>
<li><a href="https://www.gov.uk/cma-cases/investigation-into-apple-appstore">Investigation into Apple AppStore - GOV.UK UK Consumers to CMA: Don't Put App Store Safety and Security ... Improving the way Apple and Google deliver app store services ... Apple says UK App Store proposal amounts to price regulation UK watchdog plans to break Apple and Google’s ‘effective ... Apple Says UK App Store Steering Rules Would Be 'Highly ...</a></li>
<li><a href="https://ccianet.org/news/2026/07/uk-consumers-to-cma-dont-put-app-store-safety-and-security-at-risk/">UK Consumers to CMA: Don't Put App Store Safety and Security ...</a></li>

</ul>
</details>

**Tags**: `#App Store`, `#regulation`, `#antitrust`, `#UK`, `#payments`

---
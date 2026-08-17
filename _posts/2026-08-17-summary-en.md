---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
lang: en
---

> From 34 items, 20 important content pieces were selected

---

1. [Stripe Acquires AI Gateway OpenRouter in $7B Deal](#item-1) ⭐️ 9.0/10
2. [Anthropic makes Claude system prompts public for community analysis](#item-2) ⭐️ 8.0/10
3. [Qwen 3.8 27B Impresses But Default Reasoning Overthinks](#item-3) ⭐️ 8.0/10
4. [PJM's $12 Billion Modeling Mistake Risks Repeated Ratepayer Waste](#item-4) ⭐️ 8.0/10
5. [SSOG-Attention: Sum of Separable Gaussians offers sub-quadratic attention](#item-5) ⭐️ 8.0/10
6. [Anthropic Q2 Preliminary Revenue Tops $11.5B, Up 14x Year Over Year](#item-6) ⭐️ 8.0/10
7. [Embedded Engineer Defends RISC-V for Developing-World Accessibility](#item-7) ⭐️ 7.0/10
8. [Frontier Models Get 'Dumber' by Design: Knowledge Moves Out of Weights](#item-8) ⭐️ 7.0/10
9. [AI Credit Resale Economy Emerges via Token Brokers](#item-9) ⭐️ 7.0/10
10. [Firefox for iOS Gains Native Ad Blocker Feature](#item-10) ⭐️ 7.0/10
11. [Cloudflare silently injects Web Analytics when nameservers switch](#item-11) ⭐️ 7.0/10
12. [St. Lucie Nuclear Unit 1 Manually Shutdown After 3 Control Rods Drop](#item-12) ⭐️ 7.0/10
13. [Revisiting ECA: Cross-Channel Interaction Hypothesis Is Flawed](#item-13) ⭐️ 7.0/10
14. [Dario Amodei: AI Distrust Reflects Broader Crisis in Institutions](#item-14) ⭐️ 6.0/10
15. [SineKAN Introduces Sinusoidal Activations for Kolmogorov-Arnold Networks](#item-15) ⭐️ 6.0/10
16. [Seeking Solutions for Long-Range Recall in Linear Attention](#item-16) ⭐️ 6.0/10
17. [US Tells Allies: Sign Pax Silica or Face AI Exclusion](#item-17) ⭐️ 6.0/10
18. [AI Tool Flags Telegram Piracy, Leading to 524 Channel Takedowns](#item-18) ⭐️ 6.0/10
19. [SafePal Discloses Data Breach Affecting Nearly 40,000 Customers](#item-19) ⭐️ 6.0/10
20. [How to Enable a 1M Token Context Window in Codex with GPT-5.6 Sol](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Stripe Acquires AI Gateway OpenRouter in $7B Deal](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 9.0/10

Stripe has closed a deal to acquire OpenRouter, an AI model routing and API gateway platform, for over $7 billion. The acquisition was reported around August 16, 2026, and represents one of the largest AI infrastructure deals involving a payments company. This deal signals that AI model access is becoming core payment and API infrastructure, as Stripe positions itself as the middleman for both financial transactions and LLM token usage. It could reshape how developers buy AI compute and how AI labs route payments, with major implications for AWS Bedrock, OpenAI, and other providers. OpenRouter reportedly raised money at a $1.3 billion valuation only a few months before the $7 billion exit. The deal also follows OpenAI's decision to move its payment processing from Stripe to Adyen, and OpenRouter controls a large share of AI model API payment volume for major labs.

hackernews · zacharyozer · Aug 16, 20:31 · [Discussion](https://news.ycombinator.com/item?id=49323381)

**Background**: OpenRouter is a unified API gateway and marketplace that routes a single OpenAI-compatible request across more than 400 large language models and AI models from over 60 providers, automatically selecting hosts for cost, speed, and reliability while consolidating billing into one account. In the broader ecosystem, AI model routing is a critical infrastructure pattern that includes cost-optimized model selection, load balancing, and unified API gateways that abstract away provider complexity. Stripe, known as one of the best API companies in the world, has built its business abstracting financial rails for payments and is now extending that model to LLM tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/openrouter">OpenRouter API and Models | OpenRouter</a></li>
<li><a href="https://www.knolli.ai/post/what-is-openrouter">What Is OpenRouter? A Practical Guide to AI Model Routing</a></li>
<li><a href="https://aiwiki.ai/wiki/openrouter">OpenRouter - AI Wiki</a></li>

</ul>
</details>

**Discussion**: Commenters largely saw the deal as a strategic move by Stripe to own the 'rails' for LLMs, not just payments, and to secure AI-related payment volume after losing OpenAI's business to Adyen. Some questioned how a 'middleman for API calls' could be worth more than Lyft or Dolby, while others noted network effects, switching costs, and Stripe's distribution as key value drivers. Several also pointed out the rapid jump from a $1.3 billion valuation to a $7 billion exit in just a few months and hoped employees shared in the outcome.

**Tags**: `#AI`, `#Acquisitions`, `#Payments`, `#OpenRouter`, `#Stripe`

---

<a id="item-2"></a>
## [Anthropic makes Claude system prompts public for community analysis](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic has published the official system prompts for Claude models in its platform release notes, making the default prompts visible to anyone. The release enables developers and researchers to inspect the exact instructions given to Claude and to track how those prompts change across model versions. This is a significant step toward transparency in commercial AI systems, which usually keep system prompts secret. It helps developers understand model behavior, reproduce results, and adjust their applications when prompts change unexpectedly. Simon Willison created a git commit history of the prompts to make diffs easier to inspect, highlighting notable additions between Opus 4.8 and Opus 5. Since system prompts are prepended to every API call and consume context-window tokens, their length and content directly affect cost and model behavior.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**Background**: System prompts are instruction blocks prepended to every request sent to an LLM; they define the model's behavior, personality, constraints, and task context. They consume part of the context-window token budget on every call, so prompt length and clarity can materially affect performance. Many AI labs keep these prompts proprietary, so Anthropic's public release notes are unusual and give the community a rare inside look.

<details><summary>References</summary>
<ul>
<li><a href="https://hackernoon.com/system-prompts-under-the-hood-how-llms-learn-to-follow-instructions">System Prompts Under the Hood: How LLMs Learn to... | HackerNoon</a></li>
<li><a href="https://docs.runanywhere.ai/web/llm/system-prompts">System Prompts - RunAnywhere Documentation</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices">Prompting best practices - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Commenters generally welcomed the transparency: simonw built a git-based change tracker for the prompts, and ololobus noted that some housekeeping instructions (like Claude checking whether an image is really attached) resemble generic common sense rather than true reasoning. Others raised concerns, with SwellJoe arguing the prompts are longer than warranted and that models often perform better with shorter, less distracting instructions; a separate off-topic comment alleged the forum removes AI-critical stories.

**Tags**: `#Claude`, `#system prompts`, `#Anthropic`, `#AI transparency`, `#LLM`

---

<a id="item-3"></a>
## [Qwen 3.8 27B Impresses But Default Reasoning Overthinks](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

Qwen 3.8 27B, an Apache 2 licensed vision-capable 27B parameter LLM from Alibaba's Qwen lab, was released and shows benchmark gains over both Qwen 3.6 27B and the closed-weight Qwen 3.7-Plus. Simon Willison's testing found the default 'xhigh' reasoning effort causes the model to spend excessive tokens and time overthinking even simple prompts. This release is significant because a strong open-weight 27B model that can run on a laptop narrows the gap with closed-weight models and gives developers a versatile local option. The default overthinking behavior highlights the importance of reasoning-effort controls in practical deployments, affecting latency and cost on consumer hardware. The model supports a configurable 'reasoning_effort' parameter with xhigh, medium, and low levels, and defaults to xhigh. Simon Willison ran a 17GB Q4_K_M quantized build on an M5 Max MacBook Pro and NVIDIA DGX Spark, and found that the default context limit of 8,192 tokens was exhausted by reasoning; increasing to the full 262,144 tokens allowed a complex SVG generation to take 21 minutes and 22,276 reasoning tokens.

rss · Simon Willison · Aug 16, 22:00

**Background**: Qwen is a family of large language models developed by Alibaba Cloud, first launched in April 2023 under the name Tongyi Qianwen. Open-weight models like Qwen 3.8 27B are popular for local deployment because they can run on consumer hardware, and reasoning-effort settings allow users to trade accuracy against speed and compute costs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/why-large-language-models-overthink-what-google-deepminds-njagi-3xonf">Why Large Language Models Overthink: What Google...</a></li>

</ul>
</details>

**Tags**: `#qwen`, `#llm`, `#open-source`, `#local-models`, `#ai`

---

<a id="item-4"></a>
## [PJM's $12 Billion Modeling Mistake Risks Repeated Ratepayer Waste](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

A SemiAnalysis investigation reports that a modeling mistake in PJM's electricity market wasted $12 billion of ratepayers' money. The report warns that PJM is pursuing the same flawed modeling approach again, putting consumers at further risk. It exposes a systemic flaw in how the largest U.S. grid operator models reliability and procures capacity. Since PJM serves about 67 million customers, repeated mistakes could waste billions more and undermine trust in electricity market design. The report specifically refers to bad grid-planning and capacity-market models, not AI or machine-learning models. PJM operates separate day-ahead, real-time energy, and capacity markets, and the alleged waste stems from how those planning models are used.

rss · Semianalysis · Aug 16, 22:27

**Background**: PJM Interconnection is the largest power grid operator in the United States, serving about 67 million customers across a region stretching from Chicago to New Jersey. In PJM's wholesale markets, utilities buy electricity in energy markets and also pay for capacity to ensure enough generation will be available during future high-demand periods. A capacity-market modeling mistake can lead to over-procurement or mispricing of future supply, and those costs are ultimately passed on to ratepayers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PJM_Interconnection">PJM Interconnection - Wikipedia</a></li>
<li><a href="https://www.pjm.com/markets-and-operations/energy.aspx">PJM - Energy Market</a></li>
<li><a href="https://www.ferc.gov/understanding-wholesale-capacity-markets">Understanding Wholesale Capacity Markets | Federal Energy Regulatory Commission</a></li>

</ul>
</details>

**Tags**: `#energy`, `#grid`, `#modeling`, `#PJM`, `#infrastructure`

---

<a id="item-5"></a>
## [SSOG-Attention: Sum of Separable Gaussians offers sub-quadratic attention](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

SSOG-Attention replaces standard scaled dot-product attention (SDPA) with a sum of separable Gaussians, cutting complexity from O(N²·d) to O(N√N·d). Experiments show it outperforms SDPA on CIFAR-100 and matches it on ImageNet while converging faster. This work directly tackles the quadratic compute and memory bottleneck that limits transformer scalability, making it relevant for vision transformers and long-sequence applications. If validated widely, sub-quadratic attention like SSOG could enable more efficient large-scale models. SSOG learns a few Gaussian atoms per attention head and steers them geometrically based on the query token, without scoring every token. Because the atoms factorize into a separable sum, the method is faster and more memory-efficient as input scale grows; code and a blog post are available online.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**Background**: Standard scaled dot-product attention (SDPA) computes similarity scores between all query and key tokens, leading to O(N²·d) time and memory in transformers. To overcome this, many sub-quadratic attention variants have been proposed, often using linearization or sparsity, but many lack rigorous error guarantees. SSOG instead learns a geometric attention field made of separable Gaussians, avoiding explicit pairwise scoring altogether.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/4rtemi5/ssog/blob/main/README.md">ssog/README.md at main · 4rtemi5/ssog · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2209.04881">[2209.04881] On The Computational Complexity of Self-Attention</a></li>

</ul>
</details>

**Discussion**: Early discussion welcomes the idea but raises the key question of what long-range recall might be sacrificed for speed. One commenter notes it is a path worth testing while questioning the trade-off between efficiency and the ability to retrieve distant information.

**Tags**: `#efficient-attention`, `#machine-learning`, `#transformers`, `#computer-vision`, `#sub-quadratic`

---

<a id="item-6"></a>
## [Anthropic Q2 Preliminary Revenue Tops $11.5B, Up 14x Year Over Year](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic reported preliminary second-quarter revenue above $11.5 billion, a 14-fold year-over-year increase from $787 million, and turned adjusted operating profit positive. The figures are preliminary and subject to revision, with the company reportedly preparing for a possible IPO as early as this fall. This marks a major business milestone for Anthropic, showing that leading AI labs can convert surging demand into large-scale revenue and positive operating profit. It also strengthens the case for a high-profile IPO, which would give public investors a purer-play large AI model company. Sequential growth was also strong: revenue rose from $4.73 billion in Q1 2026 to more than $11.5 billion in Q2. The reported figure is preliminary, so final results could change before any IPO-related disclosures.

telegram · zaihuapd · Aug 16, 07:26

**Background**: Anthropic is the AI company behind the Claude family of large language models, a major competitor to OpenAI and other foundation-model labs. Its revenue expansion reflects strong enterprise adoption of AI assistants and API offerings; adjusted operating profit typically excludes stock-based compensation and other one-off items, giving a clearer view of core operations. The company has been widely reported to be exploring an IPO in 2026.

**Tags**: `#Anthropic`, `#AI`, `#revenue`, `#IPO`, `#business`

---

<a id="item-7"></a>
## [Embedded Engineer Defends RISC-V for Developing-World Accessibility](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

In a blog post on rvembedded.com, an embedded engineer from the developing world responds to the critique 'RISC-V They Should Have Known Better,' arguing that RISC-V's low cost and accessibility make it uniquely valuable despite performance and fragmentation concerns. This response brings a rarely heard perspective from developers in developing countries into the RISC-V debate, highlighting how cost and supply-chain barriers shape architectural choices. It underscores that RISC-V's impact on embedded computing cannot be judged by high-performance metrics alone. The author contrasts a ten-cent RISC-V part with a one-dollar alternative, arguing the price difference matters greatly in his region, while noting shipping costs of $60–$200 for small orders. The original critique focused on RISC-V's relative performance against ARM64 and fragmentation from optional ISA extensions.

hackernews · Narishma · Aug 16, 17:01 · [Discussion](https://news.ycombinator.com/item?id=49321717)

**Background**: RISC-V is an open-standard instruction set architecture (ISA) that anyone can use to design processors without paying licensing fees, making it attractive for embedded systems. Unlike ARM, RISC-V allows designers to add or remove instructions for their specific applications, which can lead to fragmentation across implementations. To address this, RISC-V International has introduced standard base profiles such as RVA22 and RVA23 for Linux-class CPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://riscv.org/specifications/ratified/">Ratified Specifications - RISC - V International</a></li>
<li><a href="https://www.stromasys.com/resources/all-about-the-risc-v-processors/">RISC - V Processors: The Comprehensive Guide (2026)</a></li>
<li><a href="https://www.cnx-software.com/2019/03/10/risc-v-compliance-tests-risc-v-fragmentation/">RISC - V Compliance Tests Aim to Address RISC - V Fragmentation</a></li>

</ul>
</details>

**Discussion**: Commenters point out that the author appears to speak past the original critique, since the original piece focused on RISC-V's performance and binary-distribution issues rather than embedded cost advantages. Some question the consistency of the cost and shipping argument, while others draw historical parallels, suggesting RISC-V performance will eventually catch up with ARM and x86 as x86 once caught up with RISC workstations.

**Tags**: `#RISC-V`, `#embedded systems`, `#hardware`, `#cost analysis`, `#developing countries`

---

<a id="item-8"></a>
## [Frontier Models Get 'Dumber' by Design: Knowledge Moves Out of Weights](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 7.0/10

The article argues that frontier LLMs are intentionally trading memorized facts for tool-based retrieval, making them appear dumber on recall benchmarks while potentially reducing hallucinations. It predicts that model-card knowledge cutoffs may eventually disappear as weights only retain slowly changing reasoning. This shift could reshape how the industry evaluates and builds LLMs, moving away from 'bigger is smarter' toward modular, tool-augmented systems with pluggable knowledge. It affects anyone relying on factual recall or purchasing models by benchmark scores, and raises new questions about what capability really means. The article cites SimpleQA, a factual recall benchmark where Gemini 2.5 Pro scored 53%, to illustrate the limits of parametric memory. Critics point out that the post is AI-generated and the benchmarks are outdated, since Gemini 2.5 Pro is now sixteen months old.

hackernews · hruvhwe · Aug 16, 19:04 · [Discussion](https://news.ycombinator.com/item?id=49322695)

**Background**: Large language models can store knowledge in two ways: parametric memory, which bakes facts into weights during training, and non-parametric memory, which retrieves information from external databases at inference time. Retrieval-augmented generation (RAG) is the dominant technique for the latter, letting models consult an authoritative knowledge base before answering. Tool use extends this idea by letting models call external functions and agents to fetch, compute, or act on data. This background is necessary because the article's core argument centers on shifting from parametric knowledge to these external mechanisms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG ? - Retrieval - Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://lawrence-emenike.medium.com/a-straightforward-explanation-of-parametric-vs-non-parametric-memory-in-llms-f0b00ac64167">A Straightforward explanation of Parametric vs. Non-Parametric Memory in LLMs | by Lawrence Emenike | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some praise the essay and note emerging tiny tool-calling LLMs like Cactus's 14MB 'Needle' model that avoid storing large amounts of world knowledge, while others question the feasibility of fully decoupling knowledge from reasoning. One top commenter calls the post AI-generated and out of date, pointing to newer models and stale benchmarks; another argues that factual knowledge is inseparable from grounded reasoning.

**Tags**: `#AI`, `#LLM`, `#knowledge bases`, `#tool use`, `#model design`

---

<a id="item-9"></a>
## [AI Credit Resale Economy Emerges via Token Brokers](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

A secondary market has emerged where 'token brokers' buy unused AI API credits from startups and resell them at substantial discounts, a trend highlighted by researcher Matt Lenhard. Dedicated marketplaces such as AICreditmart.com now facilitate these trades across providers like OpenAI, Anthropic, and Google. This gray market undermines AI providers' pricing and terms of service, while exposing buyers to security and trust risks. It signals the AI ecosystem is maturing to the point where inference credits are treated as fungible, arbitrageable assets. Reselling AI credits typically violates the issuing platform's terms of service, and brokers often operate as relays or proxies to hide account origins. Buyers typically save 20-40%, but face risks including account hacking, data leakage, and no guarantee that the model accessed is the one advertised.

hackernews · mlenhard · Aug 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=49320611)

**Background**: AI API credits are prepaid usage units for LLM providers, measured in tokens, where each token represents roughly three-quarters of a word. Providers often grant free credits to developers for onboarding or promotional purposes, and startups may accumulate more than they can use. Token brokers buy these idle credits and resell them at a discount, creating a secondary market reminiscent of gift-card arbitrage or loyalty-point resale. This activity is considered a gray market because it violates the platforms' terms of service while not being explicitly illegal.

<details><summary>References</summary>
<ul>
<li><a href="https://www.machucavalley.tech/blog/ai-credit-resale-economy-emerging-market/">The New Gold Rush: Welcome to the AI Credit Resale Economy</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-08-17-the-emergence-of-ai-token-brokers-inside-the-growing-secondary-market-for-llm-inference-credits">AI Token Brokers: The New Secondary Market for LLM Credits</a></li>
<li><a href="https://aicreditmart.com/">AICreditmart.com - AICreditMart - Buy & Sell AI Credits</a></li>

</ul>
</details>

**Discussion**: Commenters had mixed reactions: some found model distillation via cheap credits a fascinating angle, while others dismissed the trust model as dangerous, noting that buyers must rely on unvetted third parties. Several noted the research was too shallow, pointing to far larger token-resale economies on platforms like linux.do and nodeseek.com, and questioned how a buyer can verify they are truly getting the model they paid for.

**Tags**: `#AI`, `#API credits`, `#gray market`, `#token brokerage`, `#arbitrage`

---

<a id="item-10"></a>
## [Firefox for iOS Gains Native Ad Blocker Feature](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) ⭐️ 7.0/10

Firefox for iOS has introduced a built-in native ad blocker, allowing users to block ads without installing a separate extension. The feature covers ads on search engine results pages from Google, Bing, DuckDuckGo, and other providers. This update matters because iOS browsers have historically lacked the extension flexibility of desktop versions, making a native ad blocker a meaningful privacy improvement for iPhone and iPad users. It also signals Mozilla's continued investment in mobile privacy at a time when ad-blocking demand is high. The built-in blocker specifically targets ads shown on search engine results pages, including Google, Bing, and DuckDuckGo. Community members note that while uBlock Origin Lite for Safari remains the most capable iOS ad blocker, this native option reduces setup friction for Firefox users.

hackernews · pentagrama · Aug 16, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49319633)

**Background**: On iOS, all browsers are required to use Apple's WebKit engine, and browser extensions are far more restricted than on desktop. Content blocking on iOS is typically implemented through native APIs like the WebKit content blocker framework, which allow apps to block ads, trackers, and other unwanted content. Firefox Focus, a separate Mozilla browser for iOS, has included an ad-blocking feature since the late 2010s, and this new addition brings a similar capability into the main Firefox app.

<details><summary>References</summary>
<ul>
<li><a href="https://deepwiki.com/huntingcat/apple-browsers/2.3-content-blocking">Content Blocking | huntingcat/apple-browsers | DeepWiki</a></li>
<li><a href="https://gitlab.com/GhenadieP/ABPKit">WebKit content blocker management framework for iOS and macOS...</a></li>

</ul>
</details>

**Discussion**: Community reactions were mixed: several users pointed out that uBlock Origin Lite for Safari remains a stronger ad blocker, while others reminded everyone that Firefox Focus already offered a system-wide ad blocker via iOS content blockers. Some commenters expressed hope for Gecko engine support in future iOS releases and frustration over iOS extension limitations, which led them to alternatives like Orion.

**Tags**: `#Firefox`, `#iOS`, `#adblock`, `#privacy`, `#browser`

---

<a id="item-11"></a>
## [Cloudflare silently injects Web Analytics when nameservers switch](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

A user reports that after switching nameservers to Cloudflare to serve an R2 bucket from a custom subdomain, Cloudflare silently injected its Web Analytics JavaScript snippet into their HTML-only site. The snippet could only be disabled by manually adding the site to the Analytics dashboard and then opting out. This matters because DNS and CDN infrastructure providers have privileged access to traffic, and silently modifying responses raises serious consent and transparency concerns for web developers and privacy-conscious site owners. It also underscores the need for explicit opt-in defaults and careful auditing of CDN features. The injected script is served from static.cloudflareinsights.com/beacon.min.js and includes a data-cf-beacon payload with a token. Users can block it by setting a Content-Security-Policy such as script-src 'self' to allow only scripts from specified origins; injection may occur only when Cloudflare proxies traffic, not for DNS-only setups.

hackernews · stagas · Aug 16, 17:49

**Background**: Switching nameservers to Cloudflare delegates a domain's DNS to Cloudflare, and if the domain is 'proxied' (orange cloud), HTTP/S requests pass through Cloudflare's edge, which can terminate TLS and modify responses. The user was enabling R2 bucket serving from a custom subdomain, which typically requires proxying through Cloudflare's CDN. Cloudflare Web Analytics uses a JavaScript beacon from static.cloudflareinsights.com, and this auto-injection behavior has been discussed in Cloudflare community threads and blog posts. A Content-Security-Policy can block such third-party scripts independently of Cloudflare's dashboard settings.

<details><summary>References</summary>
<ul>
<li><a href="https://notifire.in/infra/cloudflare-may-be-adding-code-to-your-website">Cloudflare Analytics Script Injected Without User Consent</a></li>
<li><a href="https://burgeonlab.com/blog/cloudflare-web-analytics-rum-injected-tracking-beacon-script-into-my-sites/">Cloudflare Auto Injected Tracking Scripts To My Sites</a></li>
<li><a href="https://developers.cloudflare.com/r2/buckets/public-buckets/">Public buckets · Cloudflare R2 docs</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed the injection is invasive and confirmed seeing the beacon script with SRI integrity attributes. One suggested a Content-Security-Policy meta tag to restrict scripts to self-hosted origins. Another user observed that domains set to DNS-only did not have Web Analytics enabled, suggesting injection may only happen when Cloudflare proxies traffic.

**Tags**: `#Cloudflare`, `#Privacy`, `#Analytics`, `#DNS`, `#Web Development`

---

<a id="item-12"></a>
## [St. Lucie Nuclear Unit 1 Manually Shutdown After 3 Control Rods Drop](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core) ⭐️ 7.0/10

Unit 1 at the St. Lucie nuclear power plant in Florida was manually shut down after three control rods unexpectedly dropped into the reactor core. The event prompted an investigation, with no reported release of radioactive material or off-site impact. Control rod drops are significant safety events at nuclear reactors because they affect reactivity control, even though US pressurized water reactors are designed to shut down safely. The high community engagement shows strong public interest in nuclear safety, highlighting the need for accurate understanding of reactor safety systems. Operators manually shut down the unit after three control rods inserted into the core, reducing reactivity. Community experts note that even a single fully inserted rod can drive a US PWR subcritical; this is distinct from a full scram, and a similar event in 2024 was traced to procedural and electrical issues.

hackernews · toomuchtodo · Aug 16, 15:16 · [Discussion](https://news.ycombinator.com/item?id=49320856)

**Background**: Control rods are made of neutron-absorbing material and are used in fission reactors to manage the chain reaction by adjusting reactivity. In a scram, all control rods are rapidly inserted into the core to stop fission; in PWRs this typically occurs within two to four seconds. US nuclear reactors are designed with multiple safety layers so they can shut down safely even if control rods drop accidentally.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scram">Scram - Wikipedia</a></li>
<li><a href="https://www.nuclear-power.com/nuclear-power/reactor-physics/reactor-operation/reactor-shutdown/">Reactor Shutdown | Condition & SCRAM | nuclear -power.com</a></li>

</ul>
</details>

**Discussion**: Comments generally downplayed the risk, explaining that dropped control rods are a known failure mode and US PWRs go subcritical with even one rod inserted. Some noted a similar 2024 event and its root cause, while others reflected on why nuclear incidents attract more attention than natural gas plant explosions.

**Tags**: `#nuclear energy`, `#reactor safety`, `#control rods`, `#infrastructure`, `#incident response`

---

<a id="item-13"></a>
## [Revisiting ECA: Cross-Channel Interaction Hypothesis Is Flawed](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

A Reddit post critically re-examines the Efficient Channel Attention (ECA) paper, arguing that its central hypothesis about cross-channel interaction is conceptually flawed. The author tests ECA on chess tablebase data and finds that a k=1 convolution, which ignores cross-channel interaction, performs nearly as well as k=3, challenging the paper's rationale. ECA has over 12,000 citations and is widely used, so if its core rationale is incorrect, it could shift attention mechanism design away from cross-channel interaction toward simpler per-channel gating. This critique highlights that empirical success does not validate the explanatory story, encouraging more rigorous analysis of popular architectures. In experiments on 6-piece chess endgame tablebases, ECA with k=3 achieved about 96.68% test accuracy versus about 96.61% for k=1, showing that the marginal benefit of cross-channel interaction is tiny. The author argues that applying a 1D convolution across the channel dimension treats channels like tabular data with no inherent topology, making the operation conceptually inappropriate.

reddit · r/MachineLearning · /u/arkuto · Aug 16, 10:13

**Background**: Channel attention mechanisms like Squeeze-and-Excitation (SE) adaptively recalibrate feature maps by learning per-channel weights. ECA proposed using a 1D convolution over the channel dimension to enable efficient cross-channel interaction, claiming this was key to its gains over SE. However, convolutions assume locality and translation invariance along a meaningful axis such as space or time, which is not true for the channel dimension. The author's chess tablebase experiments provide a unique benchmark because the training data can be sampled from the complete, unbiased problem distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA -Net: Efficient Channel Attention for Deep...</a></li>
<li><a href="https://arxiv.org/abs/1709.01507">[1709.01507] Squeeze-and-Excitation Networks - arXiv.org Squeeze-and-Excitation (SE) Block in PyTorch - codegenes.net Squeeze and Excitation (SE) Block - OpenGenus IQ Introduction to Squeeze-Excitation Networks | Towards Data ... Squeeze-and-Excitation Networks. Squeeze-and-Excitation block ... Squeeze-and-Excitation Networks | IEEE Conference Publication ...</a></li>
<li><a href="https://www.emergentmind.com/topics/efficient-channel-attention-eca-mechanisms">Efficient Channel Attention Mechanisms</a></li>

</ul>
</details>

**Tags**: `#Attention Mechanisms`, `#Deep Learning`, `#CNN`, `#Paper Critique`, `#Efficient Channel Attention`

---

<a id="item-14"></a>
## [Dario Amodei: AI Distrust Reflects Broader Crisis in Institutions](https://simonwillison.net/2026/Aug/16/dario-amodei/) ⭐️ 6.0/10

Anthropic CEO Dario Amodei pushed back against the idea that AI leaders' warnings caused public distrust, arguing it stems from a long-standing crisis of trust in companies, governments, and tech. He said the fix is actually delivering tangible benefits, such as curing cancer, not marketing campaigns. The comment reframes the AI backlash debate, shifting responsibility from risk communication to delivering proven benefits. It matters because it comes from a top AI CEO and affects how the industry handles public trust and AI adoption. Amodei acknowledged that the most accurate criticism of AI companies, including Anthropic, is that they have not yet delivered on their big promises to benefit the world. He rejected calls for a 'glitzy marketing campaign' and warned that claims like 'AI will cure cancer' now sound clichéd and deceptive.

rss · Simon Willison · Aug 16, 15:05

**Background**: Dario Amodei is the CEO of Anthropic, an AI company focused on safety and reliability, and he has frequently warned about AI risks. Public perception of AI has become increasingly negative, partly because of well-publicized warnings from senior AI figures. Amodei argues that this backlash is not primarily caused by those warnings but by a deeper trust deficit in institutions. His remarks were reposted by technology blogger Simon Willison.

**Tags**: `#AI`, `#trust`, `#Anthropic`, `#Dario Amodei`, `#public perception`

---

<a id="item-15"></a>
## [SineKAN Introduces Sinusoidal Activations for Kolmogorov-Arnold Networks](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

A paper titled 'SineKAN: Kolmogorov-Arnold Networks Using Sinusoidal Activation Functions' replaces the B-spline basis functions in KANs with sinusoidal activations. The work is available on arXiv, GitHub, and a peer-reviewed MDPI publication. This offers a simpler alternative to B-spline-based KANs while achieving competitive performance, potentially making KANs easier to implement and adopt. It contributes to the growing exploration of activation functions in neural architectures beyond traditional MLPs. The arXiv paper (2407.04149) is authored by Eric A. F. Reinhardt and two collaborators. The MDPI version (Mathematics, 13(19), 3157) is peer-reviewed, and the GitHub repository provides code.

reddit · r/MachineLearning · /u/jacobgorm · Aug 17, 00:46

**Background**: Kolmogorov-Arnold Networks (KANs) are a neural network architecture inspired by the Kolmogorov-Arnold representation theorem, which states that multivariate functions can be represented as compositions of univariate functions. Unlike multilayer perceptrons (MLPs) that use fixed activation functions and linear weights, KANs replace each weight with a learnable univariate function, often parameterized with B-splines. B-splines are piecewise polynomial basis functions with minimal support, widely used in curve fitting and computer graphics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/B-spline">B-spline</a></li>

</ul>
</details>

**Tags**: `#KAN`, `#Activation Functions`, `#Neural Networks`, `#Machine Learning`

---

<a id="item-16"></a>
## [Seeking Solutions for Long-Range Recall in Linear Attention](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 6.0/10

A researcher working on DNA sequence modeling reports that linear attention models achieve only around 25% recall on a needle-in-a-haystack benchmark, near random chance for a 4-token DNA vocabulary, and that even HyenaDNA scores only 25–27%. They tested a small 16K-context model that reached 50–60% recall, but performance degrades sharply as context length grows, prompting a search for architectural solutions. This highlights a fundamental limitation of linear attention for long-context genomic modeling, where sequences can easily reach 1 million tokens. Solving long-range recall without reverting to expensive softmax attention would enable efficient, scalable DNA foundation models. The needle-in-a-haystack test uses a four-token DNA alphabet (A/C/G/T), so random chance is 25%. The author's attempts to modify the linear architecture only improved recall to about 27%, still essentially chance, and they explicitly seek approaches that can scale to million-token DNA sequences.

reddit · r/MachineLearning · /u/No-Coffee-8227 · Aug 16, 07:47

**Background**: Linear attention approximates softmax attention with a constant-size state, avoiding the linearly growing KV cache of standard transformers and enabling subquadratic scaling. However, this compressed state can struggle with exact retrieval of distant information, a key limitation exposed by needle-in-a-haystack benchmarks. HyenaDNA, a genomic foundation model built on the Hyena operator, also uses subquadratic methods and supports up to 1M context, but similarly underperforms on this recall task.

<details><summary>References</summary>
<ul>
<li><a href="https://haileyschoelkopf.github.io/blog/2024/linear-attn/">Linear Attention Fundamentals | Hailey Schoelkopf</a></li>
<li><a href="https://github.com/HazyResearch/hyena-dna">GitHub - HazyResearch/hyena-dna: Official implementation for HyenaDNA, a long-range genomic foundation model built with Hyena · GitHub</a></li>
<li><a href="https://dl.acm.org/doi/10.5555/3666122.3667994">HyenaDNA | Proceedings of the 37th International Conference on Neural Information Processing Systems</a></li>

</ul>
</details>

**Tags**: `#linear attention`, `#DNA sequencing`, `#long-range recall`, `#efficiency`, `#sequence modeling`

---

<a id="item-17"></a>
## [US Tells Allies: Sign Pax Silica or Face AI Exclusion](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 6.0/10

A draft letter from the US State Department reportedly warns allies and countries seeking AI cooperation with Washington that they must sign the Pax Silica declaration and cannot join overlapping initiatives that conflict with it, or risk exclusion from US-led AI alliances. This could reshape international AI alliances, forcing countries to pick a side between the US-led Pax Silica bloc and China-linked initiatives. It may deepen the geopolitical split in AI governance and chip supply chains, with significant implications for technology companies and global standards. The draft letter is said to describe signing the non-binding Pax Silica Declaration as more than joining a coalition — it also bars participation in duplicative initiatives with conflicting goals. Pax Silica is coordinated by the US State Department and was launched in December 2025 alongside an initial group of partner countries.

telegram · zaihuapd · Aug 16, 02:30

**Background**: Pax Silica is a US-led international initiative focused on securing supply chains for advanced technologies such as semiconductors, AI, and rare earth elements, implicitly targeting reduced reliance on China. It is seen as the US-led counterpart to the World Artificial Intelligence Cooperation Organization, and current members reportedly include Japan, South Korea, the UK, and Israel.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica</a></li>
<li><a href="https://www.state.gov/pax-silica">Pax Silica - United States Department of State</a></li>
<li><a href="https://grokipedia.com/page/Pax_Silica">Pax Silica</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#geopolitics`, `#Pax Silica`, `#international relations`, `#US alliances`

---

<a id="item-18"></a>
## [AI Tool Flags Telegram Piracy, Leading to 524 Channel Takedowns](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 6.0/10

Researchers analyzed 1,057 Telegram channels and 209,000 posts, finding 983 channels engaged in piracy with 4.85 billion views across 19,033 films. They then built an AI tool called Anti-RIP that scanned 249,000 new channels and flagged 802 suspected piracy channels with 98% test accuracy; after reporting to Telegram and rightsholders, 524 previously unknown channels were shut down within 61 days. This shows AI can be effectively applied to copyright enforcement on messaging platforms, achieving measurable real-world takedowns. It may prompt Telegram and other platforms to adopt similar automated moderation tools, while also raising concerns about false positives and freedom of speech. The Anti-RIP tool still produces false positives. The researchers used a dataset of 209,000 posts from 1,057 channels to characterize piracy, then scanned approximately 249,000 new channels, flagging 802; the study highlights the scale of piracy on Telegram.

telegram · zaihuapd · Aug 16, 09:13

**Background**: Telegram is a cloud-based messaging app that allows users to create channels broadcast to unlimited audiences, making it popular for sharing pirated movies, TV shows, and other copyrighted content. Copyright holders historically struggle to police such content due to Telegram's large scale, encrypted communications, and lax moderation. AI-based content detection has emerged as a way to automatically identify patterns of piracy, such as naming conventions, links, or metadata. This research demonstrates that such tools can complement manual reporting and lead to actual channel shutdowns when shared with platforms and rights holders.

**Tags**: `#AI`, `#Piracy`, `#Telegram`, `#Copyright`, `#Research`

---

<a id="item-19"></a>
## [SafePal Discloses Data Breach Affecting Nearly 40,000 Customers](https://www.reuters.com/legal/litigation/crypto-wallet-provider-safepal-discloses-data-breach-affecting-nearly-40000-2026-08-16/) ⭐️ 6.0/10

SafePal disclosed on August 16 that a data breach exposed order information for approximately 39,798 customers, including names, addresses, and purchase data. The vulnerability was in its order tracking system and affected records from March 2, 2025, to April 11, 2026. This incident matters because the exposed personal data could be leveraged for targeted phishing and impersonation campaigns against crypto wallet users. Even though sensitive wallet data was not stolen, it underscores persistent security challenges in the cryptocurrency industry and the need for robust customer data protection. SafePal confirmed that mnemonic phrases, private keys, wallet passwords, and bank account details were not exposed. The company has patched the flaw and taken down more than 30 fraudulent websites and phishing links connected to the breach.

telegram · zaihuapd · Aug 16, 17:06

**Background**: SafePal is a cryptocurrency wallet provider founded in 2018 that offers both hardware and software wallets for storing digital assets securely. In cryptocurrency wallets, a mnemonic phrase (or seed phrase) is used to back up the private keys that authorize transactions, making such data a prime target for attackers. Data breaches that expose personal details are frequently exploited for phishing, where attackers craft believable messages based on real information.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/SafePal">SafePal</a></li>
<li><a href="https://safepal.com/en/store/s1">SafePal | The Best Crypto Wallet for Bitcoin, Ethereum ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#data-breach`, `#crypto`, `#privacy`, `#safepal`

---

<a id="item-20"></a>
## [How to Enable a 1M Token Context Window in Codex with GPT-5.6 Sol](https://x.com/thsottiaux/status/2089082893804896524) ⭐️ 6.0/10

Tibo shared a configuration tip to enable a 1 million token context window in Codex. The method sets model_context_window=1000000 and model_auto_compact_token_limit=900000 in ~/.codex/config.toml, and the underlying GPT-5.6 Sol model supports up to 1.05 million tokens. This lets developers work with much larger codebases and longer conversation histories in a single Codex session, reducing the need to split tasks or manually summarize context. It is a practical workflow improvement for AI-assisted coding as models continue expanding their context windows. These settings are top-level keys in config.toml, not nested under a table, and take effect after saving and restarting the client or starting a new session. The same configuration can also be passed via command-line flags to apply it only to a single CLI session.

telegram · zaihuapd · Aug 17, 00:47

**Background**: Codex is OpenAI's AI coding agent that can write features, fix bugs, and propose pull requests, available through the ChatGPT web app, CLI, desktop app, and IDE integrations. Its configuration file at ~/.codex/config.toml controls the model, execution environment, and integrations. GPT-5.6 is a family of OpenAI models released in 2026; Sol is the most capable variant and is positioned as OpenAI's best coding model.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.xkiro.com/guides/tools/codex/">Codex CLI — xKiro Docs</a></li>
<li><a href="https://codex.aifenghao.com/en/config/">Codex CLI config . toml Complete Guide (2026) | Codex CLI Guide</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Codex`, `#context window`, `#GPT-5.6`, `#configuration`, `#AI coding assistant`

---
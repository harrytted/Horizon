---
layout: default
title: "Horizon Summary: 2026-07-25 (EN)"
date: 2026-07-25
lang: en
---

> From 5 items, 5 important content pieces were selected

---

1. [SGLang v0.5.16: DSpark Speculative Decoding & Inkling Support](#item-1) ⭐️ 9.0/10
2. [Ruff v0.16.0 dramatically expands default linting rules](#item-2) ⭐️ 8.0/10
3. [Claude Opus 5 Achieves Best Prompt Injection Resistance](#item-3) ⭐️ 8.0/10
4. [AMD Targets NVIDIA's CUDA Moat with AI Kernel Generation](#item-4) ⭐️ 8.0/10
5. [Go 1.26's New Green Tea GC Explored](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.16: DSpark Speculative Decoding & Inkling Support](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 9.0/10

SGLang v0.5.16 introduces DSpark confidence-driven speculative decoding, achieving 383.7 tok/s with accept length ~5 on DeepSeek-V4-Pro, and supports the 975B-parameter Inkling multimodal MoE model with up to 71.7k tok/s input throughput. These updates significantly boost inference efficiency for large language models, with DSpark offering a novel adaptive verification approach that reduces latency, and Inkling enabling deployment of a massive open multimodal model with high throughput, impacting both research and production use cases. DSpark uses semi-autoregressive drafting with confidence-sized verification windows, tuning block size via --speculative-dspark-block-size. Inkling mixes sliding-window, full, and Mamba2 linear attention with NVFP4 MoE, optional vision/audio towers, and native MTP, verified on Blackwell, H200, and AMD MI350X/MI355X.

github · Qiaolin-Yu · Jul 25, 00:13

**Background**: Speculative decoding accelerates large language model inference by using a smaller draft model to propose multiple tokens that are then verified in parallel by the target model. DSpark improves on this by adapting the verification window based on the draft's confidence, rather than using a fixed length. MoE (Mixture of Experts) models activate only a subset of parameters per token, enabling large total parameter counts with manageable compute. SGLang is an open-source inference engine for LLMs and multimodal models, known for efficient serving and support for various hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation</a></li>
<li><a href="https://www.eigent.ai/blog/thinking-machines-inkling-open-weights-model">Thinking Machines Inkling : The First Open-Weights Model</a></li>
<li><a href="https://www.baseten.co/library/inkling/">Inkling | Model library</a></li>

</ul>
</details>

**Tags**: `#SGLang`, `#speculative decoding`, `#multimodal`, `#MoE`, `#inference`

---

<a id="item-2"></a>
## [Ruff v0.16.0 dramatically expands default linting rules](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Astral released Ruff v0.16.0 on July 23, 2026, which enables 413 rules by default, up from only 59 in previous versions. This significant increase means developers will catch many more potential issues—including syntax errors and runtime errors—without any configuration, improving code quality across the Python ecosystem. Projects using unpinned Ruff dependencies may see CI failures until they update their code. Ruff now has 968 total rules, up from 708 in v0.1.0, and the new defaults include rules from categories like bugbear (B), pyupgrade (UP), and Ruff-specific (RUF), among others. The tool can also apply automatic fixes with the --fix and --unsafe-fixes flags.

rss · Simon Willison · Jul 25, 22:44

**Background**: Ruff is an extremely fast Python linter and code formatter written in Rust, often 10-100x faster than traditional tools like Flake8. It provides over 900 built-in rules, many of which are native re-implementations of popular Flake8 plugins. Previously, Ruff's default rule set was very conservative, only enabling a small subset (e.g., E4, E7, E9, F) since v0.1.0 in 2023.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/">Ruff</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://pydevtools.com/blog/ruff-0-16-0-default-rules/">Ruff 0.16.0 Enables 7x More Rules by Default | pydevtools</a></li>

</ul>
</details>

**Tags**: `#ruff`, `#python`, `#linting`, `#tooling`, `#astral`

---

<a id="item-3"></a>
## [Claude Opus 5 Achieves Best Prompt Injection Resistance](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Boris Cherny announced that Anthropic's Claude Opus 5 is the most resistant to prompt injection attacks of any model to date, as detailed in the system card. This advancement significantly enhances AI safety by reducing vulnerabilities to jailbreaking, which is crucial for deploying models in sensitive applications. The claim is supported by evaluations and red teaming results, though specific metrics are not provided in the quoted tweet.

rss · Simon Willison · Jul 25, 00:42

**Background**: Prompt injection is a technique where malicious inputs trick an AI model into overriding its instructions, potentially causing harmful outputs. Improving resistance is a key safety goal for large language models.

**Tags**: `#prompt-injection`, `#Anthropic`, `#Claude`, `#AI safety`, `#generative-ai`

---

<a id="item-4"></a>
## [AMD Targets NVIDIA's CUDA Moat with AI Kernel Generation](https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing) ⭐️ 8.0/10

AMD is advancing its AI hardware and software strategy, notably through Agentic Kernel Generation to automate CUDA kernel optimization, while facing production hurdles with the MI455X (Helios) GPU and offering financial discounts up to 105%. If AMD can successfully break NVIDIA's CUDA software moat, it could democratize AI hardware competition, reducing dependency on NVIDIA's ecosystem and potentially lowering costs for AI workloads. Agentic Kernel Generation uses reinforcement learning to automatically generate high-performance CUDA kernels, addressing a key bottleneck. The MI455X features 432GB HBM4 memory and 40.26 PFLOPS in MXFP4, but production ramp faces delays and financial engineering includes up to 105% discounts to attract customers.

rss · Semianalysis · Jul 25, 00:33

**Background**: NVIDIA's CUDA ecosystem has long been a dominant software platform for GPU computing, creating a 'moat' that competitors find hard to cross. AMD has been developing its ROCm software stack, but compatibility and performance gaps remain. Agentic Kernel Generation is a new approach using LLMs and RL to automate kernel optimization. The Helios rack is AMD's answer to NVIDIA's NVL72, integrating 72 MI455X GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.24286v1">CUDA AgentCUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html">AMD Instinct™ MI455X GPUs</a></li>
<li><a href="https://www.amd.com/en/products/rackscale-solutions/helios.html">Helios - AMD</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#CUDA`, `#AI Hardware`, `#GPU`, `#Software Ecosystem`

---

<a id="item-5"></a>
## [Go 1.26's New Green Tea GC Explored](https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html) ⭐️ 7.0/10

Go 1.26 has made the experimental Green Tea garbage collector the default, replacing the previous GC. This new collector scans memory in large contiguous blocks to improve cache locality and performance. This change addresses long-standing issues with heap fragmentation and pause times in Go applications, especially for high-throughput systems. Developers can expect more predictable memory management and better CPU cache utilization. The Green Tea GC uses a parallel marking algorithm that scans memory in contiguous blocks rather than individual objects, improving cache friendliness. However, Go's non-moving collector still faces a sparse-page problem where free pages are scattered, limiting compaction.

hackernews · matheusmoreira · Jul 25, 07:55 · [Discussion](https://news.ycombinator.com/item?id=49045474)

**Background**: Garbage collectors (GCs) automatically manage memory by reclaiming unused objects. Go previously used a concurrent, tri-color mark-sweep collector, which could lead to heap fragmentation. Heap compaction is a technique to defragment memory by moving live objects, but Go's non-moving GC traditionally avoided compaction to reduce complexity. The Green Tea GC aims to balance throughput and latency while improving memory locality.

<details><summary>References</summary>
<ul>
<li><a href="https://go.dev/blog/greenteagc">The Green Tea Garbage Collector - The Go Programming Language</a></li>
<li><a href="https://github.com/golang/go/issues/73581">runtime: green tea garbage collector · Issue #73581 · golang/go</a></li>
<li><a href="https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html">Watching Go's new garbage collector move through the heap - The Consensus</a></li>

</ul>
</details>

**Discussion**: Commenters found the article insightful but noted it ends abruptly. One user asked about manual heap compaction in Go, while another appreciated the technique of copying objects to new slices to aid GC. A tangential discussion compared Go's GC to C#'s and mentioned the high cost of developing a pauseless GC.

**Tags**: `#Go`, `#garbage collection`, `#heap`, `#performance`, `#systems programming`

---
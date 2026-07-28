---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 5 条内容中筛选出 5 条重要资讯。

---

1. [SGLang v0.5.16 发布：DSpark 推测解码和 Inkling 模型支持](#item-1) ⭐️ 9.0/10
2. [Ruff v0.16.0 大幅扩展默认规则集](#item-2) ⭐️ 8.0/10
3. [Claude Opus 5 实现最佳提示注入防护](#item-3) ⭐️ 8.0/10
4. [AMD 以 AI 内核生成挑战 NVIDIA 的 CUDA 护城河](#item-4) ⭐️ 8.0/10
5. [Go 1.26 新绿茶垃圾回收器深度解析](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.16 发布：DSpark 推测解码和 Inkling 模型支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 9.0/10

SGLang v0.5.16 引入了基于置信度的 DSpark 推测解码算法，在 DeepSeek-V4-Pro 上实现 383.7 tok/s 的吞吐量和约 5 的接受长度；同时支持 975B 参数的 Inkling 多模态 MoE 模型，输入吞吐量高达 71.7k tok/s。 这些更新显著提升了大型语言模型的推理效率：DSpark 提供了一种新颖的自适应验证方法以降低延迟，Inkling 则支持部署大规模开源多模态模型并实现高吞吐量，对研究和生产场景都产生了重要影响。 DSpark 采用半自回归草稿生成和基于置信度的验证窗口，可通过 --speculative-dspark-block-size 调整块大小。Inkling 混合了滑动窗口、全注意力和 Mamba2 线性注意力，使用 NVFP4 MoE，可选视觉/音频塔和原生 MTP，已在 Blackwell、H200 和 AMD MI350X/MI355X 上验证。

github · Qiaolin-Yu · 7月25日 00:13

**背景**: 推测解码通过使用小型草稿模型生成多个候选 token，再由目标模型并行验证，从而加速大语言模型推理。DSpark 通过根据草稿的置信度自适应调整验证窗口而不是固定长度，改进了这一方法。MoE（混合专家）模型每个 token 仅激活部分参数，使得总参数数量很大但计算量可控。SGLang 是一个用于 LLM 和多模态模型的开源推理引擎，以高效服务和多种硬件支持而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation</a></li>
<li><a href="https://www.eigent.ai/blog/thinking-machines-inkling-open-weights-model">Thinking Machines Inkling : The First Open-Weights Model</a></li>
<li><a href="https://www.baseten.co/library/inkling/">Inkling | Model library</a></li>

</ul>
</details>

**标签**: `#SGLang`, `#speculative decoding`, `#multimodal`, `#MoE`, `#inference`

---

<a id="item-2"></a>
## [Ruff v0.16.0 大幅扩展默认规则集](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Astral 于 2026 年 7 月 23 日发布了 Ruff v0.16.0，默认启用的规则从之前的 59 条增加到 413 条。 这一重大提升意味着开发者无需任何配置即可发现更多潜在问题（包括语法错误和运行时错误），从而提高整个 Python 生态系统的代码质量。使用未固定 Ruff 依赖的项目可能会在更新代码前遭遇 CI 失败。 Ruff 现在的总规则数从 v0.1.0 的 708 条增加到 968 条，新默认规则包括 bugbear (B)、pyupgrade (UP) 和 Ruff 专用 (RUF) 等类别。该工具还可以通过 --fix 和 --unsafe-fixes 标志自动修复问题。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的极速 Python 代码检查器和格式化工具，通常比 Flake8 等传统工具快 10-100 倍。它提供超过 900 条内置规则，其中许多是流行 Flake8 插件的原生重实现。此前，自 2023 年的 v0.1.0 起，Ruff 的默认规则集非常保守，只启用了很小一部分（例如 E4、E7、E9、F）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/">Ruff</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://pydevtools.com/blog/ruff-0-16-0-default-rules/">Ruff 0.16.0 Enables 7x More Rules by Default | pydevtools</a></li>

</ul>
</details>

**标签**: `#ruff`, `#python`, `#linting`, `#tooling`, `#astral`

---

<a id="item-3"></a>
## [Claude Opus 5 实现最佳提示注入防护](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Boris Cherny 宣布，Anthropic 的 Claude Opus 5 是目前最抵抗提示注入攻击的模型，系统卡中对此有详细说明。 这一进步显著增强了 AI 安全性，减少了被越狱的漏洞，对于在敏感应用中部署模型至关重要。 该声明得到评估和红队测试结果的支持，但引用的推文中未提供具体指标。

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入是一种通过恶意输入诱使 AI 模型覆盖其指令的技术，可能导致有害输出。提高抵抗力是大语言模型的关键安全目标。

**标签**: `#prompt-injection`, `#Anthropic`, `#Claude`, `#AI safety`, `#generative-ai`

---

<a id="item-4"></a>
## [AMD 以 AI 内核生成挑战 NVIDIA 的 CUDA 护城河](https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing) ⭐️ 8.0/10

AMD 正在推进其 AI 硬件和软件战略，尤其通过智能内核生成技术来自动优化 CUDA 内核，同时面临 MI455X（Helios）GPU 的生产难题，并提供高达 105%的财务折扣。 如果 AMD 能成功打破 NVIDIA 的 CUDA 软件护城河，可能会使 AI 硬件竞争民主化，减少对 NVIDIA 生态系统的依赖，并可能降低 AI 工作负载的成本。 智能内核生成利用强化学习自动生成高性能 CUDA 内核，解决了关键瓶颈。MI455X 配备 432GB HBM4 内存和 40.26 PFLOPS（MXFP4），但量产爬坡面临延迟，财务工程包括高达 105%的折扣以吸引客户。

rss · Semianalysis · 7月25日 00:33

**背景**: NVIDIA 的 CUDA 生态系统长期以来一直是 GPU 计算的主导软件平台，形成了竞争对手难以跨越的‘护城河’。AMD 一直在开发其 ROCm 软件栈，但兼容性和性能差距依然存在。智能内核生成是一种利用 LLM 和强化学习自动优化内核的新方法。Helios 机架是 AMD 对 NVIDIA NVL72 的回应，集成了 72 块 MI455X GPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.24286v1">CUDA AgentCUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html">AMD Instinct™ MI455X GPUs</a></li>
<li><a href="https://www.amd.com/en/products/rackscale-solutions/helios.html">Helios - AMD</a></li>

</ul>
</details>

**标签**: `#AMD`, `#CUDA`, `#AI Hardware`, `#GPU`, `#Software Ecosystem`

---

<a id="item-5"></a>
## [Go 1.26 新绿茶垃圾回收器深度解析](https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html) ⭐️ 7.0/10

Go 1.26 已将实验性的绿茶垃圾回收器设为默认，取代了之前的 GC。新的回收器以连续大块扫描内存，以提高缓存局部性和性能。 这一变化解决了 Go 应用中长期存在的堆碎片化和停顿时间问题，尤其对高吞吐系统而言。开发者可以期待更可预测的内存管理和更好的 CPU 缓存利用。 绿茶 GC 采用并行标记算法，以连续块而非单个对象扫描内存，提高了缓存友好性。但 Go 的非移动式收集器仍面临稀疏页面问题，即空闲页面分散，限制了压缩效果。

hackernews · matheusmoreira · 7月25日 07:55 · [社区讨论](https://news.ycombinator.com/item?id=49045474)

**背景**: 垃圾回收器（GC）通过回收未使用的对象来自动管理内存。Go 之前使用并发的三色标记-清除收集器，可能导致堆碎片化。堆压缩是一种通过移动存活对象来整理内存的技术，但 Go 的非移动式 GC 传统上避免压缩以降低复杂性。绿茶 GC 旨在平衡吞吐量和延迟，同时改善内存局部性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/blog/greenteagc">The Green Tea Garbage Collector - The Go Programming Language</a></li>
<li><a href="https://github.com/golang/go/issues/73581">runtime: green tea garbage collector · Issue #73581 · golang/go</a></li>
<li><a href="https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html">Watching Go's new garbage collector move through the heap - The Consensus</a></li>

</ul>
</details>

**社区讨论**: 评论者认为文章有见地但结尾略显突兀。有用户询问 Go 中手动堆压缩的情况，另一用户赞赏通过复制对象到新切片来帮助 GC 的技术。一个相关讨论将 Go 的 GC 与 C# 的进行比较，并提到开发无暂停 GC 的高昂成本。

**标签**: `#Go`, `#garbage collection`, `#heap`, `#performance`, `#systems programming`

---
---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
---

> 从 38 条内容中筛选出 20 条重要资讯。

---

1. [AI 初创公司越来越少发布研究成果](#item-1) ⭐️ 8.0/10
2. [开源引擎让 Gemma 4 26B 在 M 系列 Mac 上仅用 2GB 内存运行](#item-2) ⭐️ 8.0/10
3. [Mitchell Hashimoto 基于 libghostty 创办 Superlogical](#item-3) ⭐️ 8.0/10
4. [Kimi 推出半价 256K 上下文的 K3-256k](#item-4) ⭐️ 8.0/10
5. [长政策文档无法可靠约束 LLM 智能体](#item-5) ⭐️ 8.0/10
6. [AI 蠕虫通过提示注入在 Word 中自我复制](#item-6) ⭐️ 8.0/10
7. [Matthew Green 强调后量子密码学转型与 AI 密码分析机遇](#item-7) ⭐️ 8.0/10
8. [基于 Vulkan 的 ncnn 加速任意 GPU 上的 ML 推理](#item-8) ⭐️ 8.0/10
9. [俄联邦安全局指控杜罗夫协助恐怖活动并通缉](#item-9) ⭐️ 8.0/10
10. [报告称 Hugging Face 模型被广泛用于生成深度伪造裸照](#item-10) ⭐️ 8.0/10
11. [月之暗面融资 35 亿美元，估值达 350 亿美元](#item-11) ⭐️ 8.0/10
12. [中国反网络暴力法草案将 AI 网暴纳入规制](#item-12) ⭐️ 8.0/10
13. [OpenAI 向 10 万学者免费提供前沿模型](#item-13) ⭐️ 8.0/10
14. [字节最大 To B 变革：飞书并入豆包与火山引擎](#item-14) ⭐️ 8.0/10
15. [Vision Pro 用于建筑比例评估](#item-15) ⭐️ 7.0/10
16. [AI 公司招聘数千名电工和木匠建设数据中心](#item-16) ⭐️ 7.0/10
17. [D. Richard Hipp 谈 SQL 取代 COBOL 程序员](#item-17) ⭐️ 7.0/10
18. [模块化数据中心：解决劳动力与可扩展性挑战](#item-18) ⭐️ 7.0/10
19. [中国电信停止第三方互联网渠道销售 SIM 卡](#item-19) ⭐️ 7.0/10
20. [英国监管机构拟要求苹果开放 App Store 外部支付](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 初创公司越来越少发布研究成果](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) ⭐️ 8.0/10

近期一篇文章指出，包括 OpenAI 和 Anthropic 在内的顶级 AI 初创公司发表的论文越来越少，降低了该领域的透明度。 这一趋势威胁到推动 AI 进步的开放科学文化，可能会减缓创新速度，并使更广泛的研究界难以在其工作基础上进一步开发。 文章使用累计引用量作为研究影响力的替代指标，指出 OpenAI 位居榜首，其次是旷视科技（Megvii）和 Hugging Face 等公司，但总体发表数量正在下降。

hackernews · YeGoblynQueenne · 7月29日 21:25 · [社区讨论](https://news.ycombinator.com/item?id=49103285)

**背景**: 历史上，AI 研究依赖于开放的论文发表以及代码和数据的共享，重大突破通常以会议论文或预印本的形式出现。然而，随着 AI 初创公司面临竞争压力和知识产权问题，许多公司选择将成果保密以保持竞争优势。

**社区讨论**: 评论者分享了个人经历：有人指出在尝试向顶级期刊投稿遇到困难后，其初创公司转向预印本；另有人故意不发表成果，以防 OpenAI 和 Anthropic 等公司抄袭。还有评论者批评 AI 研究的“博客化”，认为这导致未经证实的说法和缺乏严谨性。

**标签**: `#AI research`, `#startups`, `#open science`, `#publications`

---

<a id="item-2"></a>
## [开源引擎让 Gemma 4 26B 在 M 系列 Mac 上仅用 2GB 内存运行](https://github.com/drumih/turbo-fieldfare) ⭐️ 8.0/10

开发者发布了 TurboFieldfare，这是一个用 Swift 和 Metal 编写的开源推理引擎，通过从 SSD 流式传输路由专家，在任何 M 系列 Mac 上仅用约 2GB 内存运行 4 位量化的 Gemma 4 26B-A4B-IT 模型。 这一突破使得在低内存设备上运行大型语言模型成为可能，极大地扩展了设备端 AI 的可及性，尤其是对于内存有限的 Mac 用户。它展示了一种在不牺牲性能的情况下克服内存限制的实用方法，根据 Mac 型号可实现 5-35 tok/s 的生成速度。 模型的 4 位权重约占 14GB，但 TurboFieldfare 仅将共享部分和 KV 缓存保留在 RAM 中，使用小型专家缓存和有界并行 pread 从 SSD 流式传输专家。目前，它在 8GB M2 MacBook Air 上生成 5-6 tok/s，在 M5 MacBook Pro 上生成 31-35 tok/s，并包含一个实验性的 OpenAI 兼容服务器，支持流式和工具调用。

hackernews · gitpusher42 · 7月29日 15:05 · [社区讨论](https://news.ycombinator.com/item?id=49098510)

**背景**: 像 Gemma 4 这样的混合专家（MoE）模型使用多个子网络（专家），并通过门控网络每个令牌仅激活少数专家，从而减少计算量。KV 缓存存储先前令牌的中间键值状态，以加速推理。4 位量化将模型权重精度降至 4 位，减少内存占用。TurboFieldfare 利用 MoE 的稀疏性，从 SSD 流式传输专家，而不是将所有权重加载到 RAM 中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/not-lain/kv-caching">KV Caching Explained: Optimizing Transformer Inference Efficiency</a></li>
<li><a href="https://arxiv.org/pdf/2103.13630">A Survey of Quantization Methods for Efcient</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞这一新颖方法，有用户指出不必将整个模型加载到内存中的效率。另一用户提供了在旧版 macOS 上编译的解决方法。有人将其与 llama.cpp 中的普通 mmap 进行对比，强调与推理活动同步的 SSD 读取是主要区别。另一位拥有相关 DiffusionGemma 项目的开发者表达了合作兴趣。

**标签**: `#on-device AI`, `#inference engine`, `#Mac`, `#Gemma`, `#model streaming`

---

<a id="item-3"></a>
## [Mitchell Hashimoto 基于 libghostty 创办 Superlogical](https://www.superlogical.com/) ⭐️ 8.0/10

Mitchell Hashimoto 宣布成立 Superlogical 公司，该公司将基于开源库 libghostty 构建终端应用，并承诺向上游贡献代码。 这标志着一种可持续的开源商业模式：创始人将核心项目移交给非营利组织，并在此基础上构建商业产品，可能为开发者工具生态系统提供借鉴。 Ghostty 的核心库 libghostty 采用 MIT 许可证，对所有人开放；Superlogical 将其作为公共构建块，并继续向上游提交改进。

hackernews · yan · 7月29日 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49098965)

**背景**: Ghostty 是一款快速且功能丰富的终端模拟器，使用平台原生 UI 和 GPU 加速，用 Zig 编写。libghostty 是一个跨平台、无依赖的 C 和 Zig 库，提供终端仿真功能。Mitchell Hashimoto 是 Ghostty 的创建者，也是 HashiCorp 的联合创始人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty-org/ghostty: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.</a></li>
<li><a href="https://ghostty.org/docs/about">About Ghostty</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏这种开源商业模式，有人注意到将 Ghostty 移交给非营利组织，并基于开源依赖构建 Superlogical。一些人将其与代理复用器和 OLE 等历史技术相提并论，也有少数人批评标题过于隐晦。

**标签**: `#terminals`, `#open-source`, `#company`, `#ghostty`, `#mitchell-hashimoto`

---

<a id="item-4"></a>
## [Kimi 推出半价 256K 上下文的 K3-256k](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 8.0/10

Moonshot AI 发布了 Kimi K3-256k，这是 K3 模型的一个低价变体，具有 256k 令牌的上下文窗口，价格仅为完整 1M 版本的一半。 这一价格调整使得长上下文 AI 对不需要完整 1M 令牌窗口的开发者和应用更加可及，可能拓展在代码分析和文档处理等领域的用例。 K3-256k 模型与 K3 (1M) 是同一个底层模型，但上下文硬性限制在 256k 令牌，消耗约一半的配额。它未经过量化，仅上下文长度不同。

hackernews · monneyboi · 7月29日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49101852)

**背景**: 上下文窗口指的是 AI 模型一次能处理的令牌数量（大致对应单词或子词）；更大的窗口允许处理更长的文档，但计算成本更高。Kimi K3 是 Moonshot AI 的旗舰模型，拥有 2.8 万亿参数和 1M 令牌上下文，采用混合线性注意力机制。新的 K3-256k 变体为不需要完整上下文的用户提供了经济实惠的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://www.userightai.com/ai-context-window-comparison">AI Context Window Comparison 2026 — Which Models Handle the Most Tokens ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，这种阶梯式定价类似于 OpenAI 的做法，且以硬性限制而非平滑梯度实现令人意外。一些人认为对于 256k 以下的用户来说，半价降幅巨大，而另一些人澄清这仅是 API 层面的变化，模型相同且未量化。

**标签**: `#AI`, `#models`, `#pricing`, `#context-length`

---

<a id="item-5"></a>
## [长政策文档无法可靠约束 LLM 智能体](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

一篇名为《Handbook.md》的新论文通过实验证明，长政策文档无法可靠地约束基于 LLM 的智能体，揭示了当前长上下文模型的一个根本性局限。 这一发现对 AI 智能体的部署和安全有直接影响，因为从业者通常依赖冗长的政策文档来指导智能体行为。结果与轶事经验一致，并对长上下文模型在治理任务中的假定可靠性提出了挑战。 该论文表明，即使是最先进的模型，随着文档长度增加，也难以遵守政策；社区讨论将失败归因于 KV 缓存量化和有限的工作记忆。本地推理被认为是部分补救措施。

hackernews · spIrr · 7月29日 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49096969)

**背景**: 许多大型语言模型（LLM）声称支持极长的上下文（如 100 万 token），但研究表明它们难以有效利用这些信息。KV 缓存（存储推理时的注意力键和值）在长序列中会被重度量化，导致性能下降。此外，工作记忆限制使得模型无法同时遵循大量指令，这与人类的认知局限类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2404.02060">[2404.02060] Long-context LLMs Struggle with Long In-context ... Efficient Solutions For An Intriguing Failure of LLMs: Long ... Efficient Solutions For An Intriguing Failure of LLMs: Long ... [2510.05381] Context Length Alone Hurts LLM Performance ... LLMs and Long Contexts: Where It Starts to Go Wrong Evaluating Long Context Lengths in LLMs: Challenges and ... Efficient Solutions For An Intriguing Failure of LLMs: Long ...</a></li>
<li><a href="https://aclanthology.org/2025.coling-main.128/">Efficient Solutions For An Intriguing Failure of LLMs: Long ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍赞同这些发现，用户分享轶事证据表明 Claude 会逐渐忽略长指令。讨论指出 KV 缓存量化、糟糕的采样器和工作记忆限制是根本原因。一些人认为本地推理可以缓解该问题，而另一些人则指出，在此类基准上实现超人表现需要非凡的能力。

**标签**: `#LLM`, `#AI safety`, `#long-context`, `#agent`, `#policy`

---

<a id="item-6"></a>
## [AI 蠕虫通过提示注入在 Word 中自我复制](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 8.0/10

安全研究人员 Håkon Måløy 展示了一种自我复制的提示注入蠕虫，它通过在文档中嵌入隐藏指令，使微软 Word 的 Copilot 功能将恶意指令传播到新文档。 这种新型攻击将 AI 助手变成传播恶意软件的帮凶，凸显了 AI 集成的生产力工具中的关键安全漏洞，可能影响数百万用户。 该蠕虫通过将其隐藏指令复制到输出文档中，使得后续任何使用该文档的 Copilot 会话再次触发攻击，无需攻击者的原始文件即可实现自我复制。

rss · Simon Willison · 7月29日 18:43

**背景**: 提示注入是一种网络安全利用方式，恶意输入导致 AI 模型出现意外行为。自我复制的 AI 蠕虫（如 Morris II 概念验证）利用对抗性提示在 AI 驱动的系统中传播。这次攻击将两种技术结合在 Word 文档场景中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/">AI Worms Explained: Adaptive Malware Threats - SentinelOne</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#security`, `#AI`, `#Microsoft Word`, `#self-replicating worm`

---

<a id="item-7"></a>
## [Matthew Green 强调后量子密码学转型与 AI 密码分析机遇](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

著名密码学家 Matthew Green 评论了从 RSA 和 ECC 等传统公钥算法向 HAWK 等后量子算法的历史性过渡，并强调现在是 AI 推进密码分析的最佳时机。 这一过渡至关重要，因为量子计算机可能破解现有密码学，而 AI 驱动的密码分析可能加强或削弱新标准，影响全球网络安全基础设施。Matthew Green 的见解凸显了 AI 与后量子密码学在关键时刻的融合。 HAWK 是 NIST 后量子签名标准的候选方案，Anthropic 最近发现了其中的一个弱点，但该问题仅针对 HAWK，不影响其他基于格密码的方案。Green 还提到了 Impagliazzo 的 Minicrypt，这是一个只有对称密码学可能的理论世界，如果 AI 破解了所有困难问题，这可能是结果之一。

rss · Simon Willison · 7月29日 18:18

**背景**: 后量子密码学旨在开发能够抵抗量子计算机攻击的算法，量子计算机将破解当前广泛使用的公钥系统如 RSA 和椭圆曲线密码学。NIST 正在举办一场标准化竞赛，HAWK 是其中签名方案的候选者。Impagliazzo 的五世界是一个概念框架，分类可能的计算复杂性世界，其中 Minicrypt 假设单向函数存在但公钥加密不存在。AI 在密码分析中的潜在作用可能有助于验证新算法的安全性或发现漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.csoonline.com/article/4202920/mythos-takes-its-first-shot-at-post-quantum-cryptography.html">Anthropic finds weakness in Hawk post - quantum digital signature ...</a></li>
<li><a href="https://fanpu.io/blog/2022/impagliazzos-five-worlds/">Impagliazzo ' s Five Worlds, or The Computational... | Fan Pu Zeng</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#AI cryptanalysis`, `#public-key algorithms`, `#Matthew Green`, `#cryptography standards`

---

<a id="item-8"></a>
## [基于 Vulkan 的 ncnn 加速任意 GPU 上的 ML 推理](https://www.reddit.com/r/MachineLearning/comments/1v9s4mz/vendoragnostic_ml_inference_on_production_edge/) ⭐️ 8.0/10

PostSlate 使用 ncnn 的 Vulkan 后端在任意 GPU 上运行人脸检测和嵌入等 ML 模型，无需供应商特定运行时，相比 ONNX CPU 推理实现了高达 10 倍的加速。 这种方法消除了对 CUDA 等供应商特定 SDK 的依赖，实现了边缘设备上无缝的跨平台 ML 推理。它降低了部署复杂性，并扩大了设备端 AI 的覆盖范围。 ncnn 是腾讯开发的高性能神经网络推理框架，无第三方依赖。Vulkan 后端利用计算着色器进行 GPU 加速，Reddit 帖子报告 ArcFace R50 从 30 毫秒（ONNX CPU）降至 3 毫秒（ncnn Vulkan）。

reddit · r/MachineLearning · /u/ppchaos · 7月29日 10:22

**背景**: 边缘 ML 推理常面临硬件多样性的挑战。CUDA 等供应商特定运行时限制了可移植性。Vulkan 是一种跨平台 GPU API，得到所有主流 GPU 供应商支持，是实现供应商无关推理的理想选择。ncnn 是一个针对移动和嵌入式平台优化的开源框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent/ncnn">GitHub - Tencent/ncnn: ncnn is a high-performance neural network inference framework optimized for the mobile platform · GitHub</a></li>
<li><a href="https://docs.vulkan.org/tutorial/latest/11_Compute_Shader.html">Compute Shader :: Vulkan Documentation Project</a></li>

</ul>
</details>

**标签**: `#ML inference`, `#Vulkan`, `#edge devices`, `#cross-platform`, `#ncnn`

---

<a id="item-9"></a>
## [俄联邦安全局指控杜罗夫协助恐怖活动并通缉](https://www.interfax.ru/russia/1106228) ⭐️ 8.0/10

俄罗斯联邦安全局（FSB）7 月 29 日宣布，已依据《刑法》第 205.1 条第 1.1 款（协助恐怖活动）对 Telegram 创始人帕维尔·杜罗夫提起刑事指控，并将其列入国际通缉名单。 这标志着国家对一位重要科技创始人的行动显著升级，对平台责任、隐私权以及国际法律规范产生影响，可能为追究科技高管因其平台用户生成内容而承担刑事责任开创先例。 FSB 指控 Telegram 管理层拒不删除被乌克兰情报机构及恐怖、极端主义组织用于在俄境内策划和协调破坏活动、恐怖袭击、大规模杀戮及网络诈骗的频道、群组和机器人，造成多人伤亡和数十亿卢布损失。

telegram · zaihuapd · 7月29日 05:56

**背景**: Telegram 是由帕维尔·杜罗夫创立的加密通信平台，他于 2014 年因与当局发生纠纷离开俄罗斯。俄政府此前曾在 2018 年试图封锁 Telegram，因其拒绝交出加密密钥。此次刑事指控标志着杜罗夫与俄罗斯国家当局之间的冲突进一步升级。

**标签**: `#Telegram`, `#Pavel Durov`, `#Russia`, `#terrorism`, `#tech regulation`

---

<a id="item-10"></a>
## [报告称 Hugging Face 模型被广泛用于生成深度伪造裸照](https://www.theverge.com/ai-artificial-intelligence/971723/hugging-face-nudify-deepfake-undress-women-children) ⭐️ 8.0/10

AI Forensics 于 7 月 28 日发布的报告显示，Hugging Face 上排名前九的图像编辑模型中有七个能轻易生成非自愿深度伪造色情内容，包括针对儿童的图像，且平台几乎未实施防护措施。 这凸显了开源 AI 平台治理中的关键漏洞，尽管有内容政策，滥用行为仍可能泛滥，威胁隐私和安全，尤其对女性和未成年人。 研究人员设置了一个蜜罐，在 7 天内收到超过 1000 条请求，其中 73%涉及性内容，近 7%针对儿童。无需精心构造提示即可绕过限制。

telegram · zaihuapd · 7月29日 08:20

**背景**: Hugging Face 是一个领先的开源平台，用于共享机器学习模型，包括图像生成工具。深度伪造是使用 AI 创建的逼真合成媒体，常被恶意用于制作非自愿的露骨内容。蜜罐是一种诱饵系统，吸引攻击者以收集滥用数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Honeypot_(computing)">Honeypot (computing)</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#deepfake`, `#HuggingFace`, `#ethics`, `#content moderation`

---

<a id="item-11"></a>
## [月之暗面融资 35 亿美元，估值达 350 亿美元](https://www.bloomberg.com/news/articles/2026-07-29/china-s-moonshot-ai-passes-funding-goal-to-hit-35-billion-value) ⭐️ 8.0/10

月之暗面完成了一轮 35 亿美元的融资，远超最初目标，投后估值达到 350 亿美元。此轮融资得益于其突破性模型 Kimi K3，该模型性能接近 OpenAI 和 Anthropic 的前沿水平。 这笔巨额融资表明投资者对中国 AI 初创公司信心十足，挑战了美国 AI 巨头的霸主地位。月之暗面的快速收入增长和 IPO 计划可能会重塑全球 AI 格局。 Kimi K3 模型拥有 2.8 万亿参数，采用名为 Kimi Delta Attention 的混合线性注意力机制，并已开源权重。月之暗面已启动新一轮融资，pre-money 估值 500 亿美元，计划最早今年在香港 IPO。

telegram · zaihuapd · 7月29日 10:12

**背景**: 月之暗面是一家以大型语言模型闻名的中国 AI 公司。Kimi K3 是其旗舰模型，拥有 2.8 万亿参数和 100 万 token 的上下文窗口。K3 的发布引发了“DeepSeek 时刻”——指 DeepSeek 的 R1 模型以低成本展示出竞争性能，曾短暂导致美国科技股下跌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**标签**: `#AI funding`, `#Moonshot AI`, `#large language models`, `#China AI`, `#startup valuation`

---

<a id="item-12"></a>
## [中国反网络暴力法草案将 AI 网暴纳入规制](https://mp.weixin.qq.com/s/PrzKFhbwjgFEGBPADvFD6Q) ⭐️ 8.0/10

2026 年 7 月 29 日，国家互联网信息办公室发布《反网络暴力法（征求意见稿）》公开征求意见，首次将利用 AI 技术制作、传播网络暴力信息纳入专门规制。 这标志着中国在 AI 治理方面迈出重要一步，应对自动化骚扰带来的新危害。该法律可能重塑科技平台监控和缓解 AI 驱动滥用的方式，影响国内及在华运营的全球平台。 草案共 60 条，明确平台建立监测识别和防护功能的义务，构建多部门协同治理体系。受害者有权请求人格权侵害禁令和精神损害赔偿，体现了对网络暴力的综合应对。

telegram · zaihuapd · 7月29日 10:59

**背景**: 网络暴力是指通过网络集中或持续侵害他人名誉权、隐私权、个人信息等合法权益的行为。AI 工具可通过深度伪造、机器人骚扰和自动生成内容放大滥用。中国持续加强网络治理，该法律将保护扩展至 AI 造成的伤害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cac.gov.cn/2026-07/29/c_1787072711938509.htm">国家互联网信息办公室关于《中华人民共和国反网络暴力法（征求意见稿...</a></li>
<li><a href="https://www.news.cn/politics/20260729/c7c9efa1710c45a78e443ced3a4def93/c.html">反网络暴力法公开征求意见 - 新华网</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#online violence`, `#China`, `#cybersecurity policy`, `#digital rights`

---

<a id="item-13"></a>
## [OpenAI 向 10 万学者免费提供前沿模型](https://openai.com/index/chatgpt-for-academic-researchers/) ⭐️ 8.0/10

2026 年 7 月 29 日，OpenAI 宣布推出“ChatGPT for Academic Researchers”项目，计划到 2027 年向 10 万名科学、数学和工程领域的研究人员免费提供其 GPT-5.6 前沿模型。首批 1 万名参与者于今年夏天开放申请。 这一举措可能通过为研究人员提供强大的 AI 工具（如文献综述、假设检验、基金申请等）显著加速科学发现。同时加强了 OpenAI 与学术界的联系，并可能促使其他 AI 公司推出类似项目。 参与者可使用 GPT-5.6 模型（包括 Sol、Terra 和 Luna 变体），并邀请最多四名机构合作者。工作区默认不将数据用于模型训练。该项目是 OpenAI 到 2027 年投入 2.5 亿美元支持外部科研的一部分。

telegram · zaihuapd · 7月30日 00:17

**背景**: GPT-5.6 是 OpenAI 于 2026 年 7 月 9 日发布的大型语言模型家族，包含三个能力层级：Luna、Terra 和 Sol。初期因政府限制仅限小范围使用，随后全面开放。OpenAI 此前曾通过“ChatGPT for Nonprofits”等项目向研究人员提供免费访问，但新项目规模大幅扩大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/chatgpt-for-academic-researchers/">Accelerating scientific discovery with ChatGPT for Academic ...</a></li>
<li><a href="https://www.axios.com/2026/07/29/openai-academics-research-chatgpt-sol">OpenAI launches free AI access program for academic researchers</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#学术研究`, `#AI模型`, `#免费`, `#GPT-5.6`

---

<a id="item-14"></a>
## [字节最大 To B 变革：飞书并入豆包与火山引擎](https://news.qq.com/rain/a/20260730A03CAP00) ⭐️ 8.0/10

字节跳动重组其企业软件业务，将飞书产品团队与豆包 AI 团队合并，组成新的“豆包产品团队”，并将飞书的市场、销售及客户服务团队整合进火山引擎，成立“创造力服务平台”。 这是字节跳动成立以来 To B 业务最大规模的组织变革，标志着 AI 与企业协作及云服务的深度融合，可能重塑中国企业软件市场的竞争格局。 飞书现有产品及服务保持不变，但将与豆包深化生产力场景合作；双方共同开发的豆包企业版已在部分飞书客户中内测。

telegram · zaihuapd · 7月30日 02:55

**背景**: 飞书是字节跳动的企业协作平台（国际版称为 Lark），豆包是字节跳动领先的 AI 聊天机器人和多模态助手，拥有超过 5000 万活跃用户，火山引擎是字节跳动的云服务平台，提供 AI 和数据分析解决方案。此次重组旨在使字节的 To B 业务与其 AI 能力更紧密地结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lark_(software)">Lark (software) - Wikipedia</a></li>
<li><a href="https://moge.ai/product/doubao">豆包:Advanced multimodal AI platform by ByteDance offering... - MOGE</a></li>
<li><a href="https://baike.baidu.com/en/item/Volcano+Engine/1423148">Volcano Engine（ByteDance's cloud service platform）_Baiduwiki</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#enterprise software`, `#AI`, `#restructuring`, `#Feishu`

---

<a id="item-15"></a>
## [Vision Pro 用于建筑比例评估](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 7.0/10

Christian Selig 的文章强调了使用 Apple Vision Pro 进行建筑可视化，让用户在 3D 建筑模型中行走，直观地评估比例和尺度。 这展示了混合现实头显的一个实用、以生产力为中心的用例，为建筑师、设计师和客户提供了在施工前进行虚拟漫游的重要价值。 该方法使用真实比例渲染和空间计算，Rhino3D、Revit 和 Enscape 等工具支持工作流程。Apple Vision Pro 以及 Quest 3 和 HTC Vive 等头显都已成功使用。

hackernews · robbiet480 · 7月29日 20:39 · [社区讨论](https://news.ycombinator.com/item?id=49102774)

**背景**: Apple Vision Pro 是一款于 2024 年发布的混合现实头显，运行 visionOS，支持眼动、手势和语音控制。空间计算将数字模型与现实世界融合，实现沉浸式建筑漫游。该技术帮助客户和设计师直观评估尺度和比例，减少代价高昂的设计错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Vision_Pro">Apple Vision Pro</a></li>
<li><a href="https://www.bulbapp.io/p/67f1f3c9-e06e-45ce-a930-b9f0dec96afc/the-future-of-architecture-through-the-lens-of-spatial-computing">The Future of Architecture Through the Lens of Spatial Computing</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人经验：一家设计公司日常使用 Quest 3 配合 Rhino3D/Revit；另有人在十年前就使用 HTC Vive 和 IrisVR。建议包括模拟太阳角度进行光照分析，以及在建造后通过现有墙壁追踪布线和管道。Christian Selig 因之前开发 Apollo Reddit 客户端而受到称赞。

**标签**: `#Vision Pro`, `#AR/VR`, `#Architecture`, `#Spatial Computing`, `#Design`

---

<a id="item-16"></a>
## [AI 公司招聘数千名电工和木匠建设数据中心](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html) ⭐️ 7.0/10

AI 公司正在招募数千名电工、木匠等技工来建设数据中心，标志着劳动力需求向技术行业的重大转变。 这一趋势突显了 AI 扩张所需的实体基础设施，可能为技工提供稳定且高薪的职业，对更广泛的经济和劳动力发展产生影响。 招聘激增是由于需要为容纳 AI 服务器的数据中心进行实体建设，这些工作不易自动化或外包。

hackernews · thm · 7月29日 14:43 · [社区讨论](https://news.ycombinator.com/item?id=49098198)

**背景**: 数据中心是容纳大量服务器和计算设备的设施，对运行 AI 模型和云服务至关重要。建设过程中需要大量的电气和木工工作。随着 AI 需求的增长，对新数据中心的需求也在增加，从而推动了建筑相关行业的繁荣。

**社区讨论**: 评论者对数据中心建设工作的繁荣-萧条周期性表示谨慎，认为职业稳定性可能不确定。一些人对技工获得更高薪酬和更多机会表示欢迎。

**标签**: `#labor`, `#data centers`, `#AI infrastructure`, `#trades`, `#economy`

---

<a id="item-17"></a>
## [D. Richard Hipp 谈 SQL 取代 COBOL 程序员](https://simonwillison.net/2026/Jul/29/d-richard-hipp/#atom-everything) ⭐️ 7.0/10

SQLite 的创建者 D. Richard Hipp 将 SQL 的出现取代 COBOL 程序员与当前编程自动化趋势进行了历史类比，指出编程工作只是发生了变化而非消失。 这一见解为 AI 和自动化对软件工程职业的影响提供了令人安心的视角，强调程序员的角色会适应而非消失，这与当前关于 AI 取代工作的讨论高度相关。 该引述出自 Hipp 的一个 YouTube 演讲，他简化了历史：在 SQL 出现之前，查询大型数据集需要编写自定义代码，这项工作由 COBOL 程序员完成；SQL 允许以声明方式指定查询，消除了这一需求，但将程序员转向更高层次的任务。

rss · Simon Willison · 7月29日 21:15

**背景**: COBOL 是 1960-80 年代主流的商业编程语言，广泛用于数据处理和报表生成。程序员必须手动编写算法来遍历文件并生成报告。SQL（结构化查询语言）发明于 1970 年代，随关系数据库普及，允许用户指定所需数据而无需编写过程式代码，大大减少了数据检索所需的工作量。

**标签**: `#sql`, `#d-richard-hipp`, `#career`, `#automation`, `#software-history`

---

<a id="item-18"></a>
## [模块化数据中心：解决劳动力与可扩展性挑战](https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters) ⭐️ 7.0/10

Semianalysis 的一篇文章探讨了如何采用类似乐高积木的模块化建造方式，来解决现代数据中心面临的劳动力短缺和可扩展性问题。 随着人工智能和云计算推动数据中心需求激增，传统建造方式已无法跟上；模块化提供了更快的部署速度并减少了对熟练劳动力的依赖，这对基础设施行业至关重要。 模块化数据中心使用在工厂预制、现场组装的模块（电源、冷却、IT），将建造时间从数月缩短至数周。这种方法还实现了可重复设计并便于扩展。

rss · Semianalysis · 7月29日 22:09

**背景**: 传统数据中心建造面临劳动力短缺、成本高昂和工期漫长等问题。已在医疗等其他行业应用的模块化建造，将预制化引入数据中心，提供了速度、成本可预测性和质量。施耐德电气和维谛等公司提供针对高密度 AI 工作负载的预制模块化解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://encoradvisors.com/modular-data-center/">The Modular Data Center Ultimate Guide [2025] - ENCOR Advisors</a></li>
<li><a href="https://www.moduledge.com/blog/modular-data-center-guide">Modular Data Center Guide: Types & When It Wins | ModulEdge</a></li>
<li><a href="https://www.se.com/us/en/product-category/7550-prefabricated-data-center-modules/">Prefabricated Data Center Modules - Schneider Electric USA</a></li>

</ul>
</details>

**标签**: `#datacenters`, `#modularization`, `#infrastructure`, `#labor`, `#construction`

---

<a id="item-19"></a>
## [中国电信停止第三方互联网渠道销售 SIM 卡](https://www.189.cn/web/notice/detail?order=1&amp;offerCode=519526800001&amp;provinceCode=600304) ⭐️ 7.0/10

中国电信于 7 月 31 日发布公告，自 8 月 1 日起，第三方互联网渠道不再提供电信号卡办理业务。有群友在其官网上发现了该通知。 作为国有大型电信运营商，中国电信的这一政策调整可能显著改变中国 SIM 卡的在线分销格局，影响电商平台，并可能涉及防欺诈或渠道管控策略。 该公告落款日期为 7 月 31 日，8 月 1 日起生效，但群友还发现了另一个日期为 7 月 29 日、省份代码不同的链接，暗示可能存在地方差异或更正。

telegram · zaihuapd · 7月29日 12:45

**背景**: 中国电信是中国三大国有电信运营商之一。第三方互联网渠道，如淘宝、京东等电商平台，一直是 SIM 卡销售的常见渠道。此举可能是监管在线销售和减少欺诈的更广泛努力的一部分。

**社区讨论**: 群友发现了该公告，并指出一处不一致：另一个类似公告的日期为 7 月 29 日且省份代码不同，引发了关于地方实施或早期版本的猜测。

**标签**: `#China Telecom`, `#Telecommunications`, `#Regulation`, `#Internet Sales`, `#Policy Change`

---

<a id="item-20"></a>
## [英国监管机构拟要求苹果开放 App Store 外部支付](https://www.macrumors.com/2026/07/29/app-store-uk-rules-highly-intrusive/) ⭐️ 7.0/10

英国竞争与市场管理局（CMA）提议要求苹果允许开发者引导用户使用外部支付方式，减少对苹果内购系统的依赖。苹果回应称该提案“过度介入”，相当于价格管制。 这一监管举措可能通过降低开发者支付的 30%佣金来重塑 App Store 的经济模式，并可能为消费者带来更低价格。同时，它为欧盟《数字市场法案》等其他司法管辖区树立了先例，影响全球应用商店监管。 CMA 拟议的行为要求允许开发者包含外部支付方式链接，但苹果仍可收取低于当前佣金水平的“公平合理”费用。该提议同样适用于谷歌，CMA 仍在评估反馈意见，尚未做出最终决定。

telegram · zaihuapd · 7月30日 02:10

**背景**: 苹果 App Store 要求开发者使用其内购系统，对数字商品和服务收取最高 30%的佣金。批评者认为这抑制了竞争并推高了消费者价格。英国自 2025 年 1 月起生效的新数字市场竞争制度，将苹果和谷歌在移动生态系统中指定为具有“战略市场地位”，使其受到定制行为要求的约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.uk/government/news/cma-secures-commitments-from-apple-and-google-to-improve-fairness-in-app-store-processes-and-enhance-ios-interoperability">CMA secures commitments from Apple and Google to improve ...</a></li>
<li><a href="https://www.gov.uk/cma-cases/investigation-into-apple-appstore">Investigation into Apple AppStore - GOV.UK UK Consumers to CMA: Don't Put App Store Safety and Security ... Improving the way Apple and Google deliver app store services ... Apple says UK App Store proposal amounts to price regulation UK watchdog plans to break Apple and Google’s ‘effective ... Apple Says UK App Store Steering Rules Would Be 'Highly ...</a></li>
<li><a href="https://ccianet.org/news/2026/07/uk-consumers-to-cma-dont-put-app-store-safety-and-security-at-risk/">UK Consumers to CMA: Don't Put App Store Safety and Security ...</a></li>

</ul>
</details>

**标签**: `#App Store`, `#regulation`, `#antitrust`, `#UK`, `#payments`

---
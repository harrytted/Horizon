---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 34 条内容中筛选出 20 条重要资讯。

---

1. [Stripe 以超 70 亿美元收购 AI 网关 OpenRouter](#item-1) ⭐️ 9.0/10
2. [Anthropic 公开 Claude 系统提示词，方便社区分析追踪](#item-2) ⭐️ 8.0/10
3. [Qwen 3.8 27B 表现出色但默认推理过度](#item-3) ⭐️ 8.0/10
4. [PJM 建模错误浪费 120 亿美元，用户或再遭损失](#item-4) ⭐️ 8.0/10
5. [SSOG-Attention：用可分离高斯和实现次二次注意力](#item-5) ⭐️ 8.0/10
6. [Anthropic 第二季初步营收超 115 亿美元，同比激增 14 倍](#item-6) ⭐️ 8.0/10
7. [嵌入式工程师为 RISC-V 在发展中世界的可及性辩护](#item-7) ⭐️ 7.0/10
8. [前沿模型故意'变笨'：知识从权重转向外部工具](#item-8) ⭐️ 7.0/10
9. [AI 额度转售经济兴起：Token 经纪商涌现](#item-9) ⭐️ 7.0/10
10. [Firefox for iOS 新增原生广告拦截功能](#item-10) ⭐️ 7.0/10
11. [Cloudflare 切换域名服务器后静默注入分析脚本](#item-11) ⭐️ 7.0/10
12. [三根控制棒落入堆芯，圣露西核电站 1 号机组手动停堆](#item-12) ⭐️ 7.0/10
13. [重新审视 ECA 论文：跨通道交互假设存在缺陷](#item-13) ⭐️ 7.0/10
14. [阿莫迪：公众对 AI 的不信任反映更广泛的制度信任危机](#item-14) ⭐️ 6.0/10
15. [SineKAN：在 Kolmogorov-Arnold 网络中使用正弦激活函数](#item-15) ⭐️ 6.0/10
16. [如何解决线性注意力模型中的长距离召回问题？](#item-16) ⭐️ 6.0/10
17. [美国要求盟友签署 Pax Silica，否则或遭 AI 排挤](#item-17) ⭐️ 6.0/10
18. [AI 工具追踪 Telegram 盗版，524 个频道被关闭](#item-18) ⭐️ 6.0/10
19. [SafePal 披露数据泄露，约 4 万名客户受影响](#item-19) ⭐️ 6.0/10
20. [Codex 开启百万 Token 上下文窗口，GPT-5.6 Sol 支持 105 万 Token](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Stripe 以超 70 亿美元收购 AI 网关 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 9.0/10

Stripe 已完成对 OpenRouter（一家人工智能模型路由与 API 网关平台）的收购，交易金额超过 70 亿美元。该消息于 2026 年 8 月 16 日前后报道，是支付公司参与的规模最大的人工智能基础设施交易之一。 这笔交易表明，AI 模型访问正在成为核心支付和 API 基础设施，Stripe 正将自己定位为金融交易和 LLM token 使用的中间人。它可能重塑开发者购买 AI 算力的方式以及 AI 实验室处理支付的路径，对 AWS Bedrock、OpenAI 和其他提供商产生重大影响。 据报道，OpenRouter 在几个月前刚刚以 13 亿美元的估值融资，随后以 70 亿美元的价格被收购。该交易还发生在 OpenAI 决定将支付处理从 Stripe 迁移至 Adyen 之后，而 OpenRouter 掌握着各大 AI 实验室相当大比例的模型 API 支付量。

hackernews · zacharyozer · 8月16日 20:31 · [社区讨论](https://news.ycombinator.com/item?id=49323381)

**背景**: OpenRouter 是一个统一的 API 网关和市场，能将单个兼容 OpenAI 的请求路由到超过 60 家提供商的 400 多个大语言模型和其他 AI 模型，自动根据成本、速度和可靠性选择主机，并将计费整合到一个账户中。在更广泛的生态系统中，AI 模型路由是一种关键的基础设施模式，包括成本优化的模型选择、推理负载均衡以及抽象供应商复杂性的统一 API 网关。Stripe 作为全球顶尖的 API 公司之一，一直以抽象金融支付基础设施为核心业务，现在正将这一模式扩展到 LLM token 领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/openrouter">OpenRouter API and Models | OpenRouter</a></li>
<li><a href="https://www.knolli.ai/post/what-is-openrouter">What Is OpenRouter? A Practical Guide to AI Model Routing</a></li>
<li><a href="https://aiwiki.ai/wiki/openrouter">OpenRouter - AI Wiki</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为，这笔交易是 Stripe 的战略举措，目的是在失去 OpenAI 的 Adyen 支付业务后，不仅掌控支付，还要主导 LLM 的'管道'并锁定 AI 相关支付量。也有人质疑，一个'API 调用中间商'凭什么比 Lyft 或 Dolby 市值还高；另一些人则指出网络效应、转换成本和 Stripe 的分发能力是核心价值。还有人注意到价值从几个月前的 13 亿美元飙升至 70 亿美元，并希望员工也能从中受益。

**标签**: `#AI`, `#Acquisitions`, `#Payments`, `#OpenRouter`, `#Stripe`

---

<a id="item-2"></a>
## [Anthropic 公开 Claude 系统提示词，方便社区分析追踪](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 在其平台发布说明中公开了 Claude 模型的官方系统提示词，任何人都能看到这些默认提示词。本次发布让开发者与研究者可以检查 Claude 收到的具体指令，并追踪这些提示词随模型版本如何变化。 这是商用 AI 系统迈向透明化的重要一步，因为这类系统通常不公开系统提示词。它能帮助开发者理解模型行为、复现结果，并在提示词意外变化时调整自己的应用。 Simon Willison 将这些提示词整理成 git 提交历史，方便查看差异，并指出了 Opus 4.8 与 Opus 5 之间的一些重要新增内容。由于系统提示词会附加到每次 API 调用并占用上下文窗口的 token，其长度和内容直接影响成本与模型行为。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 系统提示词是附加到每次发给大语言模型的请求之前的指令块，用来定义模型的行为、性格、约束和任务上下文。由于它每次调用都会占用一部分上下文窗口的 token 预算，提示词的长度和清晰度会明显影响模型表现。许多 AI 实验室将这类提示词视为机密，因此 Anthropic 公开发布说明不同寻常，也让社区难得地看到了内部信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackernoon.com/system-prompts-under-the-hood-how-llms-learn-to-follow-instructions">System Prompts Under the Hood: How LLMs Learn to... | HackerNoon</a></li>
<li><a href="https://docs.runanywhere.ai/web/llm/system-prompts">System Prompts - RunAnywhere Documentation</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices">Prompting best practices - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上欢迎这种透明化：simonw 用 git 为提示词建立了变更追踪工具，ololobus 则指出部分常规指令（比如 Claude 自行检查图片是否真的上传）更像是通用常识而非真正的推理。也有人提出担忧，SwellJoe 认为这些提示词比实际需要的更长，而模型通常在更短、干扰更少的指令下表现更好；另有一条题外评论质疑该论坛会移除批评 AI 的帖子。

**标签**: `#Claude`, `#system prompts`, `#Anthropic`, `#AI transparency`, `#LLM`

---

<a id="item-3"></a>
## [Qwen 3.8 27B 表现出色但默认推理过度](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

阿里巴巴 Qwen 实验室发布了采用 Apache 2 许可证、具备视觉能力的 27B 参数大语言模型 Qwen 3.8 27B，其基准测试成绩超过 Qwen 3.6 27B 以及闭源的 Qwen 3.7-Plus。Simon Willison 在测试中发现，默认的“xhigh”推理强度会让模型在简单问题上也消耗大量 token 和时间，进行过度思考。 此次发布意义重大，因为一款可在笔记本电脑上运行的强大开源权重 27B 模型缩小了与闭源模型的差距，为开发者提供了灵活的本地方案。默认的过度思考行为凸显了推理强度控制在实际部署中的重要性，直接影响消费级硬件上的延迟和成本。 该模型支持可配置的 reasoning_effort 参数，分为 xhigh、medium 和 low 三档，默认值为 xhigh。Simon Willison 在 M5 Max MacBook Pro 和 NVIDIA DGX Spark 上运行了 17GB 的 Q4_K_M 量化版，发现默认的 8,192 token 上下文限制会被推理过程占满；将上下文增至 262,144 token 后，一次复杂的 SVG 生成耗时 21 分钟，使用了 22,276 个推理 token。

rss · Simon Willison · 8月16日 22:00

**背景**: Qwen 是阿里巴巴云开发的大语言模型系列，最初于 2023 年 4 月以通义千问（Tongyi Qianwen）的名称推出。像 Qwen 3.8 27B 这样的开源权重模型因可在消费级硬件上运行而广受欢迎，而推理强度设置允许用户在准确性与速度、计算成本之间进行权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/why-large-language-models-overthink-what-google-deepminds-njagi-3xonf">Why Large Language Models Overthink: What Google...</a></li>

</ul>
</details>

**标签**: `#qwen`, `#llm`, `#open-source`, `#local-models`, `#ai`

---

<a id="item-4"></a>
## [PJM 建模错误浪费 120 亿美元，用户或再遭损失](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

SemiAnalysis 的一项调查报道指出，PJM 电力市场中的一个建模错误浪费了电费缴纳者 120 亿美元。该报道警告称，PJM 正打算再次采用同样有缺陷的建模方法，可能让用户面临更大风险。 这暴露了美国最大电网运营商在可靠性建模和容量采购方面的系统性缺陷。由于 PJM 服务约 6700 万用户，重复犯错可能再浪费数十亿美元，并削弱公众对电力市场设计的信任。 报道明确指出，问题出在电网规划和容量市场建模上，而不是 AI 或机器学习模型。PJM 运营日前、实时和容量等多个市场，报道所指的浪费来自这些规划模型的错误使用。

rss · Semianalysis · 8月16日 22:27

**背景**: PJM Interconnection 是美国最大的电网运营商，为从芝加哥到新泽西的约 6700 万用户提供服务。在 PJM 的批发市场中，公用事业公司通过能源市场购买电力，并通过容量市场为未来高峰时段的充足发电能力付费。容量市场中的建模错误可能导致过度采购或未来供应定价错误，而这些成本最终会转嫁给电费缴纳者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PJM_Interconnection">PJM Interconnection - Wikipedia</a></li>
<li><a href="https://www.pjm.com/markets-and-operations/energy.aspx">PJM - Energy Market</a></li>
<li><a href="https://www.ferc.gov/understanding-wholesale-capacity-markets">Understanding Wholesale Capacity Markets | Federal Energy Regulatory Commission</a></li>

</ul>
</details>

**标签**: `#energy`, `#grid`, `#modeling`, `#PJM`, `#infrastructure`

---

<a id="item-5"></a>
## [SSOG-Attention：用可分离高斯和实现次二次注意力](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

SSOG-Attention 用可分离高斯和替代标准缩放点积注意力（SDPA），将复杂度从 O(N²·d) 降至 O(N√N·d)。实验显示，它在 CIFAR-100 上胜过 SDPA，在 ImageNet 上与 SDPA 表现相当且收敛更快。 这项工作直接针对限制 Transformer 扩展性的二次方计算和内存瓶颈，对视觉 Transformer 和长序列应用具有重要意义。如果得到广泛验证，类似 SSOG 的次二次注意力有望使大规模模型更加高效。 SSOG 为每个注意力头学习少量高斯原子，并根据查询令牌在几何上调整它们，而无需对所有令牌打分。由于原子可分解为可分离高斯和，随着输入规模增大该方法在速度和内存上更具优势；相关代码和博客文章已公开发布。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**背景**: 标准缩放点积注意力（SDPA）会计算所有查询令牌与键令牌之间的相似度，导致 Transformer 的时空复杂度为 O(N²·d)。为克服这一问题，研究者提出了许多次二次注意力变体，通常利用线性化或稀疏化，但许多变体缺乏严格的误差保证。SSOG 则学习由可分离高斯构成的几何注意力场，完全避免显式的两两打分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/4rtemi5/ssog/blob/main/README.md">ssog/README.md at main · 4rtemi5/ssog · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2209.04881">[2209.04881] On The Computational Complexity of Self-Attention</a></li>

</ul>
</details>

**社区讨论**: 初步讨论对这一想法表示欢迎，但提出了关键问题：为换取速度会牺牲多少长程信息召回能力。有评论者认为这是一条值得测试的路径，同时也质疑效率与远距离信息检索能力之间的权衡。

**标签**: `#efficient-attention`, `#machine-learning`, `#transformers`, `#computer-vision`, `#sub-quadratic`

---

<a id="item-6"></a>
## [Anthropic 第二季初步营收超 115 亿美元，同比激增 14 倍](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic 公布第二季初步营收超过 115 亿美元，较去年同期的 7.87 亿美元同比增长逾 14 倍，并实现调整后营业利润转正。这些数字仍属初步数据、可能调整；据报道，该公司正在筹备最早可能于今年秋季进行的大型 IPO。 这标志着 Anthropic 的一个重大商业里程碑，表明领先的 AI 实验室能够将激增的需求转化为大规模营收和正向营业利润。这也增强了其高关注度 IPO 的前景，届时公开市场投资者将获得一家更纯粹的头部大模型公司标的。 环比增长同样强劲：营收从 2026 年第一季度的 47.3 亿美元升至第二季度的 115 亿美元以上。所公布的数字为初步数据，因此在任何与 IPO 相关的披露前，最终结果仍可能发生变化。

telegram · zaihuapd · 8月16日 07:26

**背景**: Anthropic 是 Claude 系列大语言模型背后的 AI 公司，也是 OpenAI 等基础模型实验室的主要竞争对手。其营收猛增反映了企业对 AI 助手和 API 服务的强劲采用；所谓“调整后营业利润”通常剔除股权激励等一次性项目，能更清晰地反映核心经营状况。此前业界普遍报道，该公司正在考虑于 2026 年进行 IPO。

**标签**: `#Anthropic`, `#AI`, `#revenue`, `#IPO`, `#business`

---

<a id="item-7"></a>
## [嵌入式工程师为 RISC-V 在发展中世界的可及性辩护](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

在 rvembedded.com 上的一篇博客文章中，一位来自发展中世界的嵌入式工程师回应了批评文章《RISC-V 他们本应更懂行》，认为尽管存在性能和碎片化问题，但 RISC-V 的低成本和高可及性使其具有独特价值。 这一回应将发展中世界开发者的罕见视角带入了 RISC-V 的讨论，凸显了成本和供应链障碍如何影响架构选择。它强调，RISC-V 对嵌入式计算的影响不能仅以高性能指标来衡量。 作者将十美分的 RISC-V 芯片与一美元的替代品进行对比，认为在他的地区，价格差异非常重要，同时指出小额订单的运费高达 60 至 200 美元。原批评文章重点关注 RISC-V 相对于 ARM64 的性能表现以及可选 ISA 扩展导致的碎片化问题。

hackernews · Narishma · 8月16日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49321717)

**背景**: RISC-V 是一种开放标准的指令集架构（ISA），任何人无需支付许可费即可用它设计处理器，因此对嵌入式系统很有吸引力。与 ARM 不同，RISC-V 允许设计者根据具体应用添加或删除指令，这可能导致不同实现之间出现碎片化。为解决这一问题，RISC-V International 已为标准 Linux 级 CPU 引入了 RVA22 和 RVA23 等基础配置文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://riscv.org/specifications/ratified/">Ratified Specifications - RISC - V International</a></li>
<li><a href="https://www.stromasys.com/resources/all-about-the-risc-v-processors/">RISC - V Processors: The Comprehensive Guide (2026)</a></li>
<li><a href="https://www.cnx-software.com/2019/03/10/risc-v-compliance-tests-risc-v-fragmentation/">RISC - V Compliance Tests Aim to Address RISC - V Fragmentation</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，作者似乎并未直接回应原批评，因为原文关注的是 RISC-V 的性能和二进制分发问题，而非嵌入式成本优势。有人质疑成本和运费论述的连贯性，也有人以历史类比，认为 RISC-V 的性能最终会像当年的 x86 赶上 RISC 工作站那样追上 ARM 和 x86。

**标签**: `#RISC-V`, `#embedded systems`, `#hardware`, `#cost analysis`, `#developing countries`

---

<a id="item-8"></a>
## [前沿模型故意'变笨'：知识从权重转向外部工具](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 7.0/10

文章认为，前沿大语言模型正在有意放弃记忆事实，转而依赖工具检索，这让它们在纯回忆类基准上显得'更笨'，但可能减少幻觉。作者还预测，模型卡上的知识截止日期未来可能消失，因为权重中保留的知识会变成以年计的缓慢变化。 这一转变可能重塑行业评估和构建大模型的方式，从'越大越聪明'转向模块化、可插拔知识的工具增强系统。它影响到所有依赖事实回忆或以基准分数采购模型的人，也引发对'能力'定义的新思考。 文章引用了事实回忆基准 SimpleQA 的例子，说明参数化记忆的局限：该基准上 Gemini 2.5 Pro 得分仅 53%。批评者指出，这篇帖子由 AI 生成且引用的基准已过时，因为 Gemini 2.5 Pro 已是十六个月前的旧模型。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: 大语言模型有两种知识存储方式：参数化记忆（在训练时将事实'烘焙'进权重）和非参数化记忆（推理时从外部数据库检索信息）。检索增强生成（RAG）是实现后者最主流的技术，让模型在回答前先查阅权威知识库。工具使用则是这一思路的延伸，允许模型调用外部函数和智能体来获取、计算或操作数据。文章的核心论点正是从参数化知识转向这些外部机制，因此这些背景必不可少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG ? - Retrieval - Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://lawrence-emenike.medium.com/a-straightforward-explanation-of-parametric-vs-non-parametric-memory-in-llms-f0b00ac64167">A Straightforward explanation of Parametric vs. Non-Parametric Memory in LLMs | by Lawrence Emenike | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论区观点分歧：有人称赞文章，并提到像 Cactus 的 14MB 工具调用模型 'Needle' 这类新兴小模型，它们无需存储大量世界知识；也有人质疑将知识与推理完全解耦的可行性。一条高赞评论称该文由 AI 生成且内容过时，指出基准和模型已更新；还有人认为事实知识是推理的基础，无法与推理分离。

**标签**: `#AI`, `#LLM`, `#knowledge bases`, `#tool use`, `#model design`

---

<a id="item-9"></a>
## [AI 额度转售经济兴起：Token 经纪商涌现](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

一个二级市场已经出现：'Token 经纪商'从初创公司购买未使用的 AI API 额度，再以大幅折扣转售，这一趋势由研究员 Matt Lenhard 指出。AICreditmart.com 等专门市场现在为 OpenAI、Anthropic、Google 等提供商的额度交易提供便利。 这一灰色市场破坏了 AI 提供商的价格体系和服务条款，同时让买家面临安全和信任风险。它标志着 AI 生态系统已经成熟到将推理额度视为可互换、可套利资产的程度。 转售 AI 额度通常违反发行平台的服务条款，经纪商常以中继或代理方式运作以隐藏账户来源。买家通常可节省 20%-40%，但面临账户被盗、数据泄露以及无法保证实际访问的模型与宣传一致等风险。

hackernews · mlenhard · 8月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**背景**: AI API 额度是 LLM 提供商的预付费使用单位，以 token 计量，每个 token 大约相当于四分之三个英文单词。提供商常为开发者提供免费额度用于注册或推广，初创公司可能会积累超过自身需求的额度。Token 经纪商买入这些闲置额度再打折转售，形成了类似礼品卡套利或忠诚度积分转售的二级市场。这种行为被视为灰色市场，因为它违反平台服务条款，但并不明确违法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.machucavalley.tech/blog/ai-credit-resale-economy-emerging-market/">The New Gold Rush: Welcome to the AI Credit Resale Economy</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-08-17-the-emergence-of-ai-token-brokers-inside-the-growing-secondary-market-for-llm-inference-credits">AI Token Brokers: The New Secondary Market for LLM Credits</a></li>
<li><a href="https://aicreditmart.com/">AICreditmart.com - AICreditMart - Buy & Sell AI Credits</a></li>

</ul>
</details>

**社区讨论**: 评论者反应不一：一些人认为通过廉价额度进行模型蒸馏是一个有趣的角度，而另一些人则斥责这种信任模式很危险，指出买家必须依赖没有信誉审核的第三方。还有人认为研究过于肤浅，指出 linux.do 和 nodeseek.com 等平台上存在规模大得多的 token 转售经济，并质疑买家如何验证自己确实获得了所购买的模型。

**标签**: `#AI`, `#API credits`, `#gray market`, `#token brokerage`, `#arbitrage`

---

<a id="item-10"></a>
## [Firefox for iOS 新增原生广告拦截功能](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) ⭐️ 7.0/10

Firefox for iOS 现已内置原生广告拦截功能，用户无需安装额外扩展即可拦截广告。该功能可拦截来自 Google、Bing、DuckDuckGo 等搜索服务商搜索结果页上的广告。 此更新意义重大，因为 iOS 浏览器历来缺少桌面版那样的扩展灵活性，因此原生广告拦截功能对 iPhone 和 iPad 用户来说是显著的隐私改进。这也表明在当前广告拦截需求高涨之际，Mozilla 持续投入移动端隐私保护。 内置拦截功能专门针对 Google、Bing、DuckDuckGo 等搜索结果页上展示的广告。社区用户指出，尽管 Safari 的 uBlock Origin Lite 仍是 iOS 上功能最强的广告拦截器，但 Firefox 的原生方案减少了用户的配置步骤。

hackernews · pentagrama · 8月16日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49319633)

**背景**: 在 iOS 上，所有浏览器都必须使用 Apple 的 WebKit 引擎，而且浏览器扩展比桌面端受限得多。iOS 上的内容拦截通常通过 WebKit content blocker 框架等原生 API 实现，这些 API 允许应用拦截广告、跟踪器和其他不需要的内容。Firefox Focus 是 Mozilla 为 iOS 推出的另一款浏览器，自 2010 年代末就已内置广告拦截功能，而此次新增功能则将类似能力带到了主 Firefox 应用中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/huntingcat/apple-browsers/2.3-content-blocking">Content Blocking | huntingcat/apple-browsers | DeepWiki</a></li>
<li><a href="https://gitlab.com/GhenadieP/ABPKit">WebKit content blocker management framework for iOS and macOS...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：多位用户指出 Safari 上的 uBlock Origin Lite 仍是更强的广告拦截器，也有人提醒说 Firefox Focus 早已通过 iOS 内容拦截器提供了系统级广告拦截功能。一些评论者表达了对未来 iOS 版本支持 Gecko 引擎的期望，并对 iOS 扩展限制感到失望，这也是他们转而使用 Orion 等替代品的原因。

**标签**: `#Firefox`, `#iOS`, `#adblock`, `#privacy`, `#browser`

---

<a id="item-11"></a>
## [Cloudflare 切换域名服务器后静默注入分析脚本](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

有用户报告称，为通过自定义子域名提供 R2 存储桶服务而将域名服务器切换到 Cloudflare 后，Cloudflare 静默地在其纯 HTML 网站中注入了 Web Analytics JavaScript 片段。用户必须先将站点添加到 Analytics 仪表盘，再手动关闭该片段，才能将其禁用。 这件事很重要，因为 DNS 和 CDN 基础设施提供商对流量拥有特权访问权限，而静默修改响应内容会引发 Web 开发者和注重隐私的网站所有者对知情同意与透明度的严重担忧。这也表明默认应明确选择加入（opt-in），并需要仔细审查 CDN 功能。 被注入的脚本来自 static.cloudflareinsights.com/beacon.min.js，并带有包含 token 的 data-cf-beacon 数据。用户可以通过设置 Content-Security-Policy（例如 script-src 'self'）来阻止它，从而只允许加载来自指定来源的脚本；注入可能只在 Cloudflare 代理流量时发生，而在仅 DNS 模式下不会发生。

hackernews · stagas · 8月16日 17:49

**背景**: 将域名服务器切换到 Cloudflare 意味着把域名的 DNS 委托给 Cloudflare；如果域名开启了“代理”（橙色云朵），HTTP/S 请求会经过 Cloudflare 边缘节点，Cloudflare 可以终止 TLS 并修改响应内容。该用户是为了通过自定义子域名提供 R2 存储桶服务，而这通常需要通过 Cloudflare CDN 进行代理。Cloudflare Web Analytics 使用来自 static.cloudflareinsights.com 的 JavaScript beacon，这种自动注入行为已在 Cloudflare 社区帖子和博文中被讨论。Content-Security-Policy 可以独立于 Cloudflare 仪表盘设置来阻止此类第三方脚本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://notifire.in/infra/cloudflare-may-be-adding-code-to-your-website">Cloudflare Analytics Script Injected Without User Consent</a></li>
<li><a href="https://burgeonlab.com/blog/cloudflare-web-analytics-rum-injected-tracking-beacon-script-into-my-sites/">Cloudflare Auto Injected Tracking Scripts To My Sites</a></li>
<li><a href="https://developers.cloudflare.com/r2/buckets/public-buckets/">Public buckets · Cloudflare R2 docs</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为这种注入具有侵入性，并确认看到了带有 SRI integrity 属性的 beacon 脚本。有人建议使用 Content-Security-Policy meta 标签将脚本限制为仅自托管来源。另有用户观察到，设置为 DNS-only 的域名并未启用 Web Analytics，这表明注入可能仅在 Cloudflare 代理流量时发生。

**标签**: `#Cloudflare`, `#Privacy`, `#Analytics`, `#DNS`, `#Web Development`

---

<a id="item-12"></a>
## [三根控制棒落入堆芯，圣露西核电站 1 号机组手动停堆](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core) ⭐️ 7.0/10

佛罗里达州圣露西核电站 1 号机组因三根控制棒意外掉入堆芯而被手动停堆。该事件已引发调查，据报道没有放射性物质泄漏或对厂外造成影响。 控制棒意外掉落是核反应堆的重要安全事件，因为它影响反应性控制，尽管美国压水堆被设计为能够安全停堆。社区对此事的高度关注显示出公众对核安全的极大兴趣，也凸显了准确理解反应堆安全系统的必要性。 操作员在三根控制棒插入堆芯后手动停堆，从而降低了反应性。社区专家指出，即使一根控制棒完全插入也可能使美国压水堆低于临界状态；此次事件与完全紧急停堆（SCRAM）不同，2024 年曾发生类似事件，其根源是程序问题和电气故障。

hackernews · toomuchtodo · 8月16日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49320856)

**背景**: 控制棒由吸收中子的材料制成，在裂变反应堆中用于通过调节反应性来控制链式反应。在紧急停堆（SCRAM）时，所有控制棒会快速插入堆芯以终止裂变；在压水堆中，这通常在两到四秒内完成。美国核反应堆设计有多重安全保护层，即使控制棒意外掉落也能安全停堆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scram">Scram - Wikipedia</a></li>
<li><a href="https://www.nuclear-power.com/nuclear-power/reactor-physics/reactor-operation/reactor-shutdown/">Reactor Shutdown | Condition & SCRAM | nuclear -power.com</a></li>

</ul>
</details>

**社区讨论**: 评论总体淡化了风险，解释掉落控制棒是已知的故障模式，美国压水堆即使一根控制棒插入也会低于临界状态。还有人提到 2024 年曾发生类似事件及其根本原因，另一些人则反思为何核事件比天然气厂爆炸更受关注。

**标签**: `#nuclear energy`, `#reactor safety`, `#control rods`, `#infrastructure`, `#incident response`

---

<a id="item-13"></a>
## [重新审视 ECA 论文：跨通道交互假设存在缺陷](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

Reddit 上一篇文章批判性地重新审视了高效通道注意力（ECA）论文，认为其关于跨通道交互的核心假设在概念上存在缺陷。作者在象棋残局库数据上测试 ECA，发现忽略跨通道交互的 k=1 卷积与 k=3 卷积表现几乎一样好，从而对该论文的合理性提出质疑。 ECA 被引用超过 12000 次且被广泛使用，如果其核心理由不正确，可能促使注意力机制设计从跨通道交互转向更简单的逐通道门控。这一批评凸显了经验成功并不能验证解释性论述，鼓励对流行架构进行更严谨的分析。 在 6 子象棋残局库实验中，k=3 的 ECA 测试准确率约为 96.68%，而 k=1 约为 96.61%，表明跨通道交互带来的边际收益很小。作者认为，在通道维度上应用 1D 卷积相当于把通道视为没有固有拓扑的表格数据，因此该操作在概念上并不恰当。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**背景**: 通道注意力机制（如 Squeeze-and-Excitation，SE）通过学习逐通道权重来自适应地重新校准特征图。ECA 提出在通道维度上使用 1D 卷积以实现高效的跨通道交互，并声称这是其相较 SE 获得提升的关键。然而，卷积假设沿有意义轴（如空间或时间）具有局部性和平移不变性，而通道维度并不满足这一假设。作者的象棋残局库实验提供了一个独特基准，因为训练数据可以从完整且无偏的问题分布中采样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA -Net: Efficient Channel Attention for Deep...</a></li>
<li><a href="https://arxiv.org/abs/1709.01507">[1709.01507] Squeeze-and-Excitation Networks - arXiv.org Squeeze-and-Excitation (SE) Block in PyTorch - codegenes.net Squeeze and Excitation (SE) Block - OpenGenus IQ Introduction to Squeeze-Excitation Networks | Towards Data ... Squeeze-and-Excitation Networks. Squeeze-and-Excitation block ... Squeeze-and-Excitation Networks | IEEE Conference Publication ...</a></li>
<li><a href="https://www.emergentmind.com/topics/efficient-channel-attention-eca-mechanisms">Efficient Channel Attention Mechanisms</a></li>

</ul>
</details>

**标签**: `#Attention Mechanisms`, `#Deep Learning`, `#CNN`, `#Paper Critique`, `#Efficient Channel Attention`

---

<a id="item-14"></a>
## [阿莫迪：公众对 AI 的不信任反映更广泛的制度信任危机](https://simonwillison.net/2026/Aug/16/dario-amodei/) ⭐️ 6.0/10

Anthropic CEO Dario Amodei 反驳了“AI 领袖的警告导致公众不信任”的说法，认为这源于人们对企业、政府及科技行业长期存在的信任危机。他表示，真正的解决办法是实际兑现惠及世界的承诺，比如真正治愈癌症，而不是靠营销活动。 这番评论重新框定了 AI 反弹的争论，把责任从风险沟通转向兑现实实在在的好处。由于出自顶级 AI CEO 之口，它会影响整个行业如何应对公众信任和 AI 普及。 Amodei 承认，包括 Anthropic 在内的 AI 公司至今未兑现造福世界的重大承诺，这是最准确的批评。他拒绝“华丽营销活动”的建议，并提醒说“AI 将治愈癌症”这类说法如今听起来更像陈词滥调，且被认为具有欺骗性。

rss · Simon Willison · 8月16日 15:05

**背景**: Dario Amodei 是 Anthropic 的 CEO，这家 AI 公司专注于安全性和可靠性，他曾多次就 AI 风险发声。公众对 AI 的看法越来越负面，部分原因是 AI 高层人物公开发出警告。Amodei 认为，这种反弹主要不是由这些警告引起的，而是源于对机构更深的信任赤字。科技博主 Simon Willison 转发了他的这番评论。

**标签**: `#AI`, `#trust`, `#Anthropic`, `#Dario Amodei`, `#public perception`

---

<a id="item-15"></a>
## [SineKAN：在 Kolmogorov-Arnold 网络中使用正弦激活函数](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

一篇题为《SineKAN：使用正弦激活函数的 Kolmogorov-Arnold 网络》的论文将 KAN 中的 B 样条基函数替换为正弦激活函数。该工作已在 arXiv、GitHub 和经过同行评审的 MDPI 期刊上发表。 这为基于 B 样条的 KAN 提供了一种更简单的替代方案，同时实现了具有竞争力的性能，可能使 KAN 更易于实现和采用。它促进了神经架构中超越传统 MLP 的激活函数探索。 arXiv 论文（编号 2407.04149）由 Eric A. F. Reinhardt 等三位作者撰写。MDPI 版本（《数学》期刊，13 卷 19 期，3157 页）经过了同行评审，GitHub 仓库提供了代码。

reddit · r/MachineLearning · /u/jacobgorm · 8月17日 00:46

**背景**: Kolmogorov-Arnold 网络（KAN）是一种受 Kolmogorov-Arnold 表示定理启发的神经网络架构，该定理指出多元函数可以由一元函数的复合来表示。与传统多层感知机（MLP）使用固定激活函数和线性权重不同，KAN 将每个权重替换为可学习的一元函数，通常用 B 样条参数化。B 样条是一种具有最小支撑的分段多项式基函数，广泛用于曲线拟合和计算机图形学。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/B-spline">B-spline</a></li>

</ul>
</details>

**标签**: `#KAN`, `#Activation Functions`, `#Neural Networks`, `#Machine Learning`

---

<a id="item-16"></a>
## [如何解决线性注意力模型中的长距离召回问题？](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 6.0/10

一位从事 DNA 序列建模的研究人员报告，线性注意力模型在“大海捞针”式基准测试中召回率仅约 25%，接近 DNA 四种碱基词汇的随机水平，连 HyenaDNA 也仅获得 25%–27%。他们测试了一个 16K 上下文的小模型，召回率可达 50%–60%，但随着上下文变长性能急剧下降，因此开始寻找架构层面的解决方案。 这凸显了线性注意力在长上下文基因组建模中的根本局限，因为 DNA 序列很容易达到 100 万 tokens。在不回退到昂贵的 softmax 注意力的前提下解决长距离召回问题，将有助于构建高效、可扩展的 DNA 基础模型。 该“大海捞针”测试使用四个 DNA 碱基（A/C/G/T），因此随机水平为 25%。作者尝试修改线性架构，但召回率仅提升到约 27%，仍近似随机。他们明确希望找到能扩展到百万 token DNA 序列的方法。

reddit · r/MachineLearning · /u/No-Coffee-8227 · 8月16日 07:47

**背景**: 线性注意力用固定大小的状态来近似 softmax 注意力，避免了标准 Transformer 中随序列长度线性增长的 KV 缓存，从而实现次二次方扩展。然而，这种压缩状态可能难以精确检索遥远信息，这一局限性正被“大海捞针”基准测试所揭示。HyenaDNA 是基于 Hyena 算子构建的基因组基础模型，同样采用次二次方方法，支持高达 1M 上下文，但在此类召回任务上表现也不佳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://haileyschoelkopf.github.io/blog/2024/linear-attn/">Linear Attention Fundamentals | Hailey Schoelkopf</a></li>
<li><a href="https://github.com/HazyResearch/hyena-dna">GitHub - HazyResearch/hyena-dna: Official implementation for HyenaDNA, a long-range genomic foundation model built with Hyena · GitHub</a></li>
<li><a href="https://dl.acm.org/doi/10.5555/3666122.3667994">HyenaDNA | Proceedings of the 37th International Conference on Neural Information Processing Systems</a></li>

</ul>
</details>

**标签**: `#linear attention`, `#DNA sequencing`, `#long-range recall`, `#efficiency`, `#sequence modeling`

---

<a id="item-17"></a>
## [美国要求盟友签署 Pax Silica，否则或遭 AI 排挤](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 6.0/10

据报美国国务院的一份信函草案警告盟友及希望与华盛顿开展 AI 合作的国家，必须签署 Pax Silica 宣言，且不能加入与其冲突的重复倡议，否则可能被排除在美国主导的 AI 联盟之外。 这可能重塑国际 AI 联盟格局，迫使各国在美国主导的 Pax Silica 阵营与中国相关倡议之间选边站队。此举可能加剧 AI 治理和芯片供应链方面的地缘政治分裂，对科技公司和全球标准产生深远影响。 信函草案据称将签署不具约束力的 Pax Silica 宣言描述为不仅是加入联盟，还意味着不能参加目标冲突的重复倡议。Pax Silica 由美国国务院协调，于 2025 年 12 月与首批伙伴国签署宣言时启动。

telegram · zaihuapd · 8月16日 02:30

**背景**: Pax Silica 是美国主导的国际倡议，旨在保障半导体、人工智能和稀土等先进技术的供应链安全，隐含减少对华依赖的目标。它被视为美国主导的、对应世界人工智能合作组织（World Artificial Intelligence Cooperation Organization）的机制，现有成员据报包括日本、韩国、英国和以色列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica</a></li>
<li><a href="https://www.state.gov/pax-silica">Pax Silica - United States Department of State</a></li>
<li><a href="https://grokipedia.com/page/Pax_Silica">Pax Silica</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#geopolitics`, `#Pax Silica`, `#international relations`, `#US alliances`

---

<a id="item-18"></a>
## [AI 工具追踪 Telegram 盗版，524 个频道被关闭](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 6.0/10

研究人员分析了 1,057 个 Telegram 频道和约 20.9 万条帖子，发现其中 983 个频道涉及盗版，帖子累计浏览达 48.5 亿次，涉及 19,033 部影视作品。随后他们开发了 AI 工具 Anti-RIP，扫描约 24.9 万个新频道并标记 802 个疑似盗版频道，测试准确率为 98%；将结果提交给 Telegram 及版权方后，61 天内有 524 个此前未知的频道被关闭。 这表明 AI 可以被有效应用于消息平台上的版权执法，并取得可衡量的实际关闭成果。这可能促使 Telegram 等平台采用类似的自动化审核工具，同时也引发对误报和言论自由的担忧。 Anti-RIP 工具仍存在误报。研究人员使用来自 1,057 个频道的约 20.9 万条帖子来刻画盗版特征，然后扫描了约 24.9 万个新频道并标记出 802 个；该研究凸显了 Telegram 上盗版问题的规模。

telegram · zaihuapd · 8月16日 09:13

**背景**: Telegram 是一款基于云端的即时通讯应用，允许用户创建面向无限受众的频道，因此常被用来分享盗版影视及其他受版权保护的内容。由于 Telegram 规模庞大、通信加密且审核宽松，版权方历来难以清除此类内容。基于 AI 的内容检测技术应运而生，可以通过识别命名规律、链接或元数据等模式来自动发现盗版行为。这项研究显示，当此类工具与平台和版权方共享时，能够在人工举报之外发挥补充作用，并促成实际的频道封禁。

**标签**: `#AI`, `#Piracy`, `#Telegram`, `#Copyright`, `#Research`

---

<a id="item-19"></a>
## [SafePal 披露数据泄露，约 4 万名客户受影响](https://www.reuters.com/legal/litigation/crypto-wallet-provider-safepal-discloses-data-breach-affecting-nearly-40000-2026-08-16/) ⭐️ 6.0/10

SafePal 于 8 月 16 日披露，一起数据泄露导致约 39,798 名客户的订单信息被未授权访问，涉及姓名、地址和购买数据。漏洞存在于订单追踪系统，影响时间为 2025 年 3 月 2 日至 2026 年 4 月 11 日。 此次事件之所以重要，是因为被泄露的个人信息可能被用于针对加密货币钱包用户的定向钓鱼和冒充攻击。尽管钱包敏感数据未被窃取，但这凸显了加密货币行业持续存在的安全挑战，以及加强客户数据保护的必要性。 SafePal 确认助记词、私钥、钱包密码及银行账户信息均未被泄露。公司已修复漏洞，并下架了 30 多个与该事件相关的欺诈网站和钓鱼链接。

telegram · zaihuapd · 8月16日 17:06

**背景**: SafePal 是一家成立于 2018 年的加密货币钱包提供商，提供硬件和软件钱包，帮助用户安全存储数字资产。在加密货币钱包中，助记词（或称种子短语）用于备份授权交易所需的私钥，因此这类数据成为攻击者的主要目标。泄露个人信息的數據洩漏事件常被用于钓鱼攻击，攻击者会利用真实信息编造极具迷惑性的消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/SafePal">SafePal</a></li>
<li><a href="https://safepal.com/en/store/s1">SafePal | The Best Crypto Wallet for Bitcoin, Ethereum ...</a></li>

</ul>
</details>

**标签**: `#security`, `#data-breach`, `#crypto`, `#privacy`, `#safepal`

---

<a id="item-20"></a>
## [Codex 开启百万 Token 上下文窗口，GPT-5.6 Sol 支持 105 万 Token](https://x.com/thsottiaux/status/2089082893804896524) ⭐️ 6.0/10

Tibo 分享了一个配置技巧，可在 Codex 中启用 100 万 Token 的上下文窗口。方法是在 ~/.codex/config.toml 中设置 model_context_window=1000000 和 model_auto_compact_token_limit=900000，底层 GPT-5.6 Sol 模型最高支持 105 万 Token。 这使开发者可以在单个 Codex 会话中处理更大的代码库和更长的对话历史，减少拆分任务或手动总结上下文的必要。随着模型上下文窗口不断扩展，这是对 AI 辅助编码工作流的实用改进。 这些设置是 config.toml 中的顶层键，不放在某个表格（table）下，保存并重启客户端或新建会话后生效。如果不想永久修改，也可以使用命令行参数仅对单次 CLI 会话应用相同配置。

telegram · zaihuapd · 8月17日 00:47

**背景**: Codex 是 OpenAI 开发的 AI 编程代理，可以编写功能、修复 Bug、提出拉取请求，可通过 ChatGPT 网页应用、CLI、桌面应用和 IDE 集成使用。其配置文件 ~/.codex/config.toml 用于控制模型、执行环境和集成。GPT-5.6 是 OpenAI 于 2026 年发布的模型家族，Sol 是其中能力最强的变体，被定位为 OpenAI 最好的编程模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.xkiro.com/guides/tools/codex/">Codex CLI — xKiro Docs</a></li>
<li><a href="https://codex.aifenghao.com/en/config/">Codex CLI config . toml Complete Guide (2026) | Codex CLI Guide</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Codex`, `#context window`, `#GPT-5.6`, `#configuration`, `#AI coding assistant`

---
---
layout: default
title: "Horizon Summary: 2026-08-15 (ZH)"
date: 2026-08-15
lang: zh
---

> 从 33 条内容中筛选出 20 条重要资讯。

---

1. [Cursor 宣布加入 SpaceX，将与 SpaceXAI 共同升级 Grok](#item-1) ⭐️ 10.0/10
2. [将 Doom 渲染器编译进 210 亿参数 Transformer，无需训练](#item-2) ⭐️ 9.0/10
3. [Qwen 3.8 27B：新开源本地大模型获社区好评](#item-3) ⭐️ 8.0/10
4. [走向黑暗：执法部门转向利用漏洞进行黑客攻击](#item-4) ⭐️ 8.0/10
5. [为何 Opus 5 的写作风格让开发者感到困扰](#item-5) ⭐️ 8.0/10
6. [谷歌推动同态加密，助力实用化私有 AI 推理](#item-6) ⭐️ 8.0/10
7. [Firefox 成为最后一个支持 uBlock Origin 的主流浏览器](#item-7) ⭐️ 8.0/10
8. [GLM-5.3 正式发布：具备突现网络能力的编码前沿模型](#item-8) ⭐️ 8.0/10
9. [别分类，去幻觉！更聪明的 LLM 标签技巧](#item-9) ⭐️ 8.0/10
10. [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](#item-10) ⭐️ 8.0/10
11. [美国法官下令谷歌简化第三方应用商店安装](#item-11) ⭐️ 8.0/10
12. [PostgreSQL 高危 to_char 缓冲区溢出漏洞可致任意代码执行](#item-12) ⭐️ 8.0/10
13. [苹果联手阿里训练中国专属 AI 大模型，或成首个获批外企](#item-13) ⭐️ 8.0/10
14. [RustDesk 在 Wayland 上实现真正的无人值守远程访问](#item-14) ⭐️ 7.0/10
15. [AI by Hand：以动手方式理解大语言模型的研究资料库](#item-15) ⭐️ 7.0/10
16. [Mixedbread 发布 Toast 1，一款专用于搜索的 LLM](#item-16) ⭐️ 7.0/10
17. [评估肿瘤 AI 模型的开源 Python 库与无代码仪表盘](#item-17) ⭐️ 7.0/10
18. [Hermes Agent 推出 Bot Mode，支持机器人分工与互聊](#item-18) ⭐️ 7.0/10
19. [苹果提议美国 App Store 外部购买抽成最高 15%](#item-19) ⭐️ 6.0/10
20. [中信旗下信宸资本接近以超 15 亿美元收购阿里游戏灵犀](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Cursor 宣布加入 SpaceX，将与 SpaceXAI 共同升级 Grok](https://x.com/cursor_ai/status/2088249881718919393) ⭐️ 10.0/10

Cursor 官方宣布已被收购，正式成为 SpaceX 的一部分，团队将加入 SpaceXAI。双方将共同优化 Grok、Grok Build、Grok Bot、Grok API 及 Cursor 等产品，目标是让 Grok 成为全球最实用的 AI。 此次收购有望将广泛使用的 AI 编程工具与 SpaceX 的 AI 计划整合，深刻改变 AI 编程与助手领域的格局。它可能加速 Grok 的发展，并让 Cursor 借助 SpaceX 的资源和实时数据能力。 公告中明确提到了 Grok Build、Grok Bot、Grok API 及 Cursor 等将共同优化的产品。此前有报道称，xAI 已于 2026 年 2 月并入 SpaceX，现以 SpaceXAI 的名义运营，负责开发具备语音聊天、图像与视频生成、实时搜索和高级推理等功能的 Grok。

telegram · zaihuapd · 8月14日 15:45

**背景**: Cursor 是一款开发者广泛使用的 AI 代码编辑器，提供 AI 辅助补全、自然语言编辑等功能。Grok 是由原 xAI 于 2023 年 11 月推出的系列大语言模型及聊天机器人，以实时联网和与 X（推特）集成著称。SpaceXAI 即原 xAI，是马斯克旗下 SpaceX 内的 AI 部门，此次交易将头部 AI 编程工具与重要 AI 助手平台整合到一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qz.com/what-is-xai-spacexai-elon-musk">xAI, now SpaceXAI : Elon Musk's AI company explained</a></li>
<li><a href="https://x.ai/">SpaceXAI</a></li>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>

</ul>
</details>

**标签**: `#acquisition`, `#AI`, `#Cursor`, `#SpaceX`, `#Grok`

---

<a id="item-2"></a>
## [将 Doom 渲染器编译进 210 亿参数 Transformer，无需训练](https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/) ⭐️ 9.0/10

作者利用自研编译器将《毁灭战士》的渲染算法直接编译成 210 亿参数 Transformer 的权重，完全无需训练。该模型会根据场景提示生成像素绘制命令，执行这些命令即可还原出经典的 E1M1 画面。 这项工作表明，非平凡的算法可以直接嵌入 Transformer 权重，为可解释性、算法合成以及神经-符号混合系统带来新的可能性。它也挑战了“Transformer 必须经过训练才能完成复杂程序任务”的普遍认知。 渲染一帧需要 3,614 个 token 的提示和 53,747 个生成 token，在 NVIDIA B200 上约需 40 分钟。生成的检查点是标准的 Hugging Face Transformers 格式，无需 trust_remote_code 即可加载，宿主程序仅 43 行 Python 代码。

reddit · r/MachineLearning · /u/notforrob · 8月14日 15:50

**背景**: Transformer 是一种基于自注意力机制的神经网络架构，通常通过大规模数据上的梯度下降进行训练。这项工作另辟蹊径，用编译器将符号计算图直接映射为 Transformer 权重，利用网络结构逐步骤执行 Doom 的渲染算法。相关的“将程序编译进 Transformer 权重”的工作提供了背景，Doom 引擎基于垂直列的渲染方式也是重要上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://towardsdatascience.com/i-built-a-tiny-computer-inside-a-transformer/">I Built a Tiny Computer Inside a Transformer - Towards Data Science</a></li>
<li><a href="https://en.wikipedia.org/wiki/Doom_engine">Doom engine - Wikipedia</a></li>

</ul>
</details>

**标签**: `#transformer`, `#compiler`, `#interpretability`, `#machine-learning`, `#Doom`

---

<a id="item-3"></a>
## [Qwen 3.8 27B：新开源本地大模型获社区好评](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

Qwen 团队发布了 Qwen3.8-27B-FP8，这是一个 270 亿参数的开源权重模型变体，采用 FP8 量化，面向本地部署。社区早期测试显示，它在私有推理基准上可与 Gemma 4 等模型一较高下，并且能在笔记本硬件上运行。 Qwen 是使用最广泛的开源大语言模型家族之一，新版本提升了本地推理能力，为在个人硬件上运行模型的开发者提供了更多实用选择。这一发布也表明非美国 AI 实验室之间的竞争正在加剧，GLM、DeepSeek 等模型同样在快速进步。 FP8 变体面向高效的本地推理，但社区报告指出其 VRAM 占用效率似乎不如 Gemma 4 或 Muse Glimmer，有时解决一个基准问题需要约 5 倍的 token 数量。在 RTX 5090 上使用 ninfer 引擎，据称可达约 138 tokens/秒，约为朴素 llama.cpp 配置的两倍。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**背景**: Qwen 是阿里云构建的大语言模型家族；阿里于 2023 年 4 月以“通义千问”为名开始公测，并在获得监管许可后于 2023 年 9 月向公众开放。其模型架构基于 Meta 的 Llama 设计。Qwen 组织在 Hugging Face 上持续发布大语言模型、大模态模型及其他 AGI 相关项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen">Qwen (Qwen)</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍感到惊艳：CMay 称它是继 Gemma 4 之后第二个能正确通过其私有基准测试的本地模型，尽管消耗了 5 倍的 token；simonw 称其在笔记本上跑出的图是“见过的最好的鹈鹕”；kimsey0 分享在 RTX 5090 上用 ninfer 可达约 138 tokens/秒。也有人指出，这种独特的笔记式思维链可能拖累 MTP 预测，且 VRAM 效率不如 Gemma 4；还有人认为这证明非美国开源模型正在快速追赶。

**标签**: `#LLM`, `#Qwen`, `#local-model`, `#AI`, `#open-source`

---

<a id="item-4"></a>
## [走向黑暗：执法部门转向利用漏洞进行黑客攻击](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/) ⭐️ 8.0/10

密码学工程师 Matthew Green 的新博文指出，执法部门不再要求为加密技术设置后门，而是转而利用软件漏洞来访问设备。这篇文章探讨了这一转变如何重塑“走向黑暗”的争论以及监控的未来。 这很重要，因为它将隐私之争从加密政策领域转移到了软件安全和漏洞披露领域。科技公司、用户和政府都会受到影响，合法黑客技术可能成为主要的监控手段。 文章指出，可供执法部门利用的漏洞数量可能很快达到上限，从而质疑黑客技术作为长期策略的可行性。文章还提到了美国的“漏洞公平裁决程序”（Vulnerabilities Equities Process），该程序决定是披露零日漏洞还是将其保密用于攻击性用途。

hackernews · vslira · 8月14日 20:52 · [社区讨论](https://news.ycombinator.com/item?id=49304447)

**背景**: “走向黑暗”（Going Dark）指的是执法部门越来越无法访问加密通信，他们认为这阻碍了刑事调查。过去，政府曾推动在产品中植入后门，但最近转而采用“合法黑客技术”（lawful hacking），即利用设备和软件中的漏洞。美国的“漏洞公平裁决程序”（VEP）是一个联邦框架，用于权衡是将漏洞披露给厂商，还是保留以用于情报收集和网络行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vulnerabilities_Equities_Process">Vulnerabilities Equities Process - Wikipedia</a></li>
<li><a href="https://www.statewatch.org/media/documents/news/2017/apr/ep-study-hacking.pdf">Legal Frameworks for Hacking by Law Enforcement : Identification...</a></li>
<li><a href="https://www.virtru.com/blog/file-encryption/dark">Going Dark : Why Encryption Shouldn’t Require a Back Door - Virtru</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了历史背景，指出在数字化之前，电话窃听需要铺设物理线路且成本高昂；他们还批评“走向黑暗”的说法，因为如今已经有大量的元数据和监控数据可供执法部门使用。一些评论者怀疑文章中关于漏洞数量存在上限的说法，认为人工智能生成的代码可能会导致更多漏洞。

**标签**: `#encryption`, `#surveillance`, `#law enforcement`, `#security`, `#privacy`

---

<a id="item-5"></a>
## [为何 Opus 5 的写作风格让开发者感到困扰](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) ⭐️ 8.0/10

一篇分析文章指出，Opus 5 的省略式、抽象化沟通风格使其即使能力更强，使用体验却感觉更差。文章和讨论认为，其后期训练可能已偏向智能体间交互而非人类可读性。 这场争论反映了行业正日益转向以智能体为中心的 AI，模型主要与其它模型沟通。这对依赖清晰、人性化交互的开发者和产品设计师至关重要，可能影响他们的工具选择与满意度。 Opus 5 是 Anthropic 的旗舰模型，定价为每百万输入 token 5 美元、每百万输出 token 25 美元，上下文窗口为 100 万 token。社区用户称 Opus 5 行文省略、滥用无生命主语，并频繁“忏悔”错误，使对话令人疲惫。

hackernews · numeri · 8月14日 10:12 · [社区讨论](https://news.ycombinator.com/item?id=49296740)

**背景**: 后期训练是指对基础模型进行对齐和微调、使其具备特定行为的阶段，通常使用人类反馈。文章推测，最近的后期训练可能更看重智能体基准测试上的表现，而非以人类为中心的沟通方式，从而形成一种为其他 AI 智能体优化的风格。Opus 5 的定价与长上下文使其功能强大，但多名开发者表示，在日常工作中更青睐旧模型或竞品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5">Claude Opus 5 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.wam.ae/en/article/17c8lgc-anthropic-rolls-out-opus-model-efficiency-upgrade">Anthropic rolls out Opus 5 AI model in efficiency upgrade</a></li>
<li><a href="https://arxiv.org/html/2607.25886">RSIBench-Data: Benchmarking Data- Centric Research for Recursive...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者大多赞同该分析：有用户觉得 Opus 5 的省略式写作和不必要的抽象令人疲惫，另一用户则转向 OpenAI 的 Sol 以获得更顺畅的体验。还有人推测人类已不再是后期训练的主要受众，亦有少数人称因质量明显下降而回到 4.8 等旧模型。

**标签**: `#AI`, `#LLM`, `#developer-experience`, `#communication`, `#HN-discussion`

---

<a id="item-6"></a>
## [谷歌推动同态加密，助力实用化私有 AI 推理](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 8.0/10

谷歌宣布在同态加密用于 AI 推理方面取得进展，目标是让模型能直接在加密数据上计算，从而实现实用的私有 AI。这项工作针对一个长期挑战：在完全不向云服务商暴露原始用户数据的情况下运行机器学习。 如果同态加密变得实用，企业将无需解密即可在敏感的医疗、金融或个人数据上使用 AI，从而消除采用云服务的一大隐私障碍。这可能重塑对云 AI 的信任，并在受监管行业催生新的隐私保护服务。 尽管取得了进展，同态加密的计算开销仍然巨大：社区成员估计推理任务的成本超过 1000 倍，商业可行性存疑。讨论中还提出了信任问题，认为在用户自有硬件上运行的本地模型可能比任何云端加密计算都更简单、更可靠地保护隐私。

hackernews · u1hcw9nx · 8月14日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49300314)

**背景**: 同态加密是一种密码学技术，允许在加密数据上直接执行计算，而无需事先解密；解密后的结果与对明文数据执行相同操作的结果一致。这使得将数据处理外包给云环境成为可能，同时保证数据安全，即使服务商系统被攻破也无妨。私有 AI 推理将这一思想应用于机器学习，使模型能够在加密输入上生成预测，而无需接触底层数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption</a></li>
<li><a href="https://www.splunk.com/en_us/blog/learn/homomorphic-encryption.html">Homomorphic Encryption: How It Works | Splunk</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体持怀疑态度。评论者强调了同态加密的巨大计算开销，一位硕士论文研究者认为它用于推理并不具备商业可行性，另一位则批评其能耗成本对环境有害。一些用户质疑谷歌的隐私记录，并认为最私密的 AI 是运行在用户自己硬件上的本地模型，而不是在大型数据中心里。

**标签**: `#homomorphic encryption`, `#privacy`, `#AI`, `#machine learning`, `#security`

---

<a id="item-7"></a>
## [Firefox 成为最后一个支持 uBlock Origin 的主流浏览器](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html) ⭐️ 8.0/10

Firefox 现在是唯一仍然完整支持 uBlock Origin 的主流浏览器，而 Chrome 及其他基于 Chromium 的浏览器因谷歌强制推行 Manifest V3 而失去支持。这一变化意味着 uBlock Origin 的完整版本无法再在 Chrome 及其衍生浏览器上运行。 这件事很重要，因为 uBlock Origin 是最流行的广告拦截工具之一，它从 Chrome 和 Edge 中消失会让数十亿用户只能依赖更弱的隐私保护和广告拦截方案。这也凸显了 Firefox 作为最后一个能使用户完全掌控扩展能力的主流浏览器的地位，可能会促使注重隐私的用户转向 Firefox。 Manifest V3 将 webRequestBlocking 权限限制为企业侧载扩展，使普通扩展只能使用功能较弱的 declarativeNetRequest API。目前已有非官方的 Manifest V3 版 uBlock Origin 移植，但缺少原版的部分功能；Firefox 还会在每次更新时人工审核 uBlock Origin 等热门扩展，检查是否有间谍软件或恶意代码。

hackernews · DemiGuru · 8月14日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49303202)

**背景**: Manifest V3（MV3）是谷歌为 Chrome 推出的新一代扩展平台，旨在提升扩展的隐私、安全性和性能。它限制了 uBlock Origin 等强力广告拦截器所依赖的 webRequest 阻塞 API，取而代之的是规则集受限的 declarativeNetRequest API。Chrome 拥有目前最大的浏览器市场份额，因此这一变化影响了绝大多数网民。EFF 等批评者认为，MV3 损害了隐私、安全和创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
<li><a href="https://www.eff.org/deeplinks/2021/12/googles-manifest-v3-still-hurts-privacy-security-innovation">Google’s Manifest V 3 Still Hurts Privacy, Security, and Innovation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Manifest_V3">Manifest V3</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Firefox 还会在每次更新时人工审核 uBlock Origin 等热门扩展；也有人批评谷歌为限制用户自由而破坏了扩展 API。一位用户提到存在非官方的 Manifest V3 版 uBlock Origin 移植，还有用户询问 uBlock Origin Lite 用户在广告拦截方面是否发现了不足。

**标签**: `#browsers`, `#firefox`, `#ublock-origin`, `#manifest-v3`, `#privacy`

---

<a id="item-8"></a>
## [GLM-5.3 正式发布：具备突现网络能力的编码前沿模型](https://z.ai/blog/glm-5.3) ⭐️ 8.0/10

智谱 AI（Z.ai）正式发布了 GLM-5.3，这是一款前沿的开源权重编码模型，展现出突现的网络（cyber）能力。据报道，在关键网络安全测试中它击败了 Anthropic 的 Mythos 5，并已被用于红队场景和大规模漏洞发现，披露了多项 CVE。 此次发布标志着开源权重模型在网络安全等专业领域正在缩小与闭源前沿系统的差距。GLM-5.3 据报道能够发现并适配真实世界的漏洞利用，这可能重塑组织开展安全研究的方式，同时也引发了对双重用途风险的担忧。 GLM-5.3 被定位为智谱在编码和长时程任务上的旗舰模型，拥有 100 万 token 的上下文窗口。该公司还在 cvd.z.ai 建立了协调漏洞披露（CVD）门户，列出其在流行开源软件中发现的 CVE，其中许多处于保密期或被评为关键/高危。

hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

**背景**: 前沿 AI 模型是最先进的通用大语言模型，构建通常耗资数亿美元。突现能力（emergent abilities）是指模型规模化后无意中出现的能力——例如 GLM-5.3 在未针对网络任务进行显式训练的情况下，表现出开展网络操作的能力。智谱 AI 是中国主要的 AI 实验室，已将 GLM 系列作为开源权重模型发布，允许社区测试和本地部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scmp.com/tech/big-tech/article/3364077/zhipu-launches-flagship-model-glm-53-china-seeks-mythos-level-edge-cyber-defence">Zhipu launches flagship model GLM-5.3 as China seeks Mythos-level edge in cyber defence | South China Morning Post</a></li>
<li><a href="https://openlm.ai/glm-5.1/">GLM-5.3 | OpenLM.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极但也保持审慎：一位用户报告称 GLM-5.3 执行了完整的红队行动，包括 WordPress 插件 0-day 和 6.8 内核漏洞利用适配，但也指出它仍然“略逊于 Sol 和 Fable”（可能指其他前沿模型）。其他用户称赞博客文风不像营销炒作，也有人质疑大规模扫描的成本效益，并将其与 Anthropic 的 Project Glasswing 进行比较。

**标签**: `#AI`, `#LLM`, `#cybersecurity`, `#coding`, `#frontier models`

---

<a id="item-9"></a>
## [别分类，去幻觉！更聪明的 LLM 标签技巧](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 8.0/10

Simon Willison 介绍了 Doug Turnbull 的一种技巧：让 LLM 为内容自由生成候选标签（即'幻觉'），然后用向量嵌入把这些想象中的标签映射到大型现有词表中距离最近的实际标签。这样就不必把 1856 个标签全部输入模型，嵌入模型负责匹配。 这是一个针对 LLM 常见限制的实用技巧：大多数预定义的标签或分类词表太大，无法放进提示的上下文窗口。它把传统上的弱点——幻觉——变成了优势，为开发人员提供了一种更便宜、更准确的大规模内容标签方法。 提示中会包含所需标签的形式或层级示例（例如'家具 / 客厅家具 / 咖啡桌与茶几 / 咖啡桌'），以引导模型进行猜测。随后，幻觉出的标签会被向量化，并与现有标签的向量进行比较，找到最接近的匹配项，而无需将完整词表暴露给 LLM。

rss · Simon Willison · 8月14日 21:54

**背景**: 向量嵌入是文本的数值表示，它能够捕捉语义信息，因此相似的概念会拥有相似的向量。LLM 有'幻觉'现象——会生成听起来合理但错误的回答，这通常是个问题，但这里被刻意用来以受控的方式生成候选标签。这种技巧结合了提示工程和语义搜索，嵌入常被用来将用户查询与文档进行匹配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/vector-embedding">What is Vector Embedding ? | IBM</a></li>
<li><a href="https://unstructured.io/insights/vector-embeddings-the-key-to-better-search-relevance">How Vector Embeddings Improve Search Relevance... | Unstructured</a></li>

</ul>
</details>

**标签**: `#LLM`, `#embeddings`, `#tagging`, `#search`, `#AI`

---

<a id="item-10"></a>
## [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小红书 dots 实验室开源了 dots3-note Preview，这是 dots3 系列首个开放权重模型。该模型总参数 280B，仅激活 16B 参数，支持 512K 上下文，并可处理文字、图片、视频和音频。 此次发布将大规模稀疏激活 MoE 模型开源，降低了开发者尝试前沿架构的门槛。同时，它引入了新的强化学习方法 TEMPO 和两个真实场景智能体基准，可能影响长程智能体 AI 的训练与评测方式。 该模型通过稀疏激活将存储的知识容量（280B）与每个 token 的计算量（16B）分离。TEMPO 利用自批判和测试时价值估计训练长程智能体，发布还包含 VibeSearchBench 和 VibeLifeBench 两个面向真实智能体场景的基准。

telegram · zaihuapd · 8月14日 08:27

**背景**: 混合专家（MoE）模型对每个 token 只激活部分参数，从而在可控的推理成本下实现很大的总参数量。dots 实验室是小红书的 AI 研究部门，类似的开源权重发布让社区可以独立微调和部署模型。VibeSearchBench 评估模型在模糊、多轮查询下的长程主动搜索能力，VibeLifeBench 则面向日常生活中的智能体任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.remio.ai/post/rednote-opens-dots3-note-preview-but-its-agent-claims-still-need-proof">RedNote Opens dots 3 note Preview, but Its Agent Claims Still Need...</a></li>
<li><a href="https://benchlm.ai/models/dots3-note-preview">dots 3 - note Preview Benchmarks & Context (August 2026) | BenchLM.ai</a></li>
<li><a href="https://vibebench.github.io/VibeSearchBench.github.io/">VibeSearchBench — Benchmarking Long-horizon Proactive Search in...</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#MoE`, `#multimodal`, `#reinforcement-learning`, `#AI`

---

<a id="item-11"></a>
## [美国法官下令谷歌简化第三方应用商店安装](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 8.0/10

美国地区法官下令谷歌移除用户在 Play Store 安装第三方安卓应用商店时遇到的多余步骤和警告弹窗。谷歌必须在一周内完成修改，这是 Epic 诉谷歌反垄断案的补救措施之一。 这项命令直接冲击谷歌对安卓应用分发的控制，可能让 Epic 游戏商店等竞争对手的应用商店更容易被安装。这也表明法院愿意在反垄断裁决后施加具体且有期限的结构补救措施。 法官认为 Play Store 安装流程中的多步操作——在出现“安装”按钮前还要额外确认——是故意设计的“反竞争摩擦”，目的是吓退普通用户。该命令是陪审团裁定谷歌非法垄断安卓应用分发后的补救阶段措施。

telegram · zaihuapd · 8月14日 09:55

**背景**: 安卓用户原本可以通过侧载方式从 Play Store 之外安装 APK 应用，但谷歌会显示“未知来源”等安全警告，这常常让普通用户望而却步。2023 年 12 月，联邦陪审团裁定谷歌的 Play Store 政策和计费做法违反反垄断法，Epic Games 胜诉。当前命令要求谷歌改变安装界面，让第三方应用商店像普通应用一样直接安装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/news/story/google-loses-epic-antitrust-case-5851940/">Google loses Epic antitrust case | LinkedIn</a></li>
<li><a href="https://topdisputes.com/disputes/epic-v-google">Epic v . Google : Structural remedy Litigation — TopDisputes</a></li>
<li><a href="https://www.xda-developers.com/how-to-sideload-install-android-app-apk/">How to sideload and install apps on Android as APKs or App Bundles</a></li>

</ul>
</details>

**标签**: `#Android`, `#Antitrust`, `#Google Play`, `#App Stores`, `#Legal`

---

<a id="item-12"></a>
## [PostgreSQL 高危 to_char 缓冲区溢出漏洞可致任意代码执行](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 披露了高危漏洞 CVE-2026-14669，这是 to_char(timestamptz) 在处理超长 POSIX 时区缩写时触发的堆缓冲区溢出。修复版本包括 18.6（供 18.x 用户）、17.11、16.15、15.19 和 14.24。 该漏洞意义重大，因为 PostgreSQL 是部署最广泛的数据库系统之一，成功利用可让经过认证的低权限数据库用户以 PostgreSQL 服务进程的操作系统权限执行任意代码。各组织应优先将受影响的集群升级到已修复的小版本。 该漏洞 CVSS 评分为 8.8，但利用需要低权限数据库账户，而非无需认证的访问，因此限制了远程暴露。受影响版本为 18.5、17.11、16.15、15.19 和 14.24 之前的版本；由于 18.5 因回归问题未正式发布，18.x 用户必须直接升级到 18.6。

telegram · zaihuapd · 8月14日 14:35

**背景**: to_char 函数用于将时间戳等值格式化为字符串，timestamptz 是 PostgreSQL 的带时区时间戳数据类型。POSIX 时区缩写（如 'EST' 或自定义字符串）可在服务器配置中指定，过长的缩写可能使堆缓冲区溢出。与主要版本升级不同，小版本更新只需替换二进制文件，不需要转储数据库或运行 pg_upgrade，因此应用修复相对简单。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.cyberdata.net/portal/en/kb/articles/010d63c0cfce3676151e1f2d5442e311">Posix Timezone Strings</a></li>
<li><a href="https://stackoverflow.com/questions/70800061/what-is-the-correct-posix-style-tz-format-04-4-vs-unk-4">timezone - What is the correct POSIX -style TZ format... - Stack Overflow</a></li>
<li><a href="https://www.postgresql.org/support/versioning/">PostgreSQL: Versioning Policy</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#CVE`, `#security`, `#buffer overflow`, `#database`

---

<a id="item-13"></a>
## [苹果联手阿里训练中国专属 AI 大模型，或成首个获批外企](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 8.0/10

据报道，苹果已在阿里巴巴支持下专门为中国市场训练了一款大语言模型，并将其生成式 AI 服务提交给中国网信办备案。若获批准，苹果将成为首个获准在华提供自有 AI 模型的外国公司。 这标志着苹果从依赖第三方 AI 模型向自研战略的转变，并可能重塑中国 AI 市场的竞争格局。同时，它也为外国企业如何进入中国严格监管的 AI 市场树立了监管先例。 该模型是中国专属版本，Apple Intelligence 预计在未来数月内随 iOS 更新在华上线。网信办已于上月对苹果的生成式 AI 服务进行备案，阿里巴巴则为该项目提供技术支持。

telegram · zaihuapd · 8月14日 14:47

**背景**: Apple Intelligence 是苹果于 2024 年 6 月发布的 AI 功能套件，结合设备端与服务器端处理，最初集成于 iOS 18、iPadOS 18 和 macOS Sequoia。中国根据 2023 年实施的《生成式人工智能服务管理暂行办法》，要求生成式 AI 服务通过严格的安全评估并完成备案。苹果此前在其 AI 功能中依赖 OpenAI 的 ChatGPT 等第三方模型，因此此次自研中国专属模型的报道是显著的战略转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://merics.org/en/comment/chinas-censors-back-down-generative-ai">China ’s censors back down on generative AI | Merics</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#Regulation`

---

<a id="item-14"></a>
## [RustDesk 在 Wayland 上实现真正的无人值守远程访问](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 7.0/10

RustDesk 宣布支持 Wayland 上真正的无人值守远程访问。这消除了依赖 Wayland 会话的 Linux 用户面临的一个重大限制。 Wayland 的安全模型历来使远程桌面访问变得困难，因此此更新使 RustDesk 在現代 Linux 系统上成为 TeamViewer 和 AnyDesk 等专有工具的更具可行性的开源替代方案。 RustDesk 是一个跨平台、开源的远程桌面解决方案，支持自托管服务器。该 Wayland 支持似乎解决了一个先前已知的限制，但公告中未提供具体版本或发布日期。

hackernews · rustdesk · 8月14日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=49300759)

**背景**: RustDesk 是一款开源远程桌面应用程序，作为 TeamViewer 和 AnyDesk 的安全替代品，提供自托管服务器选项，并跨平台支持 Windows、macOS 和 Linux。Wayland 是一种显示协议，旨在取代老旧的 X11/Xorg 系统，提供更好的安全性和更简洁的架构，但其更严格的安全策略使远程访问所需的屏幕捕获和输入注入变得复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustdesk.com/">RustDesk : Open-Source Remote Desktop with Self-Hosted Server...</a></li>
<li><a href="https://www.howtogeek.com/900698/what-is-wayland-on-linux-and-how-is-it-different-from-x/">What Is Wayland on Linux, and How Is It Different From X?</a></li>
<li><a href="https://medium.com/@anuj85500/rustdesk-the-open-source-remote-desktop-champion-you-didnt-know-you-needed-68433ac149a9">RustDesk : The Open-Source Remote Desktop Champion... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，一位用户表示两天前刚遇到 Wayland 限制，很高兴看到问题得到解决。一些评论提出了对缺失功能的担忧：自托管加密连接仍不受支持（引用了 GitHub issue #3714），与专有解决方案相比，客户端到主机的麦克风输入透传仍然缺失。另一位用户询问 RustDesk 与 VNC 有何不同。

**标签**: `#RustDesk`, `#Wayland`, `#remote-desktop`, `#Linux`, `#open-source`

---

<a id="item-15"></a>
## [AI by Hand：以动手方式理解大语言模型的研究资料库](https://www.byhand.ai/) ⭐️ 7.0/10

AI by Hand 是由 Tom Yeh 教授创立的研究刊物与资料库，专注于以动手操作和数学层面来理解 AI 与大语言模型。订阅者可免费获取新文章并参加直播研讨会，会员则可访问完整的研究资料库。 该资源满足了人们对 AI 可解释性日益增长的需求，让学习者和从业者能够理解复杂的模型内部机制。它也有助于推动机械可解释性（mechanistic interpretability）和透明 AI 的潮流。 研究资料库位于 byhand.ai/p/library，内容基于 Tom Yeh 教授的材料，包括“AI by Hand with Anna”系列等讲解视频。社区还有类似项目，如 ml-by-hand 和 llm-from-scratch，同样探索动手学习 AI 的方法。

hackernews · sans_souse · 8月14日 15:58 · [社区讨论](https://news.ycombinator.com/item?id=49300568)

**背景**: 机械可解释性是可解释 AI（explainable AI）的一个子领域，旨在通过分析神经网络的结构和算法来对其进行逆向工程。理解 Transformer 等模型背后的数学是这种方法的核心。费曼（Feynman）的名言“我不能创造的东西，我就不理解”正是 AI by Hand 这类动手学习资源的思想基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://www.youtube.com/watch?v=hyGJM-wsuuk">4. Three Inputs - AI by Hand with Anna - YouTube</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体对该资源表示赞赏，有用户推荐了 llm-from-scratch、ml-by-hand 等类似项目以及一本深度学习书籍。不过，也有用户对网站结构以及未订阅时可访问的内容表示困惑。

**标签**: `#AI education`, `#LLMs`, `#interpretability`, `#machine learning`, `#research`

---

<a id="item-16"></a>
## [Mixedbread 发布 Toast 1，一款专用于搜索的 LLM](https://www.mixedbread.com/blog/toast-1) ⭐️ 7.0/10

Mixedbread AI 发布了 Toast 1，一款专用于搜索和检索任务的专有大型语言模型。该模型可以独立运行，作为检索代理使用，也可以作为更大 AI 系统中的子代理使用。 此次发布凸显了从通用模型向专用于特定任务的 LLM 发展的趋势，有望提升搜索的准确性和效率。同时，它也引发了社区关于该模型与 Perplexity、带搜索的 Gemini 以及 RAG 流水线等现有搜索工具相比表现如何的讨论。 Toast 1 是专有模型，上下文窗口为 131K。它既可以作为独立的检索代理使用，也可以作为由前沿模型协调的子代理使用。

hackernews · mplappert · 8月14日 15:07 · [社区讨论](https://news.ycombinator.com/item?id=49299746)

**背景**: Mixedbread AI 是 2023 年成立于柏林的人工智能初创公司，以开发用于信息检索和语义搜索的开源嵌入和重排序模型而闻名。Toast 1 标志着其进军专用于搜索的 LLM 领域。专用搜索模型旨在比通用聊天模型更有效地处理多步检索和综合，满足超越简单关键词查找的复杂问答需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://benchlm.ai/models/toast-1">Toast 1 Pricing, Specs & Sources (August 2026) | BenchLM.ai</a></li>
<li><a href="https://www.mixedbread.com/blog/toast-1">Introducing Toast 1</a></li>
<li><a href="https://grokipedia.com/page/Mixedbread_AI">Mixedbread AI</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极但保持谨慎。有人赞赏这种专门化，也有人指出其不是开放权重模型，并将其与 Voyage AI、SearXNG MCP、Perplexity 和带搜索的 Gemini 等现有工具进行比较。还有一些关于名称“Toast”的幽默评论，以及关于它相对专用 RAG 流水线有何实际优势的疑问。

**标签**: `#LLM`, `#search`, `#AI`, `#model-release`, `#NLP`

---

<a id="item-17"></a>
## [评估肿瘤 AI 模型的开源 Python 库与无代码仪表盘](https://www.reddit.com/r/MachineLearning/comments/1vod2c8/opensource_python_library_nocode_web_dashboard/) ⭐️ 7.0/10

oncothresh 是一个新的开源 Python 库，专注于在特定临床决策阈值下评估肿瘤 AI 模型，而非只看全局平均指标。它提供了自助法置信区间、阈值敏感度曲线、边界加权校准、决策曲线净收益和需检验数等分析，并配套一个无代码网页仪表盘。 大多数肿瘤 AI 基准（如 AUC、ICC、MAE）只衡量全局一致性，忽视真正决定患者诊疗的截断值。oncothresh 填补了这一空白，为临床医生和研究人员提供了一个实用工具，用于在决定患者是否被标记、活检或治疗的精确阈值上评估模型。 该库依赖很少（numpy、scipy、scikit-learn、pydantic），专为肿瘤细胞度、Ki-67、TMB 和 PD-L1 评分等任务设计。配套仪表盘 oncothresh-web 可通过 docker compose 在本地运行，用户上传包含预测和标签的 CSV 文件，即可生成图表和可下载的 PDF 报告。

reddit · r/MachineLearning · /u/adom2989 · 8月14日 17:06

**背景**: 在医学 AI 评估中，决策曲线分析（DCA）通过权衡治疗真阳性的收益和治疗假阳性的风险，直接量化风险预测算法的临床效用。边界加权校准关注决策边界附近的校准误差，这在医学图像分割等标注模糊常见任务中尤为重要。PathBench 和 PathBench-MIL 等基准对病理基础模型进行全局评估，但并未在预定义临床阈值下结合不确定性量化进行性能评估，这正是 oncothresh 所填补的空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/oncothresh/">Clinical threshold evaluation for oncology AI models</a></li>
<li><a href="https://arxiv.org/pdf/2512.17517">PathBench - MIL : A Comprehensive AutoML and Benchmarking ...</a></li>
<li><a href="https://publications.ersnet.org/highwire_display/entity_view/node/582570/full">Moving beyond AUC: decision curve analysis for quantifying net...</a></li>

</ul>
</details>

**标签**: `#oncology AI`, `#model evaluation`, `#clinical decision thresholds`, `#open-source`, `#medical machine learning`

---

<a id="item-18"></a>
## [Hermes Agent 推出 Bot Mode，支持机器人分工与互聊](https://x.com/Teknium/status/2088003994904113614) ⭐️ 7.0/10

Hermes Agent 推出了 Bot Mode 新功能，用一组具名机器人取代单一会话，每个机器人都有自己的聊天、头像、个性和日程安排。机器人之间可以互相通信和协作。Teknium 宣布通过 GitHub 插件在 Hermes Desktop 上开展为期一天的公开测试。 这使 Hermes Agent 迈向真正的多智能体协作，让用户可以组建由专业机器人组成的团队来协调完成工作。这也反映出行业趋势：AI 智能体正变得更具社交性和互操作性，而不再只是单线程的助手。 Bot Mode 是作为 GitHub 仓库 NousResearch/Hermes-Bot-Mode 中的桌面插件实现的。Teknium 表示公开测试将持续一天，在功能并入正式版 Hermes Desktop 应用前，会先收集并整合反馈。

telegram · zaihuapd · 8月14日 04:13

**背景**: Hermes Agent 是 Nous Research 开发的开源 AI 智能体，旨在利用大型语言模型自主执行多步骤任务。它具有持久记忆和自适应学习能力，并可配置使用本地或远程 LLM。Bot Mode 扩展了这一架构，支持多个智能体档案作为独立机器人运行，拥有不同角色并可以互相发送消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NousResearch/Hermes-Bot-Mode">GitHub - NousResearch/ Hermes - Bot - Mode : Bot Mode for the Hermes ...</a></li>
<li><a href="https://digg.com/tech/jxesssj4">Nous Research Tests Bot Mode for Hermes Agent · Digg</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hermes_Agent">Hermes Agent</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#multi-agent systems`, `#Hermes Agent`, `#LLM tools`

---

<a id="item-19"></a>
## [苹果提议美国 App Store 外部购买抽成最高 15%](https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/) ⭐️ 6.0/10

苹果已向法院提交美国 App Store 外部购买抽成方案，费率最高 15%。具体而言，标准应用抽成 15%，视频、新闻等合作项目及订阅续费抽成 10%，小型企业计划应用抽成 5%。 该方案是苹果与 Epic Games 正在进行的反垄断诉讼中的关键进展，可能重塑开发者处理 App Store 内购以外支付的方式。其结果将影响应用开发者的收入，并可能为全球 App Store 政策树立先例。 美国最高法院此前驳回了苹果暂停下级法院审理费率问题的请求，诉讼得以继续推进。Epic 将有机会作出回应，苹果预计于 9 月 14 日前向最高法院提交书面意见。

telegram · zaihuapd · 8月14日 02:33

**背景**: 苹果 App Store 历来要求开发者使用其内购系统并支付最高 30%的抽成。2020 年推出的 App Store 小型企业计划，对年收入低于 100 万美元的开发者将抽成降至 15%。此次争议源于 Epic Games 对苹果 App Store 规则的挑战，法院裁决要求苹果允许外部支付链接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://applemagazine.com/apple-app-store-fees-external-purchases/">Apple Proposes 15% App Store Fees for External Purchases</a></li>
<li><a href="https://developer.apple.com/app-store/">App Store - Apple Developer</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Store`, `#Epic Games`, `#antitrust`, `#commission`

---

<a id="item-20"></a>
## [中信旗下信宸资本接近以超 15 亿美元收购阿里游戏灵犀](https://www.bloomberg.com/news/articles/2026-08-14/trustar-is-said-to-near-1-5-billion-deal-for-alibaba-gaming-arm) ⭐️ 6.0/10

中信集团旗下私募机构信宸资本（Trustar Capital）正接近达成交易，以超过 15 亿美元的估值收购阿里巴巴的游戏业务灵犀互娱。磋商仍在进行中，但信宸资本已在多家游戏公司的竞购中领先。 这笔交易标志着阿里巴巴在 CEO 吴泳铭的推动下继续剥离非核心资产，以聚焦人工智能和云计算。同时也凸显出私募股权基金对中国规模化游戏业务的兴趣，尽管行业仍在持续变化。 灵犀的旗舰产品《三国志·战略版》是与日本光荣特库摩合作开发的大型多人在线策略游戏。据知情人士透露，磋商仍在进行中，尚未做出最终决定。

telegram · zaihuapd · 8月14日 10:24

**背景**: 阿里巴巴是中国科技巨头，正通过剥离或分拆非核心业务，聚焦人工智能与云计算服务。灵犀互娱是阿里巴巴旗下的游戏部门，信宸资本则是中信集团旗下聚焦亚洲市场的私募股权投资机构。随着企业重新围绕核心优势布局，中国游戏行业的并购活动持续受到关注。

**标签**: `#M&A`, `#gaming`, `#Alibaba`, `#private equity`, `#Chinese tech`

---
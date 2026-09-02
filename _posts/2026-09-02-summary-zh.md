---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> 从 45 条内容中筛选出 20 条重要资讯。

---

1. [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1](#item-1) ⭐️ 9.0/10
2. [World Labs 发布 Atlas：面向空间智能的世界模型](#item-2) ⭐️ 9.0/10
3. [丹·陆评估艾德·齐特龙的 AI 预测，发现许多不准](#item-3) ⭐️ 8.0/10
4. [OpenAI Codex 桌面应用捆绑 LibreOffice 及完整运行时](#item-4) ⭐️ 8.0/10
5. [SlotStream 通过 SSD 专家卸载在 Mac 上运行 125B 参数 MoE 模型](#item-5) ⭐️ 8.0/10
6. [韩国万亿主权 AI：英伟达受益，海力士受损](#item-6) ⭐️ 8.0/10
7. [TontaubeV1：采用字符级分词的开源 2.9B 参数语音合成模型](#item-7) ⭐️ 8.0/10
8. [Virtualizor 更新设施遭 BGP 劫持，恶意更新植入 root 后门](#item-8) ⭐️ 8.0/10
9. [谷歌将发布 Gemini 3.8 Flash，编码能力据称缩小与竞品差距](#item-9) ⭐️ 8.0/10
10. [Anthropic 收紧 Claude API 思考块机制以防模型蒸馏](#item-10) ⭐️ 8.0/10
11. [英伟达发布 DLSS 5，引入 3D 引导神经渲染，随《NBA 2K27》上线](#item-11) ⭐️ 8.0/10
12. [EvoUndo：验证并修复 LLM 智能体自我修改可恢复性的框架](#item-12) ⭐️ 7.5/10
13. [Jujutsu 作者马丁加入 ERSC，引发版本控制工具讨论](#item-13) ⭐️ 7.0/10
14. [交互式地图收录 13,312 部影视与游戏拍摄场景](#item-14) ⭐️ 7.0/10
15. [Play Store 被曝屏蔽 AuroraStore，影响 GrapheneOS 用户](#item-15) ⭐️ 7.0/10
16. [Python 3.15.0 候选版 2 发布，维护者需提前准备](#item-16) ⭐️ 7.0/10
17. [YOLO26-RGB：复用 YOLO26 深度训练骨干网络进行图像去雨](#item-17) ⭐️ 7.0/10
18. [2026 潜在推理格局：从 Coconut 到 BDH-CQ](#item-18) ⭐️ 7.0/10
19. [瑞银：中国十年内难追平 ASML EUV，DUV 或 2 至 5 年量产](#item-19) ⭐️ 7.0/10
20. [Mozilla 为 iOS 版 Firefox 增加内置广告拦截功能](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1。两者是同一模型但安全防护级别不同，改进了写作风格，将缓存读取价格降至每百万 token 0.25 美元，并发布了全面的系统卡。 此次发布为开发者提供了一个更强大的编程和知识工作模型，同时降低了实际使用成本，可能重新定义高端大语言模型的定价预期。它还标志着 Anthropic 的策略性分割：广泛可用的模型（Fable）与仅限邀请的受限变体（Mythos）并存，反映出对前沿 AI 能力日益增长的安全警惕。 Claude Fable 5.1 支持 100 万 token 的上下文窗口和多模态输入，定价为每百万输入 token 10 美元、每百万输出 token 50 美元、每百万缓存输入 token 0.25 美元。Claude Mythos 5.1 仅通过 Project Glasswing 邀请提供，规格和定价与 Fable 5.1 相同。

hackernews · denysvitali · 9月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**背景**: Claude 是 Anthropic 的大语言模型系列；Fable 是面向推理和智能体任务的通用主力模型，而 Mythos 是最强大的系列，最初因担心其发现软件漏洞的能力而未向公众发布。系统卡是描述 AI 系统构建方式的文档，涵盖其架构、训练数据和预期局限，越来越多地被用于支持透明度和治理。缓存读取价格下调意义重大，因为它降低了重复上下文工作负载的成本，这类负载在智能体任务和长时程编程任务中很常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5.1 and Claude Mythos 5.1 \\ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://platform.claude.com/docs/en/models/mythos-5-1/overview">Claude Mythos 5.1 - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 社区评论观点不一：Anthropic 员工称赞 Fable 5.1 的写作风格更自然，Simon Willison 分享了不同思考强度下令人印象深刻的“鹈鹕”输出，其中改进后的最高强度推理耗时 14 分钟。然而，一些用户认为该模型是被削弱的 Fable，指出去掉科学基准结果后几乎没有改进，并批评移除思维痕迹以及将 Mythos 作为营销策略的做法。

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#model release`

---

<a id="item-2"></a>
## [World Labs 发布 Atlas：面向空间智能的世界模型](https://www.worldlabs.ai/blog/atlas) ⭐️ 9.0/10

World Labs 发布了 Atlas，这是一个多模态世界模型，可以从稀疏图像重建逼真的 3D 环境、生成图像和视频帧，并支持像素级相机控制。该公司将其定位为首个面向空间智能的多模态世界模型。 Atlas 之所以重要，是因为空间智能——AI 理解和推理三维物理空间的能力——是机器人、自动驾驶和虚拟模拟的基础。从少量图像生成逼真的 3D 环境，可以加速游戏原型制作、机器人训练和沉浸式内容创作，而无需昂贵的数据采集。 根据社区分析，Atlas 似乎可以从大约十几张智能手机图像重建完整环境，并支持像素级相机控制，但相机移动时时间动态似乎会冻结。官方博客文章未提及从模型潜在空间中提取语义信息，而一些评论者认为这对已部署机器人是最有吸引力的应用。

hackernews · johnsutor · 9月1日 17:36 · [社区讨论](https://news.ycombinator.com/item?id=49525160)

**背景**: 世界模型是一种机器学习系统，它构建环境的内在表征，并模拟环境如何随行动随时间变化，帮助智能体无需反复试错即可进行规划和推理。空间智能是指感知、解释和导航三维物理空间的能力，包括物体之间的关联、运动和交互方式。Atlas 建立在最近从稀疏图像进行 3D 重建的进展之上，例如 COLMAP 等多视图立体技术，利用已知相机位置计算深度信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-spatial-intelligence">What is Spatial Intelligence? | Stanford HAI</a></li>
<li><a href="https://www.lizardtech.com/post/colmap-explained-building-3d-models-from-images">COLMAP Explained: Building 3 D Models from Images</a></li>

</ul>
</details>

**社区讨论**: 社区对 Atlas 的反应总体正面，有评论者称它是目前从稀疏图像重建 3D 空间的最佳模型，还有人提出快速迭代游戏地图遮挡是其关键用例。一些评论者质疑“世界模型”一词被过度使用，并指出可能存在时间一致性问题，而 World Labs 的一位联合创始人表示愿意回答问题。

**标签**: `#world models`, `#spatial intelligence`, `#3D reconstruction`, `#AI`, `#robotics`

---

<a id="item-3"></a>
## [丹·陆评估艾德·齐特龙的 AI 预测，发现许多不准](https://danluu.com/zitron/) ⭐️ 8.0/10

丹·陆在 danluu.com 上发表了一篇详细分析，将艾德·齐特龙对 AI 的怀疑论预测与实际事件进行对照，得出的结论是许多预测并不准确，但在技术批评领域仍具影响力。 这一评估之所以重要，是因为艾德·齐特龙作为知名 AI 怀疑论者，其预测影响着公众对科技行业的讨论；要求评论员对其预测的准确性负责，对于技术批评的可信度至关重要。 该分析指出，齐特龙的文章中常出现无法构成连贯论证的数据，例如将 Facebook 月活跃用户下降与 Meta 的财务问题及强行整合 AI 联系起来。评论者也提到齐特龙预测中“死亡”一词的模糊性。

hackernews · jatins · 9月1日 18:35 · [社区讨论](https://news.ycombinator.com/item?id=49526069)

**背景**: 艾德·齐特龙是一位科技评论员，以“腐烂经济”概念闻名，该概念描述大型科技公司的产品即使财务上仍然成功，却在日益恶化。丹·陆是一位软件工程师和作家，以数据驱动的文章著称。这篇文章是围绕科技预测可靠性和媒体评论员激励机制这一更广泛讨论的一部分。

**社区讨论**: 评论者就“死亡”一词应理解为字面意义还是产品质量下降展开争论，有人指责他人将自己的预测投射到齐特龙的言论上。另一些人则讨论追求准确性与维持媒体曝光之间的矛盾，这与文章对评论员文化的批评相呼应。

**标签**: `#AI`, `#predictions`, `#analysis`, `#skepticism`, `#tech-criticism`

---

<a id="item-4"></a>
## [OpenAI Codex 桌面应用捆绑 LibreOffice 及完整运行时](https://simonwillison.net/2026/Sep/1/codex-libreoffice/) ⭐️ 8.0/10

西蒙·威利森发现，OpenAI 的 Codex 桌面应用（现已更名为 ChatGPT）在 ~/.cache 中包含一个约 1.7GB 的 codex-primary-runtime 运行时目录，里面有完整的 Python 和 Node.js 安装，以及 Poppler、git 和 LibreOffice headless 的原生二进制文件。该捆绑包还带有技能，告诉 Codex 如何使用这些工具处理文档。 这一发现揭示了 OpenAI 如何借助成熟的开源工具而非从零构建专有解析器，来为其编程智能体提供强大的本地文档处理能力。同时，它也反映出 AI 桌面应用越来越多地打包庞大依赖栈的趋势，由此带来关于磁盘占用、应用体积以及企业是否应回馈 LibreOffice 等开源项目的问题。 该运行时位于 ~/.cache/codex-runtimes/codex-primary-runtime，其中 native 子目录约 771MB，包含 libreoffice-headless（约 429.7MB）、poppler、git、libheif 和 jxrlib 等组件。plugins/openai-primary-runtime/plugins/documents 目录中的技能会指导 Codex 如何查找并调用这些二进制文件。

rss · Simon Willison · 9月1日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49527396)

**背景**: LibreOffice 是一个免费的开源办公套件，2010 年从 OpenOffice.org 分支而来，能够读写许多旧式及专有文档格式，包括老旧的 .xls 电子表格。Poppler 是一个开源的 PDF 渲染库。捆绑这些工具可以让基于大语言模型的智能体在本地检查、转换和操作文档；其他需要可靠文件格式兼容性的应用也常采用类似的捆绑方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://poppler.freedesktop.org/">Poppler</a></li>
<li><a href="https://grokipedia.com/page/Poppler_(software)">Poppler (software)</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了这些二进制文件究竟是预先捆绑还是按需下载，因为体积相当大。有人称赞 LibreOffice 能可靠读取旧版文件格式，也有人认为 OpenAI 应该向该项目捐款；还有评论指出，捆绑 LibreOffice 或许能解释为何某些 Office 文件渲染效果不佳。

**标签**: `#OpenAI`, `#Codex`, `#LibreOffice`, `#Software Engineering`, `#Desktop Apps`

---

<a id="item-5"></a>
## [SlotStream 通过 SSD 专家卸载在 Mac 上运行 125B 参数 MoE 模型](https://github.com/carloslfu/slotstream) ⭐️ 8.0/10

开发者 carloslfu 发布了 SlotStream，这是一款基于 Swift/MLX 的工具，通过将专家权重卸载到 SSD，可在最低 16GB 统一内存的 Mac 上运行 125B 参数的 Qwen3.8-Flash-Next 4-bit MoE 模型。在 48GB 内存的 Mac 上，它据说能达到约每秒 12 个 token 的生成速度。 这大幅降低了在本地运行超大型 MoE 模型的硬件门槛，让只有 16GB、32GB 内存的 Mac 用户也能跑通常需要 100GB 以上内存的模型。它验证了 SSD 卸载在消费级硬件上的实用性，并可能推动 MLX 等工具朝这一方向发展。 SlotStream 提供自动模式（auto-mode），在内存占用与速度之间做权衡，作者计划加入用于投机解码的 MTP 模块。实际性能在很大程度上取决于 SSD 读取速度，且 125B 这一参数规模指的是模型 4-bit 量化后的形态。

hackernews · carloslfu · 9月1日 16:42 · [社区讨论](https://news.ycombinator.com/item?id=49524447)

**背景**: 混合专家（MoE）模型每个 token 只激活一部分参数，因此可以将不用的专家整体存放在较慢的存储中，只在需要时载入内存。专家卸载技术会把大部分专家权重放在 CPU 内存或 SSD 上，并动态地将活跃专家流入显存，从而降低显存需求。投机解码（例如多 token 预测 MTP）则用轻量级头先草拟多个 token，再由主模型并行验证，从而提高吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apxml.com/courses/mixture-of-experts-advanced-implementation/chapter-4-efficient-moe-inference/expert-offloading">MoE Expert Offloading to CPU/NVMe</a></li>
<li><a href="https://www.emergentmind.com/topics/expert-offloading">Expert Offloading for Scalable AI</a></li>
<li><a href="https://deepwiki.com/XiaomiMiMo/MiMo-V2-Flash/2.3-multi-token-prediction-module">Multi-Token Prediction Module | XiaomiMiMo/MiMo-V2-Flash | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: 评论者既感兴趣也很谨慎：有人质疑 16GB 内存是否真能在不触发温度警告的情况下维持每秒 5 个 token，也有 48GB Mac 用户表示更想要更长的上下文窗口而非更大的模型。还有人称赞这一方向，希望这能让 32GB 设备真正有用；一位关注硬件的用户建议给 GPU 增加可安装的 DDR5，以进一步推进 MoE 权重卸载。此外也有反馈称 README 需要整理，以更好地引导新用户。

**标签**: `#llm`, `#mac`, `#mlx`, `#moe`, `#ssd-offloading`

---

<a id="item-6"></a>
## [韩国万亿主权 AI：英伟达受益，海力士受损](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 8.0/10

SemiAnalysis 的一篇分析审视了韩国耗资万亿美元的主权 AI 计划，其中包含一场全国性 AI 竞赛，最佳非中国开源模型被淘汰。该报告认为，英伟达在战略上受益，而 SK 海力士则面临竞争损失。 此事意义重大，因为主权 AI 投资正在重塑全球半导体供应链和 AI 模型开发格局。其结果可能巩固英伟达在 AI 硬件领域的主导地位，同时改变海力士和三星等内存制造商的竞争态势。 该分析重点提及韩国‘鱿鱼游戏’式的全国 AI 竞赛，以及最佳非中国开源模型被淘汰的情况。文章还讨论了英伟达为何需要开源模型来维持其 GPU 需求，并指出影响海力士和三星的 HBM（高带宽内存）供应动态。

rss · Semianalysis · 9月1日 20:14

**背景**: 主权 AI（Sovereign AI）是指一个国家利用自己的基础设施、数据和模型来构建、运行和管理 AI 的能力，从而减少对外部提供商的依赖。高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，对于英伟达 GPU 等 AI 加速器至关重要。韩国投入万亿美元发展主权 AI，旨在确保国家 AI 能力和半导体领导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.redhat.com/en/topics/ai/sovereign-ai">What is sovereign AI?</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Semiconductors`, `#Nvidia`, `#Hynix`, `#Sovereign AI`

---

<a id="item-7"></a>
## [TontaubeV1：采用字符级分词的开源 2.9B 参数语音合成模型](https://www.reddit.com/r/MachineLearning/comments/1w4afjn/we_released_tontaubev1_a_characterlevel_tts_model/) ⭐️ 8.0/10

作者发布了 TontaubeV1，这是一个 2.9B 参数的开源权重文本转语音模型，支持英语和德语，并可从最多一分钟的参考音频进行零样本声音克隆。该模型在 Qwen3-1.7B 基座模型上采用字符级分词，并使用 DualCodec 音频编解码器，专注于富有表现力的长语音生成和低延迟本地推理。 这一发布具有重要意义，因为它为富有表现力的长文本语音合成提供了一种实用的开源权重替代方案，通过字符级分词解决了上下文长度和令牌分布外的问题。这可能有利于从事旁白、有声书和本地声音克隆的开发者和研究者，且无需大型基础设施。 该模型在 7 种语言和约 20 万小时音频上训练，采用分块和逻辑位置方案，使长文本的上下文保持有界。模型强制 Qwen 分词器进行字符级分词，在保留语言理解能力的同时简化了字符到声音的映射。

reddit · r/MachineLearning · /u/EAVDR · 9月1日 12:23

**背景**: TontaubeV1 基于 DualCodec，这是一种低帧率、多码本的离散音频编解码器，能在低比特率下实现高质量音频重建。许多基于 LLM 的现代 TTTS 模型使用骨干分词器并添加音频令牌，但作者发现字符级分词对 TTS 效果更好，因为它减少了稀有令牌序列并简化了对齐。该模型在扁平序列中训练语义和声学码本模型，并使用独立的逻辑位置 ID 以保持跨块文本和音频的对齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dualcodec.github.io/">DualCodec Demo Page</a></li>
<li><a href="https://arxiv.org/abs/2505.13000">[2505.13000] DualCodec: A Low-Frame-Rate, Semantically-Enhanced Neural Audio Codec for Speech Generation</a></li>
<li><a href="https://www.shadecoder.com/topics/character-level-tokenization-a-comprehensive-guide-for-2025">Character-level Tokenization: A Comprehensive Guide for 2025 - Shadecoder - 100% Invisibile AI Coding Interview Copilot</a></li>

</ul>
</details>

**标签**: `#TTS`, `#text-to-speech`, `#open-source`, `#machine learning`, `#audio generation`

---

<a id="item-8"></a>
## [Virtualizor 更新设施遭 BGP 劫持，恶意更新植入 root 后门](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

在 2026 年 8 月 28 日至 30 日期间，攻击者通过 BGP 路由劫持接管了 Virtualizor 的更新基础设施，并利用有效的 TLS 证书推送恶意更新包，从而植入 root 后门。官方表示仅窗口期内更新的安装受影响，并强调这并非软件代码漏洞。 这一事件凸显了严重的供应链风险：攻击者无需攻破软件本身，而是劫持更新渠道，再配合有效 TLS 证书让恶意更新难以察觉。使用 Virtualizor 的主机服务商需要排查其 hypervisor，并考虑加强路由过滤和更新完整性校验。 独立取证显示，恶意包会写入 root SSH 密钥、安装 Java 载荷并建立持久化服务。AlbaHost 在 34 台 hypervisor 中发现 5 台存在被入侵指标；Softaculous 表示目前无证据表明其他产品受影响。

telegram · zaihuapd · 9月1日 06:05

**背景**: BGP 是互联网上在不同自治系统之间传递流量的路由协议；BGP 劫持是指攻击者虚假宣告自己并不拥有的 IP 前缀，把流量重定向到攻击者控制的目的地。Virtualizor 是 Softaculous 开发的基于 Web 的 VPS 控制面板，主机服务商常用它来管理虚拟机和 hypervisor。由于更新下载经由互联网传输，BGP 劫持可以拦截并替换合法更新包为恶意版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BGP_hijacking">BGP hijacking - Wikipedia</a></li>
<li><a href="https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/">What Is BGP Hijacking?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Virtualization">Virtualization</a></li>

</ul>
</details>

**标签**: `#security`, `#BGP hijacking`, `#supply chain`, `#backdoor`, `#virtualization`

---

<a id="item-9"></a>
## [谷歌将发布 Gemini 3.8 Flash，编码能力据称缩小与竞品差距](https://www.wsj.com/tech/ai/new-google-ai-model-said-to-narrow-gap-on-coding-ability-264c6052) ⭐️ 8.0/10

据《华尔街日报》报道，谷歌 DeepMind 计划最早于本周三发布 Gemini 3.8 Flash（内部代号 "Skimaki"）。据报道，新模型编码能力大幅升级，在内部 Jetski 工具的对比测试中，谷歌工程师更偏好它而非 Anthropic 的 Opus 模型。 此次发布可能帮助谷歌缩小与 OpenAI 和 Anthropic 在 AI 辅助编码这一最具商业价值的 AI 应用领域上的差距。这也表明前沿 AI 实验室在编码专用模型性能上的竞争正日趋激烈。 该报道基于匿名消息源，尚未得到谷歌官方证实。据称该模型在 8 月份于谷歌 Jetski 编码平台上测试后已完成生产部署；而 Gemini 3.7 Flash 于 2026 年 8 月 13 日发布，可见迭代节奏非常快。

telegram · zaihuapd · 9月2日 00:35

**背景**: Jetski 是谷歌内部编码工具，由 Antigravity 团队构建，支持 monorepo、文档搜索等谷歌特有功能，是谷歌 Antigravity 产品的内部版本。Gemini Flash 系列是谷歌主打快速、低成本的模型层级，面向高吞吐量的智能体与编码工作负载——Gemini 3.7 Flash 的定位是比 3.6 Flash 便宜 35%，同时提升智能体性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/google-gemini-3-8-flash-wednesday/">Google to unveil Gemini 3.8 Flash on Wednesday</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 .7 Flash — Google DeepMind</a></li>
<li><a href="https://x.com/GergelyOrosz/status/1991512105313525784">Gergely Orosz on X: "Devs at Google can use Jetski (an internal vesion of Anrigravity, supports eg monorepo, docs search etc. Built by the Antigravity team) and Cider (lots of agentic features) They are disallowed to use Antigravity for work Again not surprising given their infra" / X</a></li>

</ul>
</details>

**社区讨论**: 新闻条目本身未附带评论。不过，X 平台上的开发者讨论指出，谷歌工程师被要求内部使用 Jetski，并被禁止在工作中使用 Antigravity，原因是与谷歌的 monorepo 及自定义工具链存在兼容性问题。

**标签**: `#AI`, `#Google`, `#Gemini`, `#coding`, `#model release`

---

<a id="item-10"></a>
## [Anthropic 收紧 Claude API 思考块机制以防模型蒸馏](https://support.claude.com/zh-CN/articles/16761192-%E4%BF%9D%E7%95%99%E6%80%9D%E8%80%83-%E6%94%B9%E5%8F%98messages-api%E5%A4%84%E7%90%86%E6%80%9D%E8%80%83%E5%9D%97%E7%9A%84%E6%96%B9%E5%BC%8F%E4%BB%A5%E9%98%B2%E6%AD%A2%E8%92%B8%E9%A6%8F) ⭐️ 8.0/10

Anthropic 调整了 Claude 的 Messages API：对于受影响账户，多轮对话中返回此前的思考块时，必须保持生成该思考块时的系统提示、工具和消息不变，否则 API 会报错。开发者也可启用“非严格”模式，由系统删除不匹配的思考块后继续请求。 该变动堵住了一个安全漏洞：修改早期上下文可诱导 Claude 泄露内部推理，而这种手法常被用于工业规模的模型蒸馏。它会影响那些基于 Claude 构建多轮应用的开发者，也表明 API 提供商正加强对模型能力未经授权复制的防护。 新机制目前仅适用于 2026 年 8 月 31 日及以后创建的新 API 账户，未来模型版本将扩展到所有账户。Anthropic 表示，修改早期上下文可被用于诱导模型解密并输出推理，是工业规模非法蒸馏的一种手段。

telegram · zaihuapd · 9月2日 01:09

**背景**: Claude 的“思考模式”会生成结构化的多步推理内容，也就是思考块，帮助模型拆解复杂问题。模型蒸馏（或知识蒸馏）是一种把大型模型的知识迁移到小型模型的技术，通常用大型模型的输出来训练小型模型。如果竞争对手能通过大量查询迫使 Claude 暴露内部推理链，就能更容易地在蒸馏模型中复现其能力。该改动将思考块与其生成时的确切上下文绑定，从而加大了这一提取手法的难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amazonaws.cn/knowledge/what-is-model-distillation/">what-is-model-distillation | Amazon Web Services, Inc.</a></li>
<li><a href="https://docs-model.skyengine.com.cn/api-reference/examples/thinking/claude-thinking">Claude 思 考 模式示例 - ModelHub文档</a></li>

</ul>
</details>

**标签**: `#Claude`, `#API`, `#Security`, `#AI Distillation`, `#Anthropic`

---

<a id="item-11"></a>
## [英伟达发布 DLSS 5，引入 3D 引导神经渲染，随《NBA 2K27》上线](https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/) ⭐️ 8.0/10

英伟达正式发布 DLSS 5，引入 3D 引导神经渲染，可实时生成更真实的光影与材质。该技术于 9 月 3 日随《NBA 2K27》上线，适用于 GeForce RTX 50 系列 PC、笔记本及 GeForce NOW Ultimate 会员。 这标志着 AI 驱动的实时图形技术迈出重要一步，可能为游戏渲染画质与性能树立新标杆。它将影响玩家、游戏开发者以及整个 GPU 生态，使神经渲染成为主流功能。 启用 DLSS 5 后，RTX 5090 在 4K 超高画质加光线追踪下帧率最高可达 370 FPS，1440p 下可达 590 FPS。同日将发布新版 GeForce Game Ready 驱动，玩家需下载安装后才能使用该功能。

telegram · zaihuapd · 9月2日 03:00

**背景**: 神经渲染是一种利用人工智能生成或增强视觉内容的计算技术，通过学习光、几何与材质之间的相互作用来实现。DLSS 5 以游戏每帧的颜色输出和运动向量为输入，再通过 AI 模型增强场景的光照和材质，并锚定到原始 3D 内容上。这与传统完全依赖手工算法和光栅化管线的渲染方式有所不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-ph/geforce/news/dlss-5-3d-guided-neural-rendering/">DLSS 5: 3 D - Guided Neural Rendering Debuts in NBA 2K27 | NVIDIA</a></li>
<li><a href="https://winbuzzer.com/2026/03/17/nvidia-dlss-5-gpt-moment-graphics-gtc-2026-xcxwbn/">Nvidia DLSS 5: AI Neural Rendering Coming Fall 2026</a></li>
<li><a href="https://purefeed.ai/blog/new_ai/dlss-5-neural-reconstruction-2d-motion-insights">DLSS 5 Explained: Neural Reconstruction from 2D + Motion | PureFeed</a></li>

</ul>
</details>

**标签**: `#DLSS`, `#NVIDIA`, `#Neural Rendering`, `#Gaming`, `#Graphics`

---

<a id="item-12"></a>
## [EvoUndo：验证并修复 LLM 智能体自我修改可恢复性的框架](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 7.5/10

论文提出了 EvoUndo 框架，用于表示、综合、诊断并独立验证 LLM 智能体自我修改在反事实状态下的可恢复性。在 600 个未见任务的评估中，扩展的恢复演算将经验性 oracle 恢复从 0/197 提升到 191/197 个自然失败案例。 自我进化的智能体修改自身代码和提示词时，可能造成不可逆的有害改变，这是安全部署的主要障碍。EvoUndo 表明，可恢复性需要共同设计验证、状态锚定、见证语义和恢复语言表达能力，而不仅仅是依赖迭代提示。 在 600 个一次性自我进化任务中，有 197 个能力提升型变异未通过可恢复性验证。一项协议锁定的 2×2 接地×表达能力干预实验显示，精确状态寻址接地将恢复率从 0/48 提升至 38/48，而扩展语言在 S1 层中实现了 142/143（99.3%）的恢复；在 gpt-oss-120b 上观察到的负向交互在 Qwen3.8-27B 上未复现，表明该效应依赖于模型。

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · 9月1日 19:17

**背景**: LLM 智能体越来越多地在运行时修改自身的提示词、工具、中间件、资源和执行框架以提升能力，这一过程常被称为自我进化。然而，这类变异可能留下持久影响，在与其创建时不同的状态下无法安全撤销。EvoUndo 将可恢复性作为一等验证属性，并提出了一个处理更一般反事实状态的扩展恢复演算，从而弥补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28363v1">EvoUndo : Recoverability-ConstrainedSelf-Evolution for LLM Agent...</a></li>
<li><a href="https://huggingface.co/papers/2608.28363">Paper page - EvoUndo : Recoverability-Constrained Self-Evolution for...</a></li>

</ul>
</details>

**标签**: `#LLM Agents`, `#Self-Evolution`, `#AI Safety`, `#Machine Learning Research`

---

<a id="item-13"></a>
## [Jujutsu 作者马丁加入 ERSC，引发版本控制工具讨论](https://ersc.io/blog/martin-joins-ersc) ⭐️ 7.0/10

Jujutsu 版本控制工具的创造者 Martin von Zweigbergk 已加入 ERSC，这家初创公司正将自己定位为 GitHub 的竞争对手。这一消息在 ERSC 博客上公布，并引发了关于 Jujutsu 价值定位的讨论。 这对开发者工具生态意义重大，因为 Jujutsu 是一款备受推崇、与 Git 兼容的替代工具，注重易用性和撤销功能。Martin 的加入增强了 ERSC 的可信度，并可能加速一个真正 GitHub 替代品的开发，从而影响开发者与版本控制社区。 Jujutsu（jj）是一款开源版本控制系统，由 Martin von Zweigbergk 于 2019 年底在 Google 作为业余项目启动，并且兼容 Git 仓库。公告中未透露具体产品路线图；Hacker News 上有评论者猜测 ERSC（East River Source Control）正试图构建 GitHub 的竞品。

hackernews · steveklabnik · 9月1日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=49525297)

**背景**: 版本控制系统（如 Git）帮助开发者跟踪和协调代码变更。Jujutsu（jj）是一款开源替代品，旨在通过更直观的命令模型、工作副本的自动快照和强大的撤销功能来改进 Git 的易用性，同时仍然兼容 Git 仓库。ERSC（East River Source Control）是一家早期初创公司，一些观察者认为它试图构建类似 GitHub 的协作平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.everydev.ai/tools/jujutsu-jj">Jujutsu - Git Compatible Version Control CLI | EveryDev.ai</a></li>
<li><a href="https://mskadu.medium.com/introducing-jujutsu-a-modern-alternative-to-git-32bb8b7fadd9">Introducing Jujutsu : A Modern Alternative to Git | Medium</a></li>
<li><a href="https://news.ycombinator.com/item?id=46292447">There has to be a VC in this thread, go ahead and fund a GitHub ...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人称赞 Jujutsu 的撤销功能和易用性，也有人质疑它对于日常 Git 工作流是否足够有优势。还有几位评论者对 ERSC 作为 GitHub 竞争对手的价值主张表示怀疑，认为新工具未必能解决 GitHub 现有问题。整体氛围是好奇与谨慎并存。

**标签**: `#jujutsu`, `#version-control`, `#git`, `#ERSC`, `#developer-tools`

---

<a id="item-14"></a>
## [交互式地图收录 13,312 部影视与游戏拍摄场景](https://moviescenemap.com/) ⭐️ 7.0/10

电影场景地图（Movie Scene Map）是一款交互式网页地图，收录了 13,312 部电影、剧集、游戏、动漫和漫画的拍摄地点。用户可浏览地点，并通过专门的提交页面补充缺失场景。 该工具将电影取景地趣闻变成可浏览、适合旅行的体验，吸引了影迷和选景人。它展示了小众众包数据如何在大型企业平台之外蓬勃发展。 该数据集涵盖 13,312 条多类型媒体条目，用户可通过 /missing/ 页面添加缺失影片。其界面以流畅平移和准确的场景级标记获得好评，但低缩放级别下重叠图钉可能遮挡数据。

hackernews · Flightmussy · 9月1日 16:34 · [社区讨论](https://news.ycombinator.com/item?id=49524320)

**背景**: 电影场景地图是一款交互式网页地图，用于标注电影、剧集、游戏、动漫和漫画中场景的拍摄位置。它依靠众包贡献来扩充数据库，与其他用户生成的地图项目类似。该网站的做法顺应了将小众娱乐数据整合到易用专业界面中的大趋势。

**社区讨论**: 评论者反应热烈，称该地图“太棒了”和“非常酷”，并提出了功能建议，例如添加媒体页面直接链接、修复缩放级别图钉遮挡、以及与大数据库合作。多位用户称赞设计与用户体验，同时指出本地区域缺少条目，并询问如何贡献内容。

**标签**: `#movies`, `#interactive-map`, `#web-app`, `#location-data`, `#entertainment`

---

<a id="item-15"></a>
## [Play Store 被曝屏蔽 AuroraStore，影响 GrapheneOS 用户](https://gitlab.com/AuroraOSS/AuroraStore/-/work_items/1566) ⭐️ 7.0/10

AuroraStore 在 GitLab 上的一个 bug 报告显示，Google Play Store 正在屏蔽 AuroraStore，导致其无法正常获取应用信息和更新。该报告引发广泛关注，但具体原因和机制尚未确认。 AuroraStore 是注重隐私的 Android 用户（尤其是避免使用 Google 服务的 GrapheneOS 用户）的重要工具。如果 Google 屏蔽它，用户可能失去一种无需 Google 账号即可安装应用的便捷方式，尽管 GrapheneOS 本身推荐使用沙盒版 Play Store。 该问题报告在 AuroraStore 的 GitLab work item 1566 中。用户反映被强制退出登录、无法连接服务器或应用无法更新；一些用户拒绝重新启用 Google 服务或使用 Google 账号登录作为变通方案。

hackernews · erikvanoosten · 9月1日 15:55 · [社区讨论](https://news.ycombinator.com/item?id=49523754)

**背景**: AuroraStore 是一个开源的 Google Play Store 替代客户端，允许用户无需 Google 账号即可浏览、搜索和安装应用，并支持匿名登录。GrapheneOS 是一个面向 Pixel 设备、以安全和隐私为重点的开源 Android 操作系统，约有 40 万活跃用户。许多注重隐私的用户依赖 AuroraStore 来避免将设备使用与 Google 身份绑定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Aurora_store">Aurora store</a></li>
<li><a href="https://gitlab.com/AuroraOSS/AuroraStore">Aurora OSS / AuroraStore · GitLab</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>

</ul>
</details>

**社区讨论**: 评论者对影响存在分歧：一些人指出 GrapheneOS 实际上推荐使用沙盒版 Play Store 而非 AuroraStore，另一些人则称更喜欢 AuroraStore，因为它没有恶劣的暗黑模式和令人反感的设计。多位用户认为标题有失偏颇，因为该帖子只确认了 bug，并未确认是 Google 故意屏蔽，且对 GrapheneOS 用户的影响尚不确定。还有人描述了实际使用场景，比如在安卓游戏掌机上运行购买的游戏，以及应用无法更新的困境。

**标签**: `#Android`, `#Privacy`, `#GrapheneOS`, `#AuroraStore`, `#Google Play Store`

---

<a id="item-16"></a>
## [Python 3.15.0 候选版 2 发布，维护者需提前准备](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 7.0/10

Hugo van Kemenade 宣布发布 Python 3.15.0 候选版 2（RC2），这是 10 月正式版发布前的最后一个候选版。公告强烈鼓励第三方项目维护者在此期间进行测试，并在 PyPI 上发布 Python 3.15 wheels，为最终发布做好准备。 这一里程碑意味着 Python 3.15 已进入功能冻结阶段，正式版发布前只会包含错误修复。它为整个生态系统提供了明确的兼容性测试窗口，让最终版本能够更平稳地惠及数百万 Python 用户和软件包维护者。 根据发布经理的说法，从 RC2 到最终版本之间只允许经过审查的缺陷修复变更。针对此 RC 构建的二进制 wheels 将与未来的 Python 3.15 版本兼容；该版本目前尚未通过 actions/python-versions 在 GitHub Actions 中提供，但可以在 actions/setup-python@v7 中使用 allow-prereleases 和 check-latest 参数进行测试。

rss · Simon Willison · 9月1日 14:59

**背景**: 候选版（RC）是软件发布生命周期中 Beta 测试之后的阶段，在此阶段软件会在最终正式发布前进一步完善并测试关键问题。PyPI 是 Python 官方的第三方软件仓库，软件包以源码归档（sdists）或包含二进制模块的预编译 wheels 形式分发。文章作者还提到，他曾在 Python 3.10 的 RC 阶段之后运行测试套件时发现一个 bug，而这个 bug 已经随正式版发布，这凸显了在 RC 阶段进行测试的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Release_candidate">Release candidate</a></li>
<li><a href="https://en.wikipedia.org/wiki/PyPI">PyPI</a></li>
<li><a href="https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/">Packaging and distributing projects - Python Packaging User Guide</a></li>

</ul>
</details>

**标签**: `#Python`, `#release candidate`, `#software development`, `#ecosystem`

---

<a id="item-17"></a>
## [YOLO26-RGB：复用 YOLO26 深度训练骨干网络进行图像去雨](https://www.reddit.com/r/MachineLearning/comments/1w4fxln/yolo26rgb_repurposing_yolo26s_depthtrained/) ⭐️ 7.0/10

作者发布了 YOLO26-RGB 图像去雨模型，该模型复用了 YOLO26 深度估计模型的骨干网络和 PAN-FPN 颈部，仅将深度头替换为新的 RGBHead。受控的 nano 规模实验表明，深度预训练初始化比随机初始化平均 PSNR 高 0.48 dB，并在全部 10 个测试集上获胜。 这项工作提供了证据，表明深度预训练的稠密回归权重比从头训练更好地迁移到去雨任务，挑战了默认依赖分类预训练骨干网络的做法。它还产出了紧凑的去雨模型（5.25M 和 12.13M 参数），并且可以直接从 YOLO26 预训练模型库中加载。 YOLO26-depth 检查点与 468 个骨干和颈部张量完全匹配，因此只有新的 RGBHead 被随机初始化；该头部采用残差输出、LayerNorm，以及来自 stride-2 和 stride-4 层的跳跃连接。模型使用 ClearView 的混合合成-真实雨图配方和 Charbonnier 损失训练，在 9 个仅含雨图的测试集上平均 PSNR 为 30.83–30.95。

reddit · r/MachineLearning · /u/Naive-Explanation940 · 9月1日 15:52

**背景**: YOLO26-depth 是 Ultralytics 发布的单目深度估计模型，它从单张 RGB 图像预测以米为单位的逐像素深度图。其 CSPDarknet 骨干和 PAN-FPN 颈部是 YOLO 系列的标准组件：CSP 代表 Cross Stage Partial，PAN-FPN 是一种用于多尺度特征融合的路径聚合网络。由于深度估计和图像去雨都属于稠密的逐像素回归任务，深度预训练权重在架构上比目标检测权重更接近图像恢复任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.roboflow.com/what-is-yolo-depth/">YOLO 26 Depth : Monocular Depth Estimation in Meters</a></li>
<li><a href="https://huggingface.co/blog/dronefreak/yolo26-rgb">YOLO26-RGB: a small, fast deraining model from YOLO26's depth ...</a></li>
<li><a href="https://arxiv.org/html/2508.00698">Can Large Pretrained Depth Estimation Models Help With Image ...</a></li>

</ul>
</details>

**标签**: `#transfer-learning`, `#computer-vision`, `#image-deraining`, `#YOLO`

---

<a id="item-18"></a>
## [2026 潜在推理格局：从 Coconut 到 BDH-CQ](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 7.0/10

一篇 Reddit 帖子将潜在推理方法划分为五个家族，包括 Coconut 等连续思维模型和 BDH-CQ 等上下文循环求解器。作者主张让 LLM 远离口头化的思维链、转向潜在推理是通向 AGI 的关键，并引用了 BDH-CQ 在 ARC-AGI-1 上的结果。 这一框架挑战了业界对思维链在推理、可解释性和评估中的重度依赖。如果潜在推理被证明更高效，它可能转移研究重点，并引发关于可读推理痕迹是否值得保留的难题。 五大家族包括：自回归 LM 中的连续思维（Coconut、Soft Thinking）、压缩的离散非语言词元（Abstract-CoT）、循环深度与环回模型、任务训练的递归求解器（HRM、TRM），以及上下文循环潜在求解器（BDH-CQ）。帖子还区分了模型获取任务的方式（上下文、记忆或梯度更新）以及中间计算发生的位置（语言词元、抽象词元或连续潜在状态）。

reddit · r/MachineLearning · /u/Typical-Scene-5794 · 9月1日 15:14

**背景**: 潜在推理是思维链（CoT）的一种替代方案：模型反复变换连续隐藏状态，仅解码最终答案，而不是将每个中间步骤用语言表达出来。研究人员认为，CoT 痕迹只是推理的模仿，并非推理机制本身，因此潜在推理可能更忠实且更高效。BDH-CQ 构建在 Dragon hatchling 架构之上，利用上下文演示写入循环记忆，从而对 ARC-AGI-1 等任务进行迭代的潜在计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/latent-reasoning-in-large-language-models">Latent Reasoning in LLMs</a></li>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in...</a></li>
<li><a href="https://www.emergentmind.com/topics/bdh-cq">BDH - CQ : Recurrent Latent Reasoning for ARC</a></li>

</ul>
</details>

**标签**: `#latent reasoning`, `#language models`, `#chain-of-thought`, `#AGI`, `#continual learning`

---

<a id="item-19"></a>
## [瑞银：中国十年内难追平 ASML EUV，DUV 或 2 至 5 年量产](https://thenextweb.com/news/ubs-china-asml-euv-decade-immersion-duv-dutch-export-licence) ⭐️ 7.0/10

瑞银分析师估计，中国光刻项目大致相当于 ASML 2004 年的水平，十年内难以造出可行的 EUV 替代品；但预计浸润式 DUV 光刻机有望在 2 至 5 年内实现大规模量产。 这一评估凸显了中国与 ASML 之间持续存在的技术差距，以及荷兰出口管制对中国半导体自主化的影响。ASML 浸润式 DUV 设备售价接近 9000 万美元，而 2025 年第三季度中国占其净销售额的 42%，因此这一进展将影响全球供应链和地缘政治格局。 ASML 的 EUV 系统单台售价超过 2 亿美元，而浸润式 DUV 系统售价接近 9000 万美元。报告还指出，中国本土光刻项目大致相当于 ASML 2004 年的技术水平，DUV 的量产可能还需 2 至 5 年。

telegram · zaihuapd · 9月1日 13:58

**背景**: 光刻是使用光线在晶圆上印制微芯片图案的工艺，光线波长越短，能制造的特征越小。ASML 是唯一的 EUV 光刻系统供应商，其设备使用波长为 13.5nm 的光；而 DUV 系统主要使用 193nm 波长的 ArF 激光，并借助浸没式光刻和多重曝光技术实现更小的特征。受美国主导的出口限制影响，中国一直致力于发展本土光刻能力，而先进的浸润式 DUV 光刻机受到荷兰出口许可管制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/duv-lithography-systems">DUV lithography systems | Products</a></li>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>

</ul>
</details>

**标签**: `#半导体`, `#光刻机`, `#EUV`, `#DUV`, `#地缘政治`

---

<a id="item-20"></a>
## [Mozilla 为 iOS 版 Firefox 增加内置广告拦截功能](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/) ⭐️ 6.0/10

Mozilla 为 iOS 版 Firefox 推出了内置广告拦截功能，并逐步向用户推送。该拦截器基于 Apple 的 WebKit 内容拦截器 API 构建，但不会拦截 YouTube 或搜索引擎广告。 这一功能意义重大，因为此前 iOS 版 Firefox 没有像安卓版和桌面版那样的内置广告拦截能力。它为 iOS 用户提供了更多隐私保护和广告控制，但其局限性也反映出 WebKit 的限制以及 Mozilla 在财务上对 Google 的依赖。 该广告拦截器不拦截 YouTube 广告和搜索引擎结果页中的广告，并且用户需要先开启遥测才能使用。该功能正在分阶段推送，因此并非所有用户都能立即使用。

hackernews · HieronymusBosch · 9月1日 13:46 · [社区讨论](https://news.ycombinator.com/item?id=49521973)

**背景**: iOS 上所有浏览器都必须使用 Apple 的 WebKit 引擎，因此 iOS 版 Firefox 本质上是使用不同界面的 Safari 内核。iOS 的内容拦截依赖于 Content Blocker API，其灵活性不如 uBlock Origin 等桌面扩展。Mozilla 在历史上相当依赖 Google 的收入，这或许可以解释为什么该拦截器不拦截搜索广告和 YouTube 广告。该功能正在逐步推送，且需要开启遥测才能使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebKit">WebKit - Wikipedia</a></li>
<li><a href="https://thenextweb.com/news/firefox-ios-ad-blocker-webkit-content-blocker-dma-browser-engine">Mozilla adds a built-in ad blocker to Firefox on iOS , built on...</a></li>

</ul>
</details>

**社区讨论**: 评论区整体态度谨慎且带有批评。许多用户指出该拦截器不会拦截 YouTube 或搜索引擎广告，可能是因为 Mozilla 依赖 Google 的收入；另一些用户对缓慢的分阶段推送和必须开启遥测感到不满。有人说他们仍需 Brave 或 Orion 等浏览器来获得完整的广告拦截体验。

**标签**: `#Firefox`, `#iOS`, `#Ad-blocking`, `#Mozilla`, `#Privacy`

---
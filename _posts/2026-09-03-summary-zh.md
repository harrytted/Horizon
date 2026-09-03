---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> 从 36 条内容中筛选出 20 条重要资讯。

---

1. [谷歌发布 Gemini 3.8 Flash 及专用网络安全模型 Cyber](#item-1) ⭐️ 9.0/10
2. [Muse Spark 1.3](#item-2) ⭐️ 8.0/10
3. [三个网站批量生成 21.5 万个“最佳软件”页面，Perplexity 将其作为引用来源](#item-3) ⭐️ 8.0/10
4. [Paint.NET 作者借助 Claude 完成 18 万行 Direct2D 洁净室重写，实现对 WINE 的支持](#item-4) ⭐️ 8.0/10
5. [多数开源 AI 检测器无法达到 0.5%误报率](#item-5) ⭐️ 8.0/10
6. [阿里发布 Qwen3.8-Max-0902，CodeArena 编程榜 1691 分夺冠](#item-6) ⭐️ 8.0/10
7. [英伟达据报以 129 亿美元收购 Hugging Face](#item-7) ⭐️ 8.0/10
8. [月之暗面与微软、亚马逊、谷歌洽谈 Kimi K3 收入分成](#item-8) ⭐️ 8.0/10
9. [FBI 调查暗网服务 Nexus 出售 1.53 亿驾照扫描件](#item-9) ⭐️ 8.0/10
10. [谷歌广告技术业务免于被法院勒令拆分](#item-10) ⭐️ 7.0/10
11. [Fable 5.1 世界建模](#item-11) ⭐️ 7.0/10
12. [Mistral AI 数据训练退出选项变更引发隐私争议](#item-12) ⭐️ 7.0/10
13. [LZ 暗物质探测器记录到一个奇异粒子事件](#item-13) ⭐️ 7.0/10
14. [C++库 Deepity 展示预测编码网络在 MNIST 上媲美反向传播](#item-14) ⭐️ 7.0/10
15. [Jasper Research 发布从头训练文生图模型的指南与代码库](#item-15) ⭐️ 7.0/10
16. [纽约公立学校将自 2026-27 学年起禁止低年级学生使用生成式 AI](#item-16) ⭐️ 7.0/10
17. [老化大脑或会融合相似记忆，而不仅仅是遗忘](#item-17) ⭐️ 6.0/10
18. [Anthropic 更新 Claude 系统提示词，严格限制复现歌词](#item-18) ⭐️ 6.0/10
19. [Reddit 用户公开 59.4 亿 TikTok 视频与 32.3 亿个人资料数据集](#item-19) ⭐️ 6.0/10
20. [CABiNet 作者在 UAVid 上对比 YOLO26-sem 的评测](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 3.8 Flash 及专用网络安全模型 Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 9.0/10

谷歌 DeepMind 发布了 Gemini 3.8 Flash 这一更新版精简模型，以及专门的网络安全变体 Gemini 3.8 Flash Cyber。新模型承诺更高的速度、更低的成本，以及面向智能体与安全工作流的顶尖基准测试成绩。 Gemini Flash 系列被广泛用于实际 AI 任务，因此在速度、成本和质量上的改进会产生广泛影响。Cyber 变体还回应了日益增长的 AI 驱动漏洞检测需求，可能对更昂贵的顶级模型形成挑战。 Gemini 3.8 Flash 基于 Gemini 3.7 Flash 构建，在 Artificial Analysis 智能指数上得分约 59，与 Opus 5 medium 持平。Cyber 版本在内部渗透测试基准上召回率提高 7.5%至 9.7%，成本却降低 2.3 至 5.2 倍，并通过 Fairwind 计划提供给受信任的防御方。

hackernews · bratao · 9月2日 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553)

**背景**: Gemini 是谷歌 DeepMind 推出的多模态大语言模型系列，其中 Flash 版本面向低延迟、低成本部署设计。像 Cyber 这样的网络安全模型用于漏洞发现、自动修补和渗透测试等任务。此次发布紧随 Gemini 2.5 及多次 Flash 更新，并且通过支持音频和视频输入兼顾智能体工作流与媒体分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3.8 Flash and 3.8 Flash Cyber</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3 . 8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/">Google releases Gemini 3.8 Flash, its third Flash model in six weeks - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 早期反应热烈但并非一致。Simon Willison 强调该模型在 HTML/JavaScript 生成方面表现出色，且多模态媒体分析成本很低，但也指出低思考强度相对于 Gemini 3.7 可能有所退步；另一位评论者表示在其旅行规划测试中 Gemini 3.7 在实际知识上仍胜出。一些用户称赞它在 DeepSWE 上超越 Opus 5 且成本低，但也表示要等待实际使用后再判断。

**标签**: `#Gemini`, `#Google DeepMind`, `#AI models`, `#LLM`, `#machine learning`

---

<a id="item-2"></a>
## [Muse Spark 1.3](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta 的 Muse Spark 1.3 AI 模型以极低成本提供接近 SOTA 的性能，引发了开发者社区的热情和实用好评。

hackernews · bvaldivielso · 9月2日 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**标签**: `#AI/ML`, `#Meta`, `#model release`, `#benchmarks`, `#LLM`

---

<a id="item-3"></a>
## [三个网站批量生成 21.5 万个“最佳软件”页面，Perplexity 将其作为引用来源](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

trellner.com 的一份新报告显示，三个网站自动生成了 215,128 个“最佳软件”推荐页面，而 Perplexity AI 的答案引擎现在会在回答中将这些页面作为来源加以引用。 这表明 AI 生成的内容农场能够操纵 AI 搜索推荐，形成一种将合成、低质量页面视为权威来源的恶性循环。它削弱了人们对 AI 答案引擎乃至整个网络搜索生态的信任。 一位评论者分享的 Semrush 数据显示，涉及的三个域名是 wifitalents.com、worldmetrics.org 和 gitnux.org，其自然访问量峰值约为每月 8,000 至 18,000 次，此后便出现下滑。这些页面采用程序化 SEO 模板策略，瞄准“最佳软件”等长尾查询，而非基于原创调研。

hackernews · jakobgreenfeld · 9月2日 13:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**背景**: Perplexity 是一家成立于 2022 年的 AI 答案引擎，它结合大语言模型与实时网络搜索来综合生成回答，并提供来源引用。程序化 SEO（Programmatic SEO）是一种利用模板自动生成大量网页，以针对长尾搜索关键词排名的做法。当 AI 搜索引擎将这些程序化生成的页面用作证据时，就可能使 AI 生成或低质量内容获得不应有的权威地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perplexity_AI">Perplexity AI</a></li>
<li><a href="https://www.semrush.com/blog/programmatic-seo/">What Is Programmatic SEO? Examples + How to Do It - Semrush</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为 LLM 缺乏对来源的怀疑能力，甚至会更偏爱 AI 生成的内容：有用户在代码偏好测试中复现了这种效果，也有用户表示曾被推荐一个完全虚构的“Foobar 广场”。Perplexity 用户还反映其答案质量明显下滑；评论区分享的 Semrush 分析显示，被引用域名的自然流量已经开始回落。

**标签**: `#AI`, `#Perplexity`, `#content-farms`, `#AI-generated-content`, `#search-quality`

---

<a id="item-4"></a>
## [Paint.NET 作者借助 Claude 完成 18 万行 Direct2D 洁净室重写，实现对 WINE 的支持](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Paint.NET 作者 Rick Brewster 透露，Paint.NET 现在内置了一个借助 Anthropic 的 Claude 从零编写、采用洁净室方式的 Direct2D API 重写版本。通过 /wine 启动参数触发后，Paint.NET 可以在微软原始 Direct2D 实现不够完善的 WINE 环境下运行。 这是一个重要的真实案例，展示了 AI 编程智能体有能力完成规模庞大、但可信赖的系统级逆向工程任务。同时，Brewster 表示他无法彻底审查这 18 万行生成代码，这也凸显了“随性编码”（vibe coding）的风险。 新的库被打包为 PaintDotNet.Windows.Direct2D1.Managed.dll，并且只在 WINE 环境中启用。Brewster 表示这些代码属于“随性编码”，需要他持续盯守：Claude 起初没有正确处理 COM 引用计数（相当于漏掉 AddRef），有时还会做出糟糕的设计或架构决策，但它也逆向推导出了 Direct2D 内置效果库所需的公式。

rss · Simon Willison · 9月2日 05:50

**背景**: Direct2D 是微软提供的一种硬件加速的即时模式 2D 图形 API，Windows 应用常用它绘制几何图形、位图和文本。WINE 是一个开源兼容层，让为 Windows 开发的应用程序能够在 Linux 等类 Unix 操作系统上运行。洁净室（clean-room）重写是一种重新实现专有功能的方法：一个团队只根据对外部行为的观察编写规格说明，另一个团队再根据该规格进行实现，从而避免直接使用原版受版权保护的源代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clean-room_reverse_engineering">Clean-room reverse engineering</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#Reverse engineering`, `#WINE compatibility`, `#Graphics APIs`, `#Software engineering`

---

<a id="item-5"></a>
## [多数开源 AI 检测器无法达到 0.5%误报率](https://www.reddit.com/r/MachineLearning/comments/1w58erw/most_opensource_ai_detectors_cant_hold_a_05/) ⭐️ 8.0/10

一项针对六款开源 AI 检测器的公共数据集基准评测发现，其中四款根本无法达到匹配的 0.5%误报率。经“人类化”改写的 AI 文本使召回率大幅下降，最好的检测器也只能识别 42%；OpenAI 旧版 RoBERTa 检测器在现代生成器上 AUC 仅为 0.31，还不如随机猜测。 该结果削弱了人们对开源 AI 检测器在学术诚信、内容审核和虚假信息防控等领域广泛使用的信心，尤其是在误报代价高昂的低误报率场景下。评测还揭示了检测器对非母语英语写作者的系统性偏见，并暴露出其对改写工具的脆弱性。 评测将每款检测器的阈值在相同的 6,930 篇人类文档上校准至 0.5%误报率，然后分别测量对原始 AI 文本、人类化改写 AI 文本和前沿模型（GPT-5.x、Claude Opus 5、Gemini 3.x）输出文本的召回率。由于 MAGE 对 26%的普通人类网页文本打出高于 0.9999 的分数，它在任何阈值下都无法达到 0.5%误报率。

reddit · r/MachineLearning · /u/grumpyp2 · 9月2日 12:04

**背景**: AI 文本检测器的目标是区分人类书写文本与 LLM 生成文本；代表性的开源项目包括 OpenAI 基于 RoBERTa 的 GPT-2 输出检测器，以及 ACL 2024 论文中的机器生成文本检测测试框架 MAGE。这类检测器通常先设定误报率阈值，再测量召回率。而“人类化”改写工具能把 AI 输出改得更自然，非母语英语写作也可能与 AI 文本相似，这两者都增加了检测难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/yafuly/MAGE">GitHub - yafuly/MAGE: Machine-generated text detection in the wild (ACL 2024) · GitHub</a></li>
<li><a href="https://github.com/openai/gpt-2-output-dataset/blob/master/detector/README.md">gpt-2-output-dataset/detector/README.md at master · openai ...</a></li>
<li><a href="https://quillbot.com/ai-humanizer">Humanize AI Text: Free AI Humanizer by Quillbot</a></li>

</ul>
</details>

**标签**: `#AI detection`, `#benchmarking`, `#LLMs`, `#machine learning`, `#bias`

---

<a id="item-6"></a>
## [阿里发布 Qwen3.8-Max-0902，CodeArena 编程榜 1691 分夺冠](https://mp.weixin.qq.com/s/BfKRXMAR5ykD58LDkBftLg) ⭐️ 8.0/10

阿里巴巴发布了新一代旗舰模型 Qwen3.8-Max-0902，在 CodeArena 前端编程总榜上以 1691 分夺冠，较旧版提升 22 分。该模型已通过 Qwen AI 平台以 API 形式上线，输入每百万 tokens 收费 2 美元，输出每百万 tokens 收费 6 美元。 这一发布意义重大，因为 Qwen3.8-Max-0902 在一个由人工精选的编程基准上取得了顶尖成绩，而其综合均价约为每百万 tokens 5 美元，远低于榜单第二名和第三名模型的 20 美元和 12 美元。它增强了阿里巴巴在全球大模型市场的竞争力，也降低了使用先进 AI 辅助编程的成本门槛。 该模型拥有 2.4T 参数和 100 万 tokens 的上下文长度，并针对编程与专业办公任务进行了进一步后训练。目前已接入千问 AI 平台、千问办公、Qoder 与千问 APP。

telegram · zaihuapd · 9月2日 06:05

**背景**: CodeArena 是一个严谨的、由人工精选的代码大模型评估基准，包含 397 个高质量样本，覆盖 40 个类别和 44 种编程语言，旨在模拟真实世界编程任务的复杂度。Qwen 是阿里巴巴的大语言模型系列，其 AI 编程工具包括 Qoder IDE。Qwen3.8-Max-0902 是对阿里现有 Qwen3.8-Max 系列的增量更新，重点强化了编程与办公任务的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codearenaeval.github.io/">CodeArenaEval</a></li>
<li><a href="https://aclanthology.org/2025.emnlp-main.489/">CodeArena: Evaluating and Aligning CodeLLMs on Human ...</a></li>
<li><a href="https://www.alibabacloud.com/en/campaign/ai-scene-ai-agent-qoder?_p_lc=1">Qoder – All in One AI coder</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Qwen`, `#CodeArena`, `#Alibaba`

---

<a id="item-7"></a>
## [英伟达据报以 129 亿美元收购 Hugging Face](https://www.techzine.eu/news/analytics/143877/nvidia-to-acquire-hugging-face-for-12-9-billion/) ⭐️ 8.0/10

据报道，英伟达已达成协议，以 129 亿美元收购开源 AI 模型与数据集平台 Hugging Face。两家公司尚未正式回应，因此该交易目前仍未得到确认。 如果交易完成，全球最大的开源 AI 平台将落入英伟达手中，使这家芯片厂商在 AI 模型和数据集的共享与分发方式上拥有巨大影响力。这可能会重塑开源 AI 生态，并影响依赖 Hugging Face 的开发者、创业公司和企业。 Hugging Face 的年化收入约为 1.5 亿美元，意味着报道中 129 亿美元的价格对应非常高的估值倍数。英伟达曾于 2023 年参与 Hugging Face 2.35 亿美元的融资，这提供了相关背景，但并不能证实这笔收购。

telegram · zaihuapd · 9月2日 06:50

**背景**: Hugging Face 是一家总部位于纽约的公司，专注于开发机器学习工具，最著名的是 Transformers 库，以及让用户共享模型和数据集的开放平台。英伟达是 AI 训练芯片的主导供应商，收购 Hugging Face 将把其硬件业务与 AI 社区最核心的软件平台之一连接起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face</a></li>
<li><a href="https://www.ibm.com/think/topics/hugging-face">What is Hugging Face? - IBM</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Hugging Face`, `#acquisition`, `#AI`, `#open-source`

---

<a id="item-8"></a>
## [月之暗面与微软、亚马逊、谷歌洽谈 Kimi K3 收入分成](https://www.jiemian.com/article/15040119.html) ⭐️ 8.0/10

月之暗面正与微软、亚马逊和谷歌进行早期谈判，希望在其开源 Kimi K3 模型通过对方云平台分发时获得最高 30% 的收入分成。若达成，这将是中国 AI 公司与美国主要云服务商之间的首个大型模型收入分成协议。 这可能为中国的开源权重前沿模型如何在西方云基础设施上实现商业托管开创先例，并为月之暗面带来来自美国平台的直接收入流。这也表明，在地缘政治紧张的背景下，美国云巨头仍愿意将中国模型商业化。 谈判仍处于早期阶段，核心条款未确定，相关企业均拒绝置评。Kimi K3 于 2026 年 7 月发布，总参数达 2.8 万亿，支持 100 万 token 的上下文窗口并具备原生视觉能力；该模型的许可已要求年收入超过 2000 万美元的推理服务商分享最高 30% 的收入。截至 6 月中旬，月之暗面的年度经常性收入据称已突破 3 亿美元。

telegram · zaihuapd · 9月2日 07:36

**背景**: 月之暗面是一家总部位于北京的人工智能公司，被称为中国“AI 六小龙”之一，以开源权重的大型语言模型 Kimi 系列著称。与传统开源软件不同，前沿开源权重模型越来越多采用自定义许可：允许使用，但超过收入门槛后须分享部分商业收入。Kimi K3 被描述为迄今发布过的最大开源权重模型；有关微软、亚马逊和谷歌的谈判也反映出更广泛的行业趋势，阿里巴巴同样计划为其下一代 Qwen 模型设置类似的分成条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://qz.com/alibaba-qwen-open-source-revenue-sharing-080726">Alibaba plans revenue sharing for next open-source Qwen AI ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Cloud Computing`, `#Revenue Sharing`, `#Moonshot AI`

---

<a id="item-9"></a>
## [FBI 调查暗网服务 Nexus 出售 1.53 亿驾照扫描件](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 8.0/10

FBI 正在调查暗网身份盗窃服务 Nexus，该服务声称掌握并出售超过 1.53 亿张美国和加拿大驾照的数字扫描件。Nexus 最近出现在俄语网络犯罪论坛 Exploit 上，已开始对外售卖这些数据。 如果数据属实，超过 1.53 亿人可能面临身份盗用和欺诈的风险，因为驾照包含高度敏感的个人信息。这凸显了过去泄露事件中被盗记录的聚合数据正被打包成商业化的网络犯罪服务。 KrebsOnSecurity 称，这些驾照扫描件可能来自汽车经销商、保险公司等机构此前泄露的旧文件，官方尚未确认具体来源和受影响人数。早期报道还显示，该批数据与 IDScan.net 相关的记录有关。

telegram · zaihuapd · 9月2日 09:31

**背景**: 暗网论坛和市场是买卖被盗个人数据的常见渠道。驾照尤其具有价值，因为它包含姓名、住址、出生日期甚至照片，可用于身份欺诈、账户接管和金融犯罪。像 Nexus 这样的身份信息窃取服务会将此前泄露事件中的数据聚合起来，向买家出售访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technadu.com/fbi-investigates-nexus-dark-web-service-selling-over-153-million-us-and-canadian-drivers-licenses/634891/">FBI Probes Nexus Over 153M US and Canadian... - TechNadu</a></li>
<li><a href="https://shattered.io/nexus-dark-web-153-million-driver-licenses-2026/">Nexus Dark Web Sells 153M Driver Licenses: FBI Probes</a></li>

</ul>
</details>

**标签**: `#security`, `#data breach`, `#dark web`, `#privacy`, `#identity theft`

---

<a id="item-10"></a>
## [谷歌广告技术业务免于被法院勒令拆分](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) ⭐️ 7.0/10

谷歌挫败了美国政府强制其出售广告技术业务的诉讼请求，避免了公司被法院勒令拆分。这一裁决是在谷歌已被认定构成垄断的反垄断案件的补救措施阶段作出的。 这对美国反垄断执法机构而言是一次重大挫折，并可能影响法院今后如何处理针对数字平台巨头的补救措施。谷歌得以保留其广告技术基础设施，这关系到开放网络上的发布方、广告主和竞争格局。 谷歌广告技术业务去年创造了约 300 亿美元收入，约占 Alphabet 总收入的 8%，但该业务收入已连续 16 个季度下滑。文章援引的分析师估计，该业务对 Alphabet 利润的贡献不足 1%。

hackernews · donohoe · 9月2日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=49537131)

**背景**: 广告技术是指用于购买、销售、管理和分析数字广告的软件与工具。谷歌的广告技术业务通过广告交易平台、广告服务器等产品连接广告主与内容发布方。在反垄断法中，“拆分”是一种结构性补救措施，即强制公司出售部分业务以恢复竞争。美国政府正是在谷歌被认定垄断多项广告技术市场后请求采取这一补救措施的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ad_tech">Ad tech</a></li>
<li><a href="https://adtech.org/what-is-adtech/">What Is AdTech | AdTech</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍对结果持怀疑态度。有评论认为，既然判定构成垄断，就不应仅以停止滥用行为作为补救；还有评论指出 Alphabet 总收入中 75% 来自广告，认为“广告技术”不过是核心业务的委婉说法。也有评论跳出本案，建议对垄断企业征收累进税，并质疑企业合并容易而拆分几乎不可能的不对称现象。

**标签**: `#antitrust`, `#google`, `#adtech`, `#regulation`, `#big tech`

---

<a id="item-11"></a>
## [Fable 5.1 世界建模](https://github.com/PhiloLabs/fable51-worlds) ⭐️ 7.0/10

Fable 5.1 世界建模是一个开源项目，可从图像生成 3D 世界环境，引发了关于其在游戏开发中的实际应用及架构分类的 HN 讨论。

hackernews · surreal_ · 9月2日 19:49 · [社区讨论](https://news.ycombinator.com/item?id=49541458)

**标签**: `#world-modeling`, `#generative-ai`, `#3d-assets`, `#game-development`, `#machine-learning`

---

<a id="item-12"></a>
## [Mistral AI 数据训练退出选项变更引发隐私争议](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) ⭐️ 7.0/10

Mistral AI 的帮助页面称用户有权选择退出其输入和输出数据用于模型训练，但社区报告显示该公司更改了账户设置，使付费层级（如 Team）默认加入训练。这些更改逆转了此前允许组织集中禁用训练数据使用的选项。 此次事件影响了那些因欧洲数据保护优势而选择 Mistral 而非美国竞争对手的企业和注重隐私的用户。它也凸显了行业更广泛的担忧：随着 AI 供应商扩大使用客户数据训练模型，他们是否会兑现退出承诺。 帮助页面称数据“在某些情况下”可能被纳入训练，用户可以随时退出，但社区评论描述了这一功能的局限性和默认设置的变动。具体来说，Team 层级据报失去了通过组织仪表板集中禁用训练的能力。

hackernews · teekert · 9月2日 12:30 · [社区讨论](https://news.ycombinator.com/item?id=49535284)

**背景**: Mistral AI 是一家法国人工智能公司，成立于 2023 年，以其开源权重和商业大语言模型而闻名。它已成为欧洲领先的 AI 企业，估值超过 140 亿美元，并将自身定位为美国供应商之外注重隐私的替代选择。如今许多 AI 产品默认使用用户对话和文档进行训练，各公司提供不同条款下的退出设置。用户和组织经常仔细审查这些控制措施，因为训练政策可能在采用后发生变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mistral_AI">Mistral AI</a></li>
<li><a href="https://aidigitalspace.com/ai-training-on-your-data-opt-out/">AI Training on Your Data: How to Safely Opt Out on Every ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍表达怀疑和失望。有用户认为 AI 公司无论如何都会在未经同意的情况下使用数据训练，也有用户描述为了更好隐私而更换套餐后，默认设置却被悄悄修改的经历。还有评论者提醒说，这个编辑化的标题曲解了帮助页面实际给出的退出保证。

**标签**: `#AI`, `#privacy`, `#data-training`, `#Mistral`, `#LLM`

---

<a id="item-13"></a>
## [LZ 暗物质探测器记录到一个奇异粒子事件](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle) ⭐️ 7.0/10

运行全球最大暗物质探测器的 LUX-ZEPLIN（LZ）合作组，在其实验数据中记录到一个无法解释的粒子事件。团队虽已公布这一观测结果，但强调仅凭单个事件远不足以宣称发现新物理学。 如果这个事件确实是暗物质而非未被识别的本底，它就可能暗示超越标准模型的新物理，并帮助解决天文学最大的谜团之一。由于 LZ 探测器在规模和灵敏度上独一无二，即便是单个异常也值得深究；但历史表明，大多数这类 3-sigma 迹象最终都会消失。 LZ 探测器位于南达科他州桑福德地下研究设施中一座前金矿的地下 1480 米处。据阅读过 LZ 预印本的评论者称，合作组在发表前已深入排查了可能的背景来源和错误重建事件，目前正在积累更多数据，以观察该事件是否会重现。

hackernews · randycupertino · 9月2日 13:40 · [社区讨论](https://news.ycombinator.com/item?id=49536079)

**背景**: 暗物质是一种不可见物质，约占宇宙物质总量的 85%，人们只能通过它对星系和宇宙微波背景的引力效应推断其存在，从未直接观测到。LZ 这类直接探测实验，是在极安静的探测器内寻找暗物质粒子——最常被假设为弱相互作用大质量粒子（WIMP）——与原子核碰撞的信号。探测器埋在废弃矿井深处并使用液氙作为靶材，可屏蔽宇宙射线等本底，让稀有信号得以显现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LZ_experiment">LZ experiment - Wikipedia</a></li>
<li><a href="https://lz.lbl.gov/">The LZ Dark Matter Experiment | The status and science of the LZ ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Direct_detection_of_dark_matter">Direct detection of dark matter - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 网上评论者的态度是谨慎好奇，而非确信。不少人称赞研究团队的严谨，同时提醒粒子物理学中许多 3-sigma“发现”会随数据增多而消失；也有人引用 LZ 联合创始人 Tom Shutt 的话，称物理学家必须认真思考这一个事件可能意味着什么。少数评论者还称赞了前金矿的重新利用，并感叹物理学距离找到“一切”还有多远。

**标签**: `#dark matter`, `#particle physics`, `#LZ experiment`, `#physics anomaly`, `#scientific discovery`

---

<a id="item-14"></a>
## [C++库 Deepity 展示预测编码网络在 MNIST 上媲美反向传播](https://www.reddit.com/r/MachineLearning/comments/1w5fuhm/deepity_a_c_library_showing_predictive_coding/) ⭐️ 7.0/10

作者发布了 Deepity，这是一个 C++ 机器学习库，通过 Direct Kolen-Pollack (DKP) 反馈对齐和算法缓存实现了加速的预测编码网络。在 MNIST 上（50 个 epoch，CPU），Deepity 在 59.5 秒内达到 97.73% 的测试准确率，接近 PyTorch 反向传播在大约 70 秒内取得的 98.27% 准确率。 这很重要，因为预测编码网络具有生物学合理性，并在局部学习和持续学习方面很有前景，但此前它们因速度太慢而无法实际应用。在标准基准上缩小了与反向传播在准确率和速度上的差距，这表明 PCN 有望成为在没有全局误差信号的情况下训练深度网络的可行替代方案。 性能提升来自最近关于使用 Direct Kolen-Pollack 反馈对齐加速 PCN 的研究，以及通过缓存避免推理收敛阶段中冗余的前向投影。作者接下来的计划是将内核移植到 CUDA，并在标准反向传播难以应付的持续学习场景中测试该库。

reddit · r/MachineLearning · /u/Important-Home4431 · 9月2日 16:49

**背景**: 反向传播通过将全局误差信号逐层向后传递来训练神经网络，虽然高效，但被认为在生物学上不太合理。预测编码网络则通过自上而下的预测和自下而上的感觉信号来最小化层与层之间的局部预测误差，从而支持局部学习规则。Direct Kolen-Pollack predictive coding (DKP-PC) 是最近的一种算法，它将 Direct Feedback Alignment 与 Kolen-Pollack 的反馈权重更新相结合，从而提升了 PCN 的训练速度。Deepity 是一个轻量级的 C++ 实现，将这些思想与底层 CPU 优化结合在了一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.15571v1">Accelerated Predictive Coding Networks via Direct Kolen ...</a></li>
<li><a href="https://github.com/mbwebster/dkp-gist">GitHub - mbwebster/dkp-gist: Implementation of the Direct ...</a></li>
<li><a href="https://www.emergentmind.com/topics/predictive-coding-networks-pcns">Predictive Coding Networks ( PCNs )</a></li>

</ul>
</details>

**标签**: `#Predictive Coding Networks`, `#Backpropagation`, `#C++ Library`, `#MNIST`, `#Local Learning`

---

<a id="item-15"></a>
## [Jasper Research 发布从头训练文生图模型的指南与代码库](https://www.reddit.com/r/MachineLearning/comments/1w5c9rd/detailed_explanation_of_how_to_create_a/) ⭐️ 7.0/10

Jasper Research 发布了一份详尽的技术指南、nano-t2i 代码库和 MONET 数据集，使开发者能够从头训练一个文生图模型。nano-t2i 代码库可在单块 H200 GPU 上以低于 300 美元的成本训练一个 flow-matching 模型，而 MONET 数据集包含约 1.049 亿对经过筛选的图像-文本对。 这件事之所以重要，是因为它为研究人员和从业者提供了一条开放、可复现且成本低廉的学习路径，帮助他们理解前沿实验室是如何构建文生图模型的。它降低了深入理解和实验生成式 AI 的门槛，填补了开放教育资源方面的一个空白。 MONET 数据集采用 Apache-2.0 许可证，是从 29 亿对原始图像-文本对中经过过滤、去重和重新生成描述后构建的。这份交互式指南托管在 Hugging Face Spaces 上，包含完整的思路讲解和中间结果，既适合学习者，也适合对业界实践感兴趣的人。

reddit · r/MachineLearning · /u/dh7net · 9月2日 14:40

**背景**: 文生图模型根据自然语言描述生成图像，通常使用大规模图像-文本数据集以及扩散或 flow matching 等技术。从头训练这类模型一般需要巨大的计算资源和精心整理的数据，而这些很少被公开提供。通过发布 MONET 和 nano-t2i，Jasper Research 旨在让从数据准备到模型训练的完整流程变得透明且可复现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/gojasper/nano-t2i">GitHub - gojasper/nano-t2i: Minimal training code of a nano ...</a></li>
<li><a href="https://gojasper.github.io/monet/">MONET - gojasper.github.io</a></li>

</ul>
</details>

**标签**: `#text-to-image`, `#generative models`, `#deep learning`, `#tutorial`, `#dataset`

---

<a id="item-16"></a>
## [纽约公立学校将自 2026-27 学年起禁止低年级学生使用生成式 AI](https://abc7ny.com/post/new-york-city-public-schools-banning-ai-use-middle-school-year/19778716/) ⭐️ 7.0/10

纽约市公立学校将从 2026-2027 学年起，禁止八年级及以下学生在课堂上使用聊天机器人、AI 辅导等生成式 AI 工具。高中生只能在受限条件下使用这些工具，教师仍可使用获批准的 AI 用于备课、翻译等任务。 这是美国规模最大的 K-12 生成式 AI 限制措施之一，影响近 60 万名学生，为其他学区监管快速发展的 AI 工具树立了先例。该政策也反映了教育创新与人们对屏幕时间、学生隐私和身心发展问题的担忧之间的紧张关系。 新的屏幕时间规定为：学前班至二年级的课堂不使用个人学习设备，三至五年级每天最多使用 30 分钟，初中生每天最多使用 45 分钟。教师仍可使用获批准的 AI 进行备课、翻译和撰写通知，但不得用于评分、行为监控、危机辅导或制定特殊教育计划。

telegram · zaihuapd · 9月2日 14:38

**背景**: 纽约市公立学校系统是美国最大的学区，这项政策将影响大约 60 万名学生。生成式 AI 指的是聊天机器人、AI 辅导等能够根据用户输入生成新内容的工具。这一决定出台之际，美国国内正在围绕学校应如何整合 AI，同时应对学术诚信、屏幕依赖和儿童发展等风险展开讨论。

**标签**: `#AI regulation`, `#education policy`, `#generative AI`, `#New York City`, `#screen time`

---

<a id="item-17"></a>
## [老化大脑或会融合相似记忆，而不仅仅是遗忘](https://studyfinds.com/aging-brains-blend-memories-together-instead-of-forgetting-them-study-finds/) ⭐️ 6.0/10

这则新闻介绍了一项研究，指出与年龄相关的记忆衰退可能源于相似记忆发生重叠或“融合”，而非单纯遗忘。报道将问题归因于模式分离：随着年龄增长，大脑区分相似经历的能力下降。 这一发现很重要，因为它把对老年记忆衰退的理解从被动的信息丢失，转向主动的记忆干扰过程。理解这一机制，有助于未来开发保持老年人记忆辨别能力的诊断工具和干预方法。 评论者指出该研究存在局限：样本仅 61 人，且几乎没有 30 到 50 岁之间的参与者，因此不应将年龄趋势解读为贯穿一生的持续衰退。此外，注意力指标与年龄或脑成像模式并没有关联，因此标题中的结论显得有些牵强。

hackernews · mdp2021 · 9月2日 12:59 · [社区讨论](https://news.ycombinator.com/item?id=49535548)

**背景**: 情景记忆依赖于海马体，模式分离使大脑能将相似经历存储为不同表征，而模式补全则是根据部分线索调取完整记忆。一般认为，衰老对模式分离的损害大于模式补全，因此相似事件容易相互混淆。表征相似性分析等神经影像技术常用于比较大脑对不同刺激的表征有多相似，帮助研究者量化这类效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7819938/">Pattern separation and pattern completion: Behaviorally ...</a></li>
<li><a href="https://link.springer.com/article/10.3758/s13421-020-01072-y">Pattern separation and pattern completion: Behaviorally ...</a></li>

</ul>
</details>

**社区讨论**: 评论者总体很感兴趣但保持谨慎。一位年长用户结合自己 25 年数码照片档案的回忆经历，表示确实存在记忆融合现象；另一位质疑这究竟是生理老化，还是大脑随时间积累了更多记忆所致。还有评论者指出样本量小、缺少中年组，另外有人联想到每次提取记忆都可能轻微改变记忆本身的观点。

**标签**: `#neuroscience`, `#memory`, `#aging`, `#research`, `#cognitive science`

---

<a id="item-18"></a>
## [Anthropic 更新 Claude 系统提示词，严格限制复现歌词](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) ⭐️ 6.0/10

Anthropic 最近将 Claude 系统提示词文档重组为按模型分页，并展示了 Fable 5.1 的更新版提示词。新提示词加入了一大段说明，要求 Claude 不得完整或部分复现歌词、诗歌以及书籍和文章中的段落内容。 这很重要，因为系统提示词直接决定了 Claude 如何处理歌词等受版权保护的内容，而 Anthropic 公开提示词的做法让外部观察者能够看到这些策略变化。它同时也表明，AI 公司正在把版权合规要求写进系统指令层，而不是只依赖单独的过滤机制。 新规则适用于完整或部分复现，包括最后一句、副歌或钩子（hook）、逐音记下的旋律，以及用户逐行粘贴并称为自己创作的歌词。Claude 一旦拒绝此类请求，会在本次对话中继续拒绝更窄或改写过的版本，而 1929 年以前首次发表的作品仍属允许范围。

rss · Simon Willison · 9月2日 14:16

**背景**: 系统提示词是设定 AI 助手身份、优先级和行为边界的指令层，用户提示词则负责提出具体的任务或问题。Anthropic 会公开发布 Claude.ai 和移动应用等消费级 Claude 产品的系统提示词，在其文档页面后加 .md 即可获取 Markdown 版本。这样一来，外界可以方便地比较不同历史版本的提示词，追踪 Claude 的行为变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pulsegeek.com/articles/what-is-a-system-prompt-in-ai-roles-boundaries-and-best-practices/">What Is a System Prompt in AI? - PulseGeek</a></li>
<li><a href="https://blog.promptlayer.com/system-prompt-vs-user-prompt-a-comprehensive-guide-for-ai-prompts/">System Prompt vs User Prompt in AI: What's the difference?</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#system prompts`, `#Anthropic`, `#copyright`

---

<a id="item-19"></a>
## [Reddit 用户公开 59.4 亿 TikTok 视频与 32.3 亿个人资料数据集](https://www.reddit.com/r/MachineLearning/comments/1w5h9se/i_scraped_594_billion_tiktok_videos_and_323/) ⭐️ 6.0/10

一位 Reddit 用户在 Hugging Face 上发布了包含 59.4 亿条 TikTok 视频和 32.3 亿个个人资料的数据集，名为 kuben-developer/tiktok-videos-4b。这些数据通过对 TikTok 移动应用进行逆向工程收集而来，并附带了教程以及部分收费的代码。 这可能是公开的最大规模社交媒体数据集之一，对推荐系统、内容分发和在线行为等研究具有潜在价值。但该数据集也引发了关于平台服务条款和用户隐私的法律与伦理问题，同时由于完整代码需要付费，帖子带有一定推广性质。 数据收集者表示 TikTok 暴露了 24 个无需账号即可访问的接口，但也警告这种访问方式可能违反 TikTok 的服务条款。数据集在 Hugging Face 上免费提供，但完整的抓取代码并非免费，需要支付一小笔费用。

reddit · r/MachineLearning · /u/DataShack · 9月2日 17:38

**背景**: Hugging Face 是一个供研究人员共享机器学习模型和数据集的平台与社区。TikTok 的数据通常通过官方开发者 API 获取，但一些开发者会对移动应用的私有接口进行逆向工程，以抓取大量公开内容。如此规模的数据集可用于推荐算法、内容审核和社会行为等研究，但这种抓取行为往往处于法律灰色地带。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face</a></li>
<li><a href="https://www.ibm.com/think/topics/hugging-face">What is Hugging Face? - IBM</a></li>
<li><a href="https://github.com/mangledbottles/Musically-API">GitHub - mangledbottles/Musically- API : TikTok Reverse Engineered ...</a></li>

</ul>
</details>

**标签**: `#TikTok`, `#dataset`, `#Hugging Face`, `#web scraping`, `#social media`

---

<a id="item-20"></a>
## [CABiNet 作者在 UAVid 上对比 YOLO26-sem 的评测](https://www.reddit.com/r/MachineLearning/comments/1w5cfv1/cabinet_icra_2021_vs_yolo26sem_on_uavid_accuracy/) ⭐️ 6.0/10

在 UAVid 数据集上，CABiNet 的 MobileNetV3-L 变体达到 67.14%的 mIoU，FP16 延迟仅 4.44ms，在准确率和速度上都优于 YOLO26x-sem（64.41% mIoU，13.09ms）。作者还开放了可复现的 PyTorch 仓库，并明确说明哪些评测设置是一致的、哪些训练配置是各模型特有的。 这一对比很重要，因为无人机与航拍场景中的实时语义分割需要同时兼顾高精度和低延迟。结果表明，2021 年专门设计的高效架构在它原本针对的数据集上仍能胜过 2026 年的通用大模型，而 YOLO26 的小型变体则在低延迟一端依然具有竞争力。 作者公开说明自己是 CABiNet 的原创第一作者，因此该对比并非出自中立第三方。评测在数据、类别加权、EMA 权重和单尺度协议上保持一致，而预训练、训练轮数、优化器、损失函数和数据增强等模型专属配置则被明确保留差异；在约 44 GFLOPs 的相近算力下，CABiNet-S 比 YOLO26s 高出 3.6 个 mIoU，而 CABiNet-L 比 YOLO26x 高出 2.7 个 mIoU，前向延迟约为后者的三分之一。

reddit · r/MachineLearning · /u/Naive-Explanation940 · 9月2日 14:46

**背景**: 语义分割是为图像中每个像素分配类别标签的任务，其实时版本主要面向机器人、无人机和自动驾驶车辆。CABiNet（ICRA 2021）是一种面向低延迟语义分割的双分支 CNN，将高分辨率空间分支与基于 MobileNetV3 的轻量上下文分支相结合。UAVid 是一个高分辨率航拍语义分割数据集，相较于街景数据集带来了尺度变化大等新挑战。YOLO26-sem 是 Ultralytics 发布的 2026 年 YOLO26 通用多任务模型家族中的语义分割变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ris.utwente.nl/ws/portalfiles/portal/268629120/CABiNet_Efficient_Context_Aggregation_Network_for_Low_Latency_Semantic_Segmentation.pdf">CABiNet: Efficient Context Aggregation Network for Low ...</a></li>
<li><a href="https://arxiv.org/abs/1810.10438">UAVid : A Semantic Segmentation Dataset for UAV Imagery</a></li>
<li><a href="https://huggingface.co/JBrightmanAI/yolo26n-sem">JBrightmanAI/ yolo 26 n- sem · Hugging Face</a></li>

</ul>
</details>

**标签**: `#semantic segmentation`, `#benchmark`, `#UAVid`, `#efficient deep learning`, `#real-time inference`

---
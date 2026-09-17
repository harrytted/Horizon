---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> 从 35 条内容中筛选出 20 条重要资讯。

---

1. [4B 模型生成的查询计划号称比 Postgres 快 81%](#item-1) ⭐️ 8.0/10
2. [小米发布 MiMo 2.6 实时后训练仪表盘](#item-2) ⭐️ 8.0/10
3. [新方法将三值 LLM 权重压缩至 1.48 比特](#item-3) ⭐️ 8.0/10
4. [黑客曝光 Flock 车牌识别摄像头的严重安全漏洞](#item-4) ⭐️ 8.0/10
5. [TMLR 约谈 10 篇拟退稿论文作者，多数无法解释自己的研究](#item-5) ⭐️ 8.0/10
6. [苹果发布 2nm A20 Pro 芯片，搭载于 iPhone 18 Pro](#item-6) ⭐️ 8.0/10
7. [新浪云 SAE 永久下线：420TB 早期 B 站视频源文件面临消失](#item-7) ⭐️ 8.0/10
8. [美光展示全球首款 512 GB DDR5 RDIMM，目标 2027 年量产](#item-8) ⭐️ 8.0/10
9. [华为将发布 Ascend 960 AI 芯片，挑战英伟达](#item-9) ⭐️ 8.0/10
10. [Anthropic 将 Claude Cowork 与聊天合并为统一通用智能体](#item-10) ⭐️ 7.0/10
11. [LARA：为冻结 LLM 打造可组合的轻量残差适配器](#item-11) ⭐️ 7.0/10
12. [苹果考虑借助英伟达技术重返服务器市场](#item-12) ⭐️ 7.0/10
13. [随笔主张小技巧很重要，引发 Hacker News 热议](#item-13) ⭐️ 6.0/10
14. [Dream-RSI 论文提出通过演化世界模型实现递归自我改进](#item-14) ⭐️ 6.0/10
15. [DeepMind 成立研究院，研究 AGI 的经济与社会影响](#item-15) ⭐️ 6.0/10
16. [Datasette 0.65.5 修复尾随换行符导致的权限绕过漏洞](#item-16) ⭐️ 6.0/10
17. [苏莱曼警告：不应赋予 AI 模型权利与福利地位](#item-17) ⭐️ 6.0/10
18. [字节火山引擎发布豆包 Doubao-Seed-2.1-pro 0915，Agent 交付更可靠](#item-18) ⭐️ 6.0/10
19. [微信 8.0.78 支持将聊天记录导出给 ChatGPT 和 Claude](#item-19) ⭐️ 6.0/10
20. [小米 MiMo-V2.6 启动大规模 RL 训练，细节将陆续开源](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [4B 模型生成的查询计划号称比 Postgres 快 81%](https://rohanbansal.com/qorl) ⭐️ 8.0/10

rohanbansal.com 上的一篇博客文章介绍了训练一个 40 亿参数（4B）模型来生成查询计划，作者声称其生成的计划比 Postgres 生成的计划快 81%。这篇文章在 Hacker News 上获得了 454 个赞同和 94 条评论，评论者关注的重点主要是基准测试的方法论，而非那个速度提升数字本身。 这展示了一种新思路：体量较小、可在本地运行的模型也能用于数据库查询优化，而这原本是由优化器内部手写的基于代价的启发式规则完成的任务。如果该方法可以泛化，可能会改变优化器的构建方式并降低针对特定工作负载调优的门槛，但评论界的反应也说明这类性能宣称面临多大的质疑。 评论者指出，该基准使用的是一个 8 GB、可完全放入内存的数据集，shared_buffers 被限制在远小于数据集的大小，缓存经过预热，只执行只读 SELECT 查询，除主键外没有任何二级索引或额外的列统计信息。这些条件使人难以判断该模型学到的计划在更大规模、更贴近现实的 OLTP 工作负载上是否仍能胜过 Postgres 的启发式优化器，同时也没有提供任何证据说明模型幻觉导致计划退化会在生产环境中造成何种风险。

hackernews · polyphilz · 9月16日 18:50 · [社区讨论](https://news.ycombinator.com/item?id=49731285)

**背景**: 查询计划是数据库为执行一条 SQL 查询而遵循的一组指令，由查询优化器生成，优化器通常依据表的统计信息和索引情况来估算代价。参数规模约 40 亿的语言模型（例如较小的 Gemma 系列）体量足够小，可以在笔记本或边缘设备上运行，因此把这类模型用作查询优化器才格外引人注目。基准测试的现实性（benchmark realism）在机器学习领域是一个反复被讨论的问题：只有当测试条件与生产环境的真实情况相近时，基准结果才有意义，而简单可控的环境又更便于复现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Query_plan">Query plan - Wikipedia</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview | Google AI for Developers</a></li>
<li><a href="https://labelstud.io/learningcenter/what-are-the-differences-between-synthetic-and-real-world-ai-benchmarks/">Synthetic vs Real-World AI Benchmarks: Key Differences | Label Studio</a></li>

</ul>
</details>

**社区讨论**: 整体情绪是怀疑但建设性的：评论者认为 81% 这个数字被内存中的 8 GB 数据集、受限的 shared_buffers、预热缓存、只读 SELECT 以及缺少二级索引和额外统计信息所夸大，很可能对特定条件过拟合。另一些人指出，查询计划构造是数学与算法密集型问题，若引入即时索引（just-in-time indexes）解空间会膨胀得更快，有时瓶颈恰恰是查询优化器本身，相比 AlphaGo 式的学习型启发式，用 LLM 属于比较粗糙的手段。还有多人提出实际运维噩梦：幻觉的优化器可能在生产中悄悄漏掉索引；也有人指出，大多数需要靠查询提示（hint）救场的场景，根源是统计信息不准，而非优化器本身太差。

**标签**: `#databases`, `#query-optimization`, `#LLM`, `#machine-learning`, `#benchmarking`

---

<a id="item-2"></a>
## [小米发布 MiMo 2.6 实时后训练仪表盘](https://mimo.xiaomi.com/rl/) ⭐️ 8.0/10

小米在其网站 mimo.xiaomi.com/rl/ 上发布了 MiMo 2.6 模型的实时后训练仪表盘，让公众可以看到正在进行中的后训练过程。此事在 Hacker News 上引发讨论，涉及该次运行已报告的 120 万美元成本、基准测试分数以及小米的开源 AI 策略。 大语言模型后训练的实时仪表盘非常少见，因此小米的这一举动罕见地展示了一家主要厂商如何训练和对齐前沿级模型。这可能会促使其他 AI 实验室公开更多训练细节，同时也会加剧关于开源 AI 经济性和竞争影响的争论。 社区成员指出，仪表盘显示截至目前总运行成本为 120 万美元，并希望小米分享更多基础设施细节，包括 MFU 指标。讨论中还提到 MiMo-V2.5-Pro 在 DeepSWE 1.1 上得分为 19%，并援引 Fable、Kimi K3 和 Astra 在最高努力设置下更高的得分作为对比。

hackernews · krackers · 9月16日 20:09 · [社区讨论](https://news.ycombinator.com/item?id=49732270)

**背景**: 小米的 MiMo 系列是该公司的 大语言模型产品线；小米已发布 MiMo-V2-Pro，并开源了 MiMo-V2.5-Pro，强调智能体能力、代码能力和长周期任务。后训练指的是初始预训练之后的阶段，例如监督微调、偏好优化和强化学习，这些阶段把基础模型转变为有用、安全且能执行任务的助手。训练过程通常不对外公开，因此实时仪表盘展示后训练进展在少数开放研究之外并不常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-5-pro/">MiMo-V2.5-Pro | Xiaomi</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-training_of_large_language_models">Post-training of large language models</a></li>

</ul>
</details>

**社区讨论**: 评论者整体态度积极：一位软件工程师表示 MiMo-V2.5 的投资回报率极佳，在极低成本下接近 Anthropic 模型的质量，只是偶尔会出现幻觉循环。其他人则质疑 120 万美元的运行成本以及仪表盘缺少 MFU 细节，同时称赞其透明度，并争论开源 AI 是否对 OpenAI 和 Anthropic 构成威胁。还有一条基准对比指出，MiMo-V2.5-Pro 在 DeepSWE 1.1 上得分为 19%，而 Fable、Kimi K3 和 Astra 在最高努力设置下得分高得多。

**标签**: `#AI/ML`, `#LLM`, `#Post-training`, `#Xiaomi MiMo`, `#Open Source AI`

---

<a id="item-3"></a>
## [新方法将三值 LLM 权重压缩至 1.48 比特](https://arxiv.org/abs/2609.16338) ⭐️ 8.0/10

一种新的量化技术将三值 LLM 权重的存储压缩到约 1.48 比特/权重，突破了此前公认的 1.58 比特下限，其核心思路是利用实际量化权重中约有 51%为零这一统计特性。该研究主要面向嵌入式推理与定制芯片（ASIC），而非标准 GPU 部署场景。 如果三值模型最终被固化到专用硬件中，把权重压到 log2(3)以下就能进一步降低内存占用和功耗，让大模型真正可以移植到端侧和嵌入式设备。这也说明在 GPU 主导的浮点计算范式之外，极端量化仍是学术界持续关注的方向。 该收益主要体现在模型存储格式上：推理时压缩后的权重仍需还原为传统的三值表示（约每字节 5 个 trit），因此好处主要在于文件大小和内存带宽，而非算术运算本身。社区专家也提醒，在这一比特区间三值量化未必是最优选择，向量量化和基于网格（trellis）的训练后量化方法往往表现更好。

hackernews · matt_d · 9月16日 20:59 · [社区讨论](https://news.ycombinator.com/item?id=49732931)

**背景**: 三值 LLM 把每个权重存为-1、0 或+1 三个值之一，理论上每个参数只需 log2(3)≈1.58 比特，这正是微软 BitNet b1.58 名称的由来——它证明 1.58 比特模型能达到 16 比特基线的水平。由于乘-1、0 或+1 极为简单，这类模型可以省去绝大多数浮点乘法，因此对 CPU、FPGA 和 ASIC 特别有吸引力。训练后量化（PTQ）是对已训练好的模型做压缩，而量化感知训练（QAT）则在训练时就让模型“知道”自己会被量化，两者最终能达到的质量差异很大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/1.58-bit_large_language_model">1 . 58 - bit large language model - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/bitnet-b1-58">BitNet b 1 . 58 : Ternary Quantization for LLMs</a></li>
<li><a href="https://arxiv.org/html/2502.16473">TerEffic: Highly Efficient Ternary LLM Inference on FPGA</a></li>

</ul>
</details>

**社区讨论**: 讨论反应不一但颇具深度：有评论者认为这是个巧妙技巧，并预测一旦三值模型固化到定制硅片中会极其高效；也有人直接断言在这一区间三值量化没有意义，认为向量量化和网格方法在训练后量化上更优。还有人强调其在嵌入式和可移植性上的价值以及与 ASIC 推理的契合度，并有一位评论者指出压缩只作用于存储文件格式，因为权重在内存中必须被还原。有评论引用文献称，若采用量化感知训练，三值模型只需多约 30%的权重就能达到相当的质量。

**标签**: `#LLM quantization`, `#ternary LLMs`, `#model compression`, `#AI hardware`, `#embedded AI`

---

<a id="item-4"></a>
## [黑客曝光 Flock 车牌识别摄像头的严重安全漏洞](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

安全研究人员披露，Flock Safety 的车牌识别摄像头存在硬编码 API 凭证以及其他“天生不安全”的设计缺陷，同时 Flock 的漏洞披露政策被指意在阻挠真正的安全报告。Micah Lee 撰写的分析指出，攻击者可利用一个硬编码的 API key 去请求以明文存储的凭证，而这些凭证看起来可以访问 Flock 的后端服务器。 Flock 摄像头已部署在美国数千个城市和社区，因此任何允许本地物理接触或凭证滥用的漏洞都会威胁到大规模采集的车辆位置数据隐私。此案还凸显出监控厂商的安全能力直接影响公众信任，也加剧了社会对自动车牌识别系统（ALPR）部署的反弹情绪。 泄露的秘密并非硬编码的管理员密码，而是一个 API key，而且目前尚不清楚攻击者以摄像头身份成功认证后究竟能做什么；Flock 的漏洞披露政策明确将需要与设备交互或下载设备数据的案例排除在外。社区分析进一步指出，设备上的数据似乎未得到充分加密，使得物理接触成为一条可行的攻击路径。

hackernews · driverdan · 9月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: Flock Safety 生产自动车牌识别摄像头（ALPR）：这类由 AI 驱动的摄像头会拍摄并记录每一辆经过车辆的号牌、车型与位置，数据还会与失窃车辆、AMBER 警报等监控名单交叉比对。硬编码凭证（在漏洞分类中被列为 CWE-798）是一种经典缺陷，指密码或密钥被写死在固件中，任何能接触设备或固件的人都能将其提取出来。漏洞披露政策（VDP）是厂商邀请研究人员报告漏洞的正式渠道，而过于苛刻的政策实际上会起到抑制披露的作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://trafficvision.live/blog/flock-cameras">Flock Cameras : What They Are & Can You Watch... | TrafficVision.Live</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/798.html">CWE - CWE-798: Use of Hard - coded Credentials (4.20)</a></li>
<li><a href="https://www.bugcrowd.com/blog/vulnerability-disclosure-policy-what-is-it-why-is-it-important/">Vulnerability Disclosure Policy : What is It & Why is it... | @Bugcrowd</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论几乎一边倒地批评，有人称硬编码凭证是“彻底无能”的表现，但指出此次涉及的是 API key 而非管理员密码。也有人认为 Flock 的漏洞披露政策主要是为了营造“负责任的”安全形象，批评其出于“缩短上市时间”的心态而忽视了物理接触这一威胁模型，并因设备数据疑似未加密而表示对 Flock 毫无信任。

**标签**: `#security`, `#surveillance`, `#privacy`, `#IoT`, `#vulnerability-disclosure`

---

<a id="item-5"></a>
## [TMLR 约谈 10 篇拟退稿论文作者，多数无法解释自己的研究](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/) ⭐️ 8.0/10

TMLR（Transactions on Machine Learning Research）的联合主编亲自联系了 10 篇被列入直接拒稿（desk rejection）名单的投稿作者，并就其论文内容逐一进行面谈。十篇论文中，一篇的作者主动撤稿，一篇称因其他事务无法参加，一篇约好会议却未出席，三篇作者无法回答关于论文的基本问题，三篇能谈高层思路但在技术细节上卡壳，只有一篇作者完整回答了所有问题——而主编仍在该论文中发现了一处重大缺陷。 这是少见的直接证据，说明投向机器学习领域会议和期刊的稿件中可能有很大一部分由大模型代写或由他人代笔，而同行评审的核心前提——署名作者确实完成了并理解这项研究——正因此被动摇。若此类投稿持续规模化，期刊与会议将面临更高的审稿成本、更难落实的学术诚信治理，以及公众对已发表机器学习研究成果信任度的下降。 这次核查采取的是一种少见、以人为中心的干预方式：没有依赖可靠性长期备受争议的 AI 文本检测器，而是由联合主编进行实时面谈，要求作者解释自己的投稿。证据规模较小且属个案性质——仅有 10 篇论文，且全部来自同一期刊的拟直接拒稿名单——因此结果只提示可能存在某种普遍模式，并不能在统计上代表整个机器学习投稿群体。

reddit · r/MachineLearning · /u/hihey54 · 9月16日 23:20

**背景**: 所谓“直接拒稿”（desk rejection），是指期刊在把论文送交同行评审之前就将其退回，通常是因为选题超出范围、内容不完整或明显达不到该刊的发表门槛。TMLR 是一本开放获取的机器学习期刊，其评审过程在 OpenReview 上公开进行，也可以在不送审的情况下直接退稿。自能力强大的大语言模型普及以来，机器学习领域的会议期刊与学术出版机构一直在争论如何识别和遏制完全由模型生成或由他人代笔的论文，因此像这次这样核查作者本人是否理解论文的做法成为了热点话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scientific-publishing.webshop.elsevier.com/publication-process/paper-rejection-common-reasons/">Paper Rejection: Common Reasons | Elsevier Language Services</a></li>
<li><a href="https://authorservices.taylorandfrancis.com/blog/get-published/5-reasons-for-desk-rejection-and-how-to-avoid-them/">5 top reasons for desk rejection – and how to avoid them - Author Services</a></li>
<li><a href="https://dblp.org/db/journals/index.html?prefix=M">dblp: Browse Journals</a></li>

</ul>
</details>

**标签**: `#peer-review`, `#research-integrity`, `#LLM-generated-content`, `#academic-publishing`, `#TMLR`

---

<a id="item-6"></a>
## [苹果发布 2nm A20 Pro 芯片，搭载于 iPhone 18 Pro](https://www.bilibili.com/video/BV1oZeA6fERD) ⭐️ 8.0/10

苹果正式发布首款 2nm 旗舰手机芯片 A20 Pro，并将搭载于 iPhone 18 Pro 系列。该芯片集成 6 核 CPU（超核提速 20%）、7 核 GPU（提速 40%）、双 16 核神经网络引擎，内存带宽较 A19 Pro 提升 50%，苹果称其为「所有智能手机中速度最快」。同时苹果还发布了自研 C2 调制解调器和首款定制 N1 无线芯片，支持 Wi-Fi 7 与蓝牙 6。 这标志着手机行业正式迈入 2nm 制程节点，也体现苹果在连接芯片上的持续垂直整合——用自研 C2 替代第三方基带。这抬高了基于竞品 2nm 平台的安卓旗舰的竞争门槛，并可能重新定义下一代智能手机在性能与能效上的预期。 A20 Pro 采用借鉴 M 系列芯片的新封装设计，并叠加 3 倍面积的 VC 均热板，使持续性能较上代最多提升 40%。自研 C2 调制解调器据称上传提速 50%、功耗降低 15%，不过持续性能数据在很大程度上仍取决于整机散热设计和真实负载表现。

telegram · zaihuapd · 9月16日 13:24

**背景**: 「2nm」是继 3nm 之后的半导体制造世代名称，它只是一个营销代号，与任何实际物理尺寸并无直接对应关系；IBM 预计该节点芯片相比 7nm 可带来约 45% 的性能提升，或减少 75% 的能耗。苹果 A 系列芯片用于 iPhone，而 C 系列调制解调器是苹果用自研设计替代高通基带芯片的努力。VC 均热板是一种真空密封的金属腔体，通过两相散热把热量铺展到更大面积，从而帮助芯片更长时间维持高频率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://research.ibm.com/projects/advanced-logic-technology-at-2nm-node">Advanced logic technology at 2 nm node - IBM Research</a></li>
<li><a href="https://theaterfi.re/post/3653931">iPhone 18 Pro Models and iPhone Duo Feature Apple 's New C 2 Modem</a></li>

</ul>
</details>

**标签**: `#Apple`, `#semiconductor`, `#2nm process`, `#mobile chips`, `#hardware`

---

<a id="item-7"></a>
## [新浪云 SAE 永久下线：420TB 早期 B 站视频源文件面临消失](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

国内首个 PaaS 云计算平台新浪云 SAE 将于 2026 年 9 月 16 日 24 时正式永久下线，所有用户数据将被彻底删除。目前仍有约 420TB 早期 B 站视频源文件存放在新浪云的 S3 存储桶中，Archive Team 发起的分布式归档项目已累计抢救约 680TB 数据，完成度达到 96.26%。 这次下线不仅宣告国内最早的 PaaS 服务落幕，也让一批早期中国视频互联网历史面临消失风险，因为 B 站早期视频源文件曾大量依赖新浪云存储。它同时凸显出：当商业云服务退役并直接删除存储数据时，志愿者主导的数字保存行动往往成为最后一道防线。 该项目是 Archive Team 组织的分布式众包抓取，正在与下线期限赛跑，所公布的数字（已完成 96.26%、约 680TB 已抢救、约 420TB 仍待处理）意味着可能有一部分内容来不及保全。这些数据存放在 S3 风格的对象存储桶中，一旦存储桶被删除，除非存在独立副本，否则没有任何内置的恢复途径。

telegram · zaihuapd · 9月16日 15:00

**背景**: PaaS（平台即服务）让开发者无需自行管理服务器即可部署和运行应用，2009 年上线的新浪云 SAE 是国内首个此类平台，凭借低成本、免运维吸引了大量开发者。S3 存储桶是 Amazon S3 风格对象存储中用于存放对象的容器，这种接口被众多云厂商广泛仿效，用来存放备份、媒体、归档等任意文件。Archive Team 是由 Jason Scott 等人于 2009 年共同发起的志愿者组织，专门从濒临关停的在线服务中复制内容，此前抢救过 GeoCities、Yahoo! Video、Google Video、Friendster 和 SoundCloud 等，成果通常存入 Wayback Machine。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team</a></li>
<li><a href="https://en.wikipedia.org/wiki/S3_bucket">S3 bucket</a></li>
<li><a href="https://www.crunchbase.com/organization/sina-app-engine">Sina App Engine - Crunchbase Company Profile & Funding</a></li>

</ul>
</details>

**标签**: `#cloud-computing`, `#digital-preservation`, `#paas`, `#bilibili`, `#internet-history`

---

<a id="item-8"></a>
## [美光展示全球首款 512 GB DDR5 RDIMM，目标 2027 年量产](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 8.0/10

美光称已展示全球首款面向服务器的 512 GB DDR5 RDIMM 模组，速率最高可达 9200 MT/s，并采用 3D 堆叠 DRAM 芯片堆叠而成。该公司表示 AMD 与 Intel 正在为未来的服务器平台对该模组进行验证，预计 2027 年具备量产条件。 单根模组容量提升至四倍后，一台使用 24 根模组的服务器可达到 12 TB 内存，从而直接缓解大型数据库、虚拟化以及 AI 推理等数据中心负载所面临的“内存容量墙”。美光还宣称其在功耗上占优，这意味着该方案指向的是单位容量更省电的更高密度服务器，而不仅仅是增加 DIMM 插槽数量。 美光称单根 512 GB 模组功耗为 16 W，而四根 128 GB 模组合计为 44.2 W，降幅超过 60%。需要注意的是时间点：量产条件预计要到 2027 年才具备，且该模组仍依赖 AMD 和 Intel 的平台验证，因此这更像是一次路线图级别的发布，而非可立即出货的产品。

telegram · zaihuapd · 9月16日 16:15

**背景**: DDR5 是当前服务器与 PC 主存所采用的一代标准，而 RDIMM（寄存式 DIMM）是面向服务器的变体：在 DRAM 与内存控制器之间加入一颗寄存器芯片来重新驱动信号，使系统能够比使用非寄存内存时更稳定地承载更多模组。3D 堆叠——将多颗 DRAM 芯片垂直键合并通过硅通孔（TSV）互连——正是高带宽内存（HBM）所普及的一类技术，HBM 通过堆叠 DRAM 芯片服务于 GPU 和 AI 加速器；美光现在把这一思路用到了传统插槽式服务器内存上。单根模组的容量历来受限于一块电路板上可放置的 DRAM 芯片数量，这正是堆叠技术对实现单根 512 GB RDIMM 至关重要的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RDIMM">RDIMM</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#Micron`, `#server hardware`, `#memory`, `#3D stacking`

---

<a id="item-9"></a>
## [华为将发布 Ascend 960 AI 芯片，挑战英伟达](https://www.bloomberg.com/news/articles/2026-09-16/huawei-set-to-unveil-china-s-best-answer-to-nvidia-ai-chip-reign) ⭐️ 8.0/10

华为将于 9 月 17 日在上海年度峰会上发布新一代 Ascend 960 AI 芯片，计划于 2027 年商用；监事会主席郭平表示“我们正通过芯片架构创新缩小差距”，目标是让 Ascend 芯片能够运行所有 AI 模型。与此同时，DeepSeek 计划部署至少 16 万颗 Ascend 950DT 芯片，华为还在拓展马来西亚、埃及等海外市场。 这是华为迄今最直接地把 Ascend 定位为英伟达大规模 AI 训练与推理可行替代方案的一次尝试，而美国出口管制仍在限制中国实验室可采购的硬件。若 DeepSeek 等主要模型厂商按报道的规模转向 Ascend，这将意味着中国 AI 基础设施供应链的真正转变，而非纸面路线图，并会波及英伟达的在华收入以及全球 AI 算力定价。 据华为介绍，Ascend 960 的算力、内存访问带宽、内存容量和互连端口数量大致是 Ascend 950 的两倍，可显著提升训练与推理性能；但华为自身的路线图显示，2026 年的 Ascend 950PR/950DT 总算力仍低于 2025 年的 Ascend 910C，因此 2027 年第四季度的 960 才是其首款号称超越英伟达 H200 的芯片。Ascend 950DT 计划 2026 年第四季度上市并采用华为自研的类 HBM 内存，受产能限制其价格已上涨约 60% 至 25 万元人民币以上；当前旗舰 Ascend 950 的规格为 1.56 PFLOPS FP4 算力、112 GB HiBL 内存（1.4 TB/s 带宽）、600 W TDP。

telegram · zaihuapd · 9月17日 03:20

**背景**: 华为的 Ascend 系列基于自研的达芬奇架构，配合 CANN 软件栈和 SuperPoD 互连技术，构成了中国本土替代英伟达 CUDA 生态的核心体系。美国出口管制禁止英伟达向中国客户出售其顶级加速器，促使国内买家转向华为，而英伟达面向中国的降规格产品本身也面临监管不确定性。DeepSeek 是一家总部位于杭州的 AI 公司，以开源权重的大语言模型著称，其采购决策具有超额影响力，因为它被广泛视为中国实验室算力布局的风向标。华为的 Ascend 路线图覆盖 950、960 及后续多代产品，因此此类发布属于产品规划，而非已经量产出货的硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.straitstimes.com/business/huawei-set-to-unveil-chinas-best-answer-to-nvidia-ai-chip-reign">Huawei set to unveil China’s best answer to Nvidia AI chip reign</a></li>
<li><a href="https://www.igorslab.de/en/hbm-shortage-chinas-ai-chips-huawei-ascend-950dt-over-250000-yuan/">HBM Shortage: Huawei Ascend 950 DT Above 250,000 Yuan</a></li>
<li><a href="https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/">Huawei Ascend 950 vs NVIDIA B300 and B200 for... | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Huawei`, `#Nvidia`, `#AI infrastructure`, `#China tech`

---

<a id="item-10"></a>
## [Anthropic 将 Claude Cowork 与聊天合并为统一通用智能体](https://simonwillison.net/2026/Sep/16/one-claude/) ⭐️ 7.0/10

Anthropic 宣布将 Claude Cowork 与 Claude 聊天合并为单一的 Claude，未来几周内率先向 Pro 和 Max 订阅用户在网页端、桌面端和移动端推送。新的统一产品还加入了演示文稿与文档生成能力，可在同一窗口内生成幻灯片（支持导出为 PDF 或 PPT）以及可协作编辑的文档。 这次合并让 Claude 从一个聊天助手加一个独立智能体工具，转变为一个统一的通用智能体，减少了 Cowork、Claude 与 Claude Code 之间令人困惑的功能重叠。这也呼应了 OpenAI 近期将其 Codex 桌面应用并入 ChatGPT 的做法，说明整个行业正在从多个专用产品收敛到单一的智能体入口。 统一界面会在同一个窗口内自动路由请求，用户不再需要在“聊天”和“多步任务执行”之间做选择，而且即使用户关掉笔记本，Claude 也能继续推进任务。推送是分阶段的：网页端、桌面端和移动端的 Pro 与 Max 订阅用户优先获得，免费版和团队版随后跟进。

rss · Simon Willison · 9月16日 18:09

**背景**: Claude Cowork 是 Anthropic 面向非开发者推出的智能体产品，可以跨本地文件和网络执行任务，例如在桌面端启动任务、用手机查看进度，最后交付一份做好的演示文稿、文档或表格。相比之下，Claude Code 是 Anthropic 面向开发者的命令行与 IDE 编程智能体。所谓“通用智能体”（general agent），指的是能够把一个宽泛目标拆解成多个步骤，并跨工具、跨终端自主执行的 AI 系统，而不是只局限于某一项狭窄任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/cowork">Claude Cowork | Claude by Anthropic</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.guild.ai/glossary/general-ai-agent">General AI Agent : Definition , How It Works & Use Cases | Guild. ai</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI agents`, `#product update`, `#Simon Willison`

---

<a id="item-11"></a>
## [LARA：为冻结 LLM 打造可组合的轻量残差适配器](https://www.reddit.com/r/MachineLearning/comments/1whx9tr/lara_small_composable_behaviours_for_frozen_llms_p/) ⭐️ 7.0/10

开发者发布了 LARA（Lightweight Additive Residual Adaptation）研究项目及其配套的小型 PyTorch 库，其做法是在冻结的语言模型的部分层上训练低秩残差适配器，而不是修改模型本身的原权重。该发布包含 Mixture of Behaviors（MoBs）演示：多个独立训练的行为可以共享同一个冻结模型，并由软路由器逐 token 选择或组合它们；此外还提供了与 LoRA 的对比，以及在海明威、菲茨杰拉德和格特鲁德·斯坦文本上训练出的写作风格行为。 它把后训练推向模块化：与其为编程、数学、医疗和摘要分别维护四个适配后的模型，不如让同一个冻结底座承载多个小型行为，在推理时按需加载、移除、混合或路由。如果这一思路成立，就能简化多能力服务的部署，并让行为组合成为推理时的选择，而非训练时就锁定的结果。 这些适配器是插入到特定层的低秩加性残差，因此底座权重保持不变，每个行为都足够小，可以单独存储。MoBs 演示使用的软路由器是逐 token 工作的，仓库提供了训练代码、示例和复现说明；不过作者坦言 LARA 仍是一个进行中的研究项目，而非成熟产品。

reddit · r/MachineLearning · /u/kertara · 9月16日 13:28

**背景**: LoRA 等参数高效微调（PEFT）方法通过只学习少量额外参数，避免重新训练大模型的全部权重；LoRA 的做法是给已有权重矩阵加上低秩更新矩阵，而残差适配器（最早在计算机视觉迁移学习中流行）则是在某一层的输出上叠加一个学习到的向量。混合专家（MoE）式的门控则用一个学习到的路由器对多个专门子网络进行加权或选择。LARA 把这两类思路结合起来：小型残差适配器充当专家，软路由器决定每个生成 token 由哪些行为参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vitalab.github.io/article/2019/01/23/resAdaptorModules.html">Learning multiple visual domains with residual adapters</a></li>
<li><a href="https://www.emergentmind.com/topics/resadapt">ResAdapt: Efficient Residual Adaptation</a></li>
<li><a href="https://www.isca-archive.org/interspeech_2024/huo24_interspeech.pdf">AdaRA: Adaptive Rank Allocation of Residual Adapters for Speech</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Parameter-Efficient Fine-Tuning`, `#Adapters`, `#Modularity`, `#PyTorch`

---

<a id="item-12"></a>
## [苹果考虑借助英伟达技术重返服务器市场](https://www.reuters.com/technology/apple-considers-nvidia-tech-return-server-market-information-reports-2026-09-16/) ⭐️ 7.0/10

据 The Information 报道（路透社跟进），苹果正考虑重返企业服务器市场，推出搭载自研 M8 Ultra 芯片的 AI 服务器，并提供双芯片和四芯片两种版本。该产品面向 AI 开发者、企业及政府客户，可能采用英伟达的 NVLink Fusion 互联技术，预计最早于 2029 年上市。 这将是苹果自 2011 年停产 Xserve 以来首次推出专用服务器硬件，意味着它重新进军目前由英伟达体系主导的企业级 AI 基础设施市场，属于重大战略转向。如果苹果真的采用 NVLink Fusion，还将意味着两家公司近二十年的紧张关系出现缓和，并可能改变 AI 数据中心市场的厂商格局。 该项目仍处于早期阶段，明确存在被取消的风险，苹果也可能最终放弃使用英伟达技术。值得注意的是，M8 Ultra 比苹果目前最强的 M5 Ultra 芯片还要领先数代，而 M5 Ultra 仅用于 Mac Studio，且需要约两磅重的散热系统，因此苹果必须设计出能塞进 1U 或 2U 机架式机箱的散热方案。

telegram · zaihuapd · 9月17日 02:40

**背景**: 苹果曾在 2002 年至 2011 年间销售机架式 Xserve 服务器，随后停产并由 Mac Pro Server 和 Mac Mini Server 取代。英伟达在 Computex 上发布的 NVLink Fusion 是一种互联方案，它把 GPU 与网络解耦，让亚马逊 Trainium 之类的自研芯片能够原生接入英伟达的网络栈，Lightmatter 等厂商也已加入提供光子互联。苹果自研的 M 系列芯片则通过 UltraFusion 扩展，例如 M5 Ultra 就是将两颗双裸片 M5 Max 连接成四裸片结构，裸片间带宽超过 4.4TB/s。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/09/16/apple-planning-to-sell-ai-servers-powered-by-m8-ultra-chips-says-report/">Apple planning to sell AI servers powered by M 8 Ultra chips , says...</a></li>
<li><a href="https://www.macworld.com/article/3237195/apple-may-revive-xserve-for-the-ai-market.html">Apple may revive Xserve for the AI market | Macworld</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Xserve">Apple Xserve</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Nvidia`, `#AI servers`, `#NVLink Fusion`, `#server market`

---

<a id="item-13"></a>
## [随笔主张小技巧很重要，引发 Hacker News 热议](https://will-keleher.com/posts/small-programming-tricks-matter/) ⭐️ 6.0/10

Will Keleher 在其个人博客上发表了一篇题为 "Small programming tricks matter" 的随笔，主张那些看似微不足道、学习成本极低的编程与命令行小技巧，长期积累下来能带来远超预期的效率收益。该文在 Hacker News 上获得 444 分并引来 199 条评论，读者们在评论区互相分享各自的命令行、SQL 与工作流小技巧。 这篇文章强化了软件工程中一个普遍被感知却很少被正式总结的观点：开发者的生产力往往来自几十个单独看毫不起眼的小习惯，而非某一个工具或框架。它在 Hacker News 上的高热度也说明，诸如 shell 快捷键、性能剖析命令、目录跳转这类实战手艺，仍是开发者乐于交流与讨论的话题。 这是一篇个人随笔，而非新工具发布或基准测试结果，因此其价值主要体现在经验层面，内容属于渐进式补充而非全新突破。相应地，Hacker News 的讨论串也以实用技巧为主——例如使用 `perf` 性能剖析工具、更快的目录跳转方式以及一本工具书的推荐——而非深入的技术辩论。

hackernews · signa11 · 9月16日 15:56 · [社区讨论](https://news.ycombinator.com/item?id=49729000)

**背景**: Hacker News 是由 Y Combinator 运营的知名科技新闻与讨论社区，一篇帖子若能拿到数百分，通常意味着它在开发者群体中引起了广泛共鸣。这里所说的“小技巧”指的是 shell 一行命令、键盘快捷键、SQL 惯用写法以及命令行工具等，资深程序员往往需要多年才能在日常工作中零散习得。讨论中提到的相关工具包括 Linux 内核自带的性能剖析命令 `perf`，以及 zoxide——一个“更聪明的 cd”，它会记录你访问过的目录，让你用部分名称就能直接跳转过去。

**社区讨论**: 评论者总体上认可文章主题，但在定位上存在分歧：kccqzy 认为，把 AI 智能体设为逐条手动批准模式、并仔细阅读它执行的每条命令，能学到更多技巧，他还举例说 Claude Opus 曾以自己意想不到的方式使用 `perf`；ozim 则反驳称这些属于电脑使用或命令行技巧而非编程技巧，并感叹大多数人使用电脑的方式极其低效。其他人则分享了具体的工具经验，例如一个用于精确跳回上层目录的 gist（并提醒 zoxide 只会记录真正 `cd` 进去过的目录），以及推荐 O'Reilly 的经典著作《Unix Power Tools》。

**标签**: `#programming`, `#developer-productivity`, `#command-line`, `#hacker-news`, `#software-engineering`

---

<a id="item-14"></a>
## [Dream-RSI 论文提出通过演化世界模型实现递归自我改进](https://arxiv.org/abs/2609.14858) ⭐️ 6.0/10

一篇题为《Dream-RSI: Recursive Self-Improvement through Evolving Worlds》的 arXiv 论文（由 Tong Zheng 及另外 16 位作者合著）提出了一种方法，将学习到的世界模型与迭代式的、由智能体驱动的搜索结合起来，使智能体能够在“不断演化的世界”中反复自我改进。该工作被发到 Hacker News 上讨论（188 分、49 条评论），其优化思路获得肯定，但将其称为递归自我改进的说法遭到大量质疑。 递归自我改进（RSI）是 AGI“智能爆炸”叙事的核心前提，也是 AI 安全领域的重要担忧，因此任何声称在这一点上取得进展的论文都会受到格外严格的审视。如果这类多智能体自我精炼循环确实能在训练中带来持续累积的收益，它们既可能影响实际的强化学习流程，也会影响关于如何治理自我改进系统的更广泛讨论。 评论者指出，论文中用于离策略评估的“回放模拟器”是一种避免昂贵环境 rollout 的巧妙做法；也有人提问：随着搜索空间扩大，该方法如何防止策略对已经发现的搜索分支过拟合、从而变得陈旧僵化。该论文明确建立在 Danijar Hafner 的 Dreamer 系列工作之上，这条脉络始于 2019 年的论文 arXiv:1912.01603，此后不断迭代。

hackernews · bananaflag · 9月16日 13:44 · [社区讨论](https://news.ycombinator.com/item?id=49726955)

**背景**: 递归自我改进（RSI）是一种假想过程：AI 系统反复改写并改进自身代码，可能触发“智能爆炸”并最终走向超级智能；但迄今为止，没有任何尝试显示出这种爆炸的迹象，而且由于这类系统可能超出人类的理解与控制，该概念一直是伦理与安全担忧的核心。相比之下，世界模型是智能体学习到的环境内部模型，使智能体能够在“想象出来的经验”上做规划与训练，而不必依赖昂贵的真实交互——这一思路因 Ha 与 Schmidhuber 2018 年的《World Models》论文以及 Hafner 的 Dreamer 智能体而广为人知。Dream-RSI 正处于这两种思想的交汇点上：让智能体同时改进自身与其模拟出的世界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.14858">Dream - RSI : Recursive Self-Improvement through Evolving Worlds</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://world-models.io/en/world-models-reinforcement-learning/">World Models & Reinforcement Learning | world - models .io</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏向怀疑：最集中的批评是认为把它叫作“RSI”具有误导性，因为它看起来更像是对现有训练方法的一种不错的优化，而不是一个能够永远自我改进的系统。评论者还追溯了它与 Hafner 的 Dreamer 工作的渊源，并推荐了较易理解的 TalkRL 播客节目；有人发问为什么似乎没人担心递归自我改进可能带来危险，另有人提出技术性担忧：随着搜索空间扩大，策略可能对已发现的分支过拟合。

**标签**: `#AI/ML`, `#recursive self-improvement`, `#reinforcement learning`, `#world models`, `#AI safety`

---

<a id="item-15"></a>
## [DeepMind 成立研究院，研究 AGI 的经济与社会影响](https://institute.deepmind.com/) ⭐️ 6.0/10

DeepMind 正式推出「DeepMind Institute（DeepMind 研究院）」，这是一个面向政策议题的机构，发布关于通用人工智能（AGI）及其对人类影响的跨学科研究，其中也包括 AI 对经济冲击的分析。其首批内容包含一篇经济政策文章，勾勒了 AI 影响的不同情景，并提出扩大失业保险、提高劳动所得税抵免（EITC）、以及让公众分享 AI 利润等政策建议。 一家处在 AGI 前沿的实验室直接提出政策方案，可能影响政府、监管机构与公众如何界定 AI 的经济风险及相应的安全措施。这也引发一个疑问：正在研发 AGI 的公司，能否可信地为其研究可能造成的冲击设计应对政策。 据讨论，该经济文章设定了从轻度到重大冲击的三种情景：轻度冲击下的政策较为稳妥（失业保险、EITC），重大冲击下则强调让公众持有 AI 利润的一部分。文章还提出用「AI 评估器」来排序和衡量政策的有效性，但一些评论者认为其细节偏薄，且过度依附于 AGI 叙事。

hackernews · vertigoruntime · 9月16日 14:32 · [社区讨论](https://news.ycombinator.com/item?id=49727659)

**背景**: DeepMind 是 Google 旗下的 AI 研究实验室，以 AlphaGo、AlphaFold 以及 Gemini 系列模型闻名，长期也是预警先进 AI 风险的主要声音之一。「AGI（通用人工智能）」指的是假设中具备人类大脑全部认知能力的系统，而许多研究者认为距离这一门槛仍很遥远。与之相关的 AI 安全领域涵盖对齐、监控与鲁棒性研究，在 2023 年生成式 AI 快速进展后进入主流视野，同年举行的 AI 安全峰会也促使美国和英国分别成立了本国的 AI 安全研究所。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://institute.deepmind.com/">DeepMind Institute</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://digg.com/tech/kkgfus11">DeepMind launches institute to study AGI's societal impact · Digg</a></li>

</ul>
</details>

**社区讨论**: 评论意见分歧明显：有人称赞该经济政策文章思路合理、结构清晰，也有人认为 AGI 的叙事属于炒作，并把该机构形容为意在引导政策讨论的公司「内部智库」。讨论中还反复出现对当日大量热门链接来自同一个仅注册 11 天的 Hacker News 账号的质疑，另有用户打趣该网站字体灰度过低、难以阅读。

**标签**: `#AI policy`, `#AGI`, `#DeepMind`, `#economics`, `#AI safety`

---

<a id="item-16"></a>
## [Datasette 0.65.5 修复尾随换行符导致的权限绕过漏洞](https://simonwillison.net/2026/Sep/16/datasette-2/) ⭐️ 6.0/10

Datasette 0.65.5 是一个安全补丁版本，修复了一个权限绕过问题：在请求的表名后附加一个尾随换行符，就能绕过表级权限限制，从而暴露本应私有的数据行。该漏洞由安全研究员 dpfkdlemtp 报告，编号为 GitHub 安全公告 GHSA-h547-rmjf-5m2m。 任何依赖表级权限来保护私有数据的 Datasette 实例都应立即升级，因为该漏洞允许未授权读取受保护的数据行。它也再次说明了一类反复出现的 Web 安全漏洞：看似无害的输入规范化差异，可能让攻击者绕过访问控制检查。 该修复范围很窄，仅以补丁版本形式发布，针对的是请求表名中尾随换行符这一具体情形，而非更广泛的权限逻辑。值得注意的是，Datasette 的主线开发已推进到 1.0 alpha 系列，因此使用 1.0a 版本的管理员应另行确认自己是否受影响。

rss · Simon Willison · 9月16日 23:51

**背景**: Datasette 是 Simon Willison 开发的开源工具，可将 SQLite 数据库以交互式网站的形式浏览和发布，常被用于公开数据集。它的权限系统允许运营者限制对特定表的访问，因此一旦出现绕过，本应私有的数据就可能被任何能访问该实例的人读取。此处的问题属于输入处理类漏洞：带尾随换行符的表名，在权限检查代码和实际取数代码中被当作不同的名称处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette : An open source multi-tool for exploring and publishing data</a></li>
<li><a href="https://medium.com/data-science/introduction-to-datasette-explore-and-publish-your-data-in-one-line-of-code-cbdc40cb4583">Introduction to Datasette : Explore and Publish Your Data in... | Medium</a></li>

</ul>
</details>

**标签**: `#datasette`, `#security`, `#vulnerability-disclosure`, `#release`, `#web-security`

---

<a id="item-17"></a>
## [苏莱曼警告：不应赋予 AI 模型权利与福利地位](https://simonwillison.net/2026/Sep/16/mustafa-suleyman/) ⭐️ 6.0/10

Simon Willison 引用了微软 AI 首席执行官 Mustafa Suleyman 的文章《关于“模型福利”的警告》，其中苏莱曼主张不应把 AI 模型视作拥有感受、偏好或权利的存在。他认为意识是人类伦理、法律与政治制度的根基，把任何形式的这类权利赋予模型既缺乏证据支撑，也会让 AI 的封控（containment）与对齐（alignment）难题更加棘手。 这番表态让一位在职的头部实验室高管明确站到了新兴的“模型福利”运动的对立面，而该运动已在 Anthropic 等实验室中获得一定关注。其意义在于，企业如何界定模型是否具备感知能力，会影响产品设计、内部研究优先级，以及 AI 系统是否应获得道德或法律考量的监管争论。 苏莱曼的论证更偏向后果论而非纯粹的形而上学：他并未声称已证明模型没有意识，而是认为现有证据不足以支持赋予权利，且这样做会主动加剧封控与对齐难题。该帖子本身只是一段引用块，Willison 未附加分析，因此技术深度有限。

rss · Simon Willison · 9月16日 16:00

**背景**: AI 对齐（alignment）是 AI 安全的一个子领域，关注如何让 AI 系统朝既定目标和人类价值前进，其中包含奖励破解（reward hacking）、欺骗行为和寻求权力等难题。AI 封控（containment）则指算力治理、控制方法等旨在防止先进系统违背人类利益的策略。“模型福利”之争源自 Anthropic 等实验室：那里有研究人员被专门指派去探讨模型是否值得道德考量，也有模型被赋予诸如终止其认为受辱骂或有害对话的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://medium.com/agi-is-living-intelligence/ai-model-welfare-is-now-a-job-heres-why-that-changes-everything-bbb8ede3be1f">AI Model Welfare Is Now a Job. Here’s Why That Changes... | Medium</a></li>
<li><a href="https://safeaiaus.org/preparing-for-agi/framework/containment/">AI Containment - Preventing Dangerous Systems - SafeAI-Aus</a></li>

</ul>
</details>

**标签**: `#ai-ethics`, `#ai-safety`, `#model-welfare`, `#llms`, `#consciousness`

---

<a id="item-18"></a>
## [字节火山引擎发布豆包 Doubao-Seed-2.1-pro 0915，Agent 交付更可靠](https://mp.weixin.qq.com/s/Fp_mgF6wxMk0bkUVBqOKqA) ⭐️ 6.0/10

9 月 16 日，字节跳动旗下的火山引擎发布 Doubao-Seed-2.1-pro 0915 版本，并在 API 上全量上线。此次升级聚焦三大方向：Agent 专业任务交付、多模态 Coding 和多模态理解，同时提升 Token 效率、进一步降低综合成本。 Agent 的可靠性与幻觉抑制正成为大模型进入企业生产环境的关键门槛，而能够自主调度子 Agent 交叉核验事实的版本，显然是面向真实生产任务而非演示场景。同时，这次更新也把豆包模型家族与字节自家的 AI 编程 IDE TRAE 更紧密地串联起来，使其在 Coding 与 Agent 任务上与国内其他前沿模型的竞争更加直接。 火山引擎称新版本强化了证据溯源与多源核验能力，可自主调度数百个子 Agent 交叉比对结果以减少幻觉；多模态 Coding 则能读懂设计稿和录屏并直接生成代码。官方还表示图像与视频推理的 Token 消耗较上一代减少 30% 以上，不过这次公告并未公布公开基准测试或评测方法。

telegram · zaihuapd · 9月16日 09:48

**背景**: 火山引擎是字节跳动的云计算业务部门，豆包（Doubao）则是其在该平台上对外提供的大模型系列。Doubao-Seed-Evolving 是一种特殊的「滚动式」模型卡片：它使用统一 Model ID，开发者一次接入即可自动升级、零迁移成本。TRAE 是字节跳动推出的 AI 编程 IDE，定位类似 Cursor，内置豆包等模型；而「多模态 Coding」指的是模型可以把设计稿、录屏等图像或视频作为输入来生成代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7663097122267987995">Doubao - Seed - Evolving ...</a></li>
<li><a href="https://developer.volcengine.com/articles/7670478135158112306">我用 Doubao - Seed - Evolving 做了一个每天早上都想打开的 AI...</a></li>
<li><a href="https://www.toutiao.com/topic/7544177431712712731/">字 节 的 aiide 是 否开源-今日头条</a></li>

</ul>
</details>

**标签**: `#LLM`, `#multimodal`, `#AI agents`, `#ByteDance`, `#model release`

---

<a id="item-19"></a>
## [微信 8.0.78 支持将聊天记录导出给 ChatGPT 和 Claude](https://www.chaincatcher.com/article/2290109) ⭐️ 6.0/10

手机微信升级到 8.0.78 后，用户多选聊天记录并点击「转发到其他应用」，除了腾讯自家的元宝和 WorkBuddy，还能通过「选择手机中的应用」把内容直接交给 ChatGPT 等第三方 App，一次最多 100 条。微信会把这些聊天内容打包成 ZIP 压缩包，其中包含按时间整理的 TXT 文件与附件，电脑端微信也开放了类似入口。 这是微信生态一次明显的开放动作：此前用户想把聊天内容交给外部 AI 助手，只能手动复制粘贴，如今数亿用户可以一键把真实对话上下文导出到 ChatGPT、Claude 等工具中。同时，这一功能事实上确立了一种导出格式（ZIP 包内含 TXT 与附件），让第三方开发者可以据此搭建中转工具，围绕中国最大的社交平台形成新的 AI 接入通路。 每次导出最多 100 条消息，打包格式为 ZIP 压缩包，内含按时间排序的 TXT 文本与附件，因此超长对话或图片视频密集的聊天记录会受到一定限制。应用选择列表中仍优先展示腾讯自家的元宝与 WorkBuddy，显示腾讯在引导用户先用内部 AI 产品，不过社区开发者已经基于电脑端入口做出中转工具，可将聊天记录送进 ChatGPT 与 Claude。

telegram · zaihuapd · 9月16日 14:15

**背景**: 微信是中国用户规模最大的即时通讯应用，其聊天数据长期封闭在 App 内部，没有官方的对外导出渠道。腾讯近年在平台内持续加码 AI：元宝于 2024 年作为微信首个内置 AI 助手上线，用户可直接添加为好友；WorkBuddy 则是腾讯面向办公场景的智能体工作台。AI 助手通常需要上下文才能发挥效果，因此把真实对话以结构化文件形式交给 AI，是让 AI 融入聊天工作流的实用前提。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/17238">Yuanbao , WeChat 's First AI Assistant , Officially Launches</a></li>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>
<li><a href="https://chozan.co/tencent-ai/">Tencent AI : How Tencent Is Embedding AI Across WeChat ... - ChoZan</a></li>

</ul>
</details>

**标签**: `#WeChat`, `#ChatGPT`, `#AI Integration`, `#Data Portability`, `#China Tech`

---

<a id="item-20"></a>
## [小米 MiMo-V2.6 启动大规模 RL 训练，细节将陆续开源](https://x.com/_LuoFuli/status/2100296686719610932) ⭐️ 6.0/10

Fuli Luo 在 X 上宣布，经过近半年的研究，MiMo 团队正在对 MiMo-V2.6 进行大规模强化学习训练，并同时在三个维度上扩展：计算量（每训练步约 20 亿 tokens）、环境（多任务 agentic RL）以及裁判计算（judge compute）。她同时表示相关细节将陆续开源。 这次 MiMo-V2.6 的训练是少有的公开信号，表明一家中国大型实验室正在扩展强化学习算力，而不只是预训练算力；而承诺开源细节，则可能为更广泛的 LLM 社区提供可复用的规模化 agentic RL 方案。这也让小米的 MiMo 系列在推理与智能体模型竞争中占据更有分量的位置——在后训练阶段，训练质量正越来越决定模型在真实场景中的可用性。 最引人关注的数字是每个 RL 训练步约处理 20 亿 tokens，这在后训练阶段属于相当可观的规模，意味着需要极强的 rollout 生成与奖励打分吞吐能力。提到「judge compute」说明团队除了策略训练外，还在扩展基于模型的奖励评判或评估计算量；而多任务 agentic RL 环境则意味着训练目标涉及工具调用与多步骤任务执行，而非单轮问答。此次公告并未披露任何基准测试成绩、模型规模或发布时间。

telegram · zaihuapd · 9月17日 01:52

**背景**: MiMo 是小米自研的大语言模型系列，其中 MiMo-V2.5 基于 MiMo-V2-Flash 主干网络，并扩展了专用的视觉与音频编码器，面向多模态感知、长上下文推理和智能体工作流。强化学习属于后训练阶段，通过奖励机制引导模型产出更好的结果；而「agentic RL」则把这一过程扩展到多步骤任务中，让模型在多轮交互里调用工具并在环境中执行动作。「judge compute」指的是用于给模型输出打分的评判模型所消耗的算力，它正被视为独立于训练算力之外的又一个扩展前沿，因为单一前沿模型作为裁判在生产规模下会变得昂贵、缓慢且带有偏见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/rl/?ref=upstract.com">mimo - v 2 . 6 RL</a></li>
<li><a href="https://galileo.ai/blog/scaling-judge-compute-ai-evaluation">Scaling Judge Compute : The Next Frontier in AI Evaluation | Galileo</a></li>
<li><a href="https://deepinfra.com/XiaomiMiMo/MiMo-V2.5">MiMo V 2 .5 API - Demo - DeepInfra</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#LLM-training`, `#agentic-RL`, `#open-source`, `#MiMo`

---
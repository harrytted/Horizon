---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 4 条内容中筛选出 4 条重要资讯。

---

1. [用 ARM64 汇编从头实现 YOLO26n 推理](#item-1) ⭐️ 8.0/10
2. [SpaceX 拒接 2028 年后 Falcon 9 订单，押注 Starship](#item-2) ⭐️ 8.0/10
3. [调查揭示 LLM 代币转售与欺诈市场](#item-3) ⭐️ 7.0/10
4. [Reddit 用户征集 NeurIPS 2026 理论论文初始审稿分数](#item-4) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [用 ARM64 汇编从头实现 YOLO26n 推理](https://www.reddit.com/r/MachineLearning/comments/1v6w394/i_implemented_the_yolo26n_model_inference_from/) ⭐️ 8.0/10

一名开发者完全使用 ARM64 汇编语言和 C 语言，从头实现了 YOLO26n 目标检测模型的推理，未使用任何现有框架，并在 Raspberry Pi 4 上获得了正确的检测结果。 这项工作展示了对神经网络推理和边缘 AI 优化技术的底层深入理解，突显了在资源受限设备上实现高效执行的潜力。 该实现包含了 ARM NEON SIMD 优化、Winograd 卷积、优化 GEMM 内核、缓存感知分块和算子融合，但性能提升低于预期。

reddit · r/MachineLearning · /u/Forward_Confusion902 · 7月26日 06:43

**背景**: YOLO（You Only Look Once）是一个实时目标检测模型系列。'nano'版本（YOLO26n）专为边缘设备设计。ARM64 汇编和 NEON SIMD 允许对硬件进行细粒度控制，但从头实现推理极其复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/STMicroelectronics/stm32ai-modelzoo/blob/main/object_detection/yolo26n/README.md">stm32ai-modelzoo/object_detection/yolo26n/README.md at main · STMicroelectronics/stm32ai-modelzoo</a></li>
<li><a href="https://huggingface.co/NexaAI/yolo26n-npu">NexaAI/yolo26n-npu · Hugging Face</a></li>
<li><a href="https://www.linkedin.com/pulse/introduction-arm-neon-simd-optimization-vijay-panchal">Introduction to ARM Neon SIMD Optimization</a></li>

</ul>
</details>

**标签**: `#ARM64`, `#YOLO`, `#edge AI`, `#assembly optimization`, `#deep learning inference`

---

<a id="item-2"></a>
## [SpaceX 拒接 2028 年后 Falcon 9 订单，押注 Starship](https://www.bloomberg.com/news/articles/2026-07-23/spacex-is-turning-away-falcon-customers-in-major-bet-on-starship) ⭐️ 8.0/10

SpaceX 已停止接受 2028 年后的 Falcon 9 专属发射请求，也不再接受拼单项目的未来预订，同时缩减 Falcon 非重复使用部件的生产，以加速向 Starship 过渡。 这一重大战略转变可能在 Starship 延误时导致发射能力缺口，影响依赖 SpaceX 提供低成本轨道进入的卫星运营商和整个航天产业。 SpaceX 仍可能为美国国防部和 NASA 保留 Falcon 9 任务，但如果 Starship 在 2028 年底前未能投入商业运营，许多太空公司将面临发射缺口。由于 Starship 延误，SpaceX 股价自 2026 年 6 月 IPO 以来已下跌约 25%。

telegram · zaihuapd · 7月26日 12:42

**背景**: Falcon 9 是 SpaceX 的主力火箭，凭借可重复使用和低成本主导了商业发射市场。Starship 是 SpaceX 下一代完全可重复使用的超重型运载火箭，计划用于月球和火星任务，但目前仍在开发中，尚未投入商业运营。

**标签**: `#SpaceX`, `#Starship`, `#Falcon 9`, `#Space Industry`, `#Launch Services`

---

<a id="item-3"></a>
## [调查揭示 LLM 代币转售与欺诈市场](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 7.0/10

Matt Lenhard 发布了一项关于 LLM 代币转售市场的调查，其中转售商通过汇集来自各种来源的 API 密钥来提供折扣访问，通常滥用免费试用、被盗信用卡和未受保护的支持机器人。该市场主要活跃在中国，使用 one-api 和 new-api 等开源代理软件。 该市场暴露了 LLM API 使用中的严重安全漏洞，转售商通过利用未受保护的端点和被盗凭证获利，可能导致开发者和供应商的财务损失。这凸显了 LLM 供应商迫切需要实施严格的 API 密钥上限和更好的滥用预防措施。 该转售市场依赖于开源 API 代理项目如 one-api 及其分支 new-api，这些合法工具被滥用于非法用途。买家包括寻求廉价代币、绕过地理限制或收集数据进行模型蒸馏的用户，而转售商则使用退单攻击和免费试用滥用等手段来降低成本。

rss · Simon Willison · 7月26日 19:30

**背景**: LLM API 代币代表用于访问 GPT-4 或 Claude 等模型的计算单元，通常按代币计费。转售市场通过将来自不同来源（包括被盗或滥用的账户）的多个 API 密钥聚合到单个代理端点，使转售商能够提供低于官方价格的折扣费率。这种滥用不仅给供应商造成经济损失，还会因流量增加而降低合法用户的服务质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vectoral.com/blog/token-relay-market">An Inside Look at the Relay Market Powering Token Resellers and Fraud | Vectoral</a></li>
<li><a href="https://simonwillison.net/2026/Jul/26/relay-market/">An Inside Look at the Relay Market Powering Token Resellers and Fraud</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI`, `#security`, `#fraud`, `#API`

---

<a id="item-4"></a>
## [Reddit 用户征集 NeurIPS 2026 理论论文初始审稿分数](https://www.reddit.com/r/MachineLearning/comments/1v77r9s/neurips_2026_main_track_theory_paper_tracker/) ⭐️ 4.0/10

一位 Reddit 用户发帖，邀请 NeurIPS 2026 主赛道理论论文的提交者分享他们的初始审稿分数和置信度，旨在识别审稿过程中的模式。 这一讨论揭示了顶级机器学习会议同行评审过程中可能存在的偏见，尤其是理论论文可能获得更保守的评分。理解这些模式有助于作者调整期望并优化投稿策略。 原帖作者报告其理论稿件获得了 4/3/3 的分数，置信度为 3/3/3。他们注意到理论论文通常获得较低的初始分数，且本周期各学科的分数普遍偏低。

reddit · r/MachineLearning · /u/Mammoth-Leg-3844 · 7月26日 15:57

**背景**: NeurIPS 是顶级的机器学习会议，论文经过同行评审，通常获得数字分数和置信度评级。初始分数在作者讨论之前给出，之后可能修改。理论论文侧重于数学基础，与实证工作相比更难评估，可能导致评分更为保守。

**标签**: `#NeurIPS`, `#conference review`, `#theory papers`, `#machine learning`

---
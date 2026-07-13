**中文** | [English](README.md)

# Semantic Decompression

把高熵专家材料重组成新人可以走通、复述和继续工作的解释，同时保留正式术语、事实、来源状态和证据边界。

它适合处理两类任务：

- 一段或一份文档把太多前提、术语、因果和流程压在一起；
- 一个仓库或素材包里同时存在语义根、ADR、代码、Spec、Report、Claim、Roadmap 和过期入口，需要先判断各自能证明什么。

## 它与相邻任务的区别

| 任务 | 主要目标 |
| --- | --- |
| 摘要 | 减少信息量 |
| 翻译 | 改变语言 |
| 润色 | 改善表达表面 |
| 术语表 | 分别定义名词 |
| 语义解压 | 恢复被省略的上下文、关系、过程和边界 |

语义解压可以变长，也可以很短。篇幅取决于读者缺少哪些桥梁，而不是追求更多字数。

## Agent 实际执行的主流程

`SKILL.md` 只保留所有分支共用的六步：

```text
固定读者契约
  -> 建立真相账本
  -> 定位缺失桥梁
  -> 设计可行走的路线
  -> 在需要处解压
  -> 交付并验收
```

每一步都有可检查的完成标准。领域诊断和仓库级规则放在按需 Reference 中，避免每次调用都加载无关细节。

## 两个分支

### 单一来源

默认使用“地图、走读、回看”：先给最小全景，再让一个贯穿示例穿过整条链，最后回到关键区别、边界和下一步。

适合架构说明、研究摘要、战略材料、政策、论证、指标分析和流程文档。

### Repository and Corpus Mode

当任务跨仓库、压缩包、多份文档、快照或冲突来源时，Skill 会按需加载 [`references/repository-corpus-mode.md`](references/repository-corpus-mode.md)，增加：

- Coverage Contract，说明实际读取、搜索、抽样和未覆盖范围；
- 按问题域发现的 Authority，而不是一条固定文件优先级；
- Source Ledger，为承重结论记录来源、时效、冲突和 Claim Ceiling；
- Current-State Gate，区分工件存在、实现存在、验证已观察、结论已接受和能力已交付；
- Term Registry，保留正式术语、别名、定义拥有者和适用层级。

仓库接手说明默认采用四层输出：

```text
一屏全景
  -> 一条真实路线
  -> 当前事实与目标状态
  -> 权威来源、未决问题和继续工作
```

## 使用示例

```text
这份架构 RFC 太压缩了。保留 Candidate、owner 和 canonical 等正式词，
从一次真实请求开始，解释权限、状态变化和失败恢复。
```

```text
基于这个仓库给新同事写接手说明。README、Spec 和 Report 有冲突，
请先判断各来源能证明什么，再写当前状态和下一入口。
```

```text
把这段论文结果给刚入组的研究生讲清楚。先建立直觉，
再说明统计含义、证据上限和不能推出的结论。
```

## 安装

把解压后的 `semantic-decompression/` 目录放入支持 Skills 的客户端目录，确保 `SKILL.md` 与 `references/` 保持相对路径不变。

典型结构：

```text
semantic-decompression/
├── SKILL.md
├── README.md
├── README_ZH.md
├── VERSION
├── LICENSE
├── CHANGELOG.md
├── references/
│   ├── decompression-lenses.md
│   └── repository-corpus-mode.md
└── evals/
    ├── evals.json
    ├── repository-evals.json
    ├── trigger-eval.json
    └── fixtures/example-repository/
```

## 评测

包内包含：

- 8 个单文档质量 Eval；
- 4 个仓库级 Eval；
- 27 个触发边界样例；
- 一个完全合成的最小仓库 Fixture。

Fixture 故意包含过期 README、未来产品方向、静态报告、缺失验证路径、dirty snapshot 和未接受 Claim，用来检验 Agent 是否会写出流畅但越过证据的说明。它不包含真实测试素材或用户项目内容。

## 0.2.1 的结构调整

0.2.0 增加了仓库级能力，但 Agent 入口也随之变长。0.2.1 按信息层级重新分工：

- `SKILL.md` 只保留共用步骤、分支选择和完成标准；
- 仓库分支的 Authority、Coverage、Source Ledger、Current-State Gate 和 Term Registry 只在对应 Reference 中定义；
- 通用领域镜头保留在另一份 Reference；
- README 负责向人解释项目，不成为运行时规则的第二份来源。

能力没有回退，默认调用的上下文更短，分支规则的单一事实源也更清楚。

## 边界

这个 Skill 帮助读者理解材料，不替代法律、医学、财务或安全专业判断。它也不是自动化全仓库审计器，验证强度始终受可用环境、工具和实际覆盖范围限制。

## License

MIT

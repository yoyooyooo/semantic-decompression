<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

# Semantic Decompression：语义解压

有些材料里的每个词都认识，整条链路仍然走不通。读者不知道谁在做决定、状态怎样变化、结论依赖什么前提，也分不清已经成立的事实和仍在讨论的方案。

Semantic Decompression 补回这些被省略的桥梁，同时保留正式术语、事实、证据强度和不确定性。

## 一个最小例子

压缩表达：

> 申请在实质性完整后进入法定审查期，补件会中止时钟。

语义解压后：

> 机构收到申请，不代表法定审查期限已经开始。机构会先判断材料是否完整到可以正式审理，达到这个状态后，审查时钟才启动。后续若要求补充关键材料，计时会暂停，通常要等补件被确认后继续。读者因此需要区分“已经提交”“被认定为完整”和“正式审查中”三个状态。

解压没有替换正式概念，也没有改变规则，只把状态、触发条件和实际影响补了回来。

## 适合的任务

- 给新接手者解释技术架构、业务决策、研究结论、政策或复杂论证。
- 把术语密集的材料改成可学习的伴读说明或从零教程。
- 恢复行动者、因果、状态变化、前提、例外和端到端流程。
- 面向非专家改写，同时保留领域正式术语和证据边界。

它不替代摘要、翻译、普通润色或术语表。摘要减少信息量，翻译转换语言，润色改善表达，术语表解释单个概念。语义解压恢复概念之间缺失的连接。

## 它怎样工作

Skill 内部使用六步流程：固定读者契约，建立结论账本，定位缺失桥梁，设计可行走路线，在需要处解压，最后做读者验收。README 不复制完整运行规程，权威版本见 [`SKILL.md`](SKILL.md)。

用户通常会看到三件事：

1. 原始结论和证据边界被保留下来。
2. 一个代表性对象从触发到结果被完整走读。
3. 术语在真实流程需要它的位置出现，而不是堆成词典。

## 多来源材料

多文件、多个版本或历史报告有时会影响结论的状态、来源和覆盖范围。此时 Skill 会按需读取 [`references/multi-source-boundaries.md`](references/multi-source-boundaries.md)，只补三条边界：

- 当前、目标、提案、历史和未知不能混写。
- 承重结论要能回到支持它的来源，冲突需要保留。
- 结论范围不能超过实际检查和搜索的范围。

这是一层证据边界，不是仓库审计流程。材料位于仓库中，并不会自动触发完整盘点、Authority 梯子、术语注册表或穷尽式阅读。

## 使用示例

单文档：

> 把这段架构说明给新同事讲清楚。保留 Candidate、accepted frontier 和 canonical Utterance，补出谁有权决定、请求怎样跑、崩溃后怎样恢复。

决策材料：

> 不要只翻译 NRR、ICP 和 CAC payback。解释这些指标在当前决策里各自约束什么、因果关系是什么、可能牺牲什么。

多来源材料：

> 根据这几份设计、当前状态和历史报告写一份接手说明。区分已经验证的能力、当前 Scaffold、目标状态和未知项，并说明你实际覆盖了哪些来源。

## 安装

将整个 `semantic-decompression` 目录放入宿主支持的 Skills 目录。不要只复制 `SKILL.md`，Reference、Eval 和检查脚本都是包的一部分。

安装后，可用自然语言提出解释、接手、伴读或从零教程类请求。Skill 保持 model-invoked，不要求固定命令前缀。

## 包结构

```text
semantic-decompression/
  SKILL.md
  README.md
  README_EN.md
  VERSION
  CHANGELOG.md
  references/
    decompression-lenses.md
    multi-source-boundaries.md
  evals/
    evals.json
    trigger-eval.json
    multi-source-evals.json
    fixtures/example-corpus/
  scripts/
    check.py
    check.sh
```

`decompression-lenses.md` 是诊断工具库，只读取与当前缺口有关的小节。`multi-source-boundaries.md` 是窄范围补充，只在多来源真的改变结论时读取。

## 验证

运行静态检查：

```bash
bash scripts/check.sh
```

检查覆盖 front matter、JSON、Eval 文件引用、Markdown 相对链接、双语入口、旧文件名残留、隐私路径和破折号。

Eval 分三层：

- `evals.json` 检查输出是否恢复读者、结论、桥梁、路线和边界。
- `trigger-eval.json` 检查是否与摘要、翻译、润色、代码修复和普通仓库任务混淆。
- `multi-source-evals.json` 只检查状态、来源和覆盖边界，不测试完整仓库审计。

## 限制

语义解压只能恢复材料和可用工具能够支持的模型。它不会替材料补造事实，也不会把历史检查写成当前验证。法律、医学、财务、安全等高风险领域仍需相应专业判断。

# HANDOFF — Fortune Cookie Wisdom for Developers

## 比赛

- slug: `u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44`
- 奖金：$2（第 1 名 $1.18 / 第 2 名 $0.82）
- 截止：北京时间 2026-11-27 08:25（UTC 2026-11-27 00:25）
- 入口：程序写 `/output/entry.txt`，UTF-8，1–120 字符，非纯空白
- 仓库名：`makefun-fortune-cookie-developers`

## 文案（用户亲口原话，一字不改）

A variable you name `temporary` today will outlast your manager.

- 字符数：64（上限 120，通过）
- 字节数：64（纯 ASCII，含两处反引号，原样保留）
- sha256：`1ed76d578a3ddb824a18b4d95682795a668d632c38494b9c6f6756e878f18a57`
- 无尾随换行

## 做法

- `main.py` 亲手写了两版：第一版只写文件并跑通；第二版做了真正的改进——写完后把 `/output/entry.txt` 读回来逐字节比对，不一致就报错退出（exit 1）。
- 不读外部文件，不联网，只写固定文案。
- 其余文件均为亲手写：`LICENSE`（MIT，含 SPDX 行）、`README.md`（投稿说明 + 比赛页链接 + 三枚官方徽章）、`prompt.txt`（文案原文单行）、`.makefun/owner.json`（钱包地址）。

## 校验结果

- 第一版 main.py：运行成功，entry.txt 64 字节，sha256 `1ed76d57…8a57`。
- 第二版 main.py：连续运行两次，两次输出 sha256 均为 `1ed76d578a3ddb824a18b4d95682795a668d632c38494b9c6f6756e878f18a57`，`cmp` 逐字节一致。
- 注意：本机 `/output/entry.txt` 和 `/tmp/entry_run*.txt` 与其他并行投稿工人共享，曾被其他场的输出覆盖；校验用的两次运行输出已改存仓库内唯一路径再比对，不受干扰。评分时程序在独立沙箱里跑，不受影响。

## 状态

- 未提交、未建 GitHub 仓、未打包 bundle。等下一步指示。

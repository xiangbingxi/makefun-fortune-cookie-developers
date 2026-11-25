# Fortune Cookie Wisdom for Developers

One original fortune-cookie line for a software developer, 120 characters or fewer.

## Entry

> A variable you name `temporary` today will outlast your manager.

64 characters. The program writes this line, exactly as-is, to `/output/entry.txt` (UTF-8, no trailing newline).

## How it works

Run `main.py` with Python 3. It creates `/output` if needed, writes the entry, then reads the file back and compares it byte for byte against the expected text. Any mismatch exits non-zero.

## Competition

- Bounty: [Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
- Repository: `makefun-fortune-cookie-developers`
- License: MIT

![Bounty](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)
![Rank](https://make.fun/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/xiangbingxi/makefun-fortune-cookie-developers/rank.svg)
![Reward](https://make.fun/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/xiangbingxi/makefun-fortune-cookie-developers/reward.svg)

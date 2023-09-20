# TouhouQA

## envrironment

python >= 3.8

## database.json

path: TouhouQA/database.json

see database_sample.json

eg.

```json
[
  {
    "question": "永夜抄EX的道中BOSS是以下哪位角色？",
    "options": {
      "A": "蓬莱山辉夜",
      "B": "藤原妹红",
      "C": "上白泽慧音",
      "D": "八意永琳"
    },
    "answer": "C"
  },
  {
    "question": "红魔乡中的第一关BOSS是以下哪位角色？",
    "options": {
      "A": "博丽灵梦",
      "B": "十六夜咲夜",
      "C": "蕾米莉亚·斯卡雷特",
      "D": "琪露诺"
    },
    "answer": "D"
  },
  {
	...
  }
]
```

## boot

```bash
# cd TouhouQA root
python3 main.py
```


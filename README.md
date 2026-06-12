# 構成
zap-terraform-lab
├── .github/workflows/
│   └── zap-baseline.yml
│
├── scripts/
│   └── zap_to_sarif.py        ★SARIF変換してCode Scanningに流し、ダッシュボード表示ため
│
├── docs/
│   ├── index.html              ★ダッシュボード入口
│   ├── zap-report/
│   │    └── YYYY-MM-DD-HHMMSS/
│   │         ├── index.html
│   │         └── report_json.json
│   ├── data/
│   │    └── status.json      
│   └── dashboard/
│        └── index.html        ★NEW（統合UI）
│
└── zap.sarif                  ★生成物
│   └── app\
├── .gitignore
└── README.md

# デプロイ
git init
git add .
git commit -m "コメント"

git branch -M main
git remote add origin https://github.com/sunaiheng/zap-terraform-lab.git
git push -u origin main

git add .github/workflows/zap-baseline.yml
git commit -m "コメント"
git push

# ※二回目以降
※　push する前に pull　※　
git status
git pull --rebase origin main
git add .
git commit -m "コメント"
git push

# 確認
https://sunaiheng.github.io/zap-terraform-lab/

# test

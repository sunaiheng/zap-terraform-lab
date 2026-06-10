# 構成
zap-terraform-lab
├── .github
│   └── workflows
│       └── zap-baseline.yml
├── docs
│   ├── index.html
│   └── zap-report\
│       ├── index.html(自動生成)
│   └── app\
│   └── data\
│        └── status.json(自動生成)
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

# Portland Guide 2026 — Dave家族版

## GitHub Pages でのデプロイ方法

### 1. このリポジトリをGitHubにプッシュ

```bash
git init
git add .
git commit -m "Initial Portland Guide"
git remote add origin https://github.com/あなたのユーザー名/portland-guide.git
git push -u origin main
```

### 2. GitHub Pages を有効化

1. リポジトリの **Settings** を開く
2. 左メニューの **Pages** をクリック
3. Source: **Deploy from a branch**
4. Branch: **main** / **(root)**
5. **Save** をクリック

数分後に `https://あなたのユーザー名.github.io/portland-guide/` で公開されます。

---

## 写真の追加方法

### `images/` フォルダに写真を入れる

各カードに対応するファイル名で保存してください：

| ファイル名 | 店/スポット |
|-----------|------------|
| `images/tinshed.jpg` | Tin Shed Garden Cafe |
| `images/nongs.jpg` | Nong's Khao Man Gai |
| `images/hatyai.jpg` | Hat Yai |
| `images/eem.jpg` | Eem Thai BBQ |
| `images/gado.jpg` | Gado Gado |
| `images/campana.jpg` | Campana |
| `images/nostrana.jpg` | Nostrana |
| `images/jacqueline.jpg` | Jacqueline |
| `images/takibi.jpg` | Takibi |
| `images/stumptown.jpg` | Stumptown Coffee |
| `images/muji.jpg` | MUJI Portland |
| `images/kiriko.jpg` | Kiriko Made |
| `images/powells.jpg` | Powell's Books |
| `images/meadow.jpg` | The Meadow |
| `images/saltandstraw.jpg` | Salt & Straw |
| `images/pips.jpg` | Pip's Doughnuts |
| `images/pix.jpg` | Pix Patisserie |

写真のおすすめ取得元：
- 各店の公式Instagram
- Google Maps の写真（個人利用目的）
- Yelp の写真

### 写真サイズの目安
- 横: 800px 以上
- 縦: 500px 以上
- ファイルサイズ: 300KB 以下（圧縮推奨）

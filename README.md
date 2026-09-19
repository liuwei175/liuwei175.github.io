# Wei Liu — GitHub Pages 更新包

同步日期：2026-09-18  
版本：补齐 Teaching / Group 的完整覆盖更新包  
目标仓库：https://github.com/liuwei175/liuwei175.github.io  
目标网站：https://liuwei175.github.io/  
内容来源：https://sites.google.com/view/liu-wei/homepage 及其公开子页面。

## 上传方法

这是用于现有仓库的**覆盖更新包**，不是空仓库的完整备份。

1. 解压 ZIP。打开仓库 `main` 分支的根目录，选择 **Add file → Upload files**。
2. 将解压后的文件和 `ch` 文件夹拖入上传区域，保持目录结构并覆盖同名文件。
   `index.html` 必须位于仓库根目录；中文版必须位于 `ch/index.html`。
3. 提交修改。采用分支发布时，Pages 设置应为 **Deploy from a branch → main → /(root)**。
   原网站已使用这一发布源时，无须调整设置。

**不要只上传 ZIP 文件本身，也不要把解压后最外层文件夹整体作为一个新目录上传。**
不要清空原仓库：本更新包继续使用现有的 `lw.jpeg` 和 `favicon.ico`。
`Myphoto.jpg`、旧的 `jemdoc.css`、`MENU`、其他原有文件均可保留。
全部十一个页面使用 `site.css`，不会覆盖旧样式表或破坏其他遗留页面。

本包是已经生成的 HTML/CSS。部署不需要 Python、Node.js、Jekyll、npm 或额外构建操作。
`.nojekyll` 是静态发布标识；浏览器上传时看不到隐藏文件也不影响这些普通 HTML/CSS 页面。

## 同步范围

| 文件 | 内容 |
| --- | --- |
| `index.html` | 英文主页：新邮箱、六条消息、简介、研究兴趣、精选论文、教育、经历、奖项、技能及审稿 |
| `ch/index.html` | 对应的中文主页；全部站内跳转已使用正确的相对路径 |
| `research-summary.html` | 研究总结、当前重点及源站对大语言模型的个人评价 |
| `opening.html` | PolyU 2027 / Wuhan University 2028 招生说明及当前名额提示 |
| `publications.html` | 十条期刊论文/预印本、两条 TMLR 论文、代码及学位论文链接 |
| `talks.html` | 十一项会议报告、七项邀请报告以及源站提供的 slides 链接 |
| `grants.html` | 四项科研项目 |
| `teaching.html` | PolyU 教学：AMA542 Operations Research；AMA1140 Mathematics for Construction and Environment |
| `group.html` | 独立研究团队页面；源站尚无成员资料，保留简洁占位并链接招生页及已公开邮箱 |
| `links.html` | 数学研究机构与英文写作资源的原始目标链接 |
| `photos.html` | 保留 Google Sites 相册入口 |

保留原站简洁学术风格、英文/中文入口及所有现有页面地址；补充移动端布局、键盘焦点样式、
跳至正文链接、页面说明、canonical、sitemap 和 robots 文件。正文不依赖 JavaScript、外部字体或 CDN。

## 本次补充

- 新增 `teaching.html` 与 `group.html`，延续原更新包的学术风格和移动端布局。
- 全部 11 个页面均已加入 Teaching / Group 入口；中文主页使用“教学”“研究团队”，并指向根目录英文页面。
- 两个新页面均有正确的当前页面高亮、标题、页面说明、canonical 和 sitemap 条目。
- Teaching 按源站同步两门课程，不推断学期、授课年份或教材链接。
- Google Sites 的 Group 页当前仅有标题，因此仅添加页面框架、招生页入口和已公开邮箱，不虚构成员资料。
- 本包包含上一版的所有文件，无须先上传旧 ZIP；为了同步所有导航，请上传整包，而非仅上传两个新增 HTML。
- 除导航外，原有 9 页正文和 `site.css` 保持不变。

## 内容处理说明

- 2027 年武汉大学任职按原站的年份与职称保留，但改用将来时，避免把未来任职写成已发生。
- 新闻保留原站的 `MM.DD` 日期与顺序，不补猜年份。
- 源站主页把人才计划入选年份写为 2026，而 Grants 页把项目起始年份写为 2025；本包分别保留，未擅自统一。
- 随机光滑化论文在各页统一为主页的新表述 `min-expectation-max`；历史报告标题仍按源站保留。
- 对论文、报告、代码、学位论文恢复可点击链接，移除部分链接中的跟踪参数。
- 保留两条相关的线性约束论文/预印本记录；扩展预印本中的 MOR 链接标为 `Related MOR paper`。
- 2026 年 10 月的邀请报告标注为 scheduled。招生页的未来年份与“目前没有独立博士名额”说明都保留。
- Google Sites 的相册图片没有打包下载；原相册入口保留。头像继续使用仓库中的 `lw.jpeg`，不生成或替换人物照片。
- Google Scholar 和部分代码地址限制自动抓取，链接按源站保留；不声称全部站外地址已通过实时可达性检查。

详细来源和变更说明见 `migration-manifest.json`。核查结果见 `VALIDATION.md`。
本次只交付文件；没有修改远端仓库，也没有声称网站已经上线。

## 本地检查（可选，非部署前提）

仅检查更新包：`python check_site.py --overlay`

把更新包合并到原仓库后：`python check_site.py`

本地预览可在合并后的目录运行 `python -m http.server 8000`，打开 `http://localhost:8000/`。

## GitHub 官方说明

- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

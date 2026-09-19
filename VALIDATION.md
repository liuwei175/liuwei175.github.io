# 核查报告：Teaching / Group 补充版

同步基准日期：2026-09-18。

## 本次变更

- 新增 `teaching.html` 和 `group.html`，更新包现包含 **11 个 HTML 页面**：10 个英文页面、1 个中文主页。
- Teaching 根据 Google Sites 公开页面同步两门 PolyU 课程：AMA542 Operations Research；AMA1140 Mathematics for Construction and Environment。没有推断授课年份、学期或教材链接。
- Google Sites 的 Group 页面当前仅显示标题，没有公开成员条目。本包提供简洁占位、现有 Opening 页入口及已公开的联系邮箱，没有虚构成员资料。
- 全部 11 页导航均已加入两个新页面；中文主页使用“教学”和“研究团队”，相对路径为 `../teaching.html` 和 `../group.html`。
- 已逐页检查当前页面高亮、导航标签与目标路径；两个新页面均加入 sitemap，共 11 个页面地址。
- 与上一版 ZIP 逐文件对比：**原有 9 个 HTML 页面除导航外保持逐字一致，`site.css` 保持字节级一致。**
- `README.md`、`migration-manifest.json` 和本核查报告同步更新。

## 静态检查

执行 `python check_site.py --overlay` 的实际结果：

```text
Checked 11 HTML pages, 166 local references, 149 external references.
Existing repository assets intentionally excluded from this overlay: favicon.ico, lw.jpeg
External reference availability is not tested by this script.
PASS: local page links, anchors, required metadata, and image descriptions.
```

另行检查全部 11 页均有且仅有一个 Teaching / Group 导航入口，当前页面高亮指向本页，中文标签和相对路径正确；sitemap 包含全部 11 页。

检查范围包括站内页面链接、锚点、必要页面元信息、图片说明、导航和 sitemap。
149 是站外引用的出现次数，不代表独立站点数量；未对全部站外链接执行实时 HTTP 可达性测试。
这不是 HTML5 标准一致性认证。

## 浏览器布局检查

使用 Chromium 将全部 11 页分别在 **1440、768、390、320 像素**宽度下离线渲染，共 **44 种页面/视口组合**。
检测到的水平溢出均为 **0 像素**；确认两个新增导航入口在各宽度均可见。
另行查看了 Teaching 桌面页与 Group 手机页的截图，检查文字换行、导航高亮及页脚显示。

渲染通过直接载入页面 HTML 与本包 CSS 完成；站外资源请求被阻止。
未随包附带的头像 `lw.jpeg` 和图标 `favicon.ico` 未在离线检查中加载，必须保留原仓库中的文件。
未进行 GitHub Pages 线上部署或运行状态验证。

## 交付范围

- 本包是**包含上一版全部文件的完整覆盖更新包**，不是只有两个新增 HTML 的增量补丁，也不是可替代原仓库的完整备份。
- 上传时保留文件结构，将包内全部内容覆盖到仓库根目录，以同步所有导航；不要清空原仓库。
- 原有头像、图标及相册处理方式不变。没有添加构建步骤、外部字体、JavaScript 或 CDN 依赖。
- 本次没有修改远端仓库，没有声称更新已在线发布。

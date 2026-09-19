# 核查报告

同步基准日期：2026-09-18。

## 文件与内容

- 更新包包含 9 个 HTML 页面，其中英文页面 8 个，中文主页 1 个；保留原有页面路径。
- 中英文主页各有 6 条新闻、6 篇精选论文和 8 项期刊审稿记录。
- 论文页包含 10 条期刊论文/预印本记录及 2 条其他论文记录；学术报告页包含 11 项会议报告和 7 项邀请报告；项目页包含 4 项项目。
- 已检查新邮箱、未来任职说明、招生年份、招生名额提示、论文与报告链接及中英文站内跳转。
- 来源及需要保留的源站日期差异，见 `migration-manifest.json` 和 `README.md`。

## 静态检查

执行 `python check_site.py --overlay` 的结果：

```text
Checked 9 HTML pages, 119 local references, 144 external references.
Existing repository assets intentionally excluded from this overlay: favicon.ico, lw.jpeg
External reference availability is not tested by this script.
PASS: local page links, anchors, required metadata, and image descriptions.
```

检查范围包括本地页面链接、锚点、必要页面元信息及图片说明。
144 是页面内站外引用的出现次数，并非独立站外网站数量。
这不是 HTML5 标准一致性认证，也不是所有站外地址的实时 HTTP 可达性测试。

## 浏览器布局检查

使用 Chromium 对全部 9 页分别在 1440、768、390、320 像素宽度下离线渲染，共 36 种页面/视口组合。
检测到的水平溢出均为 0 像素；另外查看了英文桌面主页、英文手机主页和中文桌面主页的截图。

浏览器渲染通过直接载入页面内容与本包 CSS 完成；当前环境不允许本地 HTTP 页面导航，故没有完成本地 HTTP 服务或 GitHub Pages 线上部署测试。
离线检查时，未随包附带的 `lw.jpeg` 和 `favicon.ico` 不会加载。
这两项由现有 GitHub 仓库提供，上传时必须保留；不应把离线截图中的图片未加载误认为已验证线上图片显示。

## 交付边界

- 本包是现有仓库的覆盖更新包，不是独立的完整仓库备份。
- 继续引用仓库现有头像和图标；Google Sites 相册图片没有下载或复制，相册页保留源站入口。
- 正文不依赖 JavaScript、外部字体或 CDN；现有图片仍须在原仓库中保留。
- 部分站外地址限制自动抓取，按源站保留；没有声称全部站外链接均可实时访问。
- 没有修改远端仓库，没有声称更新已在线发布。

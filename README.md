# 2026 GLaDOS 自动签到

> 🎯 专为 2026 积分制度优化，精准获取 **Points**，PushPlus 微信推送

[![Auto Checkin](https://github.com/YOUR_USERNAME/2026-glados-checkin/actions/workflows/checkin.yml/badge.svg)](https://github.com/YOUR_USERNAME/2026-glados-checkin/actions)

## ✨ 功能

- 🎯 **精准积分** - 获取真实积分数据 + 变化量
- 🎁 **兑换提示** - 显示当前可兑换选项
- ☁️ **Cloud优先** - 强制使用 glados.cloud
- 📱 **微信推送** - PushPlus 漂亮的 HTML 报告
- 🍪 **智能Cookie** - 支持 Cookie-Editor 导出格式

## 🚀 快速部署 (3分钟)

### 第一步：Fork 仓库

点击右上角 **Fork** 按钮

### 第二步：获取 Cookie

1. 安装 [Cookie-Editor](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) 浏览器扩展
2. 登录 [glados.cloud](https://glados.cloud)
3. 点击 Cookie-Editor 图标，复制这两个值：
   - `koa:sess` → 长字符串
   - `koa:sess.sig` → 短字符串
4. 组合格式：
   ```
   koa:sess=你的长字符串; koa:sess.sig=你的短字符串
   ```

### 第三步：配置 Secrets

进入你 Fork 的仓库 → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| Name | Value | 必需 |
|------|-------|------|
| `GLADOS_COOKIE` | 上一步组合的 Cookie | ✅ 是 |
| `PUSHPLUS_TOKEN` | [获取方式](#获取-pushplus-token) | ❌ 否 |

### 第四步：启用 Actions

1. 进入 **Actions** 标签
2. 点击 **I understand my workflows, go ahead and enable them**
3. 点击左侧 **GLaDOS 2026 Checkin** → **Run workflow** 测试

---

## 📱 获取 PushPlus Token

1. 访问 [pushplus.plus](http://www.pushplus.plus/)
2. 微信扫码登录
3. 点击 **发送消息** → **一对一消息**
4. 复制页面上显示的 Token

---

## 📊 推送效果预览

签到后你会收到这样的微信推送：

```
👤 your@email.com

当前积分: 46 (+20)
剩余天数: 353 天
签到结果: Bindweed! Bindweed!

🎁 兑换选项:
❌ 100分→10天 (差54分)
❌ 200分→30天 (差154分)
❌ 500分→100天 (差454分)
```

---

## ⏰ 自动运行时间

每天 **北京时间 9:30** 自动执行

---

## 📂 文件说明

| 文件 | 说明 |
|------|------|
| `checkin.py` | 核心签到脚本 |
| `.github/workflows/checkin.yml` | GitHub Actions 配置 |
| `requirements.txt` | Python 依赖 |

---

## ❓ 常见问题

**Q: 显示 "please checkin via https://glados.cloud"？**  
A: 今天已经签到过了，明天会正常显示。

**Q: Cookie 多久过期？**  
A: 约 30 天，过期后重新获取即可。

**Q: 支持多账号吗？**  
A: 支持，用 `&` 分隔多个 Cookie。

---

## 📝 License

MIT

# scripts/ — 工具脚本

## check_links.py

批量链接核查器（Python 3，标准库，无依赖）。

```bash
# 全量检查（urls.json 为字符串数组）
python check_links.py urls.json out.json

# 分批检查（第 0-50 条）
python check_links.py urls.json out.json 0 50
```

- 策略：直连 HEAD → 直连 GET → 代理重试（`CHECK_PROXY` 环境变量可配置代理地址）。
- 分类：`ok`（2xx/3xx）/ `guard`（403/405/429，浏览器可达）/ `auth`（401/451）/ `fail`。
- CI 侧同时启用了 lychee（见 `.github/workflows/links.yml`），本地快速核查用本脚本。

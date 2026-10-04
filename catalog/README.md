# catalog/ — 机器可读条目目录

单一事实来源（SSOT）：工具、引擎、资源的元数据集中在这里；文档与未来站点引用这里的数据，避免同一事实多处维护。

## 字段规范

见 [`schema.json`](schema.json)。必备字段：`name` / `homepage` / `description` / `category` / `license` / `added` / `reviewed` / `status`。

注意：`license` 字段为快照信息，以各项目仓库的最新声明为准。

## 现有数据

- [`engines.yml`](engines.yml) — 开源引擎（种子）
- [`tools.yml`](tools.yml) — 开源工具（种子）
- [`art-tools.yml`](art-tools.yml) — 美术与设计工具（49 条）
- [`audio-tools.yml`](audio-tools.yml) — 音频工具（55 条）
- [`assets-free.yml`](assets-free.yml) — 免费素材库（52 条）

## 贡献

新增条目请附 `homepage` 与 `repo`（如有），自行核验可访问后提交 PR。

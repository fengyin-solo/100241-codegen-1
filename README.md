# 危险货物道路运输调度平台

面向危险货物运输企业备案、车辆罐体检验、驾驶员押运员资质、动态监控与应急处置的一体化调度后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 运输企业 | `enterprise` | 运输企业 | 企业编号、企业名称、经营许可号 |
| 危运车辆 | `vehicle` | 危运车辆 | 车辆编号、车牌号码、车辆类型 |
| 驾驶员 | `driver` | 驾驶员 | 驾驶员编号、驾驶员姓名、从业资格证号 |
| 押运员 | `escort` | 押运员 | 押运员编号、押运员姓名、资格证号 |
| 危险货物 | `cargo` | 危险货物 | 货物编号、货物名称、危险类别 |
| 运输任务 | `trip` | 运输任务 | 任务编号、承运企业、危险货物 |
| 运输路线 | `route` | 运输路线 | 路线编号、路线名称、起讫地点 |
| 罐体检验 | `tank` | 罐体检验单 | 检验编号、罐体编号、所属车辆 |
| 装卸作业 | `loading` | 装卸作业单 | 作业编号、作业类型、作业地点 |
| 动态监控 | `monitor` | 动态监控记录 | 监控编号、关联任务、监控项目 |
| 报警处置 | `alarm` | 报警事件 | 报警编号、报警类型、报警等级 |
| 事故登记 | `accident` | 事故记录 | 事故编号、关联任务、事故类型 |
| 应急预案 | `emergency` | 应急预案 | 预案编号、预案名称、适用货物 |
| 通行报备 | `permit` | 通行报备单 | 报备编号、关联任务、报备类型 |
| 安全培训 | `training` | 安全培训 | 培训编号、培训主题、培训对象 |
| 动态检查 | `inspect` | 检查记录 | 检查编号、检查对象、检查类型 |
| 隐患整改 | `rectify` | 整改单 | 整改编号、关联问题、隐患等级 |
| 运输结算 | `settle` | 运输结算单 | 结算编号、承运企业、结算周期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

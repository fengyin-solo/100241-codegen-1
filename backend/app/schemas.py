"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class EnterpriseEntry(BaseModel):
    """运输企业明细结构。"""

    field_0: str | None = None  # 企业编号
    field_1: str | None = None  # 企业名称
    field_2: str | None = None  # 经营许可号
    field_3: str | None = None  # 经营范围
    field_4: str | None = None  # 注册地址
    field_5: str | None = None  # 安全负责人
    field_6: str | None = None  # 年审日期
    field_7: str | None = None  # 企业状态

class VehicleEntry(BaseModel):
    """危运车辆明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 车牌号码
    field_2: str | None = None  # 车辆类型
    field_3: str | None = None  # 核定载质量
    field_4: str | None = None  # 罐体容积
    field_5: str | None = None  # 所属企业
    field_6: str | None = None  # 年检日期
    field_7: str | None = None  # 车辆状态

class DriverEntry(BaseModel):
    """驾驶员明细结构。"""

    field_0: str | None = None  # 驾驶员编号
    field_1: str | None = None  # 驾驶员姓名
    field_2: str | None = None  # 从业资格证号
    field_3: str | None = None  # 准驾车型
    field_4: str | None = None  # 所属企业
    field_5: str | None = None  # 证件有效期
    field_6: str | None = None  # 违章次数
    field_7: str | None = None  # 驾驶员状态

class EscortEntry(BaseModel):
    """押运员明细结构。"""

    field_0: str | None = None  # 押运员编号
    field_1: str | None = None  # 押运员姓名
    field_2: str | None = None  # 资格证号
    field_3: str | None = None  # 所属企业
    field_4: str | None = None  # 培训日期
    field_5: str | None = None  # 证件有效期
    field_6: str | None = None  # 押运次数
    field_7: str | None = None  # 押运员状态

class CargoEntry(BaseModel):
    """危险货物明细结构。"""

    field_0: str | None = None  # 货物编号
    field_1: str | None = None  # 货物名称
    field_2: str | None = None  # 危险类别
    field_3: str | None = None  # 联合国编号
    field_4: str | None = None  # 包装类别
    field_5: str | None = None  # 应急处置措施
    field_6: str | None = None  # 生产企业
    field_7: str | None = None  # 货物状态

class TripEntry(BaseModel):
    """运输任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 承运企业
    field_2: str | None = None  # 危险货物
    field_3: str | None = None  # 起运地
    field_4: str | None = None  # 目的地
    field_5: str | None = None  # 计划发车时间
    field_6: str | None = None  # 预计到达时间
    field_7: str | None = None  # 任务状态

class RouteEntry(BaseModel):
    """运输路线明细结构。"""

    field_0: str | None = None  # 路线编号
    field_1: str | None = None  # 路线名称
    field_2: str | None = None  # 起讫地点
    field_3: str | None = None  # 途经路段
    field_4: str | None = None  # 路线里程
    field_5: str | None = None  # 限速要求
    field_6: str | None = None  # 风险等级
    field_7: str | None = None  # 路线状态

class TankEntry(BaseModel):
    """罐体检验单明细结构。"""

    field_0: str | None = None  # 检验编号
    field_1: str | None = None  # 罐体编号
    field_2: str | None = None  # 所属车辆
    field_3: str | None = None  # 检验类型
    field_4: str | None = None  # 检验日期
    field_5: str | None = None  # 下次检验日
    field_6: str | None = None  # 检验结论
    field_7: str | None = None  # 检验状态

class LoadingEntry(BaseModel):
    """装卸作业单明细结构。"""

    field_0: str | None = None  # 作业编号
    field_1: str | None = None  # 作业类型
    field_2: str | None = None  # 作业地点
    field_3: str | None = None  # 危险货物
    field_4: str | None = None  # 作业人员
    field_5: str | None = None  # 计划时段
    field_6: str | None = None  # 完成时间
    field_7: str | None = None  # 作业状态

class MonitorEntry(BaseModel):
    """动态监控记录明细结构。"""

    field_0: str | None = None  # 监控编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 监控项目
    field_3: str | None = None  # 超速次数
    field_4: str | None = None  # 疲劳驾驶次数
    field_5: str | None = None  # 偏航次数
    field_6: str | None = None  # 采集时段
    field_7: str | None = None  # 监控状态

class AlarmEntry(BaseModel):
    """报警事件明细结构。"""

    field_0: str | None = None  # 报警编号
    field_1: str | None = None  # 报警类型
    field_2: str | None = None  # 报警等级
    field_3: str | None = None  # 触发车辆
    field_4: str | None = None  # 触发时间
    field_5: str | None = None  # 确认人员
    field_6: str | None = None  # 处置说明
    field_7: str | None = None  # 报警状态

class AccidentEntry(BaseModel):
    """事故记录明细结构。"""

    field_0: str | None = None  # 事故编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 事故类型
    field_3: str | None = None  # 事故等级
    field_4: str | None = None  # 发生时间
    field_5: str | None = None  # 发生地点
    field_6: str | None = None  # 伤亡情况
    field_7: str | None = None  # 事故状态

class EmergencyEntry(BaseModel):
    """应急预案明细结构。"""

    field_0: str | None = None  # 预案编号
    field_1: str | None = None  # 预案名称
    field_2: str | None = None  # 适用货物
    field_3: str | None = None  # 响应等级
    field_4: str | None = None  # 处置流程
    field_5: str | None = None  # 责任单位
    field_6: str | None = None  # 演练日期
    field_7: str | None = None  # 预案状态

class PermitEntry(BaseModel):
    """通行报备单明细结构。"""

    field_0: str | None = None  # 报备编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 报备类型
    field_3: str | None = None  # 受理单位
    field_4: str | None = None  # 提交日期
    field_5: str | None = None  # 有效期限
    field_6: str | None = None  # 批复文号
    field_7: str | None = None  # 报备状态

class TrainingEntry(BaseModel):
    """安全培训明细结构。"""

    field_0: str | None = None  # 培训编号
    field_1: str | None = None  # 培训主题
    field_2: str | None = None  # 培训对象
    field_3: str | None = None  # 培训方式
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 参加人数
    field_6: str | None = None  # 考核合格数
    field_7: str | None = None  # 培训状态

class InspectEntry(BaseModel):
    """检查记录明细结构。"""

    field_0: str | None = None  # 检查编号
    field_1: str | None = None  # 检查对象
    field_2: str | None = None  # 检查类型
    field_3: str | None = None  # 检查日期
    field_4: str | None = None  # 检查人员
    field_5: str | None = None  # 发现问题数
    field_6: str | None = None  # 整改项数
    field_7: str | None = None  # 检查状态

class RectifyEntry(BaseModel):
    """整改单明细结构。"""

    field_0: str | None = None  # 整改编号
    field_1: str | None = None  # 关联问题
    field_2: str | None = None  # 隐患等级
    field_3: str | None = None  # 整改措施
    field_4: str | None = None  # 责任单位
    field_5: str | None = None  # 整改期限
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 整改状态

class SettleEntry(BaseModel):
    """运输结算单明细结构。"""

    field_0: str | None = None  # 结算编号
    field_1: str | None = None  # 承运企业
    field_2: str | None = None  # 结算周期
    field_3: str | None = None  # 运输趟次
    field_4: str | None = None  # 运费单价
    field_5: str | None = None  # 结算金额
    field_6: str | None = None  # 结算日期
    field_7: str | None = None  # 结算状态

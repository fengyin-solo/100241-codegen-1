"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import enterprise as router_enterprise
from app.routers import vehicle as router_vehicle
from app.routers import driver as router_driver
from app.routers import escort as router_escort
from app.routers import cargo as router_cargo
from app.routers import trip as router_trip
from app.routers import route as router_route
from app.routers import tank as router_tank
from app.routers import loading as router_loading
from app.routers import monitor as router_monitor
from app.routers import alarm as router_alarm
from app.routers import accident as router_accident
from app.routers import emergency as router_emergency
from app.routers import permit as router_permit
from app.routers import training as router_training
from app.routers import inspect as router_inspect
from app.routers import rectify as router_rectify
from app.routers import settle as router_settle

ROUTERS = [router_enterprise, router_vehicle, router_driver, router_escort, router_cargo, router_trip, router_route, router_tank, router_loading, router_monitor, router_alarm, router_accident, router_emergency, router_permit, router_training, router_inspect, router_rectify, router_settle]

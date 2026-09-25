<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">危险货物道路运输调度平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向危险货物运输企业备案、车辆罐体检验、驾驶员押运员资质、动态监控与应急处置的一体化调度后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "运输企业", path: "/enterprise" }, { label: "危运车辆", path: "/vehicle" }, { label: "驾驶员", path: "/driver" }, { label: "押运员", path: "/escort" }, { label: "危险货物", path: "/cargo" }, { label: "运输任务", path: "/trip" }, { label: "运输路线", path: "/route" }, { label: "罐体检验", path: "/tank" }, { label: "装卸作业", path: "/loading" }, { label: "动态监控", path: "/monitor" }, { label: "报警处置", path: "/alarm" }, { label: "事故登记", path: "/accident" }, { label: "应急预案", path: "/emergency" }, { label: "通行报备", path: "/permit" }, { label: "安全培训", path: "/training" }, { label: "动态检查", path: "/inspect" }, { label: "隐患整改", path: "/rectify" }, { label: "运输结算", path: "/settle" }]
</script>

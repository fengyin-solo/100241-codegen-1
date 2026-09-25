import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Enterprise = () => import('@/views/enterprise/index.vue')
const Vehicle = () => import('@/views/vehicle/index.vue')
const Driver = () => import('@/views/driver/index.vue')
const Escort = () => import('@/views/escort/index.vue')
const Cargo = () => import('@/views/cargo/index.vue')
const Trip = () => import('@/views/trip/index.vue')
const Route = () => import('@/views/route/index.vue')
const Tank = () => import('@/views/tank/index.vue')
const Loading = () => import('@/views/loading/index.vue')
const Monitor = () => import('@/views/monitor/index.vue')
const Alarm = () => import('@/views/alarm/index.vue')
const Accident = () => import('@/views/accident/index.vue')
const Emergency = () => import('@/views/emergency/index.vue')
const Permit = () => import('@/views/permit/index.vue')
const Training = () => import('@/views/training/index.vue')
const Inspect = () => import('@/views/inspect/index.vue')
const Rectify = () => import('@/views/rectify/index.vue')
const Settle = () => import('@/views/settle/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/enterprise', name: 'enterprise', component: Enterprise },
    { path: '/vehicle', name: 'vehicle', component: Vehicle },
    { path: '/driver', name: 'driver', component: Driver },
    { path: '/escort', name: 'escort', component: Escort },
    { path: '/cargo', name: 'cargo', component: Cargo },
    { path: '/trip', name: 'trip', component: Trip },
    { path: '/route', name: 'route', component: Route },
    { path: '/tank', name: 'tank', component: Tank },
    { path: '/loading', name: 'loading', component: Loading },
    { path: '/monitor', name: 'monitor', component: Monitor },
    { path: '/alarm', name: 'alarm', component: Alarm },
    { path: '/accident', name: 'accident', component: Accident },
    { path: '/emergency', name: 'emergency', component: Emergency },
    { path: '/permit', name: 'permit', component: Permit },
    { path: '/training', name: 'training', component: Training },
    { path: '/inspect', name: 'inspect', component: Inspect },
    { path: '/rectify', name: 'rectify', component: Rectify },
    { path: '/settle', name: 'settle', component: Settle },
  ],
})

export default router

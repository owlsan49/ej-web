import { createRouter, createWebHistory } from 'vue-router'
import YesOr from '@/views/YesOr.vue'
import Objective from '@/views/Objective.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/yesor',
      name: 'yesor',
      component: YesOr
    },
    {
      path: '/obj',
      name: 'obj',
      component: Objective
    },
    {
      path: '/',
      redirect: '/yesor'
    }
  ]
})

export default router

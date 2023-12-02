import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../components/HomePage')
  },
  {
    path: '/winery',
    name: 'winery',
    component: () => import('../components/Winery')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../components/Login')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../components/Register')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../components/ProfilePage')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

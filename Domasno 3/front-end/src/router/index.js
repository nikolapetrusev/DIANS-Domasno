import { createRouter, createWebHashHistory } from 'vue-router'
import {mutations, store} from "@/store/store";

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../components/HomePage'),
    beforeEnter: async (to, from, next) => {
      const response1 = await fetch(store.api_url + "/wineries");
      let wineries = await response1.json();
      wineries = JSON.parse(JSON.stringify(wineries))["wineries"];
      mutations.setWineries(wineries)

      const response2 = await fetch(store.api_url + "/cities");
      let cities = await response2.json();
      cities = JSON.parse(JSON.stringify(cities))["data"]
      mutations.setCities(cities)

      if(store.loggedIn===true) {
        sessionStorage.setItem("loggedIn", "true")
      } else {
        sessionStorage.setItem("loggedIn", "false")
      }

      next()
    }
  },
  {
    path: '/winery',
    name: 'winery',
    component: () => import('../components/Winery'),
    beforeEnter: async (to, from, next) => {
      const response = await fetch(store.api_url + "/wineries");
      let wineries = await response.json();
      wineries = JSON.parse(JSON.stringify(wineries))["wineries"];

      const storedWinery = JSON.parse(sessionStorage.getItem("selectedWinery"));
      const winery = wineries.filter(winery => winery.id === storedWinery.id)[0]
      sessionStorage.setItem("selectedWinery", JSON.stringify(winery))

      sessionStorage.setItem("selectedWineryReviews", JSON.stringify(winery.reviews))

      next()
    }
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
    component: () => import('../components/ProfilePage'),
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

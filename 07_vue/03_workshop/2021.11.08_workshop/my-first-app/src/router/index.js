import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import lotto from '../views/lotto.vue'
import lunch from '../views/lunch.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/about',
    name: 'About',
    component: About
  },

  {
    path: '/lotto/:lottonum',
    name: 'lotto',
    component: lotto,
  },

  {
    path: '/lunch/',
    name: 'lunch',
    component: lunch,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

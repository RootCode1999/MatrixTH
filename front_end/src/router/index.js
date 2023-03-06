import Vue from 'vue'
import Router from 'vue-router'
import main from '../components/main.vue'
import home from '../components/home.vue'
import History from '../components/History.vue'
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'
import Setting from '../components/Setting.vue'
import Warning from '../components/Warning.vue'


Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', redirect: '/Login' },
    {
      path: '/main',
      name: 'main',
      component: main,
      children: [
        {
          path: '/main/home',
          name: 'home',
          component: home,
        },
        {
          path: '/main/history',
          name: 'history',
          component: History,
        },
        {
          path:'/main/setting',
          name:'setting',
          component: Setting
        },
        {
          path:'/main/warning',
          name:'warning',
          component: Warning
        }
      ]
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
  ]
})
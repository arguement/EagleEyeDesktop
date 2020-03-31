import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login-page',
      component: require('@/components/LoginPage').default
    },
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/home',
      name: 'home-page',
      component: require('@/components/HomePage').default
    },
    {
      path: '/reports',
      name: 'report-page',
      component: require('@/components/ReportPage').default
    }
  ]
})

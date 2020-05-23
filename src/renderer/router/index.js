import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
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
    },
    {
      path: '/map',
      name: 'map-page',
      component: require('@/components/MapPage').default
    },
    {
      path: '/analytics',
      name: 'analytics-page',
      component: require('@/components/AnalyticsPage').default
    }, 
    {
      path: '/adduser',
      name: 'Adduser-page',
      component: require('@/components/admin/Adduserpage').default 
    }, 
    {
      path:'/modifypriority' ,
      name: 'ModifyPriority' ,
      component: require('@/components/admin/modifypriority').default
    },
    {
      path:'/allusers',
      name: 'Alluserpage',
      component: require('@/components/admin/Alluserpage').default
    },
    {
      path:'/dispatch',
      name: 'dispatch',
      component: require('@/components/sidebarContent/dispatchofficer').default
    },
    {
     path:'/:userinfo_id',
     name:'Userinfo' ,
     component:require('@/components/admin/content/Userinfo').default
    },

  
  ]
})

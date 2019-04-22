// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router/router'
import store from './store'
import axios from 'axios'
import qs from 'qs'

Vue.prototype.$qs = qs
axios.defaults.withCredentials = true
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.baseURL = 'http://127.0.0.1:8000'
Vue.prototype.$axios = axios
// Vue.prototype.$store = store

Vue.use(ElementUI, { size: 'small' })
Vue.config.productionTip = false

// loading框设置局部刷新，且所有请求完成后关闭loading框
let loading
let needLoadingRequestCount = 0 // 声明一个对象用于存储请求个数
function startLoading () {
  loading = Vue.prototype.$loading({
    lock: true,
    text: '努力加载中...',
    background: 'rgba(0,0,0,0.5)',
    target: document.querySelector('.loading-area') // 设置加载动画区域
  })
}
function endLoading () {
  loading.close()
}
function showFullScreenLoading () {
  if (needLoadingRequestCount === 0) {
    startLoading()
  }
  needLoadingRequestCount++
}
function hideFullScreenLoading () {
  if (needLoadingRequestCount <= 0) return
  needLoadingRequestCount--
  if (needLoadingRequestCount === 0) {
    endLoading()
  }
}

let token = localStorage.getItem('Token')
if (token) {
  // 设置vuex状态已登陆
  store.dispatch('setToken', token)
}

// http request 拦截器
axios.interceptors.request.use(
  config => {
    if (config.isLoading !== false) { // 如果配置了isLoading: false，则不显示loading
      showFullScreenLoading()
    }
    if (localStorage.Token) { // 判断token是否存在
      config.headers.Authorization = 'Token ' + localStorage.Token // 将token设置成请求头
    }
    return config
  },
  err => {
    hideFullScreenLoading()
    return Promise.reject(err)
  }
)
// http response 拦截器
axios.interceptors.response.use(
  response => {
    hideFullScreenLoading() // 响应成功关闭loading
    return response
  },
  error => {
    hideFullScreenLoading() // 响应成功关闭loading
    if (error.response) {
      switch (error.response.status) {
        case 401: {
          store.dispatch('setToken', null)
          router.replace({
            path: '/login'
            // query: {redirect: router.currentRoute.fullPath}
          })
        }
      }
    }
    return Promise.reject(error.response.data)
  }
)
router.beforeEach((to, from, next) => {
  let token = localStorage.getItem('Token')
  if (token) {
    let userinfo = store.state.userinfo
    console.log('同步前的userinfo  ', userinfo)
    // 如果已经登陆且没有用户数据，从接口获取数据并存入vuex
    if (userinfo == null || !userinfo.username) {
      axios.get('/user/info').then(res => {
        let userinfo = res.data
        console.log('同步后的userinfo  ', userinfo)
        store.dispatch('setUserinfo', userinfo)
      })
    }
    // 设置vuex状态已登陆
    store.dispatch('setToken', token)
    next()
    // 如果登陆了还要进入注册登录界面，重定向主页
    if (!to.meta.isLogin) {
      next({path: '/home'})
    }
  // 如果登陆标志不存在，就是没登录
  } else {
    // 没登录就把store里的userinfo删了
    store.dispatch('setUserinfo', {})
    // 要进入登陆后界面，给登陆界面
    if (to.meta.isLogin) {
      next({
        path: '/login'
      })
    } else {
      next()
    }
  }
})

// 执行完导航钩子函数，定位滚动条到顶端
router.afterEach(router => {
  // window.scroll(0, 0)
})

/* eslint-disable no-new */
// 创建vue实例开始
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  beforeCreate: function () {
  },
  created: function () {
  },
  beforeMount: function () {
  },
  mounted: function () {
  },
  beforeUpdate: function () {
  },
  updated: function () {
  },
  beforeDestroy: function () {
  },
  destroyed: function () {
  }

})

import Vue from 'vue'
import Router from 'vue-router'
import MyHeader from '../components/common/MyHeader'
import Home from '../components/views/Home'
import Goods from '../components/views/Goods'
import Login from '../components/views/Login'
import Register from '../components/views/Register'
import Publish from '../components/views/Publish'
import Personal from '../components/views/Personal'
import Want from '../components/views/goods/Want'
import GoodsDetail from '../components/views/goods/GoodsDetail'
// import GoodsDetail from '../components/views/goods/GoodsDetail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/home',
      name: 'home',
      components: {
        default: Home,
        header: MyHeader
      },
      meta: { isLogin: false }
    },
    {
      path: '/goods',
      name: 'goods',
      components: {
        default: Goods,
        header: MyHeader
      },
      meta: { isLogin: true },
      children: [
        {
          path: ':id',
          name: 'goodsDetail',
          component: GoodsDetail,
          meta: { isLogin: true }
        },
        {
          path: ':id/want',
          name: 'goodsWant',
          component: Want,
          meta: { isLogin: true }
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      components: {
        default: Login,
        header: MyHeader
      },
      meta: {
        isLogin: false
      }
    },
    {
      path: '/register',
      name: 'register',
      components: {
        default: Register,
        header: MyHeader
      },
      meta: {
        isLogin: false
      }
    },
    {
      path: '/personal',
      name: 'personal',
      components: {
        default: Personal,
        header: MyHeader
      },
      meta: { isLogin: true },
      children: [
        {
          path: 'image',
          name: 'personalImage',
          components: {
            personal: resolve =>
              require(['../components/views/personal/Image.vue'], resolve)
          },
          meta: { isLogin: true }
        },
        {
          path: 'info',
          name: 'personalInfo',
          components: {
            personal: resolve =>
              require(['../components/views/personal/Info.vue'], resolve)
          },
          meta: { isLogin: true }
        },
        {
          path: 'password',
          name: 'personalPassword',
          components: {
            personal: resolve =>
              require(['../components/views/personal/Password.vue'], resolve)
          },
          meta: { isLogin: true }
        },
        {
          path: 'publish',
          name: 'personalPublish',
          components: {
            personal: resolve =>
              require(['../components/views/personal/MyPublish.vue'], resolve)
          },
          meta: { isLogin: true },
          children: [
            {
              path: ':id',
              name: 'personalPublishDetail',
              components: {
                personalDetail: resolve =>
                  require([
                    '../components/views/personal/MyPublishDetail.vue'
                  ], resolve)
              },
              meta: { isLogin: true }
            }
          ]
        },
        {
          path: 'order',
          name: 'personalOrder',
          components: {
            personal: resolve =>
              require(['../components/views/personal/MyOrder.vue'], resolve)
          },
          meta: { isLogin: true },
          children: [
            {
              path: ':id',
              name: 'personalOrderDetail',
              components: {
                personalDetail: resolve =>
                  require([
                    '../components/views/personal/MyOrderDetail.vue'
                  ], resolve)
              },
              meta: { isLogin: true }
            }
          ]
        },
        {
          path: 'collection',
          name: 'personalCollection',
          components: {
            personal: resolve =>
              require([
                '../components/views/personal/MyCollection.vue'
              ], resolve)
          },
          meta: { isLogin: true }
        }
      ]
    },
    {
      path: '/publish',
      name: 'publish',
      components: {
        default: Publish,
        header: MyHeader
      },
      meta: {
        isLogin: true
      }
    }
  ]
})

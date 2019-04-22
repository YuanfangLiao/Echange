<template>
  <div class="header-main">
    <myHeaderTop></myHeaderTop>
    <myHeaderMiddle></myHeaderMiddle>
    <br/>
    <el-menu :default-active="activeIndexHandler" class="el-menu-demo" mode="horizontal" :router="true">
      <el-menu-item :route="{name: 'home'}" index="home">首页</el-menu-item>
      <el-menu-item :route="{name: 'goods'}" index="goods">全部商品</el-menu-item>
      <el-menu-item :route="{name: 'publish'}" index="publish">我要发布</el-menu-item>
      <el-menu-item :route="{name: 'personal'}" index="personal">个人中心</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import myHeaderTop from './header/myHeaderTop'
import myHeaderMiddle from './header/myHeaderMiddle'

export default {
  name: 'MyHeader',
  data () {
    return {
      activeIndex: this.$route.name
      // activeName: 'second'
    }
  },
  computed: {
    activeIndexHandler () {
      // console.log(this.$route.path.split('/')[1])
      // 控制多级路由能匹配到合适的下标上
      return this.$route.path.split('/')[1]
    }
  },
  methods: {
    handleClick (tab, event) {
      console.log(tab, event)
    }
  },
  components: {
    myHeaderTop,
    myHeaderMiddle
  }
}
</script>

<style scoped>
  .el-menu {
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }
  .header-main{
    display: flex;
    flex-direction:column
  }
</style>

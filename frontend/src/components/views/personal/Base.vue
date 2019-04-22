<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
    </el-breadcrumb>
    <h3>Welcome，亲爱的Echange用户 {{ getusername }}</h3>
    <h1><i class="el-icon-loading"></i><i class="el-icon-loading"></i><i class="el-icon-loading"></i></h1>
    <h4>这里是个人中心，点击左侧的菜单栏可以修改您的信息，或者管理你的订单噢</h4>
  </div>
</template>

<script>

export default {
  data () {
    return {

    }
  },
  computed: {
    getusername: function () {
      if (!this.$store.state.userinfo) return ''
      return this.$store.state.userinfo.username
    }
  },
  components: {

  }
}
</script>

<style scoped>
</style>

<template>
  <div class="page">
    <el-container class="main-container">
      <el-aside width="220px">
        <el-menu class="el-menu-vertical"
                 :default-active="this.$route.name"
                 :router="true"
                 @open="handleOpen"
                 @close="handleClose"
                 background-color="#545c64"
                 text-color="#fff"
                 active-text-color="#ffd04b">
          <img :src="getuserpic"
               width="100px"
               height="100px"
               class="user_img"
               @click="goPersonal">
          <p class="personal-name">hello {{ getusername }}</p>
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-info"></i>
              <span>个人信息</span>
            </template>
            <el-menu-item :route="{name: 'personalImage'}"
                          index="personalImage">修改头像</el-menu-item>
            <el-menu-item :route="{name: 'personalInfo'}"
                          index="personalInfo">基本资料</el-menu-item>
            <el-menu-item :route="{name: 'personalPassword'}"
                          index="personalPassword">修改密码</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span slot="title">换物中心</span>
            </template>
            <el-menu-item :route="{name: 'personalPublish'}"
                          index="personalPublish">我的发布</el-menu-item>
            <el-menu-item :route="{name: 'personalOrder'}"
                          index="personalOrder">我的换物</el-menu-item>
            <el-menu-item :route="{name: 'personalCollection'}"
                          index="personalCollection">我的收藏</el-menu-item>
          </el-submenu>
          <el-menu-item index="3"
                        disabled>
            <i class="el-icon-document"></i>
            <span slot="title">导航三</span>
          </el-menu-item>
          <el-menu-item @click="doLogout">
            <i class="el-icon-close"></i>
            <span slot="title">退出登陆</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <myBase v-if="this.$route.name==='personal'"></myBase>
        <router-view name="personal"></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
// 因为是子组件，所以要在本组件创建前创建
import myBase from './personal/Base'
export default {
  data () {
    return {
      // userinfo: this.$store.state.userinfo
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    goPersonal () {
      this.$router.push('/personal')
    },
    doLogout () {
      console.log('登出中')
      this.$confirm('确定要登出吗，亲？', '登出确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        localStorage.removeItem('Token')
        this.$store.dispatch('setToken', null)
        this.$router.push('/login')
        this.myusername = ''
        this.$message({
          type: 'success',
          message: '登出成功！'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消登出'
        })
      })
    }
  },
  mounted () {

  },
  computed: {
    getuserpic: function () {
      if (!this.$store.state.userinfo) return ''
      console.log('picaddress :' + this.$store.state.userinfo)
      return this.$store.state.base_url + this.$store.state.userinfo.picture
    },
    getusername: function () {
      if (!this.$store.state.userinfo) return ''
      return this.$store.state.userinfo.username
    }
  },
  components: {
    myBase
  }
}
</script>

<style scoped>
.main-container {
  height: 800px;
  overflow: auto;
}
.el-menu-vertical {
  min-height: 800px;
}
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  /* line-height: 160px; */
}
.user_img {
  margin-top: 30px;
  margin-left: 60px;
  border-radius: 100px;
}
.user_img:hover {
  cursor: pointer;
}
.personal-name {
  color: rgb(255, 255, 255);
  width: 100%;
  text-align: center;
}
</style>

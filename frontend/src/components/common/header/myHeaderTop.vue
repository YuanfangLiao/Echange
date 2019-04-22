<template>
  <div class="header-top">
    <el-row class="header-row">
      <el-col :span="4">
        <div class="grid-content bg-purple">
          <a style="float:left">欢迎来到青岛大学Echange Site</a>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple-light"></div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple-light"></div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :span="4"
              class="right-box">
        <div class="grid-content bg-purple-light">
          <a @click="goRegister"
             v-show="!islogin">注册&nbsp;|&nbsp;</a>
          <a @click="goLogin"
             v-show="!islogin">登陆</a>
          <a @click="goPersonal"
             v-show="islogin">Welcome {{ myusername }}&nbsp;|&nbsp;</a>
          <a @click="goLogout"
             v-show="islogin">登出</a>
        </div>
      </el-col>
    </el-row>

  </div>
</template>

<script>
export default {
  data () {
    return {
      // myusername: this.$store.state.userinfo.username
      // loginFlag: this.$store.state.token
    }
  },
  mounted () {
    console.log('获取pic基本路径 ', this.$store.state.base_url)
    console.log('获取mount中store中userinfo ', this.$store.state.userinfo)
  },
  name: 'myHeaderTop',
  methods: {
    goPersonal () {

    },
    goLogin () {
      this.$router.push('/login')
    },
    goRegister () {
      this.$router.push('/register')
    },
    goLogout () {
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
  computed: {
    islogin () {
      let token = this.$store.state.token
      if (token) {
        return true
      } else {
        return false
      }
    },
    myusername: {
      get: function () {
      // if (this.$store.state.userinfo.username)
        return localStorage.getItem('username')
      },
      set: function (newValue) {
        console.log(newValue)
      }
    }
  }
}
</script>

<style scoped>
.header-top {
  width: 100%;
  max-width: 100%;
  /* display: flex; */
  /* align-items: center; */
  /* justify-content: flex-end; */
  background-color: #e4e7ed;
  font-size: 0.5em;
  padding: 3px 30px;
  box-sizing: border-box;
  color: #8c939d;
}
.header-row {
  height: 0px;
  margin-bottom: -10px;
  padding-bottom: -10px;
}
.grid-content {
  min-height: 10px;
}
.header-top a {
  cursor: pointer;
}
.right-box {
  display: flex;
  flex-direction:row-reverse
}
</style>

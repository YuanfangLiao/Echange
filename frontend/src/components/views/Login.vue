<template>
  <div class="login-div">
    <h1>登陆EChange</h1>
    <el-form ref="form"
             :model="form"
             label-width="80px"
             :rules="rules">
      <el-form-item label="用户名"
                    prop="username">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码"
                    prop="password">
        <el-input show-password
                  v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary"
                   @click="onSubmit">登陆</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      form: {
        username: '',
        password: ''

      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 5, message: '用户名要在五个字符以上', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onSubmit () {
      let that = this
      this.$refs['form'].validate((valid) => {
        if (valid) {
          // 发起登陆ajax请求
          that.$axios.post('user/login', this.form).then(res => {
            let code = res.data.code
            let flag = res.data.flag
            console.log(code, flag)
            if (code === 200 && flag === 'success') {
              // 通过django rest framework的tokenapi接口获得token数据
              that.$axios.post('/api-token-auth', this.form).then(res => {
                let token = res.data.token
                // 登陆成功
                // this.$store.dispatch('setUser', true)
                this.$store.dispatch('setToken', token)
                // 存到localStorage里面保持登陆
                // localStorage.setItem('Flag', 'isLogin')
                localStorage.setItem('Token', token)
                localStorage.setItem('username', this.form.username)
                this.$notify({
                  title: '登录成功',
                  message: '欢迎你,恭喜你登陆成功,尊敬的用户' + that.form.username,
                  type: 'success'
                })
                that.$router.push('/home')
              }).catch(err => {
                that.$message.error(err)
                // alert(err)
              })
            } else {
              that.$message.error('登陆不成功，密码错误')
              localStorage.removeItem('Token')
            }
          }).catch(err => {
            that.$message.error(err)
            // console.log(err)
          })
        } else {
          that.$message.error('submit not valid')
          return false
        }
      })
    },
    resetForm () {
      this.$refs['form'].resetFields()
    }
  }
}
</script>

<style scoped>
.login-div {
  width: 30em;
  margin: 0 auto;
}
.login-div h1 {
  width: 100%;
  text-align: center;
}
</style>

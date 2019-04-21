<template>
  <div class="login-div">
    <h1>注册EChange会员</h1>
    <el-form ref="form" :model="form" label-width="80px" :rules="rules">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="passwd">
        <el-input show-password v-model="form.passwd"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="confpasswd">
        <el-input show-password v-model="form.confpasswd"></el-input>
      </el-form-item>
      <el-form-item label="手机号" prop="phone">
        <el-input v-model="form.phone"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-radio-group v-model="form.sex">
          <el-radio label="1">男</el-radio>
          <el-radio label="2">女</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即注册</el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      form: {
        username: '',
        passwd: '',
        confpasswd: '',
        phone: '',
        email: '',
        sex: ''
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 5, message: '用户名要在五个字符以上', trigger: 'blur' }
        ],
        passwd: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        confpasswd: [
          { required: true, message: '请输入确认密码', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' }
        ],
        sex: [
          { required: true, message: '请选择性别', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onSubmit () {
      let that = this
      this.$refs['form'].validate((valid) => {
        if (valid) {
          that.$axios.request({
            url: '/user/register',
            method: 'post',
            data: this.form
          }).then(data => {
            let code = data.data['code']
            if (code === 200) {
              this.$notify({
                title: '注册成功',
                message: '恭喜你注册成功,成为小站的用户，去登陆吧',
                type: 'success'
              })
              this.$router.push('/login')
            } else {
              that.$message.error('注册失败，代码:' + code + ' 错误信息:' + data.data['error'])
              // alert('注册失败，代码:' + code + '错误信息:' + data.data['error'])
            }
          })
        } else {
          that.$message.error('submit not valid')
          console.log('submit not valid')
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
.login-div{
  width: 30em;
  margin: 0 auto;
}
.login-div h1{
  width: 100%;
  text-align: center;
}
</style>

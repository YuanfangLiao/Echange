<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
      <el-breadcrumb-item>个人信息</el-breadcrumb-item>
      <el-breadcrumb-item>修改密码</el-breadcrumb-item>
    </el-breadcrumb>
    <h3 class="start"><i class="el-icon-warning"></i>&nbsp;要改密码吗，亲？</h3>
    <el-form ref="form"
             :model="form"
             label-width="80px"
             class="form"
             :rules="rules">
      <el-form-item label="旧密码"
                    prop="old_passwd">
        <el-input show-password
                  v-model="form.old_passwd"></el-input>
      </el-form-item>
      <el-form-item label="新密码"
                    prop="new_passwd">
        <el-input show-password
                  v-model="form.new_passwd"></el-input>
      </el-form-item>
      <el-form-item label="重复密码"
                    prop="conf_passwd">
        <el-input show-password
                  v-model="form.conf_passwd"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary"
                   @click="onSubmit">修改</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        old_passwd: '',
        new_passwd: '',
        conf_passwd: ''
      },
      rules: {
        old_passwd: [
          { required: true, message: '请输入旧密码', trigger: 'blur' }
        ],
        new_passwd: [
          { required: true, message: '请输入新密码', trigger: 'blur' },
          { min: 5, message: '密码要在五个字符以上', trigger: 'blur' }
        ],
        conf_passwd: [
          { required: true, message: '请确认密码', trigger: 'blur' },
          { min: 5, message: '密码要在五个字符以上', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onSubmit () {
      let that = this
      this.$confirm('确定修改吗，亲？', '登出确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$refs['form'].validate((valid) => {
          if (valid) {
            that.$axios.post('/user/change_pass', that.form).then(res => {
              if (res.data.flag === 'success') {
                that.$message.success('修改成功')
                localStorage.removeItem('Token')
                this.$store.dispatch('setToken', null)
                this.$router.push('/login')
                this.myusername = ''
                this.$message({
                  type: 'success',
                  message: '修改密码成功！请重新登陆'
                })
              } else {
                that.$message.warning('修改失败,' + res.data.msg)
              }
            }).catch(err => {
              that.$message.error('修改失败')
              console.log(err)
            })
          } else {
            that.$message.error('submit not valid')
            return false
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消修改'
        })
      })
    }
  },
  components: {

  }
}
</script>

<style scoped>
.form {
  width: 500px;
  margin: 0 auto;
  text-align: left;
}
.start{
  margin-top: 150px
}
</style>
